# Pricing Playbook — mer-catalog (DAKOfits US blankets)

Canonical: [../../../../_shared/unit-economics.md](../../../../_shared/unit-economics.md).

## Contribution (US, no VAT)
gross_before_ads = sell − base_cost − ship − (gateway_fee + return_reserve)
contribution_% = (gross_before_ads − allocated_cpa) / sell   → floor ≥ 15%
BE-ROAS = sell / gross_before_ads  (per-SKU, KHÔNG hard-code)

## Price band & AOV
Chăn $39.95–59.95. Ưu tiên $59.95 (free-ship threshold + BE-ROAS thấp). Bundle 2 chăn / chăn+phụ kiện để >$59.

## cost_basis
- quote = supplier thật → được chốt giá production.
- assumption = unit-economics giả định → BẮT BUỘC need_review=true, KHÔNG production.

## Go-live gate (MER-004)
live CHỈ khi 3 gate: pricing_floor_pass ∧ images_on_disk ∧ product_page_publish_ready.
