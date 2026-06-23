# SOP-PRD-001 — Niche Research đa-niche (Demand Scoring & Audience Sizing)

| Trường | Giá trị |
|--------|---------|
| **Mã SOP** | SOP-PRD-001 |
| **Phiên bản** | 1.0 |
| **Ngày** | 2026-06-23 |
| **Chủ sở hữu** | Product Studio (dept: prd) |
| **Department** | 01-product-studio |
| **AI Workforce** | `[AI WORKFORCE]` — chạy bởi **vibe-opc-pod-product-niche-research** |

---

## 0. IPO Analysis

| Loại | Mục |
|------|-----|
| **Input (I)** | AdSpy/BigSpy export, Meta Audience Insights, Google Trends CSV, danh mục niche pool (~3.200 SP hiện hữu + niche mới đề xuất), competitor list (Gearbunch + tương tự) |
| **Control (C)** | Niche scoring rubric (demand 40 / competition 25 / margin-fit 20 / IP-risk 15), ngưỡng pass ≥ 70/100, IP/TM pre-flag rule (no clear-risk → pre-flag), thị trường target = US+EU |
| **Output (O)** | **Validated niche list** (≥3 niche/tuần) với score + audience size + IP pre-flag + **competitor price table per niche** (price range + offer/bundle + ad longevity); feed sang SOP-PRD-002 và SOP-PRD-003; bàn giao competitor price → Merch **SOP-MER-003** (anh Định định giá cạnh tranh) |
| **Mechanism (M)** | AI Worker `niche-research` + AdSpy/BigSpy + Meta Audience Insights + Google Trends; human review tại `processing/human-review` |

**Upstream:** 00-company Strategy (niche pool direction, Company OKR O3) → SOP-PRD-001
**Downstream:** SOP-PRD-001 → SOP-PRD-002 (seasonal timing) → SOP-PRD-003 (design)

---

## 1. Tổng Quan

- **Mục đích:** Validate nhu cầu cho niche AOP activewear ĐA NICHE (dog breed chỉ là 1 trong nhiều niche: pet, hobby, profession, zodiac, sport, faith…) để chỉ đưa vào pipeline những niche có demand thật + audience đủ lớn + IP-risk thấp.
- **Phạm vi:** Từ niche pool → validated niche list. KHÔNG bao gồm design (PRD-003) hay clearance chính thức (PRD-004 — chỉ pre-flag ở đây).
- **Định nghĩa:**
  - **Demand score:** điểm tổng hợp từ ad-volume (AdSpy), search interest (Trends), audience size (Meta).
  - **Audience size:** số người Meta ước tính cho interest stack tại US+EU.
  - **IP pre-flag:** cảnh báo sớm tên niche/term có khả năng dính TM (vd brand, club name).

## 2. Vai Trò & Trách Nhiệm

**RACI**

| Hoạt động | OPC (Owner) | AI niche-research | AI product-design | 02-merch |
|-----------|:----:|:----:|:----:|:----:|
| Thu thập data (AdSpy/Trends/Meta) | A | R | I | - |
| Scoring & ranking niche | A | R | C | - |
| IP pre-flag | A | R | C | I |
| Duyệt validated list | R/A | C | I | I |

**AI Roles**

| AI Worker | Skill | Trách nhiệm trong SOP |
|-----------|-------|----------------------|
| vibe-opc-pod-product-niche-research | niche demand scoring, audience sizing, ad spy, IP pre-flag | Responsible — sinh validated list |

## 3. Quy Trình

### Bước 1 — Thu thập tín hiệu demand
| I | C | O | M |
|---|---|---|---|
| Niche pool + competitor list | Source whitelist (AdSpy/BigSpy/Meta/Trends) | Raw signal dataset | AI niche-research |

| # | Hành động | Công cụ | Owner |
|---|-----------|---------|-------|
| 1.1 | Pull ad-volume + ad-age cho mỗi niche | AdSpy/BigSpy | AI |
| 1.2 | Pull search trend 12 tháng | Google Trends | AI |
| 1.3 | Pull audience size interest stack US+EU | Meta Audience Insights | AI |

### Bước 1.5 — Competitor Price & Offer Capture
Cho mỗi niche được validate (hoặc shortlist), bắt **giá bán & offer của đối thủ** để bàn giao anh Định (Merch SOP-MER-003) định giá cạnh tranh.

| I | C | O | M |
|---|---|---|---|
| Validated/shortlist niche + competitor list (Gearbunch + tương tự) | Source whitelist (Meta Ad Library free + AdSpy/BigSpy) | Competitor price table per niche | AI niche-research |

| # | Hành động | Công cụ | Owner |
|---|-----------|---------|-------|
| 1.5.1 | Pull competitor list cho niche (Gearbunch + shop AOP legging tương tự đang chạy ad) | Meta Ad Library / AdSpy | AI |
| 1.5.2 | Mở landing page từ ad → ghi **price range** (min/max giá bán SP đối thủ) | Landing page đối thủ | AI |
| 1.5.3 | Ghi **bundle/offer/discount** (vd 2-for-$80, free-ship, %off) | Landing page + ad copy | AI |
| 1.5.4 | Ghi **ad longevity** (SP/creative chạy lâu nhất = winner) qua ngày bắt đầu ad trên Meta Ad Library | Meta Ad Library | AI |
| 1.5.5 | Tổng hợp `competitor price table per niche`, kèm evidence + ngày capture | — | AI |

