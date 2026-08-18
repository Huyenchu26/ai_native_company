# AI Workforce — 01 Product Studio (DAKOfits US)

**Date:** 2026-08-04 · 3 worker (1 orchestrator + 2 specialist). Namespace `vibe-us-warm-prd-*`.

| Worker | Role | SOP | Schema chính |
|--------|------|-----|--------------|
| `vibe-us-warm-prd-orchestrator` | Manager (route, không execute) | PRD-001/002/003 | pipeline-plan |
| `vibe-us-warm-prd-niche-research` | Gift niche research + scoring | PRD-001 | niche-validation |
| `vibe-us-warm-prd-design` | Blanket personalization design + IP pre-check | PRD-002/003 | design-spec, ip-clearance |

## Coverage: 3/3 SOP. Harness: dùng chung `_shared/script/validator.py` (đã fix if/then + evidence).

## Handoff chain
niche-research (validated) → design (design_status=CLEAR ∧ ip=CLEAR + clearance_id) → orchestrator (pipeline-plan) → **02-merchandising**.

## Enum thống nhất (fix bug EU)
design_status / ip_status / clearance = `CLEAR / MODIFY / REJECT / PENDING` — KHỚP giữa design ↔ orchestrator (không lặp bug PASS≠CLEAR). Output design thật validate được trực tiếp như item của orchestrator.

## Verified (2026-08-04)
skill.json valid 3/3 · gate if/then enforce (test vi phạm → FAIL) · evidence `--run-all` chạy · 0 link gãy · 0 residue legacy/PASS.
