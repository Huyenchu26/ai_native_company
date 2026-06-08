# SOP-BCK-002 — VAT / OSS / IOSS (+ US sales tax note)

**Department:** Backoffice (bck) · **AI Worker phụ trách:** Finance AI
**Loại:** OPERATIONAL (template → input → processing → output → archive)
**Phiên bản:** v1.0 · **Ngày:** 2026-06-08 · **Trạng thái:** ACTIVE (v1 — review mỗi quý)

> ⚠️ **Miễn trừ:** SOP này là quy trình vận hành nội bộ, KHÔNG phải tư vấn thuế/pháp lý. Ngưỡng và thuế suất thay đổi theo thời gian và theo nơi đăng ký kinh doanh — **phải xác nhận với kế toán/tư vấn thuế EU** trước khi nộp. AI chuẩn bị số liệu; con người duyệt & nộp.

---

## 1. Tổng quan

| Mục | Nội dung |
|---|---|
| **Mục đích** | Đảm bảo thu đúng VAT cho từng đơn bán vào EU, kê khai & nộp đúng hạn qua OSS/IOSS, không bị phạt thuế; đối soát US sales tax (do ShopBase/marketplace xử lý). |
| **Phạm vi** | Mọi đơn B2C bán vào các nước EU qua ShopBase. Đơn US: ghi chú/đối soát sales tax (không tự kê khai). KHÔNG bao gồm thuế thu nhập doanh nghiệp (tách SOP riêng). |
| **Trigger** | (a) Hàng ngày: đơn EU mới → ghi nhận VAT; (b) Theo kỳ: hạn kê khai OSS (hàng quý) / IOSS (hàng tháng); (c) Khi doanh thu xuyên biên giới EU tiến gần ngưỡng €10,000/năm. |

### IPO
| Thành phần | Chi tiết |
|---|---|
| **Input** | Đơn hàng theo nước (ShopBase), giá bán, payout report, dữ liệu nơi giao hàng, nơi xưởng in (Printify provider: US / EU Latvia-UK-DE), trạng thái đăng ký OSS/IOSS, dữ liệu US sales tax từ ShopBase |
| **Control** | Quy định VAT EU; ngưỡng micro-business €10,000/năm (bán xuyên biên giới B2C EU); ngưỡng IOSS €150/đơn nhập khẩu; lịch nộp OSS theo quý; nơi đăng ký KD của công ty; US sales tax nexus (ShopBase/marketplace facilitator) |
| **Output** | Sổ VAT theo nước EU, tờ khai OSS quý (draft), tờ khai IOSS tháng (nếu áp dụng), ghi chú đối soát US sales tax, cảnh báo khi sắp chạm ngưỡng, hồ sơ lưu trữ 10 năm |
| **Mechanism** | Finance AI + Claude API, ShopBase payout API, Google Sheets/Xero, cổng OSS/IOSS của cơ quan thuế |

---

## 2. Khái niệm nền (Knowledge)

| Khái niệm | Tóm tắt áp dụng cho shop |
|---|---|
| **VAT** | Thuế giá trị gia tăng. Bán B2C trong EU → tính VAT theo **thuế suất nước người mua** (destination principle). |
| **Ngưỡng €10,000/năm** | Nếu công ty đặt **trong EU** và tổng doanh thu bán hàng xuyên biên giới B2C ≤ €10,000/năm → có thể tính VAT theo nước mình. Vượt ngưỡng → bắt buộc theo nước khách (dùng OSS để khai gộp). |
| **OSS (One-Stop-Shop)** | Cơ chế khai gộp VAT cho toàn bộ bán B2C xuyên biên giới EU qua **một** tờ khai (thường theo **quý**) tại 1 nước đăng ký, thay vì đăng ký VAT ở từng nước. |
| **IOSS (Import OSS)** | Áp dụng khi hàng **nhập khẩu vào EU** giá trị ≤ **€150**: thu VAT tại điểm bán, khai theo **tháng**. Liên quan khi **xưởng in Printify nằm NGOÀI EU** (vd US) mà giao đơn EU. |
| **US sales tax** | Đơn giao trong US: sales tax theo state/nexus. **ShopBase / marketplace facilitator** thường tự thu/nộp thay. Công ty chỉ **đối soát** — xác nhận phạm vi nào ShopBase lo, phần nào tự lo, với kế toán US. |

> 🎯 **Khuyến nghị chiến lược (giảm phức tạp):** với đơn EU, ưu tiên **xưởng in trong EU** (Printify Latvia/UK/DE — SOP-MER-003) → hàng không "nhập khẩu" → **tránh IOSS** và hải quan; chỉ cần xử lý VAT nội khối qua OSS. Đơn US dùng provider US.

---

## 3. Vai trò & RACI

| Hoạt động | Founder | Finance AI | Kế toán/tư vấn thuế |
|---|---|---|---|
| Ghi nhận VAT mỗi đơn EU | I | **R** | I |
| Theo dõi ngưỡng €10,000 | A | **R** | C |
| Soạn draft tờ khai OSS/IOSS | A | **R** | C |
| Đối soát US sales tax (ShopBase) | A | **R** | C |
| Duyệt & nộp tờ khai | **R/A** | C | **C** |
| Quyết định đăng ký OSS/IOSS | **A** | C | **R** (tư vấn) |

## 4. Đầu vào & Điều kiện bắt đầu

