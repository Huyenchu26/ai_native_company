# SOP-MER-002 — Setup Product Printify/PrintBase

**Dept:** 02-merchandising (`mer`) · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-merch-catalog-sync` · **Accountable:** OPC

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | Cleared AOP design print-ready (300 DPI, 360° QC pass) từ phòng 01; mockup; niche/batch info; channel-config (`_shared/channel-config`) |
| **Control (C)** | Printify/PrintBase blueprint rules; provider US+EU; variant set chuẩn XS–3XL/color; design QC gate |
| **Output (O)** | Product blueprint: provider chọn, AOP áp lên leggings/activewear, variant size XS–3XL × color, mockup render |
| **Mechanism (M)** | Catalog-Sync AI + Printify/PrintBase + OPC approve |
| **Upstream** | 01-product-studio (cleared design) |
| **Downstream** | MER-003 (pricing) |

---

## 1. Tổng Quan

Setup SP AOP leggings/activewear trên Printify/PrintBase, chọn provider (US cho đơn US, EU cho đơn EU để giảm ship time/VAT), tạo full variant XS–3XL × color, render mockup. Đây là bước đầu của pipeline catalog.

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Catalog-Sync AI | 01-Product-Studio |
|-----------|-----|-----------------|-------------------|
| Chọn provider (US/EU, Printify/PrintBase) | A | **R** `[AI WORKFORCE]` | I |
| Áp design + tạo variant XS–3XL/color | A | **R** `[AI WORKFORCE]` | C |
| QC mockup render 360° | A | **R** | C |
| Approve blueprint | **A/R** | I | I |

`[AI WORKFORCE]` = skill `vibe-opc-pod-merch-catalog-sync`.

## 3. Quy Trình

### Bước 1 — Verify cleared design
| ICOM | Nội dung |
|------|----------|
| I | Design print-ready + IP-clearance log |
| C | Design QC gate (300 DPI, 360°) |
| O | Design go/no-go |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Kiểm design 300 DPI, IP cleared, 360° QC pass | AI |
| Nếu fail → trả phòng 01 | AI |

### Bước 2 — Chọn provider & blueprint
| ICOM | Nội dung |
|------|----------|
| I | Thị trường target, channel-config |
| C | Provider rule US+EU |
| O | Provider + blueprint chọn |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Map thị trường → provider (US→US provider, EU→EU provider giảm VAT/ship) | AI `[AI WORKFORCE]` |
| Chọn blueprint AOP legging/activewear phù hợp | AI |

### Bước 3 — Áp design + tạo variant
| ICOM | Nội dung |
|------|----------|
| I | Design + blueprint |
| C | Variant set XS–3XL/color |
| O | SP full variant + mockup |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Áp AOP 360° lên blueprint | AI `[AI WORKFORCE]` |
| Tạo variant size XS–3XL × tất cả color | AI |
| Render mockup, QC alignment seam/print | AI |

### Bước 4 — OPC approve
| ICOM | Nội dung |
|------|----------|
| I | Blueprint + mockup |
| C | Quality Gate MER-002 |
| O | Blueprint approved → MER-003 |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Spot-check variant coverage + mockup | OPC |
| Approve → bàn giao pricing | OPC |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| Bán cả US & EU | Setup 2 blueprint (provider US + EU) |
| Design fail QC | Trả phòng 01 |
| Blueprint thiếu size XS hoặc 3XL | Đổi blueprint hỗ trợ đủ XS–3XL |
| Provider OOS blank | Chọn provider thay thế cùng vùng |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| Setup correctness | ≥ 98% | so blueprint chuẩn |
| Variant coverage XS–3XL | 100% size | count |
| Mockup 360° alignment | pass | QC visual |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Sai provider → ship lâu/VAT cao | Map thị trường→provider bước 2 |
| Thiếu size → mất đơn | Variant coverage check |
| Print lệch seam | QC mockup bước 3 |

## 6. Tài Nguyên & Links

- Template: `setup-printify/template/`
- Upstream: phòng 01-product-studio (cleared design)
- Downstream: [SOP-MER-003](../../set-pricing/template/sop_mer-003_variant-pricing_v1.0_2026-06-23.md)
- Knowledge: [`_knowledge/README.md`](../../_knowledge/README.md)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo SOP setup Printify/PrintBase |
