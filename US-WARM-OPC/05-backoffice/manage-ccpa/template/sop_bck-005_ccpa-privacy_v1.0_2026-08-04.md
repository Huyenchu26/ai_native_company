# SOP-BCK-005 — Privacy (CCPA/CPRA + personalization PII)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 05-Backoffice · **Responsible AI:** `vibe-us-warm-bck-compliance`
**Delta vs EU:** thay GDPR bằng **CCPA/CPRA** (California) + state privacy laws. Đặc thù: cá nhân hoá dùng **tên + ẢNH khách** = PII nhạy cảm.

## 1. Mục tiêu
Xử lý PII đúng luật US: notice-at-collection, quyền know/delete/opt-out (CCPA), xử lý ảnh/tên cá nhân hoá an toàn.

## 2. IPO
- **Input:** customer PII (tên, ảnh upload cá nhân hoá), DSAR request.
- **Control:** notice at collection; opt-out "Do Not Sell/Share"; delete request ≤ 45 ngày (CCPA); ảnh cá nhân hoá chỉ dùng để in, không bán/share, xóa sau retention.
- **Output:** `privacy-record.json` (schema `privacy-record.schema.json`).

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Notice at collection | thu PII không notice → vi phạm |
| 3.2 | DSAR (know/delete) | đáp ứng ≤ 45 ngày |
| 3.3 | Ảnh cá nhân hoá | chỉ để in; không dùng marketing nếu không consent; xóa sau retention |
| 3.4 | Opt-out | tôn trọng "Do Not Sell/Share" |

## 4. RACI: R bck-compliance · A Owner · C ful-cx (nhận request) · I mer.

## 5. Gate (allOf/if-then)
dsar_closed=true ⇒ response_days ≤ 45. personalization_photo_used_marketing=true ⇒ consent=true. Fail-closed: uncertain consent → không dùng ảnh marketing.

## 6. Links: PII policy [../../../_shared/policies](../../../_shared/policies). CX intake: 04 ful-cx.

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — CCPA/CPRA, ảnh/tên cá nhân hoá PII, DSAR ≤45d. |
