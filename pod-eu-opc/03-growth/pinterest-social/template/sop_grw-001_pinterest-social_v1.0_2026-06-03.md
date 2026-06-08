# SOP-GRW-001 — Organic social & community

**Department:** Growth (grw) · **AI Worker:** Marketing AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Organic social & community HỖ TRỢ FB Ads (kéo CPM xuống, tạo social proof), KHÔNG thay thế. Kênh chính: IG/TikTok reels + FB dog-mom groups + UGC seeding. Pinterest chỉ là tùy chọn phụ.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tạo & lên lịch organic social + engage community dog-mom để tạo social proof, UGC và giảm CPM cho FB Ads. |
| **Phạm vi** | IG/TikTok reels, FB dog-mom groups, UGC seeding (Pinterest tùy chọn phụ). Paid Ads là GRW-002. |
| **Trigger** | Product/design live; UGC từ khách/influencer; lịch nội dung tuần; dịp mùa vụ. |

### IPO
| | |
|---|---|
| **Input** | Product live + mockup/design, UGC (review khách/micro-influencer), brand voice, breed angle |
| **Control** | Brand policy, Meta/platform policy, quyền sử dụng UGC, không tên breed TM (IP) |
| **Output** | Organic posts/community engagement đã lên lịch + UGC seeded |
| **Mechanism** | Marketing AI + Claude API, Canva, IG/TikTok/FB, scheduler |

## 2. Knowledge
- Organic = social proof + UGC → giảm CPM, tăng trust cho FB Ads, không phải kênh traffic chính.
- Reels theo breed (Golden Retriever/French Bulldog/Corgi/Dachshund) viral nhờ comment tagging.
- FB dog-mom groups: engage tự nhiên, seed UGC; mọi post link/CTA về product page ShopBase.

## 3. RACI
| Hoạt động | Founder | Marketing AI |
|---|---|---|
| Tạo & lên lịch organic/community | I | **R** |
| Duyệt campaign community lớn | C | R |

## 4. Đầu vào
- [ ] Product live + mockup/design · [ ] Brand voice · [ ] Breed angle · [ ] UGC (có quyền)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Chọn product | Lấy product/design live cần đẩy | [AI WORKFORCE] | Chỉ đẩy product đang live |
| 5.2 | Tạo content | Reel/post IG/TikTok/FB (breed angle) nhiều biến thể | [AI AUGMENT] | Tránh tên breed TM |
| 5.3 | UGC seeding | Seed UGC vào post + dog-mom community | [AI AUGMENT] | Chỉ dùng UGC có quyền |
| 5.4 | Lên lịch + engage | Schedule rải đều + engage community | [AI WORKFORCE] | Đủ tần suất; link product đúng |
| 5.5 | Track | Theo dõi engagement/click → GRW-004 | [AI WORKFORCE] | — |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Tần suất | posts/tuần | đều đặn (hỗ trợ ads) | ☐ |
| 2 | Link đúng | % post link tới product đúng | 100% | ☐ |
| 3 | UGC quyền | % UGC có quyền sử dụng | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/organic-social_[YYYY-Wnn].md → archive/ · **Downstream:** GRW-004 (report), social proof/UGC → FB Creative AI (GRW-005), hỗ trợ CPM → FB Ads (GRW-002)

## 8. Phụ lục
Niche spec: ../../../docs/08-niche-dog-breed-leggings-shopbase.md §5 · Mùa vụ: ../../../01-product-studio/trend-seasonal-scan/ · FB Creative (GRW-005): ../../fb-creative/template/sop_grw-005_fb-creative_v1.0_2026-06-03.md
