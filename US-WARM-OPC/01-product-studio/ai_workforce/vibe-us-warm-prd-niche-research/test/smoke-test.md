# Smoke Test — vibe-us-warm-prd-niche-research

Run all commands from the **skill root** (`.../ai_workforce/vibe-us-warm-prd-niche-research/`).
`V=../../../_shared/script/validator.py` (3-up from skill root = repo `_shared/`; 4-up would over-shoot to `ai_native_company/` — do not off-by-one).

## Step 1 — skill.json validates against skill-meta schema
```
python3 ../../../_shared/script/validator.py \
  --artifact skill.json \
  --schema ../../../_shared/schema/skill-meta.schema.json
```
**Expect:** `{"ok": true, "errors": []}` (exit 0). name matches `^vibe-us-warm-(prd|mer|grw|ful|bck)-[a-z-]+$`, sop_coverage=["PRD-001"], downstream=["vibe-us-warm-prd-design"].

## Step 2 — valid niche output passes full run (schema + evidence + confidence gate)
```
python3 ../../../_shared/script/validator.py --run-all \
  --artifact synthetic-data/sample-niche-output.json \
  --schema schema/niche-validation.schema.json --threshold 0.7
```
**Expect:** `"ok": true`; `evidence.verified` = 4, `evidence.missing` = []; `adjusted_confidence` = 0.8 ≥ 0.7. Proves the unified evidence contract resolves real files and quotes match verbatim.

## Step 3 — GATE enforcement (negative): validated + demand_score 50 MUST fail
```
python3 ../../../_shared/script/validator.py --run-all \
  --artifact synthetic-data/sample-niche-violation.json \
  --schema schema/niche-validation.schema.json --threshold 0.7
```
**Expect:** `"ok": false`, exit 1; schema error on `demand_score` (`minimum` 70 under the `decision=validated` if-then branch). Proves the allOf/if-then gate is actually enforced by Draft7Validator (not silently ignored like the old EU validator).

## Step 4 — FAIL-CLOSED (estimate/no-tool): watchlist artifact must NOT auto-validate
Create `test/tmp-estimate.json` from the estimate skeleton in `prompt/score-niche-prompt.md` (decision=watchlist, confidence 0.55, need_review true), then:
```
python3 ../../../_shared/script/validator.py --run-all \
  --artifact test/tmp-estimate.json \
  --schema schema/niche-validation.schema.json --threshold 0.7
```
**Expect:** `"ok": false` on the confidence gate (0.55 < 0.7) — the artifact is correctly held for review, never auto-validated. (Schema itself is valid because `decision` is `watchlist`, not `validated`, so the validated-branch does not trigger; only the threshold blocks it. This is the intended fail-closed behavior.)

## Step 5 — evidence tamper detection
Copy `sample-niche-output.json`, change one `verbatim_quote` to text NOT in its source, re-run Step 2 command on the copy.
**Expect:** `evidence.missing` lists the tampered entry, `confidence_adjustment` = −0.2, `adjusted_confidence` = 0.6 < 0.7 → `"ok": false`. Proves quotes are re-verified against real files.

## Pass criteria
Steps 1, 2 → ok:true. Steps 3, 4, 5 → ok:false for the stated reason. Any deviation = harness/schema regression.
