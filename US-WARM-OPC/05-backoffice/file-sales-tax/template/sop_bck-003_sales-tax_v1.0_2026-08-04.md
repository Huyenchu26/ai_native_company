# SOP-BCK-003 — US Sales Tax (nexus, collect, remit)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 05-Backoffice · **Responsible AI:** `vibe-us-warm-bck-finance`
**Delta vs EU:** thay VAT OSS/IOSS bằng **US sales tax** (không phải VAT).

## 1. Mục tiêu
Xác định **economic nexus** theo từng bang, đăng ký, thu đúng thuế suất, nộp đúng hạn. Sales tax là **thu hộ** — KHÔNG phải doanh thu/chi phí (tách khỏi P&L, xem unit-economics §1).

## 2. IPO/ICOM
- **Input:** doanh số theo bang, ngưỡng nexus, tax registration status.
- **Control:** Wayfair economic nexus (đa số bang: **$100k HOẶC 200 giao dịch/năm**, một số bang khác ngưỡng); Shopify KHÔNG mặc định là marketplace facilitator → **DAKOfits tự thu & nộp** (hoặc qua TaxJar/Avalara); nộp đúng hạn từng bang.
- **Output:** `sales-tax-status.json` (schema `sales-tax-status.schema.json`) — per-state nexus, registered, collected, remitted, filing due.
- **Mechanism:** TaxJar/Avalara API, state DOR portals (thiếu → status=needs_registration, KHÔNG khai đã nộp).

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Đo doanh số/bang vs ngưỡng nexus | vượt ngưỡng → phải đăng ký, KHÔNG bỏ sót |
| 3.2 | Đăng ký bang có nexus | thu thuế mà chưa đăng ký = vi phạm |
| 3.3 | Thu đúng rate (destination-based) | rate theo địa chỉ giao, không dùng 1 rate |
| 3.4 | Nộp đúng hạn | trễ → phạt; auto-remind theo lịch bang |

## 4. RACI
R: bck-finance · A: Owner · C: bck-orchestrator · I: —.
HITL: bang mới đạt nexus (đăng ký); nghi ngờ ngưỡng; audit.

## 5. Gate (allOf/if-then)
tax_collected=true ⇒ registered=true (không thu khi chưa đăng ký). remitted=true ⇒ collected ∧ filing_confirmation present. Fail-closed: thiếu tool → needs_registration/pending, không khai remitted.

## 6. Links
[unit-economics](../../../_shared/unit-economics.md) (sales tax tách khỏi contribution). Downstream: [track-profit](../../track-profit/template/sop_bck-002_profit_v1.0_2026-08-04.md).

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — US economic nexus (Wayfair), tự thu/nộp, tách khỏi P&L. |
