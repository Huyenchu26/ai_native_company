# 01-Product Studio (dept: prd)

**Layer:** L2 Operations · **Ngày:** 2026-06-23 · **OPC:** 1 người + AI Workforce
**Vai trò:** Niche research đa-niche + AOP design print-ready + IP/TM clearance.

> Store DAKOfits là **đa niche** (~3.200 SP — pet/dog-breed, hobby, profession, zodiac, sport, faith…), không chỉ 1 niche. Tham chiếu Gearbunch.

---

## Department IPO

| | Mô tả |
|--|-------|
| **Input (I)** | Niche pool + competitor data (AdSpy/BigSpy, Meta Audience Insights, Google Trends), strategy direction (00-company), brand style guide, provider spec (Printify/PrintBase US+EU) |
| **Control (C)** | Niche scoring rubric, 300 DPI, AOP 360° QC, 4 loại design, IP/TM gate cứng (no clearance→no listing), thị trường US+EU |
| **Output (O)** | Validated niche list + seasonal calendar → AOP design print-ready + IP-clearance log |
| **Mechanism (M)** | 2 AI Worker (niche-research, product-design) + human review tại `processing/human-review` |

## Value Chain Position

| | |
|--|--|
| **Layer** | L2 Operations |
| **Upstream** | 00-company Strategy (niche direction, Company OKR O3) |
| **Downstream** | **02-merchandising** (catalog setup từ design CLEAR) → 03-growth → 04-fulfillment |
| **Vị trí** | Điểm đầu của value chain sản phẩm: tạo "nguyên liệu" SP cho toàn pipeline |

## Internal Process IPOs

| SOP | Input | Output | Downstream |
|-----|-------|--------|-----------|
| PRD-001 Niche Research | AdSpy/Meta/Trends | Validated niche list | PRD-002, PRD-003 |
| PRD-002 Trend & Seasonal | Validated niche list | Seasonal calendar | PRD-003, 02-merch |
| PRD-003 AOP Design | Niche + calendar | Design print-ready 300 DPI | PRD-004 |
| PRD-004 IP/TM Clearance | Design + term | IP-clearance log (CLEAR) | 02-merch |

## RACI Matrix (Department)

| Hoạt động | OPC | AI niche-research | AI product-design | 02-merch |
|-----------|:----:|:----:|:----:|:----:|
| Niche research & scoring | A | R | C | I |
| Seasonal calendar | A | R | C | I |
| AOP design + QC 360° | A | C | R | I |
| IP/TM clearance | A | C | R | I |
| Approve handoff | R/A | C | C | I |

## KPI Summary

| KPI | Metric | Target | Tần suất | → Company |
|-----|--------|--------|----------|-----------|
| Niche validated/tuần | # niche pass | ≥ 3 | Weekly | KPI1 → revenue |
| Design print-ready/tuần | # design pass QC | ≥ 20 | Weekly | KPI2 → revenue |
| AOP 360° pass rate | % no-seam | ≥ 98% | Weekly | margin (giảm reprint) |
| IP/TM clearance rate | % SP cleared trước listing | 100% | Per design | Gate cứng |

## OKR Summary (Q3 2026)

**Committed (target 100%)** — align Company O3 winner đa-niche
- O.PRD1-KR1: ≥ 3 niche validated/tuần
- O.PRD1-KR2: ≥ 20 design print-ready/tuần
- O.PRD1-KR3: IP/TM clearance 100% trước listing

**Stretch (x10, target 70% = success)**
- O.PRD2-KR1: 30 niche validated/tuần (pipeline tự động hóa) — `need_review`
- O.PRD2-KR2: 200 design print-ready/tuần (design library + automation) — `need_review`

Chi tiết: [okr_prd-001](./okr_prd-001_quarterly-okr_v1.0_2026-06-23.md)

## Quality Standards Summary (SLI/SLO)

| SLI | SLO | SOP |
|-----|-----|-----|
| % niche audience ≥ 500k | ≥ 90% | PRD-001 |
| % design ≥ 300 DPI | 100% | PRD-003 |
| % design pass AOP 360° | ≥ 98% | PRD-003 |
| Design turnaround | ≤ 24h | PRD-003 |
| % SP cleared trước listing | 100% | PRD-004 |

Chi tiết: [quality_prd-001](./quality_prd-001_quality-standards_v1.0_2026-06-23.md)

## AI Integration

| SOP | AI Worker | Skill |
|-----|-----------|-------|
| PRD-001 | vibe-opc-pod-product-niche-research | demand scoring, audience sizing, ad spy, IP pre-flag |
| PRD-002 | vibe-opc-pod-product-niche-research | trend analysis, seasonal scheduling |
| PRD-003 | vibe-opc-pod-product-design | AOP design 4 loại, 300 DPI, QC 360° |
| PRD-004 | vibe-opc-pod-product-design | IP/TM clearance, clearance logging |

## Tài liệu phòng

- [Charter](./charter_prd-department_v1.0_2026-06-23.md) · [OKR](./okr_prd-001_quarterly-okr_v1.0_2026-06-23.md) · [KRI](./kri_prd-001_key-result-indicators_v1.0_2026-06-23.md) · [KPI](./kpi_prd-001_product-kpis_v1.0_2026-06-23.md) · [Quality](./quality_prd-001_quality-standards_v1.0_2026-06-23.md)
- SOP: [PRD-001](./research-niche/template/sop_prd-001_niche-research_v1.0_2026-06-23.md) · [PRD-002](./analyze-trend/template/sop_prd-002_trend-seasonal_v1.0_2026-06-23.md) · [PRD-003](./design-aop/template/sop_prd-003_aop-design_v1.0_2026-06-23.md) · [PRD-004](./clear-ip/template/sop_prd-004_ip-tm-clearance_v1.0_2026-06-23.md)
- KWSR: [_knowledge](./_knowledge/README.md) · [_workflow](./_workflow/README.md) · [_skills-agents](./_skills-agents/README.md) · [_rules](./_rules/README.md)
