# AI Workforce — 05 Backoffice (DAKOfits)

## Status: 🟢 Activated (2026-06-23)

> Build bởi vibe-aiworkforce (Phase 6.1). 8 components, bám SOP state machine. Layer 3 Support — hỗ trợ toàn bộ L2. PRIMARY tại đây; copy ở `~/.claude/skills/`.

## Skills

| # | Skill | Role | SOP source | 8-comp | Installed |
|---|-------|------|-----------|:------:|:---------:|
| 0 | vibe-eu-opc-bck-orchestrator | Manager — điều phối + CEO brief | điều phối BCK-* | ✅ | ✅ |
| 1 | vibe-eu-opc-bck-finance | Bookkeeping + profit/ROAS + VAT + P&L | SOP-BCK-001, 002, 003 | ✅ | ✅ |
| 2 | vibe-eu-opc-bck-compliance | GPSR clearance issuer + GDPR + Meta policy | SOP-BCK-004, 005 | ✅ | ✅ |
| 3 | vibe-eu-opc-bck-ops-hr | Quản AI Workforce (uptime/cost/quality) | SOP-BCK-006 | ✅ | ✅ |

**Coverage: 6/6 SOP = 100%** ✅

## Gate cứng (compliance SLO = 100%, error budget 0% — legal)
- **No GPSR → no publish** (đơn EU): compliance cấp clearance log ID PASS/FAIL → Merch verify.
- **No Meta Ad Policy → no ads**: compliance pre-check → Growth.
- **GDPR breach ≤72h** (từ "become aware"); DSAR ≤1 tháng.
- **VAT on-time 100%** (OSS quý / IOSS ≤€150 tháng).

## Vai trò đặc biệt — Compliance là GATE issuer toàn công ty
`vibe-eu-opc-bck-compliance` cấp **clearance log ID** mà các skill khác verify:
- Merch (product-page/catalog) verify clearance trước publish.
- Growth verify Meta Ad Policy trước ads.
- Finance dùng economics chuẩn ([unit-economics](../../_shared/unit-economics.md)).

## Cách gọi
- `/vibe-eu-opc-bck-orchestrator` ("chốt CEO brief tháng")
- `/vibe-eu-opc-bck-finance` ("tính profit-per-SKU + P&L kỳ này")
- `/vibe-eu-opc-bck-compliance` ("cấp GPSR clearance lô SP EU mới")
- `/vibe-eu-opc-bck-ops-hr` ("weekly report sức khỏe AI workforce")
