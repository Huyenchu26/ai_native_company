# 03-growth (Growth) — Department README

**Dept code:** grw · **Layer:** L2 (Operations / Primary value chain) · **Ngày:** 2026-06-23
**OPC + AI Workforce** · **AI Workers (3):** `vibe-opc-pod-growth-fb-ads`, `vibe-opc-pod-growth-fb-creative`, `vibe-opc-pod-growth-marketing`

> Sứ mệnh: Biến **live product** thành **traffic + đơn hàng có lãi** qua Facebook Ads (100% traffic), bổ trợ bằng creative, email (Klaviyo) và organic. Đóng góp trực tiếp Company **O1** (revenue 500tr/tháng, blended ROAS ≥ 2.5).
> **GATE CỨNG: No Meta Ad Policy pass → No ads.**

---

## 1. Department IPO

| | |
|---|---|
| **Input** | Live product + product page (02-merchandising); creative angle + audience sizing (01-product-studio); ad budget + Meta Ad Policy clearance (05-backoffice); opt-in email list |
| **Process** | Creative → FB Ads (ABO→CBO) → Email/Promotions → Organic → Growth report |
| **Output** | Đơn hàng (→ 04-fulfillment-cx); ad cost + ROAS/CPA data (→ 05-backoffice); growth report (→ 00-company) |
| **Mechanism** | Meta Ads Manager, Business Manager (5-tier), CAPI/Pixel, Klaviyo, IG/TikTok/FB, 3 AI Workers |

---

## 2. Value Chain Position (L2)

```
01-product-studio ─┐
                   ├──► [02-merchandising] ──► ★ 03-GROWTH ★ ──► 04-fulfillment-cx (đơn)
                   ┘     (live product+page)    (traffic+đơn)  └─► 05-backoffice (cost/ROAS)
```
- **Upstream:** 02-merchandising (live product + page). Phụ thuộc 01 (niche/audience) gián tiếp.
- **Downstream:** 04-fulfillment-cx (nhận đơn hàng), 05-backoffice (nhận cost/ROAS data + budget governance).
- **Gate vào:** Meta Ad Policy clearance từ 05-compliance.

---

## 3. Process IPOs (từng SOP)

| SOP | Tên | Input → Output | Folder |
|-----|-----|----------------|--------|
| **GRW-001** | Organic Social & Community | product+UGC → posts/community scheduled | `post-organic/` |
| **GRW-002** | FB Ads Campaign Mgmt | product+creative+policy → campaign tối ưu + đơn | `run-fb-ads/` |
| **GRW-003** | Email & Promotions (Klaviyo) | opt-in list+offer → email sent + revenue | `send-email/` |
| **GRW-004** | Growth Report (KPI/KRI) | cross-channel data → report + alert | `report-growth/` |
| **GRW-005** | FB Ad Creative | angle+UGC → creative package | `create-creative/` |

Luồng nội bộ: **005 (creative) → 002 (ads)**; 003 + 001 bổ trợ; **004 (report)** đóng vòng feedback cho cả 3.

---

## 4. RACI (Department-level)

| Quy trình | R | A | C | I |
|-----------|---|---|---|---|
| FB Ads (002) | `fb-ads` | OPC | 05-compliance, 05-finance | 04 |
| Creative (005) | `fb-creative` | OPC | `fb-ads` | 05-compliance |
| Email (003) | `marketing` | OPC | 05-compliance (GDPR) | 05-finance |
| Organic (001) | `marketing` | OPC | 04-CX | 05-compliance |
| Report (004) | `fb-ads` | OPC | 05-finance | 00-company |

---

## 5. KPI Summary

| KPI | Target | Nguồn |
|-----|--------|-------|
| Blended ROAS | ≥ 2.5 | SOP-GRW-002/004 |
| CPA | < $20 | SOP-GRW-002 |
| Revenue do ads/tháng | đóng góp 500tr (O1) | SOP-GRW-004 |
| CTR (link) | ≥ 1.0% | SOP-GRW-002 |
| Hook retention 3s | ≥ 30% | SOP-GRW-005 |
| Email deliverability | ≥ 98% | SOP-GRW-003 |
| BM ban (sập toàn bộ) | 0 | SOP-GRW-002 |

Chi tiết: [`kpi_grw-001_growth-kpis_v1.0_2026-06-23.md`](kpi_grw-001_growth-kpis_v1.0_2026-06-23.md) · [`kri_grw-001_key-result-indicators_v1.0_2026-06-23.md`](kri_grw-001_key-result-indicators_v1.0_2026-06-23.md)

---

## 6. OKR Summary

- **Committed:** ROAS ≥ 2.5 · CPA < $20 · revenue do ads đóng góp O1 (→ Company O1).
- **Stretch (x10):** revenue do ads 5 tỷ + 100 winner SKU scale song song (need_review).
- Chi tiết: [`okr_grw-001_quarterly-okr_v1.0_2026-06-23.md`](okr_grw-001_quarterly-okr_v1.0_2026-06-23.md)

---

## 7. Quality Standards Summary

SLI/SLO mỗi SOP (ROAS, CPA, CTR, CAPI EMQ ≥ 6, BM ban rate, email deliverability, hook retention 3s) + error budget. Chi tiết: [`quality_grw-001_quality-standards_v1.0_2026-06-23.md`](quality_grw-001_quality-standards_v1.0_2026-06-23.md)

---

## 8. AI Integration (SOP → AI Worker)

> Phòng này có **3 AI Worker** (đa chuyên trách).

| SOP | AI Worker | Vai trò |
|-----|-----------|---------|
| GRW-002 FB Ads | `vibe-opc-pod-growth-fb-ads` | vận hành Meta Ads, scale/kill, CAPI verify |
| GRW-004 Report | `vibe-opc-pod-growth-fb-ads` | tổng hợp KPI/KRI, alert |
| GRW-005 Creative | `vibe-opc-pod-growth-fb-creative` | hook/body/CTA, UGC brief, carousel |
| GRW-003 Email | `vibe-opc-pod-growth-marketing` | Klaviyo flow opt-in/GDPR |
| GRW-001 Organic | `vibe-opc-pod-growth-marketing` | organic social + community seeding |

KWSR: [`_knowledge`](_knowledge/README.md) · [`_workflow`](_workflow/README.md) · [`_skills-agents`](_skills-agents/README.md) · [`_rules`](_rules/README.md)
