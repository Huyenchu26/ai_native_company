# SOP-FUL-001 — Order monitoring & exception

**Department:** Fulfillment & CX (ful) · **AI Worker:** Order-Ops AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Printify tự fulfill khi đã kết nối + thanh toán, nhưng vẫn cần giám sát & xử lý ngoại lệ để không "rơi" đơn.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Giám sát đơn mới, verify, đưa vào sản xuất Printify ≤24h, xử lý ngoại lệ. |
| **Phạm vi** | Đơn Etsy (Phase 1), Shopify (Phase 2). |
| **Trigger** | Đơn mới phát sinh (near real-time). |

### IPO
| | |
|---|---|
| **Input** | Đơn hàng (Etsy/Shopify), trạng thái thanh toán, địa chỉ giao, tồn provider |
| **Control** | Confirm production ≤24h, validate địa chỉ, phát hiện fraud, GDPR |
| **Output** | Đơn vào sản xuất + exception log |
| **Mechanism** | Order-Ops AI + Etsy/Shopify API + Printify API |

## 2. RACI
| Hoạt động | Founder | Order-Ops AI | CX AI |
|---|---|---|---|
| Verify & route | I | **R** | I |
| Exception thường | I | **R** | C |
| Exception lớn (fraud/refund) | **A** | R | C |

## 3. Đầu vào
- [ ] Etsy/Printify đã kết nối auto-fulfill · [ ] Quy tắc validate địa chỉ · [ ] Hạn mức xử lý ngoại lệ

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Detect | Nhận đơn mới qua API | [AI WORKFORCE] | Poll/webhook; không bỏ sót |
| 4.2 | Verify | Check thanh toán OK + địa chỉ hợp lệ | [AI WORKFORCE] | Validate địa chỉ tự động |
| 4.3 | Route | Confirm vào sản xuất Printify ≤24h | [AI WORKFORCE] | SLA timer; alert nếu chưa route |
| 4.4 | Exception | Địa chỉ lỗi→CX; OOS→đổi variant/provider; payment hold; fraud→escalate | [AI AUGMENT] | Playbook ngoại lệ; escalate khi vượt hạn mức |
| 4.5 | Log | Ghi trạng thái đơn + exception | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Route đúng hạn | % đơn confirm production ≤24h | 100% | ☐ |
| 2 | Địa chỉ | % đơn validated | 100% | ☐ |
| 3 | Exception | resolved/escalated, không tồn đọng | 100% | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/order-status_[YYYY-Wnn].md + exception-log → archive/ · **Downstream:** FUL-002 (tracking), BCK-001 (doanh thu)

## 7. Phụ lục
Channel: ../../_shared/channel-config/ · GDPR: ../../05-backoffice/gdpr-data/ · Thiết kế §3.4
