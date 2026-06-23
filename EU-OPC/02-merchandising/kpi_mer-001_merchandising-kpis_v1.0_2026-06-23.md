# KPI: Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0

---

## 1. KPI chính

| # | KPI | Công thức | Target | Tần suất | Owner | SOP |
|---|-----|-----------|--------|----------|-------|-----|
| 1 | Catalog sync accuracy | field khớp / tổng field | ≥ 99% | mỗi sync | Catalog-Sync AI | MER-004 |
| 2 | GPSR label present rate (EU) | SP EU có label / tổng SP EU | = 100% | mỗi publish | Product-Page AI | MER-001 |
| 3 | Gross margin trung bình | (giá−cost)/giá | ≥ 45% (mục tiêu 45–55%) | mỗi SP | Catalog-Sync AI | MER-003 |
| 4 | Mobile CRO completeness | elements có/12 | ≥ 95% | mỗi PDP | Product-Page AI | MER-001 |
| 5 | Time-to-publish | giờ cleared→live | ≤ 48h | mỗi SP | OPC | MER-002→004 |
| 6 | Setup correctness (provider/variant) | SP đúng setup / tổng | ≥ 98% | mỗi SP | Catalog-Sync AI | MER-002 |
| 7 | Batch winner rate | SP ROAS≥2.5 / SP trong đợt | ≥ 20% | mỗi đợt | OPC | MER-006 |
| 8 | Upsell/bundle attach rate | đơn có bundle / tổng đơn | ≥ 10% | mỗi tuần | Product-Page AI | MER-001 |

## 2. KPI phụ (vận hành)

| KPI | Target | Ghi chú |
|-----|--------|---------|
| Publish throughput | ≥ 40 SP/tuần | OKR O3 |
| Listing defect rate | ≤ 2% | lỗi do Growth/CX báo |
| Variant coverage XS–3XL | 100% size có sẵn | mỗi SP |
| Re-work rate (page trả lại) | ≤ 5% | chất lượng copy |

## 3. KPI → OKR → Company mapping

| KPI | Dept OKR | Company OKR |
|-----|----------|-------------|
| GPSR label rate, Sync accuracy, Time-to-publish | O1 | O2 |
| Gross margin, Mobile CRO, Upsell attach | O2 | O1 |
| Batch winner rate, Publish throughput | O3 | O3 |

## 4. Dashboard / nguồn dữ liệu

- ShopBase admin (catalog, giá, đơn, bundle attach).
- Printify/PrintBase (cost, stock, variant).
- Batch promote log (`promote-batch/output/`) → Growth feedback ROAS/CPA.
- Sync log (`sync-catalog/output/`).
