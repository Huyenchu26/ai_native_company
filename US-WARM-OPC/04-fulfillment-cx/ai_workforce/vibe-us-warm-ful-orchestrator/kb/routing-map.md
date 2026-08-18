# Routing Map — ful-orchestrator (DAKOfits US)
| SOP | Worker | Gate |
|-----|--------|------|
| FUL-002 route | ful-order-ops | supplier QC-capable |
| FUL-001 QC+track | ful-order-ops | gsm≥260, no-fake-tracking |
| FUL-003 support | ful-cx | first-response ≤4h |
| FUL-004 returns | ful-cx | refund>$30 human; defect refundable |
Rules: [../../../_rules/README.md](../../../_rules/README.md). Downstream: [../../../../05-backoffice/ai_workforce/vibe-us-warm-bck-orchestrator](../../../../05-backoffice/) (bck-orchestrator — Phase 5).
