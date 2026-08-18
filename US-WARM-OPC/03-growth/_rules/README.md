# _rules — 03 Growth (DAKOfits US)
**Date:** 2026-08-04 · What AI MUST NOT do.

## Non-negotiables
1. **1 ngưỡng KILL duy nhất** — Platform ROAS < 1.8. KHÔNG để orchestrator/executor lệch nhau (fix EU H3).
2. **No hard-code winner ROAS** — scale gate = blended ≥ BE-ROAS per-SKU (unit-economics), không số cố định (fix EU C1).
3. **No engagement-bait** — không "tag/comment/drop a 🐾"; soft-CTA. Enforce validator --prose (fix EU M2).
4. **No deceptive / no fake review / no unverified ™** — FTC 16 CFR 255.
5. **No ads without live-product** — thiếu live-product → HOLD/escalate, không chạy ads vô sản phẩm (fix EU M7).
6. **No phantom asset** — creative chưa render → not-generated, không khai có.

## Decision authority
| Quyết định | Auto? | Authority |
|-----------|-------|-----------|
| Launch ad | live-product ∧ FTC clean | grw-fb-ads |
| Scale | blended ≥ BE-ROAS | grw-fb-ads |
| Kill | ROAS < 1.8 | grw-fb-ads (auto) |
| Spend vượt cap / FTC uncertain | ❌ | Owner/bck-compliance |

## Quality Standards
| SOP | SLI | SLO |
|-----|-----|-----|
| GRW-002 | Scale gate | blended ≥ BE-ROAS |
| GRW-002 | FTC deceptive | 0 hit (--prose) |
| GRW-001 | Engagement-bait | 0 hit (--prose) |
| GRW-005 | Unverified ™ | 0 |

## Harness: `_shared/script/validator.py --run-all --prose`.
