# KPI — Fulfillment & CX (ful)

**Dept:** 04-fulfillment-cx · **Version:** v1.0 · **Ngày:** 2026-06-23
**KPI = lagging performance metrics** (per SOP). Review: weekly.

---

## Order-Ops KPI (FUL-001/002)
| KPI | Định nghĩa | Target | Tần suất | Source |
|---|---|---|---|---|
| On-time routing rate | % đơn route ≤24h (routed_at − paid_at) | **≥ 98%** | daily | ShopBase + Printify |
| Avg routing time | trung bình routed_at − paid_at | **≤ 12h** | daily | order-ops log |
| Verification coverage | % đơn paid verify trong ngày | **100%** | daily | FUL-001 log |
| Provider-region match | % US→US, EU→EU | **≥ 99%** | weekly | routing log |
| Tracking sent rate | % đơn ship gửi tracking ≤12h | **≥ 99%** | daily | FUL-002 log |
| Fulfillment-to-ship time | paid_at → fulfilled (provider ship) | ≤ 5 ngày (US/EU) | weekly | provider |

## CX KPI (FUL-003/004)
| KPI | Định nghĩa | Target | Tần suất | Source |
|---|---|---|---|---|
| First response time | reply − ticket_created | **≤ 2h** (SLA khách ≤4h) | daily | helpdesk |
| Resolution rate | % ticket resolved ≤24h | **≥ 90%** | daily | helpdesk |
| CSAT | survey post-resolution | **≥ 4.0 / 5** | weekly | survey |
| Size exchange rate | % đơn có size exchange | ≤ 5% (theo dõi, không phạt) | weekly | FUL-003 log |
| Refund rate | refunds / orders | **≤ 3%** | weekly | ShopBase + FUL-004 |
| Reprint-over-refund ratio | reprint / (reprint+refund) eligible | ≥ 50% | weekly | FUL-004 log |
| Chargeback rate | chargebacks / orders | **≤ 0.5%** | monthly | gateway |
| GDPR request SLA | % request đáp ứng ≤30 ngày | 100% | monthly | FUL-003 log |

---

## Dashboard cadence
- **Daily:** on-time routing, verification coverage, first response, tracking gap.
- **Weekly:** CSAT, refund rate, resolution rate → feed weekly report 05-backoffice ops-hr.
- **Monthly:** chargeback, GDPR SLA.

## Liên kết
- KRI (leading risk): [kri_ful-001](./kri_ful-001_key-result-indicators_v1.0_2026-06-23.md)
- Quality (SLI/SLO/SLA): [quality_ful-001](./quality_ful-001_quality-standards_v1.0_2026-06-23.md)
- Company KPI: [00-company/kpi](../00-company/kpi_strat-001_company-kpis_v1.0_2026-06-23.md)

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo KPI |
