# Visual Playbook — chị Ảnh (vibe-eu-opc-mer-visual)

> Cẩm nang vận hành tạo mockup/visual cho ShopBase DAKOfits. Chuẩn canonical là [_shared/mockup-style-guide.md](../../../_shared/mockup-style-guide.md) (REF-VISUAL-001) — file này KHÔNG ghi đè, chỉ diễn giải cách làm. SOP gốc: SOP-MER-005.

## ⚠️ Trung thực: tạo SPEC+PROMPT+QC, KHÔNG tự render
Skill cho ra **brief + render-prompt + checklist QC**. Ảnh thật render bằng **tool ngoài**. Đừng bao giờ báo cáo là "đã có ảnh" khi mới chỉ có prompt.

---

## 1. Bộ 6 ảnh chuẩn (đúng thứ tự hiển thị)
| # | Loại (schema `type`) | Mục đích | Tỷ lệ |
|---|----------------------|----------|-------|
| 1 | `hero-front` — front 3/4 on-model | Ảnh đầu, khoe dáng + AOP | 1:1 |
| 2 | `hero-back` — back 3/4 on-model | Khoe AOP 360° liền mạch | 1:1 |
| 3 | `lifestyle` — bối cảnh niche | Gợi cảm xúc | 4:5 |
| 4 | `detail` — fabric close-up | Chất + độ nét print | 1:1 |
| 5 | `size` — size/fit XS–3XL | Giảm phân vân size | 1:1 |
| 6 | `ad` — scroll-stopper | Thumb-stop FB (→ chị Ý) | 4:5 |

- **SP live tối thiểu:** 3 ảnh (1,2,3).
- **Winner / SP chạy ads:** đủ 6.

## 2. Chuẩn đồng nhất (BẮT BUỘC)
- **Nền catalog:** xám trung tính **#F2F2F0**, sạch, không hoạ tiết.
- **Model:** dáng tự nhiên, focus garment (không lấy mặt làm chính), đa dạng vóc.
- **Ánh sáng:** soft, đều, không bóng gắt.
- **Màu print:** đúng file design gốc — KHÔNG over-saturate, KHÔNG để AI vẽ lại hoạ tiết.
- **Tỷ lệ:** 1:1 (ShopBase + FB feed) chính; 4:5 cho lifestyle/ad.
- **Độ phân giải:** ≥ 2000px cạnh dài, sRGB.
- **Branding:** watermark logo mờ góc dưới (tuỳ chọn, đồng nhất nếu dùng).

## 3. Pipeline 2 bước (giữ print chính xác)
1. **Base mockup** — đặt design AOP **thật** lên template legging (front+back) qua mockup generator → mockup đúng hoạ tiết, nền sạch.
2. **AI enhance** — đưa base mockup → AI on-model/scene, **inpaint NGOÀI vùng quần** (giữ nguyên print). Tạo đủ bộ ảnh theo style guide.

> Print PHẢI là design thật → KHÔNG dùng text-to-image vẽ lại quần.

## 4. Tool list
| Bước | Tool |
|------|------|
| Base mockup | Dynamic Mockups / Placeit / Mockey |
| AI on-model / scene | Botika / Photoroom / Pixelcut / PS Generative Fill |
| Host ảnh | Cloudinary / CDN |

## 5. QC Gate (check trước khi đẩy ShopBase)
| SLI | SLO | Cách check |
|-----|-----|-----------|
| Print khớp design gốc | 100% (gate cứng) | so sánh visual với file PRD-003 |
| Đủ ảnh (≥3, winner ≥6) | 100% | đếm `images[]` |
| Nền/tỷ lệ/ánh sáng theo chuẩn | ≥95% | đối chiếu style guide |
| Độ phân giải ≥2000px sRGB | 100% | metadata |

**Gate cứng:** `print_accuracy_pass = false` ⇒ `need_review = true` ⇒ REJECT, render lại, inpaint chặt vùng quần. Thiếu design gốc ⇒ ESCALATE OPC.

## 6. Ưu tiên winner (ROI — KHÔNG làm cả 3.200 cùng lúc)
Shop FB-ads-led + promote theo đợt → ưu tiên **winner + SKU đang/sắp chạy ads**, rồi SP mới theo chuẩn từ đầu. SP "ngủ" làm sau theo lô.

## 7. Bulk update ShopBase (CSV)
1. Render batch bộ ảnh/SP (Dynamic Mockups có API).
2. Host ảnh → lấy URL (CDN/Cloudinary).
3. ShopBase: **export product CSV → điền cột Image URL → import lại**.
4. Thứ tự ảnh trong CSV theo bộ 6 chuẩn (1→6).

## 8. Handoff
- Bộ ảnh + URL → **chị Lời** (`vibe-eu-opc-mer-product-page`) gắn vào product page.
- Ảnh #6 (`ad`) → **chị Ý** (`vibe-eu-opc-grw-creative`) làm ad creative.
- Output theo `schema/mockup-set.schema.json` (kèm evidence/confidence/need_review).
