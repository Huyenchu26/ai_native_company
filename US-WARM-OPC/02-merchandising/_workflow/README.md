# _workflow — 02 Merchandising (DAKOfits US)

**Date:** 2026-08-04 · SOP index + state machine + dependencies.

## SOP Index
| SOP | Process | Template | Worker |
|-----|---------|----------|--------|
| MER-001 | Blanket pricing & setup | [set-pricing](../set-pricing/template/sop_mer-001_blanket-pricing_v1.0_2026-08-04.md) | mer-catalog |
| MER-002 | Personalization preview | [personalization-preview](../personalization-preview/template/sop_mer-002_personalization-preview_v1.0_2026-08-04.md) | mer-visual |
| MER-003 | Gift product page | [write-product-page](../write-product-page/template/sop_mer-003_gift-product-page_v1.0_2026-08-04.md) | mer-product-page |
| MER-004 | Catalog sync & go-live | [sync-catalog](../sync-catalog/template/sop_mer-004_catalog-sync_v1.0_2026-08-04.md) | mer-catalog |

## Dependency map
```
[01 pipeline-plan: design CLEAR] ─▶ MER-001 pricing ─┬─▶ MER-002 preview ─┐
                                                     └─▶ MER-003 listing ─┴─▶ MER-004 go-live ─▶ [03 growth: live-product signal]
```
Go-live CHỈ khi pricing floor pass ∧ images on disk ∧ listing publish-ready ∧ compliance clean.

## State machine: template→input→processing→output→archive. Coverage: 4/4 SOP.
