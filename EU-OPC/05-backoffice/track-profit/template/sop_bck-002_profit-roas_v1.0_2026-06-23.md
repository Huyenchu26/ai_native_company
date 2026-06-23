# SOP-BCK-002 — Profit-per-SKU, ROAS/CPA & P&L

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-finance` `[AI WORKFORCE]`

---

## 0. IPO
| | |
|---|---|
| **Input** | Ledger khóa (SOP-BCK-001), Ad-spend per campaign/SKU (Growth), COGS print/ship (Merch/Fulfillment), tỷ giá USD→VND |
| **Process** | Tính profit-per-SKU → ROAS/CPA → P&L → quy đổi VND → CEO brief vs target |
| **Output** | `profit-per-SKU` table, ROAS/CPA report, P&L tháng, CEO brief (so target 500tr/$20k) |

> **Định nghĩa chuẩn:** [unit-economics](../../../_shared/unit-economics.md) — mọi công thức ROAS / margin / profit-per-SKU ở SOP này PHẢI khớp file canonical đó.

## 1. Tổng quan
Biến số liệu kế toán thành quyết định: SKU nào lãi/lỗ, campaign nào dưới break-even ROAS, có đạt net margin ≥20% không. Đa niche ~3.200 SP → phân tích theo SKU và theo batch (SOP-MER-006). CPA = Ad-spend/đơn; profit-per-SKU tính ĐẦY ĐỦ (xem §1b). Quy đổi VND bằng tỷ giá khóa kỳ duy nhất (Vietcombank bán ra, cuối kỳ — ghi rõ nguồn + ngày).

## 1a. Platform ROAS vs Blended/True ROAS
| Loại | Định nghĩa | Nguồn | Dùng cho |
|---|---|---|---|
| **Platform ROAS** | Revenue Meta gán cho ads / Ad spend | Ads Manager (last-click + view-through) | Đọc real-time để kill/scale; cao hơn thực 20–40% |
| **Blended / True ROAS** | **Tổng** revenue thực (ShopBase, net-of-refund) / **Tổng** ad spend (mọi BM + fee) | ShopBase orders ÷ Meta billing | **Report & P&L CHỈ dùng Blended.** Phản ánh lãi/lỗ thật |

- **Report & P&L của SOP này chỉ dùng Blended/True ROAS.** Tử số = tổng order ShopBase net-of-refund, KHÔNG phải pixel-attributed revenue.
- Platform ROAS chỉ để đọc nhanh; phải hiệu chỉnh về Blended trước khi commit kill/scale (Platform ≥ 3.0 ⇒ Blended ≈ 2.5).

## 1b. Break-even ROAS & profit-per-SKU (công thức đầy đủ)
**Break-even ROAS = 1 / gross margin** — KHÔNG hard-code 2.5. Ngưỡng winner đặt theo BE-ROAS riêng của từng **SKU × market**:
- **US ~2.75** (GM trước ads ~36%). Ngưỡng cũ "winner ≥ 2.5" THẤP HƠN break-even → scale vào vùng lỗ.
- **EU ~5.3** (GM ~23% trên giá net-of-VAT). ⚠️ Đơn EU ở giá hiện tại gần như **không lãi qua cold-ads** → bật cờ cảnh báo, **pricing EU phải tính riêng** (nâng giá / provider rẻ hơn / coi EU là retention).

```
Profit-per-SKU (mỗi đơn) =
    giá bán
  − base print cost
  − shipping
  − (ShopBase fee + payment/gateway fee)        ← ~2.9% + $0.30
  − ad cost phân bổ (= CPA của SKU/đợt)
  − VAT phải nộp (ĐƠN EU, theo nước đến — xem SOP-BCK-003)
  − fx adjustment (quy đổi USD→VND, §4 quy trình)

Contribution Margin = Profit-per-SKU / giá bán
```
⚠️ Bản trước bỏ sót **VAT (EU) + fx ở cấp SKU** → lãi ảo. Bắt buộc trừ đủ cả hai. Đơn EU tính margin trên giá **net-of-VAT**.

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Tính profit-per-SKU | finance AI | Owner | — | Merch |
| ROAS/CPA report | finance AI | Owner | Growth (fb-ads) | Owner |
| P&L + CEO brief | finance AI | Owner | — | tất cả phòng |

`[AI WORKFORCE]` finance AI: tính toán, phân bổ ad-spend, lập bảng + brief, flag SKU lỗ & campaign dưới ngưỡng. Owner: ra quyết định kill/scale.

## 3. Quy trình (ICOM)
1. **Lấy nền** (I: ledger + ad-spend + COGS; M: profit model): pull dữ liệu kỳ.
2. **Tính profit-per-SKU** (C: công thức §1b — trừ đủ fee + ad + VAT(EU) + fx): ra contribution margin từng SKU.
3. **Tính ROAS/CPA** (C: ngưỡng = BE-ROAS theo SKU/market, KHÔNG dùng 2.5 cứng; CPA<$20): so Blended ROAS với BE-ROAS riêng (US ~2.75, EU ~5.3) → gắn cờ winner/loser.
4. **Lập P&L + quy đổi VND** (C: FX = Vietcombank bán ra, cuối kỳ — 1 giá/kỳ, ghi nguồn+ngày; M: P&L template): Revenue(Blended, net-of-refund)−COGS−OPEX−Ad = net profit; quy VND.
5. **CEO brief** (O: brief so target): nêu gap vs **500tr VND/tháng (~$20k)** + đề xuất batch nào scale/kill.

## 4. Phân nhánh
- SKU contribution margin âm 2 kỳ liên tiếp → flag kill/redesign → Merch (SOP-MER-006).
- Campaign Blended ROAS < BE-ROAS của SKU/market (US ~2.75, EU ~5.3) → cảnh báo Growth (fb-ads) cùng evidence.
- Đơn EU không đạt BE-ROAS qua cold-ads → cờ cảnh báo pricing EU (đề xuất nâng giá / provider rẻ hơn / retention), không scale.
- Net margin <20% → CEO brief đánh dấu `need_review: true`.
- Thiếu phân bổ ad theo SKU → dùng Blended ROAS + ghi giả định, không bịa số per-SKU.

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| Profit calc accuracy | ≥ 99% so ledger | spot-check |
| ROAS/CPA đúng nguồn ad-spend | 100% khớp Meta billing | recon |
| CEO brief on-time | ≤ ngày 6 tháng sau | calendar |
| FX traceability | 100% có nguồn (Vietcombank bán ra)+ngày cuối kỳ | brief footnote |

**Error budget:** ≤1% lệch profit. **Prevention:** FX = Vietcombank bán ra cuối kỳ — một giá khóa kỳ duy nhất (áp cả cấp SKU lẫn P&L), công thức profit-per-SKU trừ đủ VAT(EU)+fx, ad-allocation versioned, evidence + confidence_score trong mọi brief.

## 6. Tài nguyên + Links
- **Định nghĩa chuẩn: [unit-economics](../../../_shared/unit-economics.md)** (Platform vs Blended ROAS, BE-ROAS=1/GM, profit-per-SKU, FX)
- [SOP-BCK-001 ledger](../../keep-books/template/sop_bck-001_bookkeeping_v1.0_2026-06-23.md) · [Company OKR O1](../../../00-company/okr_company-001_company-okr_v1.0_2026-06-23.md)
- KPI: [backoffice KPIs](../../kpi_bck-001_backoffice-kpis_v1.0_2026-06-23.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
