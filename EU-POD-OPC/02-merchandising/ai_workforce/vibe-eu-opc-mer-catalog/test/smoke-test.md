# Smoke Test — vibe-eu-opc-mer-catalog

Mục tiêu: xác nhận skill chạy được end-to-end 1 SP cleared design → live, đúng SOP + economics. Dùng input `synthetic-data/sample-product-input.md`.

## Bước 1 — Load & verify input (MER-002)
- **Action:** đọc `synthetic-data/sample-product-input.md`.
- **Expect:** xác nhận design 300 DPI + IP cleared + 360° QC pass + có **GPSR clearance ID** (vì có market EU). Nếu thiếu → trả design/compliance.
- **Pass:** verify go/no-go đúng; thiếu field → STOP đúng chỗ.

## Bước 2 — Provider & variant (MER-002)
- **Action:** map market → provider, tạo variant set.
- **Expect:** US → provider US, EU → provider EU (2 blueprint); variant **XS–3XL × color = 100% coverage**.
- **Pass:** không thiếu size; mockup 360° QC pass.

## Bước 3 — Pricing contribution margin (MER-003)
- **Action:** tính giá per-variant theo `Contribution % = (Giá_net − base − ship − fee − CPA − VAT)/giá ≥ 15%`; KHÔNG dùng `giá=cost/(1−margin)`.
- **Expect:** US dùng giá net = giá; **EU dùng giá/1.21 (NET-of-VAT)**; BE-ROAS = 1/GM mỗi SKU/market; EU @€49.99 ra BE-ROAS ≈ 5.3 → flag nâng giá €59–69. FX = Vietcombank bán ra (ngày ghi rõ).
- **Pass:** mỗi variant xuất theo `schema/pricing-decision.schema.json`, `floor_pass` + `break_even_roas` đúng, EU tính riêng.

## Bước 4 — GATE pre-sync + sync ShopBase (MER-004)
- **Action:** chạy pre-sync gate rồi sync.
- **Expect:** GPSR gate (EU) pass vì có clearance ID; pricing floor gate pass; sync variant/giá/ảnh/page/GPSR label; **sync accuracy ≥ 99%**.
- **Pass:** không publish khi gate fail; accuracy < 99% → re-sync.

## Bước 5 — Output & evidence
- **Action:** ghi live product + sync log + bảng giá ra `output/`.
- **Expect:** mỗi record có `evidence[]` (provider cost, CPA GRW-002, FX, GPSR ID), `confidence_score ≥ 0.7`, `need_review` set đúng (true khi giá ngoài band / BE-ROAS > winner / accuracy < 99%).
- **Pass:** execution log JSONL hợp lệ theo `schema/execution-log-entry.schema.json`.

## Kết quả mong đợi
5/5 bước pass; EU flag nâng giá; không có số nào thiếu evidence; GPSR gate hoạt động.
