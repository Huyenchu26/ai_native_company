# SOP-BCK-007 — Legal & registration calendar

**Department:** Backoffice · **Loại:** DOCUMENTATION-ONLY · **v1.0** · **2026-06-08** · **SKELETON**

> Tài liệu tham khảo (không có folder state machine). Lịch các nghĩa vụ pháp lý/đăng ký định kỳ cho mô hình ShopBase + Facebook Ads + Printify, bán US + EU. Điền ngày cụ thể khi có nơi đăng ký KD.

## Mục đích
Tập trung mọi deadline pháp lý/đăng ký vào một chỗ để không bỏ lỡ: VAT/OSS, GPSR, GDPR, IP/TM, Meta Ad Policy review, ShopBase TOS — tránh phạt, gỡ listing hoặc ban ad account.

## Nội dung chính
- **VAT/OSS (EU):** tờ khai OSS theo **quý**; IOSS theo **tháng** (nếu in ngoài EU giao đơn EU); theo dõi ngưỡng €10,000/năm (alert 80%). → SOP-BCK-002
- **US sales tax:** đối soát theo state ShopBase/marketplace facilitator đã thu/nộp (không tự kê khai trừ khi có nexus). → SOP-BCK-002
- **GPSR (đơn EU):** duy trì Responsible Person EU (gia hạn hợp đồng RP nếu dùng dịch vụ); audit nhãn listing **hàng tháng**. → SOP-BCK-004
- **IP/TM:** rà USPTO/EUIPO trước mỗi breed/title mới; review danh mục TM **hàng quý**. → SOP-BCK-004
- **GDPR:** audit data inventory **hàng quý**; rà DPA processor (ShopBase/Klaviyo/Printify); xử lý yêu cầu chủ thể ≤1 tháng; breach ≤72h. → SOP-BCK-005
- **Meta Ad Policy:** review creative trước mỗi lần chạy; theo dõi thay đổi policy + ad account health **hàng tháng**. → SOP-BCK-004
- **ShopBase / Printify / Klaviyo:** theo dõi cập nhật TOS; gia hạn subscription ShopBase ($19/tháng).
- **Đăng ký KD:** chốt nơi đặt pháp nhân (EU vs ngoài EU) — ảnh hưởng cách xử lý VAT/OSS và RP.

## Ràng buộc / Tiêu chí
- Compliance error budget = 0: trễ VAT, mất RP, ad ban, breach quá 72h đều là sự cố nghiêm trọng → escalate Founder ngay.
- Gate cứng: no Meta Ad Policy → no ads; no GPSR (đơn EU) → no publish; breed vi phạm TM → block listing.
- Mọi hồ sơ thuế/VAT lưu ≥10 năm.

## Liên kết
- VAT/OSS: ./vat-oss-ioss/template/sop_bck-002_vat-oss-ioss_v1.0_2026-06-03.md
- GPSR + Meta Policy + IP/TM: ./gpsr-compliance/template/sop_bck-004_gpsr-compliance_v1.0_2026-06-03.md
- GDPR: ./gdpr-data/template/sop_bck-005_gdpr-data_v1.0_2026-06-03.md
- Niche/stack/FB Ads: ../docs/08-niche-dog-breed-leggings-shopbase.md
- Rules: ./_rules/
