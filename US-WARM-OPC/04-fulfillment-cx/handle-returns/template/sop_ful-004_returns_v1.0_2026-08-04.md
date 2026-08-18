# SOP-FUL-004 — Returns & Refunds (US, personalized)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 04-Fulfillment-CX · **Responsible AI:** `vibe-us-warm-ful-cx`
**Delta vs EU:** US return-law (KHÔNG có 14-day withdrawal EU). Personalized = **final-sale** trừ lỗi sản xuất/không đúng mô tả.

## 1. Mục tiêu
Xử lý return/refund đúng luật US + công bằng: sản phẩm cá nhân hoá là **final-sale**, NHƯNG defect/không-đúng-mô-tả → refund/replace (nghĩa vụ thật, không né như đối thủ).

## 2. IPO/ICOM
- **Input:** yêu cầu return (lý do), order, QC record.
- **Control:** personalized → final-sale; defect/not-as-described → refund/replace bất kể; refund > $30 → human; FTC Mail Order Rule.
- **Output:** `return-resolution.json` (schema `return-resolution.schema.json`).

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Phân loại lý do | defect/not-as-described vs "đổi ý" |
| 3.2 | Defect/not-as-described | refund/replace — nghĩa vụ (dùng QC photo đối chiếu) |
| 3.3 | "Đổi ý" trên personalized | final-sale (có disclosure lúc mua) — từ chối lịch sự |
| 3.4 | Refund | > $30 → human approve; auto ≤ $30 nếu defect rõ |

## 4. RACI
R: ful-cx · A: Owner · C: bck-finance (refund), ful-order-ops (QC record) · I: —.
HITL: refund > $30; tranh chấp defect.

## 5. Gate (allOf/if-then)
refund_auto_approved=true ⇒ refund_amount ≤ 30 ∧ reason=defect. final_sale_applies=true ⇒ reason=changed-mind ∧ personalized=true. Defect luôn được refund/replace (không final-sale).

## 6. Links
Upstream: [monitor-orders](../../monitor-orders/template/sop_ful-001_order-monitoring_v1.0_2026-08-04.md). Compliance: bck-compliance (FTC). 

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — US final-sale cho personalized + nghĩa vụ defect; refund>$30 human. |
