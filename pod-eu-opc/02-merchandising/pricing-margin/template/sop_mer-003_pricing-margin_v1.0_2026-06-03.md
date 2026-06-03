# SOP-MER-003 — Pricing & margin

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Định giá đảm bảo **margin ≥ 30%** sau mọi phí, vẫn cạnh tranh. |
| **Phạm vi** | Tính giá bán + margin cho mỗi SKU. |
| **Trigger** | Có Printify product + giá in (MER-002). |

### IPO
| | |
|---|---|
| **Input** | Giá in + shipping (MER-002), bảng phí Etsy, giá competitor, VAT |
| **Control** | Margin floor 30%, chiến lược free-shipping, giá tâm lý |
| **Output** | Pricing sheet (cost, fees, sell price, margin %) |
| **Mechanism** | Catalog-Sync AI + Claude API, pricing sheet template |

## 2. Công thức (Knowledge)
```
Costs   = Printify base + shipping
Fees    = Etsy listing (~$0.20) + transaction (~6.5%) + payment processing (~3-4% + phí cố định)
          + Offsite Ads (12-15% NẾU áp dụng) + phân bổ Ads chủ động
Margin% = (Sell - Costs - Fees - VAT phần shop chịu) / Sell
Floor: Margin ≥ 30%
```
- **Free shipping:** Etsy ưu tiên listing free-ship cho khách → **bọc phí ship vào giá bán**.
- **Giá tâm lý:** .99 / .95; benchmark top sellers cùng niche.
> ⚠️ % phí thay đổi theo thời điểm/nước — xác nhận bảng phí Etsy hiện hành.

## 3. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Duyệt pricing strategy/floor | **A** | C |
| Tính giá từng SKU | I | **R** |

## 4. Đầu vào
- [ ] Giá in + shipping (MER-002) · [ ] Bảng phí Etsy hiện hành · [ ] Giá competitor

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Lấy cost | Giá in + shipping từ MER-002 | [AI WORKFORCE] | Pull số thật |
| 5.2 | Tính phí | Áp công thức §2 (gồm free-ship) | [AI WORKFORCE] | Dùng bảng phí cập nhật |
| 5.3 | Đặt giá | Sell price đạt margin ≥30% + cạnh tranh | [AI AUGMENT] | Floor check tự động |
| 5.4 | Benchmark | So với top sellers cùng niche | [AI AUGMENT] | Cảnh báo nếu lệch lớn |
| 5.5 | Xuất sheet | Pricing sheet → MER-001/MER-004 | [AI WORKFORCE] | Đủ field |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Margin | margin/SKU | ≥ 30% | ☐ |
| 2 | Free-ship | phí ship đã bọc | đúng | ☐ |
| 3 | Cạnh tranh | giá so competitor | hợp lý | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/pricing-sheet_[YYYY-MM]_DONE.md → archive/ · **Downstream:** MER-001, MER-004, BCK-003 (profit-per-SKU)

## 8. Phụ lục
Template: ../../_shared/templates/pricing-sheet-template.md · Channel: ../../_shared/channel-config/etsy.md · Thiết kế §3.2
