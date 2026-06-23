# Sample Input — Email Campaign (cart-abandon)

Input mẫu để test/demo `vibe-eu-opc-grw-marketing`. KHÔNG chứa data cá nhân thật (đã anonymize).

## Task
Tạo **cart-abandon flow** cho segment opt-in niche "German Shepherd AOP Leggings".

## Segment (opt-in)
- **Tên:** `seg_optin_cart_de-shepherd_2026-06`
- **audience_optin:** true (double opt-in, consent logged)
- **Thị trường:** EU (Đức, Pháp) → áp **GDPR** + US (một phần) → áp **CAN-SPAM**
- **Số subscriber:** ~480 (đã loại unsubscribed/bounced)
- **Trigger:** add-to-cart, no purchase tại 1h / 24h / 72h

## Promo offer
- Mail 1 (1h): nhắc nhẹ, không mã.
- Mail 2 (24h): social proof — 3 review UGC niche German Shepherd.
- Mail 3 (72h): mã **WELCOME10** (-10%), urgency thật (hết hạn 48h).
- **Margin check:** -10% còn trong khung margin 45–55% → OK (không cần escalate finance).

## Sản phẩm / bundle
- SP chính: German Shepherd AOP Leggings (XS–3XL).
- Cross-sell: matching sports-bra cùng print.

## Calendar context
- Không seasonal; flow always-on cart-recovery.

## Expected output
- 1 campaign JSON hợp lệ `schema/email-campaign.schema.json`:
  `flow_type=cart-abandon`, `audience_optin=true`, compliance_check đầy đủ GDPR+CAN-SPAM,
  evidence[] ≥ 1, confidence_score ≥ 0.7, need_review=false.
