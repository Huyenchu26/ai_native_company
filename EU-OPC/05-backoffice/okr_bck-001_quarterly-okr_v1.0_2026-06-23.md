# OKR — 05-Backoffice (bck) · Q3 2026

**Quý:** Q3 2026 · **Set bởi:** Owner · **Ngày:** 2026-06-23
> v2.0 Evidence-bound: mọi target có evidence + confidence_score; stretch (solo-capacity/tự-động-hóa, KHÔNG x10 doanh số) → mốc chưa kiểm chứng giữ need_review = true. Target doanh thu trần = 500tr VND/tháng (~$20k), không vượt.

---

## COMMITTED OKR (target 100%)

### O1: Đúng luật tuyệt đối — không rủi ro pháp lý
| KR | Metric | Baseline | Target | KRI | → Company |
|---|---|---|---|---|---|
| KR1: GPSR clearance trước EU publish | % SP EU cleared | — | **100%** | gpsr_clearance_rate | O2 |
| KR2: VAT filing on-time | % kỳ OSS/IOSS đúng hạn | — | **100%** | vat_ontime_rate | O2 |
| KR3: GDPR breach notify | % breach notify ≤72h | — | **100%** | breach_response_time | O2 |

**Evidence:** Gate cứng SOP-BCK-004 + nghĩa vụ legal OSS/IOSS & GDPR Art.33. Đây là compliance SLO = 100% (error budget 0%, ngoại lệ legal). *confidence: 0.9 · need_review: false*

### O2: Vận hành có lãi & minh bạch tài chính
| KR | Metric | Baseline | Target | KRI | → Company |
|---|---|---|---|---|---|
| KR1: Net margin | Net profit / revenue | ~15% | **≥ 20%** | net_margin | O1 |
| KR2: Bookkeeping accuracy | % giao dịch khớp | ~99% | **≥ 99.9%** | bookkeeping_accuracy | O1 |
| KR3: CEO brief on-time | % tháng có brief ≤ ngày 6 | — | **100%** | brief_ontime | O1 |

**Evidence:** Net margin 20% = Company O1 KR3. Accuracy 99.9% từ API pull + 4-eyes (SOP-BCK-001). *confidence: 0.8 · need_review: false*

### O3: AI Workforce khỏe & hiệu quả chi phí
| KR | Metric | Baseline | Target | KRI | → Company |
|---|---|---|---|---|---|
| KR1: AI worker uptime | % uptime trung bình 12 worker | ~97% | **≥ 99%** | ai_worker_uptime | O1, O2 |
| KR2: Weekly report on-time | % tuần có report | — | **100%** | workforce_report_ontime | — |

**Evidence:** SOP-BCK-006 monitoring + cron. *confidence: 0.75 · need_review: false*

---

## STRETCH OKR (SOLO-CAPACITY — tự động hóa & hiệu suất, KHÔNG đẩy doanh số · 70% = success)

> Owner đã chốt mục tiêu **500tr VND/tháng (~$20k)** và vận hành **solo**. Stretch KHÔNG phải moonshot x10 volume/doanh thu — mà là **tự động hóa để 1 người (+ AI workforce) gánh được tải hiện tại với ít thao tác tay nhất**. Mọi KR đo *hiệu suất/độ tự động*, không đo doanh số vượt 500tr.

### O4: Zero-touch compliance + finance pipeline (giải phóng thời gian Owner)
| KR | Metric | Baseline | Stretch Target | Approach Difference |
|---|---|---|---|---|
| KR1: SP EU auto-cleared không human-review | % | ~0% | **90%** | Không "review nhanh hơn" — mà breed-watchlist + RP registry + label generator tự động PASS, human chỉ xử lý exception |
| KR2: P&L + VAT draft auto-generated | thời gian khóa kỳ | ~3 ngày | **< 2 giờ** | Pipeline pull→ghi sổ→profit→VAT→brief chạy end-to-end, Owner chỉ ký |
| KR3: Owner manual-touch / tuần | giờ thao tác tay vận hành backoffice | chưa đo | **giảm ≥ 70%** | Đo capacity solo: tự động hóa cron/trigger để Owner chỉ approve, không vận hành tay |

**Evidence:** Chưa có benchmark nội bộ cho mức tự động hóa này (KR3 chưa có baseline đo). *confidence: 0.35 · need_review: **true*** → review-queue

---

## Alignment
| bck OKR | → Company | Contribution |
|---|---|---|
| O1 (GPSR/VAT/GDPR 100%) | → O2 | Cao (gate cứng) |
| O2 (margin/accuracy) | → O1 | Cao |
| O3 (workforce uptime) | → O1, O2 | Trung bình |
| O4 (zero-touch / solo-capacity) | → O3 company (hiệu suất, không scale doanh số) | Stretch |
