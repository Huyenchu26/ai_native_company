# _rules — 03-growth

Luật cứng & mềm chi phối phòng Growth. Gate cứng đứng trên mọi SLO/KPI.

## 1. GATE CỨNG (không override)
| Rule | Nội dung | Hệ quả vi phạm |
|------|----------|----------------|
| **No Meta Ad Policy → No ads** | Creative + landing page phải pass Meta Ad Policy (clearance 05-compliance) trước khi bật campaign | STOP launch; trả về 005/05-compliance |
| **GDPR — opt-in only** | Email chỉ gửi subscriber có explicit consent; honor unsubscribe + erasure | Exclude/xóa; không tiêu error budget |
| **Cost source of truth = 05-finance** | Report phải reconcile cost trước khi công bố | HOLD report |

## 2. Luật vận hành (định lượng)
| Rule | Ngưỡng |
|------|--------|
| **Scale rule** | tăng budget **≤ 20% / 2 ngày** (không sốc, không reset learning) |
| **Kill-loser rule** | ROAS < 1.5 sau 3 ngày & spend ≥ 2× CPA target ($40) → KILL; hoặc CPA>$20 & 0 conv sau $30 → KILL |
| **Winner rule** | **Blended ≥ BE-ROAS theo SKU/market** (US ~2.75, EU ~5.3 — KHÔNG dùng 2.5 cứng; xem [unit-economics](../../_shared/unit-economics.md)) & CPA < $20 → CBO scale + duplicate T2 **+ ghi [`winner-registry.json`](../../_shared/winner-registry.json)** (trigger SOP-PRD-005 nhân winner) |
| **Creative refresh** | frequency > 2.5 hoặc CTR giảm > 30% → new creative |
| **CAPI gate** | EMQ < 6 / dedup lỗi → HOLD scale tới khi fix |
| **BM anti-ban** | test ở T3, scale ở T2; account bị flag → failover T4 |

## 3. Budget & approval
- AI tự quyết scale/kill **trong** khung ngưỡng + budget cap đã duyệt.
- Vượt cap, discount ăn margin → **escalate OPC + 05-finance** trước khi hành động.

## 4. Escalation Matrix
| Trigger | Escalate tới |
|---------|-------------|
| BM/account bị ban | OPC (ngay) |
| Vượt budget cap | OPC + 05-finance |
| Off-track O1 (ROAS/revenue) | OPC |
| Meta policy / IP breed | 05-compliance |
| GDPR request / spam cap | 05-compliance |
| Số liệu lệch | 05-finance |

## 5. Community/Organic rule
Tôn trọng rule từng group (no spam link), consent khi dùng UGC, brand voice nhất quán.

> Liên quan: [`_knowledge`](../_knowledge/README.md) · [Quality](../quality_grw-001_quality-standards_v1.0_2026-06-23.md) · [KRI](../kri_grw-001_key-result-indicators_v1.0_2026-06-23.md)
