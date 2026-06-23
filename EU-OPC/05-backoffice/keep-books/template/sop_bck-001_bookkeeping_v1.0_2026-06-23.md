# SOP-BCK-001 — Bookkeeping & Fee Reconciliation

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-finance` `[AI WORKFORCE]`

---

## 0. IPO (Input – Process – Output)
| | |
|---|---|
| **Input** | ShopBase payout/order export, Printify/PrintBase invoice, Facebook Ads billing, Stripe/PayPal fee statement, bank/USD statement |
| **Process** | Ghi sổ kép → đối soát fee (gateway + provider + ads) → phân loại COGS/OPEX → khóa kỳ |
| **Output** | `ledger` (sổ cái theo kỳ), reconciliation log, danh sách discrepancy → feed SOP-BCK-002 (profit) & SOP-BCK-003 (VAT) |

## 1. Tổng quan
Ghi sổ toàn bộ dòng tiền của DAKOfits (~3.200 SP đa niche, US+EU) và đối soát phí. Mọi giao dịch phải truy được về order/SKU để SOP-BCK-002 tính profit-per-SKU. Đối soát hằng tuần, khóa sổ hằng tháng. USD là đồng ghi nhận gốc; quy đổi VND ở bước báo cáo (SOP-BCK-002).

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Ghi sổ giao dịch | finance AI | Owner | — | ops-hr AI |
| Đối soát fee | finance AI | Owner | compliance AI | — |
| Khóa kỳ + ký duyệt | Owner | Owner | finance AI | tất cả phòng |

`[AI WORKFORCE]` finance AI: import & normalize statement, match giao dịch, flag discrepancy >$5 hoặc >2%. Owner: duyệt khóa sổ.

## 3. Quy trình (ICOM)
1. **Thu thập** (I: các export; C: lịch tuần; M: ShopBase/Printify/Meta/Stripe API): finance AI pull statement vào `input/`.
2. **Normalize & ghi sổ** (C: chart of accounts; M: ledger template): map mỗi dòng → tài khoản (Revenue, COGS-print, COGS-ship, Ad-spend, Gateway-fee, Refund).
3. **Đối soát fee** (C: fee schedule provider/gateway): so phí thực tế vs phí kỳ vọng; chênh → ghi vào discrepancy log.
4. **Phân loại & gắn SKU** (M: order_id ↔ SKU map): mỗi giao dịch gắn order_id/SKU phục vụ profit-per-SKU.
5. **Khóa kỳ** (O: ledger khóa, recon log): Owner duyệt; export sang `output/`.

## 4. Phân nhánh
- Discrepancy >2% hoặc >$50 → escalate Owner, giữ kỳ mở.
- Refund/chargeback → ghi âm Revenue + COGS thu hồi (nếu có), gắn ticket FUL.
- Thiếu statement (provider chậm) → ghi accrual, đánh dấu `need_review`.
- Sai tỷ giá nguồn → dùng tỷ giá khóa kỳ của SOP-BCK-002, không tự bịa.

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| Bookkeeping accuracy | ≥ 99.9% giao dịch khớp | recon log |
| Fee reconciliation coverage | 100% statement đối soát | checklist tuần |
| Khóa sổ on-time | ≤ ngày 5 tháng sau | calendar |

**Error budget:** ≤0.1% giao dịch sai/kỳ. **Prevention:** API pull tự động (giảm nhập tay), 4-eyes Owner khi khóa, lưu raw statement trong `archive/` để audit.

## 6. Tài nguyên + Links
- Template: `./README.md` · Output: `../output/` · Archive: `../archive/`
- Liên kết: [SOP-BCK-002](../../track-profit/template/sop_bck-002_profit-roas_v1.0_2026-06-23.md) · [SOP-BCK-003](../../file-vat/template/sop_bck-003_vat-oss-ioss_v1.0_2026-06-23.md)
- Rules: [no fabricated FX/figures](../../_rules/README.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
