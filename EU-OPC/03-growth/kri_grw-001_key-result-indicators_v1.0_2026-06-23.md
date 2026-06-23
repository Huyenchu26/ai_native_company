# KRI — 03-growth · Key Result Indicators (Early-Warning)

**Dept:** grw · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Mục đích:** KRI = chỉ báo **rủi ro sớm** (leading), cảnh báo TRƯỚC khi KPI (lagging) hỏng. Owner: `vibe-opc-pod-growth-fb-ads` (SOP-GRW-004).

---

| # | KRI | Đo gì (rủi ro) | Ngưỡng cảnh báo (Amber) | Ngưỡng nguy (Red) | Hành động |
|---|-----|----------------|-------------------------|-------------------|-----------|
| 1 | `roas_3day_trend` | ROAS đang trượt | < 2.5 (3 ngày) | < 1.8 (3 ngày) | optimize → kill loser |
| 2 | `cpa_trend` | CPA leo thang | > $18 | > $20 | refresh creative / cắt audience |
| 3 | `ad_frequency` | Ad fatigue | > 2.0 | > 2.5 | refresh creative (SOP-GRW-005) |
| 4 | `ctr_drop` | Creative chết | giảm > 20% | giảm > 30% | new hook variant |
| 5 | `capi_emq` | Mất signal | < 6.5 | < 6.0 | HOLD scale, fix CAPI/dedup |
| 6 | `bm_account_health` | Nguy cơ ban | 1 account restricted | account chính/scale bị flag | failover T4, escalate OPC |
| 7 | `email_deliverability` | Inbox placement | < 98% | < 95% | warm-up, list hygiene, fix DKIM |
| 8 | `spam_complaint_rate` | Reputation email | > 0.07% | > 0.1% | pause flow, làm sạch list |
| 9 | `budget_burn_vs_revenue` | Đốt tiền | spend ≥ 1.5× CPA target, 0 conv | spend ≥ 2× target, 0 conv | KILL ngay |
| 10 | `policy_flag_rate` | Rủi ro chính sách | 1 creative flagged | account-level warning | dừng creative, 05-compliance |

**Cadence:** daily snapshot (SOP-GRW-004); Red → alert OPC < 24h.
**Liên kết KPI:** KRI 1–2,9 → ROAS/CPA · KRI 3–4 → CTR/hook · KRI 5 → CAPI · KRI 6,10 → BM ban · KRI 7–8 → email deliverability.
