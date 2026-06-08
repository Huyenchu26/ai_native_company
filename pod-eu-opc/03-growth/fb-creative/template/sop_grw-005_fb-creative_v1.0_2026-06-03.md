# SOP-GRW-005 — FB ad creative production

**Department:** Growth (grw) · **AI Worker:** FB Creative AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Hook 3 giây đầu quyết định 80% kết quả. Mỗi ad set cần ≥3 creative variations. Mọi creative phải đạt Meta Ad Policy trước khi bàn giao FB Ads.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Biến design winner thành ad creative (image/video/carousel + script) chạm cảm xúc dog-mom, sẵn cho FB Ads Specialist AI test/scale. |
| **Phạm vi** | Ad creative brief, video script (hook/body360/CTA), UGC brief, carousel copy cho Dog Breed AOP Leggings. |
| **Trigger** | Có design winner/mockup mới (Design AI); ad set bị fatigue cần refresh (signal GRW-002); dịp mùa vụ. |

### IPO
| | |
|---|---|
| **Input** | Design winner + mockup (Design AI), angle theo breed/persona, niche spec (docs §5) |
| **Control** | Meta Ad Policy, IP/TM breed, quyền sử dụng UGC, hook ≤3s |
| **Output** | Creative package (image/video/carousel + script + UGC brief) |
| **Mechanism** | FB Creative AI + Claude API, Canva, CapCut/Premiere template, Meta Creative Hub, Printify mockup |

## 2. Knowledge
- **Hook (0–3s):** hình leggings mặc + chó cùng giống; text overlay rõ angle "For Golden Retriever moms only 🐾".
- **Body (3–10s):** xoay 360° show AOP; highlight squat-proof, 4-way stretch, size XS–3XL.
- **CTA:** "Tag a Golden Retriever mom" (viral comment) hoặc "Limited sizes — shop now" (urgency); link product page ShopBase.
- **Nguồn creative:** UGC từ micro-influencer dog niche (đổi sản phẩm); self-shoot; Canva slideshow + Printify 3D mockup.

## 3. RACI
| Hoạt động | Founder | FB Creative AI | Compliance AI (05) | FB Ads Specialist AI |
|---|---|---|---|---|
| Tạo creative/script/brief | I | **R** | I | C |
| Verify Meta Ad Policy | I | C | **R** | I |
| Hợp tác UGC trả phí lớn | **A** | R | I | I |
| Nhận & chạy creative | I | C | I | **R** |

## 4. Đầu vào
- [ ] Design winner + mockup (Design AI) · [ ] Angle theo breed/persona · [ ] Niche spec §5 · [ ] Asset/quyền UGC (nếu có)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Creative brief | Xác định angle breed + persona dog-mom | [AI AUGMENT] | Bám niche spec; tránh tên breed TM |
| 5.2 | Video script | Soạn hook (0–3s) → body 360° → CTA | [AI AUGMENT] | Hook ≤3s đặt đầu; text overlay rõ angle |
| 5.3 | Carousel + UGC brief | Carousel copy (breed/variation + bundle) + brief gửi influencer | [AI AUGMENT] | UGC chỉ dùng khi có quyền/consent |
| 5.4 | Tạo asset | Canva/CapCut → ≥3 variations/ad set (image/video/carousel) | [AI WORKFORCE] | ≥3 variations/ad set |
| 5.5 | Policy check | Check Meta Ad Policy + IP/TM | [AI WORKFORCE] | Block nếu chưa đạt |
| 5.6 | Bàn giao | Gửi creative package → FB Ads Specialist AI (GRW-002) | [AI WORKFORCE] | — |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Variations | creative/ad set | ≥ 3 | ☐ |
| 2 | Hook | hook ≤3s rõ angle | 100% | ☐ |
| 3 | Policy | đạt Meta Ad Policy + IP/TM | 100% | ☐ |

**Quyết định:** Creative dính Meta Ad Policy hoặc tên breed TM → block, không bàn giao. UGC không có quyền sử dụng → không dùng.

## 7. Output & Downstream
- **Lưu:** ./output/creative-package_[breed]_[YYYY-Wnn].md → archive/ · **Downstream:** GRW-002 (FB Ads chạy), Compliance AI (Meta Ad Policy log)

## 8. Phụ lục
Niche spec & công thức creative: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §5 · FB Ads (GRW-002): ../../fb-ads/template/sop_grw-002_fb-ads_v1.0_2026-06-03.md
