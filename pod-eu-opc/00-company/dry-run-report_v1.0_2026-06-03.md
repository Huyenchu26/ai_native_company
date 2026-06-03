# Dry-Run Report — Phase 1 (Etsy + Printify)

> Mô phỏng tabletop chạy dummy data qua pipeline 5 department, kiểm mọi quality gate. Đây là dry-run trên giấy (chưa kết nối tài khoản thật) — mục tiêu: xác nhận thiết kế & gate hoạt động đúng trước go-live.

**Ngày:** 2026-06-03 · **Dữ liệu:** dummy (niche Cat Mom / Dog Dad)

---

## Kết quả theo department

### 01 Product Studio — ✅ PASS
- niche-list (5 niche, demand score) → design brief (Cat Mom) → **IP clearance log** (CLEARED).
- **Gate IP (PRD-004) hoạt động:** design qua scan trademark/copyright trước khi sang listing. ✅

### 02 Merchandising — ✅ PASS (thiết kế) · ⛔ chặn publish bởi blocker RP
- Listing Cat Mom: SEO đủ (title 138/140, 13 tags, 6 ảnh + size chart) ✅
- Pricing: margin 31-36% — **Gate margin ≥30% PASS** ✅
- **Gate GPSR (BCK-004→MER-001) hoạt động ĐÚNG:** listing bị **BLOCK publish** vì Responsible Person EU chưa thiết lập. → đúng thiết kế (chặn cứng).
- Provider EU được chọn (DE), UK bị loại — đúng quy tắc.

### 03 Growth — ⏸ PHỤ THUỘC listing live
- 4 SOP coherent, nhưng Pinterest/Ads cần listing **live** → bị chặn gián tiếp bởi blocker RP (listing chưa publish được).
- **Gate ROAS ≥2.5 & budget cap & email consent** sẵn sàng kích hoạt khi có traffic.

### 04 Fulfillment & CX — ✅ PASS
- 3 đơn dummy (DE/FR/NL) chạy: order → route Printify ≤24h → tracking gửi khách → CX trong SLA.
- Exception #1002 (địa chỉ thiếu) → CX xử lý → route lại. ✅
- On-time vs Etsy ETA: đạt. CX first response 0h45-1h20 (≤4h SLO). ✅

### 05 Backoffice — ✅ PASS
- Profit-per-SKU: margin thực 35% (> floor 30%) ✅
- Bookkeeping reconcile (payout↔đơn↔Printify↔ads) ✅
- VAT tách theo nước (DE/FR/NL) → BCK-002 ✅

---

## Phát hiện (findings)

| # | Phát hiện | Mức | Hành động |
|---|---|---|---|
| 1 | INC-MER-001: từng có listing publish trước khi có GPSR clearance | HIGH | ✅ Đã thêm prevention: MER-001/MER-004 chặn cứng "no clearance → no publish" |
| 2 | Listing không publish được khi chưa có Responsible Person EU | BLOCKER | Founder thiết lập RP (blocker #1) — **không phải lỗi thiết kế, là gate đúng** |
| 3 | Growth bị chặn gián tiếp tới khi có listing live | phụ thuộc | Tự thông sau khi clear RP |

## Kết luận

> **Thiết kế OPC & toàn bộ quality gate hoạt động đúng.** Không có lỗi thiết kế chặn launch.
> Go-live **chỉ còn phụ thuộc 6 blocker pháp lý** (đặc biệt Responsible Person EU + OSS + privacy notice + DPA), KHÔNG phụ thuộc SOP/pipeline.

→ Clear blockers (checklist) → publish listing → Growth tự kích hoạt → **GO-LIVE**.
