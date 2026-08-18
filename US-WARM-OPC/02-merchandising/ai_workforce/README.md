# AI Workforce — 02 Merchandising (DAKOfits US)

**Date:** 2026-08-04 · 4 worker (1 orchestrator + 3 specialist). Namespace `vibe-us-warm-mer-*`.

| Worker | Role | SOP | Schema chính |
|--------|------|-----|--------------|
| `vibe-us-warm-mer-orchestrator` | Manager (route) | MER-001..004 | merch-plan |
| `vibe-us-warm-mer-catalog` | Pricing + go-live | MER-001, MER-004 | pricing-decision, listing-package |
| `vibe-us-warm-mer-visual` | Personalization preview | MER-002 | mockup-set |
| `vibe-us-warm-mer-product-page` | Gift listing + FTC/CPSC | MER-003 | product-page |

## Coverage: 4/4 SOP. Harness: `_shared/script/validator.py` (fix if/then + evidence + --prose).

## Handoff chain
[01 design CLEAR] → pricing (contribution/BE-ROAS) → preview (no-phantom) → listing (FTC/CPSC, blocked-state) → go-live (3-gate) → **03-growth** (live-product signal).

## Bug EU đã sửa (verified 2026-08-04)
| Bug EU | US |
|--------|----|
| gross-45 / ROAS 2.5 hard-code | ✅ contribution + BE-ROAS per-SKU (gate FAIL nếu below floor) |
| H1 ảnh ma | ✅ no-phantom gate (production + not-generated → FAIL) |
| M4 schema thiếu validation-first + 9:16 | ✅ 2-phase + ratio 9:16 |
| P3 không model blocked-state | ✅ product-page blocked hợp lệ |
| P4/P5 gate không enforce | ✅ if/then enforce + --prose bắt deceptive |
| D1 escalate tên cũ | ✅ escalate `vibe-us-warm-bck-compliance` |
| enum PASS≠CLEAR | ✅ design_clearance khớp 01 |
