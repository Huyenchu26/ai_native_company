# Synthetic Data — Sample Validated Niche Input

Mẫu input (1 validated niche từ PRD-001) cho skill `vibe-us-warm-prd-design`. Dùng cho smoke-test.

## Validated niche record
```json
{
  "niche": "pet-memorial",
  "category": "gift-memorial",
  "market": "US",
  "validation": {
    "demand_score": 0.79,
    "trend": "stable-up",
    "validated_by": "vibe-us-warm-prd-niche-research",
    "validated_at": "2026-08-10T09:00:00Z"
  },
  "ip_pre_flag": "LOW",
  "intent": "tưởng niệm thú cưng đã mất / gift",
  "personalization_fields": ["name", "photo", "message"],
  "supplier_print_spec": {
    "product": "fleece blanket 50x60in",
    "material_options": [
      {"type": "fleece", "gsm": 300},
      {"type": "sherpa", "gsm": 280}
    ],
    "min_dpi_at_print_size": 150,
    "print_area": "front full"
  },
  "phrase_on_base": "Always in our hearts"
}
```

## Ghi chú dùng test
- `ip_pre_flag = LOW` + phrase generic "Always in our hearts" → kỳ vọng IP đi tới **CLEAR** sau khi USPTO tra sạch VÀ có `clearance_id` từ bck-compliance.
- Material fleece 300 GSM ≥ 260 → pass no-under-spec. Nếu chọn vải < 260 → phải đổi vải (KHÔNG hạ ngưỡng).
- Ảnh khách phải ≥ 150 DPI tại 50x60in. Ảnh < ngưỡng → REJECT/re-source (KHÔNG upscale).
- Test gate fail-closed: đặt `handoff_ready=true` khi `ip_status=PENDING` → schema FAIL (xem `test-fail-design-gate.json`). Đặt IP `status=CLEAR` khi `uspto_checked=false` → schema FAIL (xem `test-fail-ip-gate.json`).
