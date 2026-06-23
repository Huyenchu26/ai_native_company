# Smoke Test — vibe-eu-opc-mer-orchestrator

5 bước xác minh orchestrator route đúng, enforce GPSR gate, handoff Growth. Pass = tất cả 5 bước đạt.

---

### Bước 1 — Route việc chuyên môn (KHÔNG tự execute)
**Input:** "Set pricing cho variant XS–3XL của SP Beagle legging."
**Expected:** Manager **route** sang `vibe-eu-opc-mer-catalog` (SOP-MER-003), KHÔNG tự tính giá. Routing entry: task=pricing, worker=`vibe-eu-opc-mer-catalog`, sop=MER-003.
**Pass nếu:** delegate đúng worker, không execute trực tiếp.

### Bước 2 — Route product page
**Input:** "Viết product page cho 3 SP mới."
**Expected:** route sang `vibe-eu-opc-mer-product-page` (SOP-MER-001), yêu cầu chèn GPSR label cho SP EU.
**Pass nếu:** worker đúng + nhắc GPSR label EU.

### Bước 3 — Enforce GPSR gate (đơn EU thiếu clearance)
**Input:** Batch 6 SP, trong đó 2 SP market=EU **chưa có** GPSR clearance.
**Expected:** `gate_checks.gpsr.passed=false` cho 2 SP EU → **block publish**, escalate phòng 05-backoffice, `need_review=true`, `handoff_to_growth=false`.
**Pass nếu:** không publish/handoff SP EU thiếu GPSR; escalation đúng địa chỉ.

### Bước 4 — Enforce contribution margin (chống lãi ảo)
**Input:** SP US giá $39.99, base $22 + ship $8 + fee $1.8, CPA dự kiến $20.
**Expected:** Manager tính CM sau ads → âm/quá thấp → `contribution_margin.passed=false`, flag re-price hoặc đổi provider; KHÔNG handoff vì "gross margin nhìn ổn".
**Pass nếu:** dùng contribution margin sau ads (per `unit-economics.md`), không dùng gross ảo; tính be_roas per-SKU.

### Bước 5 — Handoff Growth (đợt sạch gate)
**Input:** Batch 5 SP, tất cả GPSR passed, margin band ok, CM dương, confidence 0.82.
**Expected:** `merch-batch-plan` hợp lệ schema, `handoff_to_growth=true`, route sang `vibe-eu-opc-grw-orchestrator` (SOP-GRW-002), kèm be_roas per-SKU + audience hint.
**Pass nếu:** package validate schema + handoff đúng downstream + có evidence/confidence.

---
**Kết quả:** ___ / 5 pass. Bất kỳ bước fail → fix skill trước khi dùng thật.
