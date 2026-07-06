# Smoke Test — vibe-eu-opc-mer-visual

Kiểm tra nhanh skill chạy đúng end-to-end. Input mẫu: [synthetic-data/sample-mockup-input.md](../synthetic-data/sample-mockup-input.md) (design Husky + SKU `DAKO-HUSKY-LEG-001`).

---

## Bước 1 — Sinh bộ ảnh từ design + SKU
**Hành động:** đưa input mẫu (design Husky, SKU DAKO-HUSKY-LEG-001, is_winner=true) qua [prompt/make-mockup-prompt.md](../prompt/make-mockup-prompt.md).
**Pass khi:** trả ra `mockup-set` đúng schema với **6 ảnh** (hero-front, hero-back, lifestyle, detail, size, ad), mỗi ảnh có `type`/`ratio`/`prompt` hợp lệ.

## Bước 2 — Kiểm pipeline 2 bước & giữ print
**Hành động:** đọc các prompt AI enhance trong output.
**Pass khi:** mọi prompt enhance đều chứa câu giữ print (vd "KEEP the legging print exactly as input"); nền #F2F2F0; tỷ lệ đúng (1:1 / 4:5). Không có prompt text-to-image vẽ lại quần.

## Bước 3 — QC style conformance
**Hành động:** chạy QC theo Quality Gate (kb/visual-playbook §5).
**Pass khi:** `min_images_met=true` (6≥3), nền/tỷ lệ/ánh sáng ≥95%, ≥2000px sRGB; `confidence_score ≥ 0.7`.

## Bước 4 — GATE print-accuracy FAIL → need_review (test ngược)
**Hành động:** mô phỏng ảnh enhance bị AI đổi hoạ tiết → set `print_accuracy_pass=false`. Validate qua `schema/mockup-set.schema.json`.
**Pass khi:** schema **bắt buộc** `need_review=true` (allOf if/then). Nếu để `need_review=false` → validate FAIL. Hành động đúng: REJECT, render lại, inpaint chặt vùng quần.

## Bước 5 — Handoff
**Hành động:** host ảnh → điền `url` cho từng ảnh → bàn giao.
**Pass khi:** package có URL đủ ảnh, evidence[] (link design PRD-003 + ảnh), confidence/need_review hợp lệ; bàn giao `vibe-eu-opc-mer-product-page` (chị Lời); ảnh `ad` đẩy `vibe-eu-opc-grw-creative` (chị Ý).

---

**Reminder:** output là SPEC+PROMPT+QC; ảnh thật render bằng tool ngoài (Dynamic Mockups/Placeit/Botika/Photoroom).
