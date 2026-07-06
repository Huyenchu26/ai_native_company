# Trigger Validation — vibe-eu-opc-ful-cx

Kiểm tra skill kích hoạt đúng (SHOULD) và KHÔNG kích hoạt sai (SHOULD NOT — bẫy routing).

## SHOULD trigger (5)
1. "Trả lời khách hỏi where is my order" → WISMO ticket. ✅
2. "Khách bảo legging chật quá, đổi size M giúp" → size exchange XS–3XL. ✅
3. "Hàng bị lỗi print, khách gửi ảnh, xử lý đi" → defect → reprint-first. ✅
4. "Khách đòi refund $45 vì hàng hư" → refund gate >$30 → escalate OPC. ✅
5. "Khách EU yêu cầu xóa hết dữ liệu cá nhân (DSAR)" → GDPR erasure. ✅

## SHOULD NOT trigger (5 — bẫy)
1. "Route đơn #DK-1042 sang Printify provider US" → ❌ → **vibe-eu-opc-ful-order-ops** (order routing).
2. "Verify đơn ShopBase rồi gửi tracking cho khách" → ❌ → **vibe-eu-opc-ful-order-ops** (verify/tracking gen).
3. "Ghi sổ khoản refund $28 vào ledger, tính VAT" → ❌ → **vibe-eu-opc-bck-finance** (bookkeeping/VAT).
4. "Lập P&L profit-per-SKU tháng này" → ❌ → **vibe-eu-opc-bck-finance** (reporting tài chính).
5. "Cấp clearance GDPR / IP-TM cho niche mới" → ❌ → compliance (cx chỉ phối, không cấp clearance).

## Ranh giới quan trọng
- cx **ĐỌC** tracking/order data từ order-ops nhưng KHÔNG tự route/verify đơn.
- cx **TẠO** refund/cost data nhưng KHÔNG ghi sổ/khai VAT (đẩy finance).
- cx **PHỐI** compliance cho DSAR nhưng KHÔNG tự cấp clearance.

## Kết quả
| # | Case | Expect | PASS/FAIL |
|---|---|---|---|
| S1–S5 | support/size/defect/refund/GDPR | trigger | |
| N1–N2 | route/verify đơn | → order-ops | |
| N3–N4 | bookkeeping/VAT/P&L | → finance | |
| N5 | cấp clearance | → compliance | |
