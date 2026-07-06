# Quality Standards — 01-Product Studio · Q3 2026

**Ngày:** 2026-06-23 · **Dept:** prd

> SLI = chỉ số đo được; SLO = mục tiêu; SLA = cam kết downstream (nếu có); Error Budget = phần được phép lỗi. SLI operational KHÔNG đặt 100% (trừ gate compliance).

---

## SLI/SLO theo SOP

| SOP | SLI (quantifiable) | SLO | SLA (downstream) | Error Budget | Measurement |
|-----|--------------------|-----|------------------|--------------|-------------|
| PRD-001 | % niche audience ≥ 500k | ≥ 90% | — | 10% | Meta Audience export / tuần |
| PRD-001 | # niche validated/tuần | ≥ 3 | feed 02-merch | — | Đếm output file |
| PRD-001 | IP pre-flag coverage | 100% | — | 0% (gate-feed) | Pre-flag log |
| PRD-002 | % design xong trước seasonal deadline | ≥ 95% | calendar cho 02-merch | 5% | Date diff |
| PRD-002 | Rolling horizon lịch | ≥ 12 tuần | — | — | Calendar audit |
| PRD-003 | % design ≥ 300 DPI | 100% | print-ready cho provider | 0% (kỹ thuật) | File metadata |
| PRD-003 | % design pass AOP 360° (no seam) | ≥ 98% | — | 2% | QC report |
| PRD-003 | Design turnaround time | ≤ 24h | handoff ≤ 24h | — | Timestamp delta |
| PRD-004 | % SP cleared trước listing | **100%** (gate cứng) | chỉ CLEAR → 02-merch | 0% | Clearance log vs catalog |
| PRD-004 | Dual-market lookup (USPTO+EUIPO) | 100% | — | 0% | Log dual-source |
| PRD-004 | Clearance turnaround time | ≤ 12h | — | — | Timestamp delta |
| PRD-004 | TM takedown rate (đo lùi) | ≤ 1% | — | 1% | Takedown register |

## Error Budget Policy
- Khi SLI operational vượt budget (vd AOP 360° < 98% trong tuần): freeze tính năng mới của SOP đó, ưu tiên RCA template seamless/mockup.
- Gate compliance (PRD-004 clearance, PRD-003 300 DPI) **không có budget** — vi phạm = dừng handoff ngay.

## Quy trình đo & review
| Tần suất | Việc |
|----------|------|
| Per design | Log DPI, AOP 360°, turnaround, clearance status |
| Weekly | Tổng hợp SLI vs SLO, cập nhật KRI dashboard |
| Per batch | Seasonal deadline hit, takedown register |

## Liên kết
- [KPI](./kpi_prd-001_product-kpis_v1.0_2026-06-23.md) · [KRI](./kri_prd-001_key-result-indicators_v1.0_2026-06-23.md) · [Rules](./_rules/README.md)
- Cross-cutting: [../_quality/README.md](../_quality/README.md)
