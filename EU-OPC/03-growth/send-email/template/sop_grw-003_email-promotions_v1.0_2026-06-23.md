# SOP-GRW-003 — Email & Promotions (Klaviyo) `[AI WORKFORCE]`

**Phòng:** 03-growth (grw) · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** 03-growth · **Responsible AI Worker:** `vibe-opc-pod-growth-marketing`
**Folder:** `send-email/`

> GATE: **Chỉ gửi cho opt-in subscribers (GDPR).** No consent → no email. Mọi mail có unsubscribe + sender identity hợp lệ.

---

## 0. IPO

| Thành phần | Chi tiết |
|-----------|----------|
| **Input** | Opt-in list (ShopBase ↔ Klaviyo); đơn hàng + cart event; seasonal calendar (01); offer từ 02-merchandising |
| **Process** | Segment opt-in → build flow (cart-abandon / post-purchase upsell / win-back / seasonal) → send → đo deliverability/revenue |
| **Control** | GDPR consent, deliverability ≥ 98%, spam < 0.1%, frequency cap |
| **Output** | Email campaigns đã gửi + revenue-per-email; cost (→ 05); signal (→ SOP-GRW-004) |
| **Mechanism** | Klaviyo, ShopBase, vibe-opc-pod-growth-marketing |

---

## 1. Tổng quan

Email là kênh **owned, biên lợi nhuận cao** bổ trợ FB Ads (FB kéo khách mới, email tăng LTV & thu hồi đơn rớt). Mục tiêu: tăng repeat-purchase & AOV mà không tốn ad spend, đóng góp O1. Tuân thủ **GDPR (opt-in only)** vì có khách EU.

4 flow lõi:
1. **Cart abandonment** — thu hồi giỏ bỏ quên.
2. **Post-purchase upsell** — bán thêm sports-bra/bundle sau mua.
3. **Win-back** — kéo khách ngủ đông quay lại.
4. **Seasonal/promotions** — chiến dịch theo mùa/niche.

---

## 2. RACI + AI Roles

| Hoạt động | R | A | C | I |
|----------|---|---|---|---|
| Segment & consent check | `marketing` (AI) | OPC | 05-compliance (GDPR) | — |
| Build flow & copy | `marketing` (AI) | OPC | `fb-creative` (asset) | — |
| Offer/discount duyệt | OPC | OPC | 05-finance (margin) | `marketing` |
| Send & monitor | `marketing` (AI) | OPC | — | `fb-ads` |

**AI Role:** `vibe-opc-pod-growth-marketing` xây + vận hành Klaviyo flow, bảo đảm chỉ gửi opt-in, theo dõi deliverability; escalate khi spam-rate cao hoặc cần duyệt discount sâu.

---

## 3. Quy trình (ICOM, 4 bước)

### Bước 1 — Segment opt-in (GDPR) `[Control]`
- Chỉ kéo subscriber có **explicit consent** (double opt-in ưu tiên). Loại unsubscribed/bounced.
- Tách EU vs US; **EU áp GDPR** (consent log, right-to-erasure honor); **US áp CAN-SPAM** (sender identity thật + địa chỉ vật lý hợp lệ trong mọi mail, unsubscribe xử lý ≤ 10 ngày, không subject lừa đảo). Hai khung song song theo thị trường người nhận.

### Bước 2 — Build flow lõi `[Process]`
| Flow | Trigger | Nội dung |
|------|---------|----------|
| Cart abandon | add-to-cart, no purchase 1h/24h/72h | nhắc + social proof + (mã nhẹ ở mail 3) |
| Post-purchase upsell | order placed | cảm ơn → cross-sell bundle/sports-bra → review request |
| Win-back | no purchase 60–90 ngày | "we miss you" + best-seller niche + offer |
| Seasonal | calendar date | drop theo mùa/niche, urgency thật |

### Bước 3 — Send & frequency cap `[Process]`
- Frequency cap để tránh fatigue/spam complaint.
- A/B subject line; gửi giờ tối ưu theo timezone US/EU.

### Bước 4 — Đo & feed report `[Output]`
- Track open / click / **revenue-per-email** / placed-order rate; deliverability + spam rate.
- Feed số liệu → SOP-GRW-004; cost → 05.

---

## 4. Phân nhánh

| Điều kiện | Hành động |
|----------|-----------|
| Subscriber không có consent | **EXCLUDE** — không gửi |
| GDPR erasure request | xóa + log (phối 05-compliance) |
| Spam complaint > 0.1% | **PAUSE** flow, làm sạch list, giảm frequency |
| Deliverability < 98% | warm-up lại, sửa authentication (SPF/DKIM/DMARC) |
| Discount ăn mòn margin | escalate OPC/05-finance |

---

## 5. Checklist + Quality Gate (SLI/SLO + Prevention)

- [ ] Chỉ opt-in, có unsubscribe + sender hợp lệ
- [ ] EU segment tuân GDPR
- [ ] Frequency cap bật
- [ ] Offer trong khung margin
- [ ] Tracking revenue-per-email

| SLI | SLO | Error budget |
|-----|-----|--------------|
| Email deliverability | ≥ 98% | ≤ 2% |
| Spam complaint rate | < 0.1% | hard cap |
| Consent compliance | 100% opt-in | 0 tolerance |
| Cart-recovery rate | ≥ 10% | — |
| Revenue-per-email | tracked; khởi điểm gợi ý **≥ $0.30** (baseline + chốt sau 30 ngày) | — |

> **Cơ chế baseline:** SLI chưa có số chuẩn (vd revenue-per-email) → **baseline = 30 ngày đầu vận hành**, review & chốt ngưỡng chính thức sau đó. $0.30 là placeholder khởi điểm, KHÔNG phải số đã chốt.

**Prevention:** double opt-in; consent log; frequency cap; SPF/DKIM/DMARC; list hygiene định kỳ.

---

## 6. Tài nguyên + Links
- Folder: `send-email/`
- GDPR: 05-backoffice/compliance · Report: [SOP-GRW-004](../../report-growth/template/sop_grw-004_growth-report_v1.0_2026-06-23.md)
- Organic: [SOP-GRW-001](../../post-organic/template/sop_grw-001_organic-social_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

---

## 7. Lịch sử
| Version | Ngày | Thay đổi | Người |
|---------|------|----------|-------|
| v1.0 | 2026-06-23 | Khởi tạo SOP email Klaviyo (4 flow, GDPR opt-in) | Company Architect |
| v1.1 | 2026-06-23 | Thêm cơ chế baseline 30 ngày + khởi điểm revenue-per-email ≥ $0.30; thêm CAN-SPAM (US) song song GDPR (EU) | 03-growth |
