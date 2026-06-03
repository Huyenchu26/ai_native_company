# SOP-BCK-003 — Profit-per-SKU & financial report

**Department:** Backoffice (bck) · **AI Worker:** Finance AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Profit-per-SKU là chỉ số sống còn của POD: biết SKU nào lãi để scale, SKU nào lỗ để kill.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tính lợi nhuận thực từng SKU sau mọi phí; lập P&L tháng + CEO brief; đề xuất scale/kill. |
| **Phạm vi** | Profit-per-SKU + báo cáo tài chính tháng. |
| **Trigger** | Cuối tháng (trước ngày 5 tháng sau). |

### IPO
| | |
|---|---|
| **Input** | Ledger (BCK-001), pricing (MER-003), ad spend theo SKU (GRW-002), refund (FUL-004) |
| **Control** | Báo cáo trước ngày 5, accuracy, margin floor 30% để đánh giá |
| **Output** | Profit-per-SKU table, P&L tháng, CEO financial brief, đề xuất scale/kill |
| **Mechanism** | Finance AI + Claude API, Sheets/Xero |

## 2. RACI
| Hoạt động | Founder | Finance AI |
|---|---|---|
| Đọc & quyết định scale/kill | **A** | C |
| Tính & soạn report | I | **R** |

## 3. Đầu vào
- [ ] Ledger kỳ (BCK-001) · [ ] Pricing sheet (MER-003) · [ ] Ad spend theo SKU (GRW-002)

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Gom theo SKU | Doanh thu + chi phí (in/ship/fees/ads/refund) theo SKU | [AI WORKFORCE] | Map đầy đủ, không sót chi phí |
| 4.2 | Tính profit | Lợi nhuận & margin thực mỗi SKU | [AI WORKFORCE] | Đối chiếu vs floor 30% |
| 4.3 | P&L | Tổng hợp P&L tháng | [AI AUGMENT] | Khớp tổng với ledger |
| 4.4 | Insight | SKU lãi nhất / lỗ; đề xuất scale (→GRW) / kill (→MER) | [AI AUGMENT] | Có ngưỡng rõ để kill |
| 4.5 | CEO brief | Tóm tắt cho Founder + gửi đúng hạn | [AI AUGMENT] | Reminder trước ngày 5 |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Đúng hạn | report nộp | trước ngày 5 | ☐ |
| 2 | Coverage | mọi SKU có profit number | 100% | ☐ |
| 3 | Khớp sổ | P&L khớp ledger BCK-001 | = €0 chênh | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/profit-per-sku_[YYYY-MM].md, pnl_[YYYY-MM].md → archive/
- **Downstream:** Founder (scale/kill), GRW-002 (scale ads SKU lãi), MER (kill SKU lỗ), OKR review

## 7. Phụ lục
Ledger: ../bookkeeping/ · Pricing: ../../02-merchandising/pricing-margin/ · Thiết kế §3.5, §7
