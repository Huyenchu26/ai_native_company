# KRI — Fulfillment & CX (ful)

**Dept:** 04-fulfillment-cx · **Version:** v1.0 · **Ngày:** 2026-06-23
**KRI = Key *Risk* Indicators** — tín hiệu sớm cảnh báo rủi ro vận hành (leading), khác KPI (lagging performance).

---

## Risk Indicators
| KRI | Định nghĩa | Ngưỡng cảnh báo (amber) | Ngưỡng đỏ (red) | Owner | SOP |
|---|---|---|---|---|---|
| `ontime_routing_breach` | % đơn route > 24h | > 2% | > 5% | order-ops AI | FUL-002 |
| `unverified_aging` | # đơn paid chưa verify > 24h | ≥ 1 | ≥ 5 | order-ops AI | FUL-001 |
| `provider_reject_rate` | % đơn provider reject/OOS | > 3% | > 7% | order-ops AI | FUL-002 |
| `production_delay_rate` | % đơn quá ngưỡng production | > 5% | > 10% | order-ops AI | FUL-002 |
| `tracking_gap` | % đơn ship chưa gửi tracking >12h | > 1% | > 5% | order-ops AI | FUL-002 |
| `first_response_breach` | % ticket quá 2h first response | > 10% | > 25% | cx AI | FUL-003 |
| `csat_drop` | CSAT trung bình | < 4.2 | < 4.0 | cx AI | FUL-003 |
| `refund_rate_spike` | refunds/orders | > 3% | > 5% | cx AI | FUL-004 |
| `chargeback_rate` | chargebacks/orders | > 0.3% | > 0.5% | cx AI / OPC | FUL-004 |
| `fraud_hold_backlog` | # đơn fraud-hold chờ OPC | ≥ 3 | ≥ 10 | OPC | FUL-001 |
| `gdpr_request_aging` | # GDPR request gần hạn 30 ngày | còn ≤ 7 ngày | quá hạn | cx AI | FUL-003 |

---

## Eskalation khi RED
1. KRI red → auto-alert OPC + freeze automation liên quan nếu cần.
2. RCA bắt buộc trong 48h (đặc biệt `ontime_routing_breach`, `refund_rate_spike`, `chargeback_rate`).
3. Cập nhật rule/SOP để diệt root cause → log vào _rules.

## Liên kết
- Company KRI: [00-company/kri](../00-company/kri_company-001_company-kri_v1.0_2026-06-23.md)
- KPI: [kpi_ful-001](./kpi_ful-001_fulfillment-kpis_v1.0_2026-06-23.md) · Quality: [quality_ful-001](./quality_ful-001_quality-standards_v1.0_2026-06-23.md)

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo KRI |
