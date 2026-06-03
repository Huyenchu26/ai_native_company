# 04 — Fulfillment & CX

> Order monitoring · production/shipping tracking (Printify) · CSKH · returns/complaints.
> Chi tiết: [Design Roadmap §3.4](../02-design/opc-design-roadmap.md)

## Department IPO
| Component | Detail |
|---|---|
| **Input** | Đơn hàng (Etsy/Shopify), Printify production status, tracking, tin nhắn khách, return request |
| **Control** | Etsy SLA (ship on-time, phản hồi <24h), return policy, GDPR, provider SLA |
| **Output** | Đơn xử lý, tracking gửi khách, ticket resolved, return/refund, CX report |
| **Mechanism** | Etsy/Shopify API, Printify API, Claude API (multilingual), helpdesk |

## Value Chain Position
- **Layer:** Operations (Service)
- **Upstream:** 03 Growth (đơn hàng) · **Downstream:** 05 Backoffice (doanh thu)

## SOP Index
| SOP | Tên | Loại | AI Worker |
|---|---|---|---|
| SOP-FUL-001 | Order monitoring & exception | OPERATIONAL | Order-Ops AI |
| SOP-FUL-002 | Production & shipping tracking | OPERATIONAL | Order-Ops AI |
| SOP-FUL-003 | Customer support (multilingual) | OPERATIONAL | CX AI |
| SOP-FUL-004 | Returns / refund / complaint | OPERATIONAL | CX AI |
| SOP-FUL-005 | Return & shipping policy | DOC-ONLY | — |

## KPIs (xem kpi_ful-001)
| KPI | Target |
|---|---|
| Đơn xử lý đúng hạn | 100% (production confirm ≤24h) |
| First response time | SLO ≤4h / SLA ≤24h |
| Resolution rate | ≥ 90% |
| Shop rating | ≥ 4.8 (Star Seller) |
