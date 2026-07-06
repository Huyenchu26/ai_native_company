# Policy: Document Control

**Mã:** POLICY-SHARED-002 · **Phiên bản:** 1.0 · **Ngày:** 2026-06-23 · **Áp dụng:** toàn công ty

---

## 1. Naming convention
`[file_type]_[file-name]_v[version]_[YYYY-MM-DD].md`
file_type: charter, sop, policy, kpi, okr, kri, quality, template, report, matrix, flow, register, guide, glossary.

## 2. SOP State Machine
OPERATIONAL SOP: `template/ → input/ → processing/ → output/ → archive/`.
- `template/` READ-ONLY — không edit trực tiếp, copy sang input/ trước.
- `archive/` immutable — audit trail, tổ chức theo `[YYYY-MM]/`.

## 3. Versioning
Thay đổi nội dung SOP → bump version (v1.0 → v1.1), ghi vào Section 7 "Lịch Sử Thay Đổi".

## 4. Guardrail (v2.0)
- Edit `template/` chỉ qua SOP review cycle.
- `archive/` không edit.
- Artifact có target (OKR/SLO) phải kèm evidence + confidence_score; <0.7 → review-queue.
