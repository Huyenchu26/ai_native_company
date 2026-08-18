# DAKOfits EU-POD-OPC — Full Audit Report (2026-07-31)

> Rà soát **toàn bộ 26 SOP + 19 skill + outputs + governance** của EU-POD-OPC theo 2 tầng: (1) quét tự động cấu trúc, (2) đọc nội dung/logic từng phòng ban (5 auditor song song). Thay thế [audit-scorecard_2026-06-25](./audit-scorecard_2026-06-25.md) — xem Finding X3.

**Người thực hiện:** Claude (agentic audit) · **Ngày:** 2026-07-31 · **Chế độ:** read + auto-fix lỗi cơ học.

---

## 1. Scorecard tổng

| Phòng | SOP | Skill | Findings | C | H | M | L |
|-------|:---:|:-----:|:--------:|:-:|:-:|:-:|:-:|
| 01 Product Studio | 5 | 3 | 15 | 3 | 5 | 4 | 3 |
| 02 Merchandising | 6 | 4 | 14 | 3 | 3 | 4 | 4 |
| 03 Growth | 5 | 4 | 13 | 1 | 3 | 7 | 2 |
| 04 Fulfillment & CX | 4 | 3 | 10 | 1 | 2 | 2 | 5 |
| 05 Backoffice | 6 | 4 | 14 | 1 | 3 | 5 | 5 |
| **Tổng** | **26** | **18(+GPS)** | **66** | **9** | **16** | **22** | **19** |

**Kết luận chung:** Tầng **skill + schema + smoke-test** chất lượng cao — anti-hallucination contract (evidence/confidence/need_review) hiện diện 19/19, gate cứng encode bằng JSON Schema `if/then` (GPSR, refund>$30, IP/TM, VAT, BE-ROAS) rất chắc. **Vấn đề tập trung ở tầng governance chưa đồng bộ với tầng skill đã nâng cấp**, và ở **khâu thực thi QC output thật** (validator chưa từng chạy trên output). Không phòng nào "hỏng logic lõi"; phần lớn là **drift** giữa các tầng tài liệu.

---

## 2. Đã tự sửa (lỗi cơ học rõ ràng) ✅

| # | Sửa gì | Phạm vi | Kiểm chứng |
|---|--------|---------|-----------|
| A1 | **20 link nội bộ gãy** | 12 file (off-by-one `../` trong kb/prompt; path review-queue.md; tạo `_quality/reports/`) | Re-check: **0 link gãy** (từ 20) |
| A2 | **3 con trỏ `$schema` sai** (`../schema/`→`./schema/`) | grw/ful/bck-orchestrator skill.json | Resolve đúng file thật |
| A3 | **9 `$schema` thiếu** (bổ sung cho nhất quán) | prd-design, prd-orchestrator, mer-catalog, mer-visual, grw-fb-ads, ful-cx, bck-finance, bck-ops-hr, gps | 19/19 skill.json vẫn valid schema |

> **KHÔNG tự sửa** namespace `vibe-opc-pod-*` (dù mỗi phòng gắn CRITICAL) — xem Quyết định D1: đây là quyết định kiến trúc, không phải lỗi cơ học.

---

## 3. Phát hiện HỆ THỐNG (xuyên phòng — quan trọng nhất)

### X1 · Namespace 2 lớp drift — binding SOP→skill không khớp folder (5/5 phòng)
Mọi SOP "Responsible AI", `_skills-agents` roster, charter, README dùng tên **`vibe-opc-pod-<domain>-<role>`**; folder skill thật là **`vibe-eu-opc-<dept>-<role>`** (~75 file, >100 lần). Nhưng nhiều file ([workforce-map](./workforce-map_v1.0_2026-06-23.md), [build-plan](./build-plan_v1.0_2026-06-23.md), ops-hr SKILL) **cố ý** mô tả mô hình **roster 2 lớp**: legacy `vibe-opc-pod-*` (đã cài `~/.claude/skills/`) + EU-OPC `vibe-eu-opc-*` (ưu tiên). → **Cần Owner quyết** (D1) trước khi rename, vì gộp/giữ 2 lớp là lựa chọn kiến trúc.

