# Smoke Test — vibe-eu-opc-bck-finance

Mục tiêu: xác nhận skill chạy đủ 4 phase và enforce gate chống lãi ảo. Input mẫu: [synthetic-data/sample-finance-input](../synthetic-data/sample-finance-input.md).

## Bước 1 — Bookkeeping & reconciliation (SOP-BCK-001)
- Nạp sample input (orders + fee + ad spend US/EU). Ghi sổ kép vào chart of accounts, gắn order_id/SKU.
- **PASS:** 100% giao dịch có account + SKU; fee thực vs kỳ vọng đối soát; discrepancy > 2%/$50 → escalate/`need_review`.

## Bước 2 — Profit-per-SKU (SOP-BCK-002)
- Chạy [prompt/profit-report-prompt](../prompt/profit-report-prompt.md). Tính profit_per_sku trừ ĐỦ base+ship+fee+ad CPA+VAT(EU)+fx.
- **PASS:** output mỗi SKU hợp lệ `schema/profit-report.schema.json`; đơn EU dùng giá net-of-VAT; KHÔNG có SKU "lãi" mà bỏ VAT/fx.

## Bước 3 — ROAS + break-even
- Tính blended_roas (revenue ShopBase / ad spend, KHÔNG pixel) và break_even_roas = 1/GM (US ~2.75, EU ~5.3).
- **PASS:** SKU EU dưới BE-ROAS qua cold-ads → `winner_flag` không phải winner + cờ pricing EU + `need_review: true`.

## Bước 4 — VAT OSS/IOSS + US note (SOP-BCK-003)
- Phân loại đơn EU: ≤ €150 → IOSS (tháng); hàng đã ở EU xuyên biên → OSS (quý). VAT = giá × rate nước đến. US → reconcile + nexus note (không khai).
- **PASS:** tờ khai draft đúng scheme + rate; VAT on-time flag 100%; US note có nhưng không tự khai.

## Bước 5 — P&L + CEO brief
- Lập P&L (USD) → quy VND bằng FX Vietcombank bán ra cuối kỳ; brief so target 500tr/$20k.
- **PASS:** P&L có FX footnote (nguồn + ngày); brief nêu gap, winner/loser, EU warning; net margin <20% → `need_review: true`; mọi output có `evidence[]` + `confidence_score ≥ 0.7`.
