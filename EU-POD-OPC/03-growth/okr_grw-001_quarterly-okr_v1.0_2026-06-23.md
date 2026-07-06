# OKR — 03-growth · Q3 2026

**Dept:** grw · **Set bởi:** OPC · **Ngày:** 2026-06-23
**Align:** Company **O1** (doanh số ổn định & có lãi)

> v2.0 Evidence-bound: mọi target có evidence + confidence_score + need_review. Stretch (hiệu suất/tự-động-hóa, giữ trần 500tr) → need_review = true → [review-queue](../00-company/output/review-queue.md).

---

## COMMITTED OKR (target 100%)

### O1-grw: Quảng cáo kéo doanh số có lãi
| KR | Metric | Baseline | Target | KRI |
|----|--------|----------|--------|-----|
| KR1 | Blended ROAS | ~2.2 | **≥ 2.5** | blended_roas |
| KR2 | CPA | ~$22 | **< $20** | cpa |
| KR3 | Revenue do ads/tháng | ~280tr | **đóng góp 500tr (O1)** | revenue_from_ads |

**Evidence:** ROAS 2.5 = ngưỡng hòa vốn+lãi với gross margin AOP ~45–55% (đồng bộ Company OKR KR2). CPA <$20 từ historical CPA ~$22 cần siết qua creative+targeting. *confidence: 0.78 · need_review: false*

### O2-grw: Bảo vệ kênh & signal
| KR | Metric | Baseline | Target | KRI |
|----|--------|----------|--------|-----|
| KR1 | BM ban "sập toàn bộ" | — | **0** | bm_ban_total |
| KR2 | CAPI Event Match Quality | ~5.5 | **≥ 6.0** | capi_emq |
| KR3 | Email deliverability | ~96% | **≥ 98%** | email_deliverability |

**Evidence:** BM 5-tier (SOP-GRW-002) thiết kế để 1 account bị flag không sập kênh; EMQ ≥6 cần để optimize đúng. *confidence: 0.8 · need_review: false*

---

## STRETCH OKR (hướng hiệu suất/tự-động-hóa — 70% = success)

> **Thay đổi (Owner chốt):** bỏ moonshot doanh thu x10 (5 tỷ / 100 winner) — Owner giữ trần doanh thu **500tr/tháng**. Stretch chuyển sang **hiệu suất vận hành & tự động hóa** TRONG khuôn khổ 500tr, không tăng cấp doanh số.

### O3-grw: Tự động hóa & hiệu suất ads (giữ trần 500tr/tháng)
| KR | Metric | Baseline | Stretch Target | Approach Difference |
|----|--------|----------|----------------|---------------------|
| KR1 | % campaign chạy auto-optimize (pipeline test→scale/kill theo ngưỡng, không can thiệp tay) | ~20% | **≥ 70%** | Rule-based scale/kill (SOP-GRW-002) + alert tự động (SOP-GRW-004), giảm thao tác thủ công |
| KR2 | Blended CPA | ~$22 | **giảm về ≤ $15** | UGC creative library + targeting tốt hơn hạ CPA, KHÔNG tăng budget; tăng lãi trên cùng doanh số |
| KR3 | Tỷ lệ winner giữ Blended ≥ BE-ROAS sau scale | baseline 30 ngày | **≥ 80%** | Neo break-even per-SKU (unit-economics), chống scale lãi ảo |

**Ràng buộc capacity (lý do giữ trần, không x10):**
- **Cashflow fund winner:** vốn xoay để scale winner có hạn → không thể đẩy budget đột biến lên mốc 5 tỷ.
- **Số BM/ad account:** BM 5-tier hiện hữu chỉ đủ chạy số batch promote giới hạn song song; mở rộng x10 cần nhiều BM verified (rủi ro ban + thời gian warm-up).

**Evidence:** Không có benchmark nội bộ cho target hiệu suất mới (auto-optimize %, CPA $15) → cần đo baseline 30 ngày. *confidence: 0.4 · need_review: **true*** → [review-queue](../00-company/output/review-queue.md)

---

## Alignment
| Dept KR | → Company | Contribution |
|---------|----------|--------------|
| O1-grw (ROAS/CPA/revenue) | → O1 (KR1, KR2) | Cao |
| O2-grw (BM/CAPI/email) | → O1 (bảo vệ traffic) | Trung bình-cao |
| O3-grw (auto-optimize, hạ CPA, giữ trần 500tr) | → O3 | Stretch |
