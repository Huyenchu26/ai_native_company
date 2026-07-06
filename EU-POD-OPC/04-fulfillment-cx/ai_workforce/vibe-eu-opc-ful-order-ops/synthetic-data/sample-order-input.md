# Synthetic Data — Sample Order Input (1 US + 1 EU)

Dữ liệu giả lập (ẩn danh) cho smoke-test. KHÔNG dùng PII thật.

## Đơn A — US (PASS, expected route US provider)
```json
{
  "order_id": "DKO-US-100245",
  "financial_status": "paid",
  "billing_country": "US",
  "shipping_address": {
    "name": "Jordan Miller",
    "line1": "742 Evergreen Terrace",
    "city": "Springfield",
    "zip": "62704",
    "country": "US"
  },
  "line_items": [
    { "sku": "DKO-LEG-CORGI-001", "variant_size": "L", "color": "Black" }
  ],
  "risk_score": 0.08,
  "order_value": 39.90,
  "paid_at": "2026-06-23T02:10:00Z",
  "fulfillment_status": "unfulfilled",
  "tracking_number": null,
  "carrier": null
}
```
**Expected:** market=US, provider=US, verify_status=PASS, exception_tag=NONE, route ≤18h, need_review=false.

## Đơn B — EU (HOLD address, expected exception)
```json
{
  "order_id": "DKO-EU-100246",
  "financial_status": "paid",
  "billing_country": "DE",
  "shipping_address": {
    "name": "Lena Schäfer",
    "line1": "Hauptstrasse 12",
    "city": "",
    "zip": "",
    "country": "DE"
  },
  "line_items": [
    { "sku": "DKO-LEG-ZODIAC-LEO-007", "variant_size": "2XL", "color": "Navy" }
  ],
  "risk_score": 0.12,
  "order_value": 42.50,
  "paid_at": "2026-06-23T05:40:00Z",
  "fulfillment_status": "unfulfilled",
  "tracking_number": null,
  "carrier": null
}
```
**Expected:** market=EU, provider=EU (sau khi fix), verify_status=HOLD, exception_tag=ADDRESS_INVALID (thiếu city + zip), need_review=true → handoff cx xin địa chỉ.

## (Tham chiếu) Đơn C — EU fulfilled, expected send-tracking
```json
{
  "order_id": "DKO-EU-100240",
  "financial_status": "paid",
  "shipping_address": { "name": "Marco Rossi", "line1": "Via Roma 9", "city": "Milano", "zip": "20121", "country": "IT" },
  "line_items": [{ "sku": "DKO-LEG-CAT-RAGDOLL-003", "variant_size": "M", "color": "Maroon" }],
  "risk_score": 0.05, "order_value": 41.00,
  "paid_at": "2026-06-22T08:00:00Z",
  "fulfillment_status": "fulfilled",
  "tracking_number": "JD0123456789DE", "carrier": "DHL"
}
```
**Expected:** verify=PASS, provider=EU, tracking_sent=true (email EN ≤6h sau fulfilled), cost_pushed_backoffice=true, need_review=false.
