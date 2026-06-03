# SOP-PRD-001 — Niche & keyword research

**Department:** Product Studio (prd) · **AI Worker:** Niche Research AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Đầu nguồn của pipeline. Chất lượng niche quyết định toàn bộ tỉ lệ thắng phía sau.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tìm niche apparel có **demand thật** trên Etsy EU + cạnh tranh không quá bão hòa, sạch IP → feed design. |
| **Phạm vi** | Chỉ nghiên cứu & validate niche. KHÔNG tạo design (đó là PRD-003). |
| **Trigger** | Theo lịch hàng tuần; hoặc khi cần mở rộng portfolio / sau seasonal scan (PRD-002). |

### IPO
| | |
|---|---|
| **Input** | Etsy search/autocomplete, eRank/Marmalead, Pinterest Trends, competitor shops, seed ideas, output PRD-002 |
| **Control** | Tiêu chí demand-vs-competition, brand fit, phù hợp in apparel, không vi phạm IP |
| **Output** | Validated niche list (mỗi niche: keyword chính, search volume, competition, seasonality, audience EU, demand score) |
| **Mechanism** | Niche Research AI + Claude API, eRank, Pinterest Trends, Etsy |

## 2. Tiêu chí Demand Score (Knowledge)
Mỗi niche chấm theo: **Demand** (search volume/engagement) · **Competition** (số listing, độ bão hòa) · **Buyer intent** · **Seasonality** (evergreen vs mùa) · **Audience EU rõ ràng** · **IP-safe**.
→ Ưu tiên: demand trung bình-cao + competition vừa (tránh "red ocean") + audience cụ thể (micro-niche).

## 3. RACI
| Hoạt động | Founder | Niche Research AI |
|---|---|---|
| Chốt portfolio niche | **A** | R |
| Phân tích & chấm điểm | C | **R** |

## 4. Đầu vào
- [ ] Seed ideas / hướng portfolio (Founder) · [ ] Truy cập eRank/Pinterest Trends · [ ] Output PRD-002 (nếu có)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Seed | Thu thập ý tưởng + dịp từ PRD-002 | [AI WORKFORCE] | — |
| 5.2 | Keyword expansion | Mở rộng long-tail từ Etsy autocomplete + eRank | [AI WORKFORCE] | Dùng dữ liệu thật, không đoán volume |
| 5.3 | Demand vs competition | Phân tích volume, số listing, top sellers | [AI AUGMENT] | Cross-check ≥2 nguồn |
| 5.4 | IP pre-flag | Loại sớm niche dính brand/character/celebrity | [AI WORKFORCE] | Pre-flag trước khi chấm điểm → không tốn công design |
| 5.5 | Score & rank | Chấm demand score, xếp hạng, chọn top | [AI AUGMENT] | Ngưỡng demand score tối thiểu |
| 5.6 | Handoff | Xuất validated niche list cho PRD-003 | [AI WORKFORCE] | Đủ field bắt buộc |

## 6. Quality Gate (SLI/SLO)
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Đủ dữ liệu | % niche đủ field | 100% | ☐ |
| 2 | Demand | demand score | ≥ ngưỡng | ☐ |
| 3 | Competition | độ bão hòa | không "saturated" | ☐ |
| 4 | IP | red-flag check | 0 niche dính IP rõ | ☐ |

**Quyết định:** pass → output/ ; fail → loop (max 3) → escalate.

## 7. Output & Downstream
- **Lưu:** ./output/niche-list_[YYYY-Wnn]_DONE.md → ./archive/
- **Downstream:** PRD-003 (design), PRD-002 (mùa vụ)

## 8. Phụ lục
- Doc: ../niche-selection-criteria.md (SOP-PRD-005) · Knowledge: ../_knowledge/ · Thiết kế: ../../02-design/opc-design-roadmap.md §3.1
