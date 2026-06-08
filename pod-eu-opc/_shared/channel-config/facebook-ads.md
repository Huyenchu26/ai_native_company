# Channel Config — Facebook Ads (ACTIVE — PRIMARY traffic)

- **Status:** active — kênh traffic chính (100% paid)
- **Vai trò:** Meta Ads Manager kéo traffic về ShopBase product page. Organic (IG/TikTok/FB dog groups) chỉ hỗ trợ — xem SOP-GRW-001.
- **API/keys:** Meta Ads API + System User token lưu NGOÀI git — KHÔNG commit

## Cấu trúc Business Manager (chống ban — 5 tầng)
```
Master BM (KHÔNG chạy ads — chỉ quản lý Pixel/asset)
  └── Ad BM 1 (Dog niche)
        ├── Ad Account 1 (TEST campaigns)
        └── Ad Account 2 (SCALE campaigns)
  └── Ad BM 2 (backup / niche mở rộng sau này)
```
- Warm account trước khi spend; verify domain ShopBase; 1 page/1 pixel chuẩn

## Pixel + CAPI
- ShopBase Pixel + Facebook CAPI bật từ ngày 1 (kể cả chưa chạy ads)
- Events: ViewContent · AddToCart · InitiateCheckout · Purchase (kèm order value) — verify fire đúng (SOP-GRW-002)

## 4 Layer Targeting
- **L1 Interest (cold):** breed-specific (Golden Retriever ~8M, French Bulldog ~6M, Corgi) + pet behavior (Chewy, BarkBox, dog training); nữ 25–54, US (mở UK/CA/AU sau)
- **L2 Behavior stack:** Engaged Shoppers + Online shoppers × Interest breed
- **L3 Custom Audience:** website visitor 7/14/30d · add-to-cart chưa mua · đã mua → upsell
- **L4 Lookalike (scale):** LAL 1% từ purchase (cần 50+ events) + LAL add-to-cart

## Campaign structure
- **Phase 1 — TEST ABO:** $5–10/ngày/ad set · 3 creative/ad set · cut ad set CPP > 2x target sau 3–5 ngày
- **Phase 2 — SCALE CBO:** $50–100/ngày · duplicate winner · +20% budget/2 ngày

## KPI & Gate
- CTR >2% · CPC <$1.5 · CPA <$20 · ROAS ≥2.5 (floor 2.0)
- **GATE:** ROAS < floor → pause campaign (SOP-GRW-002) · Meta Ad Policy chưa đạt → KHÔNG chạy ads (SOP-BCK-004)
- **Ad spend = chi phí riêng**, KHÔNG tính vào OPEX cố định (xem cost-analysis)

## Công cụ phụ trợ (thay eRank/Marmalead)
- AdSpy/BigSpy (spy competitor ads) · Meta Audience Insights · Google Trends
