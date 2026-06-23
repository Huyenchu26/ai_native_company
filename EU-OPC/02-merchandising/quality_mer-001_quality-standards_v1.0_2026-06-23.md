# Quality Standards: Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0

> Mỗi SOP có SLI (đo được) · SLO (mục tiêu) · SLA (cam kết thời gian) · Error Budget · Measurement. Schema v2.0: target mang `confidence` + `need_review`.

---

## SOP-MER-001 — Product Page + Upsell + GPSR label

| Field | Giá trị |
|-------|---------|
| **SLI** | (a) GPSR label present rate (EU); (b) Mobile CRO elements completeness (/12); (c) Upsell block present |
| **SLO** | (a) **= 100%**; (b) **≥ 95%**; (c) = 100% PDP |
| **SLA** | Page draft ≤ 4h sau khi nhận blueprint + GPSR clearance |
| **Error Budget** | GPSR: **0%** (zero-tolerance, gate cứng); CRO: ≤ 5% PDP dưới chuẩn/tháng |
| **Measurement** | Auto-check label string trên PDP EU; checklist CRO 12 elements; OPC review |
| confidence / need_review | 0.8 / false |

## SOP-MER-002 — Setup Printify/PrintBase

| Field | Giá trị |
|-------|---------|
| **SLI** | Provider + variant set (XS–3XL/color) setup correctness |
| **SLO** | **≥ 98%** SP setup đúng |
| **SLA** | Blueprint ≤ 8h sau khi nhận cleared design |
| **Error Budget** | ≤ 2% SP cần re-setup |
| **Measurement** | So variant list vs blueprint chuẩn; mockup render check |
| confidence / need_review | 0.7 / false |

## SOP-MER-003 — Variant Pricing

| Field | Giá trị |
|-------|---------|
| **SLI** | Gross margin theo variant |
| **SLO** | **≥ 45%** (mục tiêu band 45–55%) — 100% SP |
| **SLA** | Pricing ≤ 2h sau setup |
| **Error Budget** | **0%** SP dưới 45% được publish (pricing floor cứng) |
| **Measurement** | (giá−cost)/giá per variant; floor check trước publish |
| confidence / need_review | 0.75 / false |

## SOP-MER-004 — Catalog Sync + QC

| Field | Giá trị |
|-------|---------|
| **SLI** | Catalog sync accuracy (field khớp ShopBase ↔ provider) |
| **SLO** | **≥ 99%** |
| **SLA** | Sync + QC ≤ 4h sau khi page approve |
| **Error Budget** | ≤ 1% field lệch; ≤ 2% listing defect rate |
| **Measurement** | Diff field (giá, variant, ảnh, stock); QC spot-check |
| confidence / need_review | 0.7 / false |

## SOP-MER-006 — Promote theo đợt

| Field | Giá trị |
|-------|---------|
| **SLI** | (a) Batch SLA cleared→ads-ready; (b) Batch winner rate (ROAS≥2.5) |
| **SLO** | (a) **≤ 5 ngày/đợt**; (b) **≥ 20%** SP/đợt |
| **SLA** | Đọc kết quả + quyết scale/cut ≤ 48h sau khi Growth báo |
| **Error Budget** | ≤ 1 đợt/tháng trượt SLA 5 ngày |
| **Measurement** | Batch log timestamp; ROAS feedback từ Growth |
| confidence / need_review | 0.6 / false |

---

## Quality Gate tổng hợp (chặn publish)

| Gate | Điều kiện PASS | Nếu FAIL |
|------|----------------|----------|
| GPSR (EU) | Label present = 100% + clearance log tồn tại | **No publish** |
| Pricing floor | Gross margin ≥ 45% | **No publish** |
| Catalog QC | Sync accuracy ≥ 99%, variant XS–3XL đủ | Re-sync |
| CRO | ≥ 95% elements, upsell present | Trả page |

## Escalation

| Vi phạm | Escalate đến |
|---------|--------------|
| GPSR label thiếu / clearance không có | Phòng 05-Backoffice (compliance) |
| Margin không đạt do cost provider | OPC quyết đổi provider |
| Design fail QC | Phòng 01-Product-Studio |
| Đợt promote toàn loser | OPC + Phòng 03-Growth |
