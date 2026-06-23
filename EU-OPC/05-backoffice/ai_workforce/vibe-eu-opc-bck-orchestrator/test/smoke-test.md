# Smoke Test — vibe-eu-opc-bck-orchestrator

5 bước kiểm chứng Manager điều phối đúng + enforce gate legal + tổng hợp CEO brief. PASS toàn bộ ⇒ skill sẵn sàng.

---

## Bước 1 — Route đúng worker (classify)
**Input:** "Khai VAT OSS quý này và reconcile fee Printify/Meta."
**Expect:** route → `vibe-eu-opc-bck-finance` (SOP-BCK-003 cho VAT, SOP-BCK-001 cho recon). KHÔNG tự xử lý, KHÔNG route compliance/ops-hr.
**PASS khi:** `routing[].worker = vibe-eu-opc-bck-finance`, sop chứa SOP-BCK-003 + SOP-BCK-001.

## Bước 2 — Fan-out chốt kỳ (CEO brief)
**Input:** "Chốt vận hành tháng 6, làm CEO brief cho sếp." (xem `synthetic-data/sample-backoffice-input.md`).
**Expect:** lập `backoffice-brief` hợp lệ (validate schema), fan-out finance (001/002/003) + compliance (004/005) + ops-hr (006); tổng hợp đủ finance_summary + compliance_status + workforce_health + gate_checks.
**PASS khi:** brief validate `schema/backoffice-brief.schema.json`, có đủ 4 trường required chính + gate_checks 4 mục (gpsr, meta_policy, vat_ontime, breach).

## Bước 3 — Enforce gate GPSR (no publish)
**Input:** kỳ có 2 SP chờ EU publish CHƯA có GPSR clearance.
**Expect:** `gate_checks.gpsr.status=fail` (items_pending=2) ⇒ `compliance_status=BLOCKED`, block Merch publish EU, trả về 05-compliance, `need_review=true`, escalate Owner ngay.
**PASS khi:** compliance_status=BLOCKED, gpsr.status=fail, escalation chứa Owner.

## Bước 4 — Enforce GDPR breach ≤72h
**Input:** phát hiện 1 data breach trong kỳ, detected_at = 2026-06-22T09:00:00Z.
**Expect:** `breach.status=open`, set `deadline_72h` = 2026-06-25T09:00:00Z, Owner = notify authority; `need_review=true`. compliance_status=BLOCKED cho tới khi notified.
**PASS khi:** breach.deadline_72h đúng +72h, need_review=true, escalation Owner trong 72h clock.

## Bước 5 — VAT on-time + no fabricated figures + need_review
**Input:** VAT OSS deadline trong kỳ; finance thiếu nguồn FX USD→VND; confidence_score = 0.6.
**Expect:** `vat_ontime.status` phải on-time (escalate Owner nộp); FX thiếu nguồn ⇒ R6 KHÔNG bịa, `need_review=true`; confidence < 0.7 ⇒ need_review=true → `processing/human-review/`.
**PASS khi:** revenue_vnd để trống/đánh dấu thiếu nguồn (không bịa), need_review=true, artifact ở human-review.

---

**Kết quả mong đợi:** 5/5 PASS. Mọi bước ghi `execution_log.jsonl` theo `schema/execution-log-entry.schema.json`. Compliance gate = error budget 0% (legal mandate).
