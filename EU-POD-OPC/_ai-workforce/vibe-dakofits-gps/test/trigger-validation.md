# Trigger Validation — vibe-dakofits-gps

## SHOULD trigger (5)
1. "Làm SP mới niche mèo cho EU, bán tuần sau" — task đa-phòng chưa rõ định tuyến.
2. "Chạy đợt promote 8 SP mới" — full-chain, GPS điều phối.
3. "Điều hành công ty hôm nay làm gì trước" — task tổng, cần route.
4. "Task này giao cho ai / phòng nào" — hỏi định tuyến.
5. "Tổng hợp tình hình công ty cho tôi" — báo cáo tổng, GPS gom từ các phòng.

## SHOULD NOT trigger (5)
1. "/vibe-eu-opc-grw-fb-ads tối ưu campaign X" — user gọi đích danh skill phòng → dùng thẳng skill đó.
2. "Viết product page cho SP Husky" — rõ 1 nghiệp vụ → vibe-eu-opc-mer-product-page.
3. "Tính profit-per-SKU kỳ này" — rõ → vibe-eu-opc-bck-finance.
4. "Cấp GPSR clearance lô EU" — rõ → vibe-eu-opc-bck-compliance.
5. "Thời tiết hôm nay thế nào" — không thuộc vận hành DAKOfits.

Nếu test fail (over/under trigger) → tinh chỉnh description theo 4-component (WHAT/TRIGGER/EXCLUSION/PUSH).
