# Product Spec Sheet — [Breed] AOP Leggings  `[TEMPLATE v1.0]`

> **Mục đích:** 1 phiếu = 1 sản phẩm, gom **đủ thông tin để đăng lên ShopBase** (cấu trúc tham khảo gearbunch.com/collections/yoga-pants).
> Product Page AI điền phiếu này (output/) → Catalog-Sync AI map sang `sample-csv-template-products.csv` → publish (SOP-MER-004).
> Field nào map sang cột CSV nào ghi ở `→ CSV: <Cột>`. Field bắt buộc đánh `*`.

---

## 1. Định danh & phân loại
| Field | Giá trị | → CSV |
|---|---|---|
| Breed / niche * | `[vd: Golden Retriever]` | — |
| Handle * (slug, lowercase-dấu-gạch) | `[golden-retriever-aop-leggings]` | `Handle` |
| Title * (≤140 ký tự, format: `[Adjective] [Breed] Mom Yoga Leggings — [hook]`) | `[...]` | `Title` |
| Vendor * | `[Brand name]` | `Vendor` |
| Type * | `Leggings` | `Type` |
| Collection * | `[vd: Dog Breed Leggings]` | `Collection` |
| Tags (≤13, `|` phân tách) | `[breed mom | dog mom leggings | aop leggings | ...]` | `Tags` |
| Published | `TRUE` (chỉ TRUE khi qua gate GPSR/IP) | `Published` |

## 2. Giá & margin  *(Catalog-Sync xác nhận margin 45–55% — SOP-MER-003)*
| Field | Giá trị | → CSV |
|---|---|---|
| Variant Price * (USD) | `[vd: 69.99]` | `Variant Price` |
| Compare At Price (giá gạch) | `[vd: 89.99]` | `Variant Compare At Price` |
| Cost per item (base+ship provider) | `[vd: 28.00]` | `Cost per item` |
| Variant Grams | `[vd: 250]` | `Variant Grams` |

## 3. Variant — Size × Color  *(mỗi tổ hợp = 1 dòng CSV)*
- **Option1 Name:** `Size` · **Values *:** `XS, S, M, L, XL, 2XL, 3XL`  → `Option1 Name` / `Option1 Value`
- **Option2 Name:** `Color` · **Values:** `[vd: Black]`  → `Option2 Name` / `Option2 Value`
- **SKU pattern *:** `[BREED]-[SIZE]-[COLOR]` (vd `GOLDEN-XS-BLK`)  → `Variant SKU`
- Inventory Policy: `continue` (POD không giới hạn tồn) → `Variant Inventory Policy`
- Fulfillment Service: `manual` / provider → `Variant Fulfillment Service`

## 4. Mô tả sản phẩm (Body HTML) *  → `Body (HTML)`
> Mobile-first, bán bằng cảm xúc identity breed. Viết EN. Các block theo thứ tự:

1. **Hook identity** — `[vd: "For the proud Golden Retriever Mom who lives in leggings..."]`
2. **Đoạn mô tả design** — họa tiết AOP gì, nền màu, cảm xúc (`tile / watercolor / funny / mandala`)
3. **"Why You'll Love It" — feature bullets *:**
   - Buttery-soft, squat-proof — never see-through
   - 4-way stretch, tối đa vận động
   - Cạp cao (high waist) ôm nhẹ, tôn dáng
   - In AOP 360° sống động, không phai
4. **Material *:** `82% polyester / 18% spandex` · double-stitched seam · elastic waistband
5. **Care *:** machine wash cold, tumble dry low, không là lên hình in
6. **Size guide *:** link/ảnh size chart XS–3XL (số đo inch + cm)
7. **Shipping *:**
   - **Đơn US:** provider US, production 3–7 ngày + ship 5–10 ngày
   - **Đơn EU:** provider EU, production 3–7 ngày + ship 3–7 ngày
8. **Guarantee / Returns:** đổi size XS–3XL, policy đổi/hoàn (link SOP-FUL-003/004)

## 5. Hình ảnh *  → `Image Src` / `Image Position` / `Image Alt Text` / `Variant Image`
> ⚠️ **`Image Src` PHẢI là URL ảnh PUBLIC đã host** — KHÔNG dùng đường dẫn file repo/local hay placeholder.
> Nguồn hợp lệ: **(a) URL mockup Printify/PrintBase** (sinh ở bước MER-002, ưu tiên) · **(b) URL ShopBase Media** (upload thủ công) · (c) Cloudinary/S3 link `.jpg/.png` trực tiếp.
> ❌ File in 300 DPI của Design AI KHÔNG phải ảnh sản phẩm — phải áp lên blank leggings (Printify) để ra mockup trước.
> Nếu dùng **tích hợp Printify↔ShopBase**: bỏ trống cột ảnh trong CSV — ảnh tự sync từ Printify.

| # | Loại | Alt text | Nguồn URL |
|---|---|---|---|
| 1 * | Ảnh AOP mạnh nhất (mobile hero) | `[Breed] AOP leggings front` | Printify mockup |
| 2–5 * | Model 360°, flat-lay, close-up vải | `[...]` | Printify mockup (≥5 ảnh tổng) |
| 6 * | Size chart XS–3XL | `Size guide` | asset chung / ShopBase Media |

## 6. Trust / Social proof  *(chèn vào Body HTML đầu trang)*
- Badge: `🐾 [N] Happy Dog Moms | 🚚 Fast US & EU Shipping | ✅ Squat-Proof Guarantee`
- Star rating + review/UGC block (chỉ dùng số liệu thật — Meta Ad Policy)
- ⚠️ KHÔNG copy claim "Made in USA" của gearbunch trừ khi đúng provider; đơn EU = "Printed in EU".

## 7. Upsell / Bundle *  *(Catalog-Sync cấu hình trên ShopBase)*
- **Post-ATC upsell:** Sports Bra cùng design → đẩy AOV $75–95
- **Bundle:** Leggings + Sports Bra (+ Capris nếu có)
- Related products: `[Meggings / Sports Bra / Capris / Shorts cùng breed]`

## 8. SEO  → `SEO Title` / `SEO Description`
- SEO Title (≤70): `[...]`
- SEO Description (≤320): `[...]`
- Google Shopping: Age Group `Adult` · Gender `Female` · Category `Apparel & Accessories > Clothing > Activewear`

## 9. GPSR — BẮT BUỘC cho đơn EU  *(clearance SOP-BCK-004)*  → chèn vào Body HTML
| Field | Giá trị |
|---|---|
| Manufacturer | `[EU Provider, địa chỉ]` |
| Responsible Person (EU) * | `[Tên + địa chỉ EU + email]` |
| Safety / warnings | `Adult apparel — n/a` (hoặc cảnh báo nếu có) |
| Care & material label | (mục 4) |

## 10. Compliance Gate  *(phải PASS hết mới `Published = TRUE`)*
- [ ] IP/TM breed clear (không TM/brand/character) — SOP-PRD-004 / BCK
- [ ] GPSR clearance có (đơn EU) — **no clearance = no publish** (BCK-004)
- [ ] Margin 45–55% — SOP-MER-003
- [ ] ≥5 ảnh + size chart
- [ ] Upsell/bundle sports bra cấu hình
- [ ] Meta Ad Policy: 0 claim sai

---
*Product Spec Template v1.0 | 2026-06-11 | map ↔ sample-csv-template-products.csv | ref: gearbunch yoga-pants*
