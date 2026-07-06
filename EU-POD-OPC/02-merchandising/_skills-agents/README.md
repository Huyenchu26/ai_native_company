# _skills-agents — Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0
AI Workforce của phòng: 2 worker.

---

## 1. Worker Roster

| Worker | Skill | SOP phụ trách | Output chính |
|--------|-------|---------------|--------------|
| **Catalog-Sync AI** | `vibe-opc-pod-merch-catalog-sync` | MER-002, MER-003, MER-004 | Live product + sync log |
| **Product-Page AI** | `vibe-opc-pod-merch-product-page` | MER-001 | Product page publish-ready (EN) + GPSR label |

## 2. Skill Coverage Matrix (SOP × Worker)

| SOP | Catalog-Sync AI | Product-Page AI | OPC |
|-----|:---:|:---:|:---:|
| MER-001 Product page + GPSR | — | **R** | A |
| MER-002 Setup Printify/PrintBase | **R** | — | A |
| MER-003 Variant pricing | **R** | — | A |
| MER-004 Catalog sync + QC | **R** | C | A |
| MER-006 Promote theo đợt | C | C | **A/R** |

Coverage: 5/5 SOP có AI hỗ trợ; MER-006 do OPC điều phối + 2 worker support.

## 3. Capability — Catalog-Sync AI

- Setup blueprint Printify/PrintBase (provider US+EU).
- Tạo variant size XS–3XL × color.
- Tính & set pricing theo gross margin 45–55% (channel-agnostic, đọc `_shared/channel-config`).
- Sync ShopBase + catalog QC (diff field, accuracy ≥99%).

## 4. Capability — Product-Page AI

- Viết PDP copy EN (title, bullets, description, size guide).
- Mobile CRO + social proof + upsell/bundle sports-bra.
- Chèn nhãn GPSR cho đơn EU (input: GPSR clearance từ phòng 05).

## 5. Human-in-the-loop Checkpoints

| SOP | AI tự làm | OPC checkpoint |
|-----|-----------|----------------|
| MER-002 | Blueprint + variant | Approve blueprint |
| MER-003 | Giá trong band 45–55% | Duyệt giá ngoài band |
| MER-001 | Copy + GPSR label | Review + **gate GPSR** |
| MER-004 | Sync + QC | Spot-check trước publish |
| MER-006 | Tối ưu listing, đóng gói | Chọn SP, scale/cut |

## 6. Performance (theo dõi bởi Ops/HR AI — SOP-BCK-006)

| Metric | Target |
|--------|--------|
| Worker uptime | ≥ 99% |
| Output quality (re-work rate) | ≤ 5% |
| Sync accuracy (catalog-sync) | ≥ 99% |
| GPSR label rate (product-page) | = 100% |

## 7. Liên kết

- Knowledge: [`../_knowledge/README.md`](../_knowledge/README.md)
- Workflow: [`../_workflow/README.md`](../_workflow/README.md)
- Rules: [`../_rules/README.md`](../_rules/README.md)
