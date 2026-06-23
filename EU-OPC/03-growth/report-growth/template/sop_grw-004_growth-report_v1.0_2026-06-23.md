# SOP-GRW-004 — Growth Report (KPI/KRI) `[AI WORKFORCE]`

**Phòng:** 03-growth (grw) · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** 03-growth · **Responsible AI Worker:** `vibe-opc-pod-growth-fb-ads`
**Folder:** `report-growth/`

> GATE: Số liệu phải reconcile với cost data của 05-backoffice (single source of truth) trước khi báo cáo.

---

## 0. IPO

| Thành phần | Chi tiết |
|-----------|----------|
| **Input** | Campaign data (SOP-GRW-002); email metrics (003); organic metrics (001); cost data (05-finance); đơn hàng (04) |
| **Process** | Gom số liệu → reconcile cost → tính KPI/KRI → phát hiện trend/anomaly → khuyến nghị → báo cáo |
| **Control** | Data reconciliation, threshold alert (ROAS/CPA), cadence |
| **Output** | Growth report (daily snapshot + weekly) → OPC; alert → các SOP liên quan |
| **Mechanism** | Meta Ads Manager export, Klaviyo, ShopBase, vibe-opc-pod-growth-fb-ads |

---

## 1. Tổng quan

Growth report biến raw metrics thành **quyết định**: scale gì, kill gì, refresh creative gì, đang on/off-track với O1. Cadence **daily** (snapshot vận hành) + **weekly** (review trend + khuyến nghị). Đây là vòng feedback đóng cho cả phòng 03.

---

## 2. RACI + AI Roles

| Hoạt động | R | A | C | I |
|----------|---|---|---|---|
| Gom & reconcile data | `fb-ads` (AI) | OPC | 05-finance | — |
| Tính KPI/KRI | `fb-ads` (AI) | OPC | — | — |
| Khuyến nghị scale/kill | `fb-ads` (AI) | OPC | `fb-creative`, `marketing` | — |
| Báo cáo OPC | `fb-ads` (AI) | OPC | — | 00-company |

**AI Role:** `vibe-opc-pod-growth-fb-ads` tổng hợp cross-channel, phát alert khi vượt ngưỡng, đề xuất hành động cho 3 worker.

---

## 3. Quy trình (ICOM, 4 bước)

### Bước 1 — Gom số liệu cross-channel `[Input]`
- FB Ads (spend, ROAS, CPA, CTR, frequency, EMQ); email (deliverability, revenue-per-email); organic (engagement, referral).

### Bước 2 — Reconcile cost `[Control]`
- Đối chiếu ad spend với 05-finance ledger (chống lệch số). 05 là source of truth cho cost/revenue tài chính.

### Bước 3 — Tính KPI/KRI & phát hiện trend `[Process]`
- KPI: **Blended/True ROAS**, CPA, CTR, revenue do ads, repeat-rate. KRI (early-warning): xem file KRI.
- **Attribution window khai báo bắt buộc: 7-day click / 1-day view** (cố định công ty — [unit-economics](../../../_shared/unit-economics.md) §1) cho mọi phần revenue gán ads, để báo cáo đọc nhất quán giữa kỳ.
- **Tử số Blended ROAS = tổng order ShopBase thực (net-of-refund), KHÔNG phải pixel-attributed revenue của Ads Manager.** Mẫu = tổng ad spend (mọi BM + fee). Platform ROAS chỉ dùng tham chiếu real-time, ghi rõ khi nêu (cao hơn thực 20–40%).
- Phát hiện anomaly (ROAS sụt, CPA tăng, frequency cao, EMQ rớt).

### Bước 4 — Khuyến nghị & báo cáo `[Output]`
- Daily snapshot: top winner/loser, alert. Weekly: trend + khuyến nghị scale/kill/refresh + on/off-track O1.
- Gửi OPC; trigger hành động về SOP-GRW-002/003/005.

---

## 4. Phân nhánh

| Điều kiện | Hành động |
|----------|-----------|
| Số liệu lệch 05-finance | **HOLD report**, reconcile lại |
| Blended ROAS < **break-even ROAS của SKU** (~2.0–2.75 tùy SKU; US ~2.75, EU ~5.3 — xem [unit-economics](../../../_shared/unit-economics.md) §2,§4) | alert OPC + khuyến nghị **kill loser theo từng SKU** (neo break-even per-SKU, KHÔNG 1 ngưỡng cứng) |
| Blended ROAS ≥ break-even nhưng < **target-profit (~2.5)** | còn lãi mỏng — giữ, đề xuất optimize creative/giá để đạt target margin |
| CPA > $20 trend tăng | alert → SOP-GRW-002 optimize |
| KRI vượt ngưỡng cảnh báo | escalate sớm (xem file KRI) |
| Off-track O1 | flag OPC để điều chỉnh budget/đợt promote |

---

## 5. Checklist + Quality Gate (SLI/SLO + Prevention)

- [ ] Data reconcile với 05-finance
- [ ] KPI/KRI tính đủ
- [ ] Alert ngưỡng bật
- [ ] Khuyến nghị actionable

| SLI | SLO | Error budget |
|-----|-----|--------------|
| Report đúng cadence (daily/weekly) | 100% | ≤ 1 trễ/tháng |
| Data reconciliation accuracy | sai lệch < 2% vs 05 | hard cap |
| Alert latency (ngưỡng vượt → báo) | < 24h | — |
| KPI coverage | đủ ROAS/CPA/CTR/revenue/KRI | 0 thiếu |

**Prevention:** reconcile bắt buộc trước báo cáo; ngưỡng alert tự động; template report cố định để không sót KPI.

---

## 6. Tài nguyên + Links
- Folder: `report-growth/`
- KPI: [`../../kpi_grw-001_growth-kpis_v1.0_2026-06-23.md`](../../kpi_grw-001_growth-kpis_v1.0_2026-06-23.md)
- KRI: [`../../kri_grw-001_key-result-indicators_v1.0_2026-06-23.md`](../../kri_grw-001_key-result-indicators_v1.0_2026-06-23.md)
- **Định nghĩa chuẩn:** [unit-economics](../../../_shared/unit-economics.md) (Platform vs Blended ROAS, break-even per-SKU, attribution 7d-click/1d-view, FX)
- Cost source: 05-backoffice/finance · Company O1: [00-company OKR](../../../00-company/okr_company-001_company-okr_v1.0_2026-06-23.md)

---

## 7. Lịch sử
| Version | Ngày | Thay đổi | Người |
|---------|------|----------|-------|
| v1.0 | 2026-06-23 | Khởi tạo SOP growth report (KPI/KRI, reconcile) | Company Architect |
| v1.1 | 2026-06-23 | Khai báo attribution 7d-click/1d-view; tử số blended = order ShopBase thực (không pixel-attributed); kill neo break-even per-SKU, tách target-profit 2.5; trỏ unit-economics | 03-growth |
