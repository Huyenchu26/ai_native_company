# SOP-GRW-002 — Facebook Ads Campaign Management `[AI WORKFORCE]`

**Phòng:** 03-growth (grw) · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** 03-growth · **Responsible AI Worker:** `vibe-opc-pod-growth-fb-ads`
**Folder:** `run-fb-ads/`

> GATE CỨNG: **No Meta Ad Policy pass → No ads.** Mọi creative + landing page phải pass policy-check (xác nhận từ 05-backoffice/compliance) trước khi bật campaign.

---

## 0. IPO (Input → Process → Output)

| Thành phần | Chi tiết |
|-----------|----------|
| **Input** | Live product + product page (từ 02-merchandising); creative package (từ SOP-GRW-005); niche/targeting hint (từ 01-product-studio audience sizing); ad budget từ 05-backoffice; Meta Ad Policy clearance (từ 05-compliance) |
| **Process** | Setup BM/ad account → build campaign ABO test → đọc signal → CBO scale winner / kill loser → verify CAPI → optimize ROAS/CPA → daily/weekly report |
| **Control** | Meta Ad Policy gate, winner ≥ BE-ROAS theo SKU/market (KHÔNG hard-code 2.5), CPA<$20, scale rule +20%/2 ngày, BM 5-tier anti-ban, kill-loser rule, budget cap (test $10/ad set · scale cap $100/ngày · escalate >$150/ngày) |
| **Output** | Campaign tối ưu đang chạy + đơn hàng (→ 04-fulfillment-cx); ad cost + ROAS/CPA data (→ 05-backoffice); growth signal (→ SOP-GRW-004); **winner record → `_shared/winner-registry.json`** (→ 01-product-studio SOP-PRD-005 nhân winner) |
| **Mechanism** | Meta Ads Manager, Business Manager, CAPI (ShopBase ↔ Meta), Pixel, vibe-opc-pod-growth-fb-ads |

---

## 1. Tổng quan

Facebook Ads là **100% nguồn traffic** của DAKOfits. SOP này quản trị toàn vòng đời campaign cho catalog đa-niche (~3.200 SP), thị trường US+EU, theo mô hình **test rẻ → scale winner → cắt loser**, đồng bộ với "promote theo đợt" (SOP-MER-006). Mục tiêu: đóng góp doanh số có lãi cho Company O1 — winner phải đạt **Blended/True ROAS ≥ break-even ROAS theo SKU/market** (KHÔNG dùng một ngưỡng cứng 2.5 cho mọi niche) và **CPA < $20**.

> **Định nghĩa chuẩn (Platform vs Blended ROAS, break-even ROAS, attribution window, FX):** [unit-economics](../../../_shared/unit-economics.md) — single source of truth. Mọi con số ROAS trong SOP này tham chiếu file đó.

Nguyên tắc:
- **Test trước, scale sau:** ABO để tìm winning audience+creative, CBO để scale ngân sách.
- **Phân biệt Platform vs Blended ROAS:** đọc kill/scale real-time bằng Platform ROAS (Ads Manager, cao hơn thực 20–40%) nhưng **hiệu chỉnh về Blended/True ROAS** (ShopBase net-of-refund / tổng ad spend) trước khi commit. Ngưỡng winner đặt theo **Platform ROAS ≥ 3.0 ⇒ Blended ≈ 2.5** để bù over-attribution.
- **Winner = vượt break-even theo SKU/market:** US BE-ROAS ~2.75, EU ~5.3 (xem unit-economics §4). Không scale vào vùng dưới break-even.
- **Data-driven kill:** không cảm tính — cắt theo ngưỡng định lượng (xem §4).
- **Anti-ban là sống còn:** BM 5-tier để 1 ad account bị flag không làm sập toàn bộ.
- **Budget kỷ luật:** test $10/ad set · scale cap $100/ngày · escalate OPC+05-finance khi >$150/ngày.

---

## 2. RACI + AI Roles

| Hoạt động | R | A | C | I |
|----------|---|---|---|---|
| Build & launch campaign | `fb-ads` (AI) | OPC | `fb-creative` | 05-backoffice |
| Policy pre-check | 05-compliance | OPC | `fb-ads` | — |
| Scale / kill decision | `fb-ads` (AI) | OPC | 05-finance (budget) | — |
| Budget approval (>$150/ngày, escalate) | OPC | OPC | 05-finance | `fb-ads` |
| CAPI verify | `fb-ads` (AI) | OPC | 02-merchandising (ShopBase) | — |

**AI Role:** `vibe-opc-pod-growth-fb-ads` chịu trách nhiệm vận hành Meta Ads Manager, ra quyết định scale/kill trong khung ngưỡng; escalate cho OPC khi vượt budget cap, BM bị ban, hoặc cần creative mới.

---

## 3. Quy trình (ICOM, 5 bước)

