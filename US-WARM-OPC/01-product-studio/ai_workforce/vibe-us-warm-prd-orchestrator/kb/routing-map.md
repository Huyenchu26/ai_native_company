# Routing Map — vibe-us-warm-prd-orchestrator

**Date:** 2026-08-17 · Bảng route SOP → worker + hard gate. Orchestrator route, KHÔNG execute.

## 1. SOP → Worker → Gate
| SOP | Process | Route tới worker | Input | Output artifact | Gate trước khi qua bước sau |
|-----|---------|------------------|-------|-----------------|------------------------------|
| PRD-001 | Gift niche research + scoring | `vibe-us-warm-prd-niche-research` | occasion calendar, demand signals, unit-economics | `validated_niches[]` | demand_score ≥ 70 ∧ margin-fit ≥ 15% @ CPA ∧ ip_preflag ≠ HIGH ∧ confidence ≥ 0.7 |
| PRD-002 | Blanket personalization design | `vibe-us-warm-prd-design` | validated niche, personalization fields, supplier spec | `designs[]` (design-spec) | DPI ≥ min (no upscale) ∧ safe-area 100% ∧ GSM ≥ ngưỡng ∧ IP=CLEAR |
| PRD-003 | IP/TM clearance US | `vibe-us-warm-prd-design` (pre-check) → `vibe-us-warm-bck-compliance` (sign-off) | design phrase/artwork, photo policy | `ip_status` + `clearance_id` | USPTO checked trước CLEAR ∧ licensed-char = 0 ∧ có `clearance_id` |
| Handoff | Đóng gói bàn giao | `vibe-us-warm-mer-orchestrator` (downstream) | `cleared_for_handoff[]` | `pipeline-plan.json` | design_status=CLEAR ∧ clearance_id present |

## 2. Enum clearance (⚠️ khớp y hệt prd-design — tránh bug PASS≠CLEAR của EU)
| Field | Enum | Ràng buộc |
|-------|------|-----------|
| `designs[].design_status` | `CLEAR / MODIFY / REJECT / PENDING` | output prd-design (SOP-PRD-002 §5) |
| `designs[].ip_status` | `CLEAR / MODIFY / REJECT / PENDING` | output prd-design (SOP-PRD-003 §2); PENDING = fail-closed |
| `gate_checks.ip_clearance` | `CLEAR / MODIFY / REJECT / PENDING` | gate tổng hợp |
| `cleared_for_handoff[].clearance_status` | `CLEAR` (chỉ 1 giá trị) | vào list ⇒ đã qua gate |

**KHÔNG dùng `PASS`.** Pipeline EU gãy vì orchestrator chờ `CLEAR` còn design xuất `PASS`
(enum-mismatch). US chuẩn hoá đồng nhất `CLEAR` xuyên suốt design → orchestrator → handoff.

## 3. Hard gate (schema allOf/if-then — enforce bởi validator đã sửa)
| Gate | Điều kiện | Fail action |
|------|-----------|-------------|
| G1 no-upscale | ảnh khách ≥ min DPI @ print size | REJECT + re-source (KHÔNG upscale) |
| G2 material-spec | GSM ≥ ngưỡng brand-promise | block, đổi vải (KHÔNG hạ ngưỡng) |
| G3 USPTO-before-CLEAR | `uspto_checked=true` trước khi `ip_status=CLEAR` | `ip_status=PENDING` |
| G4 no-handoff-without-clearance_id | item `cleared_for_handoff` ⇒ `design_status=CLEAR` ∧ `clearance_id` present | không đưa vào handoff |
| G5 conservative confidence | `confidence_score < 0.7` ⇒ `need_review=true` | đẩy human-review |
| G6 batch-gate | có handoff item ⇒ `gate_checks.ip_clearance = CLEAR` | chặn handoff cả batch |

G4 + G6 code hoá trong [`../schema/pipeline-plan.schema.json`](../schema/pipeline-plan.schema.json)
(item-level `if clearance_status=CLEAR then design_status=CLEAR + require clearance_id`, và
top-level `if cleared_for_handoff minItems 1 then ip_clearance=CLEAR`).

## 4. Escalation (HITL)
| Tình huống | Route |
|-----------|-------|
| IP HIGH / uncertain | Owner |
| Material dưới ngưỡng (không có vải đạt) | Owner + merchandising |
| Niche mới không benchmark | Owner (watchlist → validated) |
| Thiếu tool (Trends/AdSpy/Meta) | đánh dấu estimate + hạ confidence + `need_review` |

## 5. Validate output
```bash
python3 ../../../../_shared/script/validator.py --run-all \
  --artifact ../synthetic-data/sample-pipeline-plan.json \
  --schema ../schema/pipeline-plan.schema.json --threshold 0.7
```

## 6. Links (resolve từ kb/)
- SOP-PRD-001: [research-niche](../../../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md)
- SOP-PRD-002: [design-personalization](../../../design-personalization/template/sop_prd-002_blanket-personalization-design_v1.0_2026-08-04.md)
- SOP-PRD-003: [clear-ip](../../../clear-ip/template/sop_prd-003_ip-tm-clearance-us_v1.0_2026-08-04.md)
- Rules/gates: [_rules](../../../_rules/README.md) · Workflow: [_workflow](../../../_workflow/README.md) · Roster: [_skills-agents](../../../_skills-agents/README.md)
- Validator: [_shared/script/validator.py](../../../../_shared/script/validator.py) · Evidence: [_shared/schema/evidence.schema.json](../../../../_shared/schema/evidence.schema.json)
- Artifact schema: [pipeline-plan.schema.json](../schema/pipeline-plan.schema.json) · SKILL: [../SKILL.md](../SKILL.md)
