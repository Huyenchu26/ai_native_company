# 04 — Fulfillment & CX

> Order monitoring (ShopBase) · production/shipping tracking (Printify) · CSKH (EN, US/EU) · returns/complaints.
> Chi tiết: [Niche spec](../docs/08-niche-dog-breed-leggings-shopbase.md)

## Department IPO
| Component | Detail |
|---|---|
| **Input** | Đơn hàng ShopBase, Printify production status, tracking, tin nhắn khách, return request |
| **Control** | On-time ship, phản hồi <24h, return policy, GPSR (đơn EU), GDPR, provider SLA |
| **Output** | Đơn xử lý, tracking gửi khách, ticket resolved, return/refund, CX report |
| **Mechanism** | ShopBase API, Printify API, Claude API, ShopBase helpdesk, Klaviyo |

## Value Chain Position
- **Layer:** Operations (Service)
- **Upstream:** 03 Growth (đơn từ Facebook Ads → ShopBase) · **Downstream:** 05 Backoffice (doanh thu)

## SOP Index
| SOP | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-FUL-001 | Order monitoring & exception | OPERATIONAL | Order-Ops AI |
| SOP-FUL-002 | Production & shipping tracking | OPERATIONAL | Order-Ops AI |
| SOP-FUL-003 | Customer support (EN, US/EU) | OPERATIONAL | CX AI |
| SOP-FUL-004 | Returns / refund / complaint | OPERATIONAL | CX AI |
| SOP-FUL-005 | Return & shipping policy | DOC-ONLY | — |

## KPIs (xem kpi_ful-001)
| KPI | Target |
|---|---|
| Đơn xử lý đúng hạn | 100% (production confirm ≤24h) |
| First response time | SLO ≤4h / SLA ≤24h |
| Resolution rate | ≥ 90% |
| Shop rating | ≥ 4.8 |
