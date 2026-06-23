# Smoke Test — vibe-eu-opc-grw-creative

Kiểm tra nhanh skill chạy được đầu-cuối (5 bước).

| # | Bước | Thao tác | Pass khi |
|---|------|----------|----------|
| 1 | Load skill | Mở `SKILL.md` + `skill.json` | Frontmatter `name=vibe-eu-opc-grw-creative`, `type=skill`; `skill.json` validate qua `schema/skill-meta.schema.json` (name/version/description/phases/dependencies có đủ) |
| 2 | Đọc SOP | Mở `../../create-creative/template/sop_grw-005_fb-creative_v1.0_2026-06-23.md` | Đọc được IPO + Hook/Body/CTA + policy gate; không lỗi path |
| 3 | Sinh creative | Chạy `prompt/make-creative-prompt.md` với `synthetic-data/sample-creative-brief.md` | Trả JSON đúng `schema/creative-package.schema.json`: có hook_0_3s / body_360 / cta / evidence / confidence_score / need_review |
| 4 | Policy gate | Kiểm `policy_self_check` trên output | =true khi không chạm health-claim/before-after/IP; =false + need_review=true + route 05-compliance khi chạm |
| 5 | Handoff | Đặt package vào `output/`, gọi downstream | confidence ≥ 0.7 & policy pass → sẵn cho `vibe-eu-opc-grw-fb-ads`; ngược lại nằm ở `human-review/` |

**Kết quả mong đợi:** 5/5 pass → skill production-ready. Bất kỳ bước fail → ghi `execution_log.jsonl` (status=fail) và dừng tại gate.
