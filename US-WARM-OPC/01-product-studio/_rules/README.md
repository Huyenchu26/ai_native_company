# _rules — 01 Product Studio (DAKOfits US)

**Date:** 2026-08-04 · What AI MUST NOT do. Policies · decision authority · quality gates · escalation.

## Non-negotiables (error budget = 0)
1. **No upscale** — ảnh khách/asset dưới min DPI ở size in thật → REJECT + re-source. KHÔNG upscale để "đạt DPI".
2. **No under-spec material** — không chọn vải dưới ngưỡng GSM brand-promise để hạ giá (chống "chăn mỏng" như đối thủ).
3. **No IP guess** — chưa tra USPTO/uncertain → status=PENDING, KHÔNG mặc định CLEAR. Chỉ `clearance_id` từ bck-compliance mới cho handoff.
4. **No fabricated data** — thiếu tool (Trends/AdSpy/Meta) → đánh dấu estimate + hạ confidence + need_review. KHÔNG bịa số như thật.

## Decision authority
| Quyết định | Giới hạn | Auto? | Authority |
|-----------|----------|-------|-----------|
| Validate niche | confidence ≥ 0.7 + all gate pass | ✅ | prd-niche-research |
| Watchlist→validated (thiếu benchmark) | — | ❌ | Owner |
| IP CLEAR sign-off | có clearance_id | ❌ | bck-compliance |
| Design handoff | design_status=CLEAR ∧ ip=CLEAR | ✅ | prd-design |
| IP HIGH / uncertain | — | ❌ | Owner |

## Quality Standards (SLI/SLO)
| SOP | SLI | SLO | Measurement |
|-----|-----|-----|-------------|
| PRD-001 | Demand score | ≥ 70 | rubric |
| PRD-001 | Margin-fit contribution | ≥ 15% @ CPA | unit-economics |
| PRD-002 | Personalization DPI | ≥ min @ print size | validator (no upscale) |
| PRD-002 | Material GSM | ≥ brand-promise ngưỡng | supplier spec |
| PRD-003 | USPTO checked before CLEAR | 100% | gate |

## Escalation
| Tình huống | Route |
|-----------|-------|
| IP HIGH/uncertain | Owner |
| Material dưới ngưỡng (không có vải đạt) | Owner + merchandising |
| Niche mới không benchmark | Owner (watchlist) |

## Harness
Mọi output validate qua `_shared/script/validator.py --run-all` (enforce gate if/then + evidence). Hooks chặn edit `template/` & `archive/`.
