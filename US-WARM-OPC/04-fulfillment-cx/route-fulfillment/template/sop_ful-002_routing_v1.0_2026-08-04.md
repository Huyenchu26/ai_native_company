# SOP-FUL-002 — Fulfillment Routing (US supplier)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 04-Fulfillment-CX · **Responsible AI:** `vibe-us-warm-ful-order-ops`

## 1. Mục tiêu
Route đơn tới supplier US phù hợp (chăn), tối ưu lead-time + cost, giữ QC.

## 2. IPO
- Input: paid order, supplier roster (US), SLA.
- Control: route ≤ 18h; supplier đạt QC spec (GSM); cost trong unit-economics.
- Output: routing quyết định (gộp trong order-status.json).
- Mechanism: supplier API (thiếu → manual/pending).

## 3. Gate: routed=true ⇒ supplier_qc_capable=true (supplier cam kết GSM≥260). Route SLO ≤18h.

## 4. RACI: R ful-order-ops · A Owner · C bck-finance · I ful-cx.

## 5. Links: [monitor-orders](../../monitor-orders/template/sop_ful-001_order-monitoring_v1.0_2026-08-04.md), [unit-economics](../../../_shared/unit-economics.md).

## 6. History
| 1.0 | 2026-08-04 | Khởi tạo — US supplier routing, QC-capable gate. |
