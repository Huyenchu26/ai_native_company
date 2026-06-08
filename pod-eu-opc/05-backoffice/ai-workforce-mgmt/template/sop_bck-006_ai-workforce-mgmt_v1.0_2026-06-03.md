# SOP-BCK-006 — AI workforce management

**Department:** Backoffice (bck) · **AI Worker:** Ops/HR AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> "HR" cho 12 AI Worker: theo dõi uptime, chất lượng output, chi phí, năng lực; weekly report; cập nhật skill/SOP; capacity plan; escalation.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Đảm bảo 12 AI Worker hoạt động ổn định, đạt SLO, chi phí trong budget; phát hiện & vá lỗ hổng năng lực để pipeline đạt target $8,000 (~200 triệu VNĐ)/tháng. |
| **Phạm vi** | Toàn bộ AI Workforce — 12 worker, 5 dept (xem _ai-workforce/). |
| **Trigger** | Hàng tuần (uptime/cost + weekly report) + review hiệu suất hàng tháng. |

### IPO
| | |
|---|---|
| **Input** | AI usage/cost, output quality từ Quality Gate các SOP, SLO compliance, incident log |
| **Control** | Uptime ≥ 99%, cost trong budget (cost-analysis), SLO mỗi worker |
| **Output** | Workforce roster, weekly report, performance review, capacity plan, skill-gap actions |
| **Mechanism** | Ops/HR AI + Claude API, monitoring, _ai-workforce docs |

## 2. RACI
| Hoạt động | Founder | Ops/HR AI |
|---|---|---|
| Duyệt thay đổi workforce/budget | **A** | C |
| Monitor & review | I | **R** |

## 3. Đầu vào
- [ ] AI usage/cost kỳ · [ ] Quality Gate pass/fail các SOP · [ ] Incident log (_quality/)

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Monitor | Theo dõi uptime + cost từng worker (12 worker) | [AI WORKFORCE] | Alert khi uptime <99% hoặc cost vượt |
| 4.2 | Review chất lượng | Tổng hợp quality gate pass-rate theo worker | [AI AUGMENT] | Dùng dữ liệu thật từ SOP |
| 4.3 | Skill-gap | Worker fail lặp → xác định gap → update skill/SOP/knowledge | [AI AUGMENT] | Lỗi lặp ≥3 → bắt buộc cải tiến + escalate |
| 4.4 | Capacity | Dự báo tải pipeline (PRD→MER→GRW→FUL→BCK); đề xuất thêm/bớt/điều chỉnh worker | [AI AUGMENT] | Gắn với khối lượng pipeline thật |
| 4.5 | Weekly report + roster | Cập nhật weekly report + roster + performance report → Founder | [AI WORKFORCE] | Đúng hạn |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Uptime | uptime trung bình (12 worker) | ≥ 99% | ☐ |
| 2 | Performance | mọi worker có score | 100% | ☐ |
| 3 | Cost | tổng cost vs budget | trong budget | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/workforce-roster_[YYYY-MM].md, weekly-report, performance-review → archive/
- **Downstream:** Founder (workforce decisions), _ai-workforce/ (cập nhật map/build-plan)

## 7. Phụ lục
Workforce: ../../_ai-workforce/ (map, build-plan, skills-matrix, cost-analysis) · Niche/stack: ../../docs/08-niche-dog-breed-leggings-shopbase.md §2
