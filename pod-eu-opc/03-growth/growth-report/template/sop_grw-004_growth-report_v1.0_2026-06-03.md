# SOP-GRW-004 — Growth performance report

**Department:** Growth (grw) · **AI Worker:** FB Ads Specialist AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tổng hợp hiệu suất growth (traffic FB Ads, conversion, ROAS/CPA, AOV) → insight + đề xuất cho Founder. |
| **Phạm vi** | Báo cáo tuần (KPI) + tháng (KRI/OKR). |
| **Trigger** | Cuối tuần / cuối tháng. |

### IPO
| | |
|---|---|
| **Input** | FB Ads metrics (GRW-002), email metrics Klaviyo (GRW-003), organic/community metrics (GRW-001), doanh số ShopBase (FUL/BCK) |
| **Control** | Định dạng report theo OKR/KRI/KPI, đúng hạn |
| **Output** | Growth report + đề xuất hành động |
| **Mechanism** | FB Ads Specialist AI + Claude API, report template |

## 2. RACI
| Hoạt động | Founder | FB Ads Specialist AI |
|---|---|---|
| Đọc & quyết định | **A** | C |
| Soạn report | I | **R** |

## 3. Đầu vào
- [ ] Metrics từ GRW-001/002/003 · [ ] Doanh số kỳ (ShopBase) · [ ] Report template

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Thu thập | Gom metrics các kênh (FB Ads/email/organic + doanh số) | [AI WORKFORCE] | Cross-check nguồn |
| 4.2 | Phân tích | Top breed/creative, ROAS/CPA, CVR, AOV, anomaly | [AI AUGMENT] | KPI→KRI causal chain |
| 4.3 | Đề xuất | Hành động tuần/tháng tới (scale/cut/refresh creative) | [AI AUGMENT] | Actionable, có ưu tiên |
| 4.4 | Gửi | Xuất report → Founder | [AI WORKFORCE] | Đúng hạn |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Đúng hạn | report nộp đúng hạn | 100% | ☐ |
| 2 | Đầy đủ | đủ KPI + KRI (monthly) | 100% | ☐ |
| 3 | Actionable | có đề xuất ưu tiên | đạt | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/ hoặc ../reports/{weekly,monthly}/ → archive/ · **Downstream:** Founder (strategy), OKR review

## 7. Phụ lục
Report template: ../../../_shared/templates/ · KPI: ../../kpi_grw-001_03-growth-kpis_v1.0_2026-06-03.md · Niche spec KPI: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §7
