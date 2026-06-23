# SOP-MER-004 — Catalog Sync + QC (ShopBase)

**Dept:** 02-merchandising (`mer`) · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-merch-catalog-sync` · **Accountable:** OPC

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | Product blueprint (MER-002) + pricing (MER-003) + product page approved (MER-001) |
| **Control (C)** | **Sync accuracy ≥ 99%**; GPSR label gate (EU); variant XS–3XL đủ; ShopBase schema |
| **Output (O)** | Live product trên ShopBase (variant, giá, ảnh, page, GPSR label) + sync log |
| **Mechanism (M)** | Catalog-Sync AI + ShopBase + Printify/PrintBase connector + OPC spot-check |
| **Upstream** | MER-001, MER-002, MER-003 |
| **Downstream** | MER-006 (promote), 03-growth |

---

## 1. Tổng Quan

Đẩy SP từ Printify/PrintBase → ShopBase, đảm bảo catalog khớp (giá, variant, ảnh, stock, page, GPSR label), QC trước/sau publish. Đây là gate cuối trước khi SP live. **No GPSR (EU) → no publish.**

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Catalog-Sync AI | Product-Page AI |
|-----------|-----|-----------------|-----------------|
| Sync ShopBase | A | **R** `[AI WORKFORCE]` | I |
| QC catalog (diff field) | A | **R** `[AI WORKFORCE]` | C |
| Verify GPSR label (EU) | A | **R** | C |
| Approve publish | **A/R** | I | I |

`[AI WORKFORCE]` = skill `vibe-opc-pod-merch-catalog-sync`.

## 3. Quy Trình

### Bước 1 — Pre-sync gate check
| ICOM | Nội dung |
|------|----------|
| I | Blueprint + pricing + page |
| C | GPSR gate, floor margin |
| O | Go/no-go publish |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Kiểm SP EU có GPSR label + clearance → nếu thiếu **STOP** | AI |
| Kiểm margin ≥ 45%, variant XS–3XL đủ | AI |

### Bước 2 — Sync ShopBase
| ICOM | Nội dung |
|------|----------|
| I | SP đã pass gate |
| C | ShopBase schema |
| O | SP đẩy lên ShopBase |
| M | Catalog-Sync AI + connector |

| Hành động | Ai |
|-----------|-----|
| Sync variant, giá, ảnh/mockup, page copy, GPSR label | AI `[AI WORKFORCE]` |
| Map provider variant ↔ ShopBase SKU | AI |

### Bước 3 — Catalog QC (diff)
| ICOM | Nội dung |
|------|----------|
| I | SP trên ShopBase vs source |
| C | Sync accuracy ≥ 99% |
| O | QC report + accuracy % |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Diff field: giá, variant, ảnh, stock, page, label | AI `[AI WORKFORCE]` |
| Tính sync accuracy; field lệch → re-sync | AI |

### Bước 4 — Publish & log
| ICOM | Nội dung |
|------|----------|
| I | SP QC pass |
| C | Quality Gate MER-004 |
| O | Live product + sync log |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| OPC spot-check → publish | OPC |
| Ghi sync log vào `sync-catalog/output/` | AI |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| SP EU thiếu GPSR label | STOP, trả MER-001 |
| Sync accuracy < 99% | Re-sync field lệch |
| Provider OOS variant | Ẩn variant / đổi provider |
| Ảnh mockup lỗi | Re-render (MER-002) |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| Catalog sync accuracy | ≥ 99% | diff field |
| GPSR label present (EU) | = 100% | check PDP |
| Variant XS–3XL coverage | 100% | count |
| Listing defect rate | ≤ 2% | feedback Growth/CX |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Publish EU thiếu GPSR | Pre-sync gate bước 1 |
| Giá/variant lệch → đơn lỗi | QC diff bước 3 |
| Stock sai → đơn treo | Sync stock real-time |

## 6. Tài Nguyên & Links

- Template: `sync-catalog/template/`
- Upstream: [SOP-MER-001](../../write-product-page/template/sop_mer-001_product-page_v1.0_2026-06-23.md), [MER-002](../../setup-printify/template/sop_mer-002_printify-setup_v1.0_2026-06-23.md), [MER-003](../../set-pricing/template/sop_mer-003_variant-pricing_v1.0_2026-06-23.md)
- Downstream: [SOP-MER-006](../../promote-batch/template/sop_mer-006_promote-batch_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo SOP catalog sync + QC |
