# DAKOfits — Quality Management

**Phiên bản:** 1.0 · **Ngày:** 2026-06-23

> "Build quality IN, don't inspect it IN" (Deming). 94% lỗi do hệ thống — hỏi "Process nào fail?", KHÔNG hỏi "Ai sai?".

---

## 1. Blameless Culture
Mọi incident là learning opportunity. Root cause LUÔN trace về hệ thống (thiếu rule, thiếu check, thiếu prompt, tool chưa đủ). KHÔNG blame AI Worker hay người.

## 2. Severity Levels
| Severity | Định nghĩa | Ví dụ POD |
|----------|-----------|-----------|
| CRITICAL | Mất tiền/ban/legal breach | BM bị ban, GPSR breach đơn EU, GDPR breach |
| HIGH | Ảnh hưởng nhiều đơn/khách | Route trễ >24h hàng loạt, ROAS sụp dưới hòa vốn |
| MEDIUM | Lỗi cục bộ, có workaround | 1 design sai DPI, 1 listing sai giá |
| LOW | Cosmetic, không ảnh hưởng tiền | Typo product page |

## 3. Khi nào tạo Incident Report
- Quality gate fail 3+ loops
- Output bị stakeholder reject
- SLA breach (external promise)
- SLO miss 2 kỳ liên tiếp
- Cùng loại lỗi ≥ 3 lần
- Bất kỳ CRITICAL nào (ngay lập tức)

## 4. RCA bắt buộc
5 Whys hoặc Fishbone (Manpower/Method/Machine/Material/Measurement). KHÔNG dừng ở surface cause ("AI nhập sai"). Phải đến systemic root cause.

## 5. Prevention-first (ưu tiên giảm dần)
ELIMINATE > SUBSTITUTE > DETECT EARLY > DETECT LATE.

## 6. Liên kết quality standards các phòng
- [01 Product](../01-product-studio/quality_prd-001_quality-standards_v1.0_2026-06-23.md)
- [02 Merchandising](../02-merchandising/quality_mer-001_quality-standards_v1.0_2026-06-23.md)
- [03 Growth](../03-growth/quality_grw-001_quality-standards_v1.0_2026-06-23.md)
- [04 Fulfillment & CX](../04-fulfillment-cx/quality_ful-001_quality-standards_v1.0_2026-06-23.md)
- [05 Backoffice](../05-backoffice/quality_bck-001_quality-standards_v1.0_2026-06-23.md)

## 7. Incident Register
[register_incidents_v1.0_2026-06-23.md](./register_incidents_v1.0_2026-06-23.md) · Reports: [reports/](./reports/)
