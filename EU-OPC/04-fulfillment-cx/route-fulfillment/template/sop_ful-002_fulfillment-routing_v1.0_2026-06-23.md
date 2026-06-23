# SOP-FUL-002 — Fulfillment Routing & Tracking

**Dept:** 04-fulfillment-cx (ful) · **Layer:** L2 · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-fulfillment-order-ops` `[AI WORKFORCE]`
**Upstream:** SOP-FUL-001 (verified queue) · **Downstream:** SOP-FUL-003 (CX), 05-backoffice (cost data)

> ⭐ SOP lõi của on-time KPI: **route Printify SLO ≤18h** (ceiling/SLA ≤24h) + **gửi tracking SLO ≤6h sau ship**.

---

## 0. IPO
| | |
|---|---|
| **Input** | Verified order queue (từ SOP-FUL-001), variant→provider mapping (Printify/PrintBase US+EU) |
| **Process** | Chọn provider tối ưu → submit order Printify ≤24h → theo dõi production → fetch tracking → gửi tracking khách |
| **Output** | Orders in production + tracking gửi khách (email/ShopBase fulfillment) + cost data → 05-backoffice |

---

## 1. Tổng quan
Route đơn đã verify sang print provider — **SLO nội bộ ≤18h** kể từ lúc paid (SLA khách ≤24h, ceiling hard-fail ≤24h với error budget chạy tới 24h). Phân biệt: SLO 18h là mục tiêu nội bộ chặt để giữ buffer/cảnh báo sớm; 24h là cam kết ngoài + mốc hard-fail. KPI on-time routing ≥98% đo theo SLO 18h. Chọn provider theo nước khách: **US khách → US provider, EU khách → EU provider** (giảm ship time + tránh VAT/customs). Sau khi provider ship, fetch tracking number và gửi khách trong **SLO ≤6h** sau ship để giảm WISMO ticket. Cadence routing: theo batch mỗi 2–4h.

---

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Chọn provider (US/EU) | order-ops AI | OPC | 02-merchandising | — |
| Submit order Printify ≤24h | order-ops AI | OPC | — | — |
| Theo dõi production status | order-ops AI | OPC | — | — |
| Fetch & gửi tracking | order-ops AI | OPC | cx AI | khách |
| Xử lý production fail/delay | order-ops AI | OPC | provider support | OPC |

`[AI WORKFORCE]` order-ops AI tự route + tự gửi tracking; escalate OPC khi provider reject/OOS/delay > SLA.

---

## 3. Quy trình (ICOM)
**Bước 1 — Chọn provider (I:verified order + ship country · C:provider routing rule · O:provider chọn · M:order-ops AI)**
US khách → US provider; EU khách → EU provider. Variant size XS–3XL phải có ở provider đó.

**Bước 2 — Submit Printify ≤24h** Tạo order trên Printify/PrintBase với print file + variant + shipping. **Hard SLA: hoàn tất ≤24h từ paid.** Ghi `routed_at` timestamp.

**Bước 3 — Theo dõi production** Poll trạng thái: `in-production → fulfilled`. Production trễ chuẩn (US ~2–5d, EU ~2–5d) → nhánh 4.C.

**Bước 4 — Fetch tracking & gửi khách** Khi provider ship → lấy tracking number + carrier. Cập nhật ShopBase fulfillment + **gửi email tracking EN** cho khách. Ghi `tracking_sent_at`.

**Bước 5 — Đẩy cost data** Đẩy print cost + ship cost từ provider invoice → 05-backoffice (profit-per-SKU).

---

## 4. Phân nhánh (Exception)
- **4.A Provider reject / variant OOS:** thử provider thay thế cùng vùng; không có → cx AI báo khách đổi size/màu hoặc refund (SOP-FUL-004).
- **4.B Quá SLA 24h chưa route:** auto-alert OPC + ưu tiên đẩy ngay; log lý do để chấm error budget.
- **4.C Production chậm (> ngưỡng provider):** cx AI proactive email khách báo delay + ETA mới; cân nhắc reprint hoặc đổi provider.
- **4.D Lỗi production/print defect (provider báo):** request reprint miễn phí từ provider; cx AI báo khách ETA.
- **4.E Tracking không cập nhật / lost in transit:** mở case với carrier; sau ngưỡng → reship hoặc refund.

---

## 5. Checklist — Quality Gate
**SLI / SLO**
> **SLO (nội bộ, chặt) vs SLA/ceiling (ngoài, lỏng):** SLO là mục tiêu nội bộ siết hơn cam kết ngoài để giữ buffer/error budget; SLA là cam kết với khách; ceiling là mốc hard-fail tối đa được phép. Đồng bộ với `quality_ful-001`.

| SLI | SLO (nội bộ, chặt) | SLA (external khách) / Ceiling | Đo |
|---|---|---|---|
| On-time routing | ≥ 98% đơn route **≤18h** | SLA khách ≤24h; ceiling hard-fail ≤24h (error budget tới 24h) | routed_at − paid_at |
| Routing time (avg) | ≤ 12h | — | trung bình routed_at − paid_at |
| Tracking gửi sau ship | 100% **≤6h** sau ship | tracking trong 5 ngày | tracking_sent_at − fulfilled_at |
| Provider match đúng vùng | ≥ 99% | — | US→US, EU→EU |

**Error budget:** SLO nội bộ ≤18h; budget chạy từ 18h tới ceiling 24h. Đơn route > **24h** (vượt ceiling/SLA) = hard-fail → RCA bắt buộc. Tỉ lệ vượt SLO 18h được theo dõi để cảnh báo sớm trước khi chạm ceiling.

**Prevention**
- [ ] Mọi đơn verified có `routed_at` trong 24h
- [ ] Provider chọn đúng vùng khách (no cross-region trừ OOS)
- [ ] Không đơn nào "ship" mà chưa gửi tracking khách
- [ ] Cost data mọi đơn đã đẩy 05-backoffice

---

## 6. Tài nguyên & Links
- Upstream: [SOP-FUL-001](../../monitor-orders/template/sop_ful-001_order-monitoring_v1.0_2026-06-23.md)
- [Printify routing KB](../../_knowledge/README.md) · [Rules — route ≤24h SLA](../../_rules/README.md)
- CX exception: [SOP-FUL-003](../../support-customer/template/sop_ful-003_cx-support_v1.0_2026-06-23.md) · [SOP-FUL-004](../../handle-returns/template/sop_ful-004_returns-refunds_v1.0_2026-06-23.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
