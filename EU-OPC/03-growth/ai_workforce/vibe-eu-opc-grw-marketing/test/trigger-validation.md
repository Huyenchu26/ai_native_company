# Trigger Validation — vibe-eu-opc-grw-marketing

Xác nhận skill kích hoạt đúng phạm vi (email + organic) và KHÔNG lấn việc skill khác.

## SHOULD trigger (5)
1. "Gửi email khuyến mãi seasonal cho list opt-in niche Husky." → **email seasonal flow**.
2. "Set up cart-abandon flow trên Klaviyo cho khách bỏ giỏ hàng." → **email cart-abandon**.
3. "Đăng bài organic IG + Reel cho bộ sưu tập mới." → **organic-post**.
4. "Build cộng đồng dog-mom, seed UGC review vào group." → **community-seed (UGC seeding)**.
5. "Làm win-back email cho khách 90 ngày không mua." → **email win-back**.

## SHOULD NOT trigger (5 — bẫy)
1. "Tăng budget chiến dịch FB Ads lên +20%." → **paid ads** → chuyển `vibe-eu-opc-grw-fb-ads`.
2. "Viết video script hook 0–3s + carousel asset cho ad." → **ad creative** → chuyển `vibe-eu-opc-grw-creative`.
3. "Khách hỏi đổi size XS sang M, xử lý ticket." → **fulfillment/CX** → chuyển CX AI.
4. "Tạo ad creative brief image cho leggings." → **ad creative** → chuyển `vibe-eu-opc-grw-creative`.
5. "Route đơn ShopBase sang Printify, gửi tracking." → **order-ops** → không thuộc skill này.

> PASS: 5 SHOULD kích hoạt đúng phase; 5 SHOULD NOT đều được nhận diện và đổi hướng (đặc biệt paid ads, ad creative, fulfillment).
