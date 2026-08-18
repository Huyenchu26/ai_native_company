# SOP-PRD-002 — Blanket Personalization Design (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 01-Product Studio · **Responsible AI:** `vibe-us-warm-prd-design`
**Product:** Personalized fleece/sherpa blanket · **Personalization:** name · photo · message · pet-memorial

---

## 1. Tổng quan & Mục tiêu
Thiết kế **template cá nhân hoá chăn** (KHÔNG phải AOP pattern). Mỗi design = một **layout template** nhận biến cá nhân hoá (tên, ảnh khách, thông điệp) + đủ điều kiện in đúng chất lượng đối thủ đang yếu (chống "chăn mỏng/không đúng mô tả").

Khác model cũ: **không có "AOP 300 DPI toàn mặt"**. Chăn cá nhân hoá = nền design + vùng chèn biến (variable data). QC tập trung: vùng an toàn (safe area), độ phân giải ảnh khách, spec vật liệu.

## 2. IPO / ICOM
- **Input:** validated niche (PRD-001), personalization spec (fields), supplier print spec (blanket size, DPI vùng in, material GSM).
- **Control:** print-area safe margin; ảnh khách ≥ min DPI ở kích thước in thật (KHÔNG upscale); material spec ≥ ngưỡng brand-promise; IP status = CLEAR (từ PRD-003).
- **Output:** `design-spec.json` (schema `design-spec.schema.json`) — layout template + variable slots + material spec + IP status; mockup preview brief (handoff mer-visual).
- **Mechanism:** design tool, supplier spec sheet, personalization preview renderer.

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Layout template | Thiết kế nền + vùng chèn tên/ảnh/message theo niche | Vùng chữ/ảnh nằm trong safe-area, tránh mép seam |
| 3.2 | Variable-data spec | Định nghĩa field cá nhân hoá + giới hạn (max ký tự, ảnh ratio, DPI tối thiểu) | Ảnh khách < min DPI ở size in → REJECT (KHÔNG upscale) |
| 3.3 | Material spec | Chốt loại vải (fleece/sherpa) + GSM ≥ ngưỡng brand-promise | Không chọn vải dưới ngưỡng để rẻ (chống "chăn mỏng") |
| 3.4 | IP check-in | Xác nhận IP status = CLEAR từ PRD-003 (name/quote/photo) | Chưa CLEAR → design_status=PENDING, KHÔNG handoff |
| 3.5 | Preview brief | Mô tả mockup preview để mer-visual render (personalization preview) | Không tự khai "đã render" nếu chưa có tool |
| 3.6 | QC self-check | Safe-area OK, DPI OK, material OK, IP CLEAR | Bất kỳ fail → design_status ≠ CLEAR |

## 4. RACI
- **R:** `vibe-us-warm-prd-design` · **A:** Owner · **C:** `vibe-us-warm-prd-niche-research`, `vibe-us-warm-bck-compliance` (IP) · **I:** merchandising (mer-visual/mer-catalog).
- **HITL:** ảnh khách chất lượng biên; material dưới ngưỡng; IP uncertain → Owner.

## 5. Quality Gate (SLI → SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | Personalization DPI | ≥ min DPI @ print size (no upscale) | validator | fail → REJECT/re-source ảnh |
| 2 | Safe-area compliance | 100% chữ/ảnh trong safe margin | design check | fail → sửa layout |
| 3 | Material spec | GSM ≥ ngưỡng brand-promise | supplier spec | fail → đổi vải, không hạ ngưỡng |
| 4 | IP status | = CLEAR (từ PRD-003) | handoff gate | ≠ CLEAR → design_status=PENDING |
| 5 | Evidence | ≥1 verbatim evidence/claim | validator `--run-all` | thiếu → confidence −0.2 |

**Gate handoff:** design_status = `CLEAR` CHỈ khi (1)(2)(3) pass VÀ IP=CLEAR. Enum: `CLEAR / MODIFY / REJECT / PENDING` (có PENDING cho fail-closed). `handoff_ready=true ⇒ design_status=CLEAR ∧ ip_status=CLEAR` (enforce bằng schema allOf/if-then).

## 6. Links
- Upstream niche: [SOP-PRD-001](../../research-niche/template/sop_prd-001_gift-niche-research_v1.0_2026-08-04.md)
- IP: [SOP-PRD-003](../../clear-ip/template/sop_prd-003_ip-tm-clearance-us_v1.0_2026-08-04.md)
- Downstream mockup: 02-merchandising personalization-preview (mer-visual)

## 7. History
| Ver | Date | Change |
|-----|------|--------|
| 1.0 | 2026-08-04 | Khởi tạo — personalization design cho chăn US (thay AOP 300 DPI). Enum design_status có PENDING (fix P3). |
