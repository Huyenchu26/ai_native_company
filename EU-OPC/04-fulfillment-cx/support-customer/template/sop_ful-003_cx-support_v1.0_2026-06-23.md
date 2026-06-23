# SOP-FUL-003 — Customer Support (EN, US/EU)

**Dept:** 04-fulfillment-cx (ful) · **Layer:** L2 · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-fulfillment-cx` `[AI WORKFORCE]`
**Upstream:** SOP-FUL-001/002 (order/exception data) · **Downstream:** SOP-FUL-004 (returns), 05-backoffice (refund data)

---

## 0. IPO
| | |
|---|---|
| **Input** | Customer ticket (email/ShopBase helpdesk/FB inbox), order context, size chart XS–3XL, GDPR-relevant data khách |
| **Process** | Phân loại ticket → tra cứu order → trả lời EN ≤2h → xử lý size exchange / WISMO / complaint → escalate nếu cần |
| **Output** | Ticket resolved + resolution log + (nếu cần) size exchange order / refund request → SOP-FUL-004 |

---

## 1. Tổng quan
Hỗ trợ khách US/EU **bằng tiếng Anh**, giữ rating cao (CSAT ≥4.0). Loại ticket phổ biến POD: **WISMO** (where-is-my-order), **size exchange** (XS–3XL, AOP legging chạy form nên fit-question nhiều), product defect, address change, cancel/refund. Mọi xử lý dữ liệu khách phải **tuân thủ GDPR** (chỉ dùng data tối thiểu, không share ngoài, đáp ứng quyền access/erasure trong **SLO ≤20 ngày**; mốc luật ≤30 ngày). Printify là data processor (có DPA), chỉ nhận data tối thiểu. First response ≤2h (nội bộ), SLA cam kết với khách ≤4h.

---

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Phân loại & trả lời ticket EN | cx AI | OPC | — | — |
| Size exchange XS–3XL | cx AI | OPC | order-ops AI (re-route) | khách |
| WISMO (tra tracking) | cx AI | OPC | order-ops AI | khách |
| Complaint nặng / rating risk | cx AI | OPC | OPC | — |
| GDPR data request (access/erasure) | cx AI | OPC | 05-backoffice (compliance) | khách |

`[AI WORKFORCE]` cx AI tự xử ticket rule-based + template EN; escalate OPC khi complaint pháp lý, refund > threshold, hoặc GDPR erasure request.

---

## 3. Quy trình (ICOM)
**Bước 1 — Phân loại (I:ticket · C:taxonomy + GDPR policy · O:ticket type · M:cx AI)**
Tag: WISMO / size-exchange / defect / address / cancel / refund / other. Gắn priority.

**Bước 2 — Tra cứu order context** Pull order từ ShopBase + tracking/production status (từ SOP-FUL-002). Chỉ truy cập data cần thiết (GDPR minimization).

**Bước 3 — Trả lời EN ≤2h** Dùng template EN phù hợp tone US/EU. WISMO → gửi tracking + ETA. Size question → tư vấn theo size chart XS–3XL.

**Bước 4 — Hành động** Size exchange → tạo replacement order, phối order-ops AI re-route (SOP-FUL-002). Defect → reprint. Refund/return → chuyển SOP-FUL-004.

**Bước 5 — Đóng ticket & log** Ghi resolution log (type, action, time-to-resolve, CSAT nếu có). GDPR request → log riêng + báo compliance.

---

## 4. Phân nhánh (Exception)
- **4.A Size không vừa (exchange):** xác nhận size mới theo chart XS–3XL → replacement order (thường free first exchange) → re-route. Khách giữ sản phẩm cũ (POD không thu hồi).
- **4.B WISMO — đơn chậm/lost:** nếu tracking đứng → mở case carrier (SOP-FUL-002 4.E); báo khách ETA hoặc reship.
- **4.C Product defect (ảnh chứng minh):** request reprint free từ provider; gửi khách ETA; xin lỗi + giữ rating.
- **4.D Complaint nặng / dọa chargeback / review xấu:** escalate OPC ngay; ưu tiên giải pháp giữ rating.
- **4.E GDPR request (access/erasure/rectification):** xác thực danh tính khách → phối 05-backoffice compliance → đáp ứng **SLO nội bộ ≤20 ngày** (mốc luật/SLA ≤30 ngày — giữ buffer 10 ngày cho xác minh/escalation); không tự xóa data có nghĩa vụ lưu (kế toán).
- **4.G Data processor (Printify):** Printify là **data processor**, đã ký **DPA**; chỉ gửi data **tối thiểu** cho mục đích fulfillment (tên, địa chỉ ship, line item) — không gửi data thừa.
- **4.F Refund yêu cầu:** chuyển SOP-FUL-004 (kiểm authority threshold).

---

## 5. Checklist — Quality Gate
**SLI / SLO / SLA**
| SLI | SLO (nội bộ) | SLA (external khách) | Đo |
|---|---|---|---|
| First response time | ≤ 2h | ≤ 4h | reply − ticket_created |
| Resolution rate | ≥ 90% trong 24h | — | resolved/total |
| CSAT | ≥ 4.0 / 5 | — | survey sau resolve |
| GDPR DSAR đúng hạn | 100% **≤ 20 ngày** (SLO nội bộ) | luật/SLA ≤ 30 ngày | đáp ứng/requests |

**Error budget:** ≤10% ticket được phép quá first-response 2h/tháng.

**Prevention**
- [ ] Mọi ticket có tag type + priority
- [ ] Reply EN không lộ data khách khác (GDPR)
- [ ] Size exchange xác nhận size theo chart trước khi tạo order
- [ ] Complaint rating-risk được escalate, không để tự đóng
- [ ] GDPR request log đầy đủ + thông báo compliance

---

## 6. Tài nguyên & Links
- [ShopBase Helpdesk + size chart XS–3XL KB](../../_knowledge/README.md)
- Returns: [SOP-FUL-004](../../handle-returns/template/sop_ful-004_returns-refunds_v1.0_2026-06-23.md)
- Order/tracking: [SOP-FUL-002](../../route-fulfillment/template/sop_ful-002_fulfillment-routing_v1.0_2026-06-23.md)
- GDPR: [_rules — GDPR data handling](../../_rules/README.md) · 05-backoffice compliance (SOP-BCK-005)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
