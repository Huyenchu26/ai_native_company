# SOP-FUL-001 — Order Monitoring & Verification

**Dept:** 04-fulfillment-cx (ful) · **Layer:** L2 · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-fulfillment-order-ops` `[AI WORKFORCE]`
**Upstream:** 03-growth (đơn từ Facebook Ads → ShopBase checkout) · **Downstream:** SOP-FUL-002 (routing)

---

## 0. IPO (Input – Process – Output)
| | |
|---|---|
| **Input** | Đơn mới trên ShopBase (paid order), payment status, địa chỉ shipping US/EU, line items (SKU + variant size XS–3XL + color), risk/fraud flag |
| **Process** | Sync đơn → verify payment & address → flag ngoại lệ → đẩy đơn hợp lệ sang queue routing |
| **Output** | Verified order queue (sẵn route ≤24h) + Exception log (đơn cần xử lý tay) |

---

## 1. Tổng quan
ShopBase là source of truth cho đơn. Vì traffic 100% Facebook Ads → tỉ lệ đơn impulse/địa chỉ sai/fraud cao hơn organic. SOP này là **cổng đầu vào** của fulfillment: mọi đơn phải được verify trước khi tốn chi phí print. Mục tiêu: phát hiện ngoại lệ sớm, giữ on-time routing ≥98%. Cadence: quét đơn **mỗi 2h** trong giờ vận hành, sweep cuối ngày 23:00 ICT.

---

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Sync & quét đơn ShopBase | order-ops AI | OPC | — | — |
| Verify payment/address | order-ops AI | OPC | cx AI (nếu cần liên hệ khách) | — |
| Flag fraud/risk cao | order-ops AI | OPC | — | OPC |
| Quyết hold/cancel đơn fraud | OPC | OPC | order-ops AI | 05-backoffice |

`[AI WORKFORCE]` order-ops AI tự chạy verify rule-based; chỉ escalate OPC khi fraud-score cao hoặc giá trị đơn > $150.

---

## 3. Quy trình (ICOM)
**Bước 1 — Sync đơn (I:ShopBase orders · C:API/helpdesk · O:order list · M:order-ops AI)**
Pull paid orders mới mỗi 2h. Loại đơn `unpaid/pending/cancelled`.

**Bước 2 — Verify payment** Xác nhận `financial_status = paid` & không có chargeback flag. Đơn `authorized` chưa capture → hold.

**Bước 3 — Verify address** Check đủ trường (name, line1, city, ZIP/postcode, country US/EU). Chạy address-format check theo nước. Thiếu/sai format → nhánh 4.B.

**Bước 4 — Verify line items** SKU map đúng Printify product, variant size XS–3XL + color tồn tại. SKU không map được → nhánh 4.A.

**Bước 5 — Đẩy queue** Đơn pass toàn bộ → `verified queue` (input SOP-FUL-002), gắn timestamp để tính SLA ≤24h. Đơn fail → exception log + tag lý do.

---

## 4. Phân nhánh (Exception)
- **4.A SKU/variant lỗi (không map):** giữ đơn, báo 02-merchandising fix mapping; nếu OOS variant → cx AI liên hệ khách đổi size/refund.
- **4.B Địa chỉ sai/thiếu:** cx AI email khách xin địa chỉ đúng (template EN). Không phản hồi 48h → hold; 7 ngày → đề xuất refund (SOP-FUL-004).
- **4.C Nghi fraud (risk cao / nhiều đơn cùng card / mismatch billing-shipping):** hold, escalate OPC quyết trong 12h.
- **4.D Payment authorized chưa capture:** hold tối đa 24h chờ capture; quá hạn → cancel + notify khách.
- **4.E Đơn trùng (duplicate):** merge hoặc cancel bản trùng, notify khách.

---

## 5. Checklist — Quality Gate
**SLI / SLO**
> **2 tầng thời gian verification:** (1) **Verification target (SLO nội bộ) ≤4h** — mục tiêu chặt để đơn kịp route ≤18h/24h downstream; (2) **Hard-fail ceiling ≤24h** — không đơn paid nào được "rơi" quá 24h chưa verify (vượt = sự cố, RCA). Tầng (1) là mục tiêu thường nhật; tầng (2) là lằn ranh đỏ tuyệt đối.

| SLI | SLO (nội bộ, target) | Ceiling (hard-fail) | Đo |
|---|---|---|---|
| Order verification time | ≤ 4h từ lúc paid | ≤ 24h (vượt = hard-fail, RCA) | timestamp paid → verified |
| Verification coverage | 100% đơn paid quét trong ngày | — | quét/paid |
| Exception detection accuracy | ≥ 98% (ít false-pass) | — | audit mẫu hàng tuần |

**Prevention**
- [ ] Không có đơn paid nào "rơi" quá 24h chưa verify
- [ ] Mọi exception đều có tag lý do + owner
- [ ] Đơn fraud không bao giờ tự động route sang print
- [ ] Đối soát số đơn ShopBase = số đơn verified + exception (no leakage)

---

## 6. Tài nguyên & Links
- [ShopBase Helpdesk KB](../../_knowledge/README.md)
- Downstream: [SOP-FUL-002 Routing](../../route-fulfillment/template/sop_ful-002_fulfillment-routing_v1.0_2026-06-23.md)
- Exception → CX: [SOP-FUL-003](../../support-customer/template/sop_ful-003_cx-support_v1.0_2026-06-23.md)
- Rules: [_rules/README.md](../../_rules/README.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
