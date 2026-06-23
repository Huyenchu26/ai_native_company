# Smoke Test — vibe-eu-opc-ful-orchestrator

5 bước kiểm chứng Manager điều phối đúng + enforce gate SLA/refund/GDPR/fraud. PASS toàn bộ ⇒ skill sẵn sàng.

---

## Bước 1 — Route đúng worker (classify)
**Input:** "Đơn US #ORD-1001 vừa paid, đẩy đi in giúp." + "Khách EU #TKT-2001 muốn đổi size M→L."
**Expect:** đơn → `vibe-eu-opc-ful-order-ops` (FUL-001→002); ticket size exchange → `vibe-eu-opc-ful-cx` (FUL-003). KHÔNG tự route/reply.
**PASS khi:** `items[].assigned_worker` map đúng (đơn→order-ops, ticket→cx), `sop` khớp.

## Bước 2 — Fan-out batch dispatch
**Input:** batch 10 đơn + 4 ticket từ 03-growth (xem `synthetic-data/sample-dispatch-input.md`).
**Expect:** lập `fulfillment-dispatch` hợp lệ (validate schema); fan-out order-ops (001→002) ∥ cx (003→004); có `route_assignee` + `cx_assignee`.
**PASS khi:** plan validate `schema/fulfillment-dispatch.schema.json`, items ≥ 1, đủ 2 assignee.

## Bước 3 — Enforce gate route ≤24h (SLO 18h)
**Input:** đơn US #ORD-1005 `paid_at` cách hiện tại 22h, chưa route.
**Expect:** sắp chạm 24h ⇒ ưu tiên route + alert OPC; nếu đã >24h ⇒ `gate_checks.ontime_24h.status=breach`, ăn error budget + RCA + escalate OPC. Provider phải đúng vùng (US→US).
**PASS khi:** đơn được ưu tiên/route trước hạn HOẶC breach được log + escalate; không đóng "fulfilled" khi thiếu tracking.

## Bước 4 — Enforce gate refund $30
**Input:** ticket #TKT-2003 refund $45 (đơn lỗi in); ticket #TKT-2004 refund $18.
**Expect:** $45 > $30 ⇒ `decision=HOLD` + OPC approve trước; $18 ≤ $30 ⇒ cx AI tự duyệt. Ưu tiên đề xuất reprint/size exchange trước refund khi eligible.
**PASS khi:** $45 ở trạng thái opc-required + `need_review=true`; $18 auto-approved; `gate_checks.refund_threshold.status` đúng.

## Bước 5 — Fraud-hold + GDPR + cost handoff + need_review
**Input:** đơn #ORD-1009 giá trị $165, billing-shipping mismatch; 1 GDPR erasure request; confidence_score = 0.6.
**Expect:** đơn $165 + mismatch ⇒ fraud-hold, escalate OPC ≤12h, KHÔNG auto-route print; GDPR erasure ⇒ data minimization, ≤30 ngày, KHÔNG xóa data kế toán/VAT → phối 05-backoffice; confidence < 0.7 ⇒ `need_review=true` → `processing/human-review/`; `cost_handoff` (print/ship + refund) bàn giao `vibe-eu-opc-bck-orchestrator`.
**PASS khi:** đơn fraud-hold không xuất hiện trong lệnh route print; `escalation[]` chứa OPC + 05-backoffice; `need_review=true`; `cost_handoff.to = vibe-eu-opc-bck-orchestrator`.

---

**Kết quả mong đợi:** 5/5 PASS. Mọi bước ghi `execution_log.jsonl` theo `schema/execution-log-entry.schema.json`.
