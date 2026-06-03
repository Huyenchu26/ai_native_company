# SOP-MER-002 — Printify product setup + chọn EU provider

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Chọn **xưởng in trong EU** là quyết định chiến lược: ship nhanh, không hải quan, né IOSS, hợp GPSR, giảm hoàn/khiếu nại.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Setup sản phẩm trên Printify với print provider EU phù hợp, file in đúng spec, đủ biến thể & mockup. |
| **Phạm vi** | Cấu hình product Printify. |
| **Trigger** | Có cleared design (PRD-004). |

### IPO
| | |
|---|---|
| **Input** | Cleared design (PRD-004), Printify catalog & giá in, ràng buộc EU |
| **Control** | Provider phải EU (ưu tiên); print spec; giá in nằm trong floor để margin ≥30% |
| **Output** | Printify product (blank + provider + print file + variants + mockups) |
| **Mechanism** | Catalog-Sync AI + Printify API |

## 2. Tiêu chí chọn provider EU (Knowledge)
| Tiêu chí | Ưu tiên |
|---|---|
| **Vị trí EU** | Đức / Latvia / Czech / EU-mainland. ⚠️ **UK = ngoài EU sau Brexit** → coi như nhập khẩu, tránh cho khách EU |
| Giá in + shipping nội EU | thấp, ổn định |
| Chất lượng & review | cao |
| Thời gian sản xuất + ship | nhanh (đáp ứng Etsy estimated delivery) |
| Sản phẩm available + GPSR data | có sẵn |

## 3. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Chọn provider EU | A | **R** |
| Setup product | I | **R** |

## 4. Đầu vào
- [ ] Cleared design · [ ] Sản phẩm blank mục tiêu (tee/hoodie...) · [ ] Tài khoản Printify (keys ngoài git)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Chọn blank | Chọn sản phẩm (tee/hoodie/sweat) | [AI WORKFORCE] | — |
| 5.2 | Chọn provider EU | So sánh provider theo §2, chọn EU | [AI AUGMENT] | Hard rule: provider EU; UK loại cho khách EU |
| 5.3 | Upload print file | Đặt design vào print area đúng spec | [AI WORKFORCE] | Auto-check spec; preview print area |
| 5.4 | Set variants | Cấu hình size/color | [AI WORKFORCE] | Checklist biến thể đủ |
| 5.5 | Mockups | Sinh mockup cho listing + Pinterest | [AI WORKFORCE] | ≥5 mockup |
| 5.6 | Handoff | Product → MER-003 (giá) + MER-001 (listing) | [AI WORKFORCE] | Ghi provider + giá in để MER-003 dùng |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Provider EU | % SKU provider EU | ≥ 90% | ☐ |
| 2 | Print file | đúng spec, trong print area | 100% | ☐ |
| 3 | Variants | đủ size/color | 100% | ☐ |
| 4 | Mockup | ≥ 5 | 100% | ☐ |
| 5 | Giá in | trong floor (margin ≥30% khả thi) | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/printify-product_[sku]_DONE.md (provider, giá in, variants) → archive/
- **Downstream:** MER-003 (pricing), MER-001 (listing), BCK-002 (nơi in cho VAT), BCK-004 (nhà SX cho GPSR)

## 8. Phụ lục
Channel: ../../_shared/channel-config/printify.md · GPSR: ../../05-backoffice/gpsr-compliance/ · VAT: ../../05-backoffice/vat-oss-ioss/ · Thiết kế §3.2
