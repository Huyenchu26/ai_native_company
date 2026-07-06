# KB — Creative Framework (SOP-GRW-005)

Tài liệu nền tảng để tạo ad creative cho DAKOfits (AOP leggings/activewear đa-niche, FB Ads, US + EU). Creative = đòn bẩy ROAS lớn nhất khi audience bão hòa.

---

## 1. Công thức Hook → Body → CTA

### Hook 0–3s (thumb-stop)
- Quyết định ~80% retention. Mục tiêu: dừng ngón cái scroll trong 3 giây đầu.
- **Pattern-interrupt visual:** mẫu AOP nổi bật, chuyển động bất ngờ, zoom mẫu in.
- **Text hook (góc niche):**
  - Identity: "POV: your leggings match your [breed/niche]"
  - Social proof: "These [breed] leggings sold out 3×"
  - Curiosity: "The leggings every [niche] mom is obsessed with"
  - Gift: "The perfect gift for any [breed] lover"
- **TRÁNH:** claim sức khỏe, before/after cơ thể, từ ngữ gây sốc (Meta cấm).

### Body 360° (show-off all-over-print)
- **360° rotation:** quay/mockup legging nhiều góc → khoe AOP không bị cắt mẫu (USP của all-over-print).
- **Close-up:** chất vải, độ co giãn, đường may.
- **Lifestyle:** đang tập / đi dạo chó / yoga.
- **Social proof:** review thật, "X sold", rating.

### CTA
- **1 CTA/creative** (tránh loãng). Rõ + urgency CÓ THẬT.
- Mẫu: "Shop your breed →", "Limited drop", "Tap to find your dog".
- Link đúng product page (không link sai variant/niche).

---

## 2. UGC Brief Template

```
NICHE / PERSONA: [vd dog-mom nuôi French Bulldog, 28–45, US]
PRODUCT:         [SP + link]
ANGLE:           [identity / gift / comfort / seasonal]

VOICEOVER SCRIPT (15–25s):
  Hook (0–3s):   [1 câu thumb-stop]
  Body:          [2–3 câu khoe AOP + cảm nhận thật]
  CTA:           [1 câu kêu gọi]

SHOT LIST:
  1. Unbox       (mở gói, reaction thật)
  2. Mặc thử     (full-body, thấy rõ mẫu)
  3. 360°        (xoay người khoe all-over-print)
  4. Close-up    (chất vải / chi tiết breed)
  5. Reaction    (mặt vui / "I love it")

DO:    quay dọc 9:16, ánh sáng tự nhiên, giọng thật, nhắc breed/niche
DON'T: nói claim sức khỏe, before/after cơ thể, dùng nhạc có bản quyền, đọc như quảng cáo
```

---

## 3. Carousel Structure
| Card | Nội dung |
|------|----------|
| Card 1 | Hook (text + mẫu AOP nổi bật) |
| Card 2–4 | Góc sản phẩm / benefit (360°, chất vải, lifestyle, social proof) |
| Card 5 | Offer + 1 CTA + link |

---

## 4. Meta Ad Policy Self-Check (GATE cứng — phải pass mới handoff)

| # | Check | Pass khi |
|---|-------|----------|
| 1 | Health / body claim | KHÔNG hứa giảm cân, "burn fat", "slim", chữa bệnh |
| 2 | Before/after cơ thể | KHÔNG so sánh cơ thể trước/sau |
| 3 | Misleading / sốc | KHÔNG phóng đại sai, không hình gây sốc, không personal attribute ("you are overweight") |
| 4 | IP / TM breed name | Tên breed/niche không vi phạm nhãn hiệu; nếu nghi ngờ → flag **05-compliance** |
| 5 | Restricted content | Không nội dung cấm/nhạy cảm theo Meta Ad Policy |
| 6 | Link & landing | Link product page đúng, không cloaking, page khớp ad |

**CẤM tuyệt đối:** health-claim & before-after (route bắt buộc qua 05-compliance nếu chạm).
Không pass bất kỳ dòng nào → `policy_self_check=false` → **REWORK**, KHÔNG handoff.

---

## 5. Quality Gate (SLI/SLO)
- Hook retention 3s ≥ 30% · Thumb-stop ratio ≥ 25%
- Policy pass rate (handoff đầu) ≥ 95%
- Variant coverage ≥ 2/SP cho ABO
- `confidence_score` ≥ 0.7 + `evidence[]` đủ + `need_review` đúng cờ
