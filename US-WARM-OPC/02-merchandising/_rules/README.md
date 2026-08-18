# _rules — 02 Merchandising (DAKOfits US)

**Date:** 2026-08-04 · What AI MUST NOT do.

## Non-negotiables (error budget = 0)
1. **No gross-margin ảo** — KHÔNG dùng `giá=cost/(1−margin)`. Chỉ contribution + BE-ROAS per-SKU (unit-economics).
2. **No hard-code ROAS** — KHÔNG đặt winner/kill = số cố định (2.5...). BE-ROAS tính per-SKU.
3. **No phantom image** — manifest không được khai ảnh không có trên đĩa (fix EU H1). QC đối chiếu file thật.
4. **No fake review / deceptive claim** — FTC: no fake rating/review, no "guaranteed/100%/™" chưa verify (validator --prose).
5. **No publish without compliance** — thiếu CPSC fiber label / final-sale disclosure → publish_status=blocked.

## Decision authority
| Quyết định | Auto? | Authority |
|-----------|-------|-----------|
| Chốt giá (floor pass) | ✅ | mer-catalog |
| Giá dưới floor / lệch band | ❌ | Owner |
| Publish listing | gate pass | mer-product-page + bck-compliance |
| Go-live catalog | 3 gate pass | mer-catalog |
| Compliance uncertain | ❌ | bck-compliance / Owner |

## Quality Standards (SLI/SLO)
| SOP | SLI | SLO | Measurement |
|-----|-----|-----|-------------|
| MER-001 | Contribution % @ CPA | ≥ 15% | unit-economics |
| MER-002 | Images on disk = manifest | 100% | file check |
| MER-003 | FTC deceptive/fake hits | 0 | validator --prose |
| MER-003 | CPSC fiber label | present | field |

## Escalation
Giá dưới floor → Owner+grw · compliance uncertain → bck-compliance · Shopify token thiếu → pending, không khai live.

## Harness: `_shared/script/validator.py --run-all` (enforce gate + evidence + --prose). Hooks chặn template/, archive/.
