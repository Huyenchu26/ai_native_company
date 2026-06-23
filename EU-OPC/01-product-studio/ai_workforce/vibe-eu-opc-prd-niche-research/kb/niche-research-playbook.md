# KB — Niche Research Playbook (DAKOfits, SOP-PRD-001/002)

Cẩm nang chấm điểm & validate niche đa-niche cho POD AOP leggings/activewear DAKOfits (ShopBase, US+EU).

---

## 1. Rubric scoring (tổng 100)

| Tiêu chí | Trọng số | Đo bằng | Nguồn |
|----------|:---:|---------|-------|
| **Demand** | 40 | ad-volume + ad-age (ad sống) + search interest | AdSpy/BigSpy + Google Trends |
| **Competition** | 25 | số nhà bán đang chạy ad; ad càng nhiều, đa dạng → điểm DEMAND xác nhận nhưng cạnh tranh cao → cân nhắc | AdSpy/BigSpy |
| **Margin-fit** | 20 | khả năng đạt contribution margin sau ad+fee+VAT cho leggings AOP | catalog + ước tính |
| **IP-risk** | 15 | term có dính TM/brand/club/character? (điểm cao = risk thấp) | TM/brand check |

> Ghi điểm thành phần vào `score_breakdown` (demand ≤40 / competition ≤25 / margin_fit ≤20 / ip_risk ≤15).

## 2. Ngưỡng pass (gate cứng)

- **`demand_score ≥ 70/100`** VÀ **`audience_size ≥ 500.000`** (Meta interest stack US+EU) → `decision = validated`.
- `audience < 500k` nhưng demand cao → `decision = watchlist` (micro-niche, không scale ngay).
- `demand_score < 70` → `decision = rejected`.
- Trùng với SP có trong catalog ~3.200 SP → `decision = refresh-iterate` (không tạo mới).
- **Rationale ngưỡng (need_review sau 30 ngày):** audience ≥500k = đủ rộng để FB Ads tìm winner ở CPA mục tiêu <$20; score ≥70 = mức demand tối thiểu vào pipeline. Đây là giả định ban đầu — review lại theo CPA/ROAS thực tế.

## 3. Tools whitelist

| Tool | Dùng để | Lưu ý |
|------|---------|-------|
| **AdSpy / BigSpy** | ad-volume, ad-age, competitor spy | **Lọc ad-age < 90 ngày** — tránh validate ad đã chết |
| **Meta Audience Insights** | audience size interest stack US+EU | Stack interest đúng nhóm niche |
| **Google Trends** | search interest 12–24 tháng, seasonality | Trends rỗng (niche quá mới) → hạ confidence + need_review |

## 4. IP/TM pre-flag rule (chỉ pre-flag — KHÔNG clearance chính thức)

| `ip_risk_flag` | Khi nào | Hành động |
|----------------|---------|-----------|
| **CLEAR** | Không thấy TM/brand/club/character | Tiếp tục bình thường |
| **FLAG** | Term mơ hồ, có thể chạm TM | Ghi chú, để human review |
| **HIGH** | Dính brand / club name / character / licensed IP | **Bắt buộc đẩy thẳng PRD-004** trước khi design; set `need_review=true` |

Clearance chính thức (GPSR/IP-TM/Responsible Person) thuộc Backoffice compliance — ở đây CHỈ pre-flag.

## 5. Seasonal & lead-time (SOP-PRD-002)

- Phân loại **evergreen vs seasonal** từ đường cong Google Trends 12–24 tháng.
- Map niche → holiday/event US+EU: Christmas, Halloween, Mother's/Father's Day, Valentine, back-to-school, sport season…
- **Lead-time rule:** `design_deadline = peak_week − lead_time`, đảm bảo **≥ 6 tuần** trước peak (buffer +1 tuần). Peak cận hơn lead-time → hạ priority, lên lịch năm sau.
- **Priority** = `demand_score × proximity-peak`, với `proximity-peak = 1 / (số tuần tới peak)` (deterministic, lặp lại được).
- Rolling horizon **≥ 12 tuần**. Evergreen → "always-on backlog" (không deadline cứng). Cap **5–10 SP/đợt** (SOP-MER-006).

## 6. Anti-hallucination

Mỗi entry PHẢI có `evidence[]` (≥1, từ whitelist), `confidence_score` (gate ≥0.7), `need_review`. Không bịa số — thiếu nguồn → hạ confidence + `need_review=true`. Validate output qua `schema/niche-validation.schema.json`.

## 7. Handoff

Output `validated_niche_list` + `seasonal_opportunity_calendar` → **vibe-eu-opc-prd-design** (PRD-003) + **vibe-eu-opc-prd-orchestrator**. Lưu ý chuỗi: niche → design → catalog (live ShopBase) → Growth (ads).
