# SOP-FUL-002 — Production & shipping tracking

**Department:** Fulfillment & CX (ful) · **AI Worker:** Order-Ops AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Giao đúng hạn so với **delivery estimate đã hứa trên ShopBase** là yếu tố giữ rating & repeat. Chậm → chủ động báo khách trước.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Theo dõi sản xuất + vận chuyển, gửi tracking cho khách, phát hiện & xử lý chậm trễ chủ động. |
| **Phạm vi** | Từ lúc đơn vào sản xuất đến khi giao (US + EU). |
| **Trigger** | Đơn đã route sản xuất (FUL-001). |

### IPO
| | |
|---|---|
| **Input** | Trạng thái sản xuất Printify, tracking number, delivery estimate trên đơn ShopBase |
| **Control** | On-time ship rate, gửi tracking 100%, notify chậm trước hạn |
| **Output** | Tracking gửi khách + delay flags |
| **Mechanism** | Order-Ops AI + Printify API + ShopBase API |

## 2. Knowledge
- Production Printify ~2–5 ngày + shipping US ~3–7 ngày / EU (Latvia/UK/DE) ~5–10 ngày (xác nhận theo provider).
- Đối chiếu liên tục với **delivery estimate** hiển thị cho khách trên ShopBase.

## 3. RACI
| Hoạt động | Founder | Order-Ops AI | CX AI |
|---|---|---|---|
| Track & gửi tracking | I | **R** | I |
| Xử lý delay | I | **R** | **C** (báo khách) |

## 4. Đầu vào
- [ ] Đơn đang sản xuất (FUL-001) · [ ] Delivery estimate của từng đơn

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Track production | Theo dõi status Printify | [AI WORKFORCE] | Poll định kỳ |
| 5.2 | Lấy tracking | Khi shipped, lấy tracking number | [AI WORKFORCE] | — |
| 5.3 | Push tracking | Cập nhật tracking vào đơn ShopBase + email khách (Klaviyo/ShopBase) | [AI WORKFORCE] | 100% đơn có tracking |
| 5.4 | Monitor vs ETA | So tiến độ với delivery estimate | [AI AUGMENT] | Alert khi risk chậm |
| 5.5 | Xử lý delay | Báo CX (FUL-003) chủ động liên hệ khách | [AI AUGMENT] | Notify TRƯỚC khi khách hỏi |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Tracking | % đơn gửi tracking | 100% | ☐ |
| 2 | On-time | % đơn ship đúng hạn | ≥ mục tiêu | ☐ |
| 3 | Delay notify | chậm được báo trước | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/tracking-log_[YYYY-Wnn].md → archive/ · **Downstream:** FUL-003 (CX), FUL-004 (nếu lỗi giao)

## 8. Phụ lục
Channel: ../../../_shared/channel-config/printify.md · ShopBase: ../../../_shared/channel-config/shopbase.md · Niche spec: ../../../docs/08-niche-dog-breed-leggings-shopbase.md
