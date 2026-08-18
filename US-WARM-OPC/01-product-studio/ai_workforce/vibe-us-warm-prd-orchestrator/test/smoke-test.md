# Smoke Test — vibe-us-warm-prd-orchestrator

Chạy từ thư mục skill (`.../vibe-us-warm-prd-orchestrator/`).

## T1 — skill.json hợp lệ (khớp skill-meta shared)
```bash
python3 ../../../_shared/script/validator.py \
  --artifact skill.json \
  --schema ../../../_shared/schema/skill-meta.schema.json
```
**Kỳ vọng:** `{"ok": true, "errors": []}`.

## T2 — pipeline-plan HỢP LỆ + --run-all (schema + evidence + confidence gate)
```bash
python3 ../../../_shared/script/validator.py --run-all \
  --artifact synthetic-data/sample-pipeline-plan.json \
  --schema schema/pipeline-plan.schema.json \
  --threshold 0.7
```
**Kỳ vọng:** `"ok": true`, `schema.ok=true`, `evidence.missing=[]`, `confidence.passes=true`.

## T3 — GATE enforce: PENDING design trong cleared_for_handoff PHẢI FAIL
```bash
python3 ../../../_shared/script/validator.py --run-all \
  --artifact synthetic-data/invalid-gate-pipeline-plan.json \
  --schema schema/pipeline-plan.schema.json \
  --threshold 0.7 ; echo "exit=$?"
```
**Kỳ vọng:** `"ok": false`, schema error tại `cleared_for_handoff/0/design_status`
(const CLEAR), `exit=1`.

## T4 — preflight chặn edit template/
```bash
python3 ../../../_shared/script/validator.py \
  --preflight-target ../../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md ; echo "exit=$?"
```
**Kỳ vọng:** `{"ok": false, "reason": "template/ is READ-ONLY..."}`, `exit=1`.
