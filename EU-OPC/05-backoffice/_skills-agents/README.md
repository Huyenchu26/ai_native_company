# _skills-agents — 05-Backoffice

3 AI Worker phụ trách 6 SOP. Mỗi worker là một Claude Skill chuyên biệt (`vibe-opc-pod-backoffice-*`).

---

## 3 AI Worker
| Worker | Skill | SOP (Responsible) | Output |
|---|---|---|---|
| Finance AI | `vibe-opc-pod-backoffice-finance` | BCK-001, BCK-002, BCK-003 | Ledger, profit-per-SKU, P&L, VAT draft, CEO brief |
| Compliance AI | `vibe-opc-pod-backoffice-compliance` | BCK-004, BCK-005 | GPSR clearance log, IP/TM, nhãn an toàn, RoPA, breach/DSAR log |
| Ops-HR AI | `vibe-opc-pod-backoffice-ops-hr` | BCK-006 | Roster, performance review, weekly report, capacity plan |

## Skill ↔ SOP Matrix
| SOP | finance | compliance | ops-hr |
|---|:---:|:---:|:---:|
| BCK-001 Bookkeeping | **R** | | C(cost) |
| BCK-002 Profit/ROAS | **R** | | |
| BCK-003 VAT | **R** | C | |
| BCK-004 GPSR `[GATE]` | | **R** | |
| BCK-005 GDPR | C | **R** | |
| BCK-006 Workforce | C(cost) | | **R** |

R = Responsible · C = Consulted

## Coverage
- **6/6 SOP** có Responsible worker → 100% coverage, không gap.
- Finance: 3 SOP (load cao nhất — daily/weekly/monthly + per-period VAT).
- Compliance: 2 SOP nhưng cả 2 là **gate cứng legal** (cao rủi ro).
- Ops-HR: 1 SOP nhưng giám sát **toàn bộ 12 worker** (cross-dept).

## Capability & Skill Matrix
| Capability | finance | compliance | ops-hr |
|---|:---:|:---:|:---:|
| Double-entry bookkeeping | ✓ | | |
| Fee reconciliation | ✓ | | |
| Profit/ROAS/CPA model | ✓ | | |
| FX USD→VND | ✓ | | |
| VAT OSS/IOSS calc | ✓ | ✓(consult) | |
| GPSR clearance + RP | | ✓ | |
| IP/TM breed check | | ✓ | |
| GDPR RoPA/DSAR/breach | | ✓ | |
| Meta Ad Policy review | | ✓ | |
| AI worker monitoring | | | ✓ |
| Capacity planning | | | ✓ |

## Human-in-the-loop
- Owner = Accountable: ký mọi gate legal (GPSR FAIL exception, breach notify), khóa sổ, nộp VAT.
- AI Worker draft → `processing/human-review/` → Owner duyệt → `output/`.

## Skill versioning
Skill version pinned theo SOP version (ops-hr quản, SOP-BCK-006). SOP đổi → bump skill + cập nhật `_knowledge`.
