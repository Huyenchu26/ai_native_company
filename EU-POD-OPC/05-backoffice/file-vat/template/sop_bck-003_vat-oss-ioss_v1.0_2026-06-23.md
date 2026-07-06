# SOP-BCK-003 — VAT EU (OSS/IOSS) + US Sales Tax Note

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-finance` `[AI WORKFORCE]`

---

## 0. IPO
| | |
|---|---|
| **Input** | Order export theo nước (ShopBase), giá trị đơn EU, ledger (SOP-BCK-001), ngưỡng IOSS €150, VAT rate từng EU member state |
| **Process** | Phân loại OSS vs IOSS → tính VAT theo nước đến → lập tờ khai draft → ghi chú US sales tax |
| **Output** | `tờ khai VAT (draft)` OSS/IOSS theo kỳ, VAT ledger, US sales-tax nexus note |

## 1. Tổng quan
DAKOfits bán EU → phải thu & nộp VAT theo **nước đến (destination)**. Hàng từ Printify/PrintBase EU (đã ở EU) hoặc nhập từ ngoài EU:
- **IOSS** cho đơn ≤ €150 nhập từ ngoài EU (thu VAT tại điểm bán, 1 tờ khai/tháng).
- **OSS (Union scheme)** cho hàng đã ở EU bán xuyên biên giới EU (1 tờ khai/quý).
- **US sales tax:** ghi chú nexus theo bang (economic nexus thresholds); ShopBase thu tự động nếu đã set — finance AI chỉ reconcile + note, không tự khai.

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Phân loại OSS/IOSS | finance AI | Owner | compliance AI | — |
| Tính VAT theo nước | finance AI | Owner | — | — |
| Tờ khai draft | finance AI | Owner | — | Owner |
| Nộp tờ khai | Owner | Owner | finance AI | — |

`[AI WORKFORCE]` finance AI: phân loại scheme, tính VAT đúng rate từng nước, lập draft. Owner: nộp qua portal (không tự động nộp).

## 3. Quy trình (ICOM)
1. **Lấy đơn EU** (I: order export; C: lịch OSS quý / IOSS tháng): tách đơn theo nước đến + giá trị.
2. **Phân loại scheme** (C: ngưỡng €150, xuất xứ hàng): gán OSS hoặc IOSS từng đơn.
3. **Tính VAT** (C: bảng VAT rate member state; M: VAT calc): VAT = giá × rate nước đến.
4. **Lập tờ khai draft** (M: OSS/IOSS template; O: draft): tổng hợp theo nước + scheme.
5. **US note + handoff** (O: nexus note): reconcile sales tax ShopBase đã thu; Owner duyệt & nộp.

## 4. Phân nhánh
- Đơn vượt €150 từ ngoài EU → ngoài IOSS, VAT thu khi nhập khẩu → flag note carrier/DDP.
- Thiếu VAT number/OSS registration → escalate Owner ngay (rủi ro pháp lý).
- Rate member state thay đổi → cập nhật `_knowledge` trước khi tính, không dùng rate cũ.
- US bang đạt nexus mới → cờ `need_review` để Owner đăng ký.

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| VAT filing on-time | **100%** (gate cứng legal) | calendar deadline |
| VAT rate accuracy | 100% đúng rate nước đến | spot-check vs bảng official |
| OSS/IOSS phân loại đúng | ≥ 99.5% | audit mẫu |

**Error budget (compliance):** 0% cho on-time filing (legal — ngoại lệ 100% bắt buộc). **Prevention:** lịch deadline OSS/IOSS hard-coded, bảng VAT rate versioned trong `_knowledge`, Owner 4-eyes trước nộp.

## 6. Tài nguyên + Links
- [SOP-BCK-001](../../keep-books/template/sop_bck-001_bookkeeping_v1.0_2026-06-23.md) · [_knowledge: OSS/IOSS + VAT rates](../../_knowledge/README.md)
- Rule: VAT on-time 100% — [_rules](../../_rules/README.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
