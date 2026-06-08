# SOP-GRW-002 — Facebook Ads management

**Department:** Growth (grw) · **AI Worker:** FB Ads Specialist AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Facebook Ads (Meta Ads Manager) là 100% nguồn traffic. Tối ưu ROAS, không "đốt" budget. ROAS floor 2.5, CPA floor $20. ABO test → CBO scale (+20%/2 ngày). BM 5-tier anti-ban.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Chạy & tối ưu Facebook Ads để tăng doanh số có lãi (ROAS ≥ 2.5, CPA < $20). |
| **Phạm vi** | Facebook Ads (Meta Ads Manager) cho store ShopBase, market US (chính) + EU. |
| **Trigger** | Creative package sẵn (GRW-005) + Meta Ad Policy OK (Compliance); budget được Founder duyệt; review hàng ngày/tuần. |

### IPO
| | |
|---|---|
| **Input** | Creative package (GRW-005), product page live (MER-001), ad budget, ROAS/CPA hiện tại, CAPI events |
| **Control** | Budget cap, ROAS floor 2.5, CPA floor $20, Meta Ad Policy, BM 5-tier |
| **Output** | Campaign đang chạy + tối ưu + ad report |
| **Mechanism** | FB Ads Specialist AI + Meta Ads Manager API, ShopBase Pixel/CAPI, Claude API |

## 2. RACI
| Hoạt động | Founder | FB Ads Specialist AI | Compliance AI (05) |
|---|---|---|---|
| Duyệt budget cap | **A** | C | I |
| Verify Meta Ad Policy | I | C | **R** |
| Chạy/tối ưu campaign (ABO→CBO) | I | **R** | I |
| Scale budget lớn / market mới | **A** | R | I |

## 3. Đầu vào
- [ ] Creative package (GRW-005) · [ ] Meta Ad Policy OK (Compliance) · [ ] Budget cap (Founder) · [ ] Product page live + CAPI verify · [ ] ROAS/CPA floor

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Verify CAPI | Kiểm tra Pixel + CAPI fire đúng (ViewContent, AddToCart, InitiateCheckout, Purchase + value) | [AI WORKFORCE] | Không spend nếu CAPI lỗi |
| 4.2 | Set up ABO test | Campaign test theo breed, 4-layer targeting (interest/behavior/custom/LAL), $5–10/ngày/ad set, ≥3 creative/ad set | [AI AUGMENT] | Hard cap; BM 5-tier anti-ban |
| 4.3 | Monitor | Theo dõi ROAS/CPA/CTR hàng ngày | [AI WORKFORCE] | Alert khi ROAS<2.5 / CPA>$20 |
| 4.4 | Cut / Scale | Cut ad set CPP>2x target; scale winner sang CBO (+20%/2 ngày) | [AI AUGMENT] | Pause khi ROAS<floor kéo dài; không scale audience tùy tiện |
| 4.5 | Report | Tổng hợp → GRW-004 | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | ROAS | ROAS tổng | ≥ 2.5 | ☐ |
| 2 | CPA | cost per purchase | < $20 | ☐ |
| 3 | Budget | trong cap | 100% | ☐ |
| 4 | Tối ưu | ad set lỗ pause kịp | 100% | ☐ |

**Quyết định:** Meta Ad Policy chưa đạt → không chạy ads (block). ROAS < floor 2.5 / CPA > $20 kéo dài → pause + escalate Founder (không "đốt" tiếp). CAPI lỗi → dừng spend.

## 6. Output & Downstream
- **Lưu:** ./output/fb-ads-report_[YYYY-Wnn].md → archive/ · **Downstream:** GRW-004, BCK-003 (chi phí ads vào profit-per-SKU), Marketing AI (purchaser/ATC audience → Klaviyo retarget)

## 7. Phụ lục
Niche spec FB Ads: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §5 · Creative (GRW-005): ../../fb-creative/template/sop_grw-005_fb-creative_v1.0_2026-06-03.md · Pricing (ad allocation): ../../../02-merchandising/pricing-margin/