### Bước 1 — Setup BM 5-tier anti-ban `[Input]`
| Tier | Vai trò | Mục đích |
|------|---------|---------|
| T1 — Holding BM | sở hữu trung tâm, KHÔNG chạy ads | nếu bị mất chỉ mất "vỏ" |
| T2 — Ad account chính (verified) | chạy winner đã scale | tài sản giá trị nhất, bảo vệ tối đa |
| T3 — Ad account test | chạy campaign ABO test niche mới | "vùng đệm", chịu rủi ro |
| T4 — Backup BM/account (warm) | dự phòng đã warm-up sẵn | thay thế ngay khi T2/T3 bị flag |
| T5 — Spare assets (page, pixel, domain verify dự phòng) | recovery nhanh | < 24h khôi phục |

- **C (Control):** mỗi ad account share Pixel chung qua T1; domain dakofits.com đã verify; mọi creative qua policy gate trước khi gắn vào ad.

### Bước 2 — Build ABO test (4-layer targeting) `[Process]`
- Campaign objective: **Conversions / Purchase**.
- **ABO (Ad Set Budget Optimization):** mỗi ad set 1 audience riêng, budget cố định **$10/ad set/ngày** (chuẩn test) để so sánh sòng phẳng.
- **4-layer targeting:**
  | Layer | Mô tả | Ví dụ niche |
  |-------|-------|-------------|
  | 1. Interest | sở thích Meta | "Yoga", "Running", breed/niche-specific |
  | 2. Behavior | hành vi mua | "Engaged Shoppers", "Online buyers" |
  | 3. Custom Audience | data first-party | website visitors, add-to-cart, email list (opt-in) |
  | 4. Lookalike (LAL) | mở rộng từ seed | LAL 1–3% từ purchasers / high-value CA |
- Mỗi đợt test 5–10 SP (đồng bộ SOP-MER-006), 3–5 audience × creative variant.

### Bước 3 — Verify CAPI `[Control]`
- Bật **Conversions API** song song Pixel (ShopBase ↔ Meta) để chống mất signal (iOS/ad-blocker).
- KIỂM: Events Manager → **Event Match Quality ≥ 6.0/10**, deduplication Pixel+CAPI OK (không double-count), Purchase event fire đúng giá trị.
- Nếu EMQ < 6 hoặc dedup lỗi → fix trước khi scale (signal sai → optimize sai).

### Bước 4 — Đọc signal & quyết định scale/kill `[Process]`
- Cửa sổ đánh giá: tối thiểu **3 ngày** hoặc đủ ~50 add-to-cart / ad set.
- **Attribution window chuẩn công ty: 7-day click / 1-day view** (chốt cố định để đọc nhất quán mọi ad set; xem [unit-economics](../../../_shared/unit-economics.md) §1).
- **Đọc bằng Platform ROAS (real-time) nhưng hiệu chỉnh về Blended trước khi commit scale.** Ngưỡng winner: **Platform ROAS ≥ 3.0 ⇒ Blended ≈ 2.5**; và Blended phải ≥ **break-even ROAS theo SKU/market** (US ~2.75, EU ~5.3 — KHÔNG dùng 2.5 cứng).
- **WINNER → chuyển sang CBO scale:** gom winning ad set vào CBO, scale **+20% budget mỗi 2 ngày** đến **scale cap $100/ngày**; vượt cap → escalate. LAL-expand + duplicate sang T2.
- **WINNER → ghi Winner Registry:** khi Blended đã reconcile ≥ BE-ROAS (winner ổn định), **append/update record vào [`_shared/winner-registry.json`](../../../_shared/winner-registry.json)** (sku, niche, design_type, market, blended/BE-ROAS, cpa, batch_id, `status=WINNER`, evidence[]). Đây là trigger đóng vòng cho **SOP-PRD-005** (nhân winner) phòng 01. Data khớp schema `winner-registry.schema.json`.
- **LOSER → kill:** xem §4 ngưỡng.
- **Ngân sách rủi ro tối đa/đợt test:** mỗi ad set kill trước khi spend chạm **$40** (≈ 4 ngày × $10, = 2× CPA target). Một đợt test 5–10 SP × 3–5 ad set ⇒ trần rủi ro/đợt ≈ **$40 × số ad set** (vd 6 ad set ≈ $240); OPC duyệt tổng/đợt trước khi mở batch.

### Bước 5 — Optimize & report `[Output]`
- Daily: check ROAS/CPA/CTR/frequency; refresh creative khi frequency > 2.5 hoặc CTR giảm > 30%.
- Output: campaign tối ưu → đơn về 04; cost/ROAS → 05; số liệu → SOP-GRW-004 (growth report).

---

## 4. Phân nhánh (Decision Rules)

