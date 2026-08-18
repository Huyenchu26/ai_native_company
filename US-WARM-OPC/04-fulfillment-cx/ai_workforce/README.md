# AI Workforce — 04 Fulfillment-CX (DAKOfits US)
**Date:** 2026-08-04 · 3 worker. Namespace `vibe-us-warm-ful-*`. **Phòng hiện thực hoá 3 lời hứa thương hiệu.**

| Worker | Role | SOP | Schema |
|--------|------|-----|--------|
| `vibe-us-warm-ful-orchestrator` | Manager | FUL-001..004 | fulfillment-plan |
| `vibe-us-warm-ful-order-ops` | Monitor+route+QC+tracking | FUL-001/002 | order-status |
| `vibe-us-warm-ful-cx` | Support + returns | FUL-003/004 | ticket-resolution |

## Coverage 4/4. Handoff: [03 growth] → orders → QC/ship → CX → [05 backoffice].
## Gate khác biệt hoá (verified — đối thủ customwarms yếu đúng 3 chỗ này):
- **Chất lượng thật:** ship ⇒ gsm≥260 + QC photo (chăn <260 → FAIL).
- **Tracking thật:** tracking_sent ⇒ carrier thật verified (no carrier → FAIL).
- **CX thật:** first-response ≤4h; refund>$30→human; defect luôn refundable; final-sale chỉ "đổi ý".
