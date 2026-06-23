# SOP-MER-003 — Variant Pricing (Gross Margin 45–55%)

**Dept:** 02-merchandising (`mer`) · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-merch-catalog-sync` · **Accountable:** OPC

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | Product blueprint (variant XS–3XL/color) từ MER-002; provider cost per variant; ship cost; giá tham chiếu (Gearbunch, thị trường); **CPA / BE-ROAS mục tiêu từ Growth (GRW-002)** |
| **Control (C)** | **Pricing floor đặt trên Contribution Margin SAU ads** (xem §1.1), KHÔNG phải gross-on-base-cost; **break-even ROAS = 1/GM** đối chiếu ngưỡng winner Growth; psychological pricing; VAT note (EU, tính trên giá NET-of-VAT) |
| **Output (O)** | Bảng giá variant XS–3XL/color đạt contribution floor; giá compare-at; bundle price; **BE-ROAS per SKU/market** |
| **Mechanism (M)** | Catalog-Sync AI + OPC approve ngoài band |
| **Upstream** | MER-002 (blueprint) |
| **Downstream** | MER-001 (page), MER-004 (sync) |

---

## 1. Tổng Quan

Set giá cho từng variant AOP legging/activewear sao cho **ở ROAS mục tiêu vẫn lãi**. DAKOfits là mô hình FB-ads-led → ad cost là chi phí biến đổi lớn nhất; pricing floor **KHÔNG** được đặt trên gross-margin-trên-base-cost (margin ảo) mà phải đặt trên **Contribution Margin SAU ads** (xem §1.1). AI tự quyết trong band; ngoài band cần OPC. Plus-size (2XL–3XL) thường cost cao hơn → có thể price step-up.

> **Định nghĩa chuẩn (canonical):** [unit-economics](../../../_shared/unit-economics.md). Mọi công thức ROAS / margin / profit trong SOP này phải KHỚP file đó.

### 1.1 Công thức pricing floor (thay cho `giá = cost/(1−margin)`)

Công thức cũ `giá = cost/(1 − margin)` chỉ tính margin trên base print cost → **margin ảo**: bỏ qua ship, fee, ad cost (CPA) và VAT(EU). Một SKU "gross 50%" có thể **contribution âm** sau CPA $20 + VAT. Pricing floor mới đặt trên Contribution Margin sau ads:

```
Contribution Margin (mỗi đơn) =
    Giá_net
  − base print cost
  − shipping (xem giả định phân bổ §1.2)
  − (ShopBase fee + payment/gateway fee)      ← ~2.9% + $0.30
  − ad cost phân bổ (= CPA của SKU/đợt, lấy từ Growth GRW-002)
  − VAT phải nộp (đơn EU — đã trừ ở Giá_net, xem dưới)

Giá_net = giá bán (đơn US, không VAT)
        = giá bán / 1.21 (đơn EU, VAT-inclusive 21% IOSS — tính margin trên giá NET-of-VAT)

