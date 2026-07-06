# SOP-MER-005 — Product Mockup & Image Set (v1.1)

> Chủ sở hữu: vibe-eu-opc-mer-visual ("chị Ảnh") · Cập nhật 2026-06-25
> v1.1 thêm **Validation-first mode** (concept image trước khi có đơn). Bản gốc v1.0 (2026-06-23) đã mất khi reset — bản này tái lập + nâng cấp.

## Mục tiêu
Biến niche/design thành **bộ ảnh bán hàng** đăng ShopBase + chạy Facebook Ads. Hai chế độ theo vòng đời sản phẩm.

## Nguyên tắc cốt lõi — "chưa có đơn thì chưa làm AOP in thật"
| Phase | Khi nào | Nguồn ảnh | Print-accuracy |
|-------|---------|-----------|----------------|
| **Validation** | Chưa có đơn — test demand | **Canva MCP** (concept on-model/lifestyle/flat-lay/detail/size-guide/story) | Miễn (ghi rõ "concept") |
| **Production** | Đã có đơn thật | **Printify API** mockup từ file AOP seamless thật | **100% — gate cứng** |

→ Chỉ chuyển Production (làm AOP thật + Printify product) **KHI demand pass** (có đơn / CTR-CVR đạt ngưỡng Growth).

## 🚨 GATE CỨNG — PATTERN CONSISTENCY (kể cả Validation)
> **MỌI ảnh của 1 SP PHẢI dùng CÙNG 1 design/hoạ tiết.** Một listing mà mỗi ảnh hoạ tiết khác nhau = **REJECT**.

**Sai (cấm):** dùng `generate-design` text-to-image **độc lập** cho từng góc (hero/detail/flat-lay…) — mỗi lần sinh 1 hoạ tiết ngẫu nhiên khác nhau → các ảnh không phải cùng 1 sản phẩm.

**Đúng — quy trình "DESIGN-FIRST" (áp dụng cả validation):**
```
1. Tạo/chọn 1 DESIGN AOP DUY NHẤT (1 file hoạ tiết)        ← nguồn chân lý
2. Đắp design đó lên product qua MOCKUP ENGINE             ← cùng print mọi góc
   • Printify API (upload design → front/back/on-model/detail, print-chuẩn 100%)
   • hoặc Dynamic Mockups / Placeit (apply 1 design lên template legging)
3. Canva CHỈ làm: scene/lifestyle, text/CTA, size-guide graphic — KHÔNG tự vẽ lại hoạ tiết quần
```
**Canva-only KHÔNG đủ** để giữ hoạ tiết đồng nhất giữa nhiều góc → cần mockup engine (Printify/Dynamic Mockups). Nếu chỉ có Canva: chỉ được dùng **1 ảnh** rồi `resize-design` ra các format (1:1/4:5/9:16) — đồng nhất nhưng **1 góc duy nhất**, KHÔNG ghép nhiều góc khác hoạ tiết.

`pattern_consistent_across_images = false` ⇒ **REJECT** + `need_review=true`.

## Bộ ảnh chuẩn theo kênh (Validation)
| Kênh | Ảnh | Tỷ lệ | design_type Canva |
|------|-----|-------|-------------------|
| **Shop (ShopBase)** | Hero front on-model · Hero alt/on-scene · Detail close-up hoạ tiết · Flat-lay product-only · Size guide XS–3XL | 1:1 + 4:5 | `instagram_post` |
| **FB feed/ads** | Scroll-stopper (hero) · Square feed | 1:1, 4:5 | `instagram_post` / `facebook_post` |
| **FB/IG Story + Reel** | Vertical full + CTA | 9:16 | `your_story` |
| Carousel (tùy chọn) | 3–4 frame vuông | 1:1 | `instagram_post` |

**Tối thiểu:** Shop ≥4 ảnh · FB ≥2 (1 feed + 1 story).

## Quy trình (actuator) — DESIGN-FIRST
1. Nhận niche + hướng hình đã chọn (Owner/Growth approve).
2. **Tạo 1 design AOP DUY NHẤT** (image-gen tiling Leonardo/Replicate, hoặc 1 ảnh pattern Canva làm concept) → đây là nguồn chân lý.
2b. **Đắp design đó lên mockup engine** (Printify API / Dynamic Mockups) → ra hero/back/detail/flat-lay **cùng 1 print**. Canva chỉ thêm scene/text/size-guide. (Pattern-consistency gate ở trên.)
   - *Chỉ-Canva (hạn chế):* tạo 1 ảnh tốt → `resize-design` ra các format → đồng nhất nhưng 1 góc.
3. **TẢI ẢNH VỀ LOCAL (bắt buộc):** download mỗi PNG đã export về `output/images/` theo quy ước tên `NN-type.png` (`01-hero-front`, `02-hero-altcourt`, `03-flatlay`, `04-detail-closeup`, `05-size-guide`, `06-story-reel-9x16`).
   - **Lý do:** link export Canva **hết hạn sau vài giờ** → phải lưu local làm nguồn upload ShopBase/FB ổn định + archive.
   - Cách: `curl -sS -L -o output/images/NN-type.png "<export_url>"` cho từng ảnh.
4. Ghi manifest vào `output/` (design ID + export URL + **đường dẫn file local** + kênh + tỷ lệ).
5. Bàn giao: ảnh shop → mer-product-page + mer-catalog; ảnh FB → grw-creative/grw-fb-ads.

## Khai báo bắt buộc (chống hiểu lầm)
- Ảnh validation là **concept** — hoạ tiết **không đồng nhất** giữa các ảnh, **không phải file in**.
- Mọi handoff phải kèm `evidence[]` (Canva design ID, export URL), `confidence_score`, `need_review`.
- Production: gate print-accuracy 100% — KHÔNG dùng text-to-image vẽ lại quần; phải là file AOP thật qua Printify.

## Liên kết
- Skill: `../../ai_workforce/vibe-eu-opc-mer-visual/SKILL.md`
- Style guide: `../../../_shared/mockup-style-guide.md`
- Downstream: mer-product-page · mer-catalog · grw-creative
