# _rules — 05 Backoffice (DAKOfits US)
**Date:** 2026-08-04 · What AI MUST NOT do. (US compliance — khác bản chất EU.)

## Non-negotiables (error budget = 0)
1. **No tax collected without registration** — thu sales tax bang nào phải đăng ký bang đó (Wayfair nexus).
2. **No publish without CPSC label** — thiếu fiber content/RN/origin/flammability → không clear.
3. **No fake review / no deceptive / Made-in-USA sai** — FTC 16 CFR 255.
4. **bck-compliance là authority DUY NHẤT cấp clearance_id** — prd-design chỉ pre-check (fix EU H5).
5. **No hard-code ROAS / no VAT** — profit theo contribution + BE-ROAS per-SKU, US không có VAT (fix EU C1/F3/F4).
6. **No hard-code worker count** — đếm THẬT từ ai_workforce/ (fix EU hard-code-12).
7. **PII cá nhân hoá (tên/ảnh)** — chỉ dùng để in; marketing cần consent; DSAR ≤45 ngày (CCPA).

## Decision authority
| Quyết định | Auto? | Authority |
|-----------|-------|-----------|
| Đăng ký bang nexus | ❌ | Owner |
| Remit tax | filing confirmed | bck-finance |
| Cấp clearance_id | 3 gate pass | bck-compliance |
| Made-in-USA claim | ❌ | Owner/bck-compliance |
| DSAR delete | ≤45d | bck-compliance |

## Quality Standards
| SOP | SLI | SLO |
|-----|-----|-----|
| BCK-003 | Tax collected ⇒ registered | 100% |
| BCK-004 | Clearance ⇒ CPSC+FTC+IP pass | 100% |
| BCK-005 | DSAR response | ≤ 45 ngày |
| BCK-002 | Profit basis | contribution+BE-ROAS, no VAT/2.5 |
| BCK-006 | Worker count | đếm thật (no hard-code) |

## Harness: `_shared/script/validator.py --run-all --prose`.
