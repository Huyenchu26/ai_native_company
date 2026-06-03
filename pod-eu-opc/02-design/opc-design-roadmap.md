# OPC Design Roadmap — Công ty Thương mại POD Apparel (thị trường EU)

> Blueprint thiết kế & lộ trình triển khai One Person Company (OPC) cho công ty Print-on-Demand apparel bán vào châu Âu, vận hành bằng AI Workforce. Khởi đầu **Etsy + Printify** → mở rộng **Shopify**.

**Ngày tạo:** 2026-06-03
**Phiên bản:** 1.0
**Nguồn:** [Phân tích chuyển đổi](../01-analysis/pod-opc-transformation-analysis.md)
**Ngôn ngữ:** Nội bộ tiếng Việt · Listing/sản phẩm tiếng Anh

---

## Mục Lục

1. [OPC Company Profile](#1-opc-company-profile)
2. [Thiết kế Kiến trúc Tổng thể](#2-thiet-ke-kien-truc-tong-the)
3. [Thiết kế 5 Departments Chi tiết](#3-thiet-ke-5-departments-chi-tiet)
4. [Folder Structure (channel-agnostic)](#4-folder-structure-channel-agnostic)
5. [AI Workforce Blueprint](#5-ai-workforce-blueprint)
6. [Compliance EU — VAT/OSS/IOSS, GPSR, GDPR](#6-compliance-eu)
7. [Roadmap Triển khai](#7-roadmap-trien-khai)
8. [Channel Rollout: Etsy+Printify → Shopify](#8-channel-rollout)
9. [Dummy Data Plan](#9-dummy-data-plan)

---

## 1. OPC Company Profile

| Trường | Giá trị |
|---|---|
| **Loại hình** | One Person Company (OPC) |
| **Ngành** | E-commerce Print-on-Demand (Apparel) |
| **Sản phẩm** | T-shirt, hoodie, sweatshirt in theo yêu cầu |
| **Quy mô** | 1 Founder (CEO/System Designer) + 11 AI Workers |
| **Thị trường** | EU (ưu tiên DE, FR + eurozone) |
| **Kênh** | Phase 1: Etsy + Printify → Phase 2: + Shopify |
| **Ngôn ngữ vận hành** | Tiếng Việt (nội bộ) · English (listing, CSKH) |
| **Triết lý** | Founder thiết kế cách làm việc; AI là nhân sự số |

**Value Proposition:** Năng lực vận hành tương đương shop POD 10-12 người, chi phí gần như chỉ là API + tool subscription, biên lợi nhuận tối ưu nhờ SOP và compliance chặt.

---

## 2. Thiết kế Kiến trúc Tổng thể

### 2.1 Archimate + Porter Value Chain (POD-tailored)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: STRATEGY                                                         │
│  Founder (CEO) → Niche portfolio · Brand · Target tài chính · OKR quý      │
├──────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: PRIMARY ACTIVITIES (chuỗi giá trị POD)                           │
│  ┌────────────┐  ┌─────────────┐  ┌───────────┐  ┌──────────────────┐     │
│  │01 PRODUCT  │→ │02 MERCHAN-  │→ │03 GROWTH  │→ │04 FULFILLMENT     │     │
│  │   STUDIO   │  │   DISING    │  │           │  │   & CX            │     │
│  │niche+design│  │listing+SEO  │  │Pinterest  │  │order ops+tracking │     │
│  │+mockup+QC  │  │+sync+pricing│  │+Ads+email │  │+CSKH+returns      │     │
│  │            │  │             │  │           │  │                   │     │
│  │Niche Res AI│  │Listing-SEO  │  │Marketing  │  │Order-Ops AI       │     │
│  │Design AI   │  │Catalog-Sync │  │Ads AI     │  │CX AI              │     │
│  └────────────┘  └─────────────┘  └───────────┘  └──────────────────┘     │
├──────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: SUPPORT ACTIVITIES                                               │
│  05 BACKOFFICE — Finance/VAT · Compliance (GPSR/GDPR) · AI Workforce · Admin│
│  Finance AI · Compliance AI · Ops/HR AI                                     │
│                                                                            │
│  TẤT CẢ BÁO CÁO VỀ: Founder (1 người)                                      │
└──────────────────────────────────────────────────────────────────────────┘
```

### 2.2 RACI Matrix — Toàn công ty

| Hoạt động | Founder | 01 Product | 02 Merch | 03 Growth | 04 Fulfill | 05 Backoffice |
|---|---|---|---|---|---|---|
| Chiến lược niche/brand | **A** | C | C | C | I | I |
| Niche & trend research | **A** | **R** | C | C | I | I |
| Tạo & QC design | C | **R** | I | I | I | I |
| Bản quyền/IP check | **A** | **R** | C | I | I | C |
| Tạo listing + SEO | I | C | **R** | I | I | I |
| Printify setup + chọn provider EU | I | I | **R** | I | C | C |
| Pricing & margin | **A** | I | **R** | C | I | C |
| Channel sync (Etsy/Shopify) | I | I | **R** | I | I | I |
| Marketing & Ads | **A** | I | I | **R** | I | I |
| Xử lý đơn & exception | I | I | I | I | **R** | I |
| Shipping tracking | I | I | I | I | **R** | I |
| CSKH & returns | I | I | I | I | **R** | C |
| Bookkeeping & VAT/OSS | **A** | I | I | I | I | **R** |
| GPSR/GDPR compliance | **A** | C | C | I | C | **R** |
| AI workforce mgmt | **A** | I | I | I | I | **R** |
| Báo cáo tuần/tháng | **A** | **R** | **R** | **R** | **R** | **R** |

> **R**=Responsible · **A**=Accountable · **C**=Consulted · **I**=Informed

### 2.3 Dòng giá trị end-to-end (Process flow)

```
[Niche Research AI] phát hiện niche có demand
   → [Design AI] tạo design brief + design + mockup → QC bản quyền (Founder gate nếu rủi ro)
   → [Listing-SEO AI] viết title/tags/description (Etsy SEO) + nhãn GPSR
   → [Catalog-Sync AI] setup sản phẩm Printify (chọn EU provider) + pricing → publish Etsy
   → [Marketing AI/Ads AI] Pinterest + Etsy Ads kéo traffic
   → KHÁCH ĐẶT ĐƠN
   → [Order-Ops AI] nhận đơn → Printify auto-production → [Order-Ops AI] tracking
   → [CX AI] cập nhật khách, xử lý hỏi đáp/returns
   → [Finance AI] ghi nhận doanh thu, đối soát phí, profit-per-SKU
```

---

## 3. Thiết kế 5 Departments Chi tiết

> Mỗi department theo chuẩn **KWSR** (`_knowledge/ _workflow/ _skills-agents/ _rules/`) + có file `okr_ kri_ kpi_ quality_`. SOP loại **OPERATIONAL** có 5 subfolder state machine (`template → input → processing → output → archive`); loại **DOC-ONLY** là file .md tham khảo.

---

### 3.1 Department 01 — Product Studio

#### Tổng quan
| Trường | Giá trị |
|---|---|
| **Phạm vi** | Niche/keyword/trend research, design brief, tạo & QC design, mockup |
| **Mục tiêu** | Cung cấp design có demand + sạch bản quyền, đủ tốc độ (design velocity) |
| **AI Workers** | Niche Research AI, Design AI |
| **Founder** | Chốt niche portfolio + duyệt design rủi ro IP |

#### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Etsy/Pinterest trends, keyword data, seasonal calendar EU, competitor listings, brand guidelines |
| **Control** | Tiêu chí niche, chính sách bản quyền/IP, brand voice, GPSR (design phù hợp in apparel) |
| **Output** | Validated niche list, design brief, design file (print-ready), mockup, IP-clearance log |
| **Mechanism** | Claude API, image-gen tool (Midjourney/DALL·E/Ideogram), Printify mockup, Etsy/eRank/Marmalead, Pinterest Trends |

#### SOPs
| Mã | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-PRD-001 | Niche & keyword research | OPERATIONAL | Niche Research AI |
| SOP-PRD-002 | Trend & seasonal scan (EU) | OPERATIONAL | Niche Research AI |
| SOP-PRD-003 | Design brief & production | OPERATIONAL | Design AI |
| SOP-PRD-004 | Design QC + IP/copyright clearance | OPERATIONAL | Design AI |
| SOP-PRD-005 | Niche selection criteria | DOC-ONLY | — |

#### KPI / Quality Gate
| KPI | Target | SLI → SLO |
|---|---|---|
| Design mới/tuần (velocity) | ≥ 10 | — |
| Niche validated trước khi design | 100% | Demand score ≥ ngưỡng |
| IP clearance pass rate | 100% | 0 design vi phạm trademark lọt qua |
| Design QC pass (print-ready) | ≥ 95% | DPI ≥ 300, đúng kích thước in |

---

### 3.2 Department 02 — Merchandising

#### Tổng quan
| Trường | Giá trị |
|---|---|
| **Phạm vi** | Listing copy + Etsy SEO, Printify product setup, pricing/margin, channel sync & catalog QC |
| **Mục tiêu** | Publish listing chuẩn SEO + đúng giá có lãi + đúng compliance, đa kênh |
| **AI Workers** | Listing-SEO AI, Catalog-Sync AI |
| **Founder** | Duyệt pricing strategy + spot-check listing |

#### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Design + mockup (từ 01), keyword data, Printify catalog & giá in, channel config |
| **Control** | Etsy SEO rules (140 ký tự title, 13 tags), pricing floor (margin tối thiểu), GPSR labeling, brand voice |
| **Output** | Published listing (Etsy), Printify product, pricing sheet, sync log, catalog QC report |
| **Mechanism** | Etsy API, Printify API, Shopify API (Phase 2), Claude API, eRank/Marmalead |

#### SOPs
| Mã | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-MER-001 | Tạo listing + Etsy SEO (+ nhãn GPSR) | OPERATIONAL | Listing-SEO AI |
| SOP-MER-002 | Printify product setup + chọn EU provider | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-003 | Pricing & margin | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-004 | Channel sync & catalog QC | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-005 | Listing template & brand style | DOC-ONLY | — |

#### KPI / Quality Gate
| KPI | Target | SLI → SLO |
|---|---|---|
| Listing publish/tuần | ≥ 10 | — |
| SEO completeness | 100% | ≥ 13 tags, title ≤140, ≥ 5 ảnh mockup |
| Margin mỗi SKU | ≥ 30% | Giá bán − (giá Printify + phí Etsy) ≥ floor |
| Provider EU coverage | ≥ 90% | % SKU dùng xưởng in EU |
| GPSR label present | 100% | Listing có thông tin nhà SX + cảnh báo |

---

### 3.3 Department 03 — Growth

#### Tổng quan
| Trường | Giá trị |
|---|---|
| **Phạm vi** | Pinterest/social organic, Etsy Ads (→ Meta/Shopify Ads Phase 2), email, promotions |
| **Mục tiêu** | Kéo traffic chất lượng, ROAS dương, tăng conversion |
| **AI Workers** | Marketing AI, Ads AI |
| **Founder** | Duyệt ad budget + chiến dịch lớn |

#### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Listing đã publish, design assets, audience data, ad budget, seasonal calendar |
| **Control** | Ad budget cap, brand voice, ROAS floor, chính sách quảng cáo Etsy/Meta |
| **Output** | Pinterest pins/social posts, ad campaigns, email sequences, promotions, growth report |
| **Mechanism** | Pinterest API, Etsy Ads, Meta Ads (Phase 2), Claude API, Canva, email tool (Klaviyo/Mailchimp) |

#### SOPs
| Mã | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-GRW-001 | Pinterest & social content | OPERATIONAL | Marketing AI |
| SOP-GRW-002 | Etsy Ads management (+ Meta Phase 2) | OPERATIONAL | Ads AI |
| SOP-GRW-003 | Email & promotions | OPERATIONAL | Marketing AI |
| SOP-GRW-004 | Growth performance report | OPERATIONAL | Ads AI |
| SOP-GRW-005 | Brand & channel policy | DOC-ONLY | — |

#### KPI / Quality Gate
| KPI | Target | Frequency |
|---|---|---|
| Pinterest pins/tuần | ≥ 15 | Weekly |
| Etsy Ads ROAS | ≥ 2.5 | Daily/Weekly |
| Conversion rate | ≥ 2% | Weekly |
| Email open rate | ≥ 25% | Per campaign |

---

### 3.4 Department 04 — Fulfillment & CX

#### Tổng quan
| Trường | Giá trị |
|---|---|
| **Phạm vi** | Order monitoring, production/shipping tracking (Printify), exception handling, CSKH, returns/complaints |
| **Mục tiêu** | Giao đúng hạn, giữ rating ≥ 4.8 (Star Seller), CSAT cao |
| **AI Workers** | Order-Ops AI, CX AI |
| **Founder** | Xử lý ngoại lệ lớn + khiếu nại nghiêm trọng |

#### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Đơn hàng (Etsy/Shopify), Printify production status, tracking, tin nhắn khách, yêu cầu return |
| **Control** | Etsy SLA (ship on-time, phản hồi <24h), return policy, GDPR (dữ liệu khách), provider SLA |
| **Output** | Đơn được xử lý, tracking gửi khách, ticket resolved, return/refund xử lý, CX report |
| **Mechanism** | Etsy/Shopify API, Printify API, Claude API (multilingual reply), helpdesk |

#### SOPs
| Mã | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-FUL-001 | Order monitoring & exception | OPERATIONAL | Order-Ops AI |
| SOP-FUL-002 | Production & shipping tracking | OPERATIONAL | Order-Ops AI |
| SOP-FUL-003 | Customer support (multilingual) | OPERATIONAL | CX AI |
| SOP-FUL-004 | Returns / refund / complaint | OPERATIONAL | CX AI |
| SOP-FUL-005 | Return & shipping policy | DOC-ONLY | — |

#### KPI / Quality Gate
| KPI | Target | SLI → SLO / SLA |
|---|---|---|
| Đơn xử lý đúng hạn | 100% | Production confirm ≤ 24h |
| First response time (CSKH) | SLO ≤ 4h · SLA ≤ 24h | — |
| Resolution rate | ≥ 90% | — |
| Shop rating | ≥ 4.8 | Star Seller |
| Return/complaint backlog | 0 quá hạn | — |

---

### 3.5 Department 05 — Backoffice

#### Tổng quan
| Trường | Giá trị |
|---|---|
| **Phạm vi** | Bookkeeping, đối soát phí, profit-per-SKU, VAT/OSS/IOSS, GPSR & GDPR compliance, AI workforce mgmt, admin |
| **Mục tiêu** | Số liệu chính xác, compliance EU 100%, AI workforce vận hành ổn định |
| **AI Workers** | Finance AI, Compliance AI, Ops/HR AI |
| **Founder** | Duyệt báo cáo tài chính + quyết định compliance |

#### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Etsy/Shopify payouts, Printify invoices, ad spend, đơn hàng theo nước, AI usage/cost, quy định EU |
| **Control** | Chuẩn kế toán, lịch VAT/OSS, GPSR (Responsible Person), GDPR, Etsy policy |
| **Output** | Sổ sách, báo cáo P&L, profit-per-SKU, kê khai VAT/OSS, compliance register, AI workforce report |
| **Mechanism** | Google Sheets/Xero, Etsy/Printify/Shopify API, Claude API |

#### SOPs
| Mã | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-BCK-001 | Bookkeeping & fee reconciliation | OPERATIONAL | Finance AI |
| SOP-BCK-002 | VAT / OSS / IOSS | OPERATIONAL | Finance AI |
| SOP-BCK-003 | Profit-per-SKU & financial report | OPERATIONAL | Finance AI |
| SOP-BCK-004 | GPSR compliance (Responsible Person, labeling) | OPERATIONAL | Compliance AI |
| SOP-BCK-005 | GDPR & data handling | OPERATIONAL | Compliance AI |
| SOP-BCK-006 | AI workforce management | OPERATIONAL | Ops/HR AI |
| SOP-BCK-007 | Legal & registration calendar | DOC-ONLY | — |

#### KPI / Quality Gate
| KPI | Target |
|---|---|
| Financial accuracy | ≥ 99% |
| VAT/OSS kê khai đúng hạn | 100% |
| GPSR compliance coverage | 100% listing EU |
| Báo cáo tháng | Trước ngày 5 |
| AI worker uptime | ≥ 99% |

---

## 4. Folder Structure (channel-agnostic)

```
pod-eu-opc/
│
├── README.md                          ← Tổng quan công ty + hướng dẫn vận hành
│
├── 00-company/
│   ├── README.md                      ← Org chart, value chain
│   ├── charter_company-charter_v1.0_2026-06-03.md
│   ├── charter_vision-mission-values_v1.0_2026-06-03.md
│   ├── charter_business-strategy_v1.0_2026-06-03.md
│   ├── okr_company-001_company-okr_v1.0_2026-06-03.md
│   ├── flow_value-chain_v1.0_2026-06-03.md
│   └── matrix_org-chart_v1.0_2026-06-03.md
│
├── 01-product-studio/
│   ├── README.md                      ← IPO + RACI + KPI + OKR
│   ├── charter.md
│   ├── _knowledge/  _workflow/  _skills-agents/  _rules/
│   ├── niche-research/        ← SOP-PRD-001 (template/input/processing/output/archive)
│   ├── trend-seasonal-scan/   ← SOP-PRD-002
│   ├── design-production/     ← SOP-PRD-003
│   ├── design-qc-ip/          ← SOP-PRD-004
│   ├── niche-selection-criteria.md   ← SOP-PRD-005 (doc-only)
│   ├── okr_prd-001_… · kri_prd-001_… · kpi_prd-001_… · quality_prd-001_…
│   └── reports/ (weekly/ monthly/)
│
├── 02-merchandising/
│   ├── README.md · charter.md · _knowledge/_workflow/_skills-agents/_rules/
│   ├── create-listing-seo/    ← SOP-MER-001
│   ├── printify-setup/        ← SOP-MER-002
│   ├── pricing-margin/        ← SOP-MER-003
│   ├── channel-sync-qc/       ← SOP-MER-004
│   ├── listing-template-style.md     ← SOP-MER-005 (doc-only)
│   └── okr/kri/kpi/quality + reports/
│
├── 03-growth/
│   ├── README.md · charter.md · KWSR
│   ├── pinterest-social/      ← SOP-GRW-001
│   ├── ads-management/        ← SOP-GRW-002
│   ├── email-promotions/      ← SOP-GRW-003
│   ├── growth-report/         ← SOP-GRW-004
│   ├── brand-channel-policy.md       ← SOP-GRW-005 (doc-only)
│   └── okr/kri/kpi/quality + reports/
│
├── 04-fulfillment-cx/
│   ├── README.md · charter.md · KWSR
│   ├── order-monitoring/      ← SOP-FUL-001
│   ├── shipping-tracking/     ← SOP-FUL-002
│   ├── customer-support/      ← SOP-FUL-003
│   ├── returns-complaints/    ← SOP-FUL-004
│   ├── return-shipping-policy.md     ← SOP-FUL-005 (doc-only)
│   └── okr/kri/kpi/quality + reports/
│
├── 05-backoffice/
│   ├── README.md · charter.md · KWSR
│   ├── bookkeeping/           ← SOP-BCK-001
│   ├── vat-oss-ioss/          ← SOP-BCK-002
│   ├── profit-financial-report/ ← SOP-BCK-003
│   ├── gpsr-compliance/       ← SOP-BCK-004
│   ├── gdpr-data/             ← SOP-BCK-005
│   ├── ai-workforce-mgmt/     ← SOP-BCK-006
│   ├── legal-registration-calendar.md ← SOP-BCK-007 (doc-only)
│   └── okr/kri/kpi/quality + reports/
│
├── _shared/
│   ├── templates/             ← sop, report, listing, pricing-sheet templates
│   ├── policies/              ← data-protection, ip-policy, brand-policy
│   ├── glossary/
│   └── channel-config/        ← ⭐ tách cấu hình kênh
│       ├── etsy.md
│       ├── printify.md
│       └── shopify.md         ← thêm ở Phase 2, SOP không đổi
│
├── _quality/
│   ├── README.md
│   ├── register_incidents_v1.0_2026-06-03.md
│   └── reports/
│
└── _ai-workforce/
    ├── README.md
    ├── workforce-map_v1.0_2026-06-03.md
    ├── build-plan_v1.0_2026-06-03.md
    ├── skills-matrix_v1.0_2026-06-03.md
    └── cost-analysis_v1.0_2026-06-03.md
```

> **Điểm thiết kế quan trọng:** `_shared/channel-config/` cô lập mọi khác biệt giữa Etsy/Printify/Shopify. SOP-MER-004 (channel sync) đọc config theo kênh → Phase 2 thêm Shopify chỉ cần thêm `shopify.md` + bật cờ, **không sửa SOP**.

---

## 5. AI Workforce Blueprint

| # | AI Worker | Dept | Vai trò | Phương pháp | Tự động |
|---|---|---|---|---|---|
| 1 | **Niche Research AI** | 01 | Niche/keyword/trend research, demand validation | EXPERT-CLONE | 80% |
| 2 | **Design AI** | 01 | Design brief, tạo design (prompt image-gen), QC + IP check | GPS-ENHANCED | 70% |
| 3 | **Listing-SEO AI** | 02 | Listing copy, Etsy SEO, nhãn GPSR | TEMPLATED | 85% |
| 4 | **Catalog-Sync AI** | 02 | Printify setup, pricing, channel sync, catalog QC | GPS-ENHANCED | 80% |
| 5 | **Marketing AI** | 03 | Pinterest/social, email, promotions | TEMPLATED | 85% |
| 6 | **Ads AI** | 03 | Etsy/Meta Ads, ROAS optimization, report | EXPERT-CLONE | 80% |
| 7 | **Order-Ops AI** | 04 | Order monitoring, production/shipping tracking, exception | TEMPLATED | 90% |
| 8 | **CX AI** | 04 | CSKH đa ngôn ngữ, returns, complaints | GPS-ENHANCED | 80% |
| 9 | **Finance AI** | 05 | Bookkeeping, fee reconciliation, profit-per-SKU, VAT/OSS | EXPERT-CLONE | 85% |
| 10 | **Compliance AI** | 05 | GPSR, GDPR, Etsy policy monitoring | EXPERT-CLONE | 75% |
| 11 | **Ops/HR AI** | 05 | AI workforce mgmt, performance, capacity | TEMPLATED | 90% |

> **Thứ tự build (build-plan):** ưu tiên các worker nằm trên critical path "ra hàng + an toàn pháp lý" trước → **Niche Research → Design → Listing-SEO → Catalog-Sync → Compliance (GPSR) → Order-Ops → CX → Finance → Marketing → Ads → Ops/HR**.

> Mỗi AI Worker build bằng skill `vibe-aiworkforce` (KWSR: Knowledge → Workflow → Skill → Rule), với SLI/SLO gắn vào `quality_[dept]`.

---

## 6. Compliance EU

> Đây là phần "Control" sống còn của POD apparel EU — thiết kế thành SOP bắt buộc, không phải tùy chọn.

### 6.1 VAT / OSS / IOSS — `SOP-BCK-002`
- Theo dõi doanh thu B2C theo từng nước EU; khi vượt €10,000/năm xuyên biên giới → đăng ký **OSS** và kê khai VAT theo thuế suất nước khách.
- Nếu print **ngoài EU** (hàng nhập <€150) → cân nhắc **IOSS** thu VAT tại điểm bán. → **Khuyến nghị: chọn print provider EU để né phức tạp IOSS + hải quan.**
- Lịch kê khai OSS theo quý; checklist + reminder trong SOP.

### 6.2 GPSR — `SOP-BCK-004` + check trong `SOP-MER-001`
- Mọi listing apparel bán vào EU phải có: tên + địa chỉ **Responsible Person trong EU**, thông tin nhà sản xuất (Printify provider), cảnh báo an toàn nếu áp dụng.
- Quality gate trong SOP-MER-001: listing **không được publish** nếu thiếu nhãn GPSR.
- Compliance AI giám sát thay đổi quy định + audit định kỳ.

### 6.3 GDPR — `SOP-BCK-005`
- Dữ liệu khách EU lưu trữ tối thiểu cần thiết, có quy trình xóa theo yêu cầu, privacy notice.
- CX AI (SOP-FUL-003) tuân thủ khi xử lý dữ liệu cá nhân.

### 6.4 IP / Copyright — `SOP-PRD-004`
- Quality gate bản quyền **bắt buộc** trước khi design vào listing (rủi ro gỡ shop lớn nhất của POD).
- Design rủi ro cao → escalate Founder duyệt.

---

## 7. Roadmap Triển khai

### Phase 0 — Thiết kế (đã xong)
- [x] Analysis (`01-analysis/`)
- [x] Design Roadmap (tài liệu này)

### Phase 1 — Dựng OPC + Launch Etsy + Printify (Tuần 1–4)

| Tuần | Trọng tâm | Output chính |
|---|---|---|
| **Tuần 1 — Foundation** | Folder structure + company charter + 5 dept README/charter + **Backoffice compliance SOP ưu tiên** (BCK-002 VAT, BCK-004 GPSR, BCK-005 GDPR) | Khung công ty + rào pháp lý sẵn sàng |
| **Tuần 2 — Core pipeline** | Product Studio SOP (PRD-001→004) + Merchandising SOP (MER-001→004) + Fulfillment SOP (FUL-001→004) + `channel-config/etsy.md`, `printify.md` + templates | Pipeline "research → listing → đơn → fulfillment" chạy được |
| **Tuần 3 — Growth + Populate** | Growth SOP (GRW-001→004) + dummy data (niche list, 10-20 listing mẫu, vài đơn mẫu) + cross-link SOP + quality check | Dữ liệu dry-run + bộ SOP liên kết |
| **Tuần 4 — Launch** | Dry-run 5 dept → fix → build AI Workers critical path → **GO-LIVE Etsy + Printify** | OPC vận hành thật trên Etsy |

### Milestone checklist Phase 1
```
[ ] Tuần 1: Foundation
    [ ] Folder structure 5 dept + _shared/_quality/_ai-workforce
    [ ] Company charter + OKR
    [ ] Backoffice compliance SOP (VAT, GPSR, GDPR)
[ ] Tuần 2: Core pipeline
    [ ] Product Studio + Merchandising + Fulfillment SOP
    [ ] channel-config Etsy + Printify
[ ] Tuần 3: Growth + Populate
    [ ] Growth SOP + dummy data + cross-link
[ ] Tuần 4: Launch
    [ ] Dry-run + AI Workers + GO-LIVE Etsy
```

### Phase 2 — Thêm Shopify (Tuần 5–6)
- Thêm `_shared/channel-config/shopify.md`
- Mở rộng `SOP-MER-004` (sync Etsy ↔ Shopify), `SOP-GRW-002` (Meta/Shopify Ads), `SOP-FUL-001` (đơn Shopify), `SOP-BCK-001/002` (payout & VAT Shopify)
- **Không đập SOP cũ** — chỉ bật cờ kênh Shopify.

---

## 8. Channel Rollout

```
Phase 1 (Tuần 1-4):  Etsy (marketplace) + Printify (fulfillment EU)
                     → tận dụng traffic sẵn có của Etsy, validate niche/design nhanh
                          ↓
Phase 2 (Tuần 5-6):  + Shopify (own store)
                     → giảm phụ thuộc Etsy, biên lợi nhuận cao hơn, own customer data,
                       scale Ads (Meta/Google)
```

**Vì sao thứ tự này:** Etsy có sẵn lưu lượng người mua → validate design/niche với rủi ro thấp, không cần chi Ads ngay. Khi đã có winning design → đẩy lên Shopify để giữ biên lợi nhuận và sở hữu khách hàng. Thiết kế channel-agnostic đảm bảo chuyển đổi không tốn rework.

---

## 9. Dummy Data Plan

Để dry-run trước khi go-live (Tuần 3):

| Loại dummy data | Số lượng | Vị trí |
|---|---|---|
| Validated niche list | 5-10 niche | `01-product-studio/niche-research/output/` |
| Design brief + mockup mẫu | 10-20 | `01-product-studio/design-production/output/` |
| Listing mẫu (Etsy SEO + GPSR label) | 10-20 | `02-merchandising/create-listing-seo/output/` |
| Pricing sheet | 1 | `02-merchandising/pricing-margin/output/` |
| Đơn hàng mẫu + tracking | 5-10 | `04-fulfillment-cx/order-monitoring/output/` |
| Ticket CSKH mẫu | 5 | `04-fulfillment-cx/customer-support/output/` |
| Sổ doanh thu + profit-per-SKU mẫu | 1 tháng | `05-backoffice/profit-financial-report/output/` |
| Incident mẫu (RCA) | 1-2 | `_quality/reports/` |

---

## Bước tiếp theo

Sau khi Founder duyệt Design Roadmap này:
1. **Scaffold folder structure** 5 dept + `_shared/_quality/_ai-workforce` (chạy `vibe-company-orchestrator` hoặc dựng thủ công theo Section 4).
2. **Viết SOP** theo thứ tự Roadmap Phase 1 (ưu tiên compliance tuần 1).
3. **Build AI Workers** critical path bằng `vibe-aiworkforce`.
4. **Dry-run → Go-live Etsy + Printify**.

> Cập nhật các giả định tài chính (Section 5 của Analysis) và niche cụ thể trước khi scaffold để số liệu KPI/OKR sát thực tế.
