# Channel Config — ShopBase (ACTIVE — PRIMARY store)

- **Status:** active — kênh bán chính (store)
- **Plan/Fee:** ShopBase Basic $19/tháng · transaction fee ~$1.5/đơn (theo gói) · không phí listing
- **API/keys:** lưu NGOÀI git (vd .env / secret manager) — KHÔNG commit
- **Vai trò:** landing page + checkout cho 100% traffic từ Facebook Ads (paid). KHÔNG dựa SEO organic.
- **Product page (thay Etsy SEO):** product copy hướng identity ("Golden Retriever Mom") · CRO mobile-first · upsell/cross-sell built-in (leggings → sports bra) · bundle · social proof/review (SOP-MER-001)
- **Upsell/AOV:** built-in upsell + bundle để đẩy AOV từ $59–69 lên $75–95 (sports bra cùng design)
- **Tracking:** ShopBase Pixel + Facebook CAPI bật từ ngày 1 — fire ViewContent/AddToCart/InitiateCheckout/Purchase (kèm order value). Xem `facebook-ads.md`.
- **Email:** Klaviyo (chính) + ShopBase built-in email (cart abandon, post-purchase upsell, win-back) — chỉ gửi khi opt-in (GDPR, SOP-GRW-003)
- **Compliance:** GPSR label bắt buộc cho **đơn EU** (SOP-BCK-004) → no clearance = no publish · VAT/OSS/IOSS (SOP-BCK-002) · Meta Ad Policy cho landing page (no misleading claim)
- **Fulfillment:** Printify (chính) / PrintBase / Printful / Gelato — xem `printify.md`
- **SLA chất lượng:** ship on-time · phản hồi CX <24h · rating ≥4.8 · tracking đầy đủ (SOP-FUL-002/003)
- **Tích hợp:** Printify ↔ ShopBase (auto-publish + auto-fulfill); PrintBase tích hợp sẵn trong ShopBase
