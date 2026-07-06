# 02-Merchandising (dept code: `mer`)

**Layer:** L2 Vận hành (Operations) · **Value Chain Position:** Inbound→Operations (giữa Product Studio và Growth)
**Owner:** OPC (1 người) + AI Workforce · **Ngày:** 2026-06-23 · **Version:** v1.0

> Phòng Merchandising biến **cleared design + GPSR clearance** thành **live product publish-ready** trên ShopBase (AOP leggings & activewear, đa niche ~3.200 SP), và điều phối **"promote theo đợt"** để Growth chạy ads → scale winner.

---

## 1. Department IPO (I/C/O/M)

| Thành phần | Nội dung |
|-----------|----------|
| **Input (I)** | Cleared AOP design print-ready (300 DPI, 360° QC) từ phòng 01; GPSR clearance log + Responsible Person + nhãn an toàn từ phòng 05; validated niche/batch list; mockup; channel-config (`_shared/channel-config`) |
| **Control (C)** | SOP-MER-001..006; Gate **no-GPSR-no-publish** (đơn EU); pricing floor gross margin ≥45%; mobile CRO checklist; brand voice DAKOfits; ShopBase TOS; Printify/PrintBase provider rules |
| **Output (O)** | Live product trên ShopBase (variant XS–3XL/color, pricing đúng margin); product page copy + upsell/bundle sports-bra; catalog QC pass; batch promote package bàn giao Growth; sync log |
| **Mechanism (M)** | AI Worker `vibe-opc-pod-merch-catalog-sync` + `vibe-opc-pod-merch-product-page`; Printify/PrintBase; ShopBase admin; OPC review/approve |

---

## 2. Value Chain Position (L2)

```
[01-Product-Studio]            [05-Backoffice / Compliance]
  cleared design  ─────┐         GPSR clearance ─────┐
  (300DPI, 360°QC)     │         (Responsible Person)│
                       ▼                              ▼
                ┌──────────────────────────────────────────┐
                │   02-MERCHANDISING  (L2 · dept: mer)      │
                │  setup → pricing → product page → QC →    │
                │  catalog sync → promote theo đợt          │
                └──────────────────────────────────────────┘
                       │  live product + batch promote package
                       ▼
                [03-Growth]  (FB Ads — 100% traffic)
```

- **Upstream:** `01-product-studio` (cleared design), `05-backoffice` (GPSR clearance — gate cứng cho EU).
- **Downstream:** `03-growth` (nhận batch promote → chạy FB Ads → trả kết quả ROAS/CPA để scale/cut).

---

## 3. Internal Process IPOs (theo SOP)

| SOP | Process | Input | Output | AI Worker |
|-----|---------|-------|--------|-----------|
| **MER-002** | Setup product Printify/PrintBase | Cleared design + mockup | Product blueprint (provider US+EU, variant set) | catalog-sync |
| **MER-003** | Set variant pricing | Provider cost + target margin | Variant pricing XS–3XL/color (gross margin 45–55%) | catalog-sync |
| **MER-001** | Viết product page + upsell + GPSR label | Product blueprint + GPSR clearance | Product page copy (mobile CRO, social proof, GPSR label EU) | product-page |
| **MER-004** | Catalog sync + QC | Product page + pricing | ShopBase live product (sync accuracy ≥99%) | catalog-sync |
| **MER-006** | Promote theo đợt | Live products (batch 5–10 SP) | Batch promote package → Growth; scale/cut decision | (OPC + cả 2 worker) |

---

## 4. RACI (Department-level)

| Hoạt động | OPC | Catalog-Sync AI | Product-Page AI | 01-Product-Studio | 05-Backoffice | 03-Growth |
|-----------|-----|-----------------|-----------------|-------------------|---------------|-----------|
| Setup Printify/PrintBase (MER-002) | A | **R** | C | C | I | I |
| Pricing variant (MER-003) | A | **R** | I | I | C | I |
| Product page + GPSR label (MER-001) | A | I | **R** | C | **C (gate)** | I |
| Catalog sync + QC (MER-004) | A | **R** | C | I | I | I |
| Promote theo đợt (MER-006) | **A/R** | C | C | I | I | **C** |

