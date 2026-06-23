# OKR — Fulfillment & CX (ful) · Q3 2026

**Dept:** 04-fulfillment-cx · **Set bởi:** OPC · **Ngày:** 2026-06-23
**Align:** Company **O2** (Vận hành đúng luật & đúng hạn)

> v2.0 Evidence-bound: mọi target có evidence + confidence_score + need_review. Stretch (x10) → need_review = true.

---

## COMMITTED OKR (target 100%)

### O-FUL-1: Giao đơn đúng hạn, không rò rỉ
| KR | Metric | Baseline | Target | KRI | SOP |
|---|---|---|---|---|---|
| KR1 On-time routing | % đơn route ≤24h | ~95% | **≥ 98%** | ontime_routing | FUL-002 |
| KR2 Tracking gửi khách | % đơn ship có tracking ≤12h | ~90% | **≥ 99%** | tracking_sent_rate | FUL-002 |
| KR3 Verification coverage | % đơn paid verify trong ngày | ~95% | **100%** | verify_coverage | FUL-001 |

**Evidence:** Baseline on-time ~95% lấy từ Company OKR O2/KR2 (2026-06-23). Target 98% = đóng góp trực tiếp Company O2. *confidence: 0.8 · need_review: false*

### O-FUL-2: Support EN giữ rating cao
| KR | Metric | Baseline | Target | KRI | SOP |
|---|---|---|---|---|---|
| KR1 First response | First response time | — | **≤ 2h** (SLA khách ≤4h) | first_response_time | FUL-003 |
| KR2 Resolution rate | % ticket resolved ≤24h | — | **≥ 90%** | resolution_rate | FUL-003 |
| KR3 CSAT | CSAT post-resolution | — | **≥ 4.0 / 5** | csat | FUL-003/004 |
| KR4 Refund rate | refunds / orders | — | **≤ 3%** | refund_rate | FUL-004 |

**Evidence:** Target chuẩn ngành POD CX (first response 2h, CSAT 4.0). Chưa có baseline nội bộ → đo từ Q3. *confidence: 0.65 · need_review: **true*** → review-queue.

---

## STRETCH OKR (MOONSHOT x10 — 70% = success)

### O-FUL-3: Zero-touch fulfillment & CX
| KR | Metric | Baseline | x10 Target | Approach Difference |
|---|---|---|---|---|
| KR1 Auto-route không cần OPC | % đơn route hoàn toàn tự động | ~70% | **≥ 99%** | Không "làm nhanh tay hơn" — mà luật hóa toàn bộ exception (fraud, OOS, address) để AI tự quyết; OPC chỉ chạm < 1% đơn |
| KR2 Auto-resolved ticket | % ticket AI tự đóng | ~60% | **≥ 95% với CSAT ≥4.0** | Template EN + size-fit predictor + proactive WISMO trước khi khách hỏi |
| KR3 Refund rate | refunds/orders | 3% | **≤ 1%** | Diệt root cause: size predictor, ad-expectation alignment với 03-growth, provider QC |

**Evidence:** Không có benchmark nội bộ cho mốc x10 zero-touch. *confidence: 0.35 · need_review: **true*** → review-queue.

---

## Alignment
| Dept OKR | → Company OKR | Contribution |
|---|---|---|
| O-FUL-1 (on-time routing) | → O2/KR2 | **Cao** (chủ lực) |
| O-FUL-2 (CSAT, refund) | → O2 (vận hành đúng) + O1 (giữ LTV/margin) | Trung bình–Cao |
| O-FUL-3 (zero-touch) | → O3 (scale đa-niche cần fulfillment co giãn) | Stretch |

## Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo OKR Q3 |
