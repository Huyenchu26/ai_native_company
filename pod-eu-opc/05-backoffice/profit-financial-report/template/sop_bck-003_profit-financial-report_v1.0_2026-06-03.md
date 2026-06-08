# SOP-BCK-003 — Profit-per-SKU & financial report

**Department:** Backoffice (bck) · **AI Worker:** Finance AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Profit-per-SKU + ROAS/CPA là chỉ số sống còn của POD: biết SKU/breed nào lãi để scale, SKU nào lỗ để kill; theo dõi target $8,000 (~200 triệu VNĐ)/tháng.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tính lợi nhuận thực từng SKU sau mọi phí (kể cả ad spend); track ROAS/CPA/AOV; lập P&L tháng + CEO brief; quy đổi USD→VND vs target; đề xuất scale/kill. |
| **Phạm vi** | Profit-per-SKU + báo cáo tài chính tháng + ROAS/CPA tracking. |
| **Trigger** | Cuối tháng (trước ngày 5 tháng sau). |

### IPO
| | |
|---|---|
| **Input** | Ledger (BCK-001), pricing/base cost (MER-003), Facebook ad spend theo SKU/campaign (GRW-002), ROAS/CPA (GRW-004), refund (FUL-004) |
| **Control** | Báo cáo trước ngày 5, accuracy, gross margin floor ~45–55% (kinh tế ShopBase), ROAS floor 2.5, CPA < $20, AOV > $75, target $8,000/tháng |
| **Output** | Profit-per-SKU table, P&L tháng, ROAS/CPA dashboard, doanh thu USD→VND vs target, CEO financial brief, đề xuất scale/kill |
| **Mechanism** | Finance AI + Claude API, Sheets/Xero, ShopBase/Meta Ads API |

## 2. RACI
| Hoạt động | Founder | Finance AI |
|---|---|---|
| Đọc & quyết định scale/kill | **A** | C |
| Tính & soạn report | I | **R** |

## 3. Đầu vào
- [ ] Ledger kỳ (BCK-001) · [ ] Pricing/base cost sheet (MER-003) · [ ] Facebook ad spend + ROAS/CPA theo SKU (GRW-002/GRW-004)

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Gom theo SKU | Doanh thu + chi phí (base cost/ship/ShopBase fee/Facebook ads/refund) theo SKU/breed | [AI WORKFORCE] | Map đầy đủ, không sót chi phí (nhất là ad spend) |
| 4.2 | Tính profit | Lợi nhuận & gross margin thực mỗi SKU; ROAS/CPA/AOV | [AI WORKFORCE] | Đối chiếu vs gross margin floor ~45–55% + ROAS floor 2.5 |
| 4.3 | P&L | Tổng hợp P&L tháng; quy đổi doanh thu USD→VND vs target $8k | [AI AUGMENT] | Khớp tổng với ledger |
| 4.4 | Insight | SKU/breed lãi nhất / lỗ; đề xuất scale (→GRW-002) / kill (→MER) | [AI AUGMENT] | Có ngưỡng rõ: ROAS < 2.5 hoặc margin < floor → kill/pause |
| 4.5 | CEO brief | Tóm tắt cho Founder (gồm tiến độ vs target 200 triệu) + gửi đúng hạn | [AI AUGMENT] | Reminder trước ngày 5 |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Đúng hạn | report nộp | trước ngày 5 | ☐ |
| 2 | Coverage | mọi SKU có profit number + ROAS | 100% | ☐ |
| 3 | Khớp sổ | P&L khớp ledger BCK-001 | = $0 chênh | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/profit-per-sku_[YYYY-MM].md, pnl_[YYYY-MM].md → archive/
- **Downstream:** Founder (scale/kill), GRW-002 (scale ads SKU/breed lãi), MER (kill SKU lỗ), OKR review

## 7. Phụ lục
Ledger: ../bookkeeping/ · Pricing: ../../02-merchandising/pricing-margin/ · Ads/ROAS: ../../03-growth/fb-ads/ · Niche/kinh tế: ../../docs/08-niche-dog-breed-leggings-shopbase.md §4, §7
