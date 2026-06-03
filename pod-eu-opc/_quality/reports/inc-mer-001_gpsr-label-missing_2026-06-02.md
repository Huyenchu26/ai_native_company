# Incident Report: INC-MER-001  [DUMMY]

**Ngày:** 2026-06-02 · **Severity:** HIGH · **SOP:** SOP-MER-001
**SLI vi phạm:** GPSR label present — Actual: thiếu trên 1 listing, SLO: 100%
**Phát hiện:** Audit tháng GPSR (SOP-BCK-004) · **Impact:** 1 listing rủi ro bị gỡ

## 1. Timeline
| Thời gian | Event |
|---|---|
| 01/06 | Listing "dog-dad-hoodie" publish |
| 02/06 | Audit GPSR phát hiện thiếu nhãn RP |

## 2. 5 Whys
1. Vì sao thiếu nhãn? → Bước 5.5 MER-001 bị bỏ qua
2. Vì sao bỏ qua? → Listing publish khi clearance BCK-004 chưa hoàn tất
3. Vì sao publish được? → Gate chưa chặn cứng ở thời điểm đó
4. Vì sao gate yếu? → Thiếu liên kết tự động giữa clearance log và publish
5. Root cause → **Hệ thống chưa enforce "no clearance = no publish" tự động**

## 3. Root Cause (systemic)
Quy trình cho phép publish trước khi GPSR clearance gắn vào listing.

## 4. Corrective Action
| # | Action | Type |
|---|---|---|
| 1 | Gỡ listing, bổ sung nhãn, publish lại | Corrective |
| 2 | MER-004 chặn cứng publish nếu thiếu GPSR clearance | Preventive |
| 3 | Cập nhật hard rule _rules backoffice | Systemic |

## 5. Prevention
Gate "no GPSR clearance → BLOCK publish" enforce tự động ở MER-001/MER-004.

## 6. Lessons
Compliance gate phải là **eliminate** (chặn cứng), không phải "detect late".
