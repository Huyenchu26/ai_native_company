# Trigger Validation — vibe-eu-opc-bck-orchestrator

Kiểm tra skill **kích hoạt đúng** (SHOULD) và **KHÔNG kích hoạt sai** (SHOULD NOT). Bẫy chính: việc chuyên môn cụ thể phải delegate xuống 3 specialist; việc phòng L2 khác phải escalate.

---

## SHOULD trigger (điều phối Backoffice — Manager)

| # | Input | Vì sao |
|---|-------|--------|
| 1 | "Chốt vận hành tháng 6, làm CEO brief cho sếp." | Chốt kỳ end-to-end → fan-out 3 specialist (thuật ngữ 'CEO brief', 'chốt vận hành tháng') |
| 2 | "Điều phối backoffice tháng này: tài chính tổng + tình trạng tuân thủ." | Điều phối toàn phòng L3 ('điều phối backoffice', 'tài chính tổng') |
| 3 | "Cuối kỳ tổng hợp tài chính và tuân thủ, có gì cần Owner duyệt không?" | Ngữ cảnh cuối kỳ tổng hợp finance + compliance → orchestrate |
| 4 | "Báo cáo cho sếp: lãi/lỗ, VAT, GDPR, sức khỏe AI worker." | CEO brief đa-trục → fan-out finance + compliance + ops-hr ('báo cáo cho sếp') |
| 5 | "Tình hình compliance toàn công ty kỳ này thế nào, có bị block gì không?" | Tổng hợp compliance_status cross-SOP ('compliance') → route compliance + enforce gate |

## SHOULD NOT trigger (delegate hoặc escalate — KHÔNG tự làm)

| # | Input | Đúng hành vi |
|---|-------|--------------|
| 1 | "Ghi sổ và reconcile fee Printify tháng này." | **Delegate** → `vibe-eu-opc-bck-finance` (BCK-001, việc bookkeeping chuyên môn) |
| 2 | "Cấp GPSR clearance cho SP Corgi chờ publish EU." | **Delegate** → `vibe-eu-opc-bck-compliance` (BCK-004, việc clearance chuyên môn) |
| 3 | "Đánh giá uptime + chất lượng output của 3 AI worker tuần qua." | **Delegate** → `vibe-eu-opc-bck-ops-hr` (BCK-006, việc workforce chuyên môn) |
| 4 | "Scale campaign US-BULLDOG-001, ROAS đang tốt." | **Escalate** → 03-growth (phòng khác; Backoffice chỉ cấp profit/gate, không chạy ads) |
| 5 | "Đơn #1234 chưa có tracking, khách EU hỏi." | **Escalate** → 04-fulfillment-cx (phòng khác) |

---

## Bẫy quan trọng
- Skill là **Manager** — nếu input là **một việc chuyên môn đơn lẻ** (ghi 1 sổ, cấp 1 clearance, review 1 worker), KHÔNG execute mà **route** xuống đúng specialist.
- Việc thuộc **phòng L2 khác** (ads/creative/email, đơn/CX, niche/design, pricing/page) → **escalate** theo matrix, KHÔNG xử lý.
- Chỉ "ôm" trọn vẹn khi là **điều phối đa-specialist** hoặc **chốt kỳ / CEO brief end-to-end**.
- Gate cứng legal (GPSR/Meta/GDPR/VAT) = error budget 0% — fail ⇒ BLOCKED + escalate Owner, không tự override.

**PASS khi:** 5/5 SHOULD trigger + route/orchestrate; 5/5 SHOULD NOT chuyển sang delegate/escalate đúng đích.
