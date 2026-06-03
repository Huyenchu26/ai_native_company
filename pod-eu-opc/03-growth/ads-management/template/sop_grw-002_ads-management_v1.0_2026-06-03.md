# SOP-GRW-002 — Etsy Ads management (+ Meta Phase 2)

**Department:** Growth (grw) · **AI Worker:** Ads AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Tối ưu ROAS, không "đốt" budget. ROAS floor 2.5. Phase 2 mở rộng Meta/Google qua channel-config.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Chạy & tối ưu quảng cáo để tăng doanh số có lãi (ROAS ≥ 2.5). |
| **Phạm vi** | Etsy Ads (Phase 1); Meta/Google (Phase 2). |
| **Trigger** | Listing live có tiềm năng; budget được Founder duyệt; review hàng ngày/tuần. |

### IPO
| | |
|---|---|
| **Input** | Listing live + performance, ad budget, ROAS hiện tại |
| **Control** | Budget cap, ROAS floor 2.5, chính sách quảng cáo nền tảng |
| **Output** | Campaign đang chạy + tối ưu + ad report |
| **Mechanism** | Ads AI + Etsy Ads, Meta Ads (Phase 2), Claude API |

## 2. RACI
| Hoạt động | Founder | Ads AI |
|---|---|---|
| Duyệt budget cap | **A** | C |
| Chạy/tối ưu campaign | I | **R** |
| Scale budget lớn | **A** | R |

## 3. Đầu vào
- [ ] Budget cap (Founder) · [ ] Listing live + dữ liệu performance · [ ] ROAS floor

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Chọn listing | Chọn listing tiềm năng để promote | [AI AUGMENT] | Ưu tiên listing có conversion |
| 4.2 | Set budget | Phân bổ trong cap | [AI WORKFORCE] | Hard cap; không vượt |
| 4.3 | Monitor ROAS | Theo dõi ROAS hàng ngày | [AI WORKFORCE] | Alert khi < floor |
| 4.4 | Tối ưu | Pause listing lỗ, scale listing thắng | [AI AUGMENT] | Quy tắc pause khi ROAS < 2.5 kéo dài |
| 4.5 | Report | Tổng hợp → GRW-004 | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | ROAS | ROAS tổng | ≥ 2.5 | ☐ |
| 2 | Budget | trong cap | 100% | ☐ |
| 3 | Tối ưu | listing lỗ được pause kịp | 100% | ☐ |

**Quyết định:** ROAS < floor kéo dài → pause + escalate Founder (không "đốt" tiếp).

## 6. Output & Downstream
- **Lưu:** ./output/ads-report_[YYYY-Wnn].md → archive/ · **Downstream:** GRW-004, BCK-003 (chi phí ads vào profit-per-SKU)

## 7. Phụ lục
Channel: ../../_shared/channel-config/ · Pricing (ad allocation): ../../02-merchandising/pricing-margin/ · Thiết kế §3.3
