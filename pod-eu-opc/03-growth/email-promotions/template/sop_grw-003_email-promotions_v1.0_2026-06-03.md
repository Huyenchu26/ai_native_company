# SOP-GRW-003 — Email & promotions

**Department:** Growth (grw) · **AI Worker:** Marketing AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Chỉ gửi cho người **opt-in** (GDPR — SOP-BCK-005). Tách list "đơn hàng" vs "marketing".

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Nuôi dưỡng khách qua email + chạy promotion theo mùa để tăng repeat & conversion. |
| **Phạm vi** | Email sequences + promotions/sales. |
| **Trigger** | Khách opt-in mới; dịp sale/mùa vụ; lịch email. |

### IPO
| | |
|---|---|
| **Input** | Danh sách opt-in (consent), listing/promotion, seasonal calendar |
| **Control** | GDPR consent (bắt buộc), brand voice, tần suất hợp lý |
| **Output** | Email campaign đã gửi + promotion + metrics |
| **Mechanism** | Marketing AI + Claude API, email tool (Klaviyo/Mailchimp) |

## 2. Knowledge
- **Sequences:** welcome, abandoned cart, post-purchase, win-back.
- **Promotions:** Etsy sales events, seasonal sale, coupon.
- **GDPR:** double opt-in; mọi email có unsubscribe; lưu bằng chứng consent.

## 3. RACI
| Hoạt động | Founder | Marketing AI | Compliance AI (05) |
|---|---|---|---|
| Tạo & gửi campaign | I | **R** | C (consent) |
| Duyệt promotion lớn | **A** | R | I |

## 4. Đầu vào
- [ ] List opt-in (consent OK — BCK-005) · [ ] Listing/promotion · [ ] Lịch mùa vụ

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Segment | Chia nhóm theo hành vi/giai đoạn | [AI WORKFORCE] | Chỉ nhóm có consent |
| 5.2 | Soạn | Viết email (EN) + promotion | [AI AUGMENT] | Brand voice; có unsubscribe |
| 5.3 | Check consent | Xác nhận chỉ gửi người opt-in | [AI WORKFORCE] | Block nếu list lẫn no-consent |
| 5.4 | Gửi | Gửi qua email tool | [AI WORKFORCE] | — |
| 5.5 | Track | Open/CTR/conversion → GRW-004 | [AI WORKFORCE] | — |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Consent | % người nhận có opt-in | 100% | ☐ |
| 2 | Open rate | tỉ lệ mở | ≥ 25% | ☐ |
| 3 | Unsubscribe | mọi email có link hủy | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/email-campaign_[YYYY-MM].md → archive/ · **Downstream:** GRW-004, BCK-005 (consent log)

## 8. Phụ lục
GDPR: ../../05-backoffice/gdpr-data/ · Thiết kế §3.3
