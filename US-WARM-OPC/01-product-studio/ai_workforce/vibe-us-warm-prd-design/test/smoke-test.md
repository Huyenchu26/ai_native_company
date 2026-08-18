# Smoke Test — vibe-us-warm-prd-design

Xác minh pipeline design (SOP-PRD-002) + IP pre-check (SOP-PRD-003) và **gate cứng fail-closed**. Validator: `_shared/script/validator.py`. Vocabulary: **CLEAR / MODIFY / REJECT / PENDING** (KHÔNG "PASS").

Đặt biến cho gọn:
```bash
SK=/home/huyenctn/ai_native_company/US-WARM-OPC/01-product-studio/ai_workforce/vibe-us-warm-prd-design
V=/home/huyenctn/ai_native_company/US-WARM-OPC/_shared/script/validator.py
```

## (a) Validate skill.json theo skill-meta schema
```bash
python3 "$V" --artifact "$SK/skill.json" --schema /home/huyenctn/ai_native_company/US-WARM-OPC/_shared/schema/skill-meta.schema.json
```
Kỳ vọng: `ok: true`. (quality_gates dùng `name`+`min_confidence`, name khớp pattern `^vibe-us-warm-...`.)

## (b) Design output HỢP LỆ + --run-all
```bash
python3 "$V" --run-all --artifact "$SK/synthetic-data/sample-design-output.json" --schema "$SK/schema/design-spec.schema.json"
```
Kỳ vọng: `ok: true`, `schema.ok: true`, evidence verified (không missing), `adjusted_confidence ≥ 0.7`.
IP output hợp lệ:
```bash
python3 "$V" --run-all --artifact "$SK/synthetic-data/sample-ip-clearance-output.json" --schema "$SK/schema/ip-clearance.schema.json"
```

## (c) GATE design: handoff_ready=true nhưng ip_status=PENDING → FAIL
```bash
python3 "$V" --artifact "$SK/synthetic-data/test-fail-design-gate.json" --schema "$SK/schema/design-spec.schema.json"
```
Kỳ vọng: `ok: false` — lỗi `ip_status: 'PENDING' ... 'CLEAR' was expected` (gate1 enforce).

## (d) GATE IP: status=CLEAR nhưng uspto_checked=false → FAIL
```bash
python3 "$V" --artifact "$SK/synthetic-data/test-fail-ip-gate.json" --schema "$SK/schema/ip-clearance.schema.json"
```
Kỳ vọng: `ok: false` — lỗi `uspto_checked: False ... True was expected`.

## (e) Link resolve (no off-by-one)
`skill.json $schema` = `../../../_shared/schema/skill-meta.schema.json` phải resolve tới file thật (3 cấp tới `_shared`, KHÔNG 4). SKILL.md links SOP-PRD-002/003 resolve tới `../../design-personalization|clear-ip/template/...` (2 cấp — cùng dưới 01-product-studio).

## Negative bổ sung
- Design `material_gsm=250` + `design_status=CLEAR` → FAIL gate2 (no under-spec).
- Design `min_dpi=120` + `design_status=CLEAR` → FAIL gate2 (no upscale).
- IP `licensed_char_match=2` + `status=CLEAR` → FAIL (phải REJECT).
- Confidence 0.6 + `need_review=false` → FAIL gate3.

## Kết quả mong đợi
(a)(b) PASS · (c)(d) FAIL đúng như thiết kế → gate enforce, vocabulary CLEAR nhất quán, không có nhánh upscale.
