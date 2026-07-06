# Prompt — Tạo bộ ảnh mockup + render-prompt từ 1 design + SKU

> Dùng prompt này để chị Ảnh (`vibe-eu-opc-mer-visual`) sinh **brief + render-prompt sẵn-để-chạy** cho 1 SKU. Output là SPEC+PROMPT (không phải ảnh đã render — ảnh render bằng tool ngoài).

---

## INPUT (người dùng/orchestrator cung cấp)
- `design_ref`: link/file design AOP print-ready (từ PRD-003, anh Họa).
- `sku`: vd `DAKO-HUSKY-LEG-001`.
- `niche`: vd `Husky`.
- `is_winner`: true/false (winner → đủ 6 ảnh; thường → 3 ảnh tối thiểu).
- `lifestyle_context`: gợi ý bối cảnh niche (vd "yoga ngoài trời lúc bình minh").

## NHIỆM VỤ
1. Đọc [_shared/mockup-style-guide.md](../../../_shared/mockup-style-guide.md) + SOP-MER-005 để bám chuẩn.
2. Xác định số ảnh: `is_winner=true` → 6 ảnh (hero-front, hero-back, lifestyle, detail, size, ad); ngược lại → tối thiểu 3 (hero-front, hero-back, lifestyle).
3. Với MỖI ảnh, viết 1 render-prompt theo chuẩn đồng nhất (#F2F2F0, soft light, đúng tỷ lệ, **KEEP legging print exactly as input**).
4. Ghi rõ pipeline 2 bước: base mockup (tool nào) → AI enhance (tool nào, inpaint ngoài vùng quần).
5. Trả output đúng `schema/mockup-set.schema.json` (image array có type/ratio/prompt/tool; print_accuracy_pass/min_images_met để QC điền sau; evidence/confidence_score/need_review).

## RÀNG BUỘC (gate cứng)
- KHÔNG dùng text-to-image vẽ lại quần. Print = design thật.
- Mọi prompt AI enhance PHẢI có câu giữ print: "KEEP the legging print exactly as input (do not alter pattern)".
- Nếu thiếu `design_ref` → KHÔNG sinh prompt → ESCALATE OPC, `need_review=true`.

---

## TEMPLATE RENDER-PROMPT (điền theo SKU)

**1. hero-front (1:1) — AI on-model (Botika/Photoroom), input = base mockup:**
```
Professional e-commerce product photo of a woman wearing the leggings shown,
mid-thigh to ankle, natural athletic 3/4 front pose, soft even studio light,
clean light-grey seamless background (#F2F2F0), 1:1, sharp fabric detail,
KEEP the legging print exactly as input (do not alter pattern), photorealistic.
```

**2. hero-back (1:1):**
```
Same model and setup, back 3/4 view showing hips and back of legs,
the all-over-print continuous across seams (no break at seam),
clean #F2F2F0 background, soft light, 1:1,
KEEP the legging print exactly as input, photorealistic.
```

**3. lifestyle (4:5) — bối cảnh {{lifestyle_context}}:**
```
Lifestyle photo, woman {{lifestyle_context}} wearing the leggings shown,
full body, warm natural light, soft bokeh background, aspirational mood, 4:5,
KEEP legging print unchanged, photorealistic.
```

**4. detail (1:1):**
```
Macro close-up of the legging fabric at waistband and thigh, showing texture
and crisp {{niche}} all-over-print detail, soft light, #F2F2F0, 1:1,
print exactly as input, photorealistic.
```

**5. size (1:1):**
```
Two models of different body sizes (XS–3XL range) wearing the same leggings,
neutral pose, clean #F2F2F0 background, optional size-chart overlay,
1:1, KEEP print exactly as input, photorealistic.
```

**6. ad (4:5) — scroll-stopper (→ chị Ý):**
```
Bold scroll-stopping fashion shot, dynamic pose, high contrast,
small top-corner text "{{niche}} ❤️", thumb-stopping for Facebook feed, 4:5,
KEEP legging print exactly as input.
```

## OUTPUT mẫu (rút gọn)
```json
{
  "sku": "DAKO-HUSKY-LEG-001",
  "niche": "Husky",
  "images": [
    {"type": "hero-front", "ratio": "1:1", "prompt": "...", "tool": "Botika"},
    {"type": "hero-back", "ratio": "1:1", "prompt": "...", "tool": "Botika"},
    {"type": "lifestyle", "ratio": "4:5", "prompt": "...", "tool": "Photoroom"}
  ],
  "print_accuracy_pass": null,
  "min_images_met": true,
  "evidence": ["design_ref: <link PRD-003>"],
  "confidence_score": 0.8,
  "need_review": false
}
```