### X2 · ROAS 2.5 nằm DƯỚI break-even — governance đo "có lãi" bằng ngưỡng lỗ (MER, GRW, BCK)
Tầng skill đã chuyển sang **BE-ROAS per-SKU** ([unit-economics](../_shared/unit-economics.md): GM trước ads US 36.4%→BE-ROAS ≈2.75; EU 23%→≈5.3) và tuyên bố rõ "2.5 < break-even → scale vào vùng lỗ". Nhưng tầng governance (OKR/KPI/KRI/charter/README/_knowledge của 3 phòng) **vẫn dùng ROAS≥2.5 làm target committed + gate + KRI Green**, và evidence OKR-Growth ghi "GM 45–55%" là **sai/bịa** so với 36.4%/23%. KRI early-warning mis-calibrated (vùng 2.5–2.75 báo "an toàn" khi đang lỗ). → **Rủi ro kinh tế thật**, cần Owner reconcile (D2).

### X3 · Audit-scorecard cũ (2026-06-25) không đáng tin
Scorecard cũ tuyên bố đã fix link mer-visual, dọn namespace, tạo lại mockup-style-guide. Thực tế 2026-07-31: **20 link vẫn gãy** (đã fix ở A1), **namespace legacy tràn lan**. → Fix đã bị revert (commit "remane folder" + reset) hoặc scorecard nói quá. **Báo cáo này thay thế nó.**

### X4 · Output thật không đạt schema của chính nó — validator chưa từng chạy (PRD, MER)
5 output JSON: **4/5 thiếu `evidence[]`** dù `need_review=true`; không file nào conform schema (pricing thiếu `allocated_cpa`/`vat`; mockup `type`/`ratio` ngoài enum). Nghiêm trọng nhất: **manifest mockup khai ảnh KHÔNG có trên đĩa** (yoga 0/6, pickleball thiếu size-guide) nhưng `coverage` vẫn báo OK. → QC/validator chưa chạy trên kết quả thật. Cần D5.

### X5 · Orchestrator vắng mặt trong governance roster (5/5 phòng)
Mỗi `_skills-agents/README` ghi "N worker" nhưng **bỏ skill orchestrator** đang tồn tại → coverage matrix thiếu Manager. Auto-fixable nhưng cần soạn dòng roster (D3).

### X6 · `_knowledge` (tự xưng "nguồn sự thật") dạy công thức đã bị bác (PRD, MER, GRW, BCK)
Các file `_knowledge/README.md` còn dạy `giá=cost/(1−margin)` ("margin ảo"), "ROAS≥2.5 ngưỡng vàng", profit bỏ VAT+fx — đúng thứ SOP + unit-economics đã sửa. Worker đọc KB sẽ áp nhầm. Cần đồng bộ (nằm trong D2).

---

## 4. Findings theo phòng (chi tiết)

### 01 — Product Studio (15)
- **C1** tên skill governance ≠ folder + roster thiếu orchestrator → D1/D3.
- **C2** enum clearance `PASS`(design) vs `CLEAR`(orchestrator schema, enum khoá 1 giá trị) → handoff Merch gãy tại gate G3. *Auto-fix được sau khi chốt từ khoá (D4).*
- **C3** output pickleball gắn "PASS (CLEAR)" dù chỉ tra USPTO, **chưa EUIPO** → vi phạm hard-gate G3 (dual-market, error budget 0). → D5.
- **H1** output niche-research không conform `niche-validation.schema` (dùng `score`/`audience_us` thay `demand_score`/`audience_size`; thiếu ~6 required) dù skill khai "0 lỗi schema". → D5.
- **H2** "KHÔNG upscale" non-negotiable (_rules, SOP-003) vs skill+output dùng Real-ESRGAN/Topaz upscale ≥4000px. → D4.
- **H3** SOP-001 bắt human-review sample 20% vs skill auto-pass bỏ sampling. → D4.
- **H4** IP pre-flag 3 enum khác nhau (CLEAR/FLAG/HIGH vs NONE/LOW/MEDIUM/HIGH vs "LOW-MED"). → D4.
- **H5** quyền IP/TM clearance mâu thuẫn: charter/SOP-004 nói Product Studio sở hữu gate G3 vs skills/output nói bck-compliance cấp chính thức. → D3.
- **M1–M4/L1–L3**: SLI audience đo sai (market-size US thay Meta audience US+EU); SOP-PRD-005 bỏ khỏi roster/coverage ("4/4" sai); folder input/processing/archive không tồn tại; placeholder `[AI WORKFORCE]` chưa điền ở 4 SOP header; KRI band chồng lấn (98/24); trigger-validation tên cũ.

