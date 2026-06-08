# Dry-Run Report — Phase 1 (ShopBase + Facebook Ads + Printify)

> Mô phỏng tabletop chạy dummy data qua pipeline 5 department, kiểm mọi quality gate. Đây là dry-run trên giấy (chưa kết nối tài khoản thật) — mục tiêu: xác nhận thiết kế & gate hoạt động đúng trước go-live.

**Ngày:** 2026-06-08 · **Dữ liệu:** dummy (niche Golden Retriever / French Bulldog AOP Leggings)

---

## Kết quả theo department

### 01 Product Studio — ✅ PASS
- niche-list (breed demand score + FB audience sizing) → design brief (Golden Retriever, 4 type: tile/watercolor/funny/mandala) → **IP/TM clearance log** (CLEARED).
- **Gate IP/TM (PRD-004) hoạt động:** design qua scan trademark/copyright tên breed trước khi sang product page. ✅

### 02 Merchandising — ✅ PASS (thiết kế) · ⛔ chặn publish (đơn EU) bởi blocker RP
- Product page Golden Retriever (ShopBase): copy + CRO + upsell sports bra + social proof đủ; mockup AOP 360° ✅
- Pricing: gross margin 46-53% — **Gate margin (~45–55%) PASS** ✅
- **Gate GPSR (BCK-004→MER-001) hoạt động ĐÚNG:** với đơn EU, listing bị **BLOCK publish** vì Responsible Person EU + nhãn GPSR chưa thiết lập. → đúng thiết kế (chặn cứng). Đơn US không bị chặn bởi gate này.
- Provider EU được chọn (Printify DE/Latvia) cho đơn EU; provider US cho đơn US — đúng quy tắc.

### 03 Growth — ⏸ PHỤ THUỘC product live + Meta Ad Policy
- 4 SOP (GRW-001 organic social/community, GRW-002 fb-ads, GRW-003 email, GRW-005 fb-creative) coherent; FB Ads cần product **live** → bị chặn gián tiếp khi đơn EU chưa publish được (đơn US chạy được).
- **Gate Meta Ad Policy (GRW-005/GRW-002):** creative dummy qua review policy trước khi chạy. ✅
- **Gate ROAS ≥2.5 (floor) & budget cap & email consent (GDPR)** sẵn sàng kích hoạt khi có traffic.

### 04 Fulfillment & CX — ✅ PASS
- 3 đơn dummy (US ×2, DE ×1) chạy: order → route Printify ≤24h → tracking gửi khách → CX trong SLA.
- Exception #1002 (địa chỉ thiếu) → CX xử lý → route lại. ✅
- On-time vs ShopBase ETA: đạt (US 3-7 ngày / EU 5-10 ngày). CX first response 0h45-1h20 (≤4h SLO). ✅

### 05 Backoffice — ✅ PASS
- Profit-per-SKU: gross margin thực 49% (trong ngưỡng 45-55%) ✅
- Bookkeeping reconcile (ShopBase payout↔đơn↔Printify↔Meta Ads) ✅
- VAT tách theo nước cho đơn EU (DE) → BCK-002 ✅

---

## Phát hiện (findings)

| # | Phát hiện | Mức | Hành động |
|---|---|---|---|
| 1 | INC-MER-001: từng có listing đơn EU publish trước khi có GPSR clearance | HIGH | ✅ Đã thêm prevention: MER-001/MER-004 chặn cứng "đơn EU no clearance → no publish" |
| 2 | Đơn EU không publish được khi chưa có Responsible Person EU + nhãn GPSR | BLOCKER | Founder thiết lập RP (blocker #1) — **không phải lỗi thiết kế, là gate đúng** |
| 3 | FB Ads bị chặn cho tới khi có product live + Meta Ad Policy pass | phụ thuộc | Tự thông sau khi clear RP (đơn EU) / pass policy (creative) |

## Kết luận

> **Thiết kế OPC & toàn bộ quality gate hoạt động đúng.** Không có lỗi thiết kế chặn launch.
> Go-live **chỉ còn phụ thuộc blocker pháp lý (đơn EU)** + setup Pixel/CAPI + Meta Ad Policy, KHÔNG phụ thuộc SOP/pipeline. Đơn US có thể go-live trước.

→ Clear blockers (checklist) → publish product → kích hoạt FB Ads → **GO-LIVE**.
