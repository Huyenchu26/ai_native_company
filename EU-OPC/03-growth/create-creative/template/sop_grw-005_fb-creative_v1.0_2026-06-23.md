# SOP-GRW-005 — Facebook Ad Creative Production `[AI WORKFORCE]`

**Phòng:** 03-growth (grw) · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** 03-growth · **Responsible AI Worker:** `vibe-opc-pod-growth-fb-creative`
**Folder:** `create-creative/`

> GATE: Mọi creative phải đạt **Meta Ad Policy** (no shock/before-after sai lệch, no IP vi phạm) trước khi bàn giao cho SOP-GRW-002.

---

## 0. IPO

| Thành phần | Chi tiết |
|-----------|----------|
| **Input** | Live product + page (02-merchandising); validated niche + angle (01-product-studio); UGC raw / mockup AOP 360°; winner signal cần refresh (từ SOP-GRW-002) |
| **Process** | Chọn angle → viết hook 0–3s → body 360° → CTA → UGC brief / carousel → policy self-check |
| **Control** | Hook retention chuẩn, Meta Ad Policy, brand voice, AOP show-off 360° |
| **Output** | Creative package (image/video/carousel + script + UGC brief) sẵn cho FB Ads |
| **Mechanism** | Canva / video tool, mockup generator, vibe-opc-pod-growth-fb-creative |

---

## 1. Tổng quan

Creative là đòn bẩy lớn nhất của ROAS trên FB (audience đã bão hòa → creative quyết định thắng/thua). SOP này sản xuất creative theo công thức **Hook → Body → CTA** chuyên cho AOP leggings/activewear đa-niche, nhấn mạnh **show-off pattern 360°** (điểm bán đặc thù của all-over-print). Cung cấp đủ variant cho ABO test (SOP-GRW-002).

---

## 2. RACI + AI Roles

| Hoạt động | R | A | C | I |
|----------|---|---|---|---|
| Viết script (hook/body/CTA) | `fb-creative` (AI) | OPC | `fb-ads` (angle/data) | — |
| UGC brief & seeding spec | `fb-creative` (AI) | OPC | `marketing` (organic) | — |
| Carousel copy | `fb-creative` (AI) | OPC | 02 (product info) | — |
| Policy self-check | `fb-creative` (AI) | OPC | 05-compliance | — |
| Approve & handoff | OPC | OPC | `fb-ads` | — |

**AI Role:** `vibe-opc-pod-growth-fb-creative` tạo creative package; nhận feedback ROAS/CTR từ `fb-ads` để iterate; flag IP/breed nhạy cảm về 05-compliance.

---

## 3. Quy trình (ICOM, 4 bước)

### Bước 1 — Chọn angle theo niche `[Input]`
- Lấy angle từ niche research: identity ("for [breed/hobby] lovers"), gift, comfort/performance, seasonal.
- 1 SP → 2–3 angle để test.

### Bước 2 — Viết Hook 0–3s `[Process]`
- Mục tiêu: **thumb-stop** trong 3 giây đầu (quyết định 80% retention).
- Pattern: pattern-interrupt visual (mẫu AOP nổi bật) + text hook ("POV: your leggings match your [niche]" / "These [breed] leggings sold out 3×").
- Tránh: claim sai, before/after cơ thể (Meta cấm).

### Bước 3 — Body 360° + CTA `[Process]`
- **Body (show-off 360°):** quay/mockup legging từ nhiều góc để khoe all-over-print không bị cắt mẫu; close-up chất vải; lifestyle (đang tập/đi dạo); social proof (review, "X sold").
- **CTA:** rõ + urgency có thật ("Shop your breed", "Limited drop", link product page). 1 CTA/creative.

### Bước 4 — UGC brief / Carousel + policy self-check `[Control]`
- **UGC brief:** persona (dog-mom/niche), script thoại, shot list (unbox, mặc thử, 360°, reaction), do/don't.
- **Carousel:** card1 hook → card2–4 góc sản phẩm/benefit → card5 offer+CTA.
- **Self-check:** đối chiếu Meta Ad Policy (health/body, IP breed name, misleading) → pass mới handoff.

---

## 4. Phân nhánh

| Điều kiện | Hành động |
|----------|-----------|
| Creative đụng Meta policy (body/claim/IP) | **REWORK** trước handoff |
| Tên breed/niche có rủi ro IP/TM | flag → 05-compliance trước khi dùng |
| `fb-ads` báo CTR < 1% / hook retention 3s thấp | **NEW HOOK** variant |
| Frequency cao (ad fatigue) | sản xuất batch refresh |
| Winner cần scale | tạo thêm variant cùng angle để tránh fatigue khi scale |

---

## 5. Checklist + Quality Gate (SLI/SLO + Prevention)

- [ ] Hook 0–3s rõ, pattern-interrupt
- [ ] Body khoe AOP 360°
- [ ] 1 CTA, link đúng product page
- [ ] Meta Ad Policy self-check pass
- [ ] ≥ 2 variant/SP cho ABO

| SLI | SLO | Error budget |
|-----|-----|--------------|
| Hook retention 3s (3-sec video view rate) | ≥ 30% | ≤ 25% creative dưới ngưỡng |
| Thumb-stop ratio | ≥ 25% | — |
| Policy pass rate (lần handoff đầu) | ≥ 95% | ≤ 5% phải rework |
| Variant coverage/SP | ≥ 2 | 0 vi phạm |

**Prevention:** policy self-check bắt buộc; thư viện hook winner tái dùng; theo dõi fatigue để refresh trước khi CTR sụp.

---

## 6. Tài nguyên + Links
- Folder: `create-creative/`
- Downstream: [SOP-GRW-002 FB Ads](../../run-fb-ads/template/sop_grw-002_fb-ads_v1.0_2026-06-23.md)
- Organic seeding: [SOP-GRW-001](../../post-organic/template/sop_grw-001_organic-social_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

---

## 7. Lịch sử
| Version | Ngày | Thay đổi | Người |
|---------|------|----------|-------|
| v1.0 | 2026-06-23 | Khởi tạo SOP creative (hook/body/CTA + UGC brief) | Company Architect |
