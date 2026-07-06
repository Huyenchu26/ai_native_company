# AI Workforce — 02 Merchandising (DAKOfits)

## Status: 🟢 Activated (2026-06-23)

> Build bởi vibe-aiworkforce (Phase 6.1). Mỗi skill đủ 8 components, bám SOP state machine. PRIMARY tại đây; copy ở `~/.claude/skills/`.

## Skills

| # | Skill | Role | SOP source | 8-comp | Installed |
|---|-------|------|-----------|:------:|:---------:|
| 0 | vibe-eu-opc-mer-orchestrator | Manager — điều phối + promote theo đợt | điều phối MER-* + MER-006 | ✅ | ✅ |
| 1 | vibe-eu-opc-mer-catalog | Setup Printify + pricing + sync QC | SOP-MER-002, 003, 004 | ✅ | ✅ |
| 2 | vibe-eu-opc-mer-product-page | Product page copy + GPSR label | SOP-MER-001 | ✅ | ✅ |

## SOP → Skill Coverage (Gate)

| SOP | Tên | Responsible skill |
|-----|-----|-------------------|
| SOP-MER-001 | Product page copy + upsell | vibe-eu-opc-mer-product-page |
| SOP-MER-002 | Printify/PrintBase setup | vibe-eu-opc-mer-catalog |
| SOP-MER-003 | Variant & pricing | vibe-eu-opc-mer-catalog |
| SOP-MER-004 | Catalog sync & QC | vibe-eu-opc-mer-catalog |
| SOP-MER-006 | Promote theo đợt (batch) | vibe-eu-opc-mer-orchestrator |

**Coverage: 5/5 SOP = 100%** ✅

## Gate cứng enforce
- **No GPSR clearance → no publish** (đơn EU): product-page verify clearance log ID (PASS) fail-closed; catalog pre-sync GPSR check.
- **Pricing floor trên CONTRIBUTION MARGIN** (sau ad+fee+VAT, không margin ảo) — catalog + [unit-economics](../../_shared/unit-economics.md).
- **EU tính giá NET-of-VAT** → nâng giá EU €59–69 (BE-ROAS EU ~5.3).
- Winner theo break-even ROAS per-SKU.

## Handoff
Promote theo đợt (MER-006): orchestrator gom 5–10 SP → catalog (setup+pricing) → product-page (copy+GPSR) → **bàn giao `vibe-eu-opc-grw-orchestrator`** chạy ads → đọc ROAS → scale winner/cut loser.

## Cách gọi
- `/vibe-eu-opc-mer-orchestrator` ("lên lô 8 SP design mới đã clear")
- `/vibe-eu-opc-mer-catalog` ("setup + đặt giá SP Husky US/EU")
- `/vibe-eu-opc-mer-product-page` ("viết product page cho SP Corgi EU")
