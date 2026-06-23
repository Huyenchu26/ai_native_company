# Trigger Validation — vibe-eu-opc-bck-compliance

Xác nhận skill kích hoạt đúng ngữ cảnh compliance và KHÔNG lấn việc phòng khác.

## SHOULD TRIGGER (5)
1. "SP mới này cần **clear** để **publish EU**, cấp clearance giúp." → cấp GPSR clearance log ID.
2. "Khách EU email đòi **xóa data** của họ." → DSAR/erasure (GDPR ≤1 tháng).
3. "Nghi **data breach** ở Klaviyo, làm gì giờ?" → breach log + notify ≤72h.
4. "Breed niche này có **trademark** không, check **IP/TM** đi." → ip-tm-check (USPTO+EUIPO).
5. "Trước khi chạy ad, pre-check **Meta Ad Policy** cho creative này." → meta-policy-precheck.

## SHOULD NOT TRIGGER (5 — bẫy)
1. "Ghi sổ doanh thu tháng này + đối soát **fee** Printify + làm **VAT** EU." → ❌ chuyển **vibe-eu-opc-bck-finance** (bookkeeping/VAT KHÔNG thuộc compliance).
2. "Theo dõi **uptime** + chi phí + cập nhật skill của các **AI worker**." → ❌ chuyển **vibe-eu-opc-bck-ops-hr** (quản workforce).
3. "Viết **product page** copy + upsell bundle cho SP này." → ❌ chuyển **vibe-eu-opc-mer-product-page** (Merch viết page; compliance chỉ cấp clearance + nhãn GPSR text).
4. "Setup **variant/pricing** trên Printify + sync ShopBase." → ❌ chuyển **vibe-eu-opc-mer-catalog**.
5. "Tối ưu **ROAS**, scale campaign FB Ads." → ❌ chuyển **vibe-eu-opc-grw-fb-ads** (compliance chỉ pre-check Meta Ad Policy, không chạy/tối ưu ad).

## Ghi chú ranh giới
- Compliance là **GATE issuer**: ra clearance PASS/FAIL, các phòng khác **verify** clearance_id — không tự publish/chạy ad thay họ.
- Product Studio chỉ **pre-flag** IP/TM; compliance cấp clearance **chính thức**.
