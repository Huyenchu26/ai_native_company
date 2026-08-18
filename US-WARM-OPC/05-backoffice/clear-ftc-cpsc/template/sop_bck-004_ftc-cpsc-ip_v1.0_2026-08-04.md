# SOP-BCK-004 — FTC / CPSC / IP Compliance Sign-off (US)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 05-Backoffice · **Responsible AI:** `vibe-us-warm-bck-compliance`
**Delta vs EU:** thay GPSR bằng **CPSC + FTC + IP-US**. Đây là nơi cấp **clearance_id chính thức** (prd-design chỉ pre-check — fix EU H5).

## 1. Mục tiêu
Gác cổng pháp lý US cho sản phẩm & quảng cáo:
- **CPSC** — 16 CFR 1610 (flammability textile) + **Textile Fiber Products Identification Act** (fiber content %, country of origin, **RN number** hoặc tên công ty) + Wool Act nếu có wool.
- **FTC** — 16 CFR 255 (disclose material connection/endorsement, **no fake reviews**), Made-in-USA chỉ khi đủ điều kiện, no deceptive claim.
- **IP/TM** — cấp `clearance_id` chính thức sau USPTO check (nhận pre-check từ prd-design).

## 2. IPO/ICOM
- **Input:** product (fiber, origin), listing/creative copy, IP pre-check từ 01.
- **Control:** fiber label + RN present; flammability class OK; FTC no-deceptive/no-fake-review; USPTO clear + licensed-char 0.
- **Output:** `compliance-clearance.json` (schema `compliance-clearance.schema.json`) — cpsc_pass, ftc_pass, ip_status, clearance_id, evidence, confidence, need_review.
- **Mechanism:** USPTO TESS, CPSC guidance, FTC guides.

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | CPSC label | thiếu fiber/RN/origin → cpsc_pass=false |
| 3.2 | FTC copy | fake review / deceptive / Made-in-USA sai → ftc_pass=false |
| 3.3 | IP sign-off | USPTO clear + 0 licensed → cấp clearance_id; chưa tra → PENDING |
| 3.4 | Issue clearance | chỉ khi cả 3 pass |

## 4. RACI (fix EU H5 — quyền rõ ràng)
R: bck-compliance · A: Owner · C: prd-design (IP pre-check), mer-product-page (listing) · I: growth.
**bck-compliance là authority DUY NHẤT cấp clearance_id chính thức.** prd-design pre-check, KHÔNG tự cấp CLEAR.
HITL: mọi HIGH-risk / uncertain → Owner.

## 5. Gate (allOf/if-then)
clearance_id present ⇒ cpsc_pass=true ∧ ftc_pass=true ∧ ip_status=CLEAR. ip_status=CLEAR ⇒ uspto_checked=true ∧ licensed_char_match=0. Fail-closed: chưa tra → PENDING (không CLEAR).

## 6. Links
IP pre-check upstream: 01 [SOP-PRD-003](../../../01-product-studio/clear-ip/template/sop_prd-003_ip-tm-clearance-us_v1.0_2026-08-04.md). Listing: 02 mer-product-page.

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — US CPSC+FTC+IP; bck-compliance cấp clearance_id chính thức (fix EU H5). |
