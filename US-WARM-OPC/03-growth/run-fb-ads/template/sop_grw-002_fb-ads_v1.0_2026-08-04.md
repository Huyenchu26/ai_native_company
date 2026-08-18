# SOP-GRW-002 — Facebook Ads (US, gift blankets)

**Version:** 1.0 · **Date:** 2026-08-04 · **Dept:** 03-Growth · **Responsible AI:** `vibe-us-warm-grw-fb-ads`
**Delta vs EU:** US/FTC (thay ad-rule EU); BE-ROAS chăn per-SKU; **1 ngưỡng KILL duy nhất** (fix EU H3 lệch 1.5/1.8).

---

## 1. Mục tiêu
Setup + vận hành FB ads cho chăn cá nhân hoá, US. Winner/scale/kill theo **BE-ROAS per-SKU** ([unit-economics](../../../_shared/unit-economics.md)), KHÔNG hard-code số cố định.

## 2. IPO / ICOM
- **Input:** live-product (từ 02 go-live), creative package (GRW-005), BE-ROAS per-SKU, budget.
- **Control:** FTC (no deceptive, disclosure); Meta ad policy; **KILL Platform ROAS < 1.8 sau 3 ngày & spend ≥ 2×CPA** (1 ngưỡng, thống nhất mọi file); scale khi blended ≥ BE-ROAS.
- **Output:** `fb-ads-plan.json` (schema `fb-ads-plan.schema.json`).
- **Mechanism:** Meta Marketing API (cần token — thiếu → plan-only, KHÔNG launch, ROAS/spend=0=no-data).

## 3. Các bước
| # | Bước | Action | Prevention |
|---|------|--------|-----------|
| 3.1 | Precheck | live-product tồn tại? creative FTC-clean? | thiếu live-product → HOLD (không chạy ads vô sản phẩm) |
| 3.2 | Setup | audience gift-shopper US, budget, BE-ROAS gate | scale gate ≥ BE-ROAS (không vào vùng lỗ) |
| 3.3 | Kill/scale | KILL < 1.8; scale ≥ BE-ROAS | **1 ngưỡng KILL duy nhất** — không mâu thuẫn orchestrator |
| 3.4 | FTC | no deceptive/fake trong ad copy | validator --prose |

## 4. RACI
R: grw-fb-ads · A: Owner · C: grw-creative, mer-catalog (BE-ROAS) · I: grw-orchestrator.
HITL: spend vượt cap; ROAS bất thường; FTC uncertain.

## 5. Quality Gate
| SLI | SLO | Check | On fail |
|-----|-----|-------|---------|
| Scale gate | blended ≥ BE-ROAS per-SKU | schema | < BE-ROAS → không scale |
| KILL | Platform ROAS < 1.8 → kill | rule | — |
| FTC clean | 0 deceptive hit | --prose | hit → block ad |

**Gate (allOf/if-then):** launch=true ⇒ live_product_ready=true ∧ ftc_clean=true. Fail-closed: thiếu Meta token → launch=false, HOLD.

## 6. Links
Upstream: 02 go-live · [creative](../../create-creative/template/sop_grw-005_gift-creative_v1.0_2026-08-04.md) · [unit-economics](../../../_shared/unit-economics.md).

## 7. History
| 1.0 | 2026-08-04 | Khởi tạo — US/FTC, BE-ROAS per-SKU, 1 ngưỡng KILL (fix EU H3). |
