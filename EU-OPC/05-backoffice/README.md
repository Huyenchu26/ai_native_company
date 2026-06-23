# 05-Backoffice (bck) — Finance · Compliance · AI Workforce Ops

**Dept code:** bck · **Layer:** L3 Support · **Owner:** OPC (1 người) + 3 AI Worker · **Ngày:** 2026-06-23
**Vai trò:** Hỗ trợ tất cả phòng L2 (Product Studio, Merchandising, Growth, Fulfillment) bằng gate clearance + tài chính + sức khỏe workforce.

---

## Department IPO
| | |
|---|---|
| **Input** | Cost/fee/order data từ TẤT CẢ phòng, SP chờ EU publish, DSAR/breach, run log 12 AI Worker, VAT/tax data |
| **Process** | Bookkeeping → profit/ROAS → VAT → GPSR gate → GDPR → workforce ops |
| **Output** | Gate clearance (GPSR/IP-TM), ledger + P&L + CEO brief, tờ khai VAT, breach/DSAR log, workforce health report — phục vụ Owner |

## Value Chain Position — L3 Support
Backoffice là **Support Activity** (Porter): không trực tiếp tạo SP/traffic, mà bảo đảm công ty **đúng luật + có lãi + workforce khỏe**. Hai gate cứng chặn dòng giá trị L2: **GPSR** (chặn Merch publish EU) và **Meta Ad Policy / IP-TM** (chặn Growth ads, Product listing). Finance khép vòng feedback: profit-per-SKU → quyết định scale/kill của Merch & Growth.

## Process IPOs (mỗi SOP)
| SOP | Input | Output |
|---|---|---|
| BCK-001 Bookkeeping | Statements (ShopBase/Printify/Meta/gateway) | Ledger + recon log |
| BCK-002 Profit/ROAS | Ledger + ad-spend + COGS | Profit-per-SKU, P&L, CEO brief |
| BCK-003 VAT OSS/IOSS | Order EU + rate | Tờ khai VAT draft + US tax note |
| BCK-004 GPSR `[GATE]` | SP chờ EU publish + niche | Clearance log + nhãn an toàn + IP/TM |
| BCK-005 GDPR | DSAR/breach + data flow | RoPA, DSAR log, breach log |
| BCK-006 Workforce | Run log 12 worker | Roster, review, weekly report, capacity |

## RACI (department)
| SOP | R | A | C | I |
|---|---|---|---|---|
| BCK-001/002/003 | finance AI | Owner | compliance/ops-hr | tất cả phòng |
| BCK-004/005 | compliance AI | Owner | Merch/Product/CX | Growth |
| BCK-006 | ops-hr AI | Owner | finance + trưởng phòng | tất cả worker |

## KPI summary
GPSR clearance rate 100% · Bookkeeping accuracy ≥99.9% · VAT on-time 100% · Net margin ≥20% · Breach notify ≤72h · AI worker uptime ≥99%. → [KPI](./kpi_bck-001_backoffice-kpis_v1.0_2026-06-23.md) · [KRI](./kri_bck-001_key-result-indicators_v1.0_2026-06-23.md)

## OKR summary
Committed: GPSR 100% trước publish, net margin ≥20%, VAT on-time 100%, workforce uptime ≥99%. Stretch x10: zero-touch compliance + finance pipeline. → [OKR](./okr_bck-001_quarterly-okr_v1.0_2026-06-23.md). Align Company **O1** (lãi) + **O2** (đúng luật).

## Quality Standards summary
SLI/SLO/SLA mỗi SOP; compliance SLO = **100%** (gate cứng legal, error budget 0%); finance accuracy ≥99.9%. → [Quality](./quality_bck-001_quality-standards_v1.0_2026-06-23.md)

## AI Integration (SOP → AI Worker) — 3 worker, 6 SOP
| AI Worker | SOP phụ trách (Responsible) | Output chính |
|---|---|---|
| `vibe-opc-pod-backoffice-finance` | BCK-001, BCK-002, BCK-003 | Ledger, profit-per-SKU, P&L, VAT draft, CEO brief |
| `vibe-opc-pod-backoffice-compliance` | BCK-004, BCK-005 | GPSR clearance, IP/TM, RoPA, breach/DSAR log |
| `vibe-opc-pod-backoffice-ops-hr` | BCK-006 | Roster, performance review, weekly report, capacity plan |

## KWSR
[_knowledge](./_knowledge/README.md) · [_workflow](./_workflow/README.md) · [_skills-agents](./_skills-agents/README.md) · [_rules](./_rules/README.md)

## Charter
[charter_bck-department](./charter_bck-department_v1.0_2026-06-23.md)
