# SOP-FUL-003 — Customer support (EN, US/EU)

**Department:** Fulfillment & CX (ful) · **AI Worker:** CX AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Trả lời khách đúng SLA bằng tiếng Anh, giữ CSAT/rating cao, tuân thủ GDPR. |
| **Phạm vi** | Mọi tin nhắn khách (ShopBase helpdesk + email), trừ return/complaint chính thức (FUL-004). |
| **Trigger** | Tin nhắn khách mới. |

### IPO
| | |
|---|---|
| **Input** | Tin nhắn khách, dữ liệu đơn (FUL-002), size guide, FAQ/knowledge |
| **Control** | SLA first response (SLO ≤4h / external ≤24h), tiếng Anh đúng tone, GDPR (tối thiểu dữ liệu) |
| **Output** | Phản hồi đã gửi, ticket resolved, feedback |
| **Mechanism** | CX AI + Claude API, ShopBase helpdesk |

## 2. Knowledge
- **Ngôn ngữ:** EN cho cả US & EU (DE/FR hỗ trợ qua Claude khi khách dùng).
- **Câu hỏi thường gặp:** tình trạng đơn, size/fit AOP leggings (XS–3XL), thời gian giao US/EU, đổi/trả, upsell sports bra.
- **GDPR:** chỉ dùng dữ liệu cần thiết; không gửi dư dữ liệu cá nhân cho AI; chỉ gửi email marketing khi khách opt-in.

## 3. RACI
| Hoạt động | Founder | CX AI |
|---|---|---|
| Trả lời thường | I | **R** |
| Case nhạy cảm/phức tạp | **A** | R (escalate) |

## 4. Đầu vào
- [ ] Truy cập đơn (FUL-002) · [ ] Size guide + FAQ/response templates · [ ] Quy tắc GDPR

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Triage | Phân loại tin theo loại | [AI WORKFORCE] | Gắn nhãn ticket helpdesk |
| 5.2 | Tra cứu | Lấy thông tin đơn liên quan | [AI WORKFORCE] | Tối thiểu dữ liệu (GDPR) |
| 5.3 | Soạn đáp | Template/AI EN, đúng tone, dẫn size guide khi cần | [AI AUGMENT] | Đối chiếu FAQ; không hứa sai |
| 5.4 | Gửi | Phản hồi ≤ SLA | [AI WORKFORCE] | SLA timer |
| 5.5 | Escalate/route | Phức tạp→Founder; return/size exchange→FUL-004 | [AI AUGMENT] | Tiêu chí escalate rõ |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO/SLA | Pass |
|---|---|---|---|---|
| 1 | First response | thời gian phản hồi | SLO ≤4h / SLA ≤24h | ☐ |
| 2 | Resolution | % giải quyết | ≥ 90% | ☐ |
| 3 | CSAT | rating phản hồi | ≥ 4.8 | ☐ |
| 4 | GDPR | không lộ dữ liệu thừa | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/support-log_[YYYY-Wnn].md → archive/ · **Downstream:** FUL-004 (return/complaint), BCK-005 (GDPR)

## 8. Phụ lục
GDPR: ../../../05-backoffice/gdpr-data/ · ShopBase: ../../../_shared/channel-config/shopbase.md · Niche spec: ../../../docs/08-niche-dog-breed-leggings-shopbase.md
