# Pipeline Test Report — DAKOfits EU-POD-OPC end-to-end

**Ngày:** 2026-08-03/04 · **Niche test:** Horse Riding / Equestrian (AI chọn) · **Chế độ:** dry-run tích hợp — chạy 1 sản phẩm qua toàn chuỗi research→ads, mỗi chặng đóng vai đúng skill + đọc SKILL.md/SOP/schema thật, validate artifact, ghi rõ chỗ cần API ngoài.
**Chi tiết từng chặng:** [RUN-LOG.md](./RUN-LOG.md) · **Artifacts:** [artifacts/](./artifacts/)

---

## 1. Verdict tổng

> **Các skill "chạy được và có kỷ luật" — chúng tạo ra artifact đúng schema và fail-closed (từ chối đi tiếp) đúng chỗ khi thiếu dữ liệu. NHƯNG pipeline end-to-end KHÔNG chạy tới đích thật được, vì 2 lý do độc lập: (1) mọi API ngoài đều thiếu, (2) lớp "gate cứng" thực ra không được enforce bằng công cụ — chỉ dựa vào LLM tự tuân.**

| Chặng | Skill | Artifact PASS schema? | Chạy được? | Chốt |
|-------|-------|:---:|:---:|------|
| S1 research | prd-niche-research | ✅ (`--artifact`) | ⚠️ | Ra artifact valid; mọi số là ước lượng (thiếu Meta/AdSpy/Trends). Bug validator `--run-all`. |
| S2 design+IP | prd-design | ✅ | ⚠️/🔴 | Fail-closed đúng (REJECT, tra 0/2 thị trường). Lộ 3 bug audit + validator bỏ qua gate if/then. |
| S3 pricing | mer-catalog | ✅ | ✅ | Skill mạnh: contribution + BE-ROAS per-SKU. Chứng minh output cũ chạy ẩu (fail 4 lỗi schema). |
| S4a mockup | mer-visual | ✅* | ⚠️/🔴 | *PASS chỉ vì bẻ cho vừa schema production. Canva chặn auth. Schema thiếu validation-first mode (M4). |
| S4b listing | mer-product-page | ✅ (`--artifact`) | ⚠️ | Copy chuẩn, GPSR fail-closed đúng. `--run-all` CRASH. Gate GPSR không enforce. Escalate compliance gãy tên. |
| S5 organic | grw-marketing | n/a (no schema) | ⚠️ | Worker đúng. Gate "no engagement bait" không có enforcement. SOP thiếu nhánh escalation. |
| S6 creative+ads | grw-creative / grw-fb-ads | ✅ (cả `--run-all`) | ⚠️/🔴 | Skill kỷ luật, fail-closed đúng. Xác nhận KILL 1.8/1.5 lệch + ROAS 2.5 sót. Không API → không launch. |

**Kết quả sản phẩm test:** niche Horse Riding dừng ở trạng thái **watchlist/blocked** xuyên suốt — đúng như thiết kế (thiếu dữ liệu thật → không được publish). Đây là **tín hiệu TỐT**: hệ thống không "vờ thành công".

---

## 2. 🐛 Bug MỚI chỉ lộ khi CHẠY (audit tĩnh không bắt được) — quan trọng nhất

### P1 · Validator KHÔNG enforce gate `allOf`/`if`/`then` — "gate cứng" là ảo
`script/validator.py::validate_instance` chỉ xử lý type/required/enum/const/min-max/items/properties — **bỏ qua hoàn toàn `allOf`/`if`/`then`/`anyOf`/`oneOf`**. Mọi gate fail-closed encode trong schema (vd design: `PASS ⇒ uspto_checked=true AND euipo_checked=true`; product-page: `market=EU ⇒ gpsr PASS + label`) **không được kiểm bằng công cụ**.
- **Đã verify thực nghiệm:** artifact `{PASS, handoff_ready=true, uspto_checked=false, euipo_checked=false, conf=0.95}` → validator trả **`ok:true`**.
- **Hệ quả:** báo cáo audit tĩnh khen "gate if/then rất chắc" là **SAI**. Gate chỉ được tôn trọng vì LLM tự nguyện làm đúng. Một run cẩu thả (đúng như output cũ pickleball/yoga) sẽ vượt qua trót lọt.
- **Phạm vi:** systemic — 19/19 skill dùng chung validator template này.

