# Quality Standards — 03 Growth (DAKOfits US)
**Version:** 1.0 · **Date:** 2026-08-04

| SOP | SLI | SLO | Error budget | Measurement |
|-----|-----|-----|--------------|-------------|
| GRW-002 | Scale gate vs BE-ROAS | blended ≥ BE-ROAS | 0% | schema |
| GRW-002 | KILL threshold | ROAS < 1.8 (single) | 0% | rule |
| GRW-002 | FTC deceptive | 0 hit | 0% | validator --prose |
| GRW-005 | Unverified ™ / fake | 0 | 0% | --prose |
| GRW-001 | Engagement-bait | 0 hit | 0% | --prose |
| GRW-001 | Ads/post without live-product | 0 (escalate) | 0% | precheck |

**Hard gates:** BE-ROAS scale, single-KILL-1.8, FTC-clean, no-engagement-bait, live-product-required — enforce qua validator (if/then + --prose).
