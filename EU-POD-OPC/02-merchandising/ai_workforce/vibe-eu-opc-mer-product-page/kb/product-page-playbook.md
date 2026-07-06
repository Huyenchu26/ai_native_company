# KB — Product Page Playbook (SOP-MER-001)

CRO copywriter cho DAKOfits — POD AOP leggings/activewear đa-niche, traffic 100% FB Ads (~80% mobile). Style tham chiếu Gearbunch. Mọi PDP output mang `evidence[] + confidence_score + need_review`.

## 1. Cấu trúc page mobile CRO (12 elements, target ≥95%)

| # | Element | Ghi chú |
|---|---------|---------|
| 1 | Headline benefit + niche | Above-fold, mobile 1–2 dòng |
| 2 | 5 bullet scannable | Value, không lan man |
| 3 | Description story | Emotional hook + 360° all-over-print show-off |
| 4 | Mockup ảnh | Show AOP 360° |
| 5 | Above-fold CTA | "Add to cart" thấy ngay không scroll |
| 6 | Trust badge | Secure checkout, ship US/EU |
| 7 | Size guide XS–3XL | cm + inch |
| 8 | Care info AOP | Wash/print care |
| 9 | Urgency nhẹ | Limited print run, không fake countdown |
| 10 | Social proof | Rating + review snippet + UGC |
| 11 | Upsell/bundle | Leggings + sports-bra cùng AOP |
| 12 | GPSR label block | Đơn EU (xem §4) |

CRO completeness < 95% (< 12 element pass đủ tỷ lệ) → `need_review=true`, bổ sung trước publish.

## 2. Upsell — sports-bra bundle (bắt buộc)

- Bundle **leggings + sports-bra cùng AOP/niche** để giữ AOV.
- Không có sports-bra cùng niche → upsell **activewear generic** (vẫn phải có 1 upsell).
- Field `upsell_bundle.present` luôn `true`; thiếu = fail quality gate.

## 3. Social proof

- Rating + 2–3 review snippet thật + UGC ref.
- KHÔNG bịa rating/review. Thiếu review pool → dùng UGC/no-claim, ghi evidence nguồn.

## 4. GPSR label requirement (đơn EU) + VERIFY clearance log ID — FAIL-CLOSED

**Gate cứng: no GPSR clearance → no publish (EU).**

### Quy trình verify (bước 1 SOP)
1. Xác định `market` (US / EU / cả hai).
2. **VERIFY clearance log ID** từ SOP-BCK-004: tra bản ghi có **`status = PASS`** cho đúng SP/design.
3. **KHÔNG chỉ check string nhãn** trên page — nhãn rỗng/giả vẫn pass string. Phải khớp nội dung label với clearance log.

### Fail-closed (mặc định BLOCK)
| Tình huống | Hành động |
|-----------|-----------|
| Thiếu clearance log ID | BLOCK publish, `need_review=true`, escalate phòng 05 |
| Không tìm thấy bản ghi | BLOCK |
| status ≠ PASS (FAIL/NOT_FOUND/MISSING) | BLOCK |
| Không xác nhận được | BLOCK (default) |

### Khi PASS (EU) — chèn GPSR label block
- Tên + địa chỉ **Responsible Person (EU)**.
- Cảnh báo an toàn + care/material.
- Mã SP.
- `gpsr_label_present=true`, render đúng trên PDP EU.

### SP chỉ US
- Bỏ qua GPSR label block (giữ care info). `gpsr_clearance_status=N/A`, `gpsr_label_present=false` là hợp lệ.

## 5. Anti-hallucination
- `evidence[]`: clearance log ID, design ID, SKU nguồn, review source.
- `confidence_score` ≥ 0.7 mới publish.
- `need_review=true` khi: gate block, CRO<95%, thiếu data, không có review thật.

## 6. Links
- SOP-MER-001: `../../write-product-page/template/sop_mer-001_product-page_v1.0_2026-06-23.md`
- Upstream catalog: `vibe-eu-opc-mer-catalog` · Compliance/GPSR: `vibe-opc-pod-backoffice-compliance` (SOP-BCK-004)
- Downstream: `vibe-eu-opc-grw-fb-ads`, `vibe-eu-opc-mer-orchestrator`
