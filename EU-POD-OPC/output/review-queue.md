# DAKOfits — HITL Review Queue

**Phiên bản:** 1.2 · **Ngày:** 2026-07-31

> Mọi artifact có `confidence_score < 0.7` hoặc `need_review = true` được tổng hợp ở đây cho Owner duyệt trước khi commit.

| # | Artifact | Loại | confidence | Lý do cần review | Quyết định Owner |
|---|----------|------|-----------|------------------|------------------|
| 1 | Company OKR O3 (Stretch x10) | OKR target | 0.40 | Mốc 5 tỷ/tháng + 100 winner SKU không có benchmark | ✅ **RESOLVED 2026-06-23** — Owner chốt giữ 500tr/tháng (solo capacity), bỏ moonshot. O3 đổi thành automation (≤2h thao tác/ngày, ≥90% đơn zero-touch). |
| 2 | Department Stretch OKR (5 phòng) | OKR target | <0.7 | Moonshot x10 cấp phòng | ⏳ **PENDING** — khuyến nghị chỉnh tương tự O3: stretch hướng tự động hóa/hiệu suất, KHÔNG đẩy volume vượt năng lực solo. Chờ Owner xác nhận có muốn tôi sửa đồng loạt 5 phòng không. |

## Quyết định từ Full Audit (2026-07-31) — chi tiết trong [audit-report](../_ai-workforce/audit-report_2026-07-31.md)

> 66 findings toàn công ty (9 CRITICAL / 16 HIGH). Lỗi cơ học đã auto-fix (20 link gãy, 12 `$schema`). 5 nhóm dưới cần Owner quyết trước khi mình sửa hàng loạt.

| ID | Quyết định | Mức | Khuyến nghị | Owner |
|----|-----------|:---:|-------------|-------|
| **D1** | Namespace: gộp về 1 lớp `vibe-eu-opc-*` hay giữ mô hình 2 lớp legacy+EU? Hiện SOP/roster/charter (~75 file) trỏ tên `vibe-opc-pod-*` không khớp folder skill thật. | 🔴 | **Gộp 1 lớp** `vibe-eu-opc-*`; rename cơ học toàn repo; bỏ mô tả legacy trong workforce-map/build-plan. | ⏳ PENDING |
| **D2** | ROAS/margin: bỏ hẳn `ROAS≥2.5` + gate `gross margin ≥45%` ở tầng governance, chuyển sang **BE-ROAS per-SKU + contribution floor** (đồng bộ tầng skill/unit-economics). Evidence OKR-Growth "GM 45–55%" đang sai (thật US 36.4%/EU 23%). | 🔴 | Reconcile OKR/KPI/KRI/_knowledge của MER+GRW+BCK về BE-ROAS (US ~2.75/EU ~5.3); sửa evidence GM về số thật. | ⏳ PENDING |
| **D3** | Roster/RACI: thêm **orchestrator (W0)** + SOP thiếu (PRD-005, MER-005) vào coverage 5 phòng; chốt **chủ sở hữu gate IP/TM G3** (Product Studio quyết CLEAR hay chỉ pre-check rồi Backoffice ký?). | 🟠 | Thêm W0 vào mọi `_skills-agents`; chốt: PRD pre-check → BCK-compliance ký clearance chính thức. | ⏳ PENDING |
| **D4** | Chốt 1 giá trị cho các ngưỡng đang lệch SOP↔skill: **KILL ROAS 1.5 vs 1.8**; routing on-time **18h vs 24h**; tracking **6h vs 12h**; enum clearance **PASS vs CLEAR**; IP pre-flag 3 enum; upscale (cấm vs dùng); human-review sample 20% (giữ vs bỏ). | 🟠 | Lấy giá trị **chặt hơn** làm chuẩn (1.8 / 18h / 6h / CLEAR); sửa đồng loạt 2 tầng. | ⏳ PENDING |
| **D5** | Compliance + Output QC (ưu tiên cao nhất): (a) **GPSR nhãn bản ngữ** theo nước bán (không EN-only); (b) **VAT thêm nhánh domestic** (in&giao cùng nước → VAT local); (c) **regenerate output** đạt schema + thêm `evidence[]` + **re-download ảnh mockup thật** (yoga 0/6, pickleball thiếu size-guide); (d) sửa IP output pickleball "PASS(CLEAR)" khi chưa EUIPO. | 🔴 | **Block publish EU** cho tới khi (a)(b)(d) xong; chạy `validator.py` trên mọi output. | ⏳ PENDING |

## Decision rules
- Owner duyệt → set `need_review=false`, ghi rationale.
- Owner bác → điều chỉnh target về Committed thực tế.
- Chưa duyệt → KHÔNG cam kết target moonshot ra ngoài (chỉ giữ làm directional).
- **D1–D5:** mình chỉ rename/sửa hàng loạt SAU khi Owner chốt hướng — để tránh đụng quyết định kiến trúc/nghiệp vụ.
