# SOP-MER-002 — Printify/PrintBase setup AOP leggings + chọn provider

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Chọn **provider theo thị trường đơn** là quyết định chiến lược: US (chính) ship nhanh; EU (Latvia/UK/DE) không hải quan, hợp GPSR, giảm hoàn/khiếu nại. Sản phẩm core = **All-Over-Print (AOP) Leggings**.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Setup AOP Leggings trên Printify/PrintBase với provider phù hợp (US/EU), file in AOP đúng spec, đủ variant size XS–3XL/color & mockup. |
| **Phạm vi** | Cấu hình product Printify/PrintBase (AOP leggings; mở rộng sports bra/hoodie/tote cùng design). |
| **Trigger** | Có cleared design (PRD-004). |

### IPO
| | |
|---|---|
| **Input** | Cleared design AOP (PRD-004), Printify/PrintBase catalog & giá in, thị trường đơn (US/EU) |
| **Control** | Provider phù hợp thị trường; AOP print spec (toàn mặt 360°); giá in trong floor để gross margin ~45–55% |
| **Output** | AOP product (blank + provider + print file + variants XS–3XL/color + mockups) |
| **Mechanism** | Catalog-Sync AI + Printify API, PrintBase, ShopBase API |

## 2. Tiêu chí chọn provider (Knowledge)
| Tiêu chí | Ưu tiên |
|---|---|
| **Thị trường** | US (chính): Printify US. EU: Latvia / UK / DE. ⚠️ Route theo địa chỉ giao để tối ưu ship + GPSR |
| Supplier | **Printify (chính)** + PrintBase/Printful/Gelato (test) |
| Giá in + shipping | thấp, ổn định (base AOP leggings ~$18–25) |
| Chất lượng AOP & review | cao (in toàn mặt đều màu, không lệch pattern) |
| Production + ship | nhanh (US 3–7 ngày, EU 5–10 ngày) |
| GPSR data (đơn EU) | có sẵn nhà SX/RP |

## 3. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Chọn provider | A | **R** |
| Setup AOP product | I | **R** |

## 4. Đầu vào
- [ ] Cleared design AOP · [ ] Blank mục tiêu (AOP leggings; sports bra cùng design) · [ ] Tài khoản Printify/PrintBase (keys ngoài git)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Chọn blank | Chọn AOP leggings (+ sports bra cho bundle) | [AI WORKFORCE] | — |
| 5.2 | Chọn provider | So sánh theo §2, chọn theo thị trường đơn (US/EU) | [AI AUGMENT] | Route US/EU; EU tránh nhập khẩu thừa |
| 5.3 | Upload print file | Đặt AOP design phủ toàn mặt đúng spec 360° | [AI WORKFORCE] | Auto-check spec; preview AOP print area |
| 5.4 | Set variants | Cấu hình **size XS–3XL + color** | [AI WORKFORCE] | Checklist size XS–3XL đủ |
| 5.5 | Mockups | Sinh mockup AOP 360° cho product page + ads | [AI WORKFORCE] | ≥5 mockup |
| 5.6 | Handoff | Product → MER-003 (giá) + MER-001 (page) | [AI WORKFORCE] | Ghi provider + giá in để MER-003 dùng |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Provider phù hợp | route đúng thị trường (US/EU) | 100% | ☐ |
| 2 | Print file AOP | đúng spec, phủ toàn mặt | 100% | ☐ |
| 3 | Variants | đủ size XS–3XL/color | 100% | ☐ |
| 4 | Mockup | ≥ 5 (360°) | 100% | ☐ |
| 5 | Giá in | trong floor (gross margin ~45–55% khả thi) | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/printify-product_[sku]_DONE.md (provider, giá in, variants) → archive/
- **Downstream:** MER-003 (pricing), MER-001 (page), BCK-002 (nơi in cho VAT), BCK-004 (nhà SX cho GPSR đơn EU)

## 8. Phụ lục
Channel: ../../_shared/channel-config/printify.md · GPSR: ../../05-backoffice/gpsr-compliance/ · VAT: ../../05-backoffice/vat-oss-ioss/ · Niche: ../../docs/08-niche-dog-breed-leggings-shopbase.md
