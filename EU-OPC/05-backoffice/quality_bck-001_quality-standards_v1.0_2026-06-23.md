# Quality Standards — 05-Backoffice (bck)

**Version:** v1.0 · **Ngày:** 2026-06-23
> SLI = chỉ số đo · SLO = mục tiêu nội bộ · SLA = cam kết với stakeholder. Compliance SLO = **100%** (gate cứng legal, error budget 0%).

---

## SLI/SLO/SLA mỗi SOP

### SOP-BCK-001 Bookkeeping
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| Bookkeeping accuracy | ≥ 99.9% | Ledger chính xác cho P&L/VAT | ≤ 0.1% giao dịch/kỳ |
| Fee reconciliation coverage | 100% | Mọi statement đối soát | 0% bỏ sót |
| Month-end close | ≤ ngày 5 | Khóa sổ cho brief | 1 ngày trễ/quý |

### SOP-BCK-002 Profit/ROAS
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| Profit calc accuracy | ≥ 99% | Quyết định scale/kill đúng | ≤ 1% lệch |
| FX traceability | 100% | Mọi figure có nguồn+ngày | 0% bịa số |
| CEO brief on-time | 100% (≤ ngày 6) | Owner có brief đúng hạn | 1 trễ/quý |

### SOP-BCK-003 VAT OSS/IOSS
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| VAT filing on-time | **100%** | Nộp đúng deadline OSS/IOSS | **0%** (legal) |
| VAT rate accuracy | 100% | Đúng rate nước đến | 0% sai rate |
| OSS/IOSS phân loại | ≥ 99.5% | Scheme đúng | ≤ 0.5% mẫu |

### SOP-BCK-004 GPSR `[GATE CỨNG]`
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| GPSR clearance rate | **100%** | No clearance → no publish EU | **0%** (legal) |
| Responsible Person present | 100% | RP hợp lệ mỗi SP EU | 0% |
| IP/TM clearance | 100% | Không trùng nhãn hiệu | 0% |
| Nhãn an toàn đầy đủ | 100% | Đủ trường GPSR | 0% |

### SOP-BCK-005 GDPR
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| Breach response time | ≤ 72h | Notify authority/khách | **0%** > 72h (legal) |
| DSAR resolution | ≤ 1 tháng, 100% | Đáp ứng quyền chủ thể | 0% trễ |
| RoPA freshness | review ≤ quý | Inventory cập nhật | — |

### SOP-BCK-006 Workforce
| SLI | SLO | SLA | Error budget |
|---|---|---|---|
| AI worker uptime | ≥ 99% | 12 worker sẵn sàng | ≤ 1%/worker/tuần |
| Output quality (1−reject) | ≥ 90% | Output dùng được | ≤ 10% reject |
| Weekly report on-time | 100% | Owner có report thứ 2 | 0% miss |

---

## Nguyên tắc Error Budget
- **Compliance (BCK-003 VAT, BCK-004 GPSR, BCK-005 breach/DSAR):** error budget = **0%** vì rủi ro pháp lý — ngoại lệ cho phép SLO 100% (theo chuẩn vibe-company: legal gate được phép tuyệt đối hóa).
- **Finance & Workforce:** error budget > 0, dùng để cân bằng tốc độ vs hoàn hảo; vượt budget → freeze cải tiến, ưu tiên ổn định.

## Evidence & need_review
Mọi SLO mang evidence (historical/benchmark/legal requirement) + confidence_score. Target không có baseline nội bộ → đánh dấu `need_review: true`, đưa vào review-queue. Compliance 100% có confidence cao (legal mandate), không cần review.

## Đo & báo cáo
Weekly (workforce, bookkeeping), monthly (P&L/margin/VAT), per-event (GPSR clearance, breach, DSAR). Vi phạm SLO → RCA trong [_quality](../_quality/README.md).
