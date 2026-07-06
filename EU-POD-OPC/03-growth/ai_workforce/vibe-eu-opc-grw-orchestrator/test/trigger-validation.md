# Trigger Validation — vibe-eu-opc-grw-orchestrator

Kiểm tra skill **kích hoạt đúng** (SHOULD) và **KHÔNG kích hoạt sai** (SHOULD NOT). Bẫy chính: việc chuyên môn cụ thể phải delegate xuống specialist, việc phòng khác phải escalate.

---

## SHOULD trigger (điều phối Growth — Manager)

| # | Input | Vì sao |
|---|-------|--------|
| 1 | "Chạy đợt promote mới cho 8 SP vừa từ Merch." | Batch end-to-end → fan-out (thuật ngữ 'promote đợt') |
| 2 | "Quản lý growth tháng này, tổng hợp ROAS các niche." | Điều phối toàn phòng + đọc report ('quản lý growth') |
| 3 | "Điều phối marketing: creative xong thì lên ads luôn." | Cross-worker coordination ('điều phối marketing') |
| 4 | "Cho tôi growth report tuần này, có gì cần scale/kill không?" | Đọc growth report + ra quyết định điều phối ('growth report') |
| 5 | "Launch batch sản phẩm mới ra Facebook." | Ngữ cảnh launch batch → orchestrate ('launch batch sản phẩm mới') |

## SHOULD NOT trigger (delegate hoặc escalate — KHÔNG tự làm)

| # | Input | Đúng hành vi |
|---|-------|--------------|
| 1 | "Viết hook 0–3s + script video cho SP Corgi." | **Delegate** → `vibe-eu-opc-grw-creative` (việc creative chuyên môn, KHÔNG tự viết) |
| 2 | "Set ABO test, chỉnh audience LAL 1%, verify CAPI." | **Delegate** → `vibe-eu-opc-grw-fb-ads` (việc chạy ads chuyên môn) |
| 3 | "Soạn email win-back Klaviyo cho khách 60 ngày." | **Delegate** → `vibe-eu-opc-grw-marketing` (việc email chuyên môn) |
| 4 | "Đơn #1234 chưa có tracking, khách hỏi." | **Escalate** → 04-fulfillment-cx (phòng khác) |
| 5 | "Khai VAT OSS quý này và reconcile cost ads." | **Escalate** → 05-finance (phòng khác) |

---

## Bẫy quan trọng
- Skill là **Manager** — nếu input là **một việc chuyên môn đơn lẻ** (viết 1 creative, set 1 campaign, gửi 1 email), KHÔNG execute mà **route** xuống đúng specialist.
- Việc thuộc **phòng khác** (fulfillment, finance, compliance clearance, niche/design, live product) → **escalate** theo matrix, KHÔNG xử lý.
- Chỉ "ôm" trọn vẹn khi là **điều phối đa-worker** hoặc **đợt promote end-to-end**.

**PASS khi:** 5/5 SHOULD trigger + route/orchestrate; 5/5 SHOULD NOT chuyển sang delegate/escalate đúng đích.
