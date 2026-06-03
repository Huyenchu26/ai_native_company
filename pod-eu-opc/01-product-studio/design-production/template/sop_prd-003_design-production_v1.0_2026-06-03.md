# SOP-PRD-003 — Design brief & production

**Department:** prd
**AI Worker phụ trách:** Design AI
**Loại:** OPERATIONAL (template -> input -> processing -> output -> archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-03 · **Trạng thái:** SKELETON (cần điền chi tiết)

> SOP khung theo framework AI Native Company. Điền nội dung cụ thể theo thực tế vận hành ("Trần sao âm vậy"). Xem thiết kế: ../../../02-design/opc-design-roadmap.md

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | [Vì sao tồn tại SOP này — kết quả nó tạo ra] |
| **Phạm vi** | [Áp dụng cho cái gì / không áp dụng cho cái gì] |
| **Trigger** | [Sự kiện kích hoạt: theo lịch / yêu cầu / đơn hàng / ngưỡng] |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | [Đầu vào — lấy từ SOP/dept nào, đặt trong ./input/] |
| **Control** | [Ràng buộc: policy, EU compliance (VAT/GPSR/GDPR), SLA, brand voice] |
| **Output** | [Kết quả — đi tới SOP/dept nào] |
| **Mechanism** | [Tool/API/skill: Claude API, Etsy API, Printify API, ...] |

## 2. Vai trò & RACI

| Hoạt động | Founder | Design AI | Khác |
|---|---|---|---|
| [Bước chính 1] | A | R | I |
| [Bước chính 2] | I | R | C |

## 3. Đầu vào & Điều kiện bắt đầu

- [ ] [Input bắt buộc đã có trong ./input/]
- [ ] [Điều kiện tiên quyết / phụ thuộc SOP upstream]

## 4. Quy trình

> Tag AI: [AI ASSIST] người làm chính · [AI AUGMENT] AI làm + người duyệt · [AI WORKFORCE] AI tự chạy

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 4.1 | [Tên bước] | [Mô tả] | [AI WORKFORCE] | [Làm sao để lỗi ở bước này KHÔNG THỂ xảy ra] |
| 4.2 | [Tên bước] | [Mô tả] | [AI AUGMENT] | [...] |
| 4.3 | [Tên bước] | [Mô tả] | [...] | [...] |

## 5. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI (đo gì) | SLO (target) | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | [Tiêu chí 1] | [metric] | [target] | [method] | ☐ |
| 2 | [Tiêu chí 2] | [metric] | [target] | [method] | ☐ |

**Quyết định:**
- ALL pass -> Output được chấp nhận -> chuyển ./output/
- ANY fail -> LOOP lại bước liên quan (tối đa 3 lần)
- 3+ loops fail -> ESCALATE Founder -> tạo Incident Report tại ../../../_quality/reports/

## 6. Output & Downstream

- **Lưu tại:** ./output/ ; cuối kỳ chuyển ./archive/[YYYY-MM]/
- **Downstream:** [SOP/dept nhận output tiếp theo]
- **Naming:** sop-prd-003_[mô-tả]_DONE_2026-06-03.md (theo quy ước repo)

## 7. Phụ lục

- **Upstream SOP:** [link]
- **Downstream SOP:** [link]
- **Knowledge:** ../../_knowledge/
- **Rules / Quality Standards:** ../../_rules/ · ../../quality_prd-001_quality-standards_v1.0_2026-06-03.md
- **Thiết kế tham chiếu:** ../../../02-design/opc-design-roadmap.md
