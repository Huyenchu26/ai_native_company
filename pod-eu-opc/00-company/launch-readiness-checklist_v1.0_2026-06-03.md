# Launch Readiness Checklist — POD EU OPC

> Tổng hợp các điều kiện **bắt buộc** trước khi go-live ShopBase + Facebook Ads + Printify. Cập nhật trạng thái khi hoàn thành.

**Ngày:** 2026-06-08 · **Phase:** 1 (ShopBase + Facebook Ads + Printify)

---

## 🔴 BLOCKERS pháp lý & policy (không có → không được bán/chạy ads)

| # | Việc | SOP | Người | Trạng thái |
|---|---|---|---|---|
| 1 | Thiết lập **Responsible Person trong EU** + nhãn GPSR cho **đơn EU** (pháp nhân EU, hoặc dịch vụ RP của Printify/bên thứ ba) | SOP-BCK-004 | Founder | ☐ |
| 2 | Chốt **nước đăng ký kinh doanh** + trạng thái VAT | SOP-BCK-002 | Founder | ☐ |
| 3 | Quyết định **đăng ký OSS** (ngay hay chờ ngưỡng €10k) — tư vấn kế toán | SOP-BCK-002 | Founder + kế toán | ☐ |
| 4 | **Publish Privacy Notice** (GDPR) trên ShopBase | SOP-BCK-005 | Founder | ☐ |
| 5 | Ký/đối chiếu **DPA** với Klaviyo, helpdesk, Printify, Meta | SOP-BCK-005 | Founder | ☐ |
| 6 | Lập kênh tiếp nhận **yêu cầu chủ thể dữ liệu** (truy cập/xóa) | SOP-BCK-005 | Founder | ☐ |
| 7 | **Meta Ad Policy compliance** + cấu trúc BM chống ban (Master BM không chạy ads) | SOP-BCK-004 / SOP-GRW-002 | Founder | ☐ |

## 🟡 Vận hành (cần để chạy pipeline — Tuần 2-3)

| # | Việc | SOP | Trạng thái |
|---|---|---|---|
| 8 | Tài khoản ShopBase + Printify + Meta Business Manager, kết nối (keys để **ngoài git**) | channel-config | ☐ |
| 9 | **ShopBase Pixel + CAPI** — verify fire đúng events (ViewContent/AddToCart/InitiateCheckout/Purchase) | SOP-GRW-002 | ☐ |
| 10 | Chọn **print provider** Printify (US + EU: Latvia/UK/DE) cho AOP leggings | SOP-MER-002 | ☐ |
| 11 | Chốt **niche khởi đầu** (Golden Retriever, French Bulldog, Corgi, Dachshund) + tiêu chí | SOP-PRD-001/002 | ☐ |
| 12 | Điền pricing floor (gross margin ~45–55%) + cấu hình upsell sports bra/bundle | SOP-MER-003 | ☐ |
| 13 | Bảng thuế suất VAT theo nước EU (knowledge) | SOP-BCK-002 | ☐ |

## ✅ Đã xong (Tuần 1 — Foundation)

- [x] Folder structure 5 department + `_shared` / `_quality` / `_ai-workforce`
- [x] Company charter, vision/mission, business strategy, OKR (pivot ShopBase + FB Ads)
- [x] 5 department README + charter
- [x] **3 SOP compliance chi tiết:** VAT/OSS (BCK-002), GPSR đơn EU (BCK-004), GDPR (BCK-005)
- [x] Backoffice Quality Standards + hard rules

---

## Hạng mục cần tư vấn chuyên môn (không tự quyết)
> AI/SOP chỉ chuẩn bị; các mục này cần **kế toán thuế EU** và/hoặc **tư vấn pháp lý**:
- Cấu trúc pháp nhân & nơi đăng ký (ảnh hưởng VAT/OSS, RP cho đơn EU)
- Phạm vi nghĩa vụ VAT US sales tax cho từng bang (đơn US)
- Yêu cầu GPSR cụ thể cho category apparel (đơn EU)
- IP/TM tên breed (tránh breed name đã đăng ký trademark)

→ Sau khi clear BLOCKERS 1-7 → chuyển sang **Tuần 2** (điền pipeline SOP: PRD → MER → GRW → FUL).
