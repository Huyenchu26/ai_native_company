# SOP-MER-003 — Gift Product Page / Listing (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 02-Merchandising · **Responsible AI:** `vibe-us-warm-mer-product-page`

---

## 1. Tổng quan & Mục tiêu
Viết listing chăn cá nhân hoá — **gift-emotional copy** + UX cá nhân hoá (nhập tên/ảnh) + tuân thủ **US/FTC**. Khác EU: không GPSR, thay bằng CPSC textile label note + FTC (no fake review, disclosure).

## 2. IPO / ICOM
- **Input:** pricing, preview, design (niche + personalization fields), IP clearance_id.
- **Control:** FTC no-deceptive-claim + no-fake-review; CPSC textile fiber label present; personalization UX rõ (max ký tự, ảnh requirement); final-sale disclosure (personalized).
- **Output:** `product-page.json` (schema `product-page.schema.json`) — title, bullets, description, personalization_ux, care_label, ftc_flags, publish_status (enum incl **blocked**), evidence, confidence, need_review.
- **Mechanism:** copy playbook, FTC/CPSC checklist.

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Gift copy | Headline + bullets + story (occasion/relationship) | Không bịa review/rating/số bán |
| 3.2 | Personalization UX | Field nhập tên/ảnh + preview link | Ghi rõ giới hạn + ảnh requirement |
| 3.3 | Compliance | CPSC fiber label + care; FTC disclosure; final-sale note | thiếu label → publish_status=blocked |
| 3.4 | QC self-check | prose-scan chống deceptive/fake (validator --prose) | claim "guaranteed/100%/™" chưa verify → block |

## 4. RACI
- **R:** mer-product-page · **A:** Owner · **C:** bck-compliance (FTC/CPSC), prd (IP) · **I:** grw.
- **HITL:** compliance uncertain; claim mạnh cần chứng cứ. Escalate compliance → `vibe-us-warm-bck-compliance` (tên đúng — fix D1).

## 5. Quality Gate (SLI→SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | CPSC fiber label | present | field | thiếu → blocked |
| 2 | FTC deceptive/fake | 0 hit | validator --prose | hit → blocked + fix |
| 3 | Final-sale disclosure | present (personalized) | field | thiếu → blocked |
| 4 | Evidence | verbatim | validator | thiếu → −0.2 |

**Gate (allOf/if-then):** `publish_status=publish-ready ⇒ cpsc_label_present=true ∧ ftc_clean=true ∧ final_sale_disclosed=true`. Model được `blocked` state (fix EU P3). min_confidence gate compliance = 1.0 (enforced qua validator threshold).

## 6. Links
- Upstream: [pricing](../../set-pricing/template/sop_mer-001_blanket-pricing_v1.0_2026-08-04.md), [preview](../../personalization-preview/template/sop_mer-002_personalization-preview_v1.0_2026-08-04.md)
- Compliance: 05-backoffice (bck-compliance) · Downstream: [catalog-sync](../../sync-catalog/template/sop_mer-004_catalog-sync_v1.0_2026-08-04.md), 03-growth

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — US/FTC/CPSC (thay GPSR EU), model blocked-state, prose-scan gate, escalate tên đúng. |
