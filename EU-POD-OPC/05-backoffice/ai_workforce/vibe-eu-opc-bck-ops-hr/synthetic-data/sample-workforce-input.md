# Sample Workforce Input — 1 tuần (DAKOfits)

Dữ liệu mẫu cho 1 tuần (`period: 2026-W25`, 2026-06-16..2026-06-22) để chạy smoke-test / weekly-review-prompt. Số liệu giả lập, vài skill đại diện cho roster.

> Nhắc: `total_workers` phải đếm THẬT từ [workforce-map](../../../../_ai-workforce/workforce-map_v1.0_2026-06-23.md) + folder `EU-OPC/**/ai_workforce/*/SKILL.md`. KHÔNG hard-code "12". Bảng dưới chỉ là sample cho vài worker.

## 1. Run log → uptime (cron/trigger)

| Worker | Layer | Scheduled runs | Success | Fail | Downtime (h) | Uptime % |
|--------|-------|----------------|---------|------|--------------|----------|
| vibe-eu-opc-prd-niche-research | eu-opc | 42 | 42 | 0 | 0.0 | 100.0 |
| vibe-eu-opc-prd-design | eu-opc | 56 | 55 | 1 | 1.2 | 99.3 |
| vibe-eu-opc-mer-catalog | eu-opc | 70 | 69 | 1 | 0.8 | 99.5 |
| vibe-eu-opc-grw-fb-ads | eu-opc | 98 | 90 | 8 | 9.5 | **94.3** ⚠ |
| vibe-eu-opc-ful-order-ops | eu-opc | 168 | 167 | 1 | 0.5 | 99.7 |
| vibe-opc-pod-fulfillment-cx | legacy | 84 | 83 | 1 | 1.0 | 99.0 |
| vibe-eu-opc-bck-finance | eu-opc | 14 | 14 | 0 | 0.0 | 100.0 |

→ **grw-fb-ads uptime 94.3% < 95%** → escalate Owner, root cause (nghi credential CAPI / cron BM rotate).

## 2. Human-review reject log → reject rate

| Worker | Output total | Rejected | Reject rate |
|--------|--------------|----------|-------------|
| vibe-eu-opc-prd-design | 48 | 3 | 6.3% |
| vibe-eu-opc-mer-catalog | 60 | 4 | 6.7% |
| vibe-eu-opc-mer-product-page | 35 | 5 | **14.3%** ⚠ |
| vibe-eu-opc-grw-creative | 40 | 3 | 7.5% |
| vibe-eu-opc-ful-cx | 120 | 6 | 5.0% |

→ **mer-product-page reject 14.3% > 10%** → flag skill-update/retrain + tăng human-review tạm thời.

## 3. Token/API cost (USD) — feed finance

| Worker | Cost tuần này | Cost tuần trước |
|--------|---------------|-----------------|
| vibe-eu-opc-prd-niche-research | 18.40 | 17.90 |
| vibe-eu-opc-prd-design | 25.10 | 24.00 |
| vibe-eu-opc-mer-catalog | 12.30 | 12.10 |
| vibe-eu-opc-grw-fb-ads | 31.80 | 24.50 |
| vibe-eu-opc-grw-creative | 22.60 | 21.90 |
| vibe-eu-opc-ful-order-ops | 9.70 | 9.50 |
| (các worker khác) | 41.20 | 39.80 |
| **TOTAL** | **161.10** | **149.70** |

→ delta = +7.6% tổng (dưới 20%, KHÔNG spike toàn cục). Nhưng **grw-fb-ads +29.8%** (31.80 vs 24.50) → cost-alert cục bộ cho finance, soi liên quan tới 8 fail run.

## 4. Workload / capacity

- Tuần này: 2 đợt promote (SOP-MER-006), tổng **16 SP** (1 đợt 9 SP + 1 đợt 7 SP).
- Roster active xử lý kịp, nhưng grw-fb-ads quá tải (fail + cost spike) khi 2 batch chồng.
- → Đề xuất status: **STRAINED** (grw gần trần) → cron-reschedule tách 2 batch + theo dõi tuần sau; chưa cần thêm worker.

## 5. SOP version
- Không SOP nào bump version trong tuần → không cần skill-update do SOP.

## Kỳ vọng output (tóm tắt)
- `total_workers`: đếm thật từ map + folder (KHÔNG ghi cứng).
- `uptime_pct` roster ≈ 98.7%; **need_review = true** (vì grw-fb-ads <95% + product-page reject >10%).
- `avg_reject_rate` ≈ 0.078 nhưng có 1 worker vi phạm → action retrain.
- `cost_summary.delta_vs_prev_pct` ≈ +7.6%; action `cost-alert` cho grw-fb-ads.
- `capacity_status`: STRAINED, action `cron-reschedule`.
- actions[]: escalate (grw-fb-ads uptime), retrain/skill-update (mer-product-page), cost-alert (grw-fb-ads), cron-reschedule.
