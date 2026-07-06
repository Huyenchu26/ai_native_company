# Trigger Validation — vibe-eu-opc-grw-fb-ads

Kiểm tra description trigger đúng phạm vi (FB Ads) và KHÔNG over-trigger sang creative/email/fulfillment.

## ✅ SHOULD trigger (5)
1. "Scale campaign legging Husky đang có ROAS 3.2, chuyển qua CBO giúp tao." — *(thuật ngữ: scale campaign, ROAS, CBO)*
2. "Chạy ads cho 8 sản phẩm mới của đợt promote này." — *(nói tự nhiên: chạy ads cho sản phẩm)*
3. "CAPI EMQ tụt xuống 4.5, kiểm tra dedup Pixel với Conversions API." — *(thuật ngữ: CAPI, EMQ)*
4. "Tối ưu campaign EU, CPA đang cao quá $25, cắt mấy ad set lỗ." — *(ngữ cảnh: tối ưu campaign, CPA cao, kill loser)*
5. "Đang đốt tiền ads mà không ra đơn, xem lại budget với ngưỡng kill." — *(ngữ cảnh than phiền: đốt tiền ads không hiệu quả)*

## ❌ SHOULD NOT trigger (5 — bẫy)
1. "Viết hook video 0–3s + script UGC cho legging Corgi." — *(BẪY creative → vibe-eu-opc-grw-creative)*
2. "Soạn email cart-abandon trên Klaviyo gửi danh sách opt-in." — *(BẪY email → vibe-eu-opc-grw-marketing)*
3. "Đăng bài organic vào group dog-mom trên Facebook." — *(BẪY organic social → vibe-eu-opc-grw-marketing)*
4. "Đơn hàng ShopBase chưa route sang Printify, kiểm tra fulfillment." — *(BẪY fulfillment → vibe-eu-opc-fulfillment-order-ops)*
5. "Thiết kế AOP mandala 300 DPI cho breed mới." — *(BẪY design → vibe-eu-opc-product-design)*

## Tiêu chí pass
- 5/5 SHOULD trigger nhận đúng skill này.
- 5/5 SHOULD NOT trả về skill khác (không over-trigger). EXCLUSION trong description phải chặn được creative/email/organic/fulfillment/design.
