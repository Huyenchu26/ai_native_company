# SOP-PRD-003 — IP / TM Clearance (US market)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 01-Product Studio · **Responsible AI:** `vibe-us-warm-prd-design` (pre-check) → `vibe-us-warm-bck-compliance` (official sign-off)
**Scope:** US only (single-market — KHÔNG dual-market như EU model). Gate cứng, error budget = 0.

---

## 1. Tổng quan & Mục tiêu
Chăn cá nhân hoá có rủi ro IP đặc thù khác AOP:
- **Tên/quote** khách nhập có thể trùng nhãn hiệu đã đăng ký (vd slogan TM).
- **Ảnh khách upload** → rủi ro bản quyền ảnh / hình người nổi tiếng / nhân vật licensed (Disney...).
- **Design nền** dùng phrase/character licensed.

Mục tiêu: xuất `ip-clearance.json` với status rõ ràng, **fail-closed**. US chỉ cần **USPTO (TESS)** + common-law + platform policy — KHÔNG cần EUIPO.

## 2. IPO / ICOM
- **Input:** design phrase/artwork, personalization fields cho phép, ảnh khách policy.
- **Control:** USPTO TESS check; licensed-character blocklist; celebrity likeness/right-of-publicity; photo-rights consent (khách xác nhận sở hữu ảnh).
- **Output:** `ip-clearance.json` (schema `ip-clearance.schema.json`), status enum `CLEAR / MODIFY / REJECT / PENDING`.
- **Mechanism:** USPTO TESS, licensed-IP blocklist, platform (Meta/Etsy) prohibited list.

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Phrase/TM | Tra USPTO TESS cho slogan/phrase trên design nền | Không tra được → status=PENDING (KHÔNG mặc định CLEAR) |
| 3.2 | Licensed character | Đối chiếu blocklist (Disney/sports/brands) | Match → REJECT ngay |
| 3.3 | Celebrity/likeness | Right-of-publicity (US theo bang) cho ảnh/tên người nổi tiếng | Uncertain → Owner |
| 3.4 | Customer photo rights | Policy: khách xác nhận sở hữu/được phép dùng ảnh | Không có consent field → block personalization ảnh |
| 3.5 | Sign-off | bck-compliance cấp clearance ID chính thức | prd-design chỉ pre-check; official = compliance |

## 4. RACI
- **R (pre-check):** `vibe-us-warm-prd-design` · **R (official):** `vibe-us-warm-bck-compliance` · **A:** Owner · **I:** merchandising.
- **Ownership rõ ràng (tránh lỗi H5 model cũ):** prd-design PRE-CHECK → bck-compliance KÝ clearance chính thức (cấp `clearance_id`). Chỉ `clearance_id` mới cho phép handoff design → merch.
- **HITL:** mọi HIGH-risk/uncertain → Owner.

## 5. Quality Gate (SLI → SLO)
| # | SLI | SLO | Check | On fail |
|---|-----|-----|-------|---------|
| 1 | USPTO checked | true trước khi CLEAR | validator gate | false → PENDING (không CLEAR) |
| 2 | Licensed-char match | 0 | blocklist | >0 → REJECT |
| 3 | Photo consent | present nếu có ảnh khách | field check | thiếu → block ảnh |
| 4 | Official clearance_id | present để handoff | compliance sign-off | thiếu → handoff blocked |

**Gate (schema allOf/if-then):** `status=CLEAR ⇒ uspto_checked=true ∧ clearance_id present`. Fail-closed default = `REJECT`; "chưa tra được" = `PENDING` (không phải REJECT về ngữ nghĩa, nhưng cũng KHÔNG handoff).

## 6. Links
- Design: [SOP-PRD-002](../../design-personalization/template/sop_prd-002_blanket-personalization-design_v1.0_2026-08-04.md)
- Compliance sign-off: 05-backoffice ftc/ip (bck-compliance)

## 7. History
| Ver | Date | Change |
|-----|------|--------|
| 1.0 | 2026-08-04 | Khởi tạo — US single-market IP (USPTO, no EUIPO). Ownership prd-design pre-check → bck-compliance sign-off (fix H5). Enum có PENDING (fix P3). |
