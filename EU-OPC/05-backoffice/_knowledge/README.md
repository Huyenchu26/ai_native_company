# _knowledge — 05-Backoffice

Knowledge base cho Finance + Compliance + Workforce Ops. Nguồn sự thật cho mọi SOP; cập nhật trước khi tính toán/clearance (không dùng dữ liệu cũ).

---

## Compliance Knowledge
### GPSR (EU 2023/988)
- Hiệu lực 13/12/2024. Áp dụng mọi consumer product bán cho khách EU.
- Yêu cầu: **Responsible Person** đặt tại EU (tên, địa chỉ, email), nhãn an toàn (manufacturer, product ID, material, warning/care), traceability.
- Gate cứng: no GPSR clearance → no publish EU (SOP-BCK-004).

### Responsible Person
- Phải có pháp nhân/đại diện trong EU. Với POD: provider EU (Printify/PrintBase EU) hoặc EU rep service. Lưu RP registry (tên/địa chỉ/contact) per provider.

### IP/TM breed check
- Breed/niche name có thể trùng trademark đã đăng ký → watchlist breed-TM. Check trước listing (đồng bộ SOP-PRD-004). Trùng → FAIL.

### GDPR
- RoPA (Art.30): map PII qua ShopBase, Klaviyo, Meta CAPI, Printify. Legal basis + retention.
- DSAR: access/erasure/portability ≤ 1 tháng. Breach notify ≤ **72h** (Art.33).
- Email marketing = chỉ opt-in (đồng bộ SOP-GRW-003).

### Meta Ad Policy (anti-ban)
- Tuân thủ policy creative/landing (no misleading, no prohibited content). BM 5-tier anti-ban (đồng bộ Growth SOP-GRW-002). No policy pass → no ads.

### ShopBase TOS
- Tuân thủ điều khoản platform (product type, payment, prohibited). Vi phạm → rủi ro suspend store.

## Finance Knowledge
### VAT OSS/IOSS
- **IOSS:** đơn ≤ €150 nhập từ ngoài EU; thu VAT điểm bán; khai tháng.
- **OSS (Union):** hàng đã ở EU bán xuyên biên giới EU; khai quý.
- VAT theo **nước đến** — giữ bảng VAT rate từng EU member state (versioned).
- **US sales tax:** economic nexus theo bang; ShopBase thu tự động nếu set; finance reconcile + note nexus mới.

### FX USD→VND
- USD là đồng ghi nhận gốc. Một **tỷ giá khóa kỳ** duy nhất/kỳ, ghi nguồn + ngày. Không bịa per-transaction FX.

### Profit model
- profit-per-SKU = giá bán − (print + ship + gateway fee + ad-spend phân bổ). ROAS ≥ 2.5, CPA < $20, net margin ≥ 20%.

## Workforce Knowledge — 12-Worker Roster
| # | Worker | Phòng |
|---|---|---|
| 1 | niche-research | 01 Product Studio |
| 2 | product-design | 01 Product Studio |
| 3 | catalog-sync | 02 Merchandising |
| 4 | product-page | 02 Merchandising |
| 5 | fb-ads | 03 Growth |
| 6 | fb-creative | 03 Growth |
| 7 | marketing | 03 Growth |
| 8 | order-ops | 04 Fulfillment & CX |
| 9 | cx | 04 Fulfillment & CX |
| 10 | finance | 05 Backoffice |
| 11 | compliance | 05 Backoffice |
| 12 | ops-hr | 05 Backoffice |

## Cập nhật
VAT rate / GPSR spec / Meta policy thay đổi → cập nhật file này TRƯỚC khi áp dụng. Versioned, ghi ngày.
