# Go-Live Sign-off — Phase 1 (ShopBase + Facebook Ads + Printify)

**Ngày:** 2026-06-08 · **Phase:** 1

## Trạng thái hệ thống (sẵn sàng)
- [x] Folder structure 5 dept + _shared/_quality/_ai-workforce
- [x] SOP operational + doc-only — **đã điền nội dung thật (pivot ShopBase + FB Ads)**
- [x] Compliance SOP: VAT/OSS (BCK-002), GPSR đơn EU (BCK-004), GDPR (BCK-005) + Meta Ad Policy
- [x] Pipeline SOP: PRD ×4, MER ×4, GRW ×5 (thêm GRW-005 fb-creative), FUL ×4, BCK ×6
- [x] channel-config: shopbase + printify (active), etsy (reference/inactive)
- [x] Quality Standards + hard rules + incident register
- [x] Dummy data + dry-run report (gates verified)
- [x] AI Workforce map (12 worker) + build-plan

## Điều kiện GO-LIVE (Founder phải clear)
> Xem [launch-readiness-checklist](launch-readiness-checklist_v1.0_2026-06-03.md). Tóm tắt blocker:
- [ ] #1 Responsible Person EU + nhãn GPSR (đơn EU) — **BLOCKER cứng cho đơn EU**
- [ ] #2 Nước đăng ký KD + VAT
- [ ] #3 Đăng ký OSS (tư vấn kế toán)
- [ ] #4 Publish Privacy Notice (GDPR) trên ShopBase
- [ ] #5 Ký DPA (Klaviyo/helpdesk/Printify/Meta)
- [ ] #6 Kênh tiếp nhận yêu cầu chủ thể dữ liệu
- [ ] #7 ShopBase Pixel + CAPI fire đúng events + Meta Ad Policy compliance (chống ban)

## Build order AI Workers (sau khi clear blocker)
> Chi tiết: [_ai-workforce/build-plan](../_ai-workforce/build-plan_v1.0_2026-06-03.md). Critical path (12 worker):
1. Niche Research AI → 2. Design AI → 3. Product Page AI → 4. Catalog-Sync AI
→ 5. FB Creative AI → 6. FB Ads Specialist AI → 7. Marketing AI
→ 8. Order-Ops AI → 9. CX AI → 10. Finance AI → 11. Compliance AI → 12. Ops/HR AI

(Build mỗi worker bằng `/vibe-aiworkforce`, gắn SLI/SLO vào quality_[dept].)

## Trình tự go-live
```
Clear blocker (đơn EU) + setup Pixel/CAPI (keys ngoài git) → build AI Workers (critical path)
→ publish loạt product đầu (gate GPSR đơn EU/IP-TM/margin ~45-55%) → kích hoạt FB Ads (ABO test nhỏ, qua Meta Ad Policy)
→ theo dõi đơn + tracking + CSKH → đối soát tài chính + ROAS/CPA/AOV + profit-per-SKU tuần đầu
→ PDCA hằng tuần
```

## Sign-off
- [ ] Founder xác nhận hệ thống & clear blocker → **LAUNCH**

_Người chuẩn bị: AI Workforce (Company Architect) · Người duyệt: Founder_
