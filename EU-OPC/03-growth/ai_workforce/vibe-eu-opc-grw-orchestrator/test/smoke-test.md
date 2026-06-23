# Smoke Test — vibe-eu-opc-grw-orchestrator

5 bước kiểm chứng Manager điều phối đúng + enforce gate. PASS toàn bộ ⇒ skill sẵn sàng.

---

## Bước 1 — Route đúng worker (classify)
**Input:** "Tối ưu lại campaign SP US-BULLDOG-001 đang ROAS tụt."
**Expect:** route → `vibe-eu-opc-grw-fb-ads` (SOP-GRW-002). KHÔNG tự xử lý, KHÔNG route creative/marketing.
**PASS khi:** `routing[].worker = vibe-eu-opc-grw-fb-ads`, `sop = SOP-GRW-002`.

## Bước 2 — Fan-out đợt promote (batch)
**Input:** batch 6 SP từ 02-merch (xem `synthetic-data/sample-batch-input.md`).
**Expect:** lập `growth-batch-plan` hợp lệ (validate schema), routing tuần tự creative (005) → fb-ads (002) → report (004); marketing (003/001) bổ trợ.
**PASS khi:** plan validate `schema/growth-batch-plan.schema.json`, có đủ creative_assignee + ads_assignee, routing ≥ 3 bước.

## Bước 3 — Enforce gate Meta Ad Policy
**Input:** 1 SP trong batch CHƯA có clearance 05-compliance.
**Expect:** `gate_checks.meta_policy.status != pass` ⇒ `decision=HOLD`, `need_review=true`, KHÔNG cho fb-ads launch SP đó, trả về creative/compliance.
**PASS khi:** SP đó BLOCKED, không xuất hiện trong lệnh launch ads.

## Bước 4 — Enforce winner = BE-ROAS per-SKU (chống lãi ảo)
**Input:** SP EU-CORGI-003, price €49.99, Blended ROAS 3.2, BE-ROAS EU = 5.3.
**Expect:** 3.2 < 5.3 ⇒ KHÔNG scale (dù > 2.5); `decision=HOLD`, đề xuất nâng giá/đổi provider. Xác nhận KHÔNG dùng ngưỡng 2.5 cứng.
**PASS khi:** decision = HOLD, evidence dẫn BE-ROAS từ unit-economics.

## Bước 5 — Budget escalate + need_review
**Input:** tổng spend đợt = $180/ngày, confidence_score = 0.6.
**Expect:** > $150/ngày ⇒ escalate OPC + 05-finance; confidence < 0.7 ⇒ `need_review=true` → `processing/human-review/`.
**PASS khi:** `escalation[]` chứa OPC + 05-finance, `need_review=true`, artifact ở human-review.

---

**Kết quả mong đợi:** 5/5 PASS. Mọi bước ghi `execution_log.jsonl` theo `schema/execution-log-entry.schema.json`.
