# Quality Standards — 01 Product Studio (DAKOfits US)

**Version:** 1.0 · **Date:** 2026-08-04

| SOP | Nghiệp vụ | SLI | SLO | SLA (ext) | Error budget | Measurement |
|-----|-----------|-----|-----|-----------|--------------|-------------|
| PRD-001 | Niche research | Demand score | ≥ 70 | — | 30% | rubric |
| PRD-001 | Niche research | Margin-fit contribution | ≥ 15% @ CPA | — | — | unit-economics |
| PRD-001 | Niche research | Evidence coverage | 100% claim có verbatim | — | 0% | validator --run-all |
| PRD-002 | Design | Personalization DPI @ print | ≥ min (no upscale) | — | 0% | validator |
| PRD-002 | Design | Material GSM | ≥ brand-promise | — | 0% | supplier spec |
| PRD-002 | Design | Safe-area | 100% | — | 0% | design check |
| PRD-003 | IP clearance | USPTO checked before CLEAR | 100% | — | 0% (hard gate) | gate |
| PRD-003 | IP clearance | Licensed-char match | 0 | — | 0% | blocklist |

**Evidence-bound:** mọi SLO target có evidence (verbatim từ brief/unit-economics/USPTO). confidence < 0.7 → need_review=true → review-queue.
**Hard gates (error budget 0):** no-upscale, material-spec, USPTO-before-CLEAR, licensed-char-reject — enforce bằng schema allOf/if-then qua validator đã sửa.
