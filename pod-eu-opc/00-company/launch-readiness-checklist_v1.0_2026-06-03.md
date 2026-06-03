# Launch Readiness Checklist — POD EU OPC

> Tổng hợp các điều kiện **bắt buộc** trước khi go-live Etsy + Printify. Sinh ra từ Tuần 1 (compliance SOPs). Cập nhật trạng thái khi hoàn thành.

**Ngày:** 2026-06-03 · **Phase:** 1 (Etsy + Printify)

---

## 🔴 BLOCKERS pháp lý (không có → không được bán vào EU)

| # | Việc | SOP | Người | Trạng thái |
|---|---|---|---|---|
| 1 | Thiết lập **Responsible Person trong EU** (đăng ký pháp nhân EU, hoặc dùng dịch vụ RP của Printify/bên thứ ba) | SOP-BCK-004 | Founder | ☐ |
| 2 | Chốt **nước đăng ký kinh doanh** + trạng thái VAT | SOP-BCK-002 | Founder | ☐ |
| 3 | Quyết định **đăng ký OSS** (ngay hay chờ ngưỡng €10k) — tư vấn kế toán | SOP-BCK-002 | Founder + kế toán | ☐ |
| 4 | **Publish Privacy Notice** (GDPR) trên shop | SOP-BCK-005 | Founder | ☐ |
| 5 | Ký/đối chiếu **DPA** với email tool, helpdesk, Printify | SOP-BCK-005 | Founder | ☐ |
| 6 | Lập kênh tiếp nhận **yêu cầu chủ thể dữ liệu** (truy cập/xóa) | SOP-BCK-005 | Founder | ☐ |

## 🟡 Vận hành (cần để chạy pipeline — Tuần 2-3)

| # | Việc | SOP | Trạng thái |
|---|---|---|---|
| 7 | Tài khoản Etsy + Printify, kết nối (keys để **ngoài git**) | channel-config | ☐ |
| 8 | Chọn **print provider EU** cho dòng sản phẩm chính | SOP-MER-002 | ☐ |
| 9 | Chốt **niche apparel** khởi đầu + tiêu chí | SOP-PRD-001/005 | ☐ |
| 10 | Điền pricing floor (margin ≥ 30%) | SOP-MER-003 | ☐ |
| 11 | Bảng thuế suất VAT theo nước EU (knowledge) | SOP-BCK-002 | ☐ |

## ✅ Đã xong (Tuần 1 — Foundation)

- [x] Folder structure 5 department + `_shared` / `_quality` / `_ai-workforce`
- [x] Company charter, vision/mission, business strategy, OKR (khung)
- [x] 5 department README + charter
- [x] **3 SOP compliance chi tiết:** VAT/OSS (BCK-002), GPSR (BCK-004), GDPR (BCK-005)
- [x] Backoffice Quality Standards + hard rules

---

## Hạng mục cần tư vấn chuyên môn (không tự quyết)
> AI/SOP chỉ chuẩn bị; các mục này cần **kế toán thuế EU** và/hoặc **tư vấn pháp lý**:
- Cấu trúc pháp nhân & nơi đăng ký (ảnh hưởng VAT/OSS, RP)
- Phạm vi Etsy "deemed supplier" cho từng thị trường
- Yêu cầu GPSR cụ thể cho từng category (đặc biệt đồ trẻ em)

→ Sau khi clear BLOCKERS 1-6 → chuyển sang **Tuần 2** (điền pipeline SOP: PRD → MER → FUL).
