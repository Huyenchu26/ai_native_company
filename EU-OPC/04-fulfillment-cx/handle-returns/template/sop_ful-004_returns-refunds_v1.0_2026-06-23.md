# SOP-FUL-004 — Returns, Refunds & Complaints

**Dept:** 04-fulfillment-cx (ful) · **Layer:** L2 · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-fulfillment-cx` `[AI WORKFORCE]`
**Upstream:** SOP-FUL-003 (refund/return ticket) · **Downstream:** 05-backoffice (refund/cost data)

---

## 0. IPO
| | |
|---|---|
| **Input** | Return/refund/complaint request (từ SOP-FUL-003), order + payment context, defect evidence, GDPR-relevant data |
| **Process** | Xác minh đủ điều kiện → quyết hướng xử lý (refund/reprint/partial) trong authority → thực thi → log |
| **Output** | Refund executed / reprint order / resolution + refund-cost data → 05-backoffice |

---

## 1. Tổng quan
POD = **made-to-order**, không có inventory → chính sách returns khác retail: **không nhận hàng về** (cost-ineffective). Refund/reprint chỉ khi defect, lỗi print, lost in transit, hoặc thiện chí giữ rating. Mục tiêu giữ **refund rate thấp** mà vẫn giữ CSAT ≥4.0. Mọi refund tuân **authority threshold** (auto vs OPC approve) và xử lý data khách theo GDPR.

---

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Xác minh điều kiện refund | cx AI | OPC | order-ops AI | — |
| Refund ≤ threshold ($30) | cx AI | OPC | — | 05-backoffice |
| Refund > threshold ($30) / full-batch | OPC | OPC | cx AI | 05-backoffice |
| Reprint (defect/lỗi print) | cx AI | OPC | order-ops AI (re-route) | provider |
| Complaint pháp lý / chargeback | OPC | OPC | cx AI, 05-backoffice | — |

`[AI WORKFORCE]` cx AI **tự duyệt refund ≤ $30**; mọi refund **> $30** cần OPC approve.

---

## 3. Quy trình (ICOM)
**Bước 1 — Xác minh (I:request + evidence · C:return/refund policy + GDPR · O:đủ/không đủ điều kiện · M:cx AI)**
Phân loại lý do: defect / wrong-item / lost / not-as-described / buyer-remorse. Yêu cầu ảnh nếu defect.

**Bước 2 — Quyết hướng xử lý**
- Defect/lỗi print/lost → **reprint free** (ưu tiên) hoặc refund.
- Wrong size do khách chọn → ưu tiên **size exchange** (SOP-FUL-003) thay vì refund.
- Buyer-remorse → tùy giá trị, ưu tiên giữ rating nhưng không lạm refund.

**Bước 3 — Check authority threshold** Refund **≤ $30** → cx AI tự thực thi. **> $30** → escalate OPC approve trước khi refund.

**Bước 4 — Thực thi** Refund qua ShopBase/payment gateway HOẶC tạo reprint order (phối order-ops AI re-route). Gửi email xác nhận EN cho khách.

**Bước 5 — Log & handoff** Ghi resolution + refund amount + lý do. Đẩy refund/cost data → 05-backoffice (P&L, chargeback tracking). GDPR: chỉ lưu data cần cho nghĩa vụ kế toán.

---

## 4. Phân nhánh (Exception)
- **4.A Defect có bằng chứng:** reprint free; refund nếu khách từ chối reprint.
- **4.B Lost in transit:** xác nhận với carrier (SOP-FUL-002 4.E) → reship hoặc refund.
- **4.C Refund > $30 (authority threshold):** hold → OPC approve → thực thi; log lý do.
- **4.D Chargeback/dispute từ ngân hàng:** escalate OPC + 05-backoffice; chuẩn bị evidence (tracking, ToS, comms) phản hồi gateway.
- **4.E Khách lạm dụng (serial refunder / fraud refund):** flag, OPC quyết từ chối; ghi blocklist.
- **4.F Đơn EU — quyền rút lui (14-day withdrawal) theo luật tiêu dùng:** Ranh giới phải phân biệt rõ:
  - **Miễn trừ withdrawal right:** Sản phẩm AOP custom-printed / made-to-order (in theo breed + cá nhân hóa cho khách) thuộc diện **miễn trừ quyền rút lui 14 ngày** theo **EU Directive 2011/83/EU, Art.16(c)** ("goods made to the consumer's specifications or clearly personalized"). → Khách **không** có quyền trả hàng đổi ý (buyer-remorse) đối với hàng custom. Phải nêu rõ điều khoản này tại checkout/policy trước khi khách đặt.
  - **VẪN bắt buộc refund/reprint:** Miễn trừ withdrawal **KHÔNG** loại bỏ nghĩa vụ pháp lý về **conformity/defect**. Khi sản phẩm **defect, lỗi print, sai sản phẩm (wrong/not-as-described), hư hỏng, lost in transit** → vẫn **bắt buộc refund hoặc reprint** theo quyền bảo hành/đúng hợp đồng của khách (EU consumer rights). → Defect/sai SP luôn xử lý như nhánh 4.A/4.B/4.D bất kể đã qua 14 ngày hay là hàng custom.
  - Phối compliance (SOP-BCK-005) khi có tranh chấp ranh giới buyer-remorse vs defect.

---

## 5. Checklist — Quality Gate
**SLI / SLO / SLA**
| SLI | SLO (nội bộ) | SLA (external khách) | Đo |
|---|---|---|---|
| Refund processing time | ≤ 24h sau khi duyệt | ≤ 48h | executed − approved |
| Refund rate | ≤ 3% đơn | — | refunds/orders |
| Reprint-over-refund ratio | ≥ 50% case eligible | — | reprint/(reprint+refund) |
| CSAT post-resolution | ≥ 4.0 | — | survey |
| Chargeback rate | ≤ 0.5% | — | chargebacks/orders |

**Error budget:** refund rate vượt 3%/tháng → RCA bắt buộc (truy nguyên: size, defect provider, ad expectation gap).

**Prevention**
- [ ] Mọi refund > $30 có OPC approval log
- [ ] Defect refund/reprint có evidence đính kèm
- [ ] Refund/cost data đã đẩy 05-backoffice
- [ ] GDPR: không giữ data quá nghĩa vụ; serial-refunder được flag
- [ ] Ưu tiên size exchange/reprint trước refund khi eligible

---

## 6. Tài nguyên & Links
- Upstream: [SOP-FUL-003](../../support-customer/template/sop_ful-003_cx-support_v1.0_2026-06-23.md)
- [Returns/refund policy + authority threshold](../../_rules/README.md)
- Reprint re-route: [SOP-FUL-002](../../route-fulfillment/template/sop_ful-002_fulfillment-routing_v1.0_2026-06-23.md)
- Refund data: 05-backoffice (SOP-BCK-001/003) · GDPR: SOP-BCK-005

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
