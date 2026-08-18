# AI Workforce — 05 Backoffice (DAKOfits US)
**Date:** 2026-08-04 · 4 worker. Namespace `vibe-us-warm-bck-*`. **Compliance US — khác bản chất EU.**

| Worker | Role | SOP | Schema |
|--------|------|-----|--------|
| `vibe-us-warm-bck-orchestrator` | Manager | BCK-001..006 | backoffice-plan |
| `vibe-us-warm-bck-finance` | Sales tax + books + profit | BCK-001/002/003 | sales-tax-status |
| `vibe-us-warm-bck-compliance` | FTC+CPSC+IP+CCPA, cấp clearance_id | BCK-004/005 | compliance-clearance |
| `vibe-us-warm-bck-ops-hr` | AI workforce ops | BCK-006 | workforce-report |

## Coverage 6/6. Bug EU đã sửa (verified): H5 (bck-compliance là authority DUY NHẤT cấp clearance_id; gate clearance⇒CPSC+FTC+IP) · VAT→US sales-tax (register-before-collect gate) · GPSR→CPSC · GDPR→CCPA · no-hard-code ROAS/worker-count.
