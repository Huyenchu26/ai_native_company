# DAKOfits — AI Workforce Audit Scorecard (2026-06-25)

Rà soát 18 skill / 5 phòng theo rubric 8 chiều (cấu trúc · frontmatter+SOP · anti-hallucination · gate cứng · Actuator · link resolve · schema+test · handoff).

## Kết quả tổng (sau khi fix P1 + P3 — 2026-06-25)
| Verdict | Trước fix | Sau fix |
|---------|-----------|---------|
| ✅ ĐẠT | 11 | **12** |
| 🟡 THIẾU-NHỎ | 7 | **6** (chỉ còn gap P2 = thiếu Actuator, theo chủ ý) |
| ❌ CHƯA-ĐẠT | 0 | 0 |

### Fix log (P1 + P3 đã hoàn tất)
- ✅ **mer-visual → ĐẠT:** sửa link SOP-MER-005 v1.0→v1.1; tạo lại `_shared/mockup-style-guide.md` (REF-VISUAL-001); link husky sample → pickleball validation.
- ✅ **Namespace nhất quán:** bỏ hết nhãn legacy `vibe-opc-pod-*` trong mer-product-page, mer-orchestrator, grw-orchestrator (+ sửa 1 path grw-orchestrator trỏ đúng mer-catalog SKILL.md).
- ✅ **ful-cx:** thêm `version: "1.0"` + mục Links (3 schema + 2 test).
- ➖ **Không phải lỗi:** prd-design phase `generate-design` không gắn schema là ĐÚNG (xuất file ảnh, không phải JSON). "15 vs 16 file" PRD chỉ là thiếu 1 prompt/seed asset — cosmetic, không sửa (tránh tạo file thừa).
- Đã sync 5 SKILL.md đã sửa sang `~/.claude/skills`.

### Còn lại (P2 — chờ quyết định, KHÔNG phải lỗi)
6 skill THIẾU-NHỎ duy nhất vì **chưa có section Actuator**: ful-order-ops, ful-cx, ful-orchestrator, bck-finance, bck-ops-hr, bck-orchestrator. Đúng chủ ý (fulfillment thủ công, support chưa tự động). Thêm Actuator khi muốn tự động hóa các phòng này.

| Phòng | Skill | Verdict |
|-------|-------|---------|
| 01 PRD | niche-research · design · orchestrator | ✅ ĐẠT (×3) |
| 02 MER | catalog · product-page · orchestrator | ✅ ĐẠT (×3) |
| 02 MER | **visual** | 🟡 THIẾU-NHỎ (3 link gãy) |
| 03 GRW | creative · fb-ads · marketing · orchestrator | ✅ ĐẠT (×4) |
| 04 FUL | order-ops · cx · orchestrator | 🟡 THIẾU-NHỎ (×3 — thiếu Actuator) |
| 05 BCK | compliance | ✅ ĐẠT |
| 05 BCK | finance · ops-hr · orchestrator | 🟡 THIẾU-NHỎ (×3 — thiếu Actuator) |

## Gap theo mức ưu tiên

### P1 — Hỏng thật (cần fix): mer-visual
- Link SOP-MER-005 trỏ `..._v1.0_2026-06-23.md` nhưng file thật là **v1.1_2026-06-25** → sửa link.
- `_shared/mockup-style-guide.md` (REF-VISUAL-001, style guide canonical) **KHÔNG tồn tại** (mất khi reset) — đây là **dependency lõi QC**, cần tạo lại.
- Link husky sample đã bị thay bằng pickleball → đổi/bỏ link.

### P2 — Quyết định (không phải lỗi): 6 skill thiếu section Actuator
Fulfillment (3) + finance/ops-hr/bck-orchestrator (3) chưa có section "🤖 Tự động hóa".
→ Đúng chủ ý: fulfillment để thủ công, support chưa chuyển actuator. Chỉ thêm khi muốn tự động hóa các phòng này.

### P3 — Cosmetic / nhất quán
- Nhãn legacy `vibe-opc-pod-*` còn trong vài link (mer-product-page → compliance; mer-orchestrator + grw-orchestrator upstream) → đổi sang `vibe-eu-opc-*`.
- ful-cx: frontmatter thiếu `version`; Links section thiếu ref schema/test.
- PRD ×3: đếm 15 file (vs 16) — thiếu 1 prompt/input seed; prd-design skill.json phase `generate-design` thiếu field `schema`.

## Điểm mạnh chung
- Anti-hallucination contract (evidence/confidence/need_review) đầy đủ ở **18/18** — cả SKILL.md lẫn schema `required`.
- Gate cứng encode bằng schema `if/then` (GPSR, refund>$30, IP/TM REJECT-default, VAT, BE-ROAS per-SKU) — rất chắc.
- Cấu trúc 16-file + link SOP/schema/handoff resolve gần như 100% (trừ mer-visual).
- BE-ROAS per-SKU không hard-code (chống lãi ảo) xuyên suốt.
