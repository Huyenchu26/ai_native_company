# SOP-GRW-001 — Pinterest & social content

**Department:** Growth (grw) · **AI Worker:** Marketing AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Pinterest là kênh organic mạnh nhất cho POD apparel: nội dung sống lâu, ý định mua cao, dẫn traffic miễn phí về listing.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Tạo & lên lịch pin/social kéo traffic chất lượng về listing live, tăng visibility không tốn phí. |
| **Phạm vi** | Pinterest (chính) + social phụ (IG/FB). Quảng cáo trả phí là GRW-002. |
| **Trigger** | Listing live (MER-004); lịch nội dung tuần; dịp mùa vụ (PRD-002). |

### IPO
| | |
|---|---|
| **Input** | Listing live + mockups (MER-004), seasonal calendar (PRD-002), brand voice, keyword Pinterest |
| **Control** | Brand policy, Pinterest SEO, tần suất tối thiểu, không từ khóa IP |
| **Output** | Pin/social posts đã lên lịch + link về listing |
| **Mechanism** | Marketing AI + Claude API, Canva, Pinterest API, scheduler |

## 2. Knowledge
- Pinterest = công cụ tìm kiếm hình ảnh → tối ưu **tiêu đề + mô tả pin theo keyword**.
- Pin tốt: mockup + lifestyle + text overlay rõ; tạo nhiều pin/listing.
- Mỗi pin gắn link trực tiếp tới listing đúng.

## 3. RACI
| Hoạt động | Founder | Marketing AI |
|---|---|---|
| Tạo & lên lịch nội dung | I | **R** |
| Duyệt campaign nội dung lớn | C | R |

## 4. Đầu vào
- [ ] Listing live + mockups · [ ] Brand voice · [ ] Keyword Pinterest · [ ] Lịch mùa vụ

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Chọn listing | Lấy listing live cần đẩy | [AI WORKFORCE] | Chỉ pin listing đang live |
| 5.2 | Tạo pin | Thiết kế pin (mockup + overlay) nhiều biến thể | [AI AUGMENT] | ≥ N pin/listing |
| 5.3 | Pin SEO | Viết tiêu đề + mô tả theo keyword | [AI AUGMENT] | Có keyword; link đúng listing |
| 5.4 | Lên lịch | Schedule rải đều, ưu tiên dịp mùa vụ | [AI WORKFORCE] | Đủ tần suất tối thiểu |
| 5.5 | Track | Theo dõi impression/click → GRW-004 | [AI WORKFORCE] | — |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Tần suất | pins/tuần | ≥ 15 | ☐ |
| 2 | Link đúng | % pin link tới listing đúng | 100% | ☐ |
| 3 | SEO | pin có keyword + mô tả | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/pins_[YYYY-Wnn].md → archive/ · **Downstream:** GRW-004 (report), traffic → listing

## 8. Phụ lục
Brand: ../../_shared/policies/brand-policy.md · Mùa vụ: ../../01-product-studio/trend-seasonal-scan/ · Thiết kế §3.3
