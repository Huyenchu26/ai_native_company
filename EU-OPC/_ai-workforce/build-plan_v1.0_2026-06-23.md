# DAKOfits — AI Workforce Build Plan

**Phiên bản:** 1.0 · **Ngày:** 2026-06-23

> Thứ tự ưu tiên nếu muốn build skill chuyên biệt theo SOP EU-OPC (qua vibe-aiworkforce, Phase 6).

| Priority | Department | Lý do |
|----------|-----------|-------|
| P0 | 03 Growth | FB Ads = 100% traffic, đòn bẩy doanh số trực tiếp |
| P0 | 02 Merchandising | Ra hàng nhanh = đầu vào cho ads |
| P1 | 01 Product Studio | Pipeline niche → design nuôi catalog |
| P1 | 04 Fulfillment & CX | Giữ on-time + rating khi scale đơn |
| P2 | 05 Backoffice | Gate compliance + tài chính (gate cứng GPSR/Meta) |

## Hiện trạng
12 skill `vibe-opc-pod-*` đã cài sẵn — dùng được ngay, KHÔNG bắt buộc build mới. Build mới chỉ khi cần skill bám sát SOP folder state machine của EU-OPC (đọc template/, xử lý input→processing→output→archive).

## Activation command
- 1 phòng: `/vibe-aiworkforce` → COMPANY_ROOT=d:/VSF/POD-OPC/EU-OPC, department=[xx]
- Company GPS: `/vibe-company-orchestrator` → "Tạo company GPS"
