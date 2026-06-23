# Sample Ticket Input — DAKOfits CX

Dữ liệu giả lập cho test/dev. KHÔNG phải khách thật.

## Ticket A — Defect refund (>$30 → escalate)
```json
{
  "ticket_id": "DK-T-2026-0623-A",
  "channel": "ShopBase helpdesk",
  "language": "EN",
  "message": "Hi, my Husky AOP leggings arrived with the print cracked across the waistband and the seam is split. Really disappointed. I'd like a full refund please. Order #DK-1075, I paid $45.",
  "order_context": {
    "order_ref": "DK-1075",
    "sku": "AOP-LEG-HUSKY-M",
    "item_value_usd": 45,
    "market": "EU-DE",
    "production_status": "delivered",
    "tracking": "DHL-EU-99213847 (delivered 2026-06-19)"
  },
  "evidence": ["photo_print_crack.jpg", "photo_seam_split.jpg"]
}
```
**Expected resolution:** `type=defect`, ưu tiên `resolution=reprint`; nếu khách từ chối → `refund`,
`refund_amount=45`, **`refund_auto_approved=false`**, **`need_review=true`** (>$30 → escalate OPC).
EU Art.16(c) KHÔNG áp dụng (defect → conformity rights bắt buộc refund/reprint). Evidence = 2 ảnh.

## Ticket B — Size exchange (XS–3XL, refund=0)
```json
{
  "ticket_id": "DK-T-2026-0623-B",
  "channel": "email",
  "language": "EN",
  "message": "Love the design but the leggings are too tight on the waist. I usually wear size M in activewear. Can I exchange for a larger size? Order #DK-1050.",
  "order_context": {
    "order_ref": "DK-1050",
    "sku": "AOP-LEG-CORGI-M",
    "item_value_usd": 32,
    "market": "US-CA",
    "production_status": "delivered",
    "size_chart": "XS, S, M, L, XL, 2XL, 3XL"
  },
  "evidence": []
}
```
**Expected resolution:** `type=size`, `resolution=exchange` → đề xuất size L theo chart XS–3XL,
tạo replacement order (free first exchange), khách giữ hàng cũ (POD không thu hồi), bàn giao
order-ops re-route. `refund_amount=0`, `refund_auto_approved=true` (n/a), `need_review=false`,
`first_response_h≤2`. Evidence = order ref + size-chart áp dụng.
