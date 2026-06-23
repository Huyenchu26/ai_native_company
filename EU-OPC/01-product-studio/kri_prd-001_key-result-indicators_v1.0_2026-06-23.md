# KRI — 01-Product Studio · Q3 2026

**Ngày:** 2026-06-23 · **Dept:** prd

> KRI = chỉ số cảnh báo sớm (leading/lagging) gắn với OKR. Có ngưỡng cảnh báo (warning) và ngưỡng nguy hiểm (critical) để escalate.

| # | KRI | Loại | Healthy | Warning | Critical | Gắn OKR/KR | Hành động khi Critical |
|---|-----|------|---------|---------|----------|-----------|------------------------|
| 1 | niche_validated_weekly | Leading | ≥ 3 | 2 | < 2 | O.PRD1-KR1 | Tăng source AdSpy, mở rộng niche pool |
| 2 | design_ready_weekly | Leading | ≥ 20 | 12–19 | < 12 | O.PRD1-KR2 | Ưu tiên reuse design base, kiểm capacity AI |
| 3 | ip_clearance_rate | Lagging | 100% | 99–99.9% | < 99% | O.PRD1-KR3 | Dừng handoff, audit clearance log |
| 4 | aop360_pass_rate | Leading | ≥ 98% | 95–98% | < 95% | Quality PRD-003 | Review template seamless tile |
| 5 | design_turnaround_h | Leading | ≤ 24h | 24–36h | > 36h | Quality PRD-003 | Giảm queue, ưu tiên seasonal deadline |
| 6 | seasonal_deadline_hit | Lagging | ≥ 95% | 85–95% | < 85% | O.PRD1-KR2 | Tăng buffer lead-time PRD-002 |
| 7 | tm_takedown_rate | Lagging | ≤ 1% | 1–3% | > 3% | O.PRD1-KR3 | RCA clearance, siết rubric conservative |

**Escalation:** Critical bất kỳ KRI → OPC review trong 24h. KRI3 & KRI7 (IP) là tối cao — chạm Critical thì **dừng listing pipeline** cho tới khi RCA xong.

**Causal chain:** KRI1/2 → đủ đầu vào catalog → Company revenue (O1). KRI3/7 → tránh ban/takedown → bảo vệ O2 + tài sản store.
