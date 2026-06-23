# SOP-MER-006 — Promote Theo Đợt (Batch Promote)

**Dept:** 02-merchandising (`mer`) · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible:** OPC (điều phối) · **Support AI:** `vibe-opc-pod-merch-catalog-sync` + `vibe-opc-pod-merch-product-page`

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | Live products đã QC (MER-004); candidate niche/SP từ phòng 01; kết quả ROAS/CPA đợt trước từ Growth |
| **Control (C)** | Chọn 5–10 SP/đợt; pricing floor & GPSR đã pass; ngân sách test ads; tiêu chí winner ROAS≥2.5 / CPA<$20 |
| **Output (O)** | Batch promote package (5–10 SP listing tối ưu) bàn giao Growth; quyết định scale winner / cut loser |
| **Mechanism (M)** | OPC + cả 2 AI worker + feedback từ 03-growth |
| **Upstream** | MER-004 (live product) |
| **Downstream** | 03-growth (FB Ads) → feedback loop về mer |

---

## 1. Tổng Quan

Chu trình **promote theo đợt** (SOP-MER-006, tham chiếu memory SOP-MER-006): mỗi đợt chọn **5–10 SP** → tối ưu listing → bàn giao Growth chạy ads → đọc kết quả → **scale winner / cut loser**. Chạy nhiều đợt song song để khám phá winner đa-niche. Đây là vòng lặp learn-fast của catalog ~3.200 SP.

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Catalog-Sync AI | Product-Page AI | 03-Growth |
|-----------|-----|-----------------|-----------------|-----------|
| Chọn 5–10 SP/đợt | **A/R** | C | C | I |
| Tối ưu listing (page/giá) | A | **R** `[AI WORKFORCE]` | **R** `[AI WORKFORCE]` | I |
| Bàn giao batch package | **A/R** | C | C | **C** |
| Đọc kết quả ROAS/CPA | **A/R** | I | I | **R** (cung cấp data) |
| Scale winner / cut loser | **A/R** | C | C | C |

`[AI WORKFORCE]` = `vibe-opc-pod-merch-catalog-sync` + `vibe-opc-pod-merch-product-page`.

## 3. Quy Trình

### Bước 1 — Chọn 5–10 SP vào đợt
| ICOM | Nội dung |
|------|----------|
| I | Live products + niche candidate + kết quả đợt trước |
| C | 5–10 SP/đợt, GPSR/margin đã pass |
| O | Batch list |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Chọn 5–10 SP theo demand/niche/mùa vụ | OPC |
| Confirm SP đã live + pass gate (MER-004) | AI |

### Bước 2 — Tối ưu listing
| ICOM | Nội dung |
|------|----------|
| I | Batch list |
| C | CRO checklist, margin band |
| O | Listing tối ưu (page + giá + bundle) |
| M | cả 2 AI worker |

| Hành động | Ai |
|-----------|-----|
| Refine product page copy + social proof + upsell | Product-Page AI `[AI WORKFORCE]` |
| Tinh chỉnh giá/compare-at/bundle trong band | Catalog-Sync AI `[AI WORKFORCE]` |

### Bước 3 — Bàn giao Growth
| ICOM | Nội dung |
|------|----------|
| I | Listing tối ưu |
| C | Batch package schema |
| O | Batch promote package → 03-growth |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Đóng gói: SP link, USP, audience hint, asset | AI |
| Bàn giao Growth chạy FB Ads (SOP-GRW-002) | OPC |

### Bước 4 — Đọc kết quả
| ICOM | Nội dung |
|------|----------|
| I | ROAS/CPA từ Growth |
| C | Winner ROAS≥2.5 / CPA<$20 |
| O | Phân loại winner/loser |
| M | OPC + Growth data |

| Hành động | Ai |
|-----------|-----|
| Thu ROAS/CPA per SP sau 3–5 ngày ads | OPC (data Growth) |
| Phân loại winner / borderline / loser | OPC |

### Bước 5 — Scale winner / Cut loser
| ICOM | Nội dung |
|------|----------|
| I | Phân loại |
| C | Tiêu chí scale/cut |
| O | Quyết định + đợt tiếp theo |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Winner → giữ live, đề xuất Growth scale +ngân sách, mở variant/niche lân cận | OPC |
| Loser → cut ads, ẩn/archive hoặc tối ưu lại 1 vòng | OPC |
| Ghi batch log → feed vào đợt sau | AI |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| Winner ROAS≥3 | Scale mạnh + nhân design lân cận (báo phòng 01) |
| Borderline (ROAS 2–2.5) | Tối ưu listing/creative 1 vòng rồi test lại |
| Loser ROAS<2 | Cut, archive |
| Cả đợt loser | Review niche selection với phòng 01 |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| Batch size | 5–10 SP/đợt | count |
| Batch SLA (cleared→ads-ready) | ≤ 5 ngày | timestamp log |
| Decision SLA (đọc kết quả→scale/cut) | ≤ 48h | log |
| Batch winner rate | ≥ 20% SP/đợt | ROAS feedback |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Đốt ads vào loser | Cut sớm theo tiêu chí ROAS |
| Đợt quá lớn khó đọc tín hiệu | Giới hạn 5–10 SP |
| Quên scale winner | Decision SLA 48h |
| Lặp lại niche kém | Feed kết quả về phòng 01 |

## 6. Tài Nguyên & Links

- Template: `promote-batch/template/`
- Upstream: [SOP-MER-004](../../sync-catalog/template/sop_mer-004_catalog-sync-qc_v1.0_2026-06-23.md)
- Downstream: phòng 03-growth (SOP-GRW-002 FB Ads)
- Memory: SOP-MER-006 "Promote theo đợt" (chọn 5–10 SP → tối ưu → ads → scale winner)
- Rules: [`_rules/README.md`](../../_rules/README.md)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo SOP promote theo đợt |
