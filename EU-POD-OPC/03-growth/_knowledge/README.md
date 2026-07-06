# _knowledge — 03-growth

Tri thức nền vận hành phòng Growth (FB-ads-led POD). AI Worker tham chiếu trước khi hành động.

## 1. Meta Ads Manager
- Objective: **Conversions/Purchase**. ABO (ad-set budget, để test) vs CBO (campaign budget, để scale).
- Learning phase: tránh edit lớn (reset learning). Scale **+20%/2 ngày**.
- Metrics: ROAS, CPA, CTR (link), frequency, CPM, hook retention 3s.

## 2. CAPI (Conversions API)
- Server-side event (ShopBase ↔ Meta) chạy **song song Pixel** chống mất signal (iOS14+/ad-blocker).
- Kiểm: **Event Match Quality ≥ 6.0/10**, deduplication Pixel+CAPI (event_id) để không double-count, Purchase value đúng.
- EMQ thấp → optimize sai → HOLD scale tới khi fix.

## 3. Business Manager — 5-tier anti-ban
| Tier | Vai trò |
|------|---------|
| T1 Holding BM | sở hữu, không chạy ads |
| T2 Ad account verified | chạy winner scale (bảo vệ tối đa) |
| T3 Ad account test | chạy ABO niche mới (vùng đệm rủi ro) |
| T4 Backup (warm) | failover ngay khi T2/T3 bị flag |
| T5 Spare assets | page/pixel/domain dự phòng, recovery < 24h |
- Domain dakofits.com verify; Pixel share qua T1; mọi creative qua policy gate.

## 4. Klaviyo (Email)
- 4 flow lõi: cart-abandon, post-purchase upsell, win-back, seasonal.
- **GDPR: chỉ opt-in** (double opt-in ưu tiên), unsubscribe bắt buộc, honor erasure.
- Deliverability: SPF/DKIM/DMARC, list hygiene, frequency cap; spam < 0.1%.

## 5. Targeting Layers (4-layer)
1. **Interest** (sở thích Meta) · 2. **Behavior** (Engaged Shoppers...) · 3. **Custom Audience** (first-party: visitor/ATC/email opt-in) · 4. **Lookalike** (LAL 1–3% từ purchaser/high-value seed).

## 6. Ngưỡng vàng (quick-ref)
ROAS ≥ 2.5 · CPA < $20 · CTR ≥ 1% · EMQ ≥ 6 · frequency refresh > 2.5 · scale ≤ 20%/2 ngày · kill khi ROAS < 1.5 & spend ≥ 2× CPA target.

> Liên quan: [`_rules`](../_rules/README.md) · [`_workflow`](../_workflow/README.md) · [`_skills-agents`](../_skills-agents/README.md)
