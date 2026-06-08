# Quality Standards: Backoffice (SLI / SLO / SLA)
> Cập nhật: 2026-06-08 · Platform: ShopBase + Facebook Ads · Niche: Dog Breed AOP Leggings · Market: US + EU

> Error Budget = 100% − SLO. Còn <25% → FREEZE changes, focus quality. Các SLO compliance dưới đây = 100% (rào pháp lý/chống ban, error budget = 0).

## Compliance SOPs (ưu tiên cao nhất)

| SOP Code | Nghiệp vụ | SLI | SLO | SLA | Error Budget | Measurement |
|---|---|---|---|---|---|---|
| SOP-BCK-004 | Meta Ad Policy — creative pass trước chạy | % creative pass | 100% | — | 0% | Policy review log |
| SOP-BCK-004 | GPSR — Responsible Person (đơn EU) | % SKU EU có RP hợp lệ | 100% | — | 0% | RP record |
| SOP-BCK-004 | GPSR — đủ nhãn (đơn EU) | % SKU đủ 5 yêu cầu | 100% | — | 0% | Checklist auto |
| SOP-BCK-004 | IP/TM — breed check | % listing được check TM | 100% | — | 0% | TM search log |
| SOP-BCK-004 | GPSR — audit coverage | % listing EU active audit/tháng | 100% | — | 0% | Audit report |
| SOP-BCK-002 | VAT/OSS — đối soát đơn | % đơn report khớp API | 100% | — | 0% | Count(API)=Count(report) |
| SOP-BCK-002 | VAT/OSS — map thuế suất | % đơn EU gán đúng VAT nước | 100% | — | 0% | 0 đơn unmapped |
| SOP-BCK-002 | VAT/OSS — nộp đúng hạn | tờ khai ≤ deadline | 100% | hạn cơ quan thuế | 0% | Ngày nộp ≤ hạn−1 |
| SOP-BCK-005 | GDPR — yêu cầu chủ thể | % xử lý ≤ 1 tháng | 100% | 1 tháng (luật) | 0% | Request log |
| SOP-BCK-005 | GDPR — breach notify | thời gian phát hiện→báo | ≤ 72h | 72h (luật) | 0% | Breach log |
| SOP-BCK-005 | GDPR — consent marketing | % email gửi có opt-in | 100% | — | 0% | Opt-in records |
| SOP-BCK-005 | GDPR — processor DPA | % processor có DPA | 100% | — | 0% | Processor list |

## Financial & Ops SOPs

| SOP Code | Nghiệp vụ | SLI | SLO | SLA | Error Budget | Measurement |
|---|---|---|---|---|---|---|
| SOP-BCK-001 | Bookkeeping | Financial accuracy | ≥ 99% | — | 1% | Reconciliation |
| SOP-BCK-003 | Financial report (P&L + profit/SKU + ROAS/CPA) | Báo cáo tháng đúng hạn | trước ngày 5 | — | — | Calendar |
| SOP-BCK-006 | AI workforce (12 worker) | AI worker uptime | ≥ 99% | — | 1% | Monitoring |

> ⚠️ Mọi SLI compliance miss → **dừng publish/ads/giao dịch liên quan** + Incident Report ngay (không chờ đủ 3 loop). GATE cứng: Meta Ad Policy → no ads; GPSR (đơn EU) → no publish.
