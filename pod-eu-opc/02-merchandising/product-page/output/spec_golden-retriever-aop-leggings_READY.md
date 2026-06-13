# Product Spec Sheet — Golden Retriever AOP Leggings  `[DUMMY — publish-ready]`

> Output mẫu SOP-MER-001 theo `product-spec-template_v1.0.md`. Điền đủ 10 mục → handoff Catalog-Sync map CSV.

---

## 1. Định danh & phân loại
| Field | Giá trị | → CSV |
|---|---|---|
| Breed / niche | Golden Retriever | — |
| Handle | golden-retriever-aop-leggings | `Handle` |
| Title | Golden Retriever Mom Yoga Leggings — Squat-Proof High-Waist AOP | `Title` |
| Vendor | PawCouture | `Vendor` |
| Type | Leggings | `Type` |
| Collection | Dog Breed Leggings | `Collection` |
| Tags | golden retriever mom \| dog mom leggings \| aop leggings \| yoga pants \| squat proof leggings \| high waist leggings \| golden retriever gift \| dog lover gift \| athletic leggings \| dog mom gift | `Tags` |
| Published | TRUE (đã qua gate — xem mục 10) | `Published` |

## 2. Giá & margin  *(Catalog-Sync confirm margin)*
| Field | Giá trị | → CSV |
|---|---|---|
| Variant Price | 69.99 | `Variant Price` |
| Compare At Price | 89.99 | `Variant Compare At Price` |
| Cost per item | 28.00 | `Cost per item` |
| Variant Grams | 250 | `Variant Grams` |
> Margin gộp ≈ (69.99 − 28.00 − ~2.50 fee) / 69.99 ≈ **56%** → ✅ trong floor 45–55%+ (Catalog-Sync chốt).

## 3. Variant — Size × Color
- **Option1 Name:** Size · **Values:** XS, S, M, L, XL, 2XL, 3XL
- **Option2 Name:** Color · **Values:** Black
- **SKU pattern:** `GOLDEN-[SIZE]-BLK`
- Inventory Policy: `continue` · Fulfillment: `manual`

## 4. Mô tả sản phẩm (Body HTML)  → `Body (HTML)`
1. **Hook:** "For the proud Golden Retriever Mom who lives in her leggings — wear the love."
2. **Design:** AOP watercolor Golden Retriever faces rải đều trên nền than chì ấm, in 360° liền mạch.
3. **Why You'll Love It:**
   - Buttery-soft, **squat-proof — never see-through**
   - 4-way stretch tối đa vận động (yoga, gym, dạo phố)
   - Cạp cao ôm nhẹ tôn dáng
   - In AOP 360° sống động, bền màu
4. **Material:** 82% polyester / 18% spandex · double-stitched seam · elastic waistband
5. **Care:** Machine wash cold, tumble dry low, không là lên hình in
6. **Size guide:** XS–3XL (ảnh size chart inch + cm) — mục 5 ảnh #6
7. **Shipping:** Đơn US: production 3–7 ngày + ship 5–10 ngày · Đơn EU: provider EU, production 3–7 + ship 3–7 ngày
8. **Guarantee/Returns:** Đổi size XS–3XL trước khi in; policy đổi/hoàn SOP-FUL-003/004.

## 5. Hình ảnh  → `Image Src/Position/Alt`
| # | Loại | Alt text |
|---|---|---|
| 1 | Hero AOP front (mobile) | Golden Retriever AOP leggings front |
| 2 | Model 360° back | Golden Retriever leggings back view |
| 3 | Flat-lay | Golden Retriever leggings flat lay |
| 4 | Close-up vải/cạp | Golden Retriever leggings high waistband closeup |
| 5 | Lifestyle (dog mom + dog) | Golden Retriever mom wearing leggings |
| 6 | Size chart XS–3XL | Size guide |

## 6. Trust / Social proof
- Badge: `🐾 12,000+ Happy Dog Moms | 🚚 Fast US & EU Shipping | ✅ Squat-Proof Guarantee`
- ⭐ 4.8 (số liệu thật khi có review) · UGC dog-mom block
- Đơn EU = "Printed in EU" (không dùng "Made in USA").

## 7. Upsell / Bundle
- Post-ATC upsell: **Golden Retriever Sports Bra** → AOV $75–95
- Bundle: Leggings + Sports Bra
- Related: Golden Retriever Sports Bra / Capris / Shorts

## 8. SEO  → `SEO Title/Description`
- SEO Title: Golden Retriever Mom Yoga Leggings — Squat-Proof AOP (XS–3XL)
- SEO Description: High-waist squat-proof Golden Retriever leggings with all-over watercolor print. 4-way stretch, XS–3XL. Fast US & EU shipping. Perfect gift for the Golden Retriever mom.
- Google Shopping: Age `Adult` · Gender `Female` · Category `Apparel & Accessories > Clothing > Activewear`

## 9. GPSR — đơn EU  → chèn Body HTML
| Field | Giá trị |
|---|---|
| Manufacturer | [EU Provider DE — địa chỉ] |
| Responsible Person (EU) | [TODO Founder — tên + địa chỉ EU + email] |
| Safety/warnings | Adult apparel — n/a |
| Care & material | (mục 4) |

## 10. Compliance Gate
- [x] IP/TM "Golden Retriever" clear (tên giống chung, không TM)
- [ ] **GPSR clearance (đơn EU)** — ⚠️ chờ Responsible Person → BLOCK publish đơn EU tới khi có RP
- [x] Margin ~56% ✅
- [x] ≥5 ảnh + size chart
- [x] Upsell/bundle sports bra
- [x] Meta Ad Policy: 0 claim sai

> **Gate:** US ✅ publish được · **EU ⚠️ chờ RP (BLOCK)** — đúng quy tắc no GPSR = no publish (BCK-004).

---
*Spec READY | 2026-06-11 | handoff Catalog-Sync AI → CSV*
