# SOP-FUL-001 — Order monitoring & exception

**Department:** Fulfillment & CX (ful) · **AI Worker:** Order-Ops AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Printify tự fulfill khi đã kết nối ShopBase + thanh toán, nhưng vẫn cần giám sát & xử lý ngoại lệ để không "rơi" đơn.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Giám sát đơn ShopBase mới, verify, đưa vào sản xuất Printify ≤24h, xử lý ngoại lệ. |
| **Phạm vi** | Đơn ShopBase (store chính), khách US + EU. |
| **Trigger** | Đơn mới phát sinh (near real-time). |

### IPO
| | |
|---|---|
| **Input** | Đơn hàng ShopBase, trạng thái thanh toán, địa chỉ giao, tồn provider Printify |
| **Control** | Confirm production ≤24h, validate địa chỉ, phát hiện fraud, GPSR (đơn EU), GDPR |
| **Output** | Đơn vào sản xuất + exception log |
| **Mechanism** | Order-Ops AI + ShopBase API + Printify API |

## 2. RACI
| Hoạt động | Founder | Order-Ops AI | CX AI |
|---|---|---|---|
| Verify & route | I | **R** | I |
| Exception thường | I | **R** | C |
| Exception lớn (fraud/refund) | **A** | R | C |

## 3. Đầu vào
- [ ] ShopBase/Printify đã kết nối auto-fulfill · [ ] Quy tắc validate địa chỉ · [ ] Hạn mức xử lý ngoại lệ

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Detect | Nhận đơn ShopBase mới qua API | [AI WORKFORCE] | Poll/webhook; không bỏ sót |
| 4.2 | Verify | Check thanh toán OK + địa chỉ hợp lệ | [AI WORKFORCE] | Validate địa chỉ tự động |
| 4.3 | GPSR check (đơn EU) | Đơn EU phải có nhãn an toàn GPSR đính kèm | [AI AUGMENT] | **Gate cứng: thiếu GPSR → không route đơn EU** |
| 4.4 | Route | Confirm vào sản xuất Printify ≤24h (US/EU provider) | [AI WORKFORCE] | SLA timer; alert nếu chưa route |
| 4.5 | Exception | Địa chỉ lỗi→CX; OOS→đổi variant/provider; payment hold; fraud→escalate | [AI AUGMENT] | Playbook ngoại lệ; escalate khi vượt hạn mức |
| 4.6 | Log | Ghi trạng thái đơn + exception | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Route đúng hạn | % đơn confirm production ≤24h | 100% | ☐ |
| 2 | Địa chỉ | % đơn validated | 100% | ☐ |
| 3 | GPSR (đơn EU) | % đơn EU có nhãn an toàn | 100% | ☐ |
| 4 | Exception | resolved/escalated, không tồn đọng | 100% | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/order-status_[YYYY-Wnn].md + exception-log → archive/ · **Downstream:** FUL-002 (tracking), BCK-001 (doanh thu)

## 7. Phụ lục
Channel: ../../../_shared/channel-config/shopbase.md · Printify: ../../../_shared/channel-config/printify.md · GPSR: ../../../05-backoffice/ · GDPR: ../../../05-backoffice/gdpr-data/ · Niche spec: ../../../docs/08-niche-dog-breed-leggings-shopbase.md
