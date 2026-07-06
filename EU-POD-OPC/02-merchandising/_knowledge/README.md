# _knowledge — Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0
Kiến thức nền cho 2 AI worker setup/price/page/sync AOP leggings.

---

## 1. Print Provider — Printify / PrintBase

| Mục | Nội dung |
|-----|----------|
| Provider US | Phục vụ đơn US — ship nhanh nội địa, không VAT EU |
| Provider EU | Phục vụ đơn EU — giảm ship time, tránh import VAT/customs |
| Blueprint AOP | All-Over-Print legging/activewear, in 360° (seam-to-seam) |
| QC AOP | Align print qua seam, không bị cắt mảng quan trọng, 300 DPI |
| Cost | Khác nhau US/EU + theo size (plus-size cao hơn) |
| Stock | Theo dõi OOS per variant → ẩn/đổi provider |

## 2. ShopBase (store dakofits.com)

| Mục | Nội dung |
|-----|----------|
| Catalog | Product → variant (size × color) → SKU |
| Sync | Printify/PrintBase connector → ShopBase; map variant↔SKU |
| PDP schema | Title, bullets, description, size guide, ảnh, review, upsell, GPSR block |
| TOS | Tuân ShopBase TOS (không bán hàng cấm/IP vi phạm) |
| Traffic | 100% Facebook Ads → ~80% mobile → ưu tiên mobile CRO |

## 3. Variant size XS–3XL

| Mục | Nội dung |
|-----|----------|
| Size range | XS, S, M, L, XL, 2XL, 3XL — bắt buộc đủ |
| Size guide | Đo cm + inch, waist/hip/inseam |
| Plus-size | 2XL–3XL cost cao → price step-up giữ margin |
| Color | Mỗi design có thể nhiều color base |

## 4. Pricing & Gross Margin

| Mục | Nội dung |
|-----|----------|
| Floor | Gross margin **≥ 45%** — không SP nào dưới |
| Band mục tiêu | 45–55% |
| Công thức | giá = cost / (1 − margin) |
| Cost base | gồm provider cost + ship |
| Reference | Gearbunch + giá thị trường AOP legging |
| Psychological | $XX.99, compare-at để show discount |
| VAT | EU: giá VAT-inclusive (phối phòng 05) |

## 5. GPSR Label (đơn EU)

| Mục | Nội dung |
|-----|----------|
| Regulation | GPSR (EU) 2023/988 — General Product Safety |
| Bắt buộc | SP bán EU phải có nhãn an toàn + Responsible Person (EU) |
| Nguồn clearance | Phòng 05-backoffice (SOP-BCK-004) |
| Nội dung label | Tên+địa chỉ Responsible Person, cảnh báo an toàn, material/care, mã SP |
| Gate | **No GPSR clearance → no publish** (đơn EU) |
| US | Không bắt buộc GPSR; giữ care info |

## 6. Liên kết

- Rules: [`../_rules/README.md`](../_rules/README.md)
- Workflow: [`../_workflow/README.md`](../_workflow/README.md)
- Skills/Agents: [`../_skills-agents/README.md`](../_skills-agents/README.md)
