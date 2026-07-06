# AI Workforce — 01 Product Studio (DAKOfits)

## Status: 🟢 Activated (2026-06-23)

> Build bởi vibe-aiworkforce (Phase 6.1). Mỗi skill đủ 8 components, bám SOP state machine. PRIMARY tại đây; copy ở `~/.claude/skills/`.

## Skills

| # | Skill | Role | SOP source | 8-comp | Installed |
|---|-------|------|-----------|:------:|:---------:|
| 0 | vibe-eu-opc-prd-orchestrator | Manager — pipeline niche→design→clearance→handoff Merch | điều phối PRD-* | ✅ | ✅ |
| 1 | vibe-eu-opc-prd-niche-research | Niche scoring + audience + spy + seasonal | SOP-PRD-001, 002 | ✅ | ✅ |
| 2 | vibe-eu-opc-prd-design | AOP design print-ready + IP/TM clearance | SOP-PRD-003, 004 | ✅ | ✅ |

## SOP → Skill Coverage (Gate)

| SOP | Tên | Responsible skill |
|-----|-----|-------------------|
| SOP-PRD-001 | Niche research & demand scoring | vibe-eu-opc-prd-niche-research |
| SOP-PRD-002 | Trend & seasonal calendar | vibe-eu-opc-prd-niche-research |
| SOP-PRD-003 | AOP design print-ready | vibe-eu-opc-prd-design |
| SOP-PRD-004 | IP/TM clearance & QC | vibe-eu-opc-prd-design |

**Coverage: 4/4 SOP = 100%** ✅

## Gate cứng enforce
- **No IP/TM clearance → no listing**: prd-design clearance status PASS/MODIFY/REJECT, conservative default REJECT; chỉ design PASS mới handoff Merch (fail-closed).

## Handoff — chuỗi vận hành ShopBase-first
```
niche-research → design + IP clearance (PASS) → prd-orchestrator
   → handoff vibe-eu-opc-mer-orchestrator (đăng SP LIVE lên ShopBase)
      → CHỈ KHI live → Growth tạo content + FB Ads
```
Xem quy tắc đầy đủ: [_shared/operating-flow.md](../../_shared/operating-flow.md)

## Cách gọi
- `/vibe-eu-opc-prd-orchestrator` ("chuẩn bị lô 6 niche mèo mới cho US/EU")
- `/vibe-eu-opc-prd-niche-research` ("tìm niche dog-mom đang hot Q4")
- `/vibe-eu-opc-prd-design` ("thiết kế AOP Corgi + check trademark")
