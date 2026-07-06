# Smoke Test — vibe-eu-opc-bck-ops-hr

Kiểm tra nhanh skill tạo được 1 weekly workforce report hợp lệ theo SOP-BCK-006. Input mẫu: [synthetic-data/sample-workforce-input.md](../synthetic-data/sample-workforce-input.md).

## 5 bước

1. **Load input + đếm roster thật**
   Nạp `sample-workforce-input.md` + `workforce-map`. Skill đếm `total_workers` từ map + folder EU-OPC, KHÔNG hard-code "12". → PASS nếu evidence[] có ghi phương pháp đếm và số khớp nguồn.

2. **monitor-uptime**
   Tính uptime % per worker + trung bình roster từ run log. Đánh dấu worker < 95%. → PASS nếu uptime_pct ∈ [0,100] và worker dưới ngưỡng được flag escalate.

3. **review-quality (reject + cost)**
   Tính reject rate per worker (<10%), tổng hợp cost summary + delta% vs baseline. → PASS nếu avg_reject_rate ∈ [0,1], cost_summary.total_cost_usd có nguồn, spike>20% → action `cost-alert`.

4. **capacity-plan**
   Đối chiếu workload (batch 5–10 SP) vs roster → status. → PASS nếu capacity_status ∈ {OK, STRAINED, OVER}; nếu OVER thì actions[] có scale/cron action.

5. **weekly-report + validate schema**
   Xuất JSON, chạy `script/validator.py` với `schema/workforce-review.schema.json`. → PASS nếu JSON hợp lệ schema, có evidence[], confidence_score (≥0.7 hoặc need_review=true), bàn giao bck-orchestrator.

## Kỳ vọng tổng
- Tất cả 5 bước PASS.
- Mọi số có evidence[]; không có số nào bịa.
- need_review=true nếu có bất kỳ gate vi phạm (uptime<95% / reject>10% / cost spike>20% / capacity OVER).
