# Quality Standards — Fulfillment & CX (ful)

**Dept:** 04-fulfillment-cx · **Version:** v1.0 · **Ngày:** 2026-06-23
**Nguyên tắc:** SLI quantifiable per SOP. **SLA external (khách) LESS strict hơn SLO nội bộ** (buffer an toàn). Vượt SLO → ăn error budget → RCA.

---

## Định nghĩa
- **SLI** (Service Level Indicator): chỉ số đo được.
- **SLO** (Objective): mục tiêu nội bộ (chặt hơn).
- **SLA** (Agreement): cam kết với khách/đối tác (lỏng hơn SLO → có đệm).
- **Error budget**: % cho phép vi phạm/tháng trước khi bắt buộc RCA.

---

## SOP-FUL-001 — Order Monitoring
| SLI | SLO (nội bộ) | SLA (external) | Error budget |
|---|---|---|---|
| Order verification time | ≤ 4h từ paid | — (internal) | 5% đơn/tháng |
| Verification coverage | 100% đơn paid/ngày | — | 0% (no leakage) |
| Exception detection accuracy | ≥ 98% | — | 2% |

## SOP-FUL-002 — Routing & Tracking
| SLI | SLO (nội bộ) | SLA (external khách) | Error budget |
|---|---|---|---|
| On-time routing | ≤ **18h** route | ≤ **24h** vào production | **2%** đơn/tháng |
| Avg routing time | ≤ 12h | — | — |
| Tracking sent | ≤ **6h** sau ship | ≤ **5 ngày** khách nhận tracking | 1% |
| Provider-region match | ≥ 99% | — | 1% |

> SLO route ≤18h chặt hơn SLA khách 24h → đệm 6h buffer cho exception.

## SOP-FUL-003 — Customer Support
| SLI | SLO (nội bộ) | SLA (external khách) | Error budget |
|---|---|---|---|
| First response time | ≤ **2h** | ≤ **4h** | 10% ticket/tháng |
| Resolution rate (24h) | ≥ 90% | — | 10% |
| CSAT | ≥ 4.0 | — | — |
| GDPR request | ≤ **20 ngày** | luật ≤ **30 ngày** | 0% |

> SLO first response 2h < SLA khách 4h; GDPR SLO 20 ngày < luật 30 ngày → buffer chống vi phạm pháp lý.

## SOP-FUL-004 — Returns & Refunds
| SLI | SLO (nội bộ) | SLA (external khách) | Error budget |
|---|---|---|---|
| Refund processing time | ≤ **24h** sau duyệt | ≤ **48h** khách nhận | 5% |
| Refund rate | ≤ 3% | — | vượt → RCA |
| Chargeback rate | ≤ 0.5% | — | — |
| Reprint-over-refund | ≥ 50% eligible | — | — |

---

## Error budget policy
- Tính theo **rolling 30 ngày**.
- On-time routing vượt 2%, refund vượt 3%, hoặc chargeback vượt 0.5% → **RCA bắt buộc** (5-why), update _rules/SOP.
- Burn budget nhanh (2 ngày) → freeze automation, OPC review.

## Liên kết
- KPI: [kpi_ful-001](./kpi_ful-001_fulfillment-kpis_v1.0_2026-06-23.md) · KRI: [kri_ful-001](./kri_ful-001_key-result-indicators_v1.0_2026-06-23.md)
- Cross-cutting: [_quality/](../_quality/README.md)

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo quality standards |
