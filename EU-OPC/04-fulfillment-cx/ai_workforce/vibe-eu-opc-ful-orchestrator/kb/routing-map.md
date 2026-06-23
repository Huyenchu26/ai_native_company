# KB — Routing Map (vibe-eu-opc-ful-orchestrator)

Manager-level routing cho phòng 04-fulfillment-cx, DAKOfits. Orchestrator **KHÔNG execute** — chỉ classify, route, enforce gate, bàn giao cost.

---

## 1. Task → Worker → SOP

| # | Task signal | Route → worker | SOP | Output mong đợi |
|---|-------------|----------------|-----|-----------------|
| 1 | Monitor/verify đơn ShopBase · exception · OOS · "đơn mới về", "đơn nào lỗi" | `vibe-eu-opc-ful-order-ops` | FUL-001 | Verified queue + exception log |
| 2 | Route Printify/PrintBase ≤24h theo vùng · gửi tracking · track production/shipping · "đẩy đơn đi in", "tracking" | `vibe-eu-opc-ful-order-ops` | FUL-002 | Orders in production + tracking gửi khách |
| 3 | Support EN · size exchange XS–3XL · hỏi đơn/tracking · complaint · "khách hỏi", "đổi size" | `vibe-eu-opc-ful-cx` | FUL-003 | Ticket resolved + resolution log |
| 4 | Returns/refund/reprint (gate $30) · chargeback intake · "hoàn tiền", "trả hàng" | `vibe-eu-opc-ful-cx` | FUL-004 | Refund/reprint + cost data 05-backoffice |
| 5 | **Batch đơn + ticket** (end-to-end dispatch) | **fan-out** order-ops (001→002) ∥ cx (003→004) | 001→002 / 003→004 | Batch điều phối + cost handoff |

> Khi task chứa nhiều signal (vd "10 đơn mới + 4 ticket support") ⇒ coi là **batch** (#5), fan-out theo loop §3.

---

## 2. Gate cứng (enforce TRƯỚC khi cho worker hành động)

| Gate | Điều kiện PASS | Fail ⇒ |
|------|----------------|--------|
| **Route ≤24h (SLO 18h)** | đơn verified route Printify/PrintBase ≤24h kể từ `paid_at`; provider đúng vùng (US→US, EU→EU); tracking đã gửi trước khi đóng "fulfilled" | breach >24h ⇒ ăn error budget (≤2%/tháng) + RCA + alert OPC; cross-region chỉ khi OOS |
| **Refund authority $30** | refund ≤ $30 → cx AI tự duyệt | > $30 ⇒ `decision=HOLD` + **OPC approve** trước khi thực thi; full-batch/chargeback ⇒ OPC + 05-backoffice; serial-refunder/fraud ⇒ flag + blocklist |
| **GDPR data minimization** | chỉ truy cập data cần xử item; không leak data khách giữa ticket; reply EN không lộ đơn/khách khác | leak/over-access ⇒ BLOCK reply; erasure quá 30 ngày ⇒ escalate; KHÔNG xóa data có nghĩa vụ kế toán/VAT |
| **Fraud-hold** | đơn không risk/mismatch, ≤ $150 | risk cao / billing-shipping mismatch / nhiều đơn cùng card / > $150 ⇒ HOLD + escalate OPC ≤12h; KHÔNG auto-route đơn fraud-hold sang print |

Luật vận hành đầy đủ: [`../../_rules/README.md`](../../_rules/README.md). KPI/SLA: [`../../README.md`](../../README.md).

---

## 3. Batch dispatch loop (đơn từ Growth → Fulfillment & CX → cost 05-backoffice)

```
[03-growth: batch đơn paid + ticket tồn]
  → CLASSIFY: tách đơn (order-ops) vs ticket support/refund (cx)
  → ENFORCE gate fraud-hold (risk/mismatch/>$150) trước khi route print
  → ROUTE order-ops (FUL-001): verify đơn, exception, chọn provider đúng vùng
  → ENFORCE gate route ≤24h (SLO 18h)
        ├─ paid→route ≤24h & tracking đã gửi   → on-time OK
        ├─ sắp chạm 24h                          → ưu tiên route + alert OPC
        └─ breach >24h                           → error budget + RCA + escalate OPC
  → ROUTE order-ops (FUL-002): route Printify/PrintBase, track production, gửi tracking
  → ROUTE cx (FUL-003): support EN, ưu tiên size exchange/reprint trước refund
  → ROUTE cx (FUL-004): returns/refund — ENFORCE gate $30
        ├─ refund ≤ $30        → cx AI tự duyệt
        ├─ refund > $30        → HOLD + OPC approve
        └─ chargeback/fraud    → HOLD + escalate OPC + 05-backoffice
  → REPORT cost: tổng print/ship cost + refund/chargeback → bàn giao 05-backoffice
```

Cadence (theo `_workflow/README.md`): liên tục monitor đơn (FUL-001) → route trong cửa sổ ≤18h SLO → first response ticket ≤2h (SLA khách ≤4h) → resolution ≤24h.

---

## 4. Cost handoff → 05-backoffice (downstream)

Sau mỗi batch dispatch, tổng hợp và **bàn giao [`vibe-eu-opc-bck-orchestrator`](../../../05-backoffice/)** (finance reconcile P&L):
- **print/ship cost** per đơn đã route (theo provider US/EU).
- **refund_total** + **chargeback_total** đã thực thi trong batch.
- Đính kèm `cost_handoff` trong `fulfillment-dispatch.json` + evidence[] (link đơn/refund).
- GDPR erasure liên quan data kế toán/VAT → phối **05-backoffice compliance** (SOP-BCK-005), KHÔNG tự xóa.

---

## 5. Escalation matrix (việc KHÔNG route nội bộ)

| Trigger | Escalate tới | SLA |
|---------|--------------|-----|
| Fraud-hold (risk/mismatch/>$150) | **OPC** | ≤12h |
| SLA route breach (>24h) | **OPC** | ngay + RCA |
| Refund > $30 | **OPC** approve | trước khi refund |
| Complaint pháp lý / chargeback | **OPC + 05-backoffice** | ≤24h |
| GDPR erasure request | cx → OPC → 05-backoffice compliance | ≤30 ngày |
| Provider reject/OOS không giải được | **OPC + 02-merchandising** | ≤24h |
| Cost lệch / cần reconcile / VAT | **05-backoffice** finance | — |
| Đơn nguồn sai / vấn đề ads | **03-growth** | — |

---

## 6. need_review triggers (đẩy `processing/human-review/`)
gate fail · route breach >24h · refund > $30 · fraud-hold · chargeback/legal complaint · GDPR erasure · confidence_score < 0.7 · task mơ hồ không map được worker.
