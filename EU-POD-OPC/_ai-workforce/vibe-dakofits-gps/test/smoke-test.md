# Smoke Test — vibe-dakofits-gps

5 bước (~5 phút):

1. **Load** — skill load, đọc được kb/company-routing-map.md (24 SOP ↔ 17 skill).
2. **Route single-dept** — input "khách EU đòi xóa data" → route đúng `vibe-eu-opc-bck-compliance` (BCK-005), scope=single-dept.
3. **Route full-chain** — input "làm 10 SP niche Corgi US+EU bán tuần sau" → routing[] có đủ 5 mắt xích theo thứ tự Product→Merch→Growth→Fulfillment→Backoffice, gate_checks.ip_tm + gpsr + shopbase_live_before_ads + meta_ad_policy = true.
4. **Gate enforce** — input "chạy ads SP mới" (SP chưa qua Merch) → GPS từ chối route thẳng Growth, route lại từ Product/Merch, log need_review.
5. **Schema** — output/routing-plan.json validate schema/task-routing.schema.json (`python script/validator.py --artifact output/routing-plan.json --schema schema/task-routing.schema.json`) → ok:true; confidence_score & need_review hiện diện.

PASS = cả 5 bước đạt.
