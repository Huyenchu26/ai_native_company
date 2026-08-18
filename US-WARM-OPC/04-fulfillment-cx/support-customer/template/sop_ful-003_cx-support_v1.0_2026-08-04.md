# SOP-FUL-003 — Customer Support (US, real CX)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 04-Fulfillment-CX · **Responsible AI:** `vibe-us-warm-ful-cx`
**Differentiator:** CX người thật, first-response ≤ 4h (đối thủ bị tố "không có người thật").

## 1. Mục tiêu
Trả lời khách nhanh, thật, hữu ích. AI draft → nhưng escalate rõ khi cần người; KHÔNG auto-reply rỗng.

## 2. IPO
- Input: ticket khách (email/chat).
- Control: first-response ≤ 4h giờ hành chính US; resolution rate; no empty auto-reply; personalization/return câu hỏi → đúng SOP.
- Output: `ticket-resolution.json` (schema `ticket-resolution.schema.json`).

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Phân loại ticket | order status / return / personalization / complaint |
| 3.2 | Draft reply | thật, cá nhân hoá; no empty template |
| 3.3 | Escalate | refund>$30, defect dispute, t*angry* → human ≤ SLA |

## 4. RACI: R ful-cx · A Owner · C ful-order-ops (status), bck-compliance · I —.

## 5. Gate: auto_resolved=true ⇒ category≠refund-over-30 ∧ category≠defect-dispute. first_response ≤ 4h SLA.

## 6. Links: [returns](../../handle-returns/template/sop_ful-004_returns_v1.0_2026-08-04.md).

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — real-CX SLA ≤4h, no empty auto-reply. |
