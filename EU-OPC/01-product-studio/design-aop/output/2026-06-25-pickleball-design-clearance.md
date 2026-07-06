# AOP Design + IP/TM Clearance — Pickleball Leggings (US validation)

> SKU: DAKO-PICKLE-LEG-001 · Niche: Pickleball (score 88) · SOP-PRD-003 + PRD-004
> Style: **tile (seamless)** · Market: US · Phase: validation
> Handoff → vibe-eu-opc-mer-orchestrator KHI status = PASS

---

## PHASE 1 — Design Spec (SOP-PRD-003)

### Canvas / print-area
| Field | Value |
|-------|-------|
| Style | tile — seamless repeat |
| DPI | 300 (lock tại print size, KHÔNG upscale từ nhỏ) |
| Target px | **≥ 4000×4000 px** cho tile repeat unit · ⚠️ canvas cuối phải khớp `getBlueprintPrintArea(AOP legging blueprint)` Printify US — **cần xác nhận px thật từ Printify API trước khi xuất file production** |
| Color profile | sRGB (Printify AOP) |
| Bleed | theo spec provider (legging có vùng seam/crotch — repeat phải liền mạch khắp) |

### Motif (IP-safe — generic pickleball)
- Paddle silhouette **generic** (KHÔNG copy hình dáng/branding paddle thương mại Selkirk/JOOLA/CRBN).
- Pickleball (quả bóng lỗ) — generic.
- Court line / "kitchen" (non-volley zone) line motif — generic.
- Optional micro-text "dink · drive · rally" (từ chung môn thể thao, KHÔNG slogan TM).
- Palette gợi ý: court teal/blue + ball neon yellow + white line trên nền than/navy (tương phản cao, hợp activewear, ăn ảnh FB Ads).

### Render-prompt (tiling engine — Leonardo Tiling / SDXL-tiling, KHÔNG Midjourney)
```
seamless repeating tile pattern, pickleball sport theme, generic paddles, perforated
pickleball balls, court lines and kitchen-zone marks, hand-drawn flat vector style,
high contrast, teal + neon yellow + white on deep navy background, balanced density,
tileable edges, no logos, no brand names, no text watermark, athletic apparel print,
300 dpi, vivid, clean --tiling
```
> Sau render: upscale Real-ESRGAN/Topaz lên ≥4000px → đặt vào canvas print-area Printify.

---

## PHASE 2 — QC 360° (Quality Gate)
| Check | Trạng thái | Ghi chú |
|-------|-----------|---------|
| DPI ≥ 300 | ⏳ verify khi có file render | spec đã lock 300 |
| Seamless tile (ghép 2×2 no seam ≥98%) | ⏳ auto-QC sau render | tile style bắt buộc seamless |
| Seam / crotch / waistband align khi wrap 360° | ⏳ verify trên mockup | density đều → giảm rủi ro lệch crotch |
| Bleed + canvas khớp print-area px thật | ⚠️ **BLOCKER** | cần Printify blueprint print-area px (chưa cắm API) |
| Đúng 1/4 style chuẩn (tile) | ✅ | |
| Mockup XS–3XL render | ⏳ → bàn giao mer-visual | |

→ **QC status: PENDING-RENDER** — spec đạt chuẩn; cần render file thật + xác nhận px Printify để đóng QC.

---

## PHASE 3 — IP/TM CLEARANCE (SOP-PRD-004) — GATE

| Term / element | Lookup | Kết quả | Rubric |
|----------------|--------|---------|--------|
| "pickleball" (từ chung môn thể thao) | USPTO TESS | Generic/descriptive cho apparel — không độc quyền bởi 1 bên | **PASS** |
| USA Pickleball (logo/wordmark giải) | blocklist | TM của governing body | **AVOID** — không dùng logo/tên giải |
| PPA Tour | blocklist | TM giải đấu | **AVOID** |
| Selkirk / JOOLA / CRBN (brand paddle) | blocklist | TM thương mại — paddle shape/logo có thể protected | **AVOID** — dùng paddle generic |
| Court line / ball / "dink/rally" | USPTO | Generic descriptive | **PASS** |

> ⚠️ Dual-market note: clearance chính thức cần **cả USPTO + EUIPO** + cấp bởi **bck-compliance** (gate công ty). Đây là US validation → check US-side; nếu mở rộng EU phải EUIPO + GPSR trước khi publish EU.

### Clearance decision
- **Status: PASS (CLEAR) — CÓ ĐIỀU KIỆN** ✅
- Điều kiện bắt buộc giữ PASS:
  1. Design dùng motif **generic** — KHÔNG render logo giải (USA Pickleball/PPA) hay branding/shape paddle thương mại.
  2. KHÔNG micro-text trùng slogan/wordmark đã TM.
  3. Trước publish chính thức (ngoài validation) → **bck-compliance cấp clearance log ID** dual-market.

---

## PHASE 4 — Handoff Merch
- `handoff_ready`: **PARTIAL** — IP gate PASS (conditional), nhưng **file print-ready chưa render + px Printify chưa confirm**.
- Bàn giao: spec + render-prompt + IP-clearance (conditional PASS) → **mer-orchestrator** để: (a) tạo Printify product → lấy print-area px thật → feed ngược render đúng canvas; (b) mer-visual render mockup; (c) publish ShopBase.

---

## Gate summary (cho GPS)
| Gate công ty | Trạng thái |
|---|---|
| No IP/TM → no listing | ✅ PASS (conditional, US validation) — full clearance ID từ bck-compliance khi publish thật |
| File AOP print-ready 300 DPI | ⏳ spec sẵn, **chưa render file thật** |
| Printify print-area px | ⚠️ cần cắm Printify API / blueprint để khớp canvas |

---

**evidence[]:**
- Niche + IP risk LOW-MED, tránh logo giải/brand paddle: `01-product-studio/research-niche/output/2026-06-24-niche-research-live.json`
- IP rubric generic-descriptive: SOP-PRD-004
- Printify print-area requirement: SOP-PRD-003 (px thật cần API)

**confidence_score:** 0.72
**need_review:** true — (1) IP clearance chính thức phải do **bck-compliance** cấp log ID dual-market trước khi publish ngoài validation; (2) **file print-ready chưa render** + canvas px Printify chưa xác nhận (cần API token) — đây là 2 việc thật còn lại để unblock fulfillment.
