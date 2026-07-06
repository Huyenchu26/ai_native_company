# SOP-BCK-004 — GPSR Compliance & Responsible Person `[GATE CỨNG]`

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-compliance` `[AI WORKFORCE]`

> ⛔ **GATE CỨNG: No GPSR clearance → No publish (EU).** Không có Responsible Person + nhãn an toàn EU + IP/TM clearance → SP KHÔNG được lên store cho thị trường EU.

---

## 0. IPO
| | |
|---|---|
| **Input** | SP/design chờ publish (Merch SOP-MER-001), breed/niche name, provider EU info, product safety data (material, care) |
| **Process** | Verify Responsible Person → soạn nhãn an toàn EU → IP/TM breed check → clearance decision |
| **Output** | `clearance log` (PASS/FAIL), nhãn GPSR (text chèn vào product page EU), IP/TM check record, audit trail |

## 1. Tổng quan
GPSR (EU 2023/988, hiệu lực 13/12/2024) yêu cầu mọi SP bán cho consumer EU phải có: (1) **Responsible Person** đặt tại EU (tên + địa chỉ + email), (2) **nhãn an toàn**: manufacturer info, product ID, warning/care, material; (3) traceability. Với POD đa niche, mỗi SP còn cần **IP/TM clearance** theo tên breed/niche (tránh trademark dog-breed brand). Đây là gate cứng: compliance AI ra quyết định PASS/FAIL, Merch chỉ publish EU khi PASS.

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Verify Responsible Person | compliance AI | Owner | — | — |
| Soạn nhãn an toàn EU | compliance AI | Owner | — | Merch (product-page) |
| IP/TM breed check | compliance AI | Owner | Product Studio | — |
| Clearance decision (gate) | compliance AI | Owner | — | Merch, Growth |

`[AI WORKFORCE]` compliance AI: chạy checklist GPSR, soạn nhãn, IP/TM lookup, ghi clearance log. Owner: ký duyệt FAIL→exception hoặc xác nhận Responsible Person hợp lệ.

## 3. Quy trình (ICOM)
1. **Nhận SP chờ EU publish** (I: SP/design + niche; C: GPSR checklist): vào `input/`.
2. **Verify Responsible Person** (C: EU RP requirement; M: RP registry): xác nhận RP đặt tại EU + contact hợp lệ.
3. **Soạn nhãn an toàn** (C: GPSR label spec; M: label template): manufacturer, product ID, material, warning/care EN.
4. **IP/TM breed check** (C: breed trademark watchlist; M: TM search): không trùng nhãn hiệu đã đăng ký.
5. **Clearance decision** (O: clearance log PASS/FAIL): PASS → nhãn handoff Merch; FAIL → block + lý do.

## 4. Phân nhánh
- Không có Responsible Person EU → **FAIL, block publish EU** (không ngoại lệ tự động).
- IP/TM trùng/nghi ngờ → FAIL, trả Product Studio re-clear (SOP-PRD-004).
- Chỉ bán US (không EU) → GPSR không bắt buộc; vẫn cần IP/TM clearance.
- Provider EU đổi → cập nhật RP info, re-verify nhãn.

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| GPSR clearance rate trước publish EU | **100%** (gate cứng) | clearance log |
| Responsible Person present | 100% đơn EU | RP registry |
| IP/TM clearance | 100% trước listing | TM record |
| Nhãn an toàn đầy đủ trường | 100% | label QC |

**Error budget (compliance):** **0%** — không SP EU nào lên store thiếu clearance (legal, ngoại lệ 100% bắt buộc). **Prevention:** gate tự động chặn publish ở Merch nếu thiếu clearance log PASS; breed watchlist versioned; audit trail mọi quyết định trong `archive/`.

## 6. Tài nguyên + Links
- [_knowledge: GPSR + Responsible Person](../../_knowledge/README.md) · [SOP-MER-001 product page](../../../02-merchandising/write-product-page/) · [SOP-PRD-004 IP clearance](../../../01-product-studio/clear-ip/)
- Rule: [no-GPSR-no-publish](../../_rules/README.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo — gate cứng |
