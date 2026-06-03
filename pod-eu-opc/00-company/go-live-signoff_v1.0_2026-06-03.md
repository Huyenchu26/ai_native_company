# Go-Live Sign-off — Phase 1 (Etsy + Printify)

**Ngày:** 2026-06-03 · **Phase:** 1

## Trạng thái hệ thống (sẵn sàng)
- [x] Folder structure 5 dept + _shared/_quality/_ai-workforce (228 thư mục)
- [x] 22 SOP operational + 5 doc-only — **đã điền nội dung thật**
- [x] Compliance SOP: VAT/OSS (BCK-002), GPSR (BCK-004), GDPR (BCK-005)
- [x] Pipeline SOP: PRD ×4, MER ×4, GRW ×4, FUL ×4, BCK ×6
- [x] channel-config: etsy + printify (active), shopify (planned)
- [x] Quality Standards + hard rules + incident register
- [x] Dummy data + dry-run report (gates verified)
- [x] AI Workforce map + build-plan

## Điều kiện GO-LIVE (Founder phải clear)
> Xem [launch-readiness-checklist](launch-readiness-checklist_v1.0_2026-06-03.md). Tóm tắt blocker:
- [ ] #1 Responsible Person EU (GPSR) — **BLOCKER cứng**
- [ ] #2 Nước đăng ký KD + VAT
- [ ] #3 Đăng ký OSS (tư vấn kế toán)
- [ ] #4 Publish Privacy Notice (GDPR)
- [ ] #5 Ký DPA (email/helpdesk/Printify)
- [ ] #6 Kênh tiếp nhận yêu cầu chủ thể dữ liệu

## Build order AI Workers (sau khi clear blocker)
> Chi tiết: [_ai-workforce/build-plan](../_ai-workforce/build-plan_v1.0_2026-06-03.md). Critical path:
1. Niche Research AI → 2. Design AI → 3. Listing-SEO AI → 4. Catalog-Sync AI
→ 5. Compliance AI (GPSR) → 6. Order-Ops AI → 7. CX AI → 8. Finance AI
→ 9. Marketing AI → 10. Ads AI → 11. Ops/HR AI

(Build mỗi worker bằng `/vibe-aiworkforce`, gắn SLI/SLO vào quality_[dept].)

## Trình tự go-live
```
Clear 6 blocker → kết nối Etsy+Printify (keys ngoài git) → build AI Workers (critical path)
→ publish loạt listing đầu (gate GPSR/IP/margin) → kích hoạt Growth (Pinterest + Ads nhỏ)
→ theo dõi đơn + tracking + CSKH → đối soát tài chính + profit-per-SKU tuần đầu
→ PDCA hằng tuần
```

## Sign-off
- [ ] Founder xác nhận hệ thống & clear blocker → **LAUNCH**

_Người chuẩn bị: AI Workforce (Company Architect) · Người duyệt: Founder_
