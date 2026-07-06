# Smoke Test — vibe-eu-opc-prd-niche-research

Kiểm tra nhanh skill chạy đúng end-to-end với 1 niche seed list mẫu.

## Bước 1 — Load SOP & input
- Đọc `../../research-niche/template/sop_prd-001_niche-research_v1.0_2026-06-23.md` và SOP-PRD-002.
- Nạp input mẫu `synthetic-data/sample-niche-input.md` (niche seed list + signal AdSpy/Meta/Trends).
- **PASS:** rubric (demand40/comp25/margin20/IP15) + ngưỡng (score≥70, audience≥500k) được nạp đúng.

## Bước 2 — Score & shortlist
- Chấm điểm từng niche, điền `score_breakdown`, audience_size, competition_level, margin_fit.
- Loại niche `demand_score < 70` HOẶC `audience_size < 500.000` (→ rejected/watchlist).
- **PASS:** mỗi niche có đủ điểm thành phần và một `decision`.

## Bước 3 — IP pre-flag + seasonal
- Gắn `ip_risk_flag` (CLEAR/FLAG/HIGH); HIGH → `need_review=true`.
- Phân loại evergreen/seasonal; niche seasonal có `design_deadline` ≥ 6 tuần trước peak.
- **PASS:** không niche seasonal nào vi phạm lead-time; HIGH được flag.

## Bước 4 — Validate schema + evidence/confidence
- Validate output qua `schema/niche-validation.schema.json` (vd `python script/validator.py`).
- Mỗi entry có `evidence[]` ≥1, `confidence_score` ∈ [0,1], `need_review` boolean.
- **PASS:** schema hợp lệ; entry `confidence_score < 0.7` đều có `need_review=true`.

## Bước 5 — Output + handoff + archive
- Ghi `validated_niche_list` + `seasonal_opportunity_calendar` ra `output/`.
- Xác nhận handoff target = `vibe-eu-opc-prd-design` (+ orchestrator); ghi `execution_log.jsonl`; auto-archive task.
- **PASS:** file output tồn tại, log audit ghi đúng, task được archive.

## Kết quả mong đợi
≥1 niche `decision=validated` (score≥70 & audience≥500k), 0 lỗi schema, mọi entry mang evidence + confidence + need_review.
