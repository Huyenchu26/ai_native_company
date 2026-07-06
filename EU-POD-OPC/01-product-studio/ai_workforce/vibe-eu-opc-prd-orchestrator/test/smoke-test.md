# Smoke Test — vibe-eu-opc-prd-orchestrator

**Mục tiêu:** xác minh Manager route đúng, enforce IP gate, và handoff Merch
(KHÔNG handoff thẳng Growth). 5 bước.

---

## Bước 1 — Route research đúng worker
**Input:** "Có batch niche seed mới, cần research và scoring."
**Kỳ vọng:** route sang `vibe-eu-opc-prd-niche-research` (SOP-PRD-001/002).
KHÔNG tự research. Output có `evidence[]` + `confidence_score`.
**PASS khi:** worker đích = niche-research; Manager không tự execute.

## Bước 2 — Route design đúng worker
**Input:** validated niche list từ bước 1.
**Kỳ vọng:** route sang `vibe-eu-opc-prd-design` cho SOP-PRD-003 (AOP design 300
DPI, QC 360°) rồi SOP-PRD-004 (clearance).
**PASS khi:** worker đích = design; design type ∈ {tile,watercolor,funny,mandala}.

## Bước 3 — Enforce IP/TM gate (CLEAR cho qua)
**Input:** design có `clearance_status = CLEAR`, dual-market USPTO+EUIPO done.
**Kỳ vọng:** design vào `cleared_designs[]`;
`gate_checks.ip_tm_clearance = CLEAR`.
**PASS khi:** chỉ design CLEAR được nạp vào cleared_designs.

## Bước 4 — Enforce IP/TM gate (nghi ngờ → conservative REJECT)
**Input:** design có term nghi ngờ trademark (uncertain).
**Kỳ vọng:** conservative default = **REJECT**; `need_review = true`; đẩy OPC.
**KHÔNG** đưa vào cleared_designs; **KHÔNG** handoff.
**PASS khi:** design uncertain bị REJECT, không lọt gate.

## Bước 5 — Handoff Merch, KHÔNG thẳng Growth
**Input:** batch cleared_designs hợp lệ.
**Kỳ vọng:** `handoff_to_merch = true`, `shopbase_live_required = true`, đích =
`vibe-eu-opc-mer-orchestrator`. Handoff note nêu rõ Merch đăng LIVE ShopBase
TRƯỚC, rồi Growth mới content/ads.
**FAIL khi:** đích là Growth, hoặc thiếu shopbase_live_required, hoặc bàn giao
thẳng Growth bỏ qua Merch.

---

## Tổng kết
| Bước | Kiểm tra | Pass/Fail |
|------|----------|-----------|
| 1 | Route research | |
| 2 | Route design | |
| 3 | IP gate CLEAR | |
| 4 | IP gate conservative REJECT | |
| 5 | Handoff Merch (không thẳng Growth) | |
