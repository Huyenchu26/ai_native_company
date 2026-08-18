# _workflow — 01 Product Studio (DAKOfits US)

**Date:** 2026-08-04 · HOW work flows. SOP index + state machine + dependencies.

## SOP Index
| SOP | Process | Template | AI Worker | Freq |
|-----|---------|----------|-----------|------|
| PRD-001 | Gift niche research | [research-niche](../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md) | prd-niche-research | per batch/seasonal |
| PRD-002 | Blanket personalization design | [design-personalization](../design-personalization/template/sop_prd-002_blanket-personalization-design_v1.0_2026-08-04.md) | prd-design | per validated niche |
| PRD-003 | IP/TM clearance US | [clear-ip](../clear-ip/template/sop_prd-003_ip-tm-clearance-us_v1.0_2026-08-04.md) | prd-design → bck-compliance | per design |

## State machine (mỗi SOP)
`template/ (READ-ONLY) → input/ → processing/{ai-draft,human-review} → output/ → archive/[YYYY-MM]/`

## Dependency map
```
PRD-001 (validated niche) ──▶ PRD-002 (design) ──▶ [handoff 02-merchandising]
                               │
                               ▼
                          PRD-003 (IP clearance) ──▶ clearance_id (bck-compliance) ──▶ gate handoff
```
Handoff design→merch CHỈ khi design_status=CLEAR ∧ có clearance_id.

## Coverage: 3/3 SOP indexed.
