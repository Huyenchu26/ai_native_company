# Pipeline Test Run Log — DAKOfits EU-POD-OPC
**Ngày:** 2026-08-03/04 · **Niche:** Horse Riding / Equestrian (AI chọn) · **Chế độ:** dry-run tích hợp (không có API ngoài thật)

> Test "SOP/skill có chạy được không" bằng cách chạy 1 sản phẩm qua toàn chuỗi. Không truy cập được Meta/AdSpy/Canva/Printify/FB → các bước cần tool ngoài được đánh dấu 🔴 hoặc workaround ước lượng.

## S1 — niche-research (vibe-eu-opc-prd-niche-research) → ⚠️ chạy được, workaround nặng + 1 bug thật
- Niche: **Horse Riding / Equestrian** (hobby). demand_score 74, audience_size 3.2M (ƯỚC LƯỢNG), ip_risk_flag CLEAR, decision=watchlist, confidence 0.42, need_review=true.
- Artifact schema-valid ✅ (`--artifact/--schema` PASS). Trung thực: mọi evidence source="other" ghi rõ "estimate — no live tool access", không bịa số tool.
- 🔴 Bước cần tool thật KHÔNG chạy: SOP 1.1 AdSpy/BigSpy, 1.2 Google Trends, 1.3 Meta Audience Insights (gate 500k phụ thuộc hoàn toàn), 1.5 Meta Ad Library. SKILL "Actuator" (pull live API) không chạy.
- 🐛 **BUG THẬT (đã verify):** `validator.py --run-all` verify_evidence() tìm `verbatim_quote` + coi `source` là filepath (validator.py:147-151), nhưng schema niche định nghĩa evidence `{source=enum tên tool, detail, value, date}`. → mọi artifact niche hợp lệ luôn bị -0.2/evidence → confidence sập → KHÔNG BAO GIỜ pass `--run-all`. Lỗi contract cross-tool, độc lập việc thiếu tool. **Nghi ngờ lặp ở nhiều skill** (validator copy từ template generic).
- 🐛 Mâu thuẫn rule: "auto-pass khi demand≥70 & audience≥500k" vs "data thiếu→need_review" — không nói rule nào thắng. + SOP 3.3 human-review 20% vs SKILL auto-pass (trùng finding audit H3).

## S2 — design + IP clearance (vibe-eu-opc-prd-design) → ✅ fail-closed đúng, nhưng lộ 3 bug audit + 2 lỗ hổng validator
- Artifact schema-valid ✅. clearance_status=REJECT (fail-closed đúng: tra 0/2 thị trường), handoff_ready=false, need_review=true. Không bịa "EUIPO PASS" (tránh lỗi C3).
- ✅ XÁC NHẬN 3 finding audit là bug THẬT khi chạy:
  - (a) Enum PASS↔CLEAR: design schema `ip_clearance_status` enum [PASS,MODIFY,REJECT]; orchestrator `cleared_designs.clearance_status` enum [CLEAR] + `additionalProperties:false`. Design xuất "PASS" → gãy schema orchestrator. Không ai map PASS→CLEAR. Handoff Merch gãy.
  - (b) "KHÔNG upscale" non-negotiable vs SKILL.md Actuator dòng 69,71 BẮT dùng Real-ESRGAN/Topaz upscale ≥4000px. Mâu thuẫn hard-rule khi chạy actuator.
  - (c) Single/dual-market: tra 0/2 → đúng phải REJECT (không PASS/CLEAR).
- 🐛🐛 **LỖ HỔNG HARNESS NGHIÊM TRỌNG (đã verify thực nghiệm):** `validator.py::validate_instance` KHÔNG xử lý `allOf`/`if`/`then`/`anyOf`/`oneOf`. → mọi GATE CỨNG fail-closed encode trong schema (handoff⇒PASS, PASS⇒dual-checked, conf<0.7⇒need_review) KHÔNG được validator kiểm. Test: artifact {PASS, handoff_ready=true, uspto_checked=false, euipo_checked=false, conf 0.95} → validator trả **ok:true**. Audit tĩnh khen "gate if/then rất chắc" là SAI — gate chỉ dựa LLM tự tuân, không có enforcement tất định. **Hệ thống (mọi skill dùng chung validator template).**
- 🐛 Xác nhận lại bug evidence-contract của validator `--run-all` (verbatim_quote vs source/detail) — lặp ở skill design → **systemic đúng như nghi ngờ ở S1.**
- 🐛 Schema design thiếu trạng thái PENDING (chỉ PASS/MODIFY/REJECT); orchestrator lại có PENDING → vocabulary 2 tầng không khớp.
- 🔴 KHÔNG handoff Merch được (đúng, do fail-closed + bug enum).

