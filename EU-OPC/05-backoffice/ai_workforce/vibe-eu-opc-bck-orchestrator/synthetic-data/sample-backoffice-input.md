# Synthetic Data — Sample Backoffice Input (1 kỳ chốt sổ)

Dữ liệu mẫu 1 kỳ để orchestrator điều phối CEO brief. Dữ liệu giả lập, không phải số liệu thật.

---

## Period metadata
- **period:** `2026-06`
- **prepared_for:** Owner
- **ngày:** 2026-06-23
- **handoff từ:** tất cả phòng L2 (cost/fee/order/ad-spend) + run log 3 AI Worker
- **FX source:** Vietcombank USD→VND 2026-06-23 = 25.450 (có nguồn, R6)

## A. Finance input (→ vibe-eu-opc-bck-finance, BCK-001/002/003)
| Mục | Giá trị |
|-----|---------|
| Revenue (USD) | $32.400 |
| Ad spend (Meta) | $14.800 |
| COGS (Printify + fee) | $11.900 |
| Net profit (USD) | $5.700 |
| Net margin | 17.6% ← **dưới target ≥20%** |
| Blended ROAS | 2.19 |
| Revenue (VND, FX 25.450) | ~825 triệu |
| VAT OSS deadline kỳ | 2026-07-20 (due) |
| Fee discrepancy Printify | 2.4% ← **> 2%, escalate** |

Top SKU (profit): US-BULLDOG-001 +$1.450 (SCALE) · EU-CORGI-003 −$320 (KILL) · US-YOGA-CAT-005 +$610 (KEEP).

## B. Compliance input (→ vibe-eu-opc-bck-compliance, BCK-004/005)
| Mục | Trạng thái |
|-----|-----------|
| SP chờ EU publish | 2 SP (EU-DACHS-006, EU-HUSKY-009) — **GPSR clearance: pending** ← gate #1 fail |
| IP/TM breed check | Husky OK; Dachshund OK |
| Meta Ad Policy (creative batch W26) | pass |
| GDPR breach | 1 breach phát hiện 2026-06-22T09:00:00Z — **status: open** ← gate #3, deadline 72h = 2026-06-25T09:00:00Z |
| DSAR mở | 1 (erasure request, in progress) |

## C. Workforce input (→ vibe-eu-opc-bck-ops-hr, BCK-006)
| Mục | Giá trị |
|-----|---------|
| Worker count | 3 (finance, compliance, ops-hr) |
| Uptime | 99.3% ← đạt ≥99% |
| Cost (compute) | $180 |
| Quality flag | amber (compliance worker backlog clearance) |
| Capacity note | clearance queue tăng do batch SP mới |

## Kỳ vọng điều phối (để đối chiếu test)
- **GPSR gate FAIL** (2 SP pending) ⇒ `compliance_status=BLOCKED`, no publish EU, trả 05-compliance, escalate Owner ngay.
- **GDPR breach open** ⇒ timer 72h (deadline 2026-06-25T09:00:00Z), Owner = notify authority, need_review=true.
- **VAT due 2026-07-20** ⇒ finance draft tờ khai, Owner nộp on-time 100%.
- **Net margin 17.6% < 20%** + **fee discrepancy 2.4% > 2%** ⇒ escalate Owner qua finance; đề xuất KILL EU-CORGI-003, SCALE US-BULLDOG-001.
- **FX có nguồn** ⇒ revenue_vnd điền được (R6 OK). Nếu thiếu nguồn ⇒ để trống + need_review.
- Tổng: `compliance_status=BLOCKED`, `need_review=true` (gate fail + breach + margin dưới target).
