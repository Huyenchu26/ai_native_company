# Smoke Test — vibe-eu-opc-ful-order-ops

5 bước kiểm tra skill chạy đầu-cuối. Dùng `synthetic-data/sample-order-input.md` làm input.

## Bước 1 — Monitor / sync
- Cho input 2 đơn (1 US, 1 EU). Skill phải nhận diện cả 2 là `paid`, loại đơn `unpaid/cancelled` nếu có.
- **PASS**: cả 2 đơn vào pipeline, gắn `paid_at`.

## Bước 2 — Verify
- Skill chạy 4 check (payment/address/SKU XS–3XL/fraud) cho mỗi đơn.
- **PASS**: đơn hợp lệ → `verify_status = PASS`; đơn lỗi → HOLD/FRAUD + `exception_tag` đúng.

## Bước 3 — Route theo vùng
- Đơn US → provider **US**; đơn EU → provider **EU**.
- Tính `routed_within_h`. **PASS**: provider match đúng vùng, `routed_within_h ≤ 18` (cảnh báo nếu 18–24, hard-fail nếu > 24).

## Bước 4 — Send tracking
- Đơn `fulfilled` có tracking# → `tracking_sent = true`, email EN soạn, `tracking_sent_at` ≤6h sau fulfilled.
- **PASS**: tracking gửi + `cost_pushed_backoffice = true`.

## Bước 5 — Output schema + gate
- Output validate qua `schema/order-routing.schema.json` (8 field required).
- **PASS**: có `evidence[]` ≥1, `confidence_score` ∈ [0,1], `need_review` đúng quy tắc (true khi conf<0.7 / HOLD / FRAUD / >24h).

**Kết quả mong đợi:** 5/5 PASS → skill sẵn sàng. Bất kỳ FAIL → kiểm SOP binding + schema.
