# Synthetic Data — Sample Validated Niche Input

Mẫu input (1 validated niche từ PRD-001) cho skill `vibe-eu-opc-prd-design`. Dùng cho smoke-test.

## Validated niche record
```json
{
  "niche": "Border Collie",
  "category": "dog-breed",
  "market": ["US", "EU"],
  "validation": {
    "demand_score": 0.82,
    "fb_audience_size": 2400000,
    "competitor_ad_count": 18,
    "trend": "stable-up",
    "validated_by": "vibe-eu-opc-prd-niche-research",
    "validated_at": "2026-06-22T09:00:00Z"
  },
  "ip_pre_flag": "LOW",
  "intent": "dog-mom gift / breed pride",
  "suggested_styles": ["tile", "watercolor"],
  "provider": "printify-eu",
  "provider_template": {
    "product": "AOP legging",
    "canvas_px": "4500x5400",
    "dpi": 300,
    "bleed_px": 75,
    "color_profile": "sRGB"
  },
  "season_window": "year-round"
}
```

## Ghi chú dùng test
- `ip_pre_flag = LOW` → kỳ vọng clearance đi tới **PASS** sau dual lookup sạch (USPTO + EUIPO).
- Để test **gate fail-closed**: đổi `niche` thành term dính TM (vd tên club/brand có live trademark) hoặc đổi `ip_pre_flag = HIGH` → kỳ vọng **REJECT/MODIFY**, `handoff_ready` không bật, đẩy `human-review/`.
- `provider_template.canvas_px` + `bleed_px` dùng để kiểm bleed/canvas px ở QC 360°.
