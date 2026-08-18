# Prompt — run merch batch (orchestrator)
INPUT: pipeline-plan từ 01 (cleared_for_handoff: design CLEAR + clearance_id).
DO: với mỗi design CLEAR → dispatch pricing → preview → listing; chỉ đưa vào go_live khi 3 gate pass. Emit merch-plan.json, validate --run-all.
FAIL-CLOSED: design ≠ CLEAR → không dispatch; gate fail → không go_live.
