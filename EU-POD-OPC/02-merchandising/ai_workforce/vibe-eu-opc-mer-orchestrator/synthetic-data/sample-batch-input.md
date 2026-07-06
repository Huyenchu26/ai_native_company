# Sample Batch Input — 1 đợt promote (5–10 cleared design)

Dữ liệu mẫu để chạy `prompt/run-batch-prompt.md` / `test/smoke-test.md`. Nguồn: cleared design từ `vibe-opc-pod-product-design` (Product Studio) + GPSR clearance từ phòng 05.

---

## Batch meta
- **batch_id:** MER006-2026-W26-01
- **Ngày tạo:** 2026-06-23
- **Nguồn design:** vibe-opc-pod-product-design (300 DPI, 360° QC pass, IP cleared)
- **Mục tiêu:** tối ưu listing → handoff `vibe-eu-opc-grw-orchestrator` chạy FB Ads (SOP-GRW-002)

## Products (6 SP)

| # | sku | title | niche | market | giá dự kiến | provider cost (base+ship+fee) | GPSR clearance (EU) |
|---|-----|-------|-------|--------|------------|-------------------------------|---------------------|
| 1 | DKF-LEG-BEA-001 | Beagle Mom AOP Legging | Beagle (dog) | US+EU | US $49.99 / EU €59.99 | $31.80 | ✅ CLR-EU-0612 |
| 2 | DKF-LEG-HUS-002 | Husky Lover All-Over Legging | Husky (dog) | US+EU | US $49.99 / EU €59.99 | $31.80 | ✅ CLR-EU-0613 |
| 3 | DKF-LEG-COR-003 | Corgi Butt Funny Legging | Corgi (dog) | US | $49.99 | $31.80 | n/a (US only) |
| 4 | DKF-LEG-YOG-004 | Yoga Mandala Activewear Legging | Yoga/mandala | US+EU | US $52.99 / EU €64.99 | $32.50 | ✅ CLR-EU-0614 |
| 5 | DKF-LEG-CAT-005 | Cat Mom Watercolor Legging | Cat | EU | €59.99 | $31.80 | ⚠️ PENDING (chưa cleared) |
| 6 | DKF-LEG-HOR-006 | Horse Lover Tile Legging | Horse | US | $49.99 | $31.80 | n/a (US only) |

## Ghi chú điều phối (kỳ vọng manager xử lý)
- **SP #5 (Cat, EU, GPSR PENDING):** gate GPSR fail → **block publish + escalate phòng 05** → loại khỏi handoff đợt này (`need_review=true` cho SP này). Đợt còn 5 SP đủ điều kiện.
- **Giá EU €59.99:** đã nâng so với €49.99 (theo cảnh báo `unit-economics.md`: EU giá thấp gần như không lãi qua cold-ads). Manager kiểm contribution margin sau ads + VAT IOSS để xác nhận CM dương.
- **Pricing:** route `vibe-eu-opc-mer-catalog` set variant XS–3XL/color trong band 45–55% gross.
- **Page:** route `vibe-eu-opc-mer-product-page` viết copy + upsell sports-bra + GPSR label cho SP EU.
- **be_roas:** tính per-SKU/market (1/GM) trước handoff để Growth dùng làm ngưỡng winner thật (không dùng 2.5 cứng).

## Kỳ vọng output
`merch-batch-plan` với 5 SP pass gate → `handoff_to_growth=true` → `vibe-eu-opc-grw-orchestrator`; SP #5 ở review queue chờ GPSR.
