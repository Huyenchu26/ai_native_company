# SOP-FUL-003 — Customer support (multilingual)

**Department:** Fulfillment & CX (ful) · **AI Worker:** CX AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Trả lời khách đúng SLA, đúng ngôn ngữ, giữ CSAT/rating cao, tuân thủ GDPR. |
| **Phạm vi** | Mọi tin nhắn khách (Etsy/Shopify), trừ return/complaint chính thức (FUL-004). |
| **Trigger** | Tin nhắn khách mới. |

### IPO
| | |
|---|---|
| **Input** | Tin nhắn khách, dữ liệu đơn (FUL-002), FAQ/knowledge |
| **Control** | SLA first response (SLO ≤4h / external ≤24h), ngôn ngữ đúng, GDPR (tối thiểu dữ liệu) |
| **Output** | Phản hồi đã gửi, ticket resolved, feedback |
| **Mechanism** | CX AI + Claude API (đa ngôn ngữ), helpdesk, Etsy messaging |

## 2. Knowledge
- **Ngôn ngữ:** EN mặc định; DE/FR khi khách dùng (Claude dịch/đáp).
- **Câu hỏi thường gặp:** tình trạng đơn, size/fit, tùy chỉnh, thời gian giao, đổi/trả.
- **GDPR:** chỉ dùng dữ liệu cần thiết; không gửi dư dữ liệu cá nhân cho AI.

## 3. RACI
| Hoạt động | Founder | CX AI |
|---|---|---|
| Trả lời thường | I | **R** |
| Case nhạy cảm/phức tạp | **A** | R (escalate) |

## 4. Đầu vào
- [ ] Truy cập đơn (FUL-002) · [ ] FAQ/response templates · [ ] Quy tắc GDPR

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Triage | Phân loại tin theo loại + ngôn ngữ | [AI WORKFORCE] | Auto-detect ngôn ngữ |
| 5.2 | Tra cứu | Lấy thông tin đơn liên quan | [AI WORKFORCE] | Tối thiểu dữ liệu (GDPR) |
| 5.3 | Soạn đáp | Template/AI, đúng ngôn ngữ, đúng tone | [AI AUGMENT] | Đối chiếu FAQ; không hứa sai |
| 5.4 | Gửi | Phản hồi ≤ SLA | [AI WORKFORCE] | SLA timer |
| 5.5 | Escalate/route | Phức tạp→Founder; return→FUL-004 | [AI AUGMENT] | Tiêu chí escalate rõ |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO/SLA | Pass |
|---|---|---|---|---|
| 1 | First response | thời gian phản hồi | SLO ≤4h / SLA ≤24h | ☐ |
| 2 | Resolution | % giải quyết | ≥ 90% | ☐ |
| 3 | Ngôn ngữ | đúng ngôn ngữ khách | 100% | ☐ |
| 4 | GDPR | không lộ dữ liệu thừa | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/support-log_[YYYY-Wnn].md → archive/ · **Downstream:** FUL-004 (return/complaint), BCK-005 (GDPR)

## 8. Phụ lục
GDPR: ../../05-backoffice/gdpr-data/ · Thiết kế §3.4
