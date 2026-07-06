# KB — AOP Design & IP/TM Clearance Playbook (DAKOfits)

Tham chiếu: SOP-PRD-003 (design-aop), SOP-PRD-004 (clear-ip). Đây là kiến thức nền cho AI Worker `vibe-eu-opc-prd-design`. Mọi quyết định mang **evidence[] + confidence_score + need_review**.

---

## 1. Bốn loại design chuẩn DAKOfits

| Loại | Đặc tả | Khi nào dùng | Yêu cầu kỹ thuật riêng |
|------|--------|--------------|------------------------|
| **tile** | Pattern lặp (icon/silhouette niche) phủ kín | Niche có motif lặp được (paw, breed silhouette) | BẮT BUỘC seamless tile, kiểm 4 cạnh nối |
| **watercolor** | Loang màu nghệ thuật, gradient mềm | Niche thẩm mỹ, dog-mom, hoa/cảnh | Tránh banding khi in; canvas đủ lớn |
| **funny** | Graphic vui, quote/meme niche | Niche humor, gift, quote tee/legging | Quote phải qua IP/TM check (slogan TM) |
| **mandala** | Đối xứng tâm, hoa văn | Niche spiritual/yoga/zen | Seamless + đối xứng tuyệt đối |

Lock **300 DPI** tại kích thước in thật ngay từ đầu — KHÔNG upscale. Sinh artwork theo **canvas template px thật** của provider; tách profile **US vs EU** (color + size khác nhau).

---

## 2. QC 360° Checklist (gate kỹ thuật trước handoff clearance)

AOP wrap quanh thân legging 360°, nên mọi mép phải khớp khi may. Kiểm:

- [ ] **DPI ≥ 300** — đọc file metadata (100%, fail-closed).
- [ ] **seam** — đường nối hông/ống: pattern liên tục, không lệch, không lộ mối.
- [ ] **crotch** — vùng đáy quần: hoạ tiết không bị cắt phản cảm, không vỡ pattern.
- [ ] **waistband** — cạp quần: pattern align khi gập mép, không đứt gãy.
- [ ] **bleed** — chừa bleed ≥ spec provider (tránh hở trắng khi cắt-may).
- [ ] **canvas px** — đúng kích thước template px thật của Printify/PrintBase (sai px = lỗi cắt-may AOP).
- [ ] **style tag** — đúng 1/4 loại.
- [ ] **mockup** — render XS–3XL đại diện để mắt người soát.

Fail xử lý: seam lộ → tạo lại seamless tile; DPI < 300 → re-generate canvas lớn hơn (không upscale); color lệch US/EU → tách 2 profile, QC từng provider.

---

## 3. IP/TM Clearance Process (GATE CỨNG — no clearance → no listing)

### Bước 1 — Trích term
Tên niche/breed, slogan/quote, logo, character. Ưu tiên item có **pre-flag HIGH** từ PRD-001.

### Bước 2 — Dual lookup BẮT BUỘC
- **USPTO TESS** (thị trường US).
- **EUIPO** (thị trường EU).
- Đối chiếu **blocklist** brand / celebrity / club / character.

Thiếu 1 trong 2 nguồn → KHÔNG được PASS.

### Bước 3 — Phân loại (rubric)

| Tình huống | Status |
|-----------|--------|
| TM exact match | **REJECT** |
| TM similar (cùng class hàng hoá) | **MODIFY** (sửa term/artwork → re-clear) |
| Generic / descriptive term, không match | **PASS** (ghi evidence) |
| Không chắc / chưa đủ nguồn / HIGH-risk | **REJECT → human review** |

### Bước 4 — Log & handoff
Ghi IP-clearance log ra `output/`. **Chỉ PASS** → `handoff_ready = true` → bàn giao Merch. MODIFY → loop sửa. REJECT → loại bỏ.

---

## 4. Conservative default = REJECT

Triết lý fail-closed: khi mơ hồ, **mặc định REJECT** + `need_review = true`, KHÔNG listing. Lý do: dính TM → takedown/ban store/ads thiệt hại lớn hơn nhiều so với bỏ 1 design. AI tự tin sai là rủi ro chính → `confidence_score < 0.7` hoặc HIGH-risk → đẩy human review.

| Rủi ro | Phòng ngừa |
|--------|-----------|
| Listing dính TM → takedown/ban | Gate cứng no-clearance-no-listing |
| Bỏ sót thị trường EU | Dual lookup USPTO + EUIPO bắt buộc |
| AI tự tin sai | Conservative default REJECT + human review HIGH-risk |
| In lộ seam | QC 360° bắt buộc trước handoff |
| File mờ khi in | Lock 300 DPI từ đầu, không upscale |
