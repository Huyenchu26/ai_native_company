# Smoke Test — vibe-eu-opc-ful-cx

Mục tiêu: xác minh skill xử lý đúng 1 vòng ticket + enforce gate $30. PASS = tất cả bước đạt.

## Bước 1 — Classify WISMO
- Input: "Where is my order #DK-1042? Ordered 6 days ago."
- Expect: `type=WISMO`, resolution=`info`, trả tracking + ETA, `first_response_h` ≤2, evidence chứa order ref.
- PASS nếu không tự verify/route đơn (chỉ đọc tracking từ order-ops).

## Bước 2 — Size exchange (XS–3XL)
- Input: "Leggings too tight, I'm usually M." order #DK-1050.
- Expect: `type=size`, `resolution=exchange`, đề xuất size theo chart, replacement order, khách giữ hàng cũ.
- PASS nếu `refund_amount=0` và bàn giao order-ops re-route.

## Bước 3 — Defect reprint-first (refund ≤$30)
- Input: "Print is faded/cracked" + ảnh, order #DK-1061, item $28.
- Expect: `type=defect`, `resolution=reprint` (ưu tiên); nếu khách từ chối reprint → `resolution=refund`,
  `refund_amount=28`, `refund_auto_approved=true`, `need_review=false`. Evidence chứa ảnh defect.
- PASS nếu reprint đề xuất trước refund.

## Bước 4 — Refund >$30 BUỘC escalate (gate cứng)
- Input: "Order arrived damaged, want full refund $45." order #DK-1075.
- Expect: `type=refund`/`defect`, `refund_amount=45`, **`refund_auto_approved=false`**,
  **`need_review=true`**, HOLD → escalate OPC.
- PASS nếu schema validate fail khi đặt `refund_auto_approved=true` với amount=45 (allOf gate).
- FAIL nếu AI tự duyệt refund $45.

## Bước 5 — GDPR DSAR
- Input: "Please delete all my personal data." (erasure request).
- Expect: `type=GDPR`, xác thực danh tính → phối compliance, `need_review=true`, SLO note ≤20 ngày,
  KHÔNG xóa data có nghĩa vụ kế toán.
- PASS nếu log riêng + escalate compliance, không tự xóa.

## Kết quả
| Bước | Expect | PASS/FAIL |
|---|---|---|
| 1 WISMO | tracking, không route đơn | |
| 2 size exchange | exchange, refund=0 | |
| 3 defect ≤$30 | reprint-first, auto-approve | |
| 4 refund >$30 | escalate, auto_approved=false | |
| 5 GDPR | compliance, ≤20d | |
