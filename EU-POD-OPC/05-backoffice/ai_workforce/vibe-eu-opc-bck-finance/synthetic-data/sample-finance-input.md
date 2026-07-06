# Sample Finance Input — 1 kỳ (DAKOfits)

> Dữ liệu giả lập 1 kỳ (tháng 2026-05) cho smoke-test. KHÔNG phải số thật. FX kỳ: Vietcombank bán ra **25.450 VND/USD**, ngày **2026-05-31**.

## A. Orders (ShopBase export, net-of-refund)
| order_id | SKU | market | nước đến | qty | giá bán | refund |
|---|---|---|---|---|---|---|
| SB-10231 | LEG-GSD-US | US | US | 1 | $49.99 | 0 |
| SB-10232 | LEG-GSD-US | US | US | 1 | $49.99 | 0 |
| SB-10233 | LEG-CORGI-US | US | US | 1 | $49.99 | $49.99 (refund) |
| SB-10240 | LEG-GSD-EU | EU | DE (VAT 19%) | 1 | €49.99 | 0 |
| SB-10241 | LEG-GSD-EU | EU | FR (VAT 20%) | 1 | €49.99 | 0 |
| SB-10242 | LEG-YOGA-EU | EU | IE (VAT 23%) | 1 | €49.99 | 0 |

- Tổng đơn hợp lệ: US 2 net (1 refund) + EU 3. Đơn EU đều ≤ €150 → **IOSS** (nhập từ ngoài EU). Tờ khai IOSS theo **tháng**.

## B. COGS — Printify/PrintBase invoice
| SKU | base print | shipping |
|---|---|---|
| LEG-GSD-US | $22.00 | $8.00 |
| LEG-CORGI-US | $22.00 | $8.00 |
| LEG-GSD-EU | €19.00 | €6.50 |
| LEG-YOGA-EU | €19.00 | €6.50 |

## C. Fee statements
- **ShopBase + gateway fee:** ~2.9% + $0.30 mỗi đơn.
- Ví dụ đơn $49.99 → fee ≈ $1.75 + $0.30 = ~$1.80 (đối chiếu kỳ vọng vs statement Stripe).
- Discrepancy mẫu: Meta billing lệch +$0.40 so kỳ vọng trên 1 charge → < $5 & < 2% → ghi log, không escalate.

## D. Ad spend (Facebook Ads billing — mọi BM)
| campaign | SKU/đợt | market | spend | đơn từ ads | platform ROAS (Ads Mgr) |
|---|---|---|---|---|---|
| CMP-GSD-US | LEG-GSD-US | US | $66.00 | 2 | 3.1 |
| CMP-GSD-EU | LEG-GSD-EU | EU | $58.00 | 1 | 2.0 |
| CMP-YOGA-EU | LEG-YOGA-EU | EU | $61.00 | 1 | 1.9 |

- **CPA US (GSD)** = $66 / 2 = $33/đơn. **CPA EU (GSD)** = $58/1 = $58. **CPA EU (YOGA)** = $61.
- Blended (true) ROAS tính = tổng revenue ShopBase net-of-refund / tổng ad spend (KHÔNG dùng platform ROAS ở cột trên — chỉ để đối chiếu hiệu chỉnh).

## E. Kết quả kỳ vọng (để chấm smoke-test)
- **LEG-GSD-US:** giá $49.99 − base $22 − ship $8 − fee $1.80 − CPA $33 − VAT $0 ⇒ profit ≈ **−$14.81/đơn** → **loser**, BE-ROAS ~2.75 > blended ⇒ `need_review: true`.
- **LEG-GSD-EU (DE 19%):** giá net = 49.99/1.19 ≈ €42.01; trừ base+ship+fee+CPA $58 ⇒ **âm sâu** → cờ **pricing EU** (nâng giá / provider rẻ / retention), BE-ROAS ~5.3, KHÔNG scale.
- **LEG-CORGI-US:** refund toàn bộ → revenue net 0, ghi contra-revenue, không tính winner.
- **P&L kỳ:** Net profit (USD) âm → × 25.450 ⇒ VND; brief nêu gap vs target 500tr/$20k + đề xuất kill US loser + EU pricing warning; `need_review: true` (net margin < 20%).
- **VAT:** IOSS draft theo nước đến (DE 19% / FR 20% / IE 23%), kỳ tháng; US note: chưa đạt nexus mới → reconcile only.
