# 04 — Fulfillment & CX (dept: ful)

**Layer:** L2 (Operations) · **OPC:** 1 người + AI Workforce · **Ngày:** 2026-06-23
**Vai trò:** Order-Ops (route đơn ≤24h, tracking, on-time) + CX (support EN US/EU, size exchange XS–3XL, returns/refund, GDPR).

---

## Department IPO
| | |
|---|---|
| **Input** | Đơn ShopBase (từ 03-growth / Facebook Ads), customer tickets, provider production/shipping status |
| **Process** | Monitor & verify → route Printify/PrintBase ≤24h → track & gửi tracking → support EN → returns/refund |
| **Output** | Orders in production + tracking gửi khách · ticket resolved · **fee/cost & refund data → 05-backoffice** |

---

## Value Chain Position (Porter — L2)
```
03-growth (đơn paid) ──▶  [04-FULFILLMENT & CX]  ──▶ 05-backoffice (cost/refund/fee data)
   upstream                  L2 Operations                  downstream
```
- **Upstream:** 03-growth — đơn hàng từ Facebook Ads checkout trên ShopBase.
- **Downstream:** 05-backoffice — print/ship cost, refund, chargeback, fee để reconcile & P&L.

---

## Process IPOs (4 SOP)
| SOP | Process | Input → Output |
|---|---|---|
| [FUL-001](./monitor-orders/template/sop_ful-001_order-monitoring_v1.0_2026-06-23.md) | Order Monitoring & Verification | đơn ShopBase → verified queue + exception log |
| [FUL-002](./route-fulfillment/template/sop_ful-002_fulfillment-routing_v1.0_2026-06-23.md) | Routing & Tracking (⭐≤24h) | verified queue → orders in production + tracking |
| [FUL-003](./support-customer/template/sop_ful-003_cx-support_v1.0_2026-06-23.md) | Customer Support EN | ticket → resolved + resolution log |
| [FUL-004](./handle-returns/template/sop_ful-004_returns-refunds_v1.0_2026-06-23.md) | Returns, Refunds & Complaints | refund request → refund/reprint + data 05-backoffice |

---

## RACI (department-level)
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Verify & route đơn ≤24h | order-ops AI | OPC | 02-merch (mapping) | khách |
| Gửi tracking | order-ops AI | OPC | cx AI | khách |
| Support / size exchange | cx AI | OPC | order-ops AI | khách |
| Refund > threshold | OPC | OPC | cx AI | 05-backoffice |
| GDPR data request | cx AI | OPC | 05-backoffice | khách |

---

## KPI Summary
| KPI | Target | SOP |
|---|---|---|
| On-time routing (≤24h) | ≥ 98% | FUL-002 |
| Routing time (avg) | ≤ 12h | FUL-002 |
| First response time | ≤ 2h (SLA khách ≤4h) | FUL-003 |
| Resolution rate (24h) | ≥ 90% | FUL-003 |
| CSAT | ≥ 4.0 / 5 | FUL-003/004 |
| Refund rate | ≤ 3% | FUL-004 |
→ chi tiết: [kpi_ful-001](./kpi_ful-001_fulfillment-kpis_v1.0_2026-06-23.md) · [kri_ful-001](./kri_ful-001_key-result-indicators_v1.0_2026-06-23.md)

## OKR Summary
**Committed:** on-time routing ≥98%, CSAT ≥4.0, resolution rate ≥90%, first response ≤2h → align **Company O2 (vận hành đúng hạn)**. **Stretch x10:** zero-touch fulfillment + 100% CSAT auto.
→ [okr_ful-001](./okr_ful-001_quarterly-okr_v1.0_2026-06-23.md)

## Quality Standards Summary
SLI/SLO/SLA per SOP, SLA external (khách) luôn ≤ strict hơn SLO nội bộ (vd first response: SLO 2h < SLA 4h). Error budget on-time routing ≤2%, refund ≤3%.
→ [quality_ful-001](./quality_ful-001_quality-standards_v1.0_2026-06-23.md)

---

## AI Integration (SOP → AI Worker)
| SOP | AI Worker | Skill |
|---|---|---|
| FUL-001, FUL-002 | Order-Ops AI | `vibe-opc-pod-fulfillment-order-ops` |
| FUL-003, FUL-004 | CX AI | `vibe-opc-pod-fulfillment-cx` |

→ KWSR: [_knowledge](./_knowledge/README.md) · [_workflow](./_workflow/README.md) · [_skills-agents](./_skills-agents/README.md) · [_rules](./_rules/README.md)
