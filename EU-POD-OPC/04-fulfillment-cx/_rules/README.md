# _rules — Fulfillment & CX

**Dept:** 04-fulfillment-cx · **Ngày:** 2026-06-23
Guardrails & decision rules cho order-ops AI + cx AI. (R trong KWSR)

---

## R1 — Route ≤24h SLA (hard gate)
- Mọi đơn verified PHẢI route sang Printify/PrintBase **≤24h kể từ paid_at** (SLO nội bộ ≤18h).
- Quá 24h → auto-alert OPC + ăn error budget (≤2%/tháng) + RCA nếu burn nhanh.
- Provider chọn đúng vùng: **US khách → US provider, EU khách → EU provider** (chỉ cross-region khi OOS).
- Không đóng đơn "fulfilled" nếu **chưa gửi tracking** cho khách.

## R2 — Refund Authority Threshold
| Trường hợp | Quyết bởi |
|---|---|
| Refund ≤ **$30** | cx AI tự duyệt |
| Refund > **$30** | **OPC approve** trước khi thực thi |
| Full-batch refund / reship hàng loạt | OPC |
| Chargeback/dispute | OPC + 05-backoffice |
- Ưu tiên **size exchange / reprint** trước refund khi eligible.
- Serial-refunder / fraud refund → flag + blocklist, OPC quyết.

## R3 — GDPR Data Handling
- **Minimization:** chỉ truy cập data cần để xử ticket/đơn.
- Quyền khách EU (access/rectification/erasure/portability) đáp ứng **≤30 ngày** (SLO 20 ngày).
- **Không xóa** data có nghĩa vụ lưu kế toán/VAT → phối 05-backoffice compliance (SOP-BCK-005).
- Không share/leak data khách giữa các ticket hay sang khách khác.
- Reply EN không vô tình lộ thông tin đơn/khách khác.

## R4 — Fraud / Hold
- Risk cao / billing-shipping mismatch / nhiều đơn cùng card / đơn > $150 → **hold + escalate OPC ≤12h**.
- Không bao giờ tự động route đơn fraud-hold sang print.

## R5 — Escalation Matrix
| Tình huống | Escalate đến | SLA |
|---|---|---|
| Fraud-hold | OPC | ≤12h |
| SLA route breach (>24h) | OPC | ngay |
| Refund > threshold | OPC | trước khi refund |
| Complaint pháp lý / chargeback | OPC + 05-backoffice | ≤24h |
| GDPR erasure request | cx AI → OPC → compliance | ≤30 ngày |
| Provider reject/OOS không giải được | OPC + 02-merchandising | ≤24h |

## R6 — Quality / Error Budget
- On-time routing ≤2%, refund ≤3%, chargeback ≤0.5% vi phạm/tháng → RCA bắt buộc + update rule/SOP.

→ Links: [SOP-FUL-002](../route-fulfillment/template/sop_ful-002_fulfillment-routing_v1.0_2026-06-23.md) · [Quality standards](../quality_ful-001_quality-standards_v1.0_2026-06-23.md) · [Charter](../charter_ful-department_v1.0_2026-06-23.md)

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo rules |
