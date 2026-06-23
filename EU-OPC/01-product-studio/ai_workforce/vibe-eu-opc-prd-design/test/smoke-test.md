# Smoke Test — vibe-eu-opc-prd-design

Mục tiêu: xác minh skill chạy đúng pipeline design → QC 360° → IP/TM clearance → handoff, và **gate cứng fail-closed** khi REJECT.

## Bước 1 — Generate design từ validated niche
- Input: `synthetic-data/sample-design-input.md` (niche "Border Collie", pre-flag LOW).
- Kỳ vọng: chọn 1/4 style; tạo file 300 DPI theo canvas template provider; tile/mandala có seamless tile.
- PASS khi: `design_type ∈ {tile,watercolor,funny,mandala}` và `dpi ≥ 300`.

## Bước 2 — QC 360°
- Chạy checklist seam/crotch/waistband + bleed + canvas px.
- PASS khi: `qc_360_pass = true` và có `evidence[]` source `file-metadata` + `qc-report`.
- Negative: ép DPI=250 → kỳ vọng QC fail, re-generate, KHÔNG handoff.

## Bước 3 — IP/TM clearance dual lookup
- Trích term "Border Collie", tra **USPTO + EUIPO** + blocklist.
- PASS khi: `uspto_checked = true` VÀ `euipo_checked = true`, có evidence cả 2 nguồn.
- Negative: chỉ check USPTO (euipo_checked=false) → schema validation FAIL nếu cố set `ip_clearance_status=PASS`.

## Bước 4 — TEST GATE FAIL-CLOSED (REJECT)
- Input niche dính TM exact match (vd term có live trademark, hoặc blocklist club/brand).
- Kỳ vọng: `ip_clearance_status = REJECT`, `handoff_ready` KHÔNG được true.
- PASS khi: schema chặn `handoff_ready=true` lúc status ≠ PASS; record vào `human-review/`; KHÔNG bàn giao Merch.
- Đồng thời test MODIFY: TM similar cùng class → `MODIFY`, loop sửa term/artwork → re-clear, vẫn chưa handoff cho tới khi PASS.

## Bước 5 — Handoff + confidence/need_review
- Design PASS hết → `handoff_ready = true` → package ra `output/` (print-ready + mockup + clearance log) bàn giao `vibe-eu-opc-mer-orchestrator`.
- Negative: `confidence_score = 0.6` → kỳ vọng `need_review = true` (schema ép), đẩy `human-review/`, không auto-handoff.
- Xác minh: ghi `execution_log.jsonl` đúng `schema/execution-log-entry.schema.json`.

## Kết quả mong đợi
Tất cả 5 bước PASS → skill sẵn sàng. Đặc biệt Bước 4: **không có clearance PASS thì tuyệt đối không handoff** (no clearance → no listing).
