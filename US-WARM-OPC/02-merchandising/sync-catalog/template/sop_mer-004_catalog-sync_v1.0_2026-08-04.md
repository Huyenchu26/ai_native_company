# SOP-MER-004 — Catalog Sync & Go-Live (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 02-Merchandising · **Responsible AI:** `vibe-us-warm-mer-catalog`

## 1. Mục tiêu
Đóng gói listing đã pass (pricing + preview + product-page + compliance) thành **listing package** đẩy lên store (Shopify) và register vào catalog live → tín hiệu cho 03-growth.

## 2. IPO
- **Input:** pricing-decision (floor pass), mockup-set (production, images on disk), product-page (publish-ready).
- **Control:** chỉ sync khi CẢ 3 pass gate; SKU unique; live-product register.
- **Output:** `listing-package.json` — sku, price, images_ref, page_ref, live_status, evidence, confidence, need_review.
- **Mechanism:** Shopify API (cần token — thiếu → live_status=pending, KHÔNG khai live).

## 3. Gate (allOf/if-then)
`live_status=live ⇒ pricing_floor_pass=true ∧ images_on_disk=true ∧ product_page_publish_ready=true`. Fail-closed: thiếu Shopify token → pending.

## 4. RACI
R: mer-catalog · A: Owner · C: mer-visual, mer-product-page · I: grw (nhận live-product signal — giải quyết bug EU M7: growth chờ catalog).

## 5. Links
Upstream: MER-001/002/003. Downstream: 03-growth (organic/ads cần live-product). Register: `_shared/winner-registry`.

## 6. History
| 1.0 | 2026-08-04 | Khởi tạo — go-live gate, phát live-product signal cho growth (fix EU M7 cadence). |
