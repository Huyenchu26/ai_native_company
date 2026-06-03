# SOP-MER-004 — Channel sync & catalog QC

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE (channel-agnostic)**

> SOP đọc `_shared/channel-config/*.md`. Etsy = active (Phase 1). Shopify = planned → bật ở Phase 2 **không sửa SOP này**, chỉ đổi status trong shopify.md.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Publish listing lên kênh đang active, đồng bộ trạng thái, QC catalog để không có listing lỗi. |
| **Phạm vi** | Publish + sync + catalog QC cho mọi kênh có status=active. |
| **Trigger** | Listing publish-ready (MER-001) + pricing (MER-003). |

### IPO
| | |
|---|---|
| **Input** | Listing ready (MER-001), pricing (MER-003), printify product (MER-002), channel-config |
| **Control** | Cấu hình kênh, GPSR present, giá/variants khớp |
| **Output** | Listing live + sync log + catalog QC report |
| **Mechanism** | Catalog-Sync AI + Printify→Etsy integration, Etsy/Shopify API |

## 2. RACI
| Hoạt động | Founder | Catalog-Sync AI |
|---|---|---|
| Publish & sync | I | **R** |
| Catalog QC | C | **R** |

## 3. Đầu vào
- [ ] Listing ready · [ ] Pricing · [ ] channel-config kênh active · [ ] Printify đã liên kết Etsy

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Đọc config | Lấy danh sách kênh status=active | [AI WORKFORCE] | Chỉ publish kênh active |
| 4.2 | Publish Etsy | Đẩy qua Printify→Etsy | [AI WORKFORCE] | Verify API success |
| 4.3 | Verify live | Kiểm listing hiển thị đúng (ảnh/giá/variants) | [AI AUGMENT] | Tự kiểm sau publish |
| 4.4 | Catalog QC | Quét ảnh lỗi, variant sai, giá lệch, thiếu GPSR | [AI WORKFORCE] | Checklist QC; fail → fix |
| 4.5 | (Phase 2) Shopify | Nếu shopify.md=active → replicate sang Shopify | [AI WORKFORCE] | Đọc config, không hard-code |
| 4.6 | Log | Ghi sync log → Growth (03) | [AI WORKFORCE] | — |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Live đúng | listing hiển thị đúng | 100% | ☐ |
| 2 | Ảnh | không lỗi/thiếu | 100% | ☐ |
| 3 | Giá/variants | khớp pricing/MER-002 | 100% | ☐ |
| 4 | GPSR | present trên listing | 100% | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/sync-log_[YYYY-Wnn]_DONE.md → archive/ · **Downstream:** 03 Growth (marketing listing live)

## 7. Phụ lục
Config: ../../_shared/channel-config/ (etsy/printify/shopify) · Thiết kế §3.2, §8 (channel rollout)
