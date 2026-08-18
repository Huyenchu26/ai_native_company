# _rules — 04 Fulfillment-CX (DAKOfits US)
**Date:** 2026-08-04 · What AI MUST NOT do. (Hiện thực hoá 3 lời hứa thương hiệu.)

## Non-negotiables (error budget = 0)
1. **No fake tracking** — chỉ set tracking_sent=true khi có carrier_code THẬT verified. TUYỆT ĐỐI không mã giả (đối thủ bị tố tracking giả).
2. **No ship under-QC** — material_gsm < 260 / QC photo fail / sai personalization → HOLD, không ship (chống "chăn mỏng").
3. **No empty auto-reply** — CX phải thật, không template rỗng; escalate người khi cần.
4. **Defect luôn được refund/replace** — personalized = final-sale CHỈ cho "đổi ý", KHÔNG né nghĩa vụ defect/not-as-described (US law).
5. **Refund > $30 → human** — không auto-refund lớn.

## Decision authority
| Quyết định | Auto? | Authority |
|-----------|-------|-----------|
| Ship approve | QC pass | ful-order-ops |
| Tracking notify | carrier thật | ful-order-ops |
| Refund ≤ $30 defect | ✅ | ful-cx |
| Refund > $30 / defect dispute | ❌ | Owner |
| Final-sale "đổi ý" | ✅ | ful-cx |

## Quality Standards
| SOP | SLI | SLO |
|-----|-----|-----|
| FUL-001 | QC material_gsm | ≥ 260 |
| FUL-001 | Fake tracking | 0 |
| FUL-001 | Tracking sent | ≤ 24h |
| FUL-002 | Route on-time | ≤ 18h |
| FUL-003 | First response | ≤ 4h |
| FUL-004 | Defect refund honored | 100% |

## Harness: `_shared/script/validator.py --run-all`.