Contribution % = Contribution Margin / Giá bán      ← FLOOR đặt trên số này
```

**Floor cứng: Contribution % ≥ 15% SAU khi trừ CPA mục tiêu.** Nếu chưa biết CPA thực, dùng CPA mục tiêu của Growth cho đợt.

### 1.2 Break-even ROAS per SKU

Mỗi SKU + mỗi market (US/EU) có BE-ROAS riêng — **KHÔNG có một ngưỡng ROAS chung cho 3.200 SP**:

```
Gross Margin trước ads (GM) = (Giá_net − COGS_non_ad) / Giá_net
COGS_non_ad = base + ship + (ShopBase + payment fee)
Break-even ROAS (BE-ROAS) = 1 / GM     ← ROAS tối thiểu để hòa vốn trên ads
Target-profit ROAS = BE-ROAS / (1 − target_net_margin)
```

Đặt giá sao cho **ở ROAS mục tiêu của Growth (winner threshold) vẫn lãi**: nếu BE-ROAS của SKU **cao hơn** ngưỡng winner Growth → SKU sẽ scale vào vùng lỗ → phải nâng giá hoặc đổi provider.

**Ví dụ US** (giá $49.99): base $22 + ship $8 + fee $1.80 → GM = 18.19/49.99 = 36.4% → **BE-ROAS ≈ 2.75**. Ngưỡng cũ "winner ROAS ≥ 2.5" THẤP HƠN break-even 2.75 → đang scale vào vùng lỗ. Winner thật cần Blended ≥ 2.75 chỉ để hòa vốn; muốn net margin 15% cần Blended ≈ 3.2.

**Đơn EU — cảnh báo:** tính margin trên giá NET-of-VAT (€49.99/1.21 = €41.31). Ở mức giá này GM ≈ 23% → BE-ROAS (gross basis) ≈ 5.3 → **EU gần như không lãi qua cold-ads**. Hành động bắt buộc: **nâng giá EU lên €59–69**, hoặc chọn provider EU rẻ hơn, hoặc coi EU là retention/organic. **Pricing EU phải tính riêng, không dùng chung công thức/giá với US.**

### 1.3 Giả định phân bổ

- **Shipping phân bổ per-order** (1 đơn = 1 lần ship cơ bản); nếu đơn nhiều item, ship bổ sung per-item theo bảng provider → ghi rõ giả định đang dùng vào ledger pricing.
- **Ad cost (CPA) phân bổ per-order** theo CPA SKU/đợt từ Growth.

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Catalog-Sync AI | 05-Backoffice |
|-----------|-----|-----------------|---------------|
| Lấy cost provider | A | **R** `[AI WORKFORCE]` | I |
| Tính giá theo margin | A | **R** `[AI WORKFORCE]` | C (VAT) |
| Set giá trong band 45–55% | I | **R (tự quyết)** | I |
| Duyệt giá ngoài band | **A/R** | C | I |

`[AI WORKFORCE]` = skill `vibe-opc-pod-merch-catalog-sync`.

## 3. Quy Trình

### Bước 1 — Lấy cost & reference
| ICOM | Nội dung |
|------|----------|
| I | Provider cost, ship, giá ref, CPA mục tiêu (GRW-002) |
| C | Nguồn base cost = provider chuẩn (Printify/PrintBase official cost API, US+EU provider); FX USD→VND = **Vietcombank bán ra, ngày cuối kỳ** (xem [unit-economics §5](../../../_shared/unit-economics.md)); ship/fee lấy theo bảng provider+ShopBase hiện hành |
| O | Cost base per variant (đủ base+ship+fee, đã quy đổi FX nhất quán) |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Lấy cost từng variant (provider US/EU khác nhau) | AI `[AI WORKFORCE]` |
| Thu giá ref Gearbunch/thị trường cho legging AOP | AI |

### Bước 2 — Tính giá theo Contribution Margin sau ads
| ICOM | Nội dung |
|------|----------|
| I | Cost base, CPA mục tiêu, ngưỡng winner Growth |
| C | Contribution floor ≥ 15% sau CPA (§1.1); giá NET-of-VAT cho EU |
| O | Giá variant đề xuất + Contribution % |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Tính giá sao cho **Contribution % ≥ floor SAU ad+fee+VAT** theo §1.1 (KHÔNG dùng `giá = cost/(1−margin)`) | AI `[AI WORKFORCE]` |
| EU: tính margin trên **giá NET-of-VAT** (giá/1.21) rồi mới áp floor → nếu không đạt, nâng giá EU €59–69 (§1.2) | AI `[AI WORKFORCE]` |
| Plus-size 2XL–3XL: step-up giữ contribution floor | AI |
| Psychological pricing ($XX.99), set compare-at | AI |

### Bước 3 — Verify contribution floor, BE-ROAS & VAT
| ICOM | Nội dung |
|------|----------|
| I | Giá đề xuất, CPA mục tiêu, ngưỡng winner Growth |
| C | Contribution floor sau ads; BE-ROAS = 1/GM ≤ ngưỡng winner; VAT EU note |
| O | Giá pass floor + BE-ROAS per SKU/market |
| M | Catalog-Sync AI |

| Hành động | Ai |
|-----------|-----|
| Check 100% variant **Contribution % ≥ floor SAU ad+fee+VAT** | AI |
| Tính **BE-ROAS = 1/GM** mỗi SKU/market; đối chiếu ngưỡng winner Growth (US ví dụ BE-ROAS ~2.75) | AI |
| BE-ROAS > ngưỡng winner Growth → SKU sẽ scale lỗ → nâng giá / đổi provider trước khi publish | AI |
| EU: tính trên giá NET-of-VAT; nếu BE-ROAS quá cao (~5.3 ở €49.99) → nâng giá EU €59–69 hoặc tính riêng (phối 05) | AI |
| Variant không đạt contribution floor → flag OPC / đổi provider | AI |

### Bước 4 — Bundle pricing & approve
| ICOM | Nội dung |
|------|----------|
| I | Giá variant + sports-bra cost |
| C | Bundle margin ≥ 45% |
| O | Giá bundle + approve |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Tính giá bundle leggings+sports-bra (chiết khấu nhẹ, giữ margin) | AI |
| OPC duyệt nếu có giá ngoài band | OPC |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| Contribution % < floor sau ads | Đổi provider rẻ hơn / nâng giá / OPC quyết bỏ |
| BE-ROAS > ngưỡng winner Growth | Nâng giá để BE-ROAS ≤ ngưỡng (đảm bảo lãi ở ROAS mục tiêu) |
| Plus-size cost cao | Step-up giá giữ floor |
| Provider EU cost cao / EU không lãi qua ads | Nâng giá EU €59–69, tính trên giá NET-of-VAT, hoặc coi EU retention/organic |
| Promo/bundle | Discount nhưng không phá floor |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| Contribution % per variant (sau ad+fee+VAT) | ≥ floor (15% sau CPA), 100% SP | (giá_net − base − ship − fee − CPA)/giá |
| BE-ROAS per SKU/market ≤ ngưỡng winner Growth | 100% SP | 1/GM đối chiếu GRW-002 |
| Gross margin trước ads (tham chiếu) | trong band 45–55% | (giá_net − COGS_non_ad)/giá_net |
| Compare-at set | 100% SP | check |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Lãi ảo (margin trên base cost) | Floor đặt trên Contribution sau ad+fee+VAT, KHÔNG dùng `giá=cost/(1−margin)` |
| Scale vào vùng lỗ | Đối chiếu BE-ROAS=1/GM với ngưỡng winner Growth trước publish |
| Quên cost ship/fee/CPA/VAT | Cost base gồm ship+fee; trừ CPA; EU tính trên giá NET-of-VAT |
| Plus-size lỗ margin | Step-up pricing giữ contribution floor |

## 6. Tài Nguyên & Links

- **Định nghĩa chuẩn: [unit-economics](../../../_shared/unit-economics.md)** (canonical — platform vs blended ROAS, BE-ROAS, contribution margin, FX Vietcombank)
- Template: `set-pricing/template/`
- Upstream: [SOP-MER-002](../../setup-printify/template/sop_mer-002_printify-setup_v1.0_2026-06-23.md)
- CPA / ngưỡng winner ROAS: Growth [SOP-GRW-002]
- VAT: phòng 05-backoffice (finance)
- Downstream: [SOP-MER-001](../../write-product-page/template/sop_mer-001_product-page_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo SOP variant pricing |
| v1.1 | 2026-06-23 | Sửa floor sang Contribution Margin sau ads (bỏ `giá=cost/(1−margin)`); thêm BE-ROAS=1/GM per SKU đối chiếu winner Growth; EU tính trên giá NET-of-VAT + nâng giá €59–69; điền Control Bước 1 (provider cost + FX Vietcombank); ghi giả định ship per-order; link unit-economics |
