# Trigger Validation — vibe-eu-opc-bck-finance

Xác nhận skill kích hoạt đúng phạm vi Finance và KHÔNG lấn sang compliance / ops-hr / ads.

## SHOULD trigger (5)
1. "Cuối tháng rồi, **chốt sổ** và **đối soát phí Meta** với gateway kỳ này." → bookkeeping + reconcile (SOP-BCK-001).
2. "**SP này lãi hay lỗ**? Tính **profit-per-SKU** cho batch legging US." → profit-per-SKU (SOP-BCK-002).
3. "**ROAS** thật của campaign tuần này bao nhiêu, có trên **break-even** không?" → blended/true ROAS + BE-ROAS.
4. "Lập **P&L** tháng và quy ra **VND** theo Vietcombank, làm **báo cáo tài chính** cho CEO." → P&L + FX + CEO brief.
5. "Tới kỳ **khai VAT** OSS/IOSS cho đơn EU rồi." → VAT (SOP-BCK-003).

## SHOULD NOT trigger (5) — bẫy
1. "Sản phẩm này cần **GPSR clearance** và **Responsible Person** chưa?" → ❌ Finance. → **vibe-eu-opc-bck-compliance** (GPSR/GDPR/IP-TM).
2. "Khách EU gửi **GDPR data request** xóa dữ liệu." → ❌ Finance. → **vibe-eu-opc-bck-compliance**.
3. "Đánh giá **uptime + chất lượng output** của các AI worker tháng này." → ❌ Finance. → **vibe-eu-opc-bck-ops-hr** (workforce/capacity).
4. "**Scale campaign** winner +20% ngân sách và **kill** ad lỗ." → ❌ Finance (chỉ ĐỌC ROAS, không chạy ads). → **vibe-eu-opc-grw-fb-ads**.
5. "Viết **ad creative / video script** cho SP mới." → ❌ Finance. → **vibe-eu-opc-grw-creative**.

> Quy tắc biên: Finance **đọc** số ad/ROAS để tính lãi + cảnh báo, nhưng **không** chạy/tối ưu/scale ads, **không** cấp clearance pháp lý, **không** quản AI worker.
