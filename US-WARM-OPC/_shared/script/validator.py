#!/usr/bin/env python3
"""US-WARM-OPC shared validator — harness v2 (fixes 5 bugs found in EU pipeline test).

Fixes vs EU validator:
  P1: uses jsonschema.Draft7Validator → ENFORCES allOf/if/then/anyOf/oneOf
      (EU validator hand-rolled type/enum only and silently ignored conditional gates).
  P2: ONE unified evidence contract for the whole company (see EVIDENCE_SHAPE).
      verify_evidence matches the schema, so --run-all works for every skill.
  P3: schemas are expected to model fail-closed states (PENDING/blocked/validation) —
      this validator does not force a happy-path.
  P4: --run-all reads a per-gate min_confidence (via --threshold or gate arg) and enforces it.
  P5: optional --prose-scan runs a deceptive-content lexical check (fake-tracking / fake-review /
      unverified-™ / engagement-bait) for content artifacts.

Unified evidence contract (P2) — every artifact's `evidence` is an array of objects:
  {"claim": str, "verbatim_quote": str, "source": str(filepath), "location": str?}
  → verbatim_quote MUST appear verbatim in the file at `source`. Missing/unverifiable → -0.2 each.
"""
from __future__ import annotations
import argparse, json, sys, re
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    print(json.dumps({"ok": False, "errors": ["jsonschema not installed: pip install jsonschema"]}))
    sys.exit(2)

EVIDENCE_SHAPE = "array<{claim, verbatim_quote, source(filepath), location?}>"

# ---- P1: full draft-07 schema validation (enforces allOf/if/then) ----
def validate_schema(instance: dict, schema: dict) -> dict:
    errors = sorted(Draft7Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    return {
        "ok": not errors,
        "errors": [f"{'/'.join(map(str, e.path)) or '$'}: {e.message}" for e in errors],
    }

# ---- P2: unified evidence verification ----
def verify_evidence(evidence, base_dir: Path) -> dict:
    verified, missing = 0, []
    for i, ev in enumerate(evidence or []):
        if not isinstance(ev, dict):
            missing.append(f"evidence[{i}]: not an object (expected {EVIDENCE_SHAPE})"); continue
        quote = (ev.get("verbatim_quote") or "").strip()
        source = ev.get("source") or ""
        if not quote or not source:
            missing.append(f"evidence[{i}]: missing verbatim_quote/source"); continue
        p = Path(source)
        if not p.is_absolute():
            p = base_dir / source
        if not p.exists():
            missing.append(f"evidence[{i}]: source not found ({source})"); continue
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            missing.append(f"evidence[{i}]: unreadable source ({e})"); continue
        if quote in content:
            verified += 1
        else:
            missing.append(f"evidence[{i}]: quote not found verbatim in {source}")
    return {"verified": verified, "missing": missing, "confidence_adjustment": -0.2 * len(missing)}

# ---- P4: confidence gate ----
def check_confidence(score, threshold: float) -> dict:
    if score is None:
        return {"passes": False, "score": None, "reason": "confidence_score missing"}
    return {"passes": score >= threshold, "score": score, "threshold": threshold}

# ---- P5: deceptive-content prose scan ----
PROSE_PATTERNS = {
    "fake_tracking": r"\b(fake|placeholder|dummy)\s+tracking\b",
    "engagement_bait": r"\b(tag your|comment below|drop a\s+\S+|like if|share to unlock|dm us and we'?ll)\b",
    "unverified_tm": r"\b\w+™",
    "fake_review": r"\b(5[- ]star|verified)\s+review\b",
    "deceptive_claim": r"\b(guaranteed|100%|best in the world|clinically proven)\b",
}
def prose_scan(text: str) -> dict:
    hits = {}
    for name, pat in PROSE_PATTERNS.items():
        m = re.findall(pat, text, flags=re.IGNORECASE)
        if m:
            hits[name] = list({x if isinstance(x, str) else x[0] for x in m})[:5]
    return {"ok": not hits, "hits": hits}

# ---- preflight (hooks): block edits to template/ and archive/ ----
def preflight(target: str) -> dict:
    t = target.replace("\\", "/")
    if "/template/" in t:
        return {"ok": False, "reason": "template/ is READ-ONLY (copy to input/ first)"}
    if "/archive/" in t:
        return {"ok": False, "reason": "archive/ is immutable"}
    return {"ok": True}

def run_all(artifact_path, schema_path, threshold, prose):
    art = Path(artifact_path)
    data = json.loads(art.read_text(encoding="utf-8"))
    base_dir = art.parent
    result = {"artifact": str(art)}
    schema_res = validate_schema(data, json.loads(Path(schema_path).read_text())) if schema_path else {"ok": True, "errors": []}
    ev_res = verify_evidence(data.get("evidence", []), base_dir)
    base_conf = data.get("confidence_score", 0.0)
    adj_conf = max(0.0, base_conf + ev_res["confidence_adjustment"])
    conf_res = check_confidence(adj_conf, threshold)
    result.update({"schema": schema_res, "evidence": ev_res,
                   "adjusted_confidence": adj_conf, "confidence": conf_res})
    if prose:
        # scan string fields for deceptive content
        blob = json.dumps(data, ensure_ascii=False)
        result["prose"] = prose_scan(blob)
    ok = schema_res["ok"] and conf_res["passes"] and (result.get("prose", {"ok": True})["ok"])
    result["ok"] = ok
    return result

def main():
    ap = argparse.ArgumentParser(description="US-WARM-OPC shared validator (harness v2)")
    ap.add_argument("--artifact"); ap.add_argument("--schema")
    ap.add_argument("--threshold", type=float, default=0.7)
    ap.add_argument("--run-all", action="store_true")
    ap.add_argument("--prose", action="store_true", help="run P5 deceptive-content scan")
    ap.add_argument("--preflight-target")
    args = ap.parse_args()

    if args.preflight_target:
        r = preflight(args.preflight_target)
        print(json.dumps(r, ensure_ascii=False)); sys.exit(0 if r["ok"] else 1)
    if args.run_all:
        r = run_all(args.artifact, args.schema, args.threshold, args.prose)
    elif args.artifact and args.schema:
        r = validate_schema(json.loads(Path(args.artifact).read_text()), json.loads(Path(args.schema).read_text()))
    else:
        ap.error("need --artifact+--schema, --run-all, or --preflight-target")
    print(json.dumps(r, ensure_ascii=False, indent=2))
    sys.exit(0 if r.get("ok") else 1)

if __name__ == "__main__":
    main()