## S3 — pricing (vibe-eu-opc-mer-catalog) → ✅ CHẠY ĐƯỢC (skill mạnh), chứng minh output cũ chạy ẩu
- Artifact schema-valid ✅ (pricing-decision.schema, đủ 11 required + evidence[]). Contribution margin US 13.3% / EU 7.9% ở CPA giả định (FAIL floor 15% — trung thực, niche này chưa viable ở giả định đó). BE-ROAS per-SKU per-market (US 2.15/2.75, EU 2.27/4.32), KHÔNG hard-code 2.5.
- ✅ CHỨNG MINH X4/C3: validate output pricing CŨ `2026-06-25-pickleball-pricing.json` → FAIL 4 lỗi (thiếu 7 required do nhét nested trong `us`, competitive_position sai enum, evidence[] là dict thay vì string). Skill đủ khả năng; output cũ hỏng do chạy không theo schema → **audit đúng: validator/QC chưa từng chạy trên output thật.**
- ✅ (a) contribution margin, KHÔNG còn gross 45% (chỉ tiêu đề SOP-MER-003 còn chữ "Gross Margin 45-55%"). (c) BE-ROAS per-SKU đúng.
- 🐛 Bug schema mới: mô tả `contribution_margin = net_price − ... − vat` **double-count VAT** cho EU (net_price đã trừ VAT). Skill tính đúng nhưng schema formula sai.
- 🔧 Chặn số thật: Printify/PrintBase cost API, Growth CPA/winner-ROAS thật, FX — đều giả định (bỏ trống field không bịa).
- 🔴 Không handoff publish (upstream REJECT + floor FAIL) nhưng ✅ cơ chế skill chạy đúng.

## S4 — mockup (mer-visual) + product-page (mer-product-page) [song song]

### S4a mockup (mer-visual) → ⚠️ chạy được, gap schema M4 + Canva chặn
- Artifact PASS schema NHƯNG chỉ vì bẻ manifest cho vừa schema production (bỏ ảnh 9:16, ép type enum). Trung thực: 0 ảnh trên đĩa, local_file="NOT ON DISK", print_accuracy_pass=false, min_images_met=false, conf 0.28, need_review=true. **Tránh đúng lỗi H1 (không khai ảnh ma).**
- ✅ XÁC NHẬN M4: schema mockup-set KHÔNG có phase/local_file/canva_design_id; ratio enum thiếu "9:16"; type thiếu flat-lay/story; print_accuracy_pass không nullable. **Mẫu pickleball validation CŨ chạy validator → FAIL toàn bộ** (chính mẫu chuẩn của skill không hợp schema mình).
- 🔴 Canva MCP chưa authorize (non-interactive) → không render/tải ảnh. Blocker cứng.

### S4b product-page (mer-product-page) → ⚠️ copy chuẩn, nhưng 3 lỗi harness + dependency gãy
- Skill CÓ schema product-page.schema.json. Artifact `--artifact/--schema` PASS. Copy trung thực (rating=0, review placeholder ghi rõ "do not publish fake"). GPSR fail-closed đúng: publish_status=blocked, need_review=true.
- 🐛 `--run-all` **CRASH** (`AttributeError: 'str'...` validator.py:147) — evidence schema là array of string nhưng verify_evidence() giả định array of object. Biến thể NẶNG của bug systemic (crash, không chỉ -0.2).
- 🐛 GPSR gate min_confidence=1.0 **KHÔNG enforce** — không script nào đọc quality_gates[].min_confidence; check_confidence dùng threshold mặc định 0.7 (chỉ qua --run-all vốn crash). Xác nhận L3: catalog 0.7 vs product-page 1.0, không cái nào enforce.
- 🐛 Schema `allOf` ép market=EU⇒gpsr PASS+label true → **không model được trang EU bị BLOCK** (draft-07 báo INVALID); nhưng validator harness bỏ qua allOf nên vẫn ok:true. Gate GPSR trong schema là decorative.
- 🔴 XÁC NHẬN D1 tác động cụ thể: escalate GPSR trỏ `vibe-opc-pod-backoffice-compliance` (skill.json+prompt+kb) — folder thật `vibe-eu-opc-bck-compliance` → **dependency gãy** khi cần escalate.
- 🔴 Không handoff (GPSR block + upstream REJECT + floor FAIL) — đúng fail-closed.

