# Smoke Test — vibe-eu-opc-grw-fb-ads

5 bước xác nhận skill load & vận hành đúng. Pass = tất cả 5 ✔.

## Bước 1 — Skill load
- [ ] `SKILL.md` có frontmatter hợp lệ (`name: vibe-eu-opc-grw-fb-ads`, `type: skill`, `description` 80–250 từ, đủ 4 phần WHAT/TRIGGER/EXCLUSION/PUSH).
- [ ] `skill.json` parse OK & validate theo `schema/skill-meta.schema.json` (required: name, version, description 80–300 ký tự, phases, dependencies).
- **Expect:** skill nhận diện được, không lỗi parse.

## Bước 2 — Đọc SOP binding
- [ ] Skill mở được SOP-GRW-002 (`run-fb-ads/template/...`) và SOP-GRW-004 (`report-growth/template/...`).
- [ ] Mở được `_shared/unit-economics.md`.
- **Expect:** đọc đúng quy trình ABO→CBO, decision rules, BE-ROAS per-SKU (US ~2.75/EU ~5.3).

## Bước 3 — GATE policy (cứng)
- [ ] Đưa input THIẾU Meta Ad Policy clearance.
- **Expect:** skill trả `decision=HOLD`, `policy_cleared=false`, `need_review=true`, KHÔNG launch campaign. Trả task về creative/compliance.

## Bước 4 — Output đúng schema
- [ ] Chạy synthetic input (`synthetic-data/sample-campaign-input.md`).
- [ ] Output campaign-decision validate theo `schema/campaign-decision.schema.json` (đủ campaign_id, decision enum SCALE/KILL/OPTIMIZE/HOLD, platform_roas, blended_roas, break_even_roas, rationale, evidence[], confidence_score, need_review).
- [ ] Mỗi `evidence[]` item có `claim` + `verbatim_quote` + `source`.
- **Expect:** JSON hợp lệ, không thiếu required field.

## Bước 5 — Confidence & state machine
- [ ] Khi `confidence_score < 0.7` hoặc Blended < BE-ROAS / vượt budget cap ⇒ `need_review=true`.
- [ ] Output đi đúng đường: `input/` → `processing/ai-draft/` → (review) `processing/human-review/` → `output/` → `archive/[YYYY-MM]/`.
- [ ] `execution_log.jsonl` ghi mỗi bước theo `schema/execution-log-entry.schema.json`.
- **Expect:** review routing + log đúng.
