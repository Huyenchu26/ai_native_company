# Quality Standards — 02 Merchandising (DAKOfits US)

**Version:** 1.0 · **Date:** 2026-08-04

| SOP | SLI | SLO | SLA | Error budget | Measurement |
|-----|-----|-----|-----|--------------|-------------|
| MER-001 | Contribution % @ CPA | ≥ 15% | — | — | unit-economics |
| MER-001 | BE-ROAS per-SKU | present, not hard-coded | — | 0% | schema |
| MER-002 | Images on disk = manifest | 100% | — | 0% | file check (no phantom) |
| MER-002 | Min images (production) | ≥ 4 | — | — | count |
| MER-003 | FTC deceptive/fake | 0 hit | — | 0% | validator --prose |
| MER-003 | CPSC fiber label | present | — | 0% | field |
| MER-003 | Final-sale disclosure | present | — | 0% | field |
| MER-004 | Go-live gate (3 pass) | 100% | — | 0% | gate |

**Hard gates (error budget 0):** no-phantom-image, FTC-clean, CPSC-label, contribution-floor — enforce bằng schema allOf/if-then + `--prose` qua validator đã sửa.
**Evidence-bound + confidence < 0.7 → need_review → review-queue.**
