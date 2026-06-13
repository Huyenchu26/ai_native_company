# SOP-MER-006 — Promote-set theo đợt (chọn winner từ catalog có sẵn)

**Department:** Merchandising (mer) · **AI Worker:** Catalog-Sync AI (R) · **Loại:** OPERATIONAL · **v1.0** · **2026-06-11** · **ACTIVE**

> Store DAKOfits có **~3.200 SP AOP đa niche đã live**. Không chạy ads dàn trải. Mỗi đợt **chỉ chọn vài SP** (promote set) để tối ưu page + creative + ads, test → scale winner. SOP này chuẩn hóa cách **chọn, kích hoạt, theo dõi, luân chuyển** promote set.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Chọn promote set nhỏ (5–10 SP) mỗi đợt từ catalog có sẵn, tối ưu & đẩy ads tập trung, đo hiệu quả, giữ winner / loại loser. |
| **Phạm vi** | Curation + điều phối promote (KHÔNG tạo SP mới — đó là PRD-003/MER-002). Đa niche. |
| **Trigger** | Đầu mỗi đợt (tuần/2 tuần/mùa vụ) hoặc khi winner cũ bão hòa. |

### IPO
| | |
|---|---|
| **Input** | `catalog-register_live-products.csv` (3.200 SP phân loại), tín hiệu mùa vụ (calendar PRD-002), data ads đợt trước (GRW-002), niche signal (PRD-001) |
| **Control** | Mỗi đợt 5–10 SP · ưu tiên niche có demand + đúng mùa · margin đạt floor · GPSR sẵn (đơn EU) trước khi đẩy ads |
| **Output** | **Promote set** (đánh dấu trong register: `PromoteStatus`, `PromotePhase`) + brief handoff Product Page/Creative/Ads |
| **Mechanism** | Catalog-Sync AI + register CSV + ShopBase + phối hợp Niche Research / Product Page / FB Creative / FB Ads |

## 2. Tiêu chí chọn promote set (Knowledge)
| Tiêu chí | Ưu tiên |
|---|---|
| **Mùa vụ / sự kiện** | Sát sự kiện (vd July 4th → Patriotic; Giáng sinh → Holiday) — launch trước 3–4 tuần để ads ramp |
| **Demand niche** | Niche có audience FB lớn + bằng chứng bán (PRD-001/002); né niche đã bão hòa |
| **Hiệu quả lịch sử** | Giữ winner ROAS ≥2.5 / CPA <$20 đợt trước; loại loser |
| **IP/TM sạch** | Né title dính TM/brand/celebrity (vd tên chính trị gia, nhân vật) — Compliance |
| **GPSR-ready (EU)** | Có clearance nếu định bán EU |
| **Đa dạng test** | 1 đợt nên có 2–3 niche để so sánh, không bỏ trứng 1 giỏ |

## 3. RACI
| Hoạt động | Founder | Catalog-Sync | Niche Research | Product Page | FB Creative | FB Ads | Compliance |
|---|---|---|---|---|---|---|---|
| Chốt promote set | **A** | **R** | C | I | I | C | C |
| Tối ưu page SP đã chọn | I | C | - | **R** | - | - | C (GPSR/IP) |
| Creative cho SP đã chọn | I | I | - | C | **R** | C | C (Meta policy) |
| Chạy & tối ưu ads | A | I | C | - | C | **R** | C |

## 4. Đầu vào
- [ ] Register cập nhật · [ ] Calendar mùa vụ (PRD-002) · [ ] Data ads đợt trước (GRW-004) · [ ] Niche signal (PRD-001)

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Lọc ứng viên | Lọc register theo niche/mùa/giá → shortlist 15–20 SP | [AI AUGMENT] | Bám tiêu chí §2, không chọn cảm tính |
| 5.2 | Sàng IP/TM + GPSR | Loại SP title rủi ro TM; check GPSR nếu bán EU | [AI WORKFORCE] | Né ban ads / GPSR block |
| 5.3 | Chốt set 5–10 SP | Đề xuất → **Founder duyệt** | [HUMAN-AI] | Founder = Approver |
| 5.4 | Đánh dấu register | Set `PromoteStatus=Active`, `PromotePhase=<đợt>` cho SP đã chọn | [AI WORKFORCE] | Nguồn sự thật duy nhất |
| 5.5 | Handoff tối ưu | → Product Page AI (CRO/upsell/GPSR) → FB Creative AI (creative) → FB Ads (campaign) | [AI WORKFORCE] | Brief rõ angle/niche/mùa |
| 5.6 | Theo dõi & luân chuyển | Sau đợt: winner→`Scaling`, loser→`Paused`; cập nhật register | [AI AUGMENT] | Không để ads chạy SP lỗ |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Kích thước set | 5–10 SP/đợt | 100% | ☐ |
| 2 | Phù hợp mùa/demand | có lý do data cho mỗi SP | 100% | ☐ |
| 3 | IP/TM sạch | 0 title rủi ro | 100% | ☐ |
| 4 | GPSR (nếu bán EU) | clearance present | 100% | ☐ |
| 5 | Đánh dấu register | PromoteStatus + Phase đủ | 100% | ☐ |
| 6 | Handoff đủ 3 nhánh | Page + Creative + Ads nhận brief | 100% | ☐ |

## 7. Output & Downstream
- **Lưu:** register cập nhật (`PromoteStatus`/`PromotePhase`) + `./output/promote-set_<đợt>_DONE.md` (lý do chọn + KPI mục tiêu) → archive/
- **Downstream:** MER-001 (tối ưu page), GRW-005 (creative), GRW-002 (ads), GRW-004 (đo hiệu quả → feedback đợt sau)

## 8. Vòng lặp luân chuyển (mỗi đợt)
```
Register (3.200 SP) → [5.1 lọc] → shortlist → [5.3 Founder duyệt] → Promote set (5–10)
        ▲                                                              │
        │ winner giữ/scale · loser pause                               ▼
   [5.6 cập nhật] ◄────── data ads (GRW-004) ◄──── Page+Creative+Ads tối ưu (5.5)
```

## 9. Phụ lục
Register: ../output/catalog-register_live-products.csv · Calendar: ../../../01-product-studio/trend-seasonal-scan/ · Ads: ../../../03-growth/ · GPSR: ../../../05-backoffice/gpsr-compliance/ · Spec: ../../product-page/template/product-spec-template_v1.0.md
