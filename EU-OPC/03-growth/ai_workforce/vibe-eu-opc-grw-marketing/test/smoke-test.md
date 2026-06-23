# Smoke Test — vibe-eu-opc-grw-marketing

Kiểm tra nhanh skill chạy đúng end-to-end. 5 bước.

## Bước 1 — Load skill & SOP binding
- Mở `SKILL.md` + `skill.json`. Xác nhận `name = vibe-eu-opc-grw-marketing`, version `1.0`.
- Xác nhận 2 link SOP-GRW-003 và SOP-GRW-001 resolve được.
- **PASS:** frontmatter có đủ 4 phần (WHAT/TRIGGER/EXCLUSION/PUSH); links mở được.

## Bước 2 — Đọc input mẫu
- Nạp `synthetic-data/sample-email-input.md`.
- **PASS:** input có segment opt-in + promo offer rõ ràng.

## Bước 3 — Tạo email flow
- Dùng `prompt/email-flow-prompt.md` tạo 1 flow `cart-abandon` từ input mẫu.
- **PASS:** output JSON hợp lệ với `schema/email-campaign.schema.json` (chạy `validator.py`).

## Bước 4 — Kiểm gate compliance
- Đặt `audience_optin = false` → skill phải DỪNG, không gửi, need_review=true.
- **PASS:** consent gate chặn đúng; spam/deliverability rule hiện trong KB.

## Bước 5 — Organic + log
- Tạo 1 organic post + 1 UGC seed (xin consent) theo SOP-GRW-001.
- Ghi `execution-log-entry` (qua `log_helper.py`) hợp lệ với `schema/execution-log-entry.schema.json`.
- **PASS:** post có evidence[] + confidence_score; log entry valid.

> Tất cả 5 bước PASS = smoke test xanh.