### 02 — Merchandising (14)
- **C1** 8 file governance/SOP dùng `vibe-opc-pod-merch-*` → D1.
- **C2** ⚠️ **mâu thuẫn kinh tế lõi**: governance dùng "gross margin ≥45%" làm gate chặn + _knowledge dạy `giá=cost/(1−margin)` mà SOP-MER-003 v1.1 gọi "margin ảo" (có thể contribution âm). → D2.
- **C3** yoga-pricing thiếu `evidence[]`; 2 mockup imageset thiếu evidence + ngoài enum schema. → D5.
- **H1** ⚠️ **ảnh ma**: manifest khai 6 ảnh, đĩa có yoga 0/6 (thư mục `images-yoga/` không tồn tại), pickleball 5/6, `coverage` vẫn OK. → D5.
- **H2** winner "ROAS≥2.5" (đã bị bác) còn ở kpi/kri/quality/README. → D2.
- **H3** đếm "2 worker" (thật 4); "5/5=100%" bỏ MER-005; _workflow nói MER-005 "chưa dùng" là sai. → D3.
- **M1–M4/L1–L4**: orchestrator SKILL giữ cả gross lẫn contribution làm gate; dependency tên lệch (skill.json vs SKILL.md); `_shared/channel-config` referenced 4 nơi nhưng không tồn tại; mockup-set.schema chưa hỗ trợ validation-first; version drift header/filename MER-001/003; link review-queue (đã fix); GPSR gate confidence lệch (catalog 0.7 vs product-page 1.0); mọi output market=US (chưa kiểm chứng nhánh EU). *Điểm tốt: output product-page trung thực, không bịa số.*

### 03 — Growth (13)
- **C1** ⚠️ target committed ROAS≥2.5 thực chất **lỗ** + evidence "GM 45–55%" bịa (thật 36.4%/23%); KRI Amber<2.5/Red<1.8 mis-calibrated. → D2.
- **H1** hệ tên `vibe-opc-pod-growth-*` (kể cả "fb-creative"→thật "creative") ≠ folder. → D1.
- **H2** link gãy kb/prompt orchestrator (**đã fix** A1).
- **H3** ngưỡng **KILL 1.5** (orchestrator/_rules/_knowledge) vs **1.8** (SOP/executor/KRI) → automation mâu thuẫn vùng 1.5–1.8. → D4.
- **M1–M7/L1–L2**: _knowledge "ROAS≥2.5 ngưỡng vàng" stale; output organic có **comment/tag bait** ("Drop a 🐾", "Tag your partner") vi phạm gate "no engagement bait" nhưng self-check ✅ (batch 07-21 đã sửa); weekly-posts do **sai worker** tạo (creative thay marketing, RACI); link OKR→review-queue (**đã fix**); đếm "3 worker" bỏ orchestrator; ref xuyên phòng tên cũ; **catalog upstream thiếu 3 tuần → 3/4 post HOLD**, SOP-GRW-001 thiếu escalation → cadence SLO không đạt; ™ trên "Pickleball Obsessed™"; template README stub. *Điểm tốt: SOP-002/004 chất lượng cao, winner-registry đóng vòng.*

### 04 — Fulfillment & CX (10)
- **F1(C)** mọi SOP "Responsible AI" + governance dùng `vibe-opc-pod-fulfillment-*` → D1.
- **F2(H)** orchestrator không có trong dept governance. → D3.
- **F3(H)** link gãy routing-map (**đã fix** A1).
- **F5/F6(M)** ⚠️ metric 2 ngưỡng: "on-time routing ≥98%" đo ở **18h (SOP) vs 24h (KPI/OKR)**; tracking-sent **6h/100% (SOP) vs 12h/99% (KPI/KRI)** → KPI xanh khi SLO breach. → D4.
- **F4/F7/F8/F9/F10(L)**: downstream backoffice tên lệch (bck-finance vs bck-orchestrator, schema const); GDPR KPI đo ≤30 ngày (legal) thay SLO ≤20; SOP-004 conformity thiếu bound "2 năm bảo hành EU (Dir 2019/771)"; SOP-003 nhánh 4.G trước 4.F; order-routing.schema thiếu `order_value`/`paid_at`/`routed_at` mà escalation cần. *Điểm tốt: EU consumer law Art.16(c) làm tốt; $30 refund gate enforce chuẩn.*

