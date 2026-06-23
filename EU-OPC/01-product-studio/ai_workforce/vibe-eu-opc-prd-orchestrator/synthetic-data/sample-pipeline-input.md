# Sample Pipeline Input — niche seed batch

Input mẫu cho `vibe-eu-opc-prd-orchestrator` (dùng với
`prompt/run-pipeline-prompt.md`). Dữ liệu tổng hợp, không phải khách thật.

---

## Pipeline meta
- `pipeline_id`: `PRD-PIPE-2026-06-23-batch01`
- Thị trường: US + EU · Nền tảng: ShopBase · Provider: Printify/PrintBase
- Đợt: 6 niche seed (đa-niche), mục tiêu ra cleared design handoff Merch.

## Niche seed batch
| # | niche_name | category | seed demand | ghi chú IP pre-flag |
|---|------------|----------|-------------|----------------------|
| 1 | German Shepherd | pet/dog-breed | cao | tên breed phổ thông — pre-flag LOW |
| 2 | Registered Nurse | profession | trung bình-cao | có thể đụng slogan TM — pre-flag MEDIUM |
| 3 | Scorpio Zodiac | zodiac | trung bình | LOW |
| 4 | Pickleball | sport/hobby | đang lên (seasonal) | LOW |
| 5 | Faith / Christian Cross | faith | ổn định | tránh logo nhà thờ cụ thể — pre-flag MEDIUM |
| 6 | "Bluey" Dog Theme | pet/cartoon | viral | **trùng franchise TM** — pre-flag HIGH (dự kiến REJECT) |

## Kỳ vọng pipeline (để đối chiếu test)
- Niche #1,#3,#4 → nhiều khả năng `validated` → design → có thể `CLEAR`.
- Niche #2,#5 → cần clearance kỹ (MEDIUM) → có thể `MODIFY`.
- Niche #6 → IP pre-flag HIGH, trùng franchise → **conservative REJECT**, escalate
  OPC, KHÔNG handoff.

## Ràng buộc
- Design type ∈ {tile, watercolor, funny, mandala}; 300 DPI; AOP 360° seamless.
- Clearance dual-market USPTO + EUIPO (G3).
- Chỉ design `CLEAR` mới vào `cleared_designs[]` và handoff
  `vibe-eu-opc-mer-orchestrator` (Merch đăng LIVE ShopBase TRƯỚC, rồi Growth).
