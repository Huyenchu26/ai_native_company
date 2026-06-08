# SOP-MER-001 — Tạo product page ShopBase + CRO/upsell (+ nhãn GPSR EU)

**Department:** Merchandising (mer) · **AI Worker:** Product Page AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Gate publish của store: product page KHÔNG được publish nếu thiếu nhãn GPSR cho đơn EU (clearance từ SOP-BCK-004) hoặc dính từ khóa IP/TM tên breed.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tạo product page ShopBase (Dog Breed AOP Leggings) bán bằng cảm xúc, tối ưu chuyển đổi mobile, có upsell/bundle + nhãn GPSR (EU), sẵn sàng publish. |
| **Phạm vi** | Soạn nội dung page (copy/CRO/upsell/social proof/images). Publish thực hiện ở MER-004. |
| **Trigger** | Có cleared design (PRD-004) + AOP product (MER-002) + pricing (MER-003). |

### IPO
| | |
|---|---|
| **Input** | Cleared design + IP/TM log (PRD-004), mockups (MER-002), pricing (MER-003), GPSR clearance (BCK-004) |
| **Control** | ShopBase CRO rules (mobile-first, upsell sports bra), GPSR labeling (đơn EU), brand voice (EN), Meta Ad Policy align, không từ khóa IP/TM breed |
| **Output** | Product page publish-ready (EN) |
| **Mechanism** | Product Page AI + Claude API, ShopBase API, Printify mockup gen |

## 2. ShopBase CRO checklist (Knowledge)
- **Hook (identity):** mở bằng danh tính breed — "For Golden Retriever moms only 🐾"; emotion trước feature
- **Above-the-fold (mobile):** offer rõ, ảnh AOP mạnh nhất, sticky Add-to-Cart, star rating
- **Body:** benefits → AOP feature (squat-proof, 4-way stretch, **size XS–3XL**) → **size guide** → care
- **Upsell/bundle:** cấu hình bundle/post-ATC upsell **sports bra cùng design** → đẩy AOV $75–95
- **Social proof:** review/UGC block, "dog-mom community", urgency hợp lệ (không claim sai)
- **Ảnh:** ≥ 5 mockup AOP 360° + 1 size chart; ảnh đầu là ảnh mạnh nhất trên mobile
- **GPSR block (đơn EU):** nhà sản xuất + Responsible Person EU + cảnh báo (nếu có)

## 3. RACI
| Hoạt động | Founder | Product Page AI | Compliance AI (05) |
|---|---|---|---|
| Soạn copy/CRO/upsell | I | **R** | I |
| Chèn nhãn GPSR (đơn EU) | I | R | **C** (cấp clearance) |
| Spot-check page | C | R | I |

## 4. Đầu vào
- [ ] Cleared design + IP/TM log · [ ] Mockups AOP · [ ] Pricing · [ ] **GPSR clearance (BCK-004)**

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Angle | Xác định identity angle theo breed (đồng bộ FB Creative) | [AI WORKFORCE] | Theo niche brief thật |
| 5.2 | Copy & CRO | Viết hook → benefits → AOP feature; mobile-first, sticky ATC | [AI AUGMENT] | Template; có size guide |
| 5.3 | Upsell/bundle | Cấu hình upsell sports bra cùng design (AOV $75–95) | [AI AUGMENT] | Bắt buộc có upsell |
| 5.4 | Social proof/images | Review/UGC block + ≥5 mockup AOP + size chart | [AI WORKFORCE] | Checklist ảnh + social proof |
| 5.5 | GPSR | Chèn nhãn GPSR (đơn EU) từ clearance BCK-004 | [AI AUGMENT] | Đơn EU không có clearance → BLOCK |
| 5.6 | IP/TM recheck | Quét tên breed không trùng TM đã đăng ký + không brand/character | [AI WORKFORCE] | Block nếu dính IP/TM |
| 5.7 | Handoff | Page publish-ready → MER-004 | [AI WORKFORCE] | Gate đủ điều kiện |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | CRO block | offer/CTA/size guide/social proof đủ | 100% | ☐ |
| 2 | Upsell/bundle | sports bra present | 100% | ☐ |
| 3 | Ảnh | ≥ 5 mockup AOP + size chart | 100% | ☐ |
| 4 | **GPSR (đơn EU)** | nhãn present | 100% | ☐ |
| 5 | IP/TM breed | 0 từ khóa vi phạm | 100% | ☐ |

**Quyết định:** ALL pass → MER-004 publish. GPSR (EU)/IP-TM fail → **BLOCK** (không loop "cho qua") → escalate.

## 7. Output & Downstream
- **Lưu:** ./output/page_[sku]_READY.md → archive/ · **Downstream:** MER-004 (publish), MER-003 (giá), FB Creative AI (angle)

## 8. Phụ lục
Doc: ../listing-template-style.md · GPSR: ../../05-backoffice/gpsr-compliance/ · Channel: ../../_shared/channel-config/ · Niche: ../../docs/08-niche-dog-breed-leggings-shopbase.md
