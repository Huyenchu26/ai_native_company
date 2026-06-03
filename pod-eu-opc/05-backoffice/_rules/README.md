# _rules — Backoffice

> AI KHÔNG ĐƯỢC làm gì: policies, quality gates, escalation. Backoffice là **tuyến phòng thủ compliance cuối cùng** của OPC.

## Hard rules (không ngoại lệ)
1. **KHÔNG publish listing vào EU** nếu chưa có GPSR clearance + Responsible Person hợp lệ (SOP-BCK-004).
2. **KHÔNG nộp tờ khai VAT** khi chênh lệch VAT khai vs sổ ≠ €0 (SOP-BCK-002).
3. **KHÔNG gửi email marketing** cho người chưa opt-in (SOP-BCK-005).
4. **KHÔNG tích hợp tool mới** xử lý dữ liệu khách khi chưa có DPA (SOP-BCK-005).
5. **KHÔNG commit secrets** (API key, RP/tax info nhạy cảm) vào git — giữ ngoài repo.

## Quality Standards (SLI/SLO/SLA)
→ Xem chi tiết: [quality_bck-001_quality-standards_v1.0_2026-06-03.md](../quality_bck-001_quality-standards_v1.0_2026-06-03.md). Tất cả SLO compliance = 100% (error budget = 0).

## Escalation
- Quality gate thường fail 3x → escalate Founder + Incident Report (`../../_quality/`).
- **Rủi ro pháp lý (IP/GPSR/GDPR/VAT) → dừng ngay, escalate Founder, KHÔNG chờ đủ 3 loop.**
- GDPR breach → kích playbook 72h ngay khi phát hiện.

## Incident History
| INC | Date | SOP | Root Cause | Prevention |
|---|---|---|---|---|
