# DAKOfits — AI Workforce Overview

**Phiên bản:** 1.0 · **Ngày:** 2026-06-23

---

## Mô hình
Human Layer (SOP = ground truth) + AI Layer (12 worker vận hành theo đúng SOP). AI KHÔNG phát minh lại quy trình — tuân thủ SOP của từng phòng.

## Tài liệu
- [Workforce Map](./workforce-map_v1.0_2026-06-23.md) — 12 worker ↔ 24 SOP
- [Build Plan](./build-plan_v1.0_2026-06-23.md) — thứ tự activate nếu build skill chuyên biệt

## Trạng thái hiện tại
| Department | AI Workforce | Status |
|-----------|-------------|--------|
| 01 Product Studio | **vibe-eu-opc-prd-** orchestrator/niche-research/design | 🟢 **ACTIVATED** (8-comp, bám SOP) |
| 02 Merchandising | **vibe-eu-opc-mer-** orchestrator/catalog/product-page | 🟢 **ACTIVATED** (8-comp, bám SOP) |
| 03 Growth | **vibe-eu-opc-grw-** orchestrator/fb-ads/creative/marketing | 🟢 **ACTIVATED** (8-comp, bám SOP) |
| 04 Fulfillment & CX | **vibe-eu-opc-ful-** orchestrator/order-ops/cx | 🟢 **ACTIVATED** (8-comp, bám SOP) |
| 05 Backoffice | **vibe-eu-opc-bck-** orchestrator/finance/compliance/ops-hr | 🟢 **ACTIVATED** (8-comp, bám SOP) |

## Company GPS — 🟢 vibe-dakofits-gps (ACTIVATED 2026-06-23)
**AI Chief of Staff** — nhận task tự nhiên → route đến đúng phòng/skill (5 orchestrator), enforce gate cứng, báo cáo. PRIMARY: `_ai-workforce/vibe-dakofits-gps/` · installed `~/.claude/skills/`.
- Gọi: `/vibe-dakofits-gps` ("làm 10 SP niche Corgi US+EU bán tuần sau")
- Routing map: [vibe-dakofits-gps/kb/company-routing-map.md](./vibe-dakofits-gps/kb/company-routing-map.md)
- Điều phối theo operating-flow ShopBase-first; KHÔNG execute trực tiếp.
