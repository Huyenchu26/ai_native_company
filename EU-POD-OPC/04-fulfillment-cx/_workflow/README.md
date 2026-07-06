# _workflow — Fulfillment & CX

**Dept:** 04-fulfillment-cx · **Ngày:** 2026-06-23
4 SOP + dependency + daily cadence. (W trong KWSR)

---

## SOP Chain (dependency)
```
03-growth (đơn paid)
      │
      ▼
FUL-001 Monitor & Verify ──exception──▶ FUL-003 CX (address/SKU)
      │ verified queue
      ▼
FUL-002 Route ≤24h + Tracking ──delay/defect──▶ FUL-003 CX
      │ cost data
      ▼
05-backoffice          FUL-003 CX ──refund──▶ FUL-004 Returns/Refunds
                                                   │ refund/cost data
                                                   ▼
                                              05-backoffice
```

| SOP | Trigger | Output | Next |
|---|---|---|---|
| FUL-001 | đơn paid mới | verified queue / exception | FUL-002 / FUL-003 |
| FUL-002 | verified queue | in-production + tracking | 05-backoffice |
| FUL-003 | ticket khách | resolved / size exchange | FUL-002 / FUL-004 |
| FUL-004 | refund request | refund/reprint | 05-backoffice |

---

## Daily Cadence
| Giờ (ICT) | Hoạt động | SOP | Worker |
|---|---|---|---|
| Mỗi 2h (giờ VH) | Sync & verify đơn | FUL-001 | order-ops AI |
| Mỗi 2–4h | Route batch ≤24h | FUL-002 | order-ops AI |
| Liên tục / ≤2h | First response ticket | FUL-003 | cx AI |
| 2×/ngày | Poll production + gửi tracking | FUL-002 | order-ops AI |
| EOD 23:00 | Sweep đơn chưa route + exception backlog | FUL-001/002 | order-ops AI |
| Weekly | CSAT, refund rate, KPI roll-up → 05-backoffice | all | OPC |

---

## SLA gates trong flow
- FUL-001 → FUL-002: chỉ đơn verified mới route (no fraud passthrough).
- FUL-002: hard gate **route ≤24h** + tracking trước khi đóng.
- FUL-004: refund > threshold gate qua OPC approve.

→ Rules chi tiết: [_rules](../_rules/README.md)
