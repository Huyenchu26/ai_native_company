# SOP-FUL-001 — Order Monitoring, QC & Tracking (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 04-Fulfillment-CX · **Responsible AI:** `vibe-us-warm-ful-order-ops`
**Differentiator (vs customwarms):** QC vật liệu thật + **KHÔNG tracking giả** (đối thủ bị tố tracking giả).

## 1. Mục tiêu
Theo dõi đơn từ paid → shipped, ép **2 gate cứng đạo đức**: (a) QC chăn đạt spec trước ship, (b) chỉ gửi tracking khi có mã carrier THẬT.

## 2. IPO/ICOM
- **Input:** order (personalization), supplier status, QC photo, carrier tracking.
- **Control:** QC gate (material_gsm ≥ 260, qc_photo_pass, personalization đúng); **no-fake-tracking** (tracking_sent ⇒ carrier_code verified real); SLA tracking ≤ 24h sau ship.
- **Output:** `order-status.json` (schema `order-status.schema.json`).
- **Mechanism:** supplier API, carrier tracking API (thiếu → tracking_sent=false, KHÔNG bịa mã).

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Nhận đơn paid, route supplier | order_value > $150 → flag fraud review |
| 3.2 | **QC trước ship** | material_gsm < 260 / qc_photo fail / sai personalization → HOLD, không ship |
| 3.3 | **Tracking** | CHỈ set tracking_sent=true khi có carrier_code THẬT verified. Không có → false + note (chống tracking giả) |
| 3.4 | Monitor SLA | tracking ≤24h; chậm → escalate |

## 4. RACI
R: ful-order-ops · A: Owner · C: bck-finance (cost) · I: ful-cx.
HITL: QC fail lặp; fraud > $150; supplier lỗi.

## 5. Quality Gate
| SLI | SLO | On fail |
|-----|-----|---------|
| QC material_gsm | ≥ 260 | HOLD, không ship |
| Fake tracking | 0 (100% carrier thật) | block ship-notify |
| Tracking sent | ≤ 24h sau ship | escalate |

**Gate (allOf/if-then):** ship_approved=true ⇒ qc_photo_pass=true ∧ material_gsm≥260. tracking_sent=true ⇒ carrier_code present ∧ carrier_verified=true (no-fake-tracking).

## 6. Links
Downstream: [returns](../../handle-returns/template/sop_ful-004_returns_v1.0_2026-08-04.md), [support](../../support-customer/template/sop_ful-003_cx-support_v1.0_2026-08-04.md). Charter promises: [../../00-company/charter_company-charter_v1.0_2026-08-04.md](../../../00-company/charter_company-charter_v1.0_2026-08-04.md).

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — QC gate chăn + no-fake-tracking (đối thủ yếu). |
