# SOP-MER-002 — Personalization Preview / Mockup (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 02-Merchandising · **Responsible AI:** `vibe-us-warm-mer-visual`

---

## 1. Tổng quan & Mục tiêu
Tạo **preview cá nhân hoá** (khách xem chăn với tên/ảnh của họ) + ảnh mockup listing. KHÔNG phải AOP mockup 360°. 2 phase: **validation-first** (concept/spec) → **production** (render thật khi có supplier/tool).

⚠️ Bài học EU H1: TUYỆT ĐỐI không khai ảnh tồn tại nếu chưa render. Schema hỗ trợ cả 2 phase (fix M4).

## 2. IPO / ICOM
- **Input:** design-spec (layout + variable slots), pricing, personalization fields.
- **Control:** min images theo phase; preview phải phản ánh đúng variable-data; ảnh thật phải tải về local trước khi khai coverage OK.
- **Output:** `mockup-set.json` (schema `mockup-set.schema.json`) — có `phase` (validation/production), `images[]` (type, ratio incl 9:16, local_file, render_status), coverage, evidence, confidence, need_review.
- **Mechanism:** render/preview tool (cần auth — Canva/preview engine).

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Preview spec | Định nghĩa preview slots (tên/ảnh) render thế nào | — |
| 3.2 | Mockup set | Liệt kê ảnh cần (hero, lifestyle, personalization-demo, story 9:16) | ratio enum đủ 9:16 (fix M4) |
| 3.3 | Render | Nếu có tool → render + TẢI LOCAL | Không tool → render_status="not-generated", min_images_met=false (KHÔNG bịa) |
| 3.4 | QC | Đối chiếu file thật vs manifest trước khi set coverage | manifest khai ảnh không có trên đĩa → FAIL (fix H1) |

## 4. RACI
- **R:** mer-visual · **A:** Owner · **C:** prd-design (layout), mer-catalog · **I:** grw (creative reuse).
- **HITL:** ảnh khách chất lượng biên; preview sai variable-data.

## 5. Quality Gate (SLI→SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | Images on disk = manifest | 100% match | file check | mismatch → FAIL (no phantom) |
| 2 | Min images (production) | ≥ 4 | count | production phase fail → block listing |
| 3 | Evidence | verbatim | validator | thiếu → −0.2 |

**Gate (allOf/if-then):** `phase=production ⇒ min_images_met=true ∧ all local_file present`. `phase=validation` → miễn gate ảnh nhưng render_status phải trung thực.

## 6. Links
- Upstream: [pricing](../../set-pricing/template/sop_mer-001_blanket-pricing_v1.0_2026-08-04.md), 01 design-spec
- Downstream: [product-page](../../write-product-page/template/sop_mer-003_gift-product-page_v1.0_2026-08-04.md), 03-growth creative

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — personalization preview, schema 2-phase (fix M4), no-phantom-image gate (fix H1). |
