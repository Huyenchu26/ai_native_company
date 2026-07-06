# Synthetic Input — Sample Page (EU, clearance PASS)

Input mẫu để chạy `prompt/write-page-prompt.md` và `test/smoke-test.md` bước 1.

```yaml
sku: DKF-LEG-HUSKY-001
design_id: DSGN-HUSKY-AOP-tile-2026
niche: dog-breed Siberian Husky (dog-mom)
market: EU
gpsr_clearance_id: BCK004-CLR-2026-0617-HUSKY
gpsr_clearance_status_expected: PASS   # verify từ SOP-BCK-004, status=PASS cho đúng sku/design
responsible_person: "DAKOfits EU Rep — Maes Compliance BV, Kerkstraat 12, 1000 Brussel, Belgium"
sports_bra_sku: DKF-BRA-HUSKY-001       # cùng AOP niche → bundle
review_pool:
  rating: 4.8
  snippets:
    - "Print is vivid front and back — true 360° all-over. My Husky-mom heart is full!"
    - "Soft, squat-proof, fits true to size. Ordered XL, perfect."
  ugc_refs:
    - "IG @husky.mom.fit reel 2026-06"
brand_voice: "DAKOfits — benefit-driven, mobile-first, đáng tin"
```

## Cleared design info
- AOP tile pattern, Siberian Husky, 360° all-over-print, print-ready 300 DPI (đã QC phòng 01).
- Variant size XS–3XL, color: charcoal / navy (blueprint từ vibe-eu-opc-mer-catalog / MER-002).

## GPSR clearance (từ SOP-BCK-004)
- Log ID: `BCK004-CLR-2026-0617-HUSKY` · status: **PASS** · breed IP/TM cleared.
- Responsible Person (EU) như trên · safety warning + care/material kèm theo.

## Kỳ vọng output
PDP publish-ready (EN): headline benefit + Husky niche, 5 bullet, story 360° AOP, size guide XS–3XL, bundle leggings+sports-bra, social proof 4.8★, **GPSR label block** (Responsible Person EU). `gpsr_label_present=true`, `confidence_score≥0.7`, `need_review=false`, `evidence[]` gồm clearance log ID + design ID + SKU + review source.
```
