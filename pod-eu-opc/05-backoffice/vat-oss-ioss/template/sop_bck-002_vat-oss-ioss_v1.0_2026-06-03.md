# SOP-BCK-002 — VAT / OSS / IOSS

**Department:** Backoffice (bck) · **AI Worker phụ trách:** Finance AI
**Loại:** OPERATIONAL (template → input → processing → output → archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-03 · **Trạng thái:** ACTIVE (v1 — review mỗi quý)

> ⚠️ **Miễn trừ:** SOP này là quy trình vận hành nội bộ, KHÔNG phải tư vấn thuế/pháp lý. Ngưỡng và thuế suất thay đổi theo thời gian và theo nơi đăng ký kinh doanh — **phải xác nhận với kế toán/tư vấn thuế EU** trước khi nộp. AI chuẩn bị số liệu; con người duyệt & nộp.

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | Đảm bảo thu đúng VAT cho từng đơn bán vào EU, kê khai & nộp đúng hạn qua OSS/IOSS, không bị phạt thuế. |
| **Phạm vi** | Mọi đơn B2C bán vào các nước EU qua Etsy (Phase 1) và Shopify (Phase 2). KHÔNG bao gồm thuế thu nhập doanh nghiệp (tách SOP riêng). |
| **Trigger** | (a) Hàng ngày: đơn mới phát sinh → ghi nhận VAT; (b) Theo kỳ: hạn kê khai OSS (hàng quý) / IOSS (hàng tháng); (c) Khi doanh thu xuyên biên giới tiến gần ngưỡng €10,000/năm. |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Đơn hàng theo nước (Etsy/Shopify), giá bán, payout report, dữ liệu nơi giao hàng, nơi xưởng in (Printify provider), trạng thái đăng ký OSS/IOSS |
| **Control** | Quy định VAT EU; ngưỡng micro-business €10,000/năm (bán xuyên biên giới B2C); ngưỡng IOSS €150/đơn hàng nhập khẩu; lịch nộp OSS theo quý; nơi đăng ký KD của công ty |
| **Output** | Sổ VAT theo nước, tờ khai OSS quý (draft), tờ khai IOSS tháng (nếu áp dụng), cảnh báo khi sắp chạm ngưỡng, hồ sơ lưu trữ 10 năm |
| **Mechanism** | Finance AI + Claude API, Etsy/Shopify payout API, Google Sheets/Xero, cổng OSS/IOSS của cơ quan thuế |

---

## 2. Khái niệm nền (Knowledge)

| Khái niệm | Tóm tắt áp dụng cho shop |
|---|---|
| **VAT** | Thuế giá trị gia tăng. Bán B2C trong EU → tính VAT theo **thuế suất nước người mua** (destination principle). |
| **Ngưỡng €10,000/năm** | Nếu công ty đặt **trong EU** và tổng doanh thu bán hàng xuyên biên giới B2C ≤ €10,000/năm → có thể tính VAT theo nước mình. Vượt ngưỡng → bắt buộc theo nước khách (dùng OSS để khai gộp). |
| **OSS (One-Stop-Shop)** | Cơ chế khai gộp VAT cho toàn bộ bán B2C xuyên biên giới EU qua **một** tờ khai (thường theo **quý**) tại 1 nước đăng ký, thay vì đăng ký VAT ở từng nước. |
| **IOSS (Import OSS)** | Áp dụng khi hàng **nhập khẩu vào EU** giá trị ≤ **€150**: thu VAT tại điểm bán, khai theo **tháng**. Liên quan khi **xưởng in nằm NGOÀI EU**. |
| **Marketplace deemed supplier** | Trong một số trường hợp Etsy đóng vai trò "deemed supplier" và tự thu/nộp VAT thay. **Phải xác nhận phần nào Etsy lo, phần nào công ty tự lo** — tránh nộp trùng/thiếu. |

> 🎯 **Khuyến nghị chiến lược (giảm phức tạp):** ưu tiên **xưởng in trong EU** (SOP-MER-002) → hàng không "nhập khẩu" → **tránh IOSS** và hải quan; chỉ cần xử lý VAT nội khối qua OSS.

---

## 3. Vai trò & RACI

| Hoạt động | Founder | Finance AI | Kế toán/tư vấn thuế |
|---|---|---|---|
| Ghi nhận VAT mỗi đơn | I | **R** | I |
| Theo dõi ngưỡng €10,000 | A | **R** | C |
| Soạn draft tờ khai OSS/IOSS | A | **R** | C |
| Duyệt & nộp tờ khai | **R/A** | C | **C** |
| Quyết định đăng ký OSS/IOSS | **A** | C | **R** (tư vấn) |

## 4. Đầu vào & Điều kiện bắt đầu

- [ ] Đã xác định **nước đăng ký kinh doanh** của công ty và trạng thái đăng ký VAT/OSS/IOSS (đặt trong `./input/`)
- [ ] Payout/transaction report kỳ này đã tải về `./input/`
- [ ] Bảng map **nơi xưởng in** (EU/ngoài EU) cho từng SKU (từ SOP-MER-002)
- [ ] Xác nhận phạm vi Etsy "deemed supplier" cho thị trường liên quan

## 5. Quy trình

> Tag AI: [AI ASSIST] người chính · [AI AUGMENT] AI làm + người duyệt · [AI WORKFORCE] AI tự chạy

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 5.1 | Thu thập đơn | Tải payout/order report theo kỳ, chuẩn hóa: nước giao hàng, giá, VAT đã thu, kênh | [AI WORKFORCE] | Pull tự động qua API → không nhập tay; reconcile số đơn API vs report |
| 5.2 | Phân loại VAT | Gán thuế suất VAT theo **nước người mua**; đánh dấu đơn Etsy đã "deemed supplier" (không khai lại) | [AI AUGMENT] | Bảng thuế suất theo nước cập nhật hàng quý; flag đơn không map được |
| 5.3 | Kiểm ngưỡng | Cộng dồn doanh thu xuyên biên giới B2C YTD; cảnh báo khi đạt 80% và 100% của €10,000 | [AI WORKFORCE] | Auto-alert ở 80% ngưỡng → Founder có thời gian đăng ký OSS trước khi vượt |
| 5.4 | Xử lý nhập khẩu | Nếu có SKU in **ngoài EU** & đơn ≤ €150 → tính IOSS; >€150 → cờ "cần thủ tục nhập khẩu" | [AI AUGMENT] | Ưu tiên provider EU để nhánh này = rỗng; nếu phát sinh → escalate |
| 5.5 | Soạn tờ khai | Tổng hợp VAT theo nước → draft tờ khai OSS (quý) / IOSS (tháng) vào `./processing/` | [AI AUGMENT] | Đối chiếu tổng VAT khai vs tổng VAT ghi nhận trong sổ (chênh = 0) |
| 5.6 | Duyệt & nộp | Founder (+ kế toán nếu cần) duyệt → nộp qua cổng thuế → lưu xác nhận | [AI ASSIST] | Checklist trước nộp ở §6; reminder hạn nộp trước 5 ngày |
| 5.7 | Lưu trữ | Lưu sổ + tờ khai + xác nhận nộp vào `./output/` → cuối kỳ `./archive/` (giữ ≥10 năm) | [AI WORKFORCE] | Lưu trữ bất biến; backup theo SOP backup |

## 6. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI | SLO | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Đối soát đơn | % đơn trong report khớp API | 100% | Count(API) = Count(report) | ☐ |
| 2 | Map thuế suất | % đơn được gán VAT đúng nước | 100% | Không còn đơn "unmapped" | ☐ |
| 3 | Cân đối VAT | Chênh lệch VAT khai vs sổ | = €0 | Diff check tự động | ☐ |
| 4 | Đúng hạn | Tờ khai nộp trước deadline | 100% | Ngày nộp ≤ hạn − 1 | ☐ |
| 5 | Cảnh báo ngưỡng | Alert khi đạt 80%/100% €10k | 100% | Log alert | ☐ |

**Quyết định:** ALL pass → `./output/` + nộp. ANY fail → LOOP (max 3) → ESCALATE Founder + kế toán → Incident Report tại `../../../_quality/reports/`.

## 7. Output & Downstream

- **Lưu tại:** `./output/` → `./archive/[YYYY-MM]/` (giữ ≥10 năm theo yêu cầu lưu trữ VAT EU)
- **Naming:** `sop-bck-002_vat-return-oss_[YYYY-Q]_DONE_[date].md`, `..._vat-ledger_[YYYY-MM]_DONE_[date].md`
- **Downstream:** SOP-BCK-001 (bookkeeping — VAT là khoản phải nộp), SOP-BCK-003 (profit-per-SKU dùng giá net-of-VAT)

## 8. Phụ lục

- **Upstream:** SOP-BCK-001 (payout data), SOP-MER-002 (nơi xưởng in), SOP-MER-003 (pricing — VAT có gộp trong giá bán?)
- **Knowledge:** `../../_knowledge/` (bảng thuế suất VAT theo nước — cập nhật hàng quý)
- **Rules / Quality:** `../../_rules/README.md` · `../../quality_bck-001_quality-standards_v1.0_2026-06-03.md`
- **Lịch tuân thủ:** `../legal-registration-calendar.md` (SOP-BCK-007)
- **Thiết kế:** `../../../02-design/opc-design-roadmap.md` §6.1
- **TODO Founder:** ① chốt nước đăng ký KD ② quyết định đăng ký OSS ngay hay chờ ngưỡng ③ xác nhận phạm vi Etsy deemed-supplier với kế toán.
