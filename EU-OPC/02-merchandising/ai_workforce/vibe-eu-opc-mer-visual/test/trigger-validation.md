# Trigger Validation — vibe-eu-opc-mer-visual

Xác nhận skill kích hoạt đúng việc & nhường đúng skill khác. 5 SHOULD + 5 SHOULD NOT.

---

## ✅ SHOULD trigger (đây là việc của chị Ảnh)
1. "Làm bộ ảnh mockup cho SKU Husky leggings lên ShopBase." → tạo bộ 6 ảnh.
2. "Ảnh shop nhìn chưa đẹp, rời rạc — chuẩn hoá lại visual đi." → áp style guide, dựng lại bộ ảnh.
3. "Cần hero shot + lifestyle photo cho SP mới vừa clear design." → sinh render-prompt bộ ảnh.
4. "Render mockup product image cho winner đang chạy ads." → ưu tiên winner, đủ 6 ảnh.
5. "Sửa ảnh sản phẩm này, ảnh không bắt mắt trên feed FB." → QC + scroll-stopper 4:5.

## ❌ SHOULD NOT trigger (nhường skill khác — đây là BẪY)
1. "Thiết kế file AOP print-ready 300 DPI họa tiết Husky." → **vibe-eu-opc-prd-design** (anh Họa). (chị Ảnh chỉ DÙNG design có sẵn, không vẽ design.)
2. "Viết product page copy + bullet + upsell cho SP này." → **vibe-eu-opc-mer-product-page** (chị Lời).
3. "Làm video quảng cáo / kịch bản ad / carousel creative cho FB." → **vibe-eu-opc-grw-creative** (chị Ý). (chị Ảnh chỉ giao ảnh #6 scroll-stopper, không dựng ad video.)
4. "Setup product trên Printify, đặt giá variant XS–3XL, sync ShopBase." → **vibe-eu-opc-mer-catalog**.
5. "Định giá / pricing / margin cho SKU này." → **vibe-eu-opc-mer-catalog**.

---

**Ranh giới cốt lõi:** chị Ảnh = **dùng design có sẵn → tạo SPEC+PROMPT+QC bộ ảnh mockup**. KHÔNG vẽ design (prd-design), KHÔNG viết copy (mer-product-page), KHÔNG làm ad creative (grw-creative), KHÔNG setup/pricing/sync (mer-catalog).
