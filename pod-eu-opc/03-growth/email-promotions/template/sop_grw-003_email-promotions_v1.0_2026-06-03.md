# SOP-GRW-003 — Email & promotions (Klaviyo)

**Department:** Growth (grw) · **AI Worker:** Marketing AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Chỉ gửi cho người **opt-in** (GDPR — SOP-BCK-005). Email (Klaviyo + ShopBase) là đòn bẩy AOV & repeat. Tách list "đơn hàng" vs "marketing".

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Nuôi dưỡng khách qua email flow + promotion theo mùa để tăng AOV, repeat & conversion. |
| **Phạm vi** | Klaviyo flows + ShopBase built-in email + promotions/sales. |
| **Trigger** | Khách opt-in mới; cart abandon / purchase event; dịp sale/mùa vụ; lịch email. |

### IPO
| | |
|---|---|
| **Input** | Danh sách opt-in (consent), product/promotion, purchaser/ATC audience (GRW-002), seasonal calendar |
| **Control** | GDPR consent (bắt buộc), brand voice, tần suất hợp lý |
| **Output** | Email campaign/flow đã gửi + promotion + metrics |
| **Mechanism** | Marketing AI + Claude API, Klaviyo, ShopBase email |

## 2. Knowledge
- **Flows (Klaviyo):** welcome, cart-abandon, post-purchase upsell (sports bra cùng design → AOV $75–95), win-back.
- **Promotions:** seasonal sale (Christmas, Mother's Day, gift angle), coupon.
- **GDPR:** double opt-in; mọi email có unsubscribe; lưu bằng chứng consent.

## 3. RACI
| Hoạt động | Founder | Marketing AI | Compliance AI (05) |
|---|---|---|---|
| Tạo & gửi campaign/flow | I | **R** | C (consent) |
| Duyệt promotion lớn | **A** | R | I |

## 4. Đầu vào
- [ ] List opt-in (consent OK — BCK-005) · [ ] Product/promotion · [ ] Lịch mùa vụ · [ ] Purchaser/ATC audience (GRW-002)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Segment | Chia nhóm theo hành vi/breed/giai đoạn | [AI WORKFORCE] | Chỉ nhóm có consent |
| 5.2 | Soạn | Viết email (EN) — cart-abandon / post-purchase upsell / win-back / seasonal | [AI AUGMENT] | Brand voice; có unsubscribe |
| 5.3 | Check consent | Xác nhận chỉ gửi người opt-in | [AI WORKFORCE] | Block nếu list lẫn no-consent |
| 5.4 | Gửi | Gửi/kích hoạt flow qua Klaviyo | [AI WORKFORCE] | — |
| 5.5 | Track | Open/CTR/conversion/AOV → GRW-004 | [AI WORKFORCE] | — |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Consent | % người nhận có opt-in | 100% | ☐ |
| 2 | Open rate | tỉ lệ mở | ≥ 25% | ☐ |
| 3 | Unsubscribe | mọi email có link hủy | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/email-campaign_[YYYY-MM].md → archive/ · **Downstream:** GRW-004, BCK-005 (consent log)

## 8. Phụ lục
GDPR: ../../../05-backoffice/gdpr-data/ · Niche spec (kinh tế/upsell): ../../../docs/08-niche-dog-breed-leggings-shopbase.md §4
