# _workflow — 03-growth

Trình tự & phụ thuộc giữa 5 SOP, cùng cadence vận hành.

## 1. SOP & dependency
```
[02 live product+page] + [05 Meta Ad Policy clearance]
            │
            ▼
   SOP-GRW-005 (Creative) ──creative package──► SOP-GRW-002 (FB Ads ABO→CBO)
            ▲                                          │
            │ refresh khi fatigue                      ├─► đơn ► 04-fulfillment-cx
            │                                          └─► cost/ROAS ► 05-backoffice
   SOP-GRW-001 (Organic) ─social proof/UGC─┐           │
   SOP-GRW-003 (Email)   ─LTV/repeat───────┤           │
                                            ▼           ▼
                              SOP-GRW-004 (Growth Report) ──alert/khuyến nghị──┐
                                            ▲                                  │
                                            └──────── feedback loop ───────────┘
```
- **Gate vào:** No Meta Ad Policy → No ads (005/002 dừng).
- **Đồng bộ:** đợt promote (SOP-MER-006) → 005 tạo creative cho 5–10 SP/đợt → 002 test → scale winner.

## 2. Cadence
| Nhịp | Hoạt động | SOP |
|------|-----------|-----|
| **Daily** | check ROAS/CPA/CTR/frequency, scale/kill, snapshot report | 002, 004 |
| **Mỗi 2 ngày** | scale winner +20% | 002 |
| **Per send / event** | email flow, organic post | 003, 001 |
| **Weekly** | trend review + khuyến nghị + on/off-track O1 + creative refresh batch | 004, 005 |
| **Per batch** | đợt promote mới: creative → launch ABO | 005 → 002 |

## 3. Vòng feedback
SOP-GRW-004 đọc signal cross-channel → trigger: scale (002), refresh hook (005), tinh chỉnh flow (003), điều chỉnh seeding (001). Đóng vòng học liên tục.

## 4. Handoff out
- Đơn → 04-fulfillment-cx · Cost/ROAS → 05-backoffice/finance · Report → 00-company.

> Liên quan: [`_knowledge`](../_knowledge/README.md) · [`_rules`](../_rules/README.md)
