# Trigger Validation — vibe-eu-opc-prd-design

Xác minh skill kích hoạt đúng việc của mình (design AOP + IP/TM clearance) và KHÔNG lấn việc skill khác.

## SHOULD trigger (5)
1. "Làm AOP design print-ready 300 DPI cho niche Border Collie." → design AOP.
2. "Tạo seamless tile cho legging niche này, đảm bảo no seam." → design + QC 360°.
3. "Check bản quyền tên breed này trước khi listing." → IP/TM clearance.
4. "Có niche đã cleared cần design, làm giúp 4 loại style." → generate design.
5. "Design bị lỗi cắt may ở cạp/đáy quần, fix QC 360°." → QC seam/crotch/waistband.

## SHOULD NOT trigger (5) — bẫy

| # | Câu (bẫy) | Đúng skill | Lý do KHÔNG nhận |
|---|-----------|-----------|------------------|
| 1 | "Research xem niche Border Collie có demand không, audience size bao nhiêu?" | **vibe-eu-opc-prd-niche-research** | Đây là niche research/validation, không phải design |
| 2 | "Setup product trên Printify, đặt giá variant XS–3XL." | **vibe-eu-opc-mer-catalog** | Catalog setup + pricing, không phải design/clearance |
| 3 | "Viết product page copy + upsell sports-bra cho SP này." | **vibe-eu-opc-mer-product-page** | Page copy/CRO, không phải design |
| 4 | "Sync ShopBase bị lệch field, fix QC catalog." | **vibe-eu-opc-mer-catalog** | Catalog-sync QC (≠ QC AOP 360° kỹ thuật in) |
| 5 | "Làm video script/hook quảng cáo FB cho design này." | **vibe-eu-opc-grw-creative** | Ad creative, không phải design print-ready |

## Lưu ý phân biệt then chốt
- **QC 360°** (skill này) = QC kỹ thuật in AOP (seam/crotch/waistband/bleed/canvas), KHÁC **catalog-sync QC** của Merch.
- **IP/TM clearance** (skill này) = gate trước listing; **KHÁC** GPSR clearance (Merch/Backoffice) và Meta Ad Policy (Growth).
- Input là **validated niche** (đã qua research). Skill này KHÔNG tự research demand.
