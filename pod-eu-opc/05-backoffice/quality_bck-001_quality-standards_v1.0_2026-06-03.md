# Quality Standards: Backoffice (SLI / SLO / SLA)

> Error Budget = 100% − SLO. Còn <25% → FREEZE changes, focus quality. Các SLO compliance dưới đây = 100% (rào pháp lý, error budget = 0).

## Compliance SOPs (Tuần 1 — ưu tiên cao nhất)

| SOP Code | Nghiệp vụ | SLI | SLO | SLA | Error Budget | Measurement |
|---|---|---|---|---|---|---|
| SOP-BCK-002 | VAT/OSS — đối soát đơn | % đơn report khớp API | 100% | — | 0% | Count(API)=Count(report) |
| SOP-BCK-002 | VAT/OSS — map thuế suất | % đơn gán đúng VAT nước | 100% | — | 0% | 0 đơn unmapped |
| SOP-BCK-002 | VAT/OSS — nộp đúng hạn | tờ khai ≤ deadline | 100% | hạn cơ quan thuế | 0% | Ngày nộp ≤ hạn−1 |
| SOP-BCK-004 | GPSR — Responsible Person | % SKU có RP hợp lệ | 100% | — | 0% | RP record |
| SOP-BCK-004 | GPSR — đủ nhãn | % SKU đủ 5 yêu cầu | 100% | — | 0% | Checklist auto |
| SOP-BCK-004 | GPSR — audit coverage | % listing active audit/tháng | 100% | — | 0% | Audit report |
| SOP-BCK-005 | GDPR — yêu cầu chủ thể | % xử lý ≤ 1 tháng | 100% | 1 tháng (luật) | 0% | Request log |
| SOP-BCK-005 | GDPR — breach notify | thời gian phát hiện→báo | ≤ 72h | 72h (luật) | 0% | Breach log |
| SOP-BCK-005 | GDPR — processor DPA | % processor có DPA | 100% | — | 0% | Processor list |

## Financial SOPs

| SOP Code | Nghiệp vụ | SLI | SLO | SLA | Error Budget | Measurement |
|---|---|---|---|---|---|---|
| SOP-BCK-001 | Bookkeeping | Financial accuracy | ≥ 99% | — | 1% | Reconciliation |
| SOP-BCK-003 | Financial report | Báo cáo tháng đúng hạn | trước ngày 5 | — | — | Calendar |
| SOP-BCK-006 | AI workforce | AI worker uptime | ≥ 99% | — | 1% | Monitoring |

> ⚠️ Mọi SLI compliance miss → **dừng publish/giao dịch liên quan** + Incident Report ngay (không chờ đủ 3 loop).
