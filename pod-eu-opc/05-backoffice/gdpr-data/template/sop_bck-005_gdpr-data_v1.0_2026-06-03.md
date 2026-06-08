# SOP-BCK-005 — GDPR & data handling

**Department:** Backoffice (bck) · **AI Worker phụ trách:** Compliance AI
**Loại:** OPERATIONAL (template → input → processing → output → archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-08 · **Trạng thái:** ACTIVE

> ⚠️ **Miễn trừ:** Quy trình vận hành nội bộ, không phải tư vấn pháp lý. GDPR (Regulation EU 2016/679) áp dụng cho mọi xử lý dữ liệu cá nhân của người ở EU. Với ShopBase (store chính) công ty là controller dữ liệu khách; ShopBase/Printify/Klaviyo là processor. Xác nhận vai trò với tư vấn.

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | Xử lý dữ liệu cá nhân khách EU hợp lệ, an toàn, tối thiểu; đáp ứng quyền của chủ thể dữ liệu; sẵn sàng khi có sự cố. |
| **Phạm vi** | Mọi dữ liệu cá nhân thu/xử lý: tên, địa chỉ giao hàng, email, dữ liệu Facebook Pixel/CAPI, nội dung CSKH (ShopBase, Klaviyo, Printify, helpdesk). |
| **Trigger** | (a) Theo lịch: audit dữ liệu hàng quý; (b) Sự kiện: yêu cầu của khách (truy cập/xóa), nghi ngờ rò rỉ dữ liệu, thêm tool mới xử lý dữ liệu. |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Danh mục dữ liệu thu thập, danh sách tool/processor (ShopBase, Printify, Klaviyo, Meta Pixel/CAPI, helpdesk), yêu cầu chủ thể dữ liệu, sự cố |
| **Control** | GDPR: hợp pháp (lawful basis), tối thiểu hóa, mục đích rõ, thời hạn lưu, quyền truy cập/xóa/đính chính, thông báo vi phạm trong **72h** |
| **Output** | Data inventory (ROPA rút gọn), privacy notice, log xử lý yêu cầu chủ thể, danh sách processor + DPA, breach log |
| **Mechanism** | Compliance AI + Claude API, công cụ lưu trữ an toàn, ShopBase/Klaviyo/helpdesk |

---

## 2. Nguyên tắc GDPR áp dụng cho shop (Knowledge)

| Nguyên tắc | Áp dụng |
|---|---|
| **Lawful basis** | Xử lý đơn hàng = "thực hiện hợp đồng"; **email marketing (Klaviyo/ShopBase) = cần consent (opt-in)**; Facebook Pixel/quảng cáo retarget với khách EU → cần consent (cookie banner). |
| **Data minimization** | Chỉ thu dữ liệu cần để giao hàng & hỗ trợ. Không lưu thẻ thanh toán (ShopBase payment xử lý). |
| **Purpose limitation** | Dữ liệu giao hàng không dùng cho marketing nếu chưa có consent. |
| **Storage limitation** | Đặt thời hạn lưu (vd dữ liệu đơn giữ theo yêu cầu thuế ~10 năm cho hóa đơn; dữ liệu marketing Klaviyo xóa khi rút consent). |
| **Quyền chủ thể** | Truy cập, đính chính, **xóa ("right to be forgotten")**, di chuyển dữ liệu — đáp ứng trong **1 tháng**. |
| **Processors & DPA** | Mỗi bên thứ ba xử lý dữ liệu (ShopBase, Klaviyo, Printify, helpdesk) cần có Data Processing Agreement. |
| **Breach 72h** | Rò rỉ dữ liệu có rủi ro → thông báo cơ quan giám sát trong **72 giờ**. |

> ⚙️ **Khi dùng AI (Claude API) cho CSKH:** không gửi nhiều dữ liệu cá nhân hơn mức cần; ưu tiên ẩn danh/giảm thiểu (vd chỉ gửi nội dung câu hỏi, không kèm địa chỉ đầy đủ trừ khi cần).

---

## 3. Vai trò & RACI

| Hoạt động | Founder | Compliance AI | CX AI (04) |
|---|---|---|---|
| Lập & duy trì data inventory | A | **R** | I |
| Soạn/cập nhật privacy notice | **A** | **R** | I |
| Xử lý yêu cầu truy cập/xóa | A | **R** | C |
| Ký DPA với processor | **R/A** | C | I |
| Xử lý breach (72h) | **R/A** | **R** | C |

## 4. Đầu vào & Điều kiện bắt đầu

- [ ] Danh sách tool/processor đang xử lý dữ liệu khách (đặt trong `./input/processor-list.md`)
- [ ] Privacy notice + cookie/consent banner đã publish trên ShopBase — điều kiện trước launch
- [ ] Kênh tiếp nhận yêu cầu chủ thể dữ liệu (email/biểu mẫu) đã có

## 5. Quy trình

> Tag AI: [AI ASSIST] · [AI AUGMENT] · [AI WORKFORCE]

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 5.1 | Data inventory | Lập/cập nhật danh mục: dữ liệu gì, ở đâu, mục đích, thời hạn lưu, processor nào | [AI AUGMENT] | Review mỗi quý + khi thêm tool mới; template ROPA rút gọn |
| 5.2 | Privacy notice | Soạn/cập nhật thông báo quyền riêng tư + cookie/consent banner (EN) trên ShopBase | [AI AUGMENT] | Checklist các mục bắt buộc GDPR; Founder duyệt |
| 5.3 | Consent marketing | Đảm bảo email marketing (Klaviyo/ShopBase) chỉ gửi cho người opt-in; lưu bằng chứng consent | [AI WORKFORCE] | Double opt-in; tách list "đơn hàng" vs "marketing" |
| 5.4 | Xử lý yêu cầu chủ thể | Nhận yêu cầu truy cập/xóa → xác minh danh tính → thực hiện trong 1 tháng → log | [AI AUGMENT] | SLA nhắc hạn; mẫu phản hồi; xác minh trước khi xóa |
| 5.5 | Quản lý processor | Rà soát DPA với từng processor (ShopBase/Klaviyo/Printify/helpdesk); gắn cờ thiếu DPA | [AI WORKFORCE] | Không tích hợp tool mới khi chưa có DPA |
| 5.6 | Breach response | Phát hiện rò rỉ → đánh giá rủi ro → nếu cần thông báo cơ quan ≤72h → log + RCA | [AI ASSIST] | Playbook breach sẵn; đồng hồ 72h bắt đầu từ lúc phát hiện |

## 6. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI | SLO | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Privacy notice live | Có & cập nhật | 100% | Check link | ☐ |
| 2 | Processor có DPA | % processor có DPA | 100% | Processor list | ☐ |
| 3 | Yêu cầu chủ thể đúng hạn | % xử lý ≤ 1 tháng | 100% | Request log | ☐ |
| 4 | Consent marketing | % email gửi có consent | 100% | Opt-in records | ☐ |
| 5 | Breach notify ≤72h | thời gian từ phát hiện → báo | ≤ 72h | Breach log | ☐ |

**Quyết định:** ALL pass → `./output/`. ANY fail → LOOP (max 3) → ESCALATE Founder → Incident Report. Breach luôn tạo Incident Report + RCA.

## 7. Output & Downstream

- **Lưu tại:** `./output/` (data-inventory, privacy-notice, subject-request-log, breach-log) → `./archive/`
- **Downstream:** SOP-FUL-003 (CX AI tuân thủ khi xử lý dữ liệu), SOP-GRW-003 (email chỉ gửi opt-in), SOP-BCK-003 (audit report)
- **Naming:** `sop-bck-005_data-inventory_[YYYY-Q]_DONE_[date].md`, `..._subject-request-log_[YYYY]_DONE_[date].md`

## 8. Phụ lục

- **Upstream:** danh sách tool/processor, privacy notice (Founder duyệt)
- **Downstream:** SOP-FUL-003 (customer support), SOP-GRW-003 (email/promotions)
- **Knowledge:** `../../_knowledge/`
- **Rules / Quality:** `../../_rules/README.md` · `../../quality_bck-001_quality-standards_v1.0_2026-06-03.md`
- **Policy:** `../../../_shared/policies/data-protection-policy.md`
- **TODO Founder (trước launch):** ① publish privacy notice + cookie/consent banner trên ShopBase ② ký/đối chiếu DPA với ShopBase + Klaviyo + Printify + helpdesk ③ lập kênh tiếp nhận yêu cầu chủ thể dữ liệu.
