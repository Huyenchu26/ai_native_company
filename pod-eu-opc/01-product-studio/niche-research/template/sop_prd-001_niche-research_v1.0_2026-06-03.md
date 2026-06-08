# SOP-PRD-001 — Niche & breed demand research

**Department:** Product Studio (prd) · **AI Worker:** Niche Research AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Đầu nguồn của pipeline. Chất lượng breed-niche quyết định toàn bộ tỉ lệ thắng (ROAS) phía sau.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tìm **dog breed** có **demand thật** (FB audience đủ lớn + có ad đang chạy/scale) cho AOP Leggings, cạnh tranh không bão hòa, sạch IP/TM → feed design. |
| **Phạm vi** | Chỉ nghiên cứu & validate breed-niche. KHÔNG tạo design (đó là PRD-003). |
| **Trigger** | Theo lịch hàng tuần; hoặc khi cần mở rộng portfolio breed / sau seasonal scan (PRD-002) / tín hiệu demand từ FB Ads Specialist AI. |

### IPO
| | |
|---|---|
| **Input** | Meta Audience Insights (FB audience size), AdSpy/BigSpy (competitor ads), Google Trends, seed breed, output PRD-002 |
| **Control** | Demand-vs-ad-competition, FB audience đủ lớn, phù hợp AOP leggings, không vi phạm IP/TM (tên breed) |
| **Output** | Validated niche list (mỗi breed: FB audience size, ad-competition, seasonality/gift angle, design type gợi ý, demand score, IP/TM status) |
| **Mechanism** | Niche Research AI + Claude API, Meta Audience Insights, AdSpy/BigSpy, Google Trends |

## 2. Tiêu chí Demand Score (Knowledge)
Mỗi breed chấm theo: **FB audience size** (Audience Insights, vd Golden Retriever ~8M / French Bulldog ~6M US) · **Ad competition** (AdSpy/BigSpy — winner đang scale?) · **Buyer intent** ("dog mom" identity, engaged shoppers) · **Seasonality / gift angle** · **Design fit AOP** (4 loại: tile/watercolor/funny/mandala) · **IP/TM-safe** (tên breed).
→ Ưu tiên: FB audience trung bình-cao + ad-competition vừa (tránh "red ocean") + identity rõ (micro-niche theo breed). Start: Golden Retriever, French Bulldog, Corgi, Dachshund.

## 3. RACI
| Hoạt động | Founder | Niche Research AI |
|---|---|---|
| Chốt portfolio breed | **A** | R |
| Phân tích & chấm điểm | C | **R** |

## 4. Đầu vào
- [ ] Seed breed / hướng portfolio (Founder) · [ ] Truy cập Meta Audience Insights + AdSpy/BigSpy + Google Trends · [ ] Output PRD-002 (nếu có)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Seed | Thu thập breed + dịp từ PRD-002 + tín hiệu từ FB Ads Specialist AI | [AI WORKFORCE] | — |
| 5.2 | Audience sizing | Đo FB audience size từng breed (Meta Audience Insights) | [AI WORKFORCE] | Dùng dữ liệu thật, không đoán size |
| 5.3 | Ad spy + demand vs competition | Spy ad đang chạy/scale (AdSpy/BigSpy) + Google Trends | [AI AUGMENT] | Cross-check ≥2 nguồn |
| 5.4 | IP/TM pre-flag | Loại sớm breed name đã đăng ký TM / dính brand/character/celebrity | [AI WORKFORCE] | Pre-flag trước khi chấm điểm → không tốn công design |
| 5.5 | Score & rank | Chấm demand score, xếp hạng, chọn top breed | [AI AUGMENT] | Ngưỡng demand score tối thiểu |
| 5.6 | Handoff | Xuất validated niche list cho PRD-003 | [AI WORKFORCE] | Đủ field bắt buộc |

## 6. Quality Gate (SLI/SLO)
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Đủ dữ liệu | % breed đủ field | 100% | ☐ |
| 2 | Demand | demand score | ≥ ngưỡng | ☐ |
| 3 | Competition | độ bão hòa ad | không "saturated" | ☐ |
| 4 | IP/TM | red-flag check tên breed | 0 breed dính IP/TM rõ | ☐ |

**Quyết định:** pass → output/ ; fail → loop (max 3) → escalate.

## 7. Output & Downstream
- **Lưu:** ./output/niche-list_[YYYY-Wnn]_DONE.md → ./archive/
- **Downstream:** PRD-003 (design), PRD-002 (mùa vụ), FB Ads Specialist AI (targeting input)

## 8. Phụ lục
- Doc: ../niche-selection-criteria.md (SOP-PRD-005) · Knowledge: ../_knowledge/ · Niche strategy: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §3
