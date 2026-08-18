# Niche Research Playbook — US Personalized Gift Blankets (PRD-001)

**Dept:** 01-product-studio · **Skill:** `vibe-us-warm-prd-niche-research` · **Market:** US · **Product:** personalized fleece/sherpa blankets ($39.95–59.95)

Canonical contracts (paths resolve from THIS `kb/` folder — verified 4-up to repo `_shared/`):
- SOP-PRD-001: [../../../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md](../../../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md)
- Unit economics (margin-fit source of truth): [../../../../_shared/unit-economics.md](../../../../_shared/unit-economics.md)
- Unified evidence contract: [../../../../_shared/schema/evidence.schema.json](../../../../_shared/schema/evidence.schema.json)
- Skill-meta schema: [../../../../_shared/schema/skill-meta.schema.json](../../../../_shared/schema/skill-meta.schema.json)
- Shared validator (harness v2): [../../../../_shared/script/validator.py](../../../../_shared/script/validator.py)
- Product-studio rules: [../../../_rules/README.md](../../../_rules/README.md)
- Company charter: [../../../../00-company/charter_company-charter_v1.0_2026-08-04.md](../../../../00-company/charter_company-charter_v1.0_2026-08-04.md)

> Path-resolution note: from a **subfolder** (`kb/`, `schema/`, `synthetic-data/`) the repo root `_shared/` is **4 levels up** (`../../../../_shared`). From the **skill root** (`SKILL.md`, `skill.json`, validator cwd) it is **3 levels up** (`../../../_shared`). Do not off-by-one.

---

## 1. Scoring rubric (100 pts) — maps to `demand_score`

Weighted per SOP-PRD-001 §2 Control: **demand 40 / competition 25 / margin-fit 20 / ip-risk 15**. Normalize to 0–100.

| Dimension | Weight | 0 pts | Half | Full |
|-----------|:------:|-------|------|------|
| **Demand** | 40 | flat/declining Trends, no ad longevity | moderate + some evergreen | rising Trends **and** competitor ads live >90d, audience proxy ≥ 500k |
| **Competition** | 25 | saturated (many ads, low differentiation) | moderate, room for "kind personalization" | few credible competitors / quality gap vs customwarms |
| **Margin-fit** | 20 | contribution < 15% even @ $59.95 (`poor`) | clears floor only at $59.95 / low CPA (`borderline`) | clears 15% comfortably @ target CPA (`good`) |
| **IP-risk** | 15 | HIGH (character/licensed/celebrity) | FLAG (quote/logo/style-adjacent) | CLEAR (own photo/name/message, no 3rd-party IP) |

`demand_score = round(demand_pts + competition_pts + marginfit_pts + iprisk_pts)`. **Gate: ≥ 70 to `validated`.**
Estimated inputs (no live tool) → cap contribution of that dimension AND set `need_review=true`, `confidence_score < 0.7`.

## 2. Decision matrix

| Condition | decision |
|-----------|----------|
| `demand_score ≥ 70` ∧ `ip_risk_flag ≠ HIGH` ∧ `need_review = false` ∧ `confidence ≥ 0.7` | **validated** → handoff PRD-002 |
| Promising but blocked (estimate-only, design_deadline < 6wk, new niche no benchmark, IP=FLAG) | **watchlist** → Owner |
| `margin_fit = poor` OR `ip_risk_flag = HIGH` OR demand clearly absent | **rejected** (or PRD-003 first if IP) |
| Previously validated but data stale (> 1 quarter or post-season) | **refresh** |

The schema encodes the `validated` row as `allOf/if-then`; the validator (Draft7) rejects any `validated` artifact that violates it (fail-closed).

## 3. US gift-niche taxonomy (occasion × relationship × recipient)

**Occasion axis** (schema `niche_category: gift-occasion`): Christmas / Noel, Valentine's Day, Mother's Day, Father's Day, wedding anniversary, graduation, housewarming, memorial (in-memory-of).

**Relationship axis** (`relationship`): to my daughter / son, to my wife / husband, to my mom / dad, to grandma / grandpa, to my best friend, first-time-mom.

**Recipient-special axes:**
- `pet` — dog / cat "fur mom/dad", breed-portrait blankets. Strong evergreen + gift lift.
- `pet-memorial` — "in memory of" pet-loss blankets. High emotional AOV, evergreen, low seasonality; own-photo → usually IP CLEAR.
- `baby` — new-baby / nursery, birth-stats blanket. Watch CPSC flammability + baby-safety labeling.
- `military` — deployment / homecoming, "my soldier". Sensitive; avoid unit insignia/branch logos (IP FLAG).
- `other` — anything not above; default to conservative scoring + need_review.

**US seasonal peaks (set `design_deadline` ≥ 6 weeks before):** Christmas ~W51 (deadline ≤ ~W44), Valentine's ~W07 (deadline ≤ ~W01), Mother's Day ~W19, Father's Day ~W24. Evergreen niches (pet, pet-memorial) → `seasonal_window.type = evergreen`, `peak_week = "none"`.

## 4. Margin-fit quick-screen (from unit-economics.md)

- Blanket **$49.95** @ CPA $15 → contribution ≈ 12.4% → **below floor** (`borderline`/`poor`); needs CPA ≤ ~$13.6 or price ≥ ~$52.
- Blanket **$59.95** (free-ship threshold) @ CPA $18 → contribution ≈ 21.0% → **`good`**.
- Rule: price toward $59.95 + bundle to > $59 to clear free-ship and lower BE-ROAS. Never scale ads unless blended ROAS ≥ per-SKU BE-ROAS. All cost numbers are `ASSUMPTION` until a real supplier quote replaces them → keep confidence honest.

## 5. IP pre-flag cheat-sheet (pre-flag ONLY, not clearance)

| Signal in niche concept | flag |
|-------------------------|------|
| Customer's own photo / name / message, generic motifs | CLEAR |
| Well-known quote, brand-adjacent style, sports/hobby logo-ish | FLAG → PRD-003 |
| Named character (Disney/Marvel/etc.), celebrity photo, licensed team logo, unit insignia | HIGH → PRD-003 mandatory, cannot validate |

CLEAR here = "no third-party IP in the concept". Official trademark clearance (`clearance_id`) still comes from **bck-compliance** — never sign off CLEAR for legal purposes from this skill.

## 6. Evidence discipline (P2)

Cite every material claim with `{claim, verbatim_quote, source(filepath), location?}` where `verbatim_quote` is copy-exact from `source`. The validator re-reads `source` and penalizes −0.2 confidence per quote it cannot find. Prefer citing the SOP, unit-economics, charter, or Owner-provided evidence files. `source` is always a **filepath**, never a tool name.
