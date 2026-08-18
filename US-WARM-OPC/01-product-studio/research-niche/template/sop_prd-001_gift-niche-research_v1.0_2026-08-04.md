# SOP-PRD-001 — Gift Niche Research (Personalized Blankets, US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 01-Product Studio · **Responsible AI:** `vibe-us-warm-prd-niche-research`
**Market:** US · **Product focus:** Personalized fleece/sherpa blankets

---

## 1. Tổng quan & Mục tiêu
Research & chấm điểm **niche quà tặng cá nhân hoá** cho chăn (không phải multi-niche AOP như model cũ). Trục niche = **occasion × relationship × recipient**:
- Occasion: Christmas, Valentine's, Mother's/Father's Day, anniversary, memorial.
- Relationship: to my daughter/son/wife/husband/mom/dad/grandma.
- Recipient special: **pet & pet-memorial**, new baby, deployment/military.

Mục tiêu: xuất **validated niche list** (JSON) để feed design (PRD-002). Chỉ pass niche có demand thật + IP an toàn + margin đạt.

## 2. IPO / ICOM
- **Input:** occasion calendar (US), gift-search demand signals, competitor blanket offers (customwarms & peers), unit-economics.
- **Control:** rubric demand40/competition25/margin-fit20/ip-risk15; gate demand_score ≥ 70; audience proxy ≥ 500k; seasonal design-deadline ≥ 6 tuần trước peak.
- **Output:** `niche-validation.json` (schema `niche-validation.schema.json`), evidence-bound.
- **Mechanism:** Google Trends (gift terms), Meta Ad Library (competitor gift ads), Etsy/Amazon gift best-sellers, AdSpy; unit-economics.md.

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Demand | Trends + gift-search volume theo occasion×relationship; ad longevity đối thủ | Chỉ dùng số đo được; thiếu tool → đánh dấu estimate + hạ confidence |
| 3.2 | Competition | Đếm ad-volume/ad-age <90d cho gift-blanket cùng niche | Không suy competition từ 1 nguồn |
| 3.3 | Margin-fit | Chiếu unit-economics: chăn $49.95–59.95 có đạt floor 15% sau CPA không | KHÔNG dùng gross ảo; dùng contribution + BE-ROAS |
| 3.4 | IP pre-flag | Cờ sớm: tên nhân vật/licensed/quote/logo/photo-of-celebrity | HIGH → bắt buộc đẩy PRD-003 trước design |
| 3.5 | Seasonal | Xác định peak_week + design_deadline (≥6 tuần) | Trễ deadline → watchlist, không launch gấp |
| 3.6 | Score & decide | Tổng rubric → validated / watchlist / rejected | confidence < 0.7 hoặc data thiếu → need_review=true |

## 4. RACI
- **R:** `vibe-us-warm-prd-niche-research` · **A:** Owner (OPC) · **C:** `vibe-us-warm-prd-design` (design feasibility) · **I:** merchandising.
- **HITL:** IP pre-flag HIGH → Owner; niche mới chưa có benchmark → Owner duyệt watchlist→validated.

## 5. Quality Gate (SLI → SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | Demand score | ≥ 70 | rubric | < 70 → watchlist/reject |
| 2 | Audience proxy US | ≥ 500k | Meta/estimate | thiếu → need_review |
| 3 | Margin-fit | contribution ≥ 15% @ CPA mục tiêu | unit-economics | fail → reject/repricing |
| 4 | IP pre-flag | ≠ HIGH để auto-continue | rubric | HIGH → PRD-003 mandatory |
| 5 | Evidence | ≥1 evidence/claim, verbatim | validator `--run-all` | thiếu → confidence −0.2 |

**Decision:** all pass + confidence ≥ 0.7 → `validated` → handoff PRD-002. Ngược lại watchlist/reject/need_review (fail-closed).

## 6. Links
- Design downstream: [SOP-PRD-002](../../design-personalization/template/sop_prd-002_blanket-personalization-design_v1.0_2026-08-04.md)
- IP: [SOP-PRD-003](../../clear-ip/template/sop_prd-003_ip-tm-clearance-us_v1.0_2026-08-04.md)
- Economics: [unit-economics](../../../_shared/unit-economics.md)

## 7. History
| Ver | Date | Change |
|-----|------|--------|
| 1.0 | 2026-08-04 | Khởi tạo cho DAKOfits US personalized-blanket (pivot từ EU AOP). |