### 05 — Backoffice (14)
- **F1(C)** ⚠️ **GPSR nhãn chỉ tiếng Anh** — vi phạm GPSR 2023/988 Art.9(7)&45 (bắt buộc bản ngữ nước bán: FR/DE/IT/ES; Toubon FR). Gate `label_ready` cho PASS SP non-compliant. → D5 (pháp lý).
- **F2(H)** ⚠️ **VAT thiếu nhánh domestic** — chỉ IOSS vs OSS Union, bỏ cung ứng nội địa (in&giao cùng nước → phải đăng ký VAT local). POD provider gần → đơn nội địa phổ biến → rủi ro khai sai. → D5.
- **F3(H)** `_knowledge:41` giữ công thức profit cũ (bỏ VAT+fx, ROAS 2.5). → D2. *Auto-fixable.*
- **F4(H)** KRI `blended_roas` hard-code Green≥2.5 (BE US 2.75). → D2. *Auto-fixable.*
- **F5–F9(M)**: tên skill governance ≠ folder (D1); orchestrator vắng roster (D3); hard-code "12 worker" vs GATE cấm hard-code + workforce-map canonical stale; 6 link gãy (**đã fix** A1); không có `quality_tier`, gate legal chỉ min_confidence 0.7 (quá thấp cho pháp lý). → D4.
- **F10–F14(L)**: `$schema` orchestrator sai (**đã fix** A2); finance skill.json thiếu `$schema` (**đã fix** A3); README "Stretch x10" mâu thuẫn OKR; folder pipeline chưa tồn tại; Meta CAPI legal basis nên chốt = consent (ePrivacy). *Điểm tốt: clearance-log/profit-report schema chuẩn; GDPR (DSAR/breach 72h/RoPA) + GPSR 13/12/2024 chính xác.*

---

## 5. Quyết định cần Owner (đã ghi vào [review-queue](../output/review-queue.md))

| ID | Quyết định | Ảnh hưởng | Khuyến nghị |
|----|-----------|-----------|-------------|
| **D1** | Namespace: gộp về 1 lớp `vibe-eu-opc-*` hay giữ 2 lớp legacy+EU? | 75 file, binding SOP→skill | Gộp 1 lớp `vibe-eu-opc-*`, rename cơ học toàn repo, bỏ mô tả legacy |
| **D2** | ROAS/margin: bỏ ROAS 2.5 + gross-45 gate, chuyển hẳn BE-ROAS per-SKU + contribution floor ở governance | MER/GRW/BCK OKR/KPI/KRI/_knowledge | Reconcile toàn bộ về BE-ROAS; sửa evidence GM về 36.4%/23% |
| **D3** | Roster: thêm orchestrator + SOP thiếu (PRD-005, MER-005) vào coverage; chốt chủ sở hữu gate IP G3 | 5 phòng governance | Thêm orchestrator W0; chốt Product Studio pre-check → BCK ký |
| **D4** | Chốt 1 ngưỡng cho các metric lệch: KILL 1.8, routing 18h, tracking 6h, enum clearance=CLEAR, IP enum, upscale policy, human-review 20% | SOP vs skill | Lấy giá trị chặt hơn làm chuẩn; sửa đồng loạt |
| **D5** | Compliance + output QC: GPSR nhãn bản ngữ, VAT domestic branch, regenerate output đạt schema + re-download ảnh, chạy validator | Pháp lý + output thật | Ưu tiên cao nhất; block publish EU cho tới khi xong |

---

## 6. Điểm mạnh (giữ nguyên)
- Anti-hallucination contract (evidence/confidence/need_review) đầy đủ 19/19 skill — cả SKILL.md lẫn schema `required`.
- Gate cứng encode bằng JSON Schema `if/then`: GPSR No-Publish, refund>$30, IP/TM REJECT-default, VAT, BE-ROAS per-SKU — rất chắc.
- Smoke-test thực tế (fail-closed GPSR, contribution anti-lãi-ảo, schema if/then).
- EU consumer law (Fulfillment) + GDPR/GPSR mốc pháp lý (Backoffice) chính xác.
- `.secrets/.gitignore` cấu hình đúng chuẩn bảo mật — secrets không bị commit.
- Output (nơi có) **trung thực** — khai rõ concept/giả định, không bịa review/đơn.
