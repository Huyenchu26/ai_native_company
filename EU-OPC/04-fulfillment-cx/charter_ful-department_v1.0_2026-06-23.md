# Charter — Fulfillment & CX (ful)

**Dept:** 04-fulfillment-cx · **Layer:** L2 Operations · **Version:** v1.0 · **Ngày:** 2026-06-23
**Owner (A):** OPC · **AI Workforce:** order-ops AI, cx AI

---

## Mission
Biến mỗi đơn từ Facebook Ads thành **trải nghiệm giao hàng on-time + support EN xuất sắc** cho khách US/EU, với chi phí ngoại lệ thấp nhất — giữ rating cao để bảo vệ ad account và LTV, đồng thời feed cost/refund data sạch cho 05-backoffice.

## Scope (trong phạm vi)
- Monitor & verify đơn ShopBase (payment, address, fraud, SKU/variant XS–3XL).
- Route Printify/PrintBase (US+EU) **≤24h**, theo dõi production, gửi tracking.
- Support EN: WISMO, size exchange XS–3XL, defect, address change.
- Returns / refunds / complaints / chargebacks theo authority threshold.
- Tuân thủ GDPR khi xử lý data khách.

## Out of scope
- Tạo/publish product, pricing, design → 01/02.
- Chạy ads, traffic → 03-growth.
- Bookkeeping, VAT, P&L, GPSR/compliance gốc → 05-backoffice (ful chỉ feed data).

## Boundaries / Handoff
- **Upstream:** 03-growth → đơn paid trên ShopBase.
- **Downstream:** 05-backoffice ← print/ship cost, refund, chargeback, fee.
- **Lateral:** 02-merchandising (SKU↔provider mapping, OOS variant).

## Authority
- order-ops AI: tự verify + route + gửi tracking (rule-based).
- cx AI: tự xử ticket + refund **≤ $30**; size exchange free first.
- OPC: refund **> $30**, fraud hold/cancel, complaint pháp lý, GDPR erasure.

## Mục tiêu (đóng góp Company O2)
On-time routing ≥98% · CSAT ≥4.0 · resolution rate ≥90% · first response ≤2h · refund ≤3%.

## AI Workforce
| Worker | SOP | Output |
|---|---|---|
| `vibe-opc-pod-fulfillment-order-ops` | FUL-001/002 | orders in production + tracking |
| `vibe-opc-pod-fulfillment-cx` | FUL-003/004 | ticket resolved + resolution log |

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo charter |