A=Accountable, R=Responsible, C=Consulted, I=Informed.

---

## 5. KPI Summary

| KPI | Target | Nguồn |
|-----|--------|-------|
| Catalog sync accuracy | ≥ 99% | MER-004 |
| GPSR label present rate (EU) | = 100% | MER-001 |
| Gross margin trung bình | ≥ 45% (mục tiêu 45–55%) | MER-003 |
| Product page mobile CRO completeness | ≥ 95% elements | MER-001 |
| Time-to-publish (cleared → live) | ≤ 48h | MER-002→004 |
| Batch winner rate (ROAS≥2.5) | ≥ 20% SP/đợt | MER-006 |

Chi tiết: [`kpi_mer-001_merchandising-kpis_v1.0_2026-06-23.md`](kpi_mer-001_merchandising-kpis_v1.0_2026-06-23.md)

---

## 6. OKR Summary

- **O1 (Committed):** Catalog đúng-luật & publish-ready → 100% SP EU có GPSR label, sync accuracy ≥99%. *Align Company O1, O2.*
- **O2 (Committed):** Margin chuẩn → 100% SP gross margin ≥45%. *Align Company O1.*
- **O3 (Stretch x10):** Pipeline đa-niche tự động → publish ≥500 SP/quý, ≥100 winner SKU. *Align Company O3.*

Chi tiết: [`okr_mer-001_quarterly-okr_v1.0_2026-06-23.md`](okr_mer-001_quarterly-okr_v1.0_2026-06-23.md)

---

## 7. Quality Standards Summary

| SOP | SLI | SLO |
|-----|-----|-----|
| MER-001 | GPSR label present rate (EU) | = 100% |
| MER-001 | Mobile CRO elements completeness | ≥ 95% |
| MER-002 | Provider/variant setup correctness | ≥ 98% |
| MER-003 | Gross margin floor | ≥ 45% (100% SP) |
| MER-004 | Catalog sync accuracy | ≥ 99% |
| MER-006 | Batch SLA (cleared→ads-ready) | ≤ 5 ngày/đợt |

Chi tiết: [`quality_mer-001_quality-standards_v1.0_2026-06-23.md`](quality_mer-001_quality-standards_v1.0_2026-06-23.md)

---

## 8. AI Integration (SOP → AI Worker)

| SOP | AI Worker (skill) | Vai trò | Human checkpoint |
|-----|-------------------|---------|------------------|
| MER-002 | `vibe-opc-pod-merch-catalog-sync` | Setup blueprint Printify/PrintBase, variant XS–3XL/color | OPC approve blueprint |
| MER-003 | `vibe-opc-pod-merch-catalog-sync` | Tính & set pricing theo margin | OPC approve pricing floor |
| MER-001 | `vibe-opc-pod-merch-product-page` | Viết copy + upsell + chèn GPSR label | OPC review + **gate GPSR** |
| MER-004 | `vibe-opc-pod-merch-catalog-sync` | Sync ShopBase + QC catalog | OPC spot-check QC |
| MER-006 | cả 2 worker (điều phối bởi OPC) | Chuẩn bị batch package, đọc kết quả | OPC quyết scale/cut |

---

## 9. Cấu trúc folder

```
02-merchandising/
├── README.md                         (file này)
├── charter_mer-department_v1.0_*.md
├── okr_mer-001_*.md / kri_mer-001_*.md / kpi_mer-001_*.md / quality_mer-001_*.md
├── setup-printify/      (SOP-MER-002 + I/O/processing/template/archive)
├── set-pricing/         (SOP-MER-003)
├── write-product-page/  (SOP-MER-001)
├── sync-catalog/        (SOP-MER-004)
├── promote-batch/       (SOP-MER-006)
├── _knowledge/  _workflow/  _skills-agents/  _rules/
```