> **GIỚI HẠN (phải ghi rõ):** LẤY ĐƯỢC giá bán (landing page), bundle/offer/discount, ad longevity (qua Meta Ad Library free + AdSpy/BigSpy). **KHÔNG lấy được** ad spend / CPM / bid thật của đối thủ — Meta KHÔNG công khai → chỉ ước lượng tương đối (suy từ ad longevity + số creative), tuyệt đối KHÔNG bịa con số spend.

### Bước 2 — Scoring & ranking
| I | C | O | M |
|---|---|---|---|
| Raw signal dataset | Scoring rubric (demand 40 / competition 25 / margin-fit 20 / IP-risk 15) | Scored niche table | AI niche-research |

| # | Hành động | Output |
|---|-----------|--------|
| 2.1 | Tính demand/competition/margin-fit/IP-risk | Score 0–100 |
| 2.2 | Loại niche score < 70 hoặc audience < 500k | Shortlist |
| | **Rationale ngưỡng:** audience ≥ 500k = đủ rộng để FB-ads tìm winner ở CPA mục tiêu < $20 (US+EU); score ≥ 70/100 = mức demand tối thiểu để vào pipeline. *Đây là giả định ban đầu — chưa có data thật, đánh dấu `need_review` để review-lại sau 30 ngày dựa trên CPA/ROAS thực tế.* | Ghi chú |
| 2.3 | Rank shortlist theo score | Ranked list |

### Bước 3 — IP pre-flag & xuất validated list
| I | C | O | M |
|---|---|---|---|
| Ranked list | IP pre-flag rule | Validated niche list + pre-flag | AI + human review |

| # | Hành động | Output |
|---|-----------|--------|
| 3.1 | Quét tên niche/term vs known TM/brand | Pre-flag tag |
| 3.2 | Ghi `validated_niche_list` ra `output/` | File handoff |
| 3.3 | Human review sample 20% | Approve/reject |

## 4. Phân Nhánh & Xử Lý Đặc Biệt

| Tình huống | Xử lý |
|-----------|-------|
| Audience < 500k nhưng score demand cao | Đưa vào "micro-niche watchlist", không scale ngay |
| IP pre-flag = HIGH | Bắt buộc đẩy thẳng PRD-004 trước khi design |
| Niche trùng SP đã có trong 3.200 SP | Đánh dấu "refresh/iterate", không tạo mới |
| Data Trends rỗng (niche quá mới) | Hạ confidence, gắn need_review, chờ tín hiệu ads |

## 5. Checklist

**Quality Gate**

| Tiêu chí | SLI | SLO | Check Method | Pass |
|----------|-----|-----|-------------|:----:|
| Đủ số niche/tuần | # validated niche/tuần | ≥ 3 | Đếm file output | ☐ |
| Audience đủ lớn | % niche audience ≥ 500k | ≥ 90% | Meta export | ☐ |
| Demand validity | % niche score ≥ 70 | 100% (đã lọc) | Scoring table | ☐ |
| IP pre-flag coverage | % niche được pre-flag check | 100% | Pre-flag log | ☐ |
| Competitor price captured | % niche validated có competitor price table | ≥ 80% | Competitor price table + evidence | ☐ |

**Prevention Measures**

| Rủi ro | Phòng ngừa |
|--------|-----------|
| Validate niche "ảo" (ad cũ, đã chết) | Lọc ad-age < 90 ngày |
| Bỏ sót IP risk | Pre-flag bắt buộc trước handoff |
| Trùng lặp SP | Dedupe vs catalog 3.200 SP |

## 6. Tài Nguyên & Tham Chiếu

- **Upstream:** [Company OKR O3](../../../00-company/okr_company-001_company-okr_v1.0_2026-06-23.md)
- **Downstream:** [SOP-PRD-002](../../analyze-trend/template/sop_prd-002_trend-seasonal_v1.0_2026-06-23.md) · [SOP-PRD-003](../../design-aop/template/sop_prd-003_aop-design_v1.0_2026-06-23.md)
- **Handoff Merch:** competitor price table per niche → **SOP-MER-003** (variant-pricing, anh Định) làm input định giá cạnh tranh (đặt giá trên contribution margin, tham chiếu price range đối thủ).
- **AI Skill:** vibe-opc-pod-product-niche-research
- **Rules:** [../../_rules/README.md](../../_rules/README.md)

## 7. Lịch Sử Thay Đổi

| Phiên bản | Ngày | Thay đổi | Tác giả |
|-----------|------|----------|---------|
| 1.0 | 2026-06-23 | Khởi tạo SOP | Company Architect |
| 1.0 | 2026-06-23 | Bổ sung Bước 1.5 "Competitor Price & Offer Capture" (A: giá bán/bundle/offer; B: ad longevity) qua Meta Ad Library free + AdSpy; thêm output competitor price table + Quality Gate + handoff anh Định (SOP-MER-003) | Company Architect |
