# Trigger Validation — vibe-eu-opc-mer-orchestrator

Kiểm description trigger đúng (SHOULD) và không bắt nhầm (SHOULD NOT). Bẫy: việc chuyên môn phải delegate, việc phòng khác phải từ chối.

---

## SHOULD trigger (5)

| # | Câu người dùng | Lý do |
|---|----------------|-------|
| 1 | "Lên lô 8 sản phẩm mới đợt này, đưa ra bán." | Promote theo đợt (SOP-MER-006) — đúng core. |
| 2 | "Có batch design mới cleared từ Product Studio cần publish." | Ngữ cảnh handoff design → Merch điều phối. |
| 3 | "Quản lý catalog AOP leggings tuần này." | Thuật ngữ 'catalog' — điều phối phòng Merch. |
| 4 | "Promote đợt SP Beagle + Husky rồi bàn giao Growth chạy ads." | 'promote đợt' + handoff Growth — đúng vai trò manager. |
| 5 | "Đưa nhóm SP mùa Giáng sinh ra listing." | 'listing' / 'đưa SP ra bán' — điều phối setup→publish. |

## SHOULD NOT trigger (5) — route/từ chối, KHÔNG tự làm

| # | Câu người dùng | Phải route/từ chối đến |
|---|----------------|------------------------|
| 1 | "Tính giá variant XS–3XL cho SP này." | → `vibe-eu-opc-mer-catalog` (MER-003). Việc chuyên môn, không tự execute. |
| 2 | "Viết product page copy + upsell cho SP Corgi." | → `vibe-eu-opc-mer-product-page` (MER-001). |
| 3 | "Chạy FB Ads + tối ưu ROAS cho đợt này." | → `vibe-eu-opc-grw-orchestrator` (GRW-002). Việc phòng Growth. |
| 4 | "Tạo design AOP 300 DPI + IP clearance cho breed mới." | → `vibe-opc-pod-product-design` (phòng 01). Việc Product Studio. |
| 5 | "Làm tờ khai VAT EU + P&L tháng." | → phòng 05-backoffice / finance. Việc phòng khác hẳn. |

---
**Pass:** cả 5 SHOULD kích hoạt manager (route/orchestrate), cả 5 SHOULD NOT được delegate đúng địa chỉ hoặc từ chối — manager KHÔNG tự setup/pricing/page/ads.
