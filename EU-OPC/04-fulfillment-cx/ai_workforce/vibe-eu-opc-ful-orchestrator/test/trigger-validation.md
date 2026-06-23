# Trigger Validation — vibe-eu-opc-ful-orchestrator

Kiểm tra skill **kích hoạt đúng** (SHOULD) và **KHÔNG kích hoạt sai** (SHOULD NOT). Bẫy chính: việc chuyên môn cụ thể (route 1 đơn, reply 1 ticket, duyệt 1 refund) phải delegate xuống specialist; việc phòng khác (ghi sổ, clearance, live product) phải escalate.

---

## SHOULD trigger (điều phối Fulfillment & CX — Manager)

| # | Input | Vì sao |
|---|-------|--------|
| 1 | "Điều phối lô đơn + ticket hôm nay, đảm bảo on-time." | Batch dispatch end-to-end → fan-out (thuật ngữ 'điều phối đơn') |
| 2 | "Quản lý đơn & support tuần này cho cả US và EU." | Điều phối toàn phòng order-ops + cx ('quản lý đơn & support') |
| 3 | "Xử lý vận hành đơn: 12 đơn mới về cần route, 5 ticket đang chờ." | Nhiều đơn + ticket cần điều phối ('xử lý vận hành đơn') |
| 4 | "Lô đơn từ Growth vừa đổ về, điều phối fulfillment & CX giúp." | Ngữ cảnh batch từ upstream cần orchestrate ('fulfillment', 'CX') |
| 5 | "On-time SLA đang rủi ro, sắp xếp ưu tiên route + ai xử ticket refund." | Cross-worker coordination + enforce SLA gate |

## SHOULD NOT trigger (delegate hoặc escalate — KHÔNG tự làm)

| # | Input | Đúng hành vi |
|---|-------|--------------|
| 1 | "Route đơn #ORD-1001 sang Printify US, gửi tracking cho khách." | **Delegate** → `vibe-eu-opc-ful-order-ops` (việc route cụ thể, KHÔNG tự route) |
| 2 | "Soạn reply EN cho khách đổi size M→L và xử refund $20." | **Delegate** → `vibe-eu-opc-ful-cx` (việc support/refund cụ thể) |
| 3 | "Verify queue đơn ShopBase và lọc đơn exception OOS." | **Delegate** → `vibe-eu-opc-ful-order-ops` (việc monitor cụ thể FUL-001) |
| 4 | "Reconcile print/ship cost với fee ShopBase và khai VAT OSS." | **Escalate** → 05-backoffice finance (ghi sổ, phòng khác) |
| 5 | "Cấp GPSR clearance + Responsible Person cho SP EU mới." | **Escalate** → 05-backoffice compliance (clearance chính thức, phòng khác) |

---

## Bẫy quan trọng
- Skill là **Manager** — nếu input là **một việc chuyên môn đơn lẻ** (route 1 đơn, reply 1 ticket, duyệt 1 refund, verify 1 queue), KHÔNG execute mà **route** xuống đúng specialist.
- Việc thuộc **phòng khác** (ghi sổ/reconcile/VAT, clearance GPSR/IP/GDPR chính thức, live product/variant, đơn nguồn/ads) → **escalate** theo matrix, KHÔNG xử lý.
- Chỉ "ôm" trọn vẹn khi là **điều phối đa-worker** hoặc **batch đơn + ticket end-to-end**.

**PASS khi:** 5/5 SHOULD trigger + route/orchestrate; 5/5 SHOULD NOT chuyển sang delegate/escalate đúng đích.