### P2 · Hợp đồng `evidence` không nhất quán → `--run-all` khi thì trừ điểm khi thì CRASH
`verify_evidence()` giả định evidence là **array of object** có `verbatim_quote` + `source` là **đường dẫn file**. Nhưng schema các skill dùng 2 quy ước khác nhau:
- **(A) object/generic** (fb-ads, orchestrator...): `{verbatim_quote, source=filepath}` → validator OK, `--run-all` chạy (S6 verified 7/7).
- **(B) domain** (niche: `{source=enum tên tool, detail}`; product-page: array-of-**string**): → mọi evidence bị coi "missing" trừ 0.2/item về 0 (S1/S2), hoặc **CRASH** `AttributeError` (S4b product-page).
- **Hệ quả:** `--run-all` (pipeline validate chính thức) **không dùng được** cho ≥4 skill. Cần thống nhất 1 quy ước evidence toàn hệ.

### P3 · Nhiều schema không model được trạng thái fail-closed hợp lệ
- design-clearance: enum chỉ `PASS/MODIFY/REJECT` — không có `PENDING`/"chưa tra được" → case "0 nguồn" phải nhét vào REJECT (sai ngữ nghĩa). Orchestrator lại CÓ `PENDING` → vocabulary 2 tầng lệch.
- product-page: `allOf` ép EU⇒gpsr PASS → **không biểu diễn được trang EU bị BLOCK** dù `publish_status` enum có "blocked" (draft-07 báo INVALID).
- mockup-set: thiếu `phase`/`local_file`/`canva_design_id`, ratio thiếu `9:16`, `print_accuracy_pass` không nullable → **mode validation-first không hợp schema** (mẫu pickleball cũ của chính skill fail validator).

### P4 · `quality_gates[].min_confidence` khai trong skill.json nhưng KHÔNG script nào đọc
product-page khai GPSR gate `min_confidence=1.0`; catalog khai `0.7` cho cùng cổng GPSR. **Không runtime nào enforce** — `check_confidence` chỉ dùng `--threshold` mặc định 0.7 (và chỉ qua `--run-all`). Ngưỡng 1.0 là trang trí.

### P5 · Gate content (prose) không có bộ kiểm tất định
Organic posts + ad copy: gate "no engagement bait", "no fake review", IP/TM claim (™) — không có schema lẫn detector. Validator chỉ check JSON. → mọi "✅ policy pass" là LLM tự khai (đúng lý do output cũ "Drop a 🐾" vẫn ✅).

---

## 3. ✅ Xác nhận audit — chạy thật chứng minh các finding là bug THẬT

| Finding audit | Xác nhận khi chạy |
|---|---|
| **C2 gate enum PASS↔CLEAR (PRD)** | S2: design xuất "PASS", orchestrator schema chỉ nhận "CLEAR" (`additionalProperties:false`) → handoff Merch gãy schema. Không ai map. |
| **H2 "KHÔNG upscale" (PRD)** | S2: SKILL.md Actuator dòng 69,71 bắt Real-ESRGAN/Topaz upscale — mâu thuẫn non-negotiable. |
| **C3 output "PASS(CLEAR)" khi chưa EUIPO** | S2: khi chạy trung thực, tra 0/2 thị trường → phải REJECT. Output cũ "PASS" là vi phạm gate. |
| **X4/C3 output không đạt schema (MER)** | S3: pickleball-pricing cũ fail 4 lỗi schema; skill chạy đúng thì PASS 100% → output cũ chạy ẩu, validator chưa từng chạy. |
| **H1 ảnh ma (MER)** | S4a: xác nhận Canva chặn → nếu chạy đúng phải khai "0 ảnh trên đĩa"; output cũ khai coverage OK là bịa. |
| **M4 schema mockup (MER)** | S4a: schema không hỗ trợ validation-first; mẫu cũ fail schema. |
| **L3 GPSR confidence lệch (MER)** | S4b: catalog 0.7 vs product-page 1.0, không cái nào enforce. |
| **D1 namespace (toàn cty)** | S4b: escalate GPSR trỏ `vibe-opc-pod-backoffice-compliance` (tên cũ) → dependency gãy khi cần. |
| **M3 sai worker organic (GRW)** | S5: SOP R=marketing; output cũ ghi creative + tên cũ. |
| **M7 thiếu escalation catalog (GRW)** | S5: SOP-GRW-001 §4 không có nhánh thiếu live product → cadence SLO âm thầm fail. |
| **H3 KILL 1.8 vs 1.5 (GRW)** | S6: SOP/skill/playbook=1.8; _rules/_knowledge/orchestrator=1.5. |
| **C1 ROAS 2.5 dưới break-even (GRW)** | S6: SOP/skill đã dùng BE-ROAS per-SKU, nhưng `_knowledge:34` vẫn hard-code 2.5. |

