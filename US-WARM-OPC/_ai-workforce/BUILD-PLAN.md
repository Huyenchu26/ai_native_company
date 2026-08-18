# US-WARM-OPC — Build Plan (AI-Native Company cho Personalized Winter Comfort & Gifts, thị trường US)

**Ngày:** 2026-08-04 · **Chế độ:** rebuild sạch (folder mới, song song EU-POD-OPC làm tham chiếu/rollback).
**Bối cảnh:** Pivot từ AOP-leggings-EU sang **đồ giữ ấm mùa đông cá nhân hoá** (blanket-first), thị trường **US**, cạnh tranh với customwarms.com.

---

## 1. Định vị & khác biệt hoá (từ phân tích đối thủ)

**Đối thủ customwarms.com** (Trustpilot lẫn lộn–tiêu cực) yếu ở đúng 3 điểm:
- ❌ **QC sản phẩm** — chăn "mỏng như giấy", không đúng mô tả.
- ❌ **Fulfillment** — đơn không tới, **tracking giả**.
- ❌ **CX** — không có người thật hỗ trợ.

→ **Chiến lược khác biệt hoá của US-WARM-OPC = thắng ở đúng 3 chỗ đó**, encode thành gate cứng trong SOP:
- **QC gate**: spec GSM/vật liệu tối thiểu + ảnh QC thật trước ship (chống "chăn mỏng").
- **No-fake-tracking gate**: chỉ gửi tracking khi có mã carrier thật, verified (chống tracking giả — đây là gate cứng đạo đức).
- **Real-CX SLA**: first-response ≤ 4h, resolution rate, không auto-reply vô nghĩa.

## 2. Sản phẩm & thị trường

| | Giá trị |
|--|--|
| Sản phẩm P0 (ưu tiên) | **Chăn cá nhân hoá** (personalized fleece/sherpa blanket): tên, ảnh, thông điệp, dòng pet-memorial |
| Sản phẩm P1 (mở rộng) | Beanie leather-patch, mũ pom pom, khăn, beret thêu |
| Cá nhân hoá | tên/monogram · ảnh (chăn) · thêu/leather-patch (phụ kiện) |
| Niche | **dịp tặng quà** (Christmas, Valentine, Mother's/Father's Day, kỷ niệm) · **quan hệ** (to my daughter/wife/mom) · **pet & pet-memorial** |
| Mùa vụ | Nặng Q4 (Oct–Dec) + Valentine + Mother's Day → design deadline lùi ≥6 tuần |
| Thị trường | **US** |
| Giá tham chiếu | Chăn $39.95–59.95 (free-ship >$59), phụ kiện $24.95–34.95 |

## 3. Thay đổi compliance: EU → US (viết lại toàn bộ 05-backoffice)

| Bỏ (EU) | Thay bằng (US) |
|---------|----------------|
| VAT OSS/IOSS | **US sales tax nexus** (economic nexus theo bang, marketplace facilitator, TaxJar/Avalara) |
| GPSR (product safety EU) | **CPSC**: 16 CFR 1610 flammability cho textile/chăn; **Textile Fiber Products Identification Act** (nhãn sợi + RN number); wool labeling nếu có |
| EU consumer law (14-day withdrawal) | **US**: FTC Mail/Internet Order Rule (ship trong 30 ngày hoặc báo), state return laws; **made-to-order/personalized = final-sale** trừ lỗi sản xuất |
| — | **FTC** advertising: endorsement/review disclosure (16 CFR 255), "Made in USA" nếu dùng, no deceptive claims |
| GDPR | **US privacy**: CCPA/CPRA (California) + state laws; PII cá nhân hoá (tên/ảnh) xử lý cẩn thận |

## 4. Cấu trúc công ty (5 phòng, giữ khung KWSR)

```
US-WARM-OPC/
├── 00-company/        charter, org-chart, value-chain, glossary, OKR/KPI/KRI (US, blanket)
├── 01-product-studio/ niche-research (gift/occasion) · design-personalization · trend-seasonal · ip-clearance-US · amplify-winner
├── 02-merchandising/  setup-product · variant-pricing (blanket econ) · personalization-preview · product-page (gift copy) · catalog-sync · promote-batch
├── 03-growth/         fb-creative (gift-emotional) · run-fb-ads (US, seasonal) · organic-social · email (gift/abandoned-personalization) · growth-report
├── 04-fulfillment-cx/ route-fulfillment (US supplier) · monitor-orders (REAL tracking) · handle-returns (personalized=final-sale) · support-customer (real CX) · QC-gate
├── 05-backoffice/     sales-tax-nexus · bookkeeping · profit-roas · ftc-advertising · cpsc-textile-labeling · privacy-ccpa · manage-workforce
├── _shared/           unit-economics · script/ (HARNESS ĐÃ SỬA) · policies · winner-registry
├── _quality/  _ai-workforce/  output/
```

## 5. Harness đã sửa (áp dụng ngay từ đầu — không lặp bug pipeline test)

Từ EU pipeline-test (đã retire — xem git history), 5 bug harness sẽ được fix trong `_shared/script/validator.py` dùng chung:
1. **P1** — validator thực thi `allOf`/`if`/`then` (hoặc dùng `jsonschema` draft-07) → gate cứng thành thật.
2. **P2** — 1 quy ước `evidence` thống nhất toàn hệ + `verify_evidence()` khớp.
3. **P3** — schema model được trạng thái fail-closed (PENDING/blocked/validation-phase).
4. **P4** — enforce `min_confidence` per-gate.
5. **P5** — detector prose cho gate content (deceptive claim, fake review, fake tracking).

## 6. Naming convention (tránh drift D1)

- Skill: `vibe-us-warm-<dept>-<role>` (vd `vibe-us-warm-prd-design`, `vibe-us-warm-ful-cx`). **1 lớp duy nhất**, không legacy.
- SOP file: `sop_<dept>-NNN_<slug>_vX.Y_<date>.md`. Governance ↔ folder skill ↔ skill.json PHẢI khớp tên (kiểm bằng script trước khi commit).

## 7. Lộ trình thực hiện (vertical slice chăn trước)

| Phase | Nội dung | Trạng thái |
|-------|----------|-----------|
| 0 | Nền móng: scaffold + build-plan + charter + unit-economics | 🔄 đang làm |
| 1 | Harness đã sửa (shared validator + schema base) | ⏳ |
| 2 | 01 product-studio (chăn): niche-research + design-personalization + ip-US | ⏳ |
| 3 | 02 merchandising (chăn): pricing + preview + listing | ⏳ |
| 4 | 03 growth (US ads/FTC) + 04 fulfillment-cx (QC/CX differentiator) | ⏳ |
| 5 | 05 backoffice US (sales-tax + CPSC + FTC + CCPA) | ⏳ |
| 6 | Chạy pipeline-test chăn end-to-end + mở rộng sang phụ kiện | ⏳ |

> Mỗi phase là 1 checkpoint — review trước khi sang phase sau, để không lặp lỗi "sinh 200 file rồi drift".

## 8. Điều CẦN Owner chốt thêm (không chặn Phase 0-1)
- **Brand name** (hiện để DAKOfits placeholder) — cần trước khi viết listing/growth thật.
- **Supplier chăn US** (Printful US / Printify US / blanket-specialist dropship) — quyết cost thật + QC gate.
- Có bán kèm **phụ kiện** ngay Q1 hay để P1.
