# SOP-PRD-003 — Design brief & production

**Department:** Product Studio (prd) · **AI Worker:** Design AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Biến validated niche thành **design print-ready** đúng chuẩn kỹ thuật, đủ biến thể. |
| **Phạm vi** | Brief → tạo → export print-ready. QC & IP clearance là PRD-004. |
| **Trigger** | Có validated niche từ PRD-001 / opportunity từ PRD-002. |

### IPO
| | |
|---|---|
| **Input** | Validated niche list (PRD-001), brand guidelines, print spec theo sản phẩm |
| **Control** | Print-ready spec, brand voice/visual, phù hợp vùng in apparel |
| **Output** | Design file print-ready + design brief + concept variations |
| **Mechanism** | Design AI + Claude API (brief/prompt), image-gen (Midjourney/Ideogram/DALL·E), Printify mockup |

## 2. Print-ready spec (Knowledge)
- **Độ phân giải:** ≥ 300 DPI
- **Định dạng:** PNG nền trong suốt (transparent)
- **Kích thước:** theo product Printify (DTG thường ~4500×5400 px)
- **Vùng in an toàn:** giữ trong print area; tránh chi tiết sát mép
- **Màu:** RGB; lưu ý chênh màu in; tránh full-bleed trừ AOP (all-over-print)
- **Biến thể:** chuẩn bị bản cho nền áo sáng & tối nếu cần

## 3. RACI
| Hoạt động | Founder | Design AI |
|---|---|---|
| Tạo & export design | I | **R** |
| Duyệt hướng sáng tạo lớn | C | R |

## 4. Đầu vào
- [ ] Validated niche (PRD-001) · [ ] Brand guidelines · [ ] Print spec product mục tiêu

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Brief | Soạn design brief từ niche (thông điệp, style, audience) | [AI AUGMENT] | Brief template chuẩn |
| 5.2 | Concept | Sinh nhiều concept (prompt image-gen) | [AI AUGMENT] | ≥ N concept để chọn |
| 5.3 | Chọn & refine | Chọn concept tốt nhất, tinh chỉnh | [AI AUGMENT] | Đối chiếu brand fit |
| 5.4 | Export | Xuất print-ready đúng spec §2 | [AI WORKFORCE] | Auto-check DPI/size/format trước khi lưu |
| 5.5 | Handoff QC | Chuyển design + brief sang PRD-004 | [AI WORKFORCE] | Không qua MER khi chưa QC |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Kỹ thuật | DPI/size/format đúng spec | 100% | ☐ |
| 2 | Vùng in | nằm trong print area | 100% | ☐ |
| 3 | Số concept | đủ tối thiểu để chọn | đạt | ☐ |
| 4 | Brand fit | đúng visual/voice | đạt | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/design_[niche]_[YYYY-MM-DD]/ (file + brief) → archive/
- **Downstream:** PRD-004 (QC + IP) → MER-001/MER-002

## 8. Phụ lục
Knowledge: ../_knowledge/ · Policy brand: ../../_shared/policies/brand-policy.md · Thiết kế §3.1