---

## 4. 🔴 Bản đồ chặn bởi tool ngoài (cần authorize/API mới chạy thật)

| Tool | Chặng phụ thuộc | Trạng thái |
|------|-----------------|-----------|
| Meta Audience Insights / AdSpy / Google Trends / Ad Library | S1 research (gate audience 500k, competition, seasonal) | ❌ Không có token |
| USPTO / EUIPO TM database | S2 IP clearance (gate G3 dual-market) | ❌ Không tra được |
| Ảnh render 300 DPI + Canva MCP | S2 design, S4a mockup, S6 creative | ❌ **Canva cần authorize** (claude.ai connector), non-interactive |
| Printify/PrintBase cost API + ShopBase bridge | S3 pricing (cost thật), S setup | ❌ Không có token |
| Video-gen (Runway/Kling/HeyGen) | S6 creative video | ❌ Không có |
| Meta Marketing / CAPI / Ads Manager | S6 fb-ads (launch, ROAS/spend thật) | ❌ Không có token |

→ Trong môi trường này pipeline **chỉ chạy tới tầng "spec + plan + fail-closed"**, không tới listing/ads thật. Đây là **giới hạn môi trường**, không phải skill bất lực.

---

## 5. Khuyến nghị sửa (ưu tiên)

**Nhóm HARNESS (làm trước — vì nó vô hiệu hoá chính cơ chế anti-hallucination):**
1. **P1** — Cho `validator.py` thực thi `allOf`/`if`/`then` (hoặc thay bằng thư viện `jsonschema` draft-07 chuẩn). Không có bước này, mọi "gate cứng" chỉ là niềm tin.
2. **P2** — Thống nhất 1 quy ước `evidence` toàn hệ + sửa `verify_evidence()` cho khớp; hiện `--run-all` gãy ở ≥4 skill.
3. **P4/P5** — Đọc & enforce `min_confidence` per-gate; thêm detector prose cho gate content (engagement-bait, fake-review, ™ claim) hoặc chuyển thành checklist bắt buộc có bằng chứng.
4. **P3** — Bổ sung trạng thái fail-closed vào schema (design `PENDING`; product-page cho phép EU-blocked; mockup validation-first mode).

**Nhóm GOVERNANCE (trùng D1–D4 của audit — giờ có bằng chứng chạy thật):**
5. **D1** namespace: escalate compliance đã gãy thật khi chạy → gộp `vibe-eu-opc-*`.
6. **D4** chốt ngưỡng: enum CLEAR (không PASS), KILL 1.8, GPSR confidence 1 giá trị.
7. **D2/C1** dọn `_knowledge` các phòng: bỏ ROAS 2.5 + công thức gross ảo còn sót.

**Nhóm QUY TRÌNH:**
8. Bắt buộc chạy `validator.py` (sau khi fix P1/P2) trên MỌI output trước khi vào `output/` — output cũ chưa từng qua bước này.
9. Thêm nhánh escalation "thiếu live product/catalog" vào SOP-GRW-001.

---

## 6. Điểm mạnh (chạy thật xác nhận)
- **Fail-closed hoạt động đúng ở mọi chặng:** thiếu dữ liệu → REJECT/HOLD/need_review, KHÔNG bịa để đi tiếp. Đây là hành vi đáng tin.
- **Trung thực dữ liệu:** mọi agent đánh dấu rõ ước lượng vs số thật, không lặp lỗi "ảnh ma"/"PASS giả" của output cũ.
- **Skill có năng lực thật:** S3 pricing chứng minh skill tạo được artifact đạt schema đầy đủ — vấn đề nằm ở khâu thực thi output cũ + thiếu tool + harness chưa enforce, KHÔNG phải thiết kế skill.
- Anti-hallucination contract (evidence/confidence/need_review) hiện diện đúng chỗ; chỉ cần harness enforce là chắc.
