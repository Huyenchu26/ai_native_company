# Synthetic Data — Sample Batch Input (1 đợt promote)

Batch mẫu do 02-merchandising bàn giao (SOP-MER-006) cho orchestrator điều phối. Dữ liệu giả lập, không phải SP thật.

---

## Batch metadata
- **batch_id:** `BATCH-2026-06-W26-001`
- **source_sop:** SOP-MER-006
- **market:** US+EU
- **handoff từ:** `vibe-opc-pod-merch-catalog-sync` (02-merchandising)
- **ngày:** 2026-06-23
- **budget cap đã duyệt:** $90/ngày tổng đợt (escalate khi > $150/ngày)

## Products (6 SP — live, có product page)

| # | SKU | Niche | Market | Price | BE-ROAS (unit-economics) | Meta Policy clearance |
|---|-----|-------|--------|-------|--------------------------|-----------------------|
| 1 | US-BULLDOG-001 | French Bulldog mom | US | $39.99 | 2.75 | pass |
| 2 | US-CORGI-002 | Corgi lover | US | $39.99 | 2.75 | pass |
| 3 | EU-CORGI-003 | Corgi lover | EU | €49.99 | 5.30 | pass |
| 4 | US-GSHEP-004 | German Shepherd | US | $42.99 | 2.70 | pending ← gate #1 chưa pass |
| 5 | US-YOGA-CAT-005 | Yoga cat mandala | US | $39.99 | 2.75 | pass |
| 6 | EU-DACHS-006 | Dachshund | EU | €49.99 | 5.30 | pass |

## Opt-in email (bổ trợ, GDPR/CAN-SPAM)
- post-purchase list: opt-in = **true** (consent qua checkout) → đủ điều kiện email winner.
- cold list mua ngoài: opt-in = **false** → **BLOCK** email.

## Kỳ vọng điều phối (để đối chiếu test)
- SP #1,2,3,5,6 → ROUTE creative → fb-ads ABO test.
- SP #4 (clearance `pending`) → **HOLD** ở gate #1, trả về compliance, KHÔNG launch.
- Sau test: SP EU (#3,#6) áp BE-ROAS 5.3 — nếu Blended < 5.3 ⇒ HOLD (lãi ảo), KHÔNG dùng 2.5.
- Email chỉ gửi post-purchase list (opt-in true); cold list BLOCK.
- Nếu tổng spend leo > $150/ngày ⇒ escalate OPC + 05-finance.
