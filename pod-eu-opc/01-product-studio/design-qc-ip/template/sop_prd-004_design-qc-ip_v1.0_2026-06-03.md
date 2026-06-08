# SOP-PRD-004 — Design QC + IP/TM clearance

**Department:** Product Studio (prd) · **AI Worker:** Design AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE (rào IP/TM — rủi ro ban ads + gỡ shop cao nhất)**

> ⚠️ Vi phạm IP/TM là rủi ro **đóng shop + ban ads (Meta)** lớn nhất của POD. Gate này BẮT BUỘC trước khi design sang Merchandising. Nghi ngờ = loại hoặc escalate Founder.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Kiểm chất lượng in AOP 360° + clearance bản quyền/trademark (đặc biệt **tên breed**) TRƯỚC khi listing. |
| **Phạm vi** | Mọi AOP design từ PRD-003. |
| **Trigger** | Có AOP design print-ready chờ clearance. |

### IPO
| | |
|---|---|
| **Input** | AOP design print-ready + brief (PRD-003) |
| **Control** | AOP print spec, luật IP/TM (trademark/copyright/publicity rights), Meta Ad Policy, ShopBase TOS |
| **Output** | Cleared design + IP-clearance log (hoặc rejected/escalated) |
| **Mechanism** | Design AI + Claude API, EUIPO TMview, USPTO TESS, reverse image search |

## 2. Rủi ro IP/TM (Knowledge)
| Loại | Ví dụ cấm | Cách kiểm |
|---|---|---|
| **Trademark (tên breed)** | breed name đã đăng ký TM, brand/logo/slogan | EUIPO TMview, USPTO TESS — dùng mô tả chung thay tên TM |
| **Copyright** | nhân vật (Disney/Marvel), lời bài hát (funny quote), artwork người khác | nhận diện + reverse image |
| **Publicity rights** | tên/ảnh người nổi tiếng | rà tên riêng |
> **Quy tắc:** nghi ngờ → **loại** hoặc escalate Founder. Không "thử vận may" (ban ads = mất ad account).

## 3. RACI
| Hoạt động | Founder | Design AI |
|---|---|---|
| QC kỹ thuật AOP 360° | I | **R** |
| IP/TM scan | I | **R** |
| Duyệt case rủi ro | **A** | C |

## 4. Đầu vào
- [ ] AOP design print-ready (PRD-003) · [ ] Truy cập công cụ tra trademark (EUIPO/USPTO)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | QC AOP 360° | Verify DPI/size/format + pattern seamless full-bleed quanh chân/đường may | [AI WORKFORCE] | Auto-check; fail → trả PRD-003 |
| 5.2 | IP/TM scan | Rà trademark (tên breed)/copyright/publicity theo §2 | [AI AUGMENT] | Checklist 3 loại; ≥1 tool trademark |
| 5.3 | Risk rating | Gán mức rủi ro (low/med/high) | [AI AUGMENT] | Med/High → bắt buộc người duyệt |
| 5.4 | Quyết định | Clear / loại / escalate Founder | [AI ASSIST] | High risk → escalate, không tự clear |
| 5.5 | Log | Ghi IP-clearance log + handoff MER-001 | [AI WORKFORCE] | Listing không có log → MER-001 không publish |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | IP/TM scan coverage | % design qua scan | 100% | ☐ |
| 2 | Vi phạm lọt | design vi phạm IP/TM lọt | 0 | ☐ |
| 3 | Kỹ thuật AOP 360° | technical pass | ≥ 95% | ☐ |
| 4 | Case rủi ro | High-risk có Founder duyệt | 100% | ☐ |

**Quyết định:** pass → cleared → MER-001. Fail/nghi ngờ → loại hoặc escalate (không loop "cho qua").

## 7. Output & Downstream
- **Lưu:** ./output/ip-clearance-log_[YYYY-MM].md + cleared designs → archive/
- **Downstream:** MER-001 (Product Page — gate publish); cleared design → FB Creative AI (GRW-005)

## 8. Phụ lục
Policy IP: ../../../_shared/policies/ip-policy.md · Liên quan GPSR (đơn EU): ../../../05-backoffice/ · Niche strategy §8 (rủi ro IP): ../../../docs/08-niche-dog-breed-leggings-shopbase.md
