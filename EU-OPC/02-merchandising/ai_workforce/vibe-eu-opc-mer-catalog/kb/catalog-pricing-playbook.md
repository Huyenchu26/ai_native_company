# KB — Catalog · Pricing · Sync Playbook (DAKOfits)

> Canonical economics: **[../../../_shared/unit-economics.md](../../../_shared/unit-economics.md)** — mọi công thức ROAS/margin/profit phải KHỚP file đó.
> SOP: MER-002 (setup) · MER-003 (pricing) · MER-004 (sync-qc).

---

## 1. Provider US/EU — map theo thị trường

| Thị trường | Provider | Lý do |
|-----------|----------|-------|
| Đơn **US** | Printify/PrintBase **provider US** | Ship nội địa nhanh, không VAT |
| Đơn **EU** | Printify/PrintBase **provider EU** | Giảm ship time + VAT/customs (IOSS) |
| Bán cả 2 | **Setup 2 blueprint** (US + EU) | Pricing & cost tính RIÊNG từng market |

- Provider OOS blank → chọn provider thay thế **cùng vùng**.
- Blueprint phải hỗ trợ đủ size **XS–3XL**; nếu thiếu XS hoặc 3XL → đổi blueprint.

## 2. Variant set chuẩn — XS–3XL × color

- Size: **XS, S, M, L, XL, 2XL, 3XL** → coverage **100%**, không bỏ size (mất đơn).
- Color: tất cả color blueprint hỗ trợ.
- **Plus-size 2XL–3XL** thường base cost cao hơn → **price step-up** giữ contribution floor (không bán lỗ size lớn).
- QC mockup: AOP 360°, alignment seam/print, render đủ góc.

## 3. Pricing — CONTRIBUTION MARGIN sau ads (KHÔNG margin ảo)

❌ KHÔNG dùng `giá = cost / (1 − margin)` → chỉ tính trên base print cost → **margin ảo** (bỏ ship, fee, ad, VAT). Một SKU "gross 50%" có thể **contribution âm** sau CPA $20 + VAT.

✅ Floor đặt trên **Contribution Margin SAU ads**:

```
Contribution Margin (mỗi đơn) =
    Giá_net
  − base print cost
  − shipping (per-order; đơn nhiều item → ship bổ sung per-item theo bảng provider)
  − (ShopBase fee + payment/gateway fee ≈ 2.9% + $0.30)
  − ad cost phân bổ (= CPA SKU/đợt từ Growth GRW-002)
  − VAT phải nộp (đơn EU)

Giá_net = giá bán            (đơn US, không VAT)
        = giá bán / 1.21     (đơn EU — VAT-inclusive 21% IOSS → tính margin trên NET-of-VAT)

Contribution % = Contribution Margin / giá bán
```

**FLOOR cứng: Contribution % ≥ 15% SAU khi trừ CPA mục tiêu.** Chưa biết CPA thực → dùng CPA mục tiêu Growth của đợt.

Psychological pricing `$XX.99` + set compare-at 100% SP.

## 4. Break-even ROAS per SKU/market

```
GM trước ads (GM) = (Giá_net − COGS_non_ad) / Giá_net
COGS_non_ad        = base + ship + (ShopBase + payment fee)
Break-even ROAS    = 1 / GM
Target-profit ROAS = BE-ROAS / (1 − target_net_margin)
```

→ **KHÔNG có một ngưỡng ROAS chung cho 3.200 SP.** Mỗi SKU + mỗi market có BE-ROAS riêng.

**Quy tắc đối chiếu:** nếu **BE-ROAS của SKU > ngưỡng winner Growth** → SKU sẽ scale vào vùng lỗ → **nâng giá / đổi provider TRƯỚC publish**.

### Ví dụ US — giá $49.99 (không VAT)
| Khoản | Giá trị |
|-------|--------|
| Giá bán = giá net | $49.99 |
| Base print | −$22.00 |
| Shipping | −$8.00 |
| ShopBase + payment fee | −$1.80 |
| **GM trước ads** | 18.19 / 49.99 = **36.4%** |
| **BE-ROAS = 1/0.364** | **≈ 2.75** |

⚠️ Ngưỡng cũ "winner ROAS ≥ 2.5" THẤP HƠN break-even 2.75 → đang scale vào vùng lỗ. Winner thật cần Blended ≥ 2.75 chỉ để hòa vốn; net margin 15% cần Blended ≈ 3.2.

### Ví dụ EU — giá €49.99 VAT-inclusive 21% (IOSS) — TÍNH RIÊNG
| Khoản | Giá trị |
|-------|--------|
| Giá net (49.99/1.21) | €41.31 |
| Base + ship + fee | −€31.80 |
| **GM trước ads** | 9.51 / 41.31 = **23%** |
| **BE-ROAS (gross basis)** | **≈ 5.3** |

