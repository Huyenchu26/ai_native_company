# _workflow — 05-Backoffice

6 SOP + dependency. Backoffice là L3 Support: nhận data từ tất cả phòng, trả gate clearance + tài chính + workforce health.

---

## 6 SOP
| SOP | Tên | Folder | Responsible |
|---|---|---|---|
| BCK-001 | Bookkeeping & Fee Reconciliation | keep-books | finance AI |
| BCK-002 | Profit-per-SKU, ROAS/CPA & P&L | track-profit | finance AI |
| BCK-003 | VAT OSS/IOSS + US tax note | file-vat | finance AI |
| BCK-004 | GPSR Compliance `[GATE]` | clear-gpsr | compliance AI |
| BCK-005 | GDPR (RoPA/DSAR/breach) | manage-gdpr | compliance AI |
| BCK-006 | AI Workforce Ops/HR | manage-workforce | ops-hr AI |

## Dependency (DAG)
```
[Tất cả phòng] --cost/fee/order--> BCK-001 Bookkeeping
                                        |
                                        v
                                   BCK-002 Profit/ROAS --profit-per-SKU--> Merch (kill/scale), Growth (ROAS)
                                        |
                                   BCK-003 VAT (dùng order EU + ledger) --> tờ khai draft --> Owner nộp

[Merch SP chờ EU publish] --> BCK-004 GPSR [GATE] --PASS--> Merch publish EU
                                                  --FAIL--> block
[CX DSAR / incident] -------> BCK-005 GDPR --> DSAR/breach log

[Run log 12 worker] --------> BCK-006 Workforce --> roster/report/capacity --cost--> BCK-001
```

## Thứ tự thực thi
1. **Hằng ngày:** BCK-004 GPSR (per SP publish), BCK-005 GDPR (per request/incident), BCK-006 uptime check.
2. **Hằng tuần:** BCK-001 reconciliation, BCK-006 weekly report + capacity.
3. **Hằng tháng:** BCK-001 close → BCK-002 P&L + CEO brief.
4. **Theo kỳ:** BCK-003 VAT (IOSS tháng / OSS quý).

## Gate trong workflow
- BCK-004 GPSR PASS là điều kiện chặn cho Merch publish EU (hard dependency).
- BCK-005 breach 72h là timer cứng.
- BCK-002 feed quyết định scale/kill về Merch (SOP-MER-006) & Growth (SOP-GRW-002).

## Handoff
Mọi output → `output/`; cost feed ngược BCK-001; brief & clearance → Owner. Schema-aware handoff cho AI Worker (evidence + confidence_score).
