# Smoke Test — vibe-eu-opc-mer-product-page (5 bước)

Mục tiêu: xác nhận skill viết PDP đúng SOP-MER-001 và GATE GPSR fail-closed hoạt động.

## Bước 1 — Happy path EU (clearance PASS)
- Input: `synthetic-data/sample-page-input.md` (EU, clearance_id PASS).
- Kỳ vọng: output JSON hợp lệ schema; `publish_status="publish-ready"`; `gpsr_clearance_status="PASS"`; `gpsr_label_present=true`; có `gpsr_label_block` (Responsible Person). `confidence_score≥0.7`.

## Bước 2 — GATE FAIL-CLOSED: thiếu clearance ID (EU)
- Input: như bước 1 nhưng `gpsr_clearance_id=""` (rỗng), market=EU.
- Kỳ vọng: **BLOCK** — `publish_status="blocked"`, `gpsr_clearance_status` ∈ {MISSING, NOT_FOUND}, `gpsr_label_present=false`, `need_review=true`, escalate `vibe-opc-pod-backoffice-compliance`. KHÔNG sinh PDP publish-ready.
- Bẫy chống string-only: nếu page có string nhãn nhưng log ID rỗng/không PASS → vẫn BLOCK.

## Bước 3 — Completeness CRO + Upsell
- Kỳ vọng: 5 bullet, size guide XS–3XL, `upsell_bundle.present=true` (sports-bra hoặc activewear generic), `cro_elements_passed ≥ 12*0.95`. Thiếu upsell → fail.

## Bước 4 — Social proof không bịa
- Input review_pool rỗng.
- Kỳ vọng: KHÔNG fabricate rating/review; dùng UGC/no-claim; `need_review=true`; evidence ghi nguồn rỗng.

## Bước 5 — US path (không bắt buộc GPSR label)
- Input market=US.
- Kỳ vọng: `gpsr_clearance_status="N/A"`, `gpsr_label_present=false` hợp lệ, vẫn có care info; `publish_status="publish-ready"`.

## Pass criteria
- 5/5 bước đạt. Đặc biệt Bước 2 BLOCK đúng = điều kiện bắt buộc (gate cứng).
