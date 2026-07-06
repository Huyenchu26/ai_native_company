# _knowledge — Fulfillment & CX

**Dept:** 04-fulfillment-cx · **Ngày:** 2026-06-23
Knowledge base cho order-ops AI + cx AI. (K trong KWSR)

---

## 1. ShopBase Helpdesk & Order Ops
- ShopBase order lifecycle: `paid → verified → routed → in-production → fulfilled → delivered`.
- Financial status: `paid / authorized / pending / refunded / partially_refunded`.
- Helpdesk channels: email, ShopBase helpdesk inbox, FB inbox. Macro/template EN library.
- Address format theo nước (US ZIP 5/9, EU postcode formats), required fields.

## 2. Printify / PrintBase Routing
- **Provider mapping theo vùng:** US khách → US provider; EU khách → EU provider (giảm ship time, tránh customs/VAT).
- Production time chuẩn: US ~2–5 ngày, EU ~2–5 ngày; ship time tùy carrier.
- Variant catalog: size XS–3XL × color cho AOP leggings & activewear.
- Print file spec, reprint policy (defect/lỗi print = free reprint), invoice → cost data.

## 3. Size Chart XS–3XL (CX)
- Bảng size đầy đủ XS–3XL (waist/hip/inseam) cho AOP legging — căn cứ tư vấn fit & size exchange.
- AOP legging fit notes: chạy form, hướng dẫn chọn size khi giữa 2 mức.
- Size exchange policy: free first exchange, không thu hồi hàng cũ (POD).

## 4. GDPR & Data Handling
- Data minimization: chỉ truy cập order data cần để xử ticket.
- Quyền khách EU: access, rectification, erasure, portability — đáp ứng ≤30 ngày (SLO 20 ngày).
- Không xóa data có nghĩa vụ lưu (kế toán/VAT) → phối 05-backoffice compliance (SOP-BCK-005).
- Không share data khách giữa các ticket/khách khác.

## 5. Policy refs
- Returns/refund policy + authority threshold → [_rules](../_rules/README.md)
- Meta/ShopBase ToS, EU consumer withdrawal right.

> Cập nhật: khi đổi provider, đổi size chart, thay đổi policy refund/GDPR → bump version + log.
