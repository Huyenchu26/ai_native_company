# 02 — Merchandising

> Listing + Etsy SEO · Printify setup · pricing/margin · channel sync & catalog QC.
> Chi tiết: [Design Roadmap §3.2](../02-design/opc-design-roadmap.md)

## Department IPO
| Component | Detail |
|---|---|
| **Input** | Design + mockup (từ 01), keyword data, Printify catalog & giá in, channel config |
| **Control** | Etsy SEO (title ≤140, 13 tags), pricing floor (margin ≥30%), GPSR labeling, brand voice |
| **Output** | Published listing, Printify product, pricing sheet, sync log, catalog QC report |
| **Mechanism** | Etsy API, Printify API, Shopify API (Phase 2), Claude API, eRank |

## Value Chain Position
- **Layer:** Operations (Outbound)
- **Upstream:** 01 Product Studio · **Downstream:** 03 Growth, 04 Fulfillment

## SOP Index
| SOP | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-MER-001 | Tạo listing + Etsy SEO (+ GPSR) | OPERATIONAL | Listing-SEO AI |
| SOP-MER-002 | Printify setup + chọn EU provider | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-003 | Pricing & margin | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-004 | Channel sync & catalog QC | OPERATIONAL | Catalog-Sync AI |
| SOP-MER-005 | Listing template & brand style | DOC-ONLY | — |

## KPIs (xem kpi_mer-001)
| KPI | Target |
|---|---|
| Listing publish/tuần | ≥ 10 |
| SEO completeness (≥13 tags, ≥5 ảnh) | 100% |
| Margin/SKU | ≥ 30% |
| Provider EU coverage | ≥ 90% |
| GPSR label present | 100% |
