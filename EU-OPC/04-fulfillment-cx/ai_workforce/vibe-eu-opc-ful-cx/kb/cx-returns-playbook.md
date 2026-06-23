# CX & Returns Playbook — DAKOfits (EN, US/EU)

Nguồn: SOP-FUL-003 (support-customer) + SOP-FUL-004 (returns/refunds). Sản phẩm: POD AOP
leggings/activewear đa-niche, made-to-order, **KHÔNG thu hồi hàng**.

## 1. Ticket Taxonomy
| type | Mô tả | First action |
|---|---|---|
| **WISMO** | Where-is-my-order | Tra tracking + ETA (data từ order-ops); nếu tracking đứng → mở carrier case |
| **size** | Fit/size question (XS–3XL) | Tư vấn theo size chart; nếu sai → size exchange |
| **defect** | Lỗi print / hư hỏng | Yêu cầu ảnh chứng minh → reprint free |
| **refund** | Yêu cầu hoàn tiền | Kiểm authority threshold $30 |
| **GDPR** | DSAR access/erasure/rectification | Xác thực danh tính → phối compliance |

Mọi ticket: tag `type` + `priority`. Complaint nặng / dọa chargeback / review xấu → escalate OPC ngay.

## 2. Reprint-first Ladder
POD made-to-order → returns khác retail (không nhận hàng về vì cost-ineffective).
1. **Wrong size (khách chọn nhầm)** → **size exchange** XS–3XL (free first exchange). Khách giữ hàng cũ.
2. **Defect / lỗi print / lost in transit** → **reprint free** (ưu tiên). Refund chỉ khi khách từ chối reprint.
3. **Refund** = phương án cuối. Mục tiêu reprint-over-refund ratio ≥50%, refund rate ≤3%.

## 3. Refund $30 Authority Gate
- **≤ $30** → cx AI **tự duyệt** (`refund_auto_approved=true`), thực thi qua ShopBase/payment gateway.
- **> $30** → **HOLD → escalate OPC** approve trước (`refund_auto_approved=false`, `need_review=true`).
- Refund processing ≤24h sau duyệt (SLA ≤48h). Log refund + lý do → đẩy finance (P&L).
- Mọi refund >$30 phải có OPC approval log; defect refund/reprint phải có evidence đính kèm.

## 4. Chargeback / Dispute
- Escalate OPC + finance. Chuẩn bị evidence pack: tracking, ToS/policy, comms history → phản hồi gateway.
- Chargeback rate target ≤0.5%. Serial-refunder / fraud → flag blocklist, OPC quyết từ chối.

## 5. EU 14-day Withdrawal — Art.16(c)
- **Miễn trừ:** hàng AOP custom/made-to-order → **miễn quyền rút lui 14 ngày** (EU Dir 2011/83/EU,
  **Art.16(c)**). Khách KHÔNG được trả vì buyer-remorse. Nêu rõ tại checkout/policy.
- **Ngoại lệ bắt buộc:** **defect / wrong / not-as-described / lost** → **vẫn refund hoặc reprint**
  (conformity rights), bất kể 14 ngày hay hàng custom. Xử như nhánh defect/lost.
- Tranh chấp ranh giới buyer-remorse vs defect → phối compliance (SOP-BCK-005).

## 6. GDPR DSAR
- access/erasure/rectification: xác thực danh tính → phối compliance → **SLO nội bộ ≤20 ngày**
  (luật ≤30, buffer 10 ngày). KHÔNG xóa data có nghĩa vụ lưu (kế toán). Log riêng + báo compliance.
- Reply EN không lộ data khách khác. Printify = data processor (DPA), chỉ data tối thiểu.

## 7. SLO/SLA tóm tắt
| SLI | SLO | SLA |
|---|---|---|
| First response | ≤2h | ≤4h |
| Resolution | ≥90% / 24h | — |
| CSAT | ≥4.0 | — |
| Refund processing | ≤24h sau duyệt | ≤48h |
| Refund rate | ≤3% | — |
| Chargeback rate | ≤0.5% | — |
| GDPR DSAR | ≤20 ngày | ≤30 ngày |
