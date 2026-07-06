# AI Workforce — 03 Growth (DAKOfits)

## Status: 🟢 Activated (2026-06-23)

> Build bởi vibe-aiworkforce (Phase 6.1). Mỗi skill đủ 8 components, bám SOP state machine. PRIMARY tại đây; bản copy ở `~/.claude/skills/`.

## Skills

| # | Skill | Role | SOP source | 8-comp | Installed |
|---|-------|------|-----------|:------:|:---------:|
| 0 | vibe-eu-opc-grw-orchestrator | Manager — điều phối, enforce gate | điều phối GRW-* + MER-006 | ✅ | ✅ |
| 1 | vibe-eu-opc-grw-fb-ads | FB Ads + growth report | SOP-GRW-002, GRW-004 | ✅ | ✅ |
| 2 | vibe-eu-opc-grw-creative | Ad creative (hook/body/CTA, UGC) | SOP-GRW-005 | ✅ | ✅ |
| 3 | vibe-eu-opc-grw-marketing | Email Klaviyo + organic/community | SOP-GRW-003, GRW-001 | ✅ | ✅ |

## SOP → Skill Coverage (Gate)

| SOP | Tên | Responsible skill |
|-----|-----|-------------------|
| SOP-GRW-001 | Organic social & community | vibe-eu-opc-grw-marketing |
| SOP-GRW-002 | FB Ads campaign mgmt | vibe-eu-opc-grw-fb-ads |
| SOP-GRW-003 | Email & promotions (Klaviyo) | vibe-eu-opc-grw-marketing |
| SOP-GRW-004 | Growth report (KPI/KRI) | vibe-eu-opc-grw-fb-ads |
| SOP-GRW-005 | FB ad creative | vibe-eu-opc-grw-creative |

**Coverage: 5/5 SOP = 100%** ✅ (orchestrator điều phối toàn bộ)

## Gate cứng enforce
- No Meta Ad Policy → no ads (orchestrator + fb-ads + creative)
- Email chỉ opt-in (GDPR/CAN-SPAM) — marketing
- Winner theo break-even ROAS per-SKU (US ~2.75 / EU ~5.3), KHÔNG 2.5 cứng — fb-ads + [unit-economics](../../_shared/unit-economics.md)
- Budget escalate >$150/ngày → OPC

## Cách gọi
- Điều phối 1 đợt: `/vibe-eu-opc-grw-orchestrator` ("chạy đợt promote 5 SP mới")
- Chạy ads: `/vibe-eu-opc-grw-fb-ads` · Creative: `/vibe-eu-opc-grw-creative` · Email/organic: `/vibe-eu-opc-grw-marketing`

## State machine
Mỗi skill đọc SOP từ `[sop]/template/`, nhận task `input/`, xử lý `processing/ai-draft/`→`human-review/`, trả `output/`, auto-archive `archive/[YYYY-MM]/`.
