# DAKOfits — HITL Review Queue

**Phiên bản:** 1.1 · **Ngày:** 2026-06-23

> Mọi artifact có `confidence_score < 0.7` hoặc `need_review = true` được tổng hợp ở đây cho Owner duyệt trước khi commit.

| # | Artifact | Loại | confidence | Lý do cần review | Quyết định Owner |
|---|----------|------|-----------|------------------|------------------|
| 1 | Company OKR O3 (Stretch x10) | OKR target | 0.40 | Mốc 5 tỷ/tháng + 100 winner SKU không có benchmark | ✅ **RESOLVED 2026-06-23** — Owner chốt giữ 500tr/tháng (solo capacity), bỏ moonshot. O3 đổi thành automation (≤2h thao tác/ngày, ≥90% đơn zero-touch). |
| 2 | Department Stretch OKR (5 phòng) | OKR target | <0.7 | Moonshot x10 cấp phòng | ⏳ **PENDING** — khuyến nghị chỉnh tương tự O3: stretch hướng tự động hóa/hiệu suất, KHÔNG đẩy volume vượt năng lực solo. Chờ Owner xác nhận có muốn tôi sửa đồng loạt 5 phòng không. |

## Decision rules
- Owner duyệt → set `need_review=false`, ghi rationale.
- Owner bác → điều chỉnh target về Committed thực tế.
- Chưa duyệt → KHÔNG cam kết target moonshot ra ngoài (chỉ giữ làm directional).
