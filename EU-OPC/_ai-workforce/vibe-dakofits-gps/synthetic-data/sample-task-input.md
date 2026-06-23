# Sample Task Inputs — vibe-dakofits-gps

## Input A (full-chain)
> "Làm 10 SP niche Corgi cho US + EU, target bán tuần sau."

Expected routing-plan.json (rút gọn):
```json
{
  "task": "Làm 10 SP niche Corgi cho US + EU, target bán tuần sau",
  "scope": "full-chain",
  "market": "US+EU",
  "routing": [
    {"step": 1, "department": "01", "skill": "vibe-eu-opc-prd-orchestrator", "sop": "PRD-001..004"},
    {"step": 2, "department": "02", "skill": "vibe-eu-opc-mer-orchestrator", "sop": "MER-001..004", "depends_on_gate": "ip_tm_clearance"},
    {"step": 3, "department": "03", "skill": "vibe-eu-opc-grw-orchestrator", "sop": "GRW-005,002", "depends_on_gate": "shopbase_live_before_ads"},
    {"step": 4, "department": "04", "skill": "vibe-eu-opc-ful-orchestrator", "sop": "FUL-001..004"},
    {"step": 5, "department": "05", "skill": "vibe-eu-opc-bck-orchestrator", "sop": "BCK-001..006"}
  ],
  "gate_checks": {"ip_tm_clearance": true, "gpsr_clearance": true, "shopbase_live_before_ads": true, "meta_ad_policy": true, "refund_threshold": true},
  "evidence": [{"claim": "Corgi cần IP/TM check trước listing", "verbatim_quote": "niche Corgi", "source": "task"}],
  "confidence_score": 0.82,
  "need_review": false
}
```

## Input B (single-dept)
> "Khách EU đòi xóa dữ liệu cá nhân." → route `vibe-eu-opc-bck-compliance` (BCK-005 GDPR DSAR), scope=single-dept.

## Input C (gate violation)
> "Chạy ads cho SP mèo mới." (SP chưa qua Product→Merch) → GPS từ chối route thẳng Growth, route lại từ step 1, `need_review=true`, ghi rõ "SP chưa live ShopBase".
