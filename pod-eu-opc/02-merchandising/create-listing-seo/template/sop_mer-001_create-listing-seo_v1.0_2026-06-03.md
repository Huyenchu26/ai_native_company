# SOP-MER-001 — Tạo listing + Etsy SEO (+ nhãn GPSR)

**Department:** Merchandising (mer) · **AI Worker:** Listing-SEO AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Gate publish của shop: listing KHÔNG được publish nếu thiếu nhãn GPSR (clearance từ SOP-BCK-004) hoặc dính từ khóa IP.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tạo listing chuẩn Etsy SEO + gắn nhãn GPSR, sẵn sàng publish có khả năng được tìm thấy. |
| **Phạm vi** | Soạn nội dung listing (title/tags/desc/attributes/images). Publish thực hiện ở MER-004. |
| **Trigger** | Có cleared design (PRD-004) + Printify product (MER-002) + pricing (MER-003). |

### IPO
| | |
|---|---|
| **Input** | Cleared design + IP log (PRD-004), mockups (MER-002), pricing (MER-003), keyword data, GPSR clearance (BCK-004) |
| **Control** | Etsy SEO rules (title ≤140, 13 tags), GPSR labeling, brand voice (EN), không từ khóa IP |
| **Output** | Listing publish-ready (EN) |
| **Mechanism** | Listing-SEO AI + Claude API, eRank, Etsy API |

## 2. Etsy SEO checklist (Knowledge)
- **Title** ≤ 140 ký tự, **front-load** keyword chính (Etsy ưu tiên đầu title)
- **13 tags**, multi-word, tận dụng tối đa 20 ký tự/tag, không trùng lặp
- **Description:** hook → benefits → chất liệu/size → **size guide** → shipping EU → care
- **Attributes & category** điền đầy đủ (Etsy dùng để xếp hạng)
- **Ảnh:** ≥ 5-10 mockup + 1 size chart; ảnh đầu là ảnh mạnh nhất
- **GPSR block:** nhà sản xuất + Responsible Person EU + cảnh báo (nếu có)

## 3. RACI
| Hoạt động | Founder | Listing-SEO AI | Compliance AI (05) |
|---|---|---|---|
| Soạn title/tags/desc | I | **R** | I |
| Chèn nhãn GPSR | I | R | **C** (cấp clearance) |
| Spot-check listing | C | R | I |

## 4. Đầu vào
- [ ] Cleared design + IP log · [ ] Mockups · [ ] Pricing · [ ] **GPSR clearance (BCK-004)**

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Keyword | Chọn keyword chính + phụ từ eRank | [AI WORKFORCE] | Dữ liệu thật |
| 5.2 | Title & tags | Viết title ≤140 front-load + 13 tags | [AI AUGMENT] | Auto-count ký tự + số tag |
| 5.3 | Description | Soạn theo cấu trúc §2 (EN) | [AI AUGMENT] | Template; có size guide + shipping EU |
| 5.4 | Attributes/images | Điền attributes, gắn ≥5 mockup + size chart | [AI WORKFORCE] | Checklist ảnh |
| 5.5 | GPSR | Chèn nhãn GPSR từ clearance BCK-004 | [AI AUGMENT] | Không có clearance → BLOCK |
| 5.6 | IP recheck | Quét title/tags không chứa từ khóa IP | [AI WORKFORCE] | Block nếu có brand/character |
| 5.7 | Handoff | Listing publish-ready → MER-004 | [AI WORKFORCE] | Gate đủ điều kiện |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Title | ≤ 140 ký tự, front-load | 100% | ☐ |
| 2 | Tags | đủ 13 | 100% | ☐ |
| 3 | Ảnh | ≥ 5 mockup + size chart | 100% | ☐ |
| 4 | **GPSR** | nhãn present | 100% | ☐ |
| 5 | IP | 0 từ khóa vi phạm | 100% | ☐ |

**Quyết định:** ALL pass → MER-004 publish. GPSR/IP fail → **BLOCK** (không loop "cho qua") → escalate.

## 7. Output & Downstream
- **Lưu:** ./output/listing_[sku]_READY.md → archive/ · **Downstream:** MER-004 (publish), MER-003 (giá)

## 8. Phụ lục
Doc: ../listing-template-style.md · GPSR: ../../05-backoffice/gpsr-compliance/ · Channel: ../../_shared/channel-config/etsy.md · Thiết kế §3.2
