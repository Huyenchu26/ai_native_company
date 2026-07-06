# OKR: Phòng 02-Merchandising — Q3 2026

**Quý:** Q3 2026 · **Set bởi:** OPC · **Ngày:** 2026-06-23 · **Version:** v1.0

> v2.0 Evidence-bound: mọi target có `evidence` + `confidence_score` + `need_review`. Stretch (x10) → `need_review = true` → vào review-queue.

---

## COMMITTED OKR (target 100%)

### O1: Catalog đúng-luật & publish-ready (→ Company O1, O2)
| KR | Metric | Baseline | Target | KRI | Evidence | confidence | need_review |
|----|--------|----------|--------|-----|----------|-----------|-------------|
| KR1 | GPSR label present rate (đơn EU) | — | **100%** | gpsr_label_rate | Gate cứng no-GPSR-no-publish (SOP-BCK-004) | 0.85 | false |
| KR2 | Catalog sync accuracy | ~96% | **≥ 99%** | sync_accuracy | Sai số sync ShopBase hiện ~4% (manual estimate) | 0.7 | false |
| KR3 | Time-to-publish (cleared→live) | ~3 ngày | **≤ 48h** | time_to_publish | Pipeline 2 worker, không có bottleneck design | 0.65 | false |

### O2: Margin & conversion chuẩn (→ Company O1)
| KR | Metric | Baseline | Target | KRI | Evidence | confidence | need_review |
|----|--------|----------|--------|-----|----------|-----------|-------------|
| KR1 | Gross margin trung bình | ~45% | **≥ 48%** | gross_margin | Provider cost AOP legging US+EU + giá ref Gearbunch | 0.75 | false |
| KR2 | Product page mobile CRO completeness | ~80% | **≥ 95%** | cro_completeness | Checklist CRO 12 elements (SOP-MER-001) | 0.7 | false |
| KR3 | Upsell/bundle attach rate (sports-bra) | ~5% | **≥ 10%** | upsell_attach | Bundle hiển thị 100% PDP | 0.55 | false |

---

## STRETCH OKR (MOONSHOT x10 — target 70% = success)

### O3: Pipeline đa-niche tự động hóa (→ Company O3)

> ⚠️ **Ràng buộc capacity (OPC là bottleneck, solo + 2 worker):** volume thô x10 chỉ khả thi **NẾU zero-touch (KR3) đạt TRƯỚC** — KR3 là điều kiện tiên quyết (gating) cho KR1/KR2. Vì vậy KR chính ưu tiên là **% tự-động-hóa / % winner**, KHÔNG phải volume thô. **Trần cứng: doanh thu KHÔNG vượt 500tr VND/tháng** dù pipeline mở rộng (tránh scale lỗ + quá tải vận hành/CX/fulfillment). Volume 500 SP/quý chỉ là moonshot tham chiếu, **bị chặn bởi KR3 + trần doanh thu**.

| KR | Metric | Baseline | x10 Target | Approach Difference | Evidence | confidence | need_review |
|----|--------|----------|-----------|---------------------|----------|-----------|-------------|
| KR3 (gate) | **Zero-touch publish rate** | ~0% | **80%** | AI tự publish khi pass đủ gate (GPSR fail-closed + contribution floor + QC), OPC chỉ spot-check. **Phải đạt trước KR1/KR2.** | Chưa có gate tự động hóa | 0.3 | **true** |
| KR1 | SP publish-ready / quý (% tự-động-hóa) | ~50 | **500 — CHỈ sau khi KR3≥80%; ưu tiên % tự-động-hóa hơn số tuyệt đối** | Batch-pipeline 2 worker tự setup→price→page→sync song song; volume bị chặn bởi zero-touch + trần 500tr/tháng | Không có benchmark nội bộ cho x10; OPC bottleneck | 0.35 | **true** |
| KR2 | % winner trong SP đã promote (ROAS ≥ BE-ROAS) | ~10 SP | **% winner ↑ (mục tiêu chất lượng), trong giới hạn 500tr/tháng** | Promote theo đợt (SOP-MER-006), scale tự động winner; **đo % winner thay vì 100 winner thô** để không vượt trần doanh thu | Phụ thuộc Growth ads + BE-ROAS per SKU (MER-003) | 0.3 | **true** |

> Stretch O3 → toàn bộ `need_review = true` → [review-queue](../output/review-queue.md).

---

## Alignment — Department → Company

| Dept OKR | → Company OKR | Contribution |
|----------|--------------|--------------|
| O1 (GPSR + sync + time) | → Company O2 (đúng luật/đúng hạn) | Cao |
| O2 (margin + CRO) | → Company O1 (doanh số có lãi) | Cao |
| O3 (pipeline x10) | → Company O3 (bùng nổ winner đa-niche) | Cao |
