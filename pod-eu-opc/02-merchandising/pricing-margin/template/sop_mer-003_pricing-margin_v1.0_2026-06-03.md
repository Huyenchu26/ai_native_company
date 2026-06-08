# SOP-MER-003 — Pricing & margin

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Định giá AOP leggings đảm bảo **gross margin ~45–55%** (trước ads) sau mọi phí ShopBase/Printify, vẫn cạnh tranh; hỗ trợ AOV $75–95 qua bundle. |
| **Phạm vi** | Tính giá bán + margin cho mỗi SKU + cấu hình giá bundle. |
| **Trigger** | Có AOP product + giá in (MER-002). |

### IPO
| | |
|---|---|
| **Input** | Base cost + shipping (MER-002), ShopBase fee, CPA mục tiêu, giá competitor |
| **Control** | Gross margin floor ~45–55%, bundle pricing (leggings + sports bra), giá tâm lý |
| **Output** | Pricing sheet (cost, fees, sell price, bundle, gross margin %) |
| **Mechanism** | Catalog-Sync AI + Claude API, pricing sheet template |

## 2. Công thức (Knowledge)
```
Costs   = Printify/PrintBase base (AOP leggings ~$20–24) + shipping (US $6–9 / EU)
Fees    = ShopBase transaction (~$1.5) + payment processing (~3-4% + phí cố định)
          (lưu ý: ads tính riêng ở ROAS/CPA, không trừ vào gross margin)
Gross%  = (Sell - Costs - Fees - VAT phần shop chịu) / Sell
Floor: Gross margin ~45–55%  (kinh tế ShopBase; đơn target ~$59–69, optimal $85 có bundle)
```
- **Bundle/upsell:** leggings + sports bra cùng design → AOV $75–95 (đòn bẩy chính đạt mục tiêu).
- **Giá tâm lý:** .99 / .95; benchmark top sellers cùng niche (dog breed leggings).
> ⚠️ % phí thay đổi theo thời điểm/nước — xác nhận bảng phí ShopBase/Printify hiện hành.

## 3. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Duyệt pricing strategy/floor | **A** | C |
| Tính giá từng SKU + bundle | I | **R** |

## 4. Đầu vào
- [ ] Base cost + shipping (MER-002) · [ ] Bảng phí ShopBase hiện hành · [ ] Giá competitor

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Lấy cost | Base + shipping từ MER-002 | [AI WORKFORCE] | Pull số thật |
| 5.2 | Tính phí | Áp công thức §2 (ShopBase/payment) | [AI WORKFORCE] | Dùng bảng phí cập nhật |
| 5.3 | Đặt giá | Sell price đạt gross margin ~45–55% + cạnh tranh | [AI AUGMENT] | Floor check tự động |
| 5.4 | Bundle | Đặt giá bundle leggings + sports bra (AOV $75–95) | [AI AUGMENT] | Kiểm bundle vẫn giữ margin |
| 5.5 | Benchmark | So với top sellers dog breed leggings | [AI AUGMENT] | Cảnh báo nếu lệch lớn |
| 5.6 | Xuất sheet | Pricing sheet → MER-001/MER-004 | [AI WORKFORCE] | Đủ field |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Gross margin | margin/SKU | ~45–55% | ☐ |
| 2 | Bundle | giá bundle giữ margin + đẩy AOV | đúng | ☐ |
| 3 | Cạnh tranh | giá so competitor | hợp lý | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/pricing-sheet_[YYYY-MM]_DONE.md → archive/ · **Downstream:** MER-001, MER-004, BCK-003 (profit-per-SKU)

## 8. Phụ lục
Template: ../../_shared/templates/pricing-sheet-template.md · Channel: ../../_shared/channel-config/ · Niche: ../../docs/08-niche-dog-breed-leggings-shopbase.md §4