⚠️ **Đơn EU ở mức giá này gần như không lãi qua cold-ads.** Hành động bắt buộc:
1. **Nâng giá EU lên €59–69**, hoặc
2. Chọn provider EU rẻ hơn, hoặc
3. Coi EU là **retention/organic** chứ không cold-ads.

**Pricing EU phải tính RIÊNG — KHÔNG dùng chung công thức/giá với US.**

## 4b. Competitive pricing — định giá cạnh tranh theo giá đối thủ

Input mới: **competitor price table** từ Product Studio **SOP-PRD-001 (chị Tầm)** — khoảng giá bán min–max của đối thủ + bundle/offer, theo niche & market (US/EU).

**Logic:** đặt giá trong **vùng cạnh tranh thị trường** (so với đối thủ) NHƯNG sàn cứng vẫn là:
- **contribution-margin floor** (sau ad+fee+VAT, §3), VÀ
- **≥ break-even ROAS** (§4).

Ghi lại vào pricing-decision: `competitor_price_ref {min,max,currency}` + `competitive_position` (`below_market` / `at_market` / `premium`).

| Quan hệ giá ta vs vùng đối thủ | Hành động |
|--------------------------------|-----------|
| Floor của ta ≤ vùng đối thủ | Đặt `at_market` / `below_market` trong vùng, miễn ≥ floor |
| Floor của ta cao hơn cận trên vùng đối thủ | `premium` + justify (AOP all-over, bundle), HOẶC đổi provider rẻ hơn |
| **Vùng giá cạnh tranh < break-even của ta** | ⚠️ **flag** `below_breakeven_flag: true` + `need_review: true` |

⚠️ **RULE — giá cạnh tranh < break-even → flag, KHÔNG phá floor.**
Nếu giá đối thủ thấp hơn giá break-even của ta (rất hay gặp ở **EU** vì VAT đẩy BE-ROAS ~5.3) → niche này **KHÔNG viable** ở mức giá cạnh tranh. KHÔNG hạ giá xuống dưới contribution floor để đú đối thủ (sẽ scale vào vùng lỗ). Hành động: **bỏ niche** hoặc **tìm provider rẻ hơn** để kéo break-even xuống. Quyết định escalate OPC qua `need_review`.

## 5. FX USD→VND

- **Nguồn cố định: Vietcombank, tỷ giá BÁN RA, ngày cuối kỳ.** Chốt 1 giá/kỳ, ghi rõ ngày + nguồn vào ledger pricing.
- Áp dụng nhất quán cả cấp SKU (profit-per-SKU) lẫn P&L tổng.

## 6. ShopBase sync — QC checklist (accuracy ≥ 99%)

Diff field source (Printify/PrintBase) ↔ ShopBase, field lệch → re-sync:

- [ ] **Giá** từng variant khớp bảng MER-003
- [ ] **Variant** XS–3XL × color đủ 100%
- [ ] **Ảnh/mockup** đúng, không lỗi render
- [ ] **Stock** real-time (provider OOS variant → ẩn variant / đổi provider)
- [ ] **Page copy** (từ MER-001) khớp
- [ ] **GPSR label** hiển thị trên PDP (đơn EU)
- [ ] Map provider variant ↔ ShopBase SKU đúng
- [ ] Tính **sync accuracy %** → < 99% → re-sync field lệch trước publish
- [ ] Listing defect rate ≤ 2%

## 7. GATE — Pre-sync GPSR (cứng, đơn EU)

**No GPSR (EU) → no publish.** Bước 1 MER-004:
- Kiểm SP EU có **GPSR label + clearance ID** → thiếu → **STOP**, trả `vibe-eu-opc-mer-product-page`.
- Kiểm Contribution floor pass + variant XS–3XL đủ trước khi sync.
- GPSR/IP clearance được CẤP bởi backoffice compliance (`vibe-eu-opc-bck-*`); skill này chỉ **ĐỌC** clearance làm gate, KHÔNG tự cấp.

## 8. Phân nhánh nhanh

| Điều kiện | Nhánh |
|-----------|-------|
| Contribution % < floor sau ads | Đổi provider rẻ hơn / nâng giá / OPC quyết bỏ |
| BE-ROAS > ngưỡng winner Growth | Nâng giá để BE-ROAS ≤ ngưỡng |
| EU không lãi qua ads | Nâng giá €59–69, tính NET-of-VAT, hoặc EU retention/organic |
| Giá cạnh tranh thị trường < break-even ta | Flag need_review (below_breakeven_flag) — bỏ niche / đổi provider rẻ hơn, KHÔNG phá floor |
| Plus-size cost cao | Step-up giá giữ floor |
| Design fail QC | Trả phòng 01 (vibe-opc-pod-product-design) |
| SP EU thiếu GPSR | STOP, trả MER-001 / product-page |
| Sync accuracy < 99% | Re-sync field lệch |
| Provider OOS variant | Ẩn variant / đổi provider cùng vùng |
