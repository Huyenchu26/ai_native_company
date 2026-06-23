# _skills-agents — Fulfillment & CX

**Dept:** 04-fulfillment-cx · **Ngày:** 2026-06-23
2 AI Worker + coverage matrix. (S trong KWSR)

---

## AI Workers
### 1. Order-Ops AI — `vibe-opc-pod-fulfillment-order-ops`
- **Responsible:** SOP-FUL-001, SOP-FUL-002.
- **Nhiệm vụ:** giám sát đơn ShopBase, verify, route Printify ≤24h, xử lý ngoại lệ, theo dõi production/shipping, gửi tracking, giữ on-time.
- **Output:** orders in production + tracking gửi khách + cost data → 05-backoffice.

### 2. CX AI — `vibe-opc-pod-fulfillment-cx`
- **Responsible:** SOP-FUL-003, SOP-FUL-004.
- **Nhiệm vụ:** support EN US/EU, size exchange XS–3XL, returns/refund/complaint, giữ rating, GDPR.
- **Output:** ticket resolved + resolution log + refund data → 05-backoffice.

---

## Coverage Matrix (SOP → Worker)
| SOP | Order-Ops AI | CX AI | OPC (human gate) |
|---|---|---|---|
| FUL-001 Monitor | **R** | C (exception khách) | A — fraud hold/cancel |
| FUL-002 Route ≤24h | **R** | C (delay comms) | A — SLA breach |
| FUL-003 CX support | C (re-route) | **R** | A — complaint pháp lý, GDPR erasure |
| FUL-004 Returns/refund | C (reprint) | **R** | A — refund > threshold, chargeback |

**Coverage:** 4/4 SOP có responsible AI. Human-in-loop chỉ ở gate: fraud, SLA breach, refund > threshold, GDPR erasure, complaint pháp lý.

---

## Skill matrix
| Skill | Order-Ops AI | CX AI |
|---|---|---|
| ShopBase order ops | ✓ | ✓ (read) |
| Printify/PrintBase routing | ✓ | — |
| Tracking/carrier | ✓ | ✓ (WISMO) |
| EN customer comms | — | ✓ |
| Size chart XS–3XL advisory | — | ✓ |
| Refund/chargeback handling | — | ✓ |
| GDPR data handling | ✓ (minimization) | ✓ |
| Fraud/risk screening | ✓ | — |

→ Worker performance & capacity theo dõi bởi 05-backoffice ops-hr (SOP-BCK-006).
