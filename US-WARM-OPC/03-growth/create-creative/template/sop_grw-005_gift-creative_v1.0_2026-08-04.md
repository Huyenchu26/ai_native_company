# SOP-GRW-005 — Gift Creative (US blankets)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 03-Growth · **Responsible AI:** `vibe-us-warm-grw-creative`
**Delta vs EU:** angle **gift-emotional** (occasion/relationship/memorial), không niche-AOP; US/FTC + IP claim (™) check.

## 1. Mục tiêu
Tạo ad creative (script/storyboard/copy) bán **cảm xúc quà tặng**: "to my daughter", pet-memorial, Christmas gift. Không bịa asset nếu chưa render.

## 2. IPO
- **Input:** design + preview (personalization), niche gift-angle, live-product.
- **Control:** FTC no-deceptive/no-fake-review; no unverified ™; emotional nhưng trung thực (material spec đúng).
- **Output:** `creative-package.json` (schema `creative-package.schema.json`) — hooks, script, angles, policy_self_check, asset_status.
- **Mechanism:** render/video tool (cần auth) — thiếu → script-only, asset_status=not-generated.

## 3. Bước
| # | Action | Prevention |
|---|--------|-----------|
| 3.1 | Angle (occasion/relationship/memorial) | phù hợp niche + material honesty |
| 3.2 | Hook + script + copy | no deceptive, no ™ chưa sở hữu (--prose) |
| 3.3 | Asset | có tool → render; không → not-generated (không bịa) |
| 3.4 | Self-check FTC/IP | prose-scan; ™/claim → route bck-compliance |

## 4. RACI
R: grw-creative · A: Owner · C: grw-fb-ads (angle), mer-visual (preview reuse), bck-compliance (IP) · I: grw-marketing.

## 5. Gate
launch-ready creative ⇒ policy_self_check=true (FTC clean, no unverified ™). Fail-closed: asset chưa render → asset_status=not-generated, không khai có.

## 6. Links
Downstream: [fb-ads](../../run-fb-ads/template/sop_grw-002_fb-ads_v1.0_2026-08-04.md). Upstream: 02 preview/listing.

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — gift-emotional angle, US/FTC, no-phantom-asset. |
