# Smoke Test — vibe-eu-opc-bck-compliance

Mục tiêu: xác nhận skill cấp clearance đúng, gate cứng fail-closed, GDPR breach 72h hoạt động.

## Bước 1 — Load skill & SOP binding
- Mở `SKILL.md` + `skill.json`. Kỳ vọng: name=`vibe-eu-opc-bck-compliance`, version `1.0`, 5 phases, upstream `vibe-eu-opc-prd-design`, downstream gồm Merch/Growth/Backoffice orchestrator.
- Kỳ vọng: link tới SOP-BCK-004 và SOP-BCK-005 resolve được.

## Bước 2 — Cấp clearance EU PASS (happy path)
- Input: `synthetic-data/sample-clearance-input.md` → design #1 (market=EU, RP đủ, breed không trùng TM).
- Chạy `prompt/issue-clearance-prompt.md`.
- Kỳ vọng: `gpsr_status=PASS`, `ip_tm_status=PASS`, `label_ready=true`, `confidence_score≥0.7`, `need_review=false`.
- Validate qua `script/validator.py` theo `schema/clearance-log.schema.json` → PASS.

## Bước 3 — EU thiếu GPSR → FAIL fail-closed (gate cứng)
- Input: design #1 nhưng **xóa Responsible Person** (hoặc địa chỉ ngoài EU).
- Kỳ vọng: `gpsr_status=FAIL`, `label_ready=false`, block publish EU, lý do ghi trong evidence[].
- Thử ép `label_ready=true` với `gpsr_status=FAIL`, market=EU → schema `allOf` REJECT (validator fail). Xác nhận **no-GPSR-no-publish** giữ vững.

## Bước 4 — IP/TM nghi trademark → REJECT
- Input: breed/niche name trùng nhãn hiệu đã đăng ký (vd brand name nổi tiếng).
- Kỳ vọng: `ip_tm_status=REJECT`, `need_review=true`, handoff Product Studio re-clear (SOP-PRD-004). Conservative default giữ vững.

## Bước 5 — GDPR breach 72h + DSAR
- Input: incident alert "nghi data breach Klaviyo export".
- Kỳ vọng: breach log immutable tạo, 72h clock kích hoạt từ "become aware", notification draft sinh ra ≤72h.
- Input phụ: DSAR erasure từ khách EU → resolution log ≤1 tháng, giữ data tài chính tối thiểu nếu xung đột kế toán.
