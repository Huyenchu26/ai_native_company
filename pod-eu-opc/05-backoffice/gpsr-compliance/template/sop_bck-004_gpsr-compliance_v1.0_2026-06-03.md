# SOP-BCK-004 — GPSR compliance (Responsible Person, labeling)

**Department:** Backoffice (bck) · **AI Worker phụ trách:** Compliance AI
**Loại:** OPERATIONAL (template → input → processing → output → archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-03 · **Trạng thái:** ACTIVE (rào pháp lý — ưu tiên cao nhất)

> ⚠️ **Miễn trừ:** Quy trình vận hành nội bộ, không phải tư vấn pháp lý. GPSR (Regulation EU 2023/988) áp dụng từ **13/12/2024**. Yêu cầu cụ thể tùy sản phẩm — **xác nhận với tư vấn pháp lý EU**. Nếu thiếu **Responsible Person trong EU**, listing/đơn vào EU có thể bị từ chối hoặc gỡ.

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | Đảm bảo mọi sản phẩm apparel bán vào EU tuân thủ GPSR: có Responsible Person trong EU, đủ thông tin truy xuất & an toàn trên listing → không bị gỡ, không rủi ro pháp lý. |
| **Phạm vi** | Tất cả listing/SKU bán vào EU (Etsy Phase 1, Shopify Phase 2). |
| **Trigger** | (a) Trước khi publish bất kỳ listing mới (gate trong SOP-MER-001); (b) Audit định kỳ hàng tháng toàn bộ listing active; (c) Khi có thay đổi quy định / thay đổi print provider. |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Listing chuẩn bị publish (từ SOP-MER-001), thông tin product Printify (nhà sản xuất/provider), thông tin Responsible Person EU, quy định GPSR hiện hành |
| **Control** | GPSR (EU 2023/988); yêu cầu nhãn: nhà sản xuất, Responsible Person EU, định danh sản phẩm, cảnh báo an toàn; chính sách Etsy về GPSR |
| **Output** | GPSR clearance log mỗi SKU, nội dung nhãn chèn vào listing, danh sách listing non-compliant cần sửa, audit report tháng |
| **Mechanism** | Compliance AI + Claude API, Etsy/Shopify API (đọc/sửa listing), Printify API (thông tin provider) |

---

## 2. Yêu cầu GPSR cho apparel POD (Knowledge)

GPSR yêu cầu sản phẩm tiêu dùng bán vào EU phải có (kiểm tra với tư vấn cho trường hợp cụ thể):

| # | Yêu cầu | Áp dụng cho shop |
|---|---|---|
| 1 | **Responsible Person trong EU** | Một pháp nhân/cá nhân đặt tại EU chịu trách nhiệm an toàn sản phẩm. Nếu công ty ngoài EU → cần ủy quyền RP (Printify có thể cung cấp/khuyến nghị dịch vụ RP cho một số sản phẩm). |
| 2 | **Thông tin nhà sản xuất** | Tên + địa chỉ + liên hệ của nhà sản xuất (print provider) hiển thị được. |
| 3 | **Định danh sản phẩm** | Model/SKU/batch để truy xuất. |
| 4 | **Cảnh báo & hướng dẫn an toàn** | Với apparel: thường tối thiểu (vd cảnh báo cho đồ trẻ em — dây rút, kích cỡ nhỏ). Sản phẩm trẻ em rủi ro cao hơn. |
| 5 | **Hiển thị trước khi mua** | Thông tin trên hoặc kèm listing để người mua thấy trước khi đặt. |

> 🎯 **Đòn bẩy:** Printify hỗ trợ thông tin GPSR/RP cho nhiều catalog — SOP-MER-002 ưu tiên provider EU + sản phẩm có sẵn dữ liệu GPSR để bước này gần như tự động.

---

## 3. Vai trò & RACI

| Hoạt động | Founder | Compliance AI | Listing-SEO AI (02) |
|---|---|---|---|
| Thiết lập Responsible Person EU | **R/A** | C | I |
| Sinh nội dung nhãn GPSR mỗi SKU | I | **R** | C |
| Gate trước publish | A | **R** | C (chèn nhãn) |
| Audit listing active hàng tháng | A | **R** | I |
| Xử lý listing non-compliant | A | **R** | C |

## 4. Đầu vào & Điều kiện bắt đầu

- [ ] **Responsible Person EU đã được thiết lập** (điều kiện tiên quyết toàn shop — Founder xử lý trước launch) → lưu thông tin tại `./input/responsible-person.md`
- [ ] Mapping mỗi SKU → print provider + thông tin nhà sản xuất (từ SOP-MER-002)
- [ ] Listing draft cần clearance đặt trong `./input/`

## 5. Quy trình

> Tag AI: [AI ASSIST] · [AI AUGMENT] · [AI WORKFORCE]

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 5.1 | Kiểm tra RP | Xác nhận SKU thuộc phạm vi Responsible Person EU đã thiết lập | [AI WORKFORCE] | Không có RP hợp lệ → BLOCK publish (không thể bỏ qua) |
| 5.2 | Thu thập dữ liệu nhà SX | Lấy tên/địa chỉ provider + định danh sản phẩm từ Printify | [AI WORKFORCE] | Pull qua API; thiếu trường → flag, không tự bịa |
| 5.3 | Sinh nội dung nhãn | Soạn block GPSR (RP, nhà SX, định danh, cảnh báo nếu có) theo template | [AI AUGMENT] | Template chuẩn hóa → không sót trường; checklist 5 yêu cầu §2 |
| 5.4 | Kiểm sản phẩm trẻ em | Nếu là đồ trẻ em → áp checklist an toàn nghiêm hơn → escalate Founder | [AI AUGMENT] | Auto-detect category "kids/baby" → bắt buộc review người |
| 5.5 | Cấp clearance | Đạt → ghi GPSR clearance log + trả nhãn cho SOP-MER-001 chèn vào listing | [AI AUGMENT] | Clearance log gắn SKU; listing không có log → MER-001 không publish |
| 5.6 | Audit tháng | Quét toàn bộ listing active: còn đủ nhãn? RP còn hiệu lực? provider đổi? | [AI WORKFORCE] | Lịch tự động; xuất danh sách non-compliant → sửa trong 48h |

## 6. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI | SLO | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Có Responsible Person EU | % SKU thuộc RP hợp lệ | 100% | Check RP record | ☐ |
| 2 | Đủ trường nhãn | % SKU đủ 5 yêu cầu §2 | 100% | Checklist tự động | ☐ |
| 3 | Hiển thị trước mua | Nhãn có mặt trên listing | 100% | Scan listing | ☐ |
| 4 | Đồ trẻ em được review | % SKU kids có người duyệt | 100% | Review log | ☐ |
| 5 | Audit coverage | % listing active được audit/tháng | 100% | Audit report | ☐ |

**Quyết định:** ALL pass → cấp clearance → `./output/`. ANY fail → **BLOCK publish** + LOOP (max 3) → ESCALATE Founder → Incident Report. **Không có ngoại lệ cho tiêu chí #1 (RP).**

## 7. Output & Downstream

- **Lưu tại:** `./output/gpsr-clearance-log_[YYYY-MM].md` (mỗi SKU 1 dòng) → `./archive/`
- **Downstream:** SOP-MER-001 (chèn nhãn vào listing — gate publish), audit feed về SOP-BCK-003 report
- **Naming:** `sop-bck-004_gpsr-clearance_[YYYY-MM]_DONE_[date].md`, `..._gpsr-audit_[YYYY-MM]_DONE_[date].md`

## 8. Phụ lục

- **Upstream:** SOP-MER-002 (provider/nhà SX), thiết lập RP (Founder)
- **Downstream:** SOP-MER-001 (gate publish listing)
- **Knowledge:** `../../_knowledge/` (tóm tắt GPSR + danh mục yêu cầu theo category)
- **Rules / Quality:** `../../_rules/README.md` · `../../quality_bck-001_quality-standards_v1.0_2026-06-03.md`
- **Policy:** `../../../_shared/policies/ip-policy.md`, `../legal-registration-calendar.md`
- **Thiết kế:** `../../../02-design/opc-design-roadmap.md` §6.2
- **TODO Founder (BLOCKER trước launch):** thiết lập **Responsible Person trong EU** (tự đăng ký pháp nhân EU, hoặc dùng dịch vụ RP của Printify/bên thứ ba). Không có RP → không được bán vào EU.
