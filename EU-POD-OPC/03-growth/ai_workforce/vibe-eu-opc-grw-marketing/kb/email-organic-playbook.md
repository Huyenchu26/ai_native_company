# KB — Email + Organic Playbook (DAKOfits)

Tài liệu tham chiếu cho `vibe-eu-opc-grw-marketing`. Bám SOP-GRW-003 (email) và SOP-GRW-001 (organic).

---

## A. 4 Klaviyo Flow

### 1. cart-abandon (thu hồi giỏ bỏ quên)
- **Trigger:** add-to-cart, no purchase tại 1h / 24h / 72h (3 mail).
- **Nội dung:** mail 1 nhắc nhẹ; mail 2 social proof (review/UGC niche); mail 3 mã giảm nhẹ + urgency thật.
- **KPI:** cart-recovery rate ≥ 10%.

### 2. upsell (post-purchase)
- **Trigger:** order placed.
- **Nội dung:** cảm ơn → cross-sell bundle / sports-bra cùng niche → review request.
- **Mục tiêu:** tăng AOV & LTV, gom review làm social proof.

### 3. win-back
- **Trigger:** no purchase 60–90 ngày.
- **Nội dung:** "we miss you" + best-seller theo niche khách từng mua + offer kéo lại.

### 4. seasonal
- **Trigger:** calendar date (seasonal opportunity từ niche-research).
- **Nội dung:** drop theo mùa/niche, urgency thật, không fake scarcity.

> Mọi flow: A/B subject, frequency cap bật, gửi theo timezone US/EU, track revenue-per-email.

---

## B. Opt-in rule (HARD GATE)
- Chỉ gửi subscriber có **explicit consent** (double opt-in ưu tiên).
- Loại: unsubscribed, hard-bounced, không-consent.
- No consent → **EXCLUDE, không gửi**. Đây là gate 0-tolerance (consent compliance = 100%).
- Tách segment **EU** (GDPR) vs **US** (CAN-SPAM) theo thị trường người nhận.

---

## C. GDPR checklist (EU)
- [ ] Consent được log (nguồn + thời điểm).
- [ ] Honor right-to-erasure: nhận request → xóa + log, phối 05-compliance.
- [ ] Không scrape / lưu data cá nhân ngoài phạm vi consent.

## D. CAN-SPAM checklist (US)
- [ ] Sender identity thật (không giả mạo From/Reply-To).
- [ ] Địa chỉ vật lý hợp lệ trong mọi mail.
- [ ] Unsubscribe rõ ràng, xử lý ≤ 10 ngày.
- [ ] Subject không lừa đảo / không gây hiểu nhầm.

> Deliverability ≥ 98%, spam complaint < 0.1% (hard cap). Spam > 0.1% → PAUSE flow, clean list, giảm frequency. Deliverability < 98% → fix SPF/DKIM/DMARC.

---

## E. Organic community rule
- Đọc **rule từng group/community trước khi seed**; xin phép admin nếu cần.
- **Không spam link**; mix content value (không bán cứng).
- Cadence đúng lịch ≥ 90%; community-rule compliance 100% (0 ban).
- Bị flag → gỡ/sửa, xin lỗi admin, dừng kịp.

## F. UGC consent
- [ ] Xin consent rõ ràng trước khi repost/seed UGC của người dùng.
- [ ] UGC chất lượng cao → đề xuất `vibe-eu-opc-grw-creative` đưa vào ad/page (vẫn cần consent).
- [ ] Lưu bằng chứng consent vào evidence[].

---

## G. Escalation
| Điều kiện | Hành động |
|----------|-----------|
| Không consent | EXCLUDE — không gửi |
| GDPR erasure request | xóa + log (05-compliance) |
| Spam > 0.1% | PAUSE flow |
| Discount ăn mòn margin | escalate OPC / 05-finance |
| Community flag / negative PR | escalate OPC + 04-CX |
| Tên niche rủi ro IP | flag 05-compliance |
