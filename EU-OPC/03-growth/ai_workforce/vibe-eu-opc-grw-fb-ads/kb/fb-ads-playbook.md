# FB Ads Playbook — DAKOfits (kb)

Tóm tắt vận hành cho `vibe-eu-opc-grw-fb-ads`. Nguồn canonical: [SOP-GRW-002](../../../run-fb-ads/template/sop_grw-002_fb-ads_v1.0_2026-06-23.md), [SOP-GRW-004](../../../report-growth/template/sop_grw-004_growth-report_v1.0_2026-06-23.md), [unit-economics](../../../../_shared/unit-economics.md).

---

## 1. BM 5-tier anti-ban
| Tier | Vai trò | Mục đích |
|------|---------|---------|
| T1 — Holding BM | sở hữu trung tâm, KHÔNG chạy ads | mất chỉ mất "vỏ" |
| T2 — Ad account chính (verified) | chạy winner đã scale | tài sản giá trị nhất, bảo vệ tối đa |
| T3 — Ad account test | chạy ABO test niche mới | vùng đệm chịu rủi ro |
| T4 — Backup BM/account (warm) | dự phòng warm-up sẵn | thay thế ngay khi T2/T3 flag |
| T5 — Spare assets (page, pixel, domain) | recovery nhanh | < 24h khôi phục |

Pixel chung share qua T1; domain dakofits.com đã verify. **Test ở T3, scale ở T2.** BM flag ⇒ failover T4 + escalate OPC.

## 2. 4-layer targeting (ABO)
1. **Interest** — sở thích Meta ("Yoga", "Running", breed/niche-specific).
2. **Behavior** — "Engaged Shoppers", "Online buyers".
3. **Custom Audience** — first-party: website visitors, add-to-cart, email list (opt-in/GDPR).
4. **Lookalike (LAL)** — 1–3% từ purchasers / high-value CA.

Mỗi đợt 5–10 SP (đồng bộ SOP-MER-006), 3–5 audience × creative variant. Objective: **Conversions / Purchase**. ABO budget cố định **$10/ad set/ngày** để so sánh sòng phẳng.

## 3. CAPI checklist (gate trước scale)
- [ ] Conversions API bật song song Pixel (ShopBase ↔ Meta).
- [ ] **Event Match Quality ≥ 6.0/10** (Events Manager).
- [ ] Deduplication Pixel+CAPI OK (không double-count).
- [ ] Purchase event fire đúng giá trị.
- EMQ < 6 hoặc dedup lỗi ⇒ **HOLD scale** đến khi fix (signal sai → optimize sai).

## 4. Decision rules (ngưỡng định lượng)
| Điều kiện | Hành động |
|----------|-----------|
| Chưa pass Meta Ad Policy | **HOLD/STOP** — trả creative/compliance |
| Platform ROAS ≥ 3.0 (⇒ Blended ≈ 2.5) **VÀ** Blended ≥ BE-ROAS SKU/market **VÀ** CPA < $20 | **SCALE** (CBO +20%/2 ngày, cap $100/ngày) |
| Platform ROAS ≥ 3.0 nhưng Blended < BE-ROAS SKU (lãi ảo) | **HOLD** — không scale; nâng giá/đổi provider |
| Platform ROAS ~1.8–3.0 | **OPTIMIZE** — đổi creative/audience, giữ 2 ngày |
| Platform ROAS < 1.8 sau 3 ngày & spend ≥ $40 | **KILL** |
| CPA > $20 & 0 conversion sau spend $30 | **KILL** ngay |
| Frequency > 2.5 & CTR giảm > 30% | **REFRESH CREATIVE** (ad fatigue) |
| EMQ < 6 / dedup lỗi | **HOLD** scale |
| BM/ad acct flag | **FAILOVER** T4 + escalate OPC |
| Chạm scale cap $100/ngày, hoặc tổng > $150/ngày | **ESCALATE** OPC + 05-finance |

Cửa sổ đánh giá: ≥ 3 ngày hoặc ~50 ATC/ad set. Attribution: **7-day click / 1-day view**.

## 5. Budget cap (kỷ luật)
- Test: **$10/ad set/ngày**.
- Kill ad set trước khi spend chạm **$40** (≈ 4 ngày, 2× CPA target).
- Scale cap: **$100/ngày**/SKU.
- Escalate OPC + 05-finance khi **> $150/ngày** (hard escalate).
- Trần rủi ro/đợt ≈ $40 × số ad set; OPC duyệt tổng/đợt trước khi mở batch.

## 6. Unit economics (link)
- **Platform ROAS** (Ads Manager): real-time, cao hơn thực 20–40% — chỉ tham chiếu.
- **Blended/True ROAS** = order ShopBase net-of-refund ÷ tổng ad spend (mọi BM + fee) — dùng cho commit scale & report.
- **BE-ROAS = 1/GM trước ads**, theo SKU/market: US ~2.75, EU ~5.3. **KHÔNG dùng 2.5 cứng.**
- EU @ €49.99 VAT-incl gần như không lãi cold-ads ⇒ nâng giá €59–69 hoặc retention.
- Chi tiết: [unit-economics](../../../../_shared/unit-economics.md).
