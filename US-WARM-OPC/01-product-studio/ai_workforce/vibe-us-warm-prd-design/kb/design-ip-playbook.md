# KB — Blanket Personalization Design & IP/TM Pre-check Playbook (DAKOfits US)

Tham chiếu: SOP-PRD-002 (design-personalization), SOP-PRD-003 (clear-ip US single-market). Kiến thức nền cho AI Worker `vibe-us-warm-prd-design`. Mọi quyết định mang **evidence[] + confidence_score + need_review**. Vocabulary trạng thái: **CLEAR / MODIFY / REJECT / PENDING** (KHÔNG dùng "PASS").

---

## 1. Design template cá nhân hoá (KHÔNG phải AOP)

Chăn cá nhân hoá = **nền design** + **vùng chèn biến (variable data)**. Không có "AOP 300 DPI toàn mặt". Mỗi design là một **layout template** nhận field khách: `name`, `photo`, `message`, `pet-memorial`.

| Thành phần | Đặc tả | QC trọng tâm |
|-----------|--------|--------------|
| Nền design | Artwork niche cố định (không đổi theo khách) | IP phrase/artwork clear |
| Vùng tên/message | Text slot: max ký tự, font, canh giữa | Nằm trong safe-area |
| Vùng ảnh khách | Photo slot: ratio, DPI tối thiểu | DPI ảnh khách đạt tại size in thật |
| Pet-memorial | Ảnh + tên + ngày | Photo-consent + safe-area |

---

## 2. Ba QC gate kỹ thuật (design_status=CLEAR bắt buộc pass hết)

### 2.1 Safe-area
Mọi chữ và ảnh cá nhân hoá phải nằm trọn trong safe-area, cách mép seam an toàn. Lệch mép → `safe_area_pass=false` → sửa layout (MODIFY).

### 2.2 DPI ảnh khách — NO UPSCALE
Ảnh khách phải đạt tối thiểu 150 DPI tại kích thước in thật; dưới ngưỡng REJECT và re-source, tuyệt đối không upscale. **KHÔNG dùng Real-ESRGAN / Topaz / bất kỳ upscaler** để "đạt DPI" — đó là lỗi H2 của model EU. Ảnh mờ khi in làm hỏng brand-promise.

### 2.3 Material GSM — NO UNDER-SPEC
Fleece/sherpa GSM tối thiểu brand-promise = 260 GSM; dưới ngưỡng = under-spec, đổi vải không hạ ngưỡng. Chống "chăn mỏng / không đúng mô tả" của đối thủ. Không có vải đạt → Owner + merchandising.

---

## 3. IP/TM Pre-check — US single-market (GATE CỨNG, error budget = 0)

### 3.1 Nguồn tra
USPTO TESS là nguồn tra trademark duy nhất cho thị trường US single-market; không dùng EUIPO. (Khác EU model dual-market — US chỉ 1 nguồn.) Bổ sung: licensed-character blocklist + right-of-publicity theo bang + platform policy (Meta/Etsy).

### 3.2 Rubric phân loại
| Tình huống | Status |
|-----------|--------|
| USPTO chưa tra được / uncertain | **PENDING** (fail-closed, KHÔNG mặc định CLEAR) |
| Exact TM match trên phrase/slogan | **REJECT** |
| Licensed-character match (blocklist) | **REJECT** |
| TM similar cùng class hàng hoá | **MODIFY** (sửa term/artwork → re-clear) |
| Generic/descriptive, tra sạch, đã có clearance_id | **CLEAR** |

Licensed-character blocklist gồm Disney, sports leagues, brand; match bất kỳ là REJECT.

### 3.3 Photo-consent
Design có field ảnh khách → cần `photo_consent=true` (khách xác nhận sở hữu/được phép dùng ảnh). Thiếu consent → block field ảnh. Design không có field ảnh → `photo_consent=null` (không áp dụng).

### 3.4 Ownership — pre-check vs official
`prd-design` chỉ **PRE-CHECK**. clearance_id chính thức chỉ do bck-compliance cấp sau sign-off. `ip_status=CLEAR` (và do đó `handoff_ready=true`) CHỈ hợp lệ khi đã có `clearance_id` không null. Đây là fix lỗi H5 (ownership mập mờ) của model cũ.

---

## 4. Conservative default = fail-closed

Khi mơ hồ: **KHÔNG CLEAR**. Dùng PENDING (chưa tra được) / MODIFY (sửa được) / REJECT (dính TM). `confidence_score < 0.7` hoặc HIGH-risk → `need_review=true` → Owner.

| Rủi ro | Phòng ngừa |
|--------|-----------|
| Design "PASS" nhưng orchestrator chờ "CLEAR" → đứng pipeline | Vocabulary CLEAR nhất quán mọi nơi (fix bug EU) |
| Ảnh mờ khi in | Lock min DPI, REJECT nếu thiếu, KHÔNG upscale |
| "Chăn mỏng" | GSM ≥ 260, không hạ ngưỡng |
| Dính TM/licensed → takedown/ban | Gate cứng: no clearance_id → no handoff |
| AI tự tin sai | Fail-closed PENDING + human review HIGH-risk |
