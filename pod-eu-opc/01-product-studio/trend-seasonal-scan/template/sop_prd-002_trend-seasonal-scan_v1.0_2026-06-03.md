# SOP-PRD-002 — Trend & seasonal scan (US+EU)

**Department:** Product Studio (prd) · **AI Worker:** Niche Research AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Nắm cơ hội theo mùa/xu hướng với **lead time đủ** — cần design + product page sẵn + Facebook Ads ramp trước mùa 4-8 tuần. Gift-driven (Christmas, Mother's Day) đẩy doanh thu 2–3x.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Lập lịch cơ hội theo mùa/trend cho thị trường US+EU, đảm bảo bắt đầu sản xuất + ramp ads đủ sớm. |
| **Phạm vi** | Scan trend + dịp lễ US+EU; ra opportunity calendar. Không tạo design. |
| **Trigger** | Hàng tháng (rolling 3 tháng tới); hoặc khi phát hiện trend/ad winner đột biến. |

### IPO
| | |
|---|---|
| **Input** | Google Trends, AdSpy/BigSpy trending, Meta signal, lịch lễ US+EU theo nước |
| **Control** | Lead time tối thiểu (≥4-8 tuần trước dịp), FB audience đủ, IP/TM-safe |
| **Output** | Seasonal opportunity calendar (dịp, ngày, lead-time bắt đầu, breed + design type gợi ý) |
| **Mechanism** | Niche Research AI + Claude API, Google Trends, AdSpy/BigSpy, Meta Audience Insights |

## 2. Lịch dịp lễ US+EU (Knowledge — bắt đầu trước dịp)
| Dịp | Thời điểm | Bắt đầu (sản xuất + ramp ads) | Lưu ý US+EU |
|---|---|---|---|
| Christmas | 24-25/12 | Tháng 9-10 | Lớn nhất; gift "Golden Retriever Mom", ugly-sweater AOP |
| New Year | 31/12-1/1 | Tháng 11 | Resolution, fitness/yoga angle |
| Valentine | 14/2 | Tháng 12 | Couple + pet-love, "dog mom" gift |
| Easter | T3-4 (đổi) | ~6 tuần trước | Spring/pastel themes |
| Mother's Day | **Khác từng nước** (US: T5 CN-2; UK: T3; phần lớn EU: T5) | ~6 tuần trước | ⚠️ Mạnh nhất cho "dog mom" — không dùng 1 ngày chung |
| Father's Day | US: T6 CN-3; phần lớn EU: T6 | ~6 tuần trước | "dog dad" angle |
| Pride | Tháng 6 | Tháng 4 | LGBTQ+ + pet |
| Halloween | 31/10 | Tháng 8-9 | Funny/costume dog AOP |
| Black Friday / Cyber Monday | Cuối T11 | Tháng 9-10 | Peak ads spend US |

> ⚠️ **Mother's/Father's Day khác nhau US vs từng nước EU** — phải tách theo thị trường (US/DE/FR/UK), không gộp.

## 3. RACI
| Hoạt động | Founder | Niche Research AI |
|---|---|---|
| Duyệt opportunity calendar | A | **R** |

## 4. Đầu vào
- [ ] Truy cập Google Trends + AdSpy/BigSpy · [ ] Lịch lễ US+EU theo nước · [ ] Portfolio breed hiện tại

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Scan trend | Quét Google Trends, AdSpy/BigSpy trending, Meta signal | [AI WORKFORCE] | ≥2 nguồn xác nhận |
| 5.2 | Map dịp lễ | Đối chiếu lịch lễ US+EU theo nước (3 tháng tới) | [AI WORKFORCE] | Dùng bảng §2, tách theo nước |
| 5.3 | Check lead time | Loại cơ hội không đủ thời gian (sản xuất + ramp ads) | [AI AUGMENT] | Lead-time gate ≥4 tuần |
| 5.4 | Xuất calendar | Lập opportunity calendar + breed/design gợi ý cho PRD-001 | [AI AUGMENT] | Mỗi mục có ngày bắt đầu rõ |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Lead time | mọi opportunity đủ lead time | 100% | ☐ |
| 2 | Nguồn | xác nhận ≥2 nguồn | 100% | ☐ |
| 3 | Theo nước | dịp lễ tách đúng nước US+EU | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/seasonal-calendar_[YYYY-MM]_DONE.md → archive/
- **Downstream:** PRD-001 (seed breed), PRD-003 (design), FB Ads Specialist AI (lịch ramp ads)

## 8. Phụ lục
Knowledge: ../_knowledge/ · Niche strategy: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §6
