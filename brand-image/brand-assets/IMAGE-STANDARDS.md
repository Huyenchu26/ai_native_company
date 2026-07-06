# Brand & Web Image Standards — DAKOfits  `v1.0 · 2026-06-16`

> Chuẩn kích cỡ + chất lượng ảnh thương hiệu/web. Em Diễm (Design AI) tuân thủ khi tạo brand asset. Nguồn: Shopify/ShopBase image guide, PageFly banner cheat-sheet, tiny-img 2026.

## Nguyên tắc VÀNG
> **Render GỐC ở đúng (hoặc lớn hơn) kích thước hiển thị. TUYỆT ĐỐI không phóng to ảnh nhỏ.** Upscale = vỡ nét (lỗi đã gặp: banner 851×315 → 1920×640).

## Kích cỡ chuẩn theo loại asset
| Asset | Kích thước render | Tỉ lệ | Retina (nên) | Ghi chú |
|---|---|---|---|---|
| **Web hero/banner slideshow** | **1920×640** (wide) hoặc 1920×1080 | 3:1 / 16:9 | xuất 2× = 3840×1280 | Mọi slide CÙNG kích thước |
| Banner an toàn (range) | 1200–2000 W × 400–600 H | — | — | |
| **Avatar / logo** | 512×512 (tối thiểu) | 1:1 | 1024×1024 | Logo gọn trong vòng tròn crop |
| Facebook cover | 851×315 hiển thị | ~2.7:1 | upload ≥1640×624 | |
| Mockup sản phẩm | ≥1500×1500 | 1:1 | 2048×2048 | (Printify thường 2000+) |

## Chất lượng & xuất file
- **Độ phân giải:** ≥72 PPI (web). Retina: xuất 2× kích thước hiển thị.
- **Format:** PNG (đồ họa/nhiều chữ, cần sắc nét) · JPG (ảnh nhiều màu). ShopBase tự phục vụ WebP.
- **Dung lượng:** nén về **<200–300KB/slide** (tốc độ tải) NHƯNG không nén tới mức vỡ. Cân bằng nét ↔ nhẹ.
- **Không** xuất từ canvas nhỏ rồi phóng to. Nếu công cụ chỉ cho canvas nhỏ → **resize design về đúng px trước khi xuất** (Canva: resize-design), rồi xuất native.

## Quy trình tạo banner đúng (Em Diễm)
1. Tạo/đặt canvas **đúng 1920×640** (hoặc 2× = 3840×1280) NGAY TỪ ĐẦU — không dùng canvas FB cover 851×315.
2. Dùng ảnh sản phẩm gốc độ phân giải cao (≥2000px) làm asset.
3. Xuất **native** (không ép width/height từ canvas nhỏ) → PNG.
4. QC: mở 100% zoom, chữ + ảnh phải sắc; kiểm trên mobile crop.
5. Nén (TinyPNG/Squoosh) về <300KB nếu cần, kiểm lại vẫn nét.

## Checklist QC trước khi giao
- [ ] Render gốc ≥1920 px chiều rộng (không upscale)
- [ ] Chữ sắc nét ở 100% zoom
- [ ] Đúng tỉ lệ, mọi slide cùng size
- [ ] File <300KB mà vẫn nét
- [ ] Vùng chữ an toàn khi crop mobile

---
*Image Standards v1.0 | 2026-06-16 | dùng cho mọi brand/web asset DAKOfits*
