# SOP-PRD-002 — Trend & Seasonal Opportunity Calendar

| Trường | Giá trị |
|--------|---------|
| **Mã SOP** | SOP-PRD-002 |
| **Phiên bản** | 1.0 |
| **Ngày** | 2026-06-23 |
| **Chủ sở hữu** | Product Studio (dept: prd) |
| **Department** | 01-product-studio |
| **AI Workforce** | `[AI WORKFORCE]` — chạy bởi **vibe-opc-pod-product-niche-research** |

---

## 0. IPO Analysis

| Loại | Mục |
|------|-----|
| **Input (I)** | Validated niche list (từ PRD-001), Google Trends seasonality, lịch holiday US+EU, lead-time design+print (Printify/PrintBase) |
| **Control (C)** | Lead-time rule (design phải xong trước peak ≥ 6 tuần), seasonal priority rubric, capacity test/đợt (promote SOP-MER-006) |
| **Output (O)** | **Seasonal opportunity calendar** — niche × thời điểm × ưu tiên, feed sang SOP-PRD-003 và 02-merchandising |
| **Mechanism (M)** | AI Worker `niche-research` + Google Trends + holiday calendar; human review |

**Upstream:** SOP-PRD-001 (validated niche list)
**Downstream:** SOP-PRD-003 (design backlog priority) + 02-merchandising (promote batch timing)

---

## 1. Tổng Quan

- **Mục đích:** Xếp lịch khi nào tung niche nào để bắt peak mùa vụ (Christmas, Halloween, Mother's/Father's Day, Valentine, back-to-school, sport season…) trên cả US+EU, đảm bảo design kịp lead-time.
- **Phạm vi:** Từ validated niche list → calendar có timing & priority. Không quyết định ad budget (đó là 03-growth).
- **Định nghĩa:**
  - **Peak window:** khoảng search/buy interest cao nhất theo Trends.
  - **Design deadline:** peak − lead-time (design + print + listing).
  - **Evergreen vs seasonal:** niche không phụ thuộc mùa vs phụ thuộc mùa.

## 2. Vai Trò & Trách Nhiệm

**RACI**

| Hoạt động | OPC | AI niche-research | AI product-design | 02-merch |
|-----------|:----:|:----:|:----:|:----:|
| Phân loại evergreen/seasonal | A | R | C | I |
| Tính design deadline | A | R | R | I |
| Set priority calendar | R/A | R | C | C |

**AI Roles**

| AI Worker | Skill | Trách nhiệm |
|-----------|-------|-------------|
| vibe-opc-pod-product-niche-research | trend analysis, seasonal scheduling | Responsible |

## 3. Quy Trình

### Bước 1 — Phân loại seasonality
| I | C | O | M |
|---|---|---|---|
| Validated niche list | Trends seasonality | Niche tagged evergreen/seasonal | AI |

| # | Hành động | Output |
|---|-----------|--------|
| 1.1 | Đọc đường cong Trends 12–24 tháng | Seasonality curve |
| 1.2 | Map niche → holiday/event US+EU | Event mapping |

### Bước 2 — Tính deadline & ưu tiên
| I | C | O | M |
|---|---|---|---|
| Event mapping | Lead-time rule (≥6 tuần) | Design deadline + priority | AI + product-design |

| # | Hành động | Output |
|---|-----------|--------|
| 2.1 | Deadline = peak − (design+print+listing) | Date |
| 2.2 | Priority = demand_score × proximity-peak; **proximity-peak = 1 / (số tuần tới peak)** — peak càng gần điểm số càng cao, đảm bảo score lặp lại được giữa các lần chạy | Score |

### Bước 3 — Xuất calendar
| I | C | O | M |
|---|---|---|---|
| Priority list | Capacity/đợt | Seasonal calendar file | AI + human review |

| # | Hành động | Output |
|---|-----------|--------|
| 3.1 | Sắp lịch rolling 12 tuần | Calendar |
| 3.2 | Ghi ra `output/` handoff PRD-003 + 02-merch | File |

## 4. Phân Nhánh & Xử Lý Đặc Biệt

| Tình huống | Xử lý |
|-----------|-------|
| Peak đã cận (< lead-time) | Hạ priority năm nay, lên lịch năm sau |
| Niche evergreen | Đưa vào "always-on backlog", không gắn deadline cứng |
| Overlap nhiều peak cùng tuần | Giới hạn theo capacity/đợt (5–10 SP) |

## 5. Checklist

**Quality Gate**

| Tiêu chí | SLI | SLO | Check Method | Pass |
|----------|-----|-----|-------------|:----:|
| Calendar coverage | % niche có timing | 100% | Calendar file | ☐ |
| Lead-time tuân thủ | % deadline ≥ 6 tuần trước peak | ≥ 95% | Date diff | ☐ |
| Rolling horizon | # tuần lịch sẵn | ≥ 12 | Calendar | ☐ |

**Prevention Measures**

| Rủi ro | Phòng ngừa |
|--------|-----------|
| Miss peak vì design trễ | Deadline buffer 1 tuần |
| Quá tải đợt promote | Cap 5–10 SP/đợt (SOP-MER-006) |

## 6. Tài Nguyên & Tham Chiếu

- **Upstream:** [SOP-PRD-001](../../research-niche/template/sop_prd-001_niche-research_v1.0_2026-06-23.md)
- **Downstream:** [SOP-PRD-003](../../design-aop/template/sop_prd-003_aop-design_v1.0_2026-06-23.md) · [SOP-MER-006 promote-batch](../../../02-merchandising/promote-batch/template/sop_mer-006_promote-batch_v1.0_2026-06-23.md) · [SOP-MER-002 setup-printify](../../../02-merchandising/setup-printify/template/sop_mer-002_printify-setup_v1.0_2026-06-23.md)
- **AI Skill:** vibe-opc-pod-product-niche-research

## 7. Lịch Sử Thay Đổi

| Phiên bản | Ngày | Thay đổi | Tác giả |
|-----------|------|----------|---------|
| 1.0 | 2026-06-23 | Khởi tạo SOP | Company Architect |
