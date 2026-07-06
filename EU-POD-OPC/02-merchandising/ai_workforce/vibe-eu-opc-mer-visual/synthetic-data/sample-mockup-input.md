# Sample Input — Mockup Set (synthetic)

> Input mẫu để chạy smoke-test / demo skill. Dữ liệu tổng hợp, không phải đơn/khách thật.

---

## INPUT
| Trường | Giá trị |
|--------|---------|
| `design_ref` | `01-product-studio/design-aop/output/2026-06-23-husky-aop-300dpi.png` (print-ready 300 DPI, từ PRD-003 / anh Họa) |
| `sku` | `DAKO-HUSKY-LEG-001` |
| `niche` | `Husky` (dog-mom) |
| `market` | US + EU |
| `is_winner` | `true` (đang chạy ads → đủ 6 ảnh) |
| `lifestyle_context` | "doing yoga outdoors at sunrise" |
| `ip_clearance_log` | `BCK-IP-2026-0617` (PASS — niche Husky đã clear) |

## Kỳ vọng output (mockup-set, đúng schema)
- `images[]`: 6 ảnh — hero-front (1:1), hero-back (1:1), lifestyle (4:5), detail (1:1), size (1:1), ad (4:5).
- Mỗi ảnh có render-prompt giữ print ("KEEP the legging print exactly as input"), nền #F2F2F0, soft light.
- `min_images_met = true` (6 ≥ 6 winner).
- `print_accuracy_pass`: do QC điền sau khi render bằng tool ngoài; gate cứng = 100%.
- `evidence[]`: link design PRD-003, base mockup, ảnh enhance, kết quả so sánh print.
- `confidence_score ≥ 0.7`; `need_review = false` nếu print pass & đủ ảnh.

## Handoff dự kiến
- Bộ ảnh + URL → `vibe-eu-opc-mer-product-page` (chị Lời).
- Ảnh `ad` (#6) → `vibe-eu-opc-grw-creative` (chị Ý).

> Lưu ý: đây là SPEC+PROMPT; render ảnh thật bằng Dynamic Mockups/Placeit (base) + Botika/Photoroom (enhance), host Cloudinary.
