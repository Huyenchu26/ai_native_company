# Sample Campaign Input — test vibe-eu-opc-grw-fb-ads

> Input mẫu cho 1 đợt promote. Đặt ở `input/` để chạy `prompt/run-campaign-prompt.md`.

## Đợt / batch
- **Batch ID:** PROMOTE-2026-06-W4
- **SOP:** SOP-MER-006 (promote theo đợt) → SOP-GRW-002 (run-fb-ads)
- **Số SP đợt này:** 6 SP (subset của ~3.200 catalog)

## Live products (từ vibe-eu-opc-merch-*)
| SKU | Niche/breed | Market | Giá bán | Product page |
|-----|-------------|--------|---------|--------------|
| DAK-LEG-HUSKY-01 | Husky AOP legging | US | $49.99 | dakofits.com/p/husky-legging |
| DAK-LEG-CORGI-02 | Corgi AOP legging | US | $49.99 | dakofits.com/p/corgi-legging |
| DAK-LEG-YOGA-03 | Yoga mandala AOP legging | EU | €49.99 (VAT-incl) | dakofits.com/eu/p/yoga-mandala |

## Creative package (từ vibe-eu-opc-grw-creative)
- 3 video (hook 0–3s + body 360° + CTA) / SKU.
- 1 carousel 5-card / SKU.
- 2 static image variant / SKU.
- **Trạng thái:** ✔ đã giao, file print-safe.

## Meta Ad Policy clearance (từ 05-compliance)
- DAK-LEG-HUSKY-01: ✔ CLEARED (2026-06-22)
- DAK-LEG-CORGI-02: ✔ CLEARED (2026-06-22)
- DAK-LEG-YOGA-03: ⏳ PENDING (chưa có clearance) → **GATE: skill phải HOLD SKU này, không launch**

## Budget (duyệt bởi OPC + 05-finance)
- Test: $10/ad set/ngày.
- Tổng đợt: trần rủi ro ≈ $40 × số ad set; batch này 3 SP × 4 audience = 12 ad set ⇒ ~$480 (đã duyệt).
- Scale cap: $100/ngày/SKU. Escalate khi > $150/ngày.

## Targeting hint (từ 01-product-studio audience sizing)
- Husky: Interest "Siberian Husky" + Behavior "Engaged Shoppers" + LAL 2% purchasers.
- Corgi: Interest "Pembroke Welsh Corgi" + Custom Audience website visitors 30d.
- Yoga (EU): Interest "Yoga" + "Mindfulness" — **lưu ý BE-ROAS EU ~5.3, cảnh báo lãi ảo.**

## Kỳ vọng output
- Husky + Corgi: build ABO test ở T3, verify CAPI EMQ ≥ 6.
- Yoga EU: **HOLD** (thiếu policy clearance) + flag cảnh báo BE-ROAS 5.3.
- Mỗi SKU → 1 campaign-decision JSON theo schema, có evidence + confidence + need_review.
