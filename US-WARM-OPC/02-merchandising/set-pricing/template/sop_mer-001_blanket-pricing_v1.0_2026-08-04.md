# SOP-MER-001 — Blanket Pricing & Product Setup (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 02-Merchandising · **Responsible AI:** `vibe-us-warm-mer-catalog`
**Input from:** 01-Product Studio pipeline-plan (design_status=CLEAR + clearance_id)

---

## 1. Tổng quan & Mục tiêu
Đặt giá + setup variant cho chăn cá nhân hoá theo **contribution margin + BE-ROAS per-SKU** (KHÔNG gross-45 ảo, KHÔNG hard-code ROAS 2.5 — bài học EU). Đẩy AOV qua ngưỡng free-ship > $59.

## 2. IPO / ICOM
- **Input:** design CLEAR (từ PRD), supplier cost (base+ship), unit-economics.
- **Control:** contribution floor ≥ 15% @ CPA; giá vùng $39.95–59.95; free-ship threshold $59; BE-ROAS = sell/gross_before_ads.
- **Output:** `pricing-decision.json` (schema `pricing-decision.schema.json`) — sell_price, base_cost, ship, fees, allocated_cpa, contribution_margin, break_even_roas, evidence, confidence, need_review.
- **Mechanism:** unit-economics.md; supplier quote.

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Cost pull | Lấy base+ship thật từ supplier | Thiếu quote → dùng ASSUMPTION + need_review, KHÔNG chốt giá production |
| 3.2 | Contribution | Tính contribution sau CPA theo unit-economics (US no VAT) | KHÔNG dùng giá=cost/(1−margin) |
| 3.3 | BE-ROAS | BE-ROAS = sell/gross_before_ads per SKU | KHÔNG hard-code 2.5 |
| 3.4 | Floor check | contribution ≥ 15% @ CPA mục tiêu | fail → tăng giá/bundle/đổi supplier, KHÔNG scale ads |
| 3.5 | AOV | Cấu hình bundle để đẩy >$59 (free-ship) | — |

## 4. RACI
- **R:** mer-catalog · **A:** Owner · **C:** grw (CPA thật), prd (design) · **I:** ful.
- **HITL:** contribution < floor; giá lệch band; supplier cost bất thường.

## 5. Quality Gate (SLI→SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | Contribution % @ CPA | ≥ 15% | unit-economics | fail → repricing/bundle |
| 2 | BE-ROAS ghi per-SKU | present, không hard-code | schema | thiếu → reject |
| 3 | Evidence | verbatim từ unit-economics/supplier | validator --run-all | thiếu → −0.2 |

**Gate (allOf/if-then):** `below_floor=false ⇒ contribution_margin ≥ 0.15`. Fail-closed: thiếu cost thật → need_review=true.

## 6. Links
- Upstream: 01-product-studio pipeline-plan · [unit-economics](../../../_shared/unit-economics.md)
- Downstream: [preview](../../personalization-preview/template/sop_mer-002_personalization-preview_v1.0_2026-08-04.md), [product-page](../../write-product-page/template/sop_mer-003_gift-product-page_v1.0_2026-08-04.md)

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — blanket US pricing, contribution+BE-ROAS (không lặp gross-45/2.5 của EU). |
