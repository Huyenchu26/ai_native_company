# SOP-BCK-001 — Bookkeeping & fee reconciliation

**Department:** Backoffice (bck) · **AI Worker:** Finance AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

> Nền của mọi số liệu tài chính. Đối soát payout (ShopBase) ↔ đơn hàng ↔ invoice Printify ↔ Facebook ad spend ↔ refund.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Ghi nhận chính xác mọi giao dịch, đối soát các nguồn, theo dõi dòng tiền hướng tới target $8,000 (~200 triệu VNĐ)/tháng. |
| **Phạm vi** | Doanh thu, chi phí (Printify base/ship, ShopBase fee, Facebook ad spend, tool), refund. KHÔNG gồm kê khai VAT (BCK-002). |
| **Trigger** | Hàng tuần (đối soát) + đóng sổ cuối tháng. |

### IPO
| | |
|---|---|
| **Input** | Payout report (ShopBase), invoice Printify, Facebook ad spend (Meta Ads), refund (FUL-004), tool subscriptions (ShopBase/Klaviyo/Canva) |
| **Control** | Chuẩn kế toán, accuracy ≥ 99%, lưu trữ ≥ 10 năm |
| **Output** | Sổ cái, cash flow, danh sách khoản phải nộp (VAT → BCK-002), discrepancy log |
| **Mechanism** | Finance AI + Claude API, ShopBase/Printify/Meta Ads API, Google Sheets/Xero |

## 2. RACI
| Hoạt động | Founder | Finance AI |
|---|---|---|
| Ghi nhận & phân loại | I | **R** |
| Đối soát | I | **R** |
| Duyệt đóng sổ | **A** | C |

## 3. Đầu vào
- [ ] Payout reports kỳ (ShopBase) · [ ] Invoice Printify · [ ] Facebook ad spend (Meta) · [ ] Refund log (FUL-004)

## 4. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 4.1 | Pull dữ liệu | Tải payout (ShopBase) + invoice (Printify) + ad spend (Meta) qua API | [AI WORKFORCE] | Không nhập tay |
| 4.2 | Phân loại | Gán doanh thu/chi phí theo nhóm + theo SKU (kèm ad spend theo campaign/SKU) | [AI WORKFORCE] | Bảng phân loại chuẩn |
| 4.3 | Đối soát | Payout ↔ đơn ↔ Printify ↔ ad spend; tìm chênh lệch | [AI AUGMENT] | Diff check; flag chênh ≠ 0 |
| 4.4 | Xử lý chênh | Điều tra discrepancy, sửa hoặc escalate | [AI AUGMENT] | Không đóng sổ khi còn chênh chưa giải thích |
| 4.5 | Đóng sổ | Chốt kỳ → cash flow → khoản phải nộp | [AI AUGMENT] | Founder duyệt |
| 4.6 | Lưu | output/ → archive/ (≥10 năm) | [AI WORKFORCE] | Backup |

## 5. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Accuracy | sai số ghi nhận | ≥ 99% | ☐ |
| 2 | Đối soát | chênh payout vs sổ | = $0 (hoặc giải thích được) | ☐ |
| 3 | Hoàn tất | mọi giao dịch được phân loại | 100% | ☐ |

## 6. Output & Downstream
- **Lưu:** ./output/ledger_[YYYY-MM]_DONE.md, cashflow → archive/
- **Downstream:** BCK-002 (VAT), BCK-003 (profit-per-SKU + ROAS/CPA)

## 7. Phụ lục
VAT: ../vat-oss-ioss/ · Profit: ../profit-financial-report/ · Niche/kinh tế: ../../docs/08-niche-dog-breed-leggings-shopbase.md §4
