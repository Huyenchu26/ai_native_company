# AI Workforce — 04 Fulfillment & CX (DAKOfits)

## Status: 🟢 Activated (2026-06-23)

> Build bởi vibe-aiworkforce (Phase 6.1). 8 components, bám SOP state machine. PRIMARY tại đây; copy ở `~/.claude/skills/`.

## Skills

| # | Skill | Role | SOP source | 8-comp | Installed |
|---|-------|------|-----------|:------:|:---------:|
| 0 | vibe-eu-opc-ful-orchestrator | Manager — điều phối đơn + ticket | điều phối FUL-* | ✅ | ✅ |
| 1 | vibe-eu-opc-ful-order-ops | Monitor + route Printify ≤24h + tracking | SOP-FUL-001, 002 | ✅ | ✅ |
| 2 | vibe-eu-opc-ful-cx | Support EN + returns/refund/exchange | SOP-FUL-003, 004 | ✅ | ✅ |

**Coverage: 4/4 SOP = 100%** ✅

## Gate cứng enforce
- Route Printify **≤24h** (SLO nội bộ 18h), tracking ≤6h sau ship — order-ops.
- Refund AI tự duyệt **≤$30**, >$30 escalate OPC — cx (schema ép `refund>30 → auto=false`).
- EU 14-day withdrawal: AOP custom miễn trừ Art.16(c) nhưng vẫn refund khi defect.
- GDPR DSAR SLO ≤20 ngày; data minimization khi gửi Printify (DPA).

## Cách gọi
- `/vibe-eu-opc-ful-orchestrator` ("điều phối lô đơn + ticket hôm nay")
- `/vibe-eu-opc-ful-order-ops` ("route đơn mới + gửi tracking")
- `/vibe-eu-opc-ful-cx` ("xử lý ticket hàng lỗi + đổi size")

Upstream: đơn từ Growth. Downstream: cost/refund data → 05-backoffice.