| Điều kiện | Hành động |
|----------|-----------|
| Creative/page CHƯA pass Meta Ad Policy | **STOP** — không launch, trả về SOP-GRW-005 / 05-compliance |
| Platform ROAS ≥ 3.0 (⇒ Blended ≈ 2.5) **và** Blended ≥ BE-ROAS theo SKU/market (US ~2.75, EU ~5.3) **và** CPA < $20 sau cửa sổ test | **WINNER** → CBO scale +20%/2 ngày, cap $100/ngày; **ghi `_shared/winner-registry.json`** → trigger SOP-PRD-005 (nhân winner) |
| Platform ROAS đạt 3.0 nhưng Blended < BE-ROAS của SKU (vd EU giá thấp) | **KHÔNG scale** — đây là lãi ảo; chuyển sang nâng giá/đổi provider (xem unit-economics §4) |
| Platform ROAS ~1.8–3.0 (Blended dưới ngưỡng winner) | **OPTIMIZE** — đổi creative/audience, giữ test thêm 2 ngày |
| Platform ROAS < 1.8 sau 3 ngày & spend ≥ 2× CPA target ($40) | **KILL** (kill-loser rule) |
| CPA > $20 & 0 conversion sau spend $30 | **KILL** ngay |
| Frequency > 2.5 & CTR giảm > 30% | **REFRESH CREATIVE** (ad fatigue) |
| BM/ad account bị flag/restricted | **FAILOVER** sang T4 backup, escalate OPC, mở recovery |
| EMQ < 6 / CAPI dedup lỗi | **HOLD scale** đến khi fix signal |
| Chi tiêu chạm scale cap $100/ngày trên 1 SKU/campaign | giữ trong cap; muốn vượt → **ESCALATE** OPC + 05-finance |
| Vượt **$150/ngày** (tổng) | **ESCALATE** OPC + 05-finance trước khi tăng (hard escalate) |

---

## 5. Checklist + Quality Gate (SLI/SLO + Prevention)

> **Attribution window chuẩn để đọc mọi SLI ROAS/CPA: 7-day click / 1-day view** (cố định công ty — [unit-economics](../../../_shared/unit-economics.md) §1). Mọi số report khai báo rõ window này.

**Pre-launch checklist:**
- [ ] Meta Ad Policy clearance (creative + page) ✔
- [ ] CAPI bật, EMQ ≥ 6, dedup OK
- [ ] BM tier đúng (test → T3, scale → T2)
- [ ] Budget trong cap đã duyệt (test $10/ad set · scale cap $100/ngày · escalate >$150/ngày)
- [ ] Attribution window set 7-day click / 1-day view
- [ ] BE-ROAS của SKU/market đã tính (US ~2.75 / EU ~5.3) làm ngưỡng winner
- [ ] UTM/tracking gắn đúng product page

**Quality Gate (SLI → SLO):**
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Winner threshold (Platform ROAS, đọc real-time) | ≥ 3.0 ⇒ Blended ≈ 2.5 | dùng để gate scale |
| **Blended/True ROAS** (commit scale & report) | ≥ **BE-ROAS theo SKU/market** (US ~2.75, EU ~5.3 — KHÔNG 2.5 cứng) | ≤ 20% campaign-days dưới ngưỡng/tháng |
| CPA | < $20 | ≤ 15% ad sets vượt |
| CTR (link) | ≥ 1.0% | — |
| CAPI Event Match Quality | ≥ 6.0/10 | < 5% thời gian dưới 6 |
| BM ban rate | < 1 account/tháng & 0 lần sập toàn bộ | 0 tolerance cho "sập toàn bộ" |
| Scale discipline | tăng ≤ 20%/2 ngày, không vượt cap $100/ngày khi chưa escalate | 0 vi phạm |

**Prevention:** policy gate cứng; BM 5-tier; scale cap; CAPI verify trước scale; kill-loser tự động theo ngưỡng (chống "đốt tiền" cảm tính).

---

## 6. Tài nguyên + Links

- Folder: `run-fb-ads/` (input/processing/output/archive)
- **Định nghĩa chuẩn:** [unit-economics](../../../_shared/unit-economics.md) (Platform vs Blended ROAS, break-even ROAS, attribution window 7d-click/1d-view, FX)
- Upstream: [02-merchandising](../../../02-merchandising/README.md) (live product + page)
- Creative: [SOP-GRW-005](../../create-creative/template/sop_grw-005_fb-creative_v1.0_2026-06-23.md)
- Report: [SOP-GRW-004](../../report-growth/template/sop_grw-004_growth-report_v1.0_2026-06-23.md)
- Policy gate: 05-backoffice/compliance (Meta Ad Policy)
- Rules: [`_rules/README.md`](../../_rules/README.md) · Knowledge: [`_knowledge/README.md`](../../_knowledge/README.md)
- Tools: Meta Ads Manager, Business Manager, Events Manager (CAPI), Pixel

---

## 7. Lịch sử

| Version | Ngày | Thay đổi | Người |
|---------|------|----------|-------|
| v1.0 | 2026-06-23 | Khởi tạo SOP FB Ads (ABO→CBO, 4-layer, CAPI, BM 5-tier) | Company Architect |
| v1.1 | 2026-06-23 | Tách Platform vs Blended ROAS; winner ≥ BE-ROAS theo SKU/market (US ~2.75/EU ~5.3, bỏ 2.5 cứng); budget cap test $10/scale $100/escalate $150; attribution 7d-click/1d-view; trỏ unit-economics; ngân sách rủi ro/đợt | 03-growth |
| v1.2 | 2026-07-04 | Khép vòng winner: WINNER ổn định → ghi `_shared/winner-registry.json` → trigger SOP-PRD-005 (nhân winner) phòng 01 | 03-growth |