- [ ] Đã xác định **nước đăng ký kinh doanh** của công ty và trạng thái đăng ký VAT/OSS/IOSS (đặt trong `./input/`)
- [ ] Payout/transaction report kỳ này đã tải về `./input/` (ShopBase)
- [ ] Bảng map **nơi xưởng in** Printify (EU/US) cho từng SKU (từ SOP-MER-003)
- [ ] Xác nhận phạm vi ShopBase/marketplace tự thu nộp US sales tax + VAT (nếu có)

## 5. Quy trình

> Tag AI: [AI ASSIST] người chính · [AI AUGMENT] AI làm + người duyệt · [AI WORKFORCE] AI tự chạy

| # | Bước | Hành động | Tag AI | Prevention (chống lỗi từ gốc) |
|---|---|---|---|---|
| 5.1 | Thu thập đơn | Tải payout/order report theo kỳ (ShopBase), chuẩn hóa: nước giao hàng, giá, VAT/sales tax đã thu, kênh | [AI WORKFORCE] | Pull tự động qua API → không nhập tay; reconcile số đơn API vs report |
| 5.2 | Phân loại VAT (EU) | Gán thuế suất VAT theo **nước người mua** EU; tách riêng đơn US (sales tax) | [AI AUGMENT] | Bảng thuế suất theo nước cập nhật hàng quý; flag đơn không map được |
| 5.3 | Kiểm ngưỡng | Cộng dồn doanh thu xuyên biên giới B2C EU YTD; cảnh báo khi đạt 80% và 100% của €10,000 | [AI WORKFORCE] | Auto-alert ở 80% ngưỡng → Founder có thời gian đăng ký OSS trước khi vượt |
| 5.4 | Xử lý nhập khẩu | Nếu có SKU in **ngoài EU** (vd US) & đơn EU ≤ €150 → tính IOSS; >€150 → cờ "cần thủ tục nhập khẩu" | [AI AUGMENT] | Ưu tiên provider EU cho đơn EU để nhánh này = rỗng; nếu phát sinh → escalate |
| 5.5 | Đối soát US sales tax | Đối chiếu sales tax ShopBase đã thu/nộp cho đơn US; ghi chú, không tự kê khai | [AI AUGMENT] | Xác nhận marketplace facilitator phạm vi với kế toán US; flag state thiếu |
| 5.6 | Soạn tờ khai | Tổng hợp VAT theo nước EU → draft tờ khai OSS (quý) / IOSS (tháng) vào `./processing/` | [AI AUGMENT] | Đối chiếu tổng VAT khai vs tổng VAT ghi nhận trong sổ (chênh = 0) |
| 5.7 | Duyệt & nộp | Founder (+ kế toán nếu cần) duyệt → nộp qua cổng thuế → lưu xác nhận | [AI ASSIST] | Checklist trước nộp ở §6; reminder hạn nộp trước 5 ngày |
| 5.8 | Lưu trữ | Lưu sổ + tờ khai + xác nhận nộp vào `./output/` → cuối kỳ `./archive/` (giữ ≥10 năm) | [AI WORKFORCE] | Lưu trữ bất biến; backup theo SOP backup |

## 6. Quality Gate (SLI / SLO)

| # | Tiêu chí | SLI | SLO | Cách kiểm tra | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Đối soát đơn | % đơn trong report khớp API | 100% | Count(API) = Count(report) | ☐ |
| 2 | Map thuế suất | % đơn EU được gán VAT đúng nước | 100% | Không còn đơn "unmapped" | ☐ |
| 3 | Cân đối VAT | Chênh lệch VAT khai vs sổ | = €0 | Diff check tự động | ☐ |
| 4 | Đúng hạn | Tờ khai nộp trước deadline | 100% | Ngày nộp ≤ hạn − 1 | ☐ |
| 5 | Cảnh báo ngưỡng | Alert khi đạt 80%/100% €10k | 100% | Log alert | ☐ |
| 6 | US sales tax | Đơn US được đối soát sales tax | 100% | Reconcile vs ShopBase | ☐ |

**Quyết định:** ALL pass → `./output/` + nộp. ANY fail → LOOP (max 3) → ESCALATE Founder + kế toán → Incident Report tại `../../../_quality/reports/`.

## 7. Output & Downstream

- **Lưu tại:** `./output/` → `./archive/[YYYY-MM]/` (giữ ≥10 năm theo yêu cầu lưu trữ VAT EU)
- **Naming:** `sop-bck-002_vat-return-oss_[YYYY-Q]_DONE_[date].md`, `..._vat-ledger_[YYYY-MM]_DONE_[date].md`
- **Downstream:** SOP-BCK-001 (bookkeeping — VAT là khoản phải nộp), SOP-BCK-003 (profit-per-SKU dùng giá net-of-VAT)

## 8. Phụ lục

- **Upstream:** SOP-BCK-001 (payout data), SOP-MER-003 (nơi xưởng in + pricing — VAT có gộp trong giá bán?)
- **Knowledge:** `../../_knowledge/` (bảng thuế suất VAT theo nước — cập nhật hàng quý)
- **Rules / Quality:** `../../_rules/README.md` · `../../quality_bck-001_quality-standards_v1.0_2026-06-03.md`
- **Lịch tuân thủ:** `../legal-registration-calendar.md` (SOP-BCK-007)
- **Niche/kinh tế:** `../../docs/08-niche-dog-breed-leggings-shopbase.md` §4
- **TODO Founder:** ① chốt nước đăng ký KD ② quyết định đăng ký OSS ngay hay chờ ngưỡng ③ xác nhận phạm vi ShopBase/marketplace tự thu US sales tax + VAT với kế toán.
