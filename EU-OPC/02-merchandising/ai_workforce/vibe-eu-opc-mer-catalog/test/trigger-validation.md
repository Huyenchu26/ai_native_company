# Trigger Validation — vibe-eu-opc-mer-catalog

Kiểm description routing đúng: kích hoạt cho setup/pricing/sync; KHÔNG nuốt việc của skill khác (product page, ads, design).

## SHOULD TRIGGER (5)

| # | Câu | Lý do |
|---|-----|-------|
| 1 | "Lên SP mới từ design corgi đã clear, setup trên Printify provider US + EU" | setup-product, thuật ngữ 'Printify','provider' |
| 2 | "Đặt giá cho variant XS–3XL của batch husky, đảm bảo không lỗ sau ads" | set-pricing, 'variant','pricing','margin sau ads' |
| 3 | "Sync catalog batch này lên ShopBase, QC xem có lệch field không" | sync-qc, 'catalog sync','ShopBase' |
| 4 | "Giá EU bị lỗ qua FB ads, tính lại contribution margin / BE-ROAS giúp" | pricing, ngữ cảnh 'giá bị lỗ', 'BE-ROAS' |
| 5 | "Set up product AOP leggings mới, tạo full variant + đặt giá + đồng bộ" | full pipeline MER-002/003/004 |

## SHOULD NOT TRIGGER (5 — bẫy)

| # | Câu | Route đúng | Bẫy |
|---|-----|-----------|-----|
| 1 | "Viết product page copy + upsell sports-bra cho SP corgi" | **vibe-eu-opc-mer-product-page** | product page copy/CRO — KHÔNG phải catalog |
| 2 | "Chạy FB ads cho batch này, scale campaign ROAS cao" | **vibe-eu-opc-grw-fb-ads** | chạy/scale ads — skill này chỉ ĐỌC CPA/winner để pricing |
| 3 | "Thiết kế file AOP print-ready 300 DPI cho breed mới" | **vibe-opc-pod-product-design** | design AOP — input của skill này, không tự design |
| 4 | "Làm video script + hook + UGC brief cho ad corgi" | **vibe-eu-opc-grw-creative** | ad creative — không liên quan catalog |
| 5 | "Cấp GPSR clearance + IP/TM check cho breed husky đơn EU" | **vibe-eu-opc-bck-compliance** | compliance CẤP clearance; skill này chỉ ĐỌC làm gate |

## Tiêu chí pass
- 5/5 SHOULD trigger; 5/5 SHOULD NOT route sang skill đúng.
- Phân biệt rõ: **pricing đọc CPA từ ads** (không chạy ads); **gate đọc GPSR** (không cấp GPSR); **input là design** (không tự design); **không viết page copy**.
