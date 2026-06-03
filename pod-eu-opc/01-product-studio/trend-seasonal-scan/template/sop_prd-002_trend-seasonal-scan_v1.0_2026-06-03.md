# SOP-PRD-002 — Trend & seasonal scan (EU)

**Department:** Product Studio (prd) · **AI Worker:** Niche Research AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Nắm cơ hội theo mùa/xu hướng với **lead time đủ** — POD cần listing index + Ads ramp trước mùa 4-8 tuần.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Lập lịch cơ hội theo mùa/trend cho thị trường EU, đảm bảo bắt đầu sản xuất đủ sớm. |
| **Phạm vi** | Scan trend + dịp lễ EU; ra opportunity calendar. Không tạo design. |
| **Trigger** | Hàng tháng (rolling 3 tháng tới); hoặc khi phát hiện trend đột biến. |

### IPO
| | |
|---|---|
| **Input** | Pinterest Trends/Predicts, Google Trends, Etsy trending, lịch lễ EU theo nước |
| **Control** | Lead time tối thiểu (≥4-8 tuần trước dịp), audience EU, IP-safe |
| **Output** | Seasonal opportunity calendar (dịp, ngày, lead-time bắt đầu, niche gợi ý) |
| **Mechanism** | Niche Research AI + Claude API, Pinterest/Google Trends, Etsy |

## 2. Lịch dịp lễ EU (Knowledge — bắt đầu trước dịp)
| Dịp | Thời điểm | Bắt đầu sản xuất | Lưu ý EU |
|---|---|---|---|
| Christmas | 24-25/12 | Tháng 9-10 | Lớn nhất; gift apparel, "family/ugly sweater" |
| New Year | 31/12-1/1 | Tháng 11 | Resolution, motivational |
| Valentine | 14/2 | Tháng 12 | Couple, pet-love |
| Easter | T3-4 (đổi) | ~6 tuần trước | Spring themes |
| Mother's Day | **Khác từng nước** (UK: T3; phần lớn EU: T5) | ~6 tuần trước | ⚠️ Không dùng 1 ngày chung |
| Father's Day | Phần lớn EU: T6 | ~6 tuần trước | — |
| Pride | Tháng 6 | Tháng 4 | LGBTQ+ |
| Oktoberfest | Cuối T9 (DE) | Tháng 8 | Mạnh ở Đức/Áo |
| Halloween | 31/10 | Tháng 8-9 | — |
| Back-to-school | T8-9 | Tháng 6-7 | Teacher gifts |

> ⚠️ **Mother's/Father's Day khác nhau theo từng nước EU** — phải tách theo thị trường (DE/FR/UK), không gộp.

## 3. RACI
| Hoạt động | Founder | Niche Research AI |
|---|---|---|
| Duyệt opportunity calendar | A | **R** |

## 4. Đầu vào
- [ ] Truy cập Pinterest/Google Trends · [ ] Lịch lễ EU theo nước · [ ] Portfolio hiện tại

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Scan trend | Quét Pinterest Predicts, Google Trends, Etsy trending | [AI WORKFORCE] | ≥2 nguồn xác nhận |
| 5.2 | Map dịp lễ | Đối chiếu lịch lễ EU theo nước (3 tháng tới) | [AI WORKFORCE] | Dùng bảng §2, tách theo nước |
| 5.3 | Check lead time | Loại cơ hội không đủ thời gian sản xuất | [AI AUGMENT] | Lead-time gate ≥4 tuần |
| 5.4 | Xuất calendar | Lập opportunity calendar + niche gợi ý cho PRD-001 | [AI AUGMENT] | Mỗi mục có ngày bắt đầu rõ |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Lead time | mọi opportunity đủ lead time | 100% | ☐ |
| 2 | Nguồn | xác nhận ≥2 nguồn | 100% | ☐ |
| 3 | Theo nước | dịp lễ tách đúng nước EU | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/seasonal-calendar_[YYYY-MM]_DONE.md → archive/
- **Downstream:** PRD-001 (seed niche), PRD-003 (design)

## 8. Phụ lục
Knowledge: ../_knowledge/ · Thiết kế: ../../02-design/opc-design-roadmap.md §3.1
