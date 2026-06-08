# SOP-BCK-004 — GPSR compliance + Meta Ad Policy + IP/TM (Responsible Person, labeling)

**Department:** Backoffice (bck) · **AI Worker phụ trách:** Compliance AI
**Loại:** OPERATIONAL (template → input → processing → output → archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-08 · **Trạng thái:** ACTIVE (rào pháp lý — ưu tiên cao nhất)

> ⚠️ **Miễn trừ:** Quy trình vận hành nội bộ, không phải tư vấn pháp lý. GPSR (Regulation EU 2023/988) áp dụng từ **13/12/2024** cho đơn EU. Meta Advertising Policies thay đổi liên tục. Yêu cầu cụ thể tùy sản phẩm — **xác nhận với tư vấn pháp lý EU**. Nếu thiếu **Responsible Person trong EU**, đơn vào EU có thể bị từ chối hoặc gỡ; nếu creative vi phạm Meta Policy → ad bị reject / account bị ban.

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | Đảm bảo (a) ad creative đạt Meta Ad Policy (chống ban — gate trước khi chạy ads); (b) mọi đơn EU tuân thủ GPSR (có Responsible Person EU, đủ nhãn truy xuất & an toàn); (c) tên breed không vi phạm IP/TM → không bị gỡ listing, không ban ad, không rủi ro pháp lý. |
| **Phạm vi** | Tất cả ad creative chạy Facebook Ads; tất cả listing/SKU bán vào EU (GPSR); IP/TM check theo tên breed cho mọi listing. |
| **Trigger** | (a) Trước khi chạy bất kỳ ad creative mới (gate Meta Policy); (b) Trước khi publish bất kỳ listing mới (gate GPSR cho đơn EU + IP/TM trong SOP-MER-001); (c) Audit định kỳ hàng tháng listing active + ad account health; (d) Khi đổi quy định / đổi print provider. |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Ad creative + copy (từ SOP-GRW-005 FB Creative), listing chuẩn bị publish (từ SOP-MER-001), thông tin product Printify (nhà sản xuất/provider US/EU), thông tin Responsible Person EU, tên breed, quy định GPSR + Meta Policy + IP/TM hiện hành |
| **Control** | Meta Advertising Policies; GPSR (EU 2023/988 — đơn EU); yêu cầu nhãn: nhà sản xuất, Responsible Person EU, định danh sản phẩm, cảnh báo an toàn; IP/TM (USPTO/EUIPO theo tên breed); ShopBase TOS |
| **Output** | Meta Policy review log, GPSR clearance log mỗi SKU (đơn EU), IP/TM clearance theo breed, nội dung nhãn chèn vào listing, danh sách non-compliant cần sửa, audit report tháng |
| **Mechanism** | Compliance AI + Claude API, Meta Policy guide/Ad Manager, ShopBase API (đọc/sửa listing), Printify API (thông tin provider), USPTO/EUIPO search |

---

## 2. Yêu cầu (Knowledge)

### 2a. Meta Ad Policy (chống ban) — gate trước khi chạy ads
| # | Điểm cần né | Áp dụng cho shop |
|---|---|---|
| 1 | **Personal attributes** | Không ám chỉ trực tiếp danh tính người xem theo cách Meta cấm (vd "you, the depressed dog owner"). Dùng affinity gián tiếp: "For Golden Retriever moms". |
| 2 | **Before/after & claim phi thực tế** | Apparel ít rủi ro; tránh claim sức khỏe (vd "chữa lo âu"). |
| 3 | **IP trong creative** | Không dùng logo/ảnh có bản quyền; design AOP tự tạo. |
| 4 | **Misleading / clickbait** | Giá, urgency ("limited sizes") phải đúng thực tế. |
| 5 | **Landing page match** | Product page ShopBase khớp nội dung ad (Meta quét). |

### 2b. GPSR cho AOP leggings (đơn EU)
| # | Yêu cầu | Áp dụng cho shop |
|---|---|---|
| 1 | **Responsible Person trong EU** | Một pháp nhân/cá nhân đặt tại EU chịu trách nhiệm an toàn sản phẩm. Công ty ngoài EU → ủy quyền RP (Printify có thể cung cấp/khuyến nghị dịch vụ RP cho một số sản phẩm). |
| 2 | **Thông tin nhà sản xuất** | Tên + địa chỉ + liên hệ của print provider Printify (EU: Latvia/UK/DE) hiển thị được. |
| 3 | **Định danh sản phẩm** | Model/SKU/batch để truy xuất. |
| 4 | **Cảnh báo & hướng dẫn an toàn** | Với leggings/apparel người lớn: thường tối thiểu (giặt, chất liệu). Sản phẩm trẻ em rủi ro cao hơn. |
| 5 | **Hiển thị trước khi mua** | Thông tin trên/kèm product page để người mua EU thấy trước khi đặt. |

### 2c. IP / Trademark theo tên breed
| # | Quy tắc | Áp dụng |
|---|---|---|
| 1 | **Breed name** | Tên giống chó (Golden Retriever, Corgi…) nói chung là generic — nhưng **tránh tên/cụm đã đăng ký TM** (vd club/brand cụ thể). |
| 2 | **Mô tả chung** | Khi nghi ngờ → dùng mô tả chung, không gắn thương hiệu. |
| 3 | **Check trước listing** | Tra USPTO/EUIPO cho cụm từ dùng trong title/design → rủi ro → block listing. |

> 🎯 **Đòn bẩy:** Printify hỗ trợ thông tin GPSR/RP cho nhiều catalog — SOP-MER-003 ưu tiên provider EU cho đơn EU + sản phẩm có sẵn dữ liệu GPSR để bước nhãn gần như tự động.

---

## 3. Vai trò & RACI

| Hoạt động | Founder | Compliance AI | FB Creative AI (03) / Product Page AI (02) |
|---|---|---|---|
| Thiết lập Responsible Person EU | **R/A** | C | I |
| Meta Ad Policy review creative (gate ads) | A | **R** | C (FB Creative AI sửa) |
| IP/TM check theo breed | A | **R** | C (Product Page AI) |
| Sinh nội dung nhãn GPSR mỗi SKU (EU) | I | **R** | C (Product Page AI chèn) |
| Gate trước publish | A | **R** | C (Product Page AI) |
| Audit listing active + ad health hàng tháng | A | **R** | I |
| Xử lý non-compliant | A | **R** | C |

## 4. Đầu vào & Điều kiện bắt đầu

- [ ] **Responsible Person EU đã được thiết lập** (điều kiện tiên quyết cho đơn EU — Founder xử lý trước launch EU) → lưu tại `./input/responsible-person.md`
- [ ] Mapping mỗi SKU → print provider Printify (US/EU) + thông tin nhà sản xuất (từ SOP-MER-003)
- [ ] Ad creative draft cần Meta Policy review đặt trong `./input/`
- [ ] Listing draft cần GPSR + IP/TM clearance đặt trong `./input/`

## 5. Quy trình

> Tag AI: [AI ASSIST] · [AI AUGMENT] · [AI WORKFORCE]

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 5.1 | Meta Ad Policy review | Quét creative/copy theo checklist §2a; đạt → pass cho FB Ads; không đạt → trả FB Creative AI sửa | [AI AUGMENT] | Gate cứng: no Meta policy → no ads (FB Ads không chạy creative chưa pass) |
| 5.2 | IP/TM breed check | Tra cụm từ breed/title/design vs USPTO/EUIPO; rủi ro → block, đề xuất mô tả chung | [AI AUGMENT] | Không listing tên breed vi phạm TM; nghi ngờ → escalate Founder |
| 5.3 | Kiểm tra RP (EU) | Xác nhận SKU thuộc phạm vi Responsible Person EU đã thiết lập | [AI WORKFORCE] | Không có RP hợp lệ → BLOCK publish đơn EU (không thể bỏ qua) |
| 5.4 | Thu thập dữ liệu nhà SX | Lấy tên/địa chỉ provider Printify + định danh sản phẩm | [AI WORKFORCE] | Pull qua API; thiếu trường → flag, không tự bịa |
| 5.5 | Sinh nội dung nhãn GPSR | Soạn block GPSR (RP, nhà SX, định danh, cảnh báo) theo template cho đơn EU | [AI AUGMENT] | Template chuẩn hóa → không sót trường; checklist 5 yêu cầu §2b |
| 5.6 | Kiểm sản phẩm trẻ em | Nếu mở rộng đồ trẻ em → checklist an toàn nghiêm hơn → escalate Founder | [AI AUGMENT] | Auto-detect category "kids/baby" → bắt buộc review người |
| 5.7 | Cấp clearance | Đạt → ghi GPSR clearance log + IP/TM clear → trả nhãn cho SOP-MER-001 chèn vào listing | [AI AUGMENT] | Clearance log gắn SKU; listing không có log → MER-001 không publish |
| 5.8 | Audit tháng | Quét listing EU active (còn đủ nhãn? RP còn hiệu lực? provider đổi?) + rà ad account health | [AI WORKFORCE] | Lịch tự động; xuất danh sách non-compliant → sửa trong 48h |

## 6. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI | SLO | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Meta Ad Policy | % creative pass trước khi chạy | 100% | Policy review log | ☐ |
| 2 | Có Responsible Person EU | % SKU EU thuộc RP hợp lệ | 100% | Check RP record | ☐ |
| 3 | Đủ trường nhãn (EU) | % SKU đủ 5 yêu cầu §2b | 100% | Checklist tự động | ☐ |
| 4 | IP/TM breed | % listing được check TM | 100% | TM search log | ☐ |
| 5 | Hiển thị trước mua | Nhãn có mặt trên product page EU | 100% | Scan listing | ☐ |
| 6 | Audit coverage | % listing EU active được audit/tháng | 100% | Audit report | ☐ |

**Quyết định:** ALL pass → cấp clearance → `./output/`. ANY fail → **BLOCK** (publish hoặc ads) + LOOP (max 3) → ESCALATE Founder → Incident Report. **Không có ngoại lệ cho #1 (Meta Policy), #2 (RP) và #4 (TM).**

## 7. Output & Downstream

- **Lưu tại:** `./output/gpsr-clearance-log_[YYYY-MM].md` (mỗi SKU 1 dòng), `meta-policy-review-log_[YYYY-MM].md` → `./archive/`
- **Downstream:** SOP-GRW-005/GRW-002 (gate Meta Policy → no ads), SOP-MER-001 (chèn nhãn + gate publish), audit feed về SOP-BCK-003 report
- **Naming:** `sop-bck-004_gpsr-clearance_[YYYY-MM]_DONE_[date].md`, `..._meta-policy_[YYYY-MM]_DONE_[date].md`, `..._gpsr-audit_[YYYY-MM]_DONE_[date].md`

## 8. Phụ lục

- **Upstream:** SOP-GRW-005 (creative), SOP-MER-003 (provider/nhà SX), thiết lập RP (Founder)
- **Downstream:** SOP-GRW-002 (gate chạy ads), SOP-MER-001 (gate publish listing)
- **Knowledge:** `../../_knowledge/` (tóm tắt GPSR + Meta Policy + danh mục yêu cầu theo category)
- **Rules / Quality:** `../../_rules/README.md` · `../../quality_bck-001_quality-standards_v1.0_2026-06-03.md`
- **Policy:** `../../../_shared/policies/ip-policy.md`, `../legal-registration-calendar.md`
- **Niche/FB Ads:** `../../docs/08-niche-dog-breed-leggings-shopbase.md` §5, §8
- **TODO Founder (BLOCKER):** ① thiết lập **Responsible Person trong EU** (pháp nhân EU hoặc dịch vụ RP Printify/bên thứ ba) cho đơn EU ② cấu trúc BM đúng + warm ad account chống ban (xem niche §5). Không có RP → không bán vào EU; creative không pass Meta Policy → không chạy ads.
