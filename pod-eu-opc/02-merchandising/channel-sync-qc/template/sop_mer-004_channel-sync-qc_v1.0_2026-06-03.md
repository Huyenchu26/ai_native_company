# SOP-MER-004 — ShopBase sync & catalog QC

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE (channel-agnostic)**

> SOP đọc `_shared/channel-config/*.md`. ShopBase = active (store chính). Etsy = reference/inactive. Kênh mới bật ở config **không sửa SOP này**, chỉ đổi status.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Publish product lên ShopBase, đồng bộ tồn/variant, QC catalog để không có product lỗi. |
| **Phạm vi** | Publish + sync + catalog QC cho mọi kênh có status=active. |
| **Trigger** | Product page publish-ready (MER-001) + pricing (MER-003). |

### IPO
| | |
|---|---|
| **Input** | Page ready (MER-001), pricing (MER-003), AOP product (MER-002), channel-config |
| **Control** | Cấu hình kênh, GPSR present (đơn EU), giá/variants khớp |
| **Output** | Product live + sync log + catalog QC report |
| **Mechanism** | Catalog-Sync AI + Printify→ShopBase integration, ShopBase API |

## 2. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Publish & sync | I | **R** |
| Catalog QC | C | **R** |

## 3. Đầu vào
- [ ] Page ready · [ ] Pricing · [ ] channel-config kênh active · [ ] Printify/PrintBase đã liên kết ShopBase

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Đọc config | Lấy danh sách kênh status=active | [AI WORKFORCE] | Chỉ publish kênh active |
| 4.2 | Publish ShopBase | Đẩy qua Printify/PrintBase→ShopBase | [AI WORKFORCE] | Verify API success |
| 4.3 | Verify live | Kiểm product hiển thị đúng (ảnh AOP/giá/variants XS–3XL/upsell) | [AI AUGMENT] | Tự kiểm sau publish |
| 4.4 | Catalog QC | Quét ảnh lỗi, variant sai, giá lệch, thiếu GPSR (đơn EU), upsell hỏng | [AI WORKFORCE] | Checklist QC; fail → fix |
| 4.5 | (Kênh mới) | Nếu config kênh khác=active → replicate, không hard-code | [AI WORKFORCE] | Đọc config |
| 4.6 | Log | Ghi sync log → Growth (03) | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Live đúng | product hiển thị đúng | 100% | ☐ |
| 2 | Ảnh | không lỗi/thiếu (AOP 360°) | 100% | ☐ |
| 3 | Giá/variants | khớp pricing/MER-002 (size XS–3XL) | 100% | ☐ |
| 4 | GPSR (đơn EU) | present trên product | 100% | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/sync-log_[YYYY-Wnn]_DONE.md → archive/ · **Downstream:** 03 Growth (FB Creative/FB Ads — product live để chạy ads)

## 7. Phụ lục
Config: ../../_shared/channel-config/ (shopbase/printify) · Niche: ../../docs/08-niche-dog-breed-leggings-shopbase.md §2
