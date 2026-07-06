# Trigger Validation — vibe-eu-opc-bck-ops-hr

Kiểm tra skill kích hoạt đúng (SHOULD) và KHÔNG kích hoạt sai (SHOULD NOT — bẫy finance & compliance).

## SHOULD trigger (5)

| # | Input người dùng | Lý do |
|---|------------------|-------|
| 1 | "Skill nào tuần này lỗi nhiều / reject cao?" | review-quality → reject rate per worker |
| 2 | "Mấy con AI worker có chạy đủ uptime không?" | monitor-uptime → uptime ≥99% |
| 3 | "Batch promote dồn quá, có cần thêm worker không?" | capacity-plan → status STRAINED/OVER |
| 4 | "Làm weekly report cho đội AI workforce." | weekly-report |
| 5 | "Review hiệu suất các skill, ai degrade thì escalate." | performance review + escalation |

## SHOULD NOT trigger (5) — bẫy

| # | Input người dùng | Route đúng | Vì sao KHÔNG phải ops-hr |
|---|------------------|-----------|--------------------------|
| 1 | "Tính ROAS / lên P&L / khai VAT tháng này." | **vibe-eu-opc-bck-finance** | Tài chính/hạch toán — ops-hr chỉ FEED cost token, không làm sổ |
| 2 | "Chi phí token đội AI đang cao, ghi vào ledger và đối soát fee." | **vibe-eu-opc-bck-finance** | Bookkeeping/reconciliation là việc finance (ops-hr chỉ tổng hợp + cảnh báo) |
| 3 | "Check GPSR / Responsible Person cho đơn EU." | **vibe-eu-opc-bck-compliance** | GPSR clearance là compliance |
| 4 | "Đơn này có dính GDPR data request / trademark breed không?" | **vibe-eu-opc-bck-compliance** | GDPR/IP-TM là compliance |
| 5 | "Điều phối cả Backoffice tuần này, phân việc các phòng." | **vibe-eu-opc-bck-orchestrator** | Điều phối toàn dept; ops-hr chỉ bàn giao report lên |

## Ghi chú bẫy
- **Bẫy finance:** "cost token cao" dễ nhầm sang ops-hr, nhưng nếu yêu cầu là **hạch toán/ledger/VAT/ROAS/P&L** → finance. ops-hr chỉ kích hoạt khi là **theo dõi/feed cost của worker**.
- **Bẫy compliance:** mọi việc GPSR/GDPR/IP-TM/Meta Ad Policy → compliance, KHÔNG phải ops-hr.
