# SOP-PRD-004 — Design QC + IP/copyright clearance

**Department:** Product Studio (prd) · **AI Worker:** Design AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE (rào IP — rủi ro gỡ shop cao nhất)**

> ⚠️ Vi phạm IP là rủi ro **đóng shop** lớn nhất của POD. Gate này BẮT BUỘC trước khi design sang Merchandising. Nghi ngờ = loại hoặc escalate Founder.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Kiểm chất lượng in + clearance bản quyền/trademark TRƯỚC khi listing. |
| **Phạm vi** | Mọi design từ PRD-003. |
| **Trigger** | Có design print-ready chờ clearance. |

### IPO
| | |
|---|---|
| **Input** | Design print-ready + brief (PRD-003) |
| **Control** | Print spec, luật IP (trademark/copyright/publicity rights), chính sách Etsy |
| **Output** | Cleared design + IP-clearance log (hoặc rejected/escalated) |
| **Mechanism** | Design AI + Claude API, EUIPO TMview, USPTO TESS, reverse image search |

## 2. Rủi ro IP (Knowledge)
| Loại | Ví dụ cấm | Cách kiểm |
|---|---|---|
| **Trademark** | tên brand, logo, slogan đã đăng ký | EUIPO TMview, USPTO TESS |
| **Copyright** | nhân vật (Disney/Marvel), lời bài hát, artwork người khác | nhận diện + reverse image |
| **Publicity rights** | tên/ảnh người nổi tiếng | rà tên riêng |
> **Quy tắc:** nghi ngờ → **loại** hoặc escalate Founder. Không "thử vận may".

## 3. RACI
| Hoạt động | Founder | Design AI |
|---|---|---|
| QC kỹ thuật | I | **R** |
| IP scan | I | **R** |
| Duyệt case rủi ro | **A** | C |

## 4. Đầu vào
- [ ] Design print-ready (PRD-003) · [ ] Truy cập công cụ tra trademark

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | QC kỹ thuật | Verify DPI/size/format/print area | [AI WORKFORCE] | Auto-check; fail → trả PRD-003 |
| 5.2 | IP scan | Rà trademark/copyright/publicity theo §2 | [AI AUGMENT] | Checklist 3 loại; ≥1 tool trademark |
| 5.3 | Risk rating | Gán mức rủi ro (low/med/high) | [AI AUGMENT] | Med/High → bắt buộc người duyệt |
| 5.4 | Quyết định | Clear / loại / escalate Founder | [AI ASSIST] | High risk → escalate, không tự clear |
| 5.5 | Log | Ghi IP-clearance log + handoff MER-001 | [AI WORKFORCE] | Listing không có log → MER-001 không publish |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | IP scan coverage | % design qua scan | 100% | ☐ |
| 2 | Vi phạm lọt | design vi phạm lọt | 0 | ☐ |
| 3 | Kỹ thuật | technical pass | ≥ 95% | ☐ |
| 4 | Case rủi ro | High-risk có Founder duyệt | 100% | ☐ |

**Quyết định:** pass → cleared → MER-001. Fail/nghi ngờ → loại hoặc escalate (không loop "cho qua").

## 7. Output & Downstream
- **Lưu:** ./output/ip-clearance-log_[YYYY-MM].md + cleared designs → archive/
- **Downstream:** MER-001 (listing — gate publish)

## 8. Phụ lục
Policy IP: ../../_shared/policies/ip-policy.md · Liên quan GPSR: ../../05-backoffice/gpsr-compliance/ · Thiết kế §6.4
