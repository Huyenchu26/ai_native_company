# DAKOfits — Unit Economics (Single Source of Truth)

**Mã:** REF-ECON-001 · **Phiên bản:** 1.0 · **Ngày:** 2026-06-23 · **Áp dụng:** toàn công ty

> Mọi SOP nói tới ROAS / margin / profit-per-SKU **PHẢI** dùng định nghĩa ở đây. Đây là canonical reference cho: BCK-002 (profit/ROAS), MER-003 (pricing), GRW-002 (FB Ads), GRW-004 (growth report).
> **Lý do tồn tại:** DAKOfits là mô hình **FB-ads-led** → ad cost là chi phí biến đổi LỚN NHẤT. Nếu công thức lãi bỏ ad cost/fee/VAT → "lãi ảo" → scale nhầm SP đang lỗ.

---

## 1. Hai loại ROAS — KHÔNG được nhầm

| Loại | Định nghĩa | Nguồn | Đặc tính |
|------|-----------|-------|----------|
| **Platform ROAS** | Revenue Meta gán cho ads / Ad spend | Ads Manager (last-click + view-through) | **Cao hơn thực 20–40%** (over-attribution, view-through, không trừ refund) |
| **Blended / True ROAS** | **Tổng** revenue thực (ShopBase, net-of-refund) / **Tổng** ad spend (mọi BM + fee) | ShopBase orders ÷ Meta billing | Phản ánh lãi/lỗ THẬT. Dùng cho mọi quyết định scale/kill & report. |

**Quy tắc:**
- Quyết định **kill/scale** đọc Platform ROAS (real-time) nhưng **hiệu chỉnh** về Blended trước khi commit.
- Ngưỡng winner Platform ROAS phải đặt **cao hơn** Blended target để bù over-attribution: **Platform ≥ 3.0 ⇒ Blended ≈ 2.5**.
- **Report & P&L (BCK-002/004) chỉ dùng Blended/True ROAS.** Tử số = tổng order ShopBase thực, KHÔNG phải pixel-attributed revenue.
- **Attribution window chuẩn công ty:** 7-day click / 1-day view (chốt cố định để đọc nhất quán).

---

## 2. Break-even ROAS — gắn vào margin, KHÔNG hard-code

```
Gross Margin trước ads (GM) = (Giá_net − COGS_non_ad) / Giá_net
COGS_non_ad = base print cost + shipping + (ShopBase fee + payment fee)
Giá_net = giá thu được SAU khi trừ VAT (đơn EU); = giá bán (đơn US, không VAT)

Break-even ROAS (BE-ROAS) = 1 / GM        ← ROAS tối thiểu để HÒA VỐN trên ads
Target-profit ROAS         = BE-ROAS / (1 − target_net_margin)
```

→ **Không có một ngưỡng ROAS chung cho 3.200 SP.** Mỗi SKU (và mỗi market US/EU) có BE-ROAS riêng theo giá & COGS.

---

## 3. Profit-per-SKU — công thức ĐẦY ĐỦ (chống lãi ảo)

```
Profit-per-SKU (mỗi đơn) =
    Giá bán
  − base print cost
  − shipping
  − (ShopBase fee + payment/gateway fee)        ← ~2.9% + $0.30
  − ad cost phân bổ (= CPA của SKU/đợt)
  − VAT phải nộp (đơn EU, theo nước đến — xem BCK-003)
  − fx adjustment (quy đổi USD→VND, xem §5)

Contribution Margin = Profit-per-SKU / Giá bán
```

**Pricing floor (MER-003) đặt trên Contribution Margin SAU ads, KHÔNG phải gross margin trên base cost.** Một SKU "gross 50%" có thể contribution âm sau CPA $20 + VAT.

---

## 4. Ví dụ thực tế (AOP legging)

**US — giá $49.99, không VAT:**
| Khoản | Giá trị |
|-------|--------|
| Giá bán | $49.99 |
| Base print | −$22.00 |
| Shipping | −$8.00 |
| ShopBase+payment fee | −$1.80 |
| **GM trước ads** | **18.19 / 49.99 = 36.4%** |
| **BE-ROAS = 1/0.364** | **≈ 2.75** |

→ ⚠️ Ngưỡng cũ "winner ROAS ≥ 2.5" **THẤP HƠN break-even 2.75** → đang scale vào vùng lỗ! Winner thật cần **Blended ≥ 2.75** (Platform ≥ ~3.3) chỉ để hòa vốn; muốn net margin 15% cần Blended ≈ 3.2.

**EU — giá €49.99 VAT-inclusive 21% (IOSS):**
| Khoản | Giá trị |
|-------|--------|
| Giá net (49.99/1.21) | €41.31 |
| Base + ship + fee | −€31.80 |
| **GM trước ads** | **9.51 / 41.31 = 23%** |
| **BE-ROAS (gross basis = 49.99/9.51)** | **≈ 5.3** |

→ ⚠️ **Đơn EU ở mức giá này gần như không có lãi qua ads.** Hành động bắt buộc: **nâng giá EU (€59–69)**, hoặc chọn provider EU rẻ hơn, hoặc coi EU là retention/organic chứ không cold-ads. **Đây là phát hiện quan trọng — pricing EU phải tính riêng.**

---

## 5. FX USD→VND
- **Nguồn cố định: Vietcombank, tỷ giá BÁN RA, ngày cuối kỳ.** (chốt 1 giá/kỳ, ghi rõ ngày + screenshot nguồn vào ledger).
- Áp dụng nhất quán cả cấp SKU (profit-per-SKU) lẫn P&L tổng.
- Target công ty: **500tr VND/tháng ≈ $20k** (tham chiếu, không hard-code tỷ giá vào target — quy đổi theo FX kỳ).

---

## 6. Checklist dùng đúng economics (cho mọi SOP tài chính/ads)
- [ ] Phân biệt Platform vs Blended ROAS đúng ngữ cảnh
- [ ] Ngưỡng winner = BE-ROAS theo SKU/market, KHÔNG dùng 2.5 cứng
- [ ] Profit-per-SKU trừ đủ: fee + ad + VAT(EU) + fx
- [ ] Đơn EU tính margin trên giá NET-of-VAT
- [ ] FX = Vietcombank bán ra, cuối kỳ
