# Sample Input — Niche Seed List (DAKOfits, SOP-PRD-001)

Task input mẫu để smoke-test. Đặt ở `input/` khi chạy thật. Dữ liệu giả lập, dùng để test pipeline.

## Task
- **task_id:** PRD-001-2026-W26-001
- **request:** Validate niche seed list cho đợt promote tuần W26, US+EU, AOP leggings/activewear.
- **target_market:** US + EU
- **deadline:** 2026-06-27

## Niche seed list + raw signal

| # | niche | category | AdSpy ad-volume (ad-age<90d) | Meta audience US+EU | Google Trends (12m) | catalog match? |
|---|-------|----------|------------------------------|---------------------|---------------------|----------------|
| 1 | German Shepherd | pet | 320 ad sống, đa seller | 4.200.000 | ổn định, +nhẹ Q4 | có (đã bán) |
| 2 | Nurse | profession | 580 ad sống | 6.800.000 | evergreen, peak Nurses Week (5) | không |
| 3 | Pickleball | sport | 95 ad sống, đang tăng | 1.900.000 | tăng mạnh 12 tháng | không |
| 4 | Pisces zodiac | zodiac | 40 ad sống | 720.000 | peak quanh Feb–Mar | không |
| 5 | Border Collie | pet | 30 ad sống | 380.000 | bằng phẳng | không |
| 6 | Manchester United | sport/club | 200 ad sống | 9.000.000 | cao quanh mùa giải | không |
| 7 | Halloween Cat | pet/seasonal | 60 ad sống (tăng từ T8) | 2.500.000 | peak rõ cuối T10 | không |

## Ghi chú nguồn (evidence seed)
- AdSpy export: `2026-06-22_adspy_w26.csv` (đã lọc ad-age < 90 ngày).
- Meta Audience Insights: stack interest theo từng niche, geo = US+EU.
- Google Trends: `2026-06-22_trends_12m.csv`, 12 tháng gần nhất.

## Kỳ vọng xử lý (để đối chiếu test)
- **#2 Nurse, #1 German Shepherd, #7 Halloween Cat**: score cao + audience ≥500k.
- **#1 German Shepherd**: trùng catalog → `refresh-iterate`.
- **#3 Pickleball**: demand tăng nhưng audience 1.9M ok → ứng viên validated.
- **#4 Pisces (720k)**: borderline; **#5 Border Collie (380k < 500k)** → watchlist.
- **#6 Manchester United**: `ip_risk_flag = HIGH` (club/TM) → need_review=true, đẩy PRD-004.
- **#7 Halloween Cat**: seasonal, peak cuối T10 → design_deadline ≥ 6 tuần trước (đầu T9).
