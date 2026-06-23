# Trigger Validation — vibe-eu-opc-ful-order-ops

Kiểm description [TRIGGER]/[EXCLUSION] route đúng. 5 SHOULD trigger + 5 SHOULD NOT (bẫy).

## SHOULD trigger (skill này nhận)
1. "Có đơn mới về trên ShopBase, **xử lý đơn** giúp." → monitor+verify. ✅
2. "**Đẩy đơn đi in** trên **Printify** cho lô đơn EU hôm nay." → route. ✅
3. "Khách hỏi **tracking** đơn #1234, đơn đã ship chưa **gửi tracking**." → send-tracking. ✅
4. "Đơn này **chưa route**, verify rồi đẩy provider đi." → verify+route. ✅
5. "**Fulfillment** đơn US: chọn provider nào, **order** đã paid." → route theo vùng. ✅

## SHOULD NOT trigger (bẫy — route sang skill khác)
1. "Khách đòi **refund** vì không vừa size, xử lý **return** giúp." → ❌ vibe-eu-opc-ful-cx (support/refund).
2. "Mở **support ticket**: khách than đơn giao chậm, soạn email xin lỗi." → ❌ vibe-eu-opc-ful-cx (CX ticket).
3. "Khách muốn **size exchange** XL sang 2XL." → ❌ vibe-eu-opc-ful-cx (exchange).
4. "**Ghi sổ** chi phí print tháng này + lên **tờ khai VAT** EU." → ❌ vibe-eu-opc-bck-finance (bookkeeping).
5. "Tính **profit-per-SKU** và **P&L** đợt promote vừa rồi." → ❌ vibe-eu-opc-bck-finance.

## Ghi chú gate
- Order-Ops CHỈ làm: monitor → verify → route → send-tracking + đẩy raw cost data sang backoffice.
- KHÔNG trả lời/ giải quyết ticket, return, refund, complaint (→ cx). KHÔNG ghi sổ/VAT/reconcile/P&L (→ finance).
- Khi đơn cần khách phản hồi (address sai / OOS / delay) → tạo exception + handoff cx, KHÔNG tự viết email support.
