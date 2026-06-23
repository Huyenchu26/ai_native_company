# Finance Playbook — DAKOfits (vibe-eu-opc-bck-finance)

> Canonical economics: [unit-economics](../../../../_shared/unit-economics.md). Mọi công thức ở đây PHẢI khớp file đó. Playbook này là cách áp dụng vận hành cho SOP-BCK-001/002/003.

---

## 1. Chart of Accounts (sổ kép)
| Account | Loại | Nguồn statement |
|---|---|---|
| Revenue | Income | ShopBase payout/order export (net-of-refund) |
| COGS — print (base) | COGS | Printify/PrintBase invoice |
| COGS — shipping | COGS | Printify/PrintBase invoice |
| Ad-spend | OPEX (biến đổi LỚN NHẤT) | Facebook Ads billing (mọi BM) |
| Gateway/payment fee | OPEX | Stripe/PayPal statement (~2.9% + $0.30) |
| ShopBase fee | OPEX | ShopBase payout |
| Refund / chargeback | Contra-revenue | ShopBase + gateway |
| VAT payable | Liability | tính theo SOP-BCK-003 |
| FX gain/loss | Adjustment | quy đổi USD→VND |

**Nguyên tắc:** mỗi giao dịch truy được về `order_id`/`SKU` để feed profit-per-SKU. USD là đồng ghi gốc; quy VND ở bước báo cáo.

## 2. Fee Reconciliation
Đối soát **hằng tuần**, khóa sổ **hằng tháng (≤ ngày 5)**.
1. Pull 4 nguồn: ShopBase payout, Printify/PrintBase invoice, Meta billing, gateway statement.
2. So **fee thực tế vs fee kỳ vọng** (theo fee schedule provider/gateway).
3. Chênh lệch → ghi vào discrepancy log. **Flag** nếu > $5 hoặc > 2%.
4. **Escalate Owner** nếu discrepancy > 2% hoặc > $50 → giữ kỳ mở.
5. Thiếu statement (provider chậm) → ghi accrual, `need_review: true`.
- Coverage = 100% statement đối soát. Accuracy ≥ 99.9%.

## 3. Profit-per-SKU — công thức ĐẦY ĐỦ
```
Profit-per-SKU (mỗi đơn) =
    giá bán
  − base print cost
  − shipping
  − (ShopBase fee + payment/gateway fee)     ← ~2.9% + $0.30
  − ad cost phân bổ (= CPA của SKU/đợt)
  − VAT phải nộp (ĐƠN EU, theo nước đến — §6)
  − fx adjustment (USD→VND, §5)

Contribution Margin = Profit-per-SKU / giá bán
```
- Đơn **EU** tính margin trên giá **net-of-VAT** (= giá / (1 + rate)).
- Bỏ sót VAT(EU) hoặc fx ở cấp SKU = **lãi ảo** → cấm.
- Pricing floor (MER-003) đặt trên **Contribution Margin SAU ads**, KHÔNG phải gross margin trên base.
- SKU contribution margin âm 2 kỳ liên tiếp → flag kill/redesign → Merch (SOP-MER-006).

## 4. True/Blended ROAS + Break-even
| Loại | Định nghĩa | Dùng cho |
|---|---|---|
| Platform ROAS | Revenue Meta gán / ad spend (last-click + view-through) | Đọc nhanh real-time; cao hơn thực 20–40% |
| **Blended/True ROAS** | **tổng** revenue ShopBase net-of-refund / **tổng** ad spend (mọi BM + fee) | **Report & P&L CHỈ dùng cái này** |

- Hiệu chỉnh trước commit kill/scale: **Platform ≥ 3.0 ⇒ Blended ≈ 2.5**. Attribution window công ty: 7-day click / 1-day view.
- **Break-even ROAS = 1 / gross margin trước ads** — KHÔNG hard-code 2.5:
  - **US ~2.75** (GM ~36% ở giá $49.99). Winner ≥ 2.5 cũ < break-even → scale vào vùng lỗ.
  - **EU ~5.3** (GM ~23% trên giá net-of-VAT €41.31 từ €49.99 @21%). ⚠️ Đơn EU gần như **không lãi qua cold-ads**.
- `Target-profit ROAS = BE-ROAS / (1 − target_net_margin)`. Muốn net 15% US ⇒ Blended ≈ 3.2.
- Campaign Blended ROAS < BE-ROAS của SKU/market → cảnh báo Growth (fb-ads) kèm evidence. EU dưới BE-ROAS qua cold-ads → cờ pricing EU (nâng €59–69 / provider rẻ hơn / retention), KHÔNG scale.

## 5. FX USD→VND
- **Nguồn cố định: Vietcombank, tỷ giá BÁN RA, ngày cuối kỳ.** Chốt 1 giá/kỳ, ghi ngày + screenshot vào ledger.
- Áp nhất quán cả cấp SKU lẫn P&L. KHÔNG bịa tỷ giá; thiếu nguồn → `need_review`.
- Target: **500tr VND/tháng ≈ $20k** (quy đổi theo FX kỳ, không hard-code tỷ giá vào target).

## 6. VAT OSS/IOSS + US nexus
| Scheme | Áp dụng | Kỳ khai |
|---|---|---|
| **IOSS** | đơn ≤ €150 nhập từ ngoài EU, thu VAT tại điểm bán | **tháng** |
| **OSS (Union)** | hàng đã ở EU bán xuyên biên giới EU | **quý** |
- VAT = giá × rate **nước đến (destination)**. Bảng VAT rate member state versioned trong `_knowledge`; rate đổi → cập nhật trước khi tính.
- Đơn > €150 từ ngoài EU → ngoài IOSS, VAT khi nhập khẩu → flag DDP/carrier.
- Thiếu VAT number/OSS registration → escalate Owner ngay (rủi ro pháp lý).
- **US sales tax:** ShopBase thu tự động nếu đã set; finance AI chỉ **reconcile + ghi chú nexus** theo bang (economic nexus thresholds). US bang đạt nexus mới → `need_review` để Owner đăng ký. **KHÔNG tự khai US.**
- SLO: VAT filing on-time **100%** (gate cứng legal, error budget 0%).

## 7. P&L + CEO brief
```
Net profit = Revenue(Blended, net-of-refund) − COGS(print+ship) − OPEX(fee+ad) − VAT − tax
```
- Quy VND theo FX kỳ. CEO brief nêu gap vs **500tr/$20k**, batch nào scale/kill, SKU lỗ, campaign dưới BE-ROAS.
- Net margin < 20% → brief đánh dấu `need_review: true`.
- Mọi brief mang `evidence[]` + `confidence_score` (≥0.7 mới commit) + FX footnote (nguồn + ngày).

## Links
- [SOP-BCK-001](../../../keep-books/template/sop_bck-001_bookkeeping_v1.0_2026-06-23.md) · [SOP-BCK-002](../../../track-profit/template/sop_bck-002_profit-roas_v1.0_2026-06-23.md) · [SOP-BCK-003](../../../file-vat/template/sop_bck-003_vat-oss-ioss_v1.0_2026-06-23.md)
- [unit-economics (canonical)](../../../../_shared/unit-economics.md)
