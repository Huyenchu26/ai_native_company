# KRI: Phòng 02-Merchandising — Key Result Indicators

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0
**Mục đích:** Leading/lagging indicators báo sớm rủi ro trước khi KPI/OKR trượt.

---

## 1. Leading KRI (báo sớm — đo liên tục)

| KRI | Định nghĩa | Ngưỡng cảnh báo | Hành động khi vượt ngưỡng |
|-----|-----------|-----------------|---------------------------|
| `gpsr_label_rate` | % SP EU có nhãn GPSR trên PDP | < 100% | **Block publish**, escalate phòng 05 ngay |
| `sync_accuracy` | % field khớp giữa ShopBase ↔ provider | < 99% | Re-sync, QC root cause |
| `gross_margin` | (Giá bán − cost) / giá bán theo variant | < 45% | Chặn publish, re-price/đổi provider |
| `cro_completeness` | % checklist CRO 12 elements có mặt | < 95% | Trả Product-Page AI bổ sung |
| `provider_stock_status` | Variant out-of-stock tại provider | bất kỳ variant OOS | Ẩn variant / đổi provider EU↔US |
| `time_to_publish` | Giờ từ cleared → live | > 48h | Review bottleneck pipeline |

## 2. Lagging KRI (kết quả — đo theo đợt/tuần)

| KRI | Định nghĩa | Ngưỡng | Liên kết |
|-----|-----------|--------|----------|
| `batch_winner_rate` | % SP/đợt đạt ROAS≥2.5 sau ads | < 20% | OKR O3, feedback Growth |
| `upsell_attach` | % đơn có bundle sports-bra | < 10% | OKR O2-KR3 |
| `listing_defect_rate` | % SP bị Growth/CX báo lỗi listing | > 2% | Quality MER-004 |
| `publish_throughput` | # SP publish-ready / tuần | < 40 | OKR O3-KR1 |

## 3. Risk → KRI mapping

| Rủi ro | KRI cảnh báo | Mitigation |
|--------|-------------|-----------|
| Publish SP EU thiếu nhãn GPSR (phạt EU) | `gpsr_label_rate` | Gate cứng, không bypass |
| Bán dưới giá vốn / margin âm | `gross_margin` | Pricing floor 45% |
| Catalog lệch giá/variant → đơn lỗi | `sync_accuracy` | QC MER-004 |
| Provider hết hàng → đơn treo | `provider_stock_status` | Dual provider US+EU |
| Đợt promote toàn loser → đốt ads | `batch_winner_rate` | Cut sớm, đọc kết quả Growth |

## 4. Cadence đo

| Tần suất | KRI |
|----------|-----|
| Mỗi SP/publish | gpsr_label_rate, gross_margin, cro_completeness, sync_accuracy |
| Hàng ngày | provider_stock_status, time_to_publish |
| Mỗi đợt promote | batch_winner_rate, upsell_attach, listing_defect_rate |
| Hàng tuần | publish_throughput |
