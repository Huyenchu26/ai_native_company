# Company Charter — US-WARM-OPC

**Phiên bản:** 1.0 · **Ngày:** 2026-08-04 · **Brand:** DAKOfits

> AI-Native One-Person Company bán **đồ giữ ấm mùa đông cá nhân hoá & quà tặng** cho thị trường **US**, khởi đầu bằng **chăn cá nhân hoá**. Vận hành bởi 1 Owner + đội AI Worker.

---

## 1. Vision / Mission

- **Vision:** Trở thành thương hiệu quà tặng cá nhân hoá giữ ấm được tin cậy nhất ở US — nơi "cá nhân hoá" đi kèm **chất lượng thật và dịch vụ thật**, không phải lời hứa suông.
- **Mission:** Biến khoảnh khắc tặng quà (Noel, Valentine, kỷ niệm, tưởng nhớ thú cưng) thành sản phẩm cá nhân hoá chất lượng cao, giao đúng hẹn, hỗ trợ bằng người thật.

## 2. Định vị cạnh tranh (Positioning)

Phân khúc personalized-blanket US hiện có nhiều tay chơi giá rẻ (điển hình customwarms.com) **yếu ở QC + fulfillment + CX** (review thực tế: chăn mỏng, tracking giả, không hỗ trợ). US-WARM-OPC định vị **"cá nhân hoá tử tế"**: cao hơn một bậc về vật liệu, minh bạch tracking, CX người thật — bán ở phân khúc **mid** ($39.95–59.95) chứ không đua đáy giá.

**3 lời hứa thương hiệu (encode thành gate cứng, error budget = 0):**
1. **Chất lượng đúng mô tả** — spec vật liệu tối thiểu (GSM, loại vải) + ảnh QC thật trước khi ship.
2. **Tracking thật** — chỉ báo "đã gửi" khi có mã carrier verified. TUYỆT ĐỐI không tracking giả.
3. **Người thật hỗ trợ** — first response ≤ 4h giờ hành chính US, không auto-reply rỗng.

## 3. Sản phẩm

| Ưu tiên | Dòng | Cá nhân hoá | Giá tham chiếu |
|---------|------|-------------|----------------|
| P0 | Chăn cá nhân hoá (fleece/sherpa) | tên, ảnh, thông điệp, pet-memorial | $39.95–59.95 |
| P1 | Beanie leather-patch, mũ pom pom, khăn, beret thêu | tên/monogram/thêu | $24.95–34.95 |

Free shipping ngưỡng > $59 (khuyến khích bundle/2 sản phẩm).

## 4. Thị trường & Compliance (US)

- **Thị trường:** US (50 bang). Ngôn ngữ EN.
- **Sales tax:** economic nexus theo bang + marketplace facilitator; công cụ TaxJar/Avalara.
- **An toàn sản phẩm:** CPSC 16 CFR 1610 (flammability textile), Textile Fiber Products Identification Act (nhãn sợi + RN).
- **Quảng cáo:** FTC 16 CFR 255 (disclosure review/endorsement), no deceptive claims, "Made in USA" chỉ khi đủ điều kiện.
- **Đơn hàng:** FTC Mail/Internet Order Rule (ship ≤30 ngày hoặc thông báo). Sản phẩm cá nhân hoá = **final-sale** trừ lỗi sản xuất/không đúng mô tả.
- **Privacy:** CCPA/CPRA + luật bang; PII cá nhân hoá (tên/ảnh khách) xử lý theo policy data-protection.

## 5. Mô hình vận hành (1 + AI Workforce)

- **Owner (người):** quyết định chiến lược, duyệt HITL (IP risk, QC ngoại lệ, refund > ngưỡng, target moonshot).
- **AI Workforce:** 5 phòng (Product Studio · Merchandising · Growth · Fulfillment-CX · Backoffice), mỗi phòng 1 orchestrator + specialist. Skill namespace `vibe-us-warm-<dept>-<role>`.
- **Nguyên tắc harness:** mọi output có evidence + confidence + need_review; gate cứng enforce bằng validator (đã fix từ bài học EU pipeline test); no-hallucination, no-fake-data.

## 6. Bắc Đẩu (North-star) & chỉ số gốc

- **North-star:** Số đơn quà cá nhân hoá **giao đúng hẹn + không lỗi QC** / tháng (kết hợp doanh thu & chất lượng, không chỉ volume).
- Company OKR/KPI/KRI chi tiết: xem `okr_company-001` / `kpi_strat-001` / `kri_company-001` (Phase sau).
- Unit economics: xem [`_shared/unit-economics.md`](../_shared/unit-economics.md).

## 7. Khác biệt so với công ty cũ (EU-POD-OPC)
Sản phẩm (chăn/phụ kiện vs leggings), cá nhân hoá (thêu/ảnh vs AOP), thị trường (US vs EU), compliance (CPSC/FTC/sales-tax vs GPSR/VAT). Giữ lại: khung KWSR, harness/schema/anti-hallucination (đã sửa 5 bug), mô hình 1+AI.