## S5 — content organic (vibe-eu-opc-grw-marketing) → ⚠️ chạy đúng cơ chế, 3 gap khớp audit
- Artifact 05-organic-posts.md (3 post, HOLD). Skill KHÔNG có organic-post schema (chỉ email-campaign/execution-log/skill-meta) → không validate được bằng script; validator chỉ check JSON, không check prose.
- 🐛 (a) Gate "No engagement bait" KHÔNG có enforcement: không nằm trong SOP-GRW-001 checklist §5 (chỉ là rule Meta tự thêm); validator không check caption. → mọi "✅" là LLM tự khai (đúng lý do output cũ 07-07 "Drop a 🐾" vẫn pass). Agent tự dựng lexical scan cho test, KHÔNG phải của skill.
- ✅ (b) XÁC NHẬN M3: SOP-GRW-001 R=marketing, C=creative. Output cũ ghi author creative `vibe-opc-pod-growth-fb-creative` = sai worker + tên cũ. Bug thật.
- ✅ (c) XÁC NHẬN M7: SOP-GRW-001 §4 KHÔNG có nhánh escalation khi thiếu live product/catalog → worker phải improvise HOLD → cadence SLO ≥90% âm thầm fail.

## S6 — creative (grw-creative) + fb-ads (grw-fb-ads) → ⚠️ skill chạy đúng+kỷ luật, nhưng pipeline-to-ads KHÔNG chạy được
- 06a-creative.json + 06b-fb-ads-plan.json đều PASS schema ✅. **06b PASS cả `--run-all`: 7/7 evidence verified, confidence 0.3 → route human-review đúng fail-closed.**
- 💡 PHÁT HIỆN quan trọng về bug validator: fb-ads `--run-all` CHẠY được vì schema dùng evidence dạng OBJECT (source=filepath + verbatim_quote). → bug evidence-contract thực chất là **KHÔNG NHẤT QUÁN 2 quy ước evidence**: (A) object/generic (fb-ads, orchestrator...) → validator OK; (B) domain (niche source=enum tool+detail; product-page array-of-string) → validator -0.2 hết hoặc CRASH. Cần thống nhất 1 quy ước.
- ✅ (a) XÁC NHẬN H3: KILL 1.8 (SOP-GRW-002 §4 + fb-ads SKILL + playbook, Platform ROAS) vs 1.5 (_rules + _knowledge + orchestrator SKILL + routing-map + run-batch-prompt). Agent set 1.8 + flag reconcile.
- ✅ (b) XÁC NHẬN C1 sót: fb-ads SKILL/SOP dùng BE-ROAS per-SKU đúng (bác 2.5), NHƯNG `_knowledge/README.md:34` VẪN hard-code winner "ROAS≥2.5". Bug sống trong knowledge file.
- ✅ (c) RACI creative(R)/marketing(C)/fb-ads(C) rõ. Agent còn bắt "Born to Ride™" TM chưa verify trong 04b → self-check=false, route compliance (fail-closed tốt).
- 🔴 Chặn: Canva/video-gen API (creative), Meta Marketing/CAPI API (ads) → không launch. Mọi ROAS/spend/CPA=0 (no data, không bịa).
- 🔴 Pipeline-to-ads KHÔNG runnable: upstream design REJECT + 04b publish-blocked + không API. Mọi gate downstream nói HOLD đúng.
