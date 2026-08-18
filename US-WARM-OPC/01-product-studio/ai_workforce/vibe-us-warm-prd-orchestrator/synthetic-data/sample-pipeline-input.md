# Sample Pipeline Input — orchestrator batch

**Batch:** PRD-PIPE-2026-08-17-batch01 · **Market:** US · **Product:** chăn fleece/sherpa cá nhân hoá.

## Yêu cầu
"Chuẩn bị lô chăn cá nhân hoá mới cho mùa Christmas + Memorial (pet). Chạy full pipeline:
niche-research → design → IP clearance → bàn giao Merchandising."

## Niche seed
| Seed | Occasion | Relationship / recipient |
|------|----------|--------------------------|
| "to my daughter christmas blanket" | Christmas | to my daughter |
| "pet memorial blanket" | memorial | pet (dog) |

## Ràng buộc
- Chăn $49.95–59.95; contribution floor ≥ 15% @ CPA mục tiêu.
- design_deadline ≥ 6 tuần trước peak Christmas.
- IP: pet-memorial ảnh khách → cần photo consent; tránh licensed character / celebrity.

## Kỳ vọng orchestrator
Route đúng specialist, enforce gate, xuất `pipeline-plan.json`. Chỉ design
`design_status=CLEAR` ∧ có `clearance_id` mới vào `cleared_for_handoff[]`. Enum
clearance `CLEAR/MODIFY/REJECT/PENDING` (KHÔNG `PASS`).
