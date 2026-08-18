# Unit Economics — US-WARM-OPC (canonical source of truth)

**Phiên bản:** 1.0 · **Ngày:** 2026-08-04 · **Đơn vị:** USD · **Thị trường:** US

> ⚠️ **Mọi con số cost/ship dưới đây là GIẢ ĐỊNH khởi tạo** (chưa có quote supplier thật). Trước khi commit pricing/ad target, phải thay bằng quote thật từ supplier chăn US (Printful/Printify US/blanket dropship). Field nào chưa có số thật → đánh dấu `ASSUMPTION`.

---

## 1. Nguyên tắc (học từ EU pipeline test)

- **KHÔNG dùng công thức gross ảo** `giá = cost/(1−margin)` → sinh "margin ảo", có thể contribution âm.
- Quyết định pricing & ad dựa trên **Contribution margin sau ads + fee** và **Break-even ROAS per-SKU**.
- **US KHÔNG có VAT** → khác EU: không trừ VAT khỏi doanh thu. Nhưng có **sales tax** (thu hộ, nộp bang — KHÔNG phải doanh thu/chi phí của mình, xử lý ở backoffice, không tính vào contribution).
- Free-ship ngưỡng >$59 → chi phí ship khách <$59 do mình chịu → phải nằm trong contribution.

## 2. Cost stack — Chăn cá nhân hoá (P0) — ASSUMPTION

| Thành phần | Giả định | Ghi chú |
|-----------|----------|---------|
| Base cost (blank blanket + in/thêu cá nhân hoá) | **$18.00** | ASSUMPTION — cần quote supplier (fleece 50x60") |
| Personalization surcharge (ảnh/tên) | gồm trong base | tuỳ supplier |
| Ship US (chăn nặng ~0.6–0.9kg, cồng kềnh) | **$7.50** | ASSUMPTION — chăn ship đắt hơn phụ kiện |
| Payment gateway (Shopify/Stripe) | 2.9% + $0.30 | chuẩn US |
| Return/defect reserve | ~3% giá | quỹ đổi trả lỗi QC |

## 3. Công thức Contribution margin (per SKU)

```
gross_before_ads = sell_price − base_cost − ship_cost − gateway_fee − return_reserve
                   (US: KHÔNG trừ VAT)

contribution_after_ads = gross_before_ads − allocated_CPA
contribution_%          = contribution_after_ads / sell_price

Break-even ROAS (BE-ROAS) = sell_price / gross_before_ads   (per SKU)
  → ROAS thực tế phải ≥ BE-ROAS thì mới có lãi; scale chỉ khi blended ≥ BE-ROAS.
Floor: contribution_% ≥ 15% sau CPA mục tiêu (nếu không đạt → không scale ads, chuyển organic/retention hoặc đổi supplier rẻ hơn).
```

## 4. Ví dụ minh hoạ (ASSUMPTION — thay bằng số thật)

**Chăn $49.95:**
```
gross_before_ads = 49.95 − 18.00 − 7.50 − (0.029×49.95 + 0.30) − (0.03×49.95)
                 = 49.95 − 18.00 − 7.50 − 1.75 − 1.50 = 21.20
BE-ROAS          = 49.95 / 21.20 ≈ 2.36
contribution @ CPA $15 = 21.20 − 15 = 6.20 → 12.4%  → DƯỚI floor 15% → không scale ở CPA $15
contribution @ CPA $12         = 9.20 → 18.4% → đạt floor
→ Winner-ROAS cold cần ≥ ~2.36; muốn floor 15% cần CPA ≤ ~$13.6 hoặc giá ≥ ~$52.
```

**Chăn $59.95 (đạt ngưỡng free-ship, khách không thấy phí ship):**
```
gross_before_ads = 59.95 − 18.00 − 7.50 − 2.04 − 1.80 = 30.61
BE-ROAS          = 59.95 / 30.61 ≈ 1.96
contribution @ CPA $18 = 12.61 → 21.0% → đạt floor tốt
→ Giá $59.95 khoẻ hơn nhiều: BE-ROAS thấp + đạt free-ship threshold. Ưu tiên bundle/upsell lên >$59.
```

## 5. Hệ quả cho các phòng

- **Merchandising:** đặt giá quanh **$49.95–59.95**, đẩy AOV lên >$59 (bundle 2 chăn / chăn + phụ kiện) để (a) qua free-ship, (b) hạ BE-ROAS.
- **Growth:** winner/scale gate = **blended ROAS ≥ BE-ROAS per-SKU** (KHÔNG hard-code con số cố định). Kill rule theo BE-ROAS, không theo số tuyệt đối tuỳ tiện.
- **Backoffice:** sales tax thu hộ tách khỏi P&L; profit = contribution − opex (tool/ad-platform-fee/supplier-adj).

## 6. TODO số thật (chặn pricing production)
- [ ] Quote base cost + ship thật từ supplier chăn US đã chọn.
- [ ] Xác nhận return/defect rate thực tế sau 30 ngày đầu.
- [ ] Đo CPA thật từ 03-growth để chốt floor & BE-ROAS per market segment.
