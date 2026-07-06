# Synthetic Data — Sample Dispatch Input (1 batch đơn + ticket)

Batch mẫu: đơn paid bàn giao từ 03-growth (FB Ads checkout) + ticket tồn cho orchestrator điều phối. Dữ liệu giả lập, không phải đơn/khách thật.

---

## Batch metadata
- **batch_id:** `DISP-2026-06-W26-001`
- **source:** `vibe-eu-opc-grw-orchestrator` (03-growth)
- **ngày:** 2026-06-23
- **now (mốc tính SLA):** 2026-06-23T12:00:00Z
- **error budget on-time:** ≤2%/tháng · **refund cap:** ≤$30 cx / >$30 OPC

## Orders (đơn — route → vibe-eu-opc-ful-order-ops)

| # | order_id | Market | paid_at | Giá trị | Provider vùng | Ghi chú |
|---|----------|--------|---------|---------|---------------|---------|
| 1 | ORD-1001 | US | 2026-06-23T06:00:00Z | $39.99 | Printify-US | bình thường |
| 2 | ORD-1002 | EU | 2026-06-23T05:30:00Z | €49.99 | Printify-EU | bình thường |
| 3 | ORD-1005 | US | 2026-06-22T13:30:00Z | $42.99 | Printify-US | **22.5h từ paid → sắp chạm 24h**, ưu tiên route |
| 4 | ORD-1007 | EU | 2026-06-23T08:00:00Z | €52.99 | Printify-EU | variant OOS → exception, có thể cross-region |
| 5 | ORD-1009 | US | 2026-06-23T09:00:00Z | **$165.00** | — | **billing-shipping mismatch → fraud-hold**, KHÔNG auto-route print |

## Tickets (support/refund → vibe-eu-opc-ful-cx)

| # | ticket_id | Market | Type | refund_amount | Ghi chú |
|---|-----------|--------|------|---------------|---------|
| A | TKT-2001 | EU | size-exchange | — | đổi M→L, ưu tiên exchange/reprint trước refund |
| B | TKT-2002 | US | tracking | — | khách hỏi tracking đơn đã route |
| C | TKT-2003 | US | refund | **$45.00** | đơn lỗi in → **> $30 ⇒ HOLD + OPC approve** |
| D | TKT-2004 | EU | refund | $18.00 | giao trễ nhẹ → ≤ $30 ⇒ cx AI tự duyệt |
| E | TKT-2005 | EU | gdpr-request | — | **erasure request** → data minimization, ≤30 ngày, KHÔNG xóa data kế toán/VAT |

## Kỳ vọng điều phối (để đối chiếu test)
- ORD-1001/1002 → ROUTE order-ops, provider đúng vùng, route ≤18h SLO, gửi tracking.
- ORD-1005 → ưu tiên route ngay (gần 24h) + alert OPC; nếu breach ⇒ error budget + RCA.
- ORD-1007 → exception OOS, đề xuất cross-region; nếu không giải được ⇒ escalate OPC + 02-merchandising.
- ORD-1009 → **fraud-hold** ($165 + mismatch), escalate OPC ≤12h, KHÔNG route print.
- TKT-2001 → size exchange/reprint (ưu tiên trước refund). TKT-2002 → cung cấp tracking.
- TKT-2003 ($45) → **HOLD + OPC approve**. TKT-2004 ($18) → cx tự duyệt.
- TKT-2005 → GDPR erasure, ≤30 ngày, phối 05-backoffice compliance, KHÔNG xóa data VAT.
- **Cost handoff:** tổng print/ship cost đơn đã route + refund_total ($18 duyệt; $45 chờ OPC) → bàn giao `vibe-eu-opc-bck-orchestrator`.
- need_review = true cho: ORD-1005 (nếu breach), ORD-1009 (fraud), TKT-2003 (>$30), TKT-2005 (GDPR erasure).
