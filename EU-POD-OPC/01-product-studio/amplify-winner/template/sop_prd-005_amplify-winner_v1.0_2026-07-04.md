# SOP-PRD-005 — Nhân Winner (Amplify Winner)

**Dept:** 01-product-studio (`prd`) · **Version:** v1.0 · **Ngày:** 2026-07-04
**Responsible:** OPC (điều phối) · **Support AI:** `vibe-eu-opc-prd-niche-research` (chấm niche lân cận) + `vibe-eu-opc-prd-design` (design + IP/TM gate)

---

> **Lý do tồn tại:** DAKOfits là mô hình POD AOP đa-niche — giá trị lớn nhất là **biến 1 SP thắng thành cụm SP mới cùng mạch niche/design**. Trước SOP này vòng feedback bị **hở**: winner được scale ads nhưng KHÔNG có đường về Product Studio để nhân bản (MER-006 chỉ ghi 1 dòng informal "nhân design lân cận — báo phòng 01"). SOP-PRD-005 **khép vòng**: winner-registry → chấm niche/design lân cận → design → IP/TM gate → đẩy vào đợt promote kế.

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | `_shared/winner-registry.json` record `status=WINNER` (do Growth ghi khi campaign SCALE); tín hiệu MER-006 §4 nhánh winner |
| **Control (C)** | Trục nhân hợp lệ; candidate score ≥ 70/100 + audience ≥ 500k; IP/TM pre-flag; gate cứng "no IP/TM clearance → no listing" (conservative REJECT khi nghi trademark) |
| **Output (O)** | 3–5 candidate niche/design mới đã pass IP/TM → handoff Merch (đợt promote kế); record winner cập nhật `amplification[]` + `status=AMPLIFIED` |
| **Mechanism (M)** | OPC + niche-research AI + design AI + winner-registry |
| **Upstream** | 03-growth (ghi winner-registry) · 02-merchandising (MER-006 §4 báo winner) |
| **Downstream** | PRD-003 (design) → PRD-004 (IP/TM gate) → 02-merchandising (đợt promote kế MER-006) |

---

## 1. Tổng Quan

Khi 1 SP đạt **WINNER** (định nghĩa chuẩn tại [unit-economics](../../../_shared/unit-economics.md): `blended_roas ≥ break_even_roas` theo SKU/market **VÀ** `cpa < $20`, ổn định ≥ 3–5 ngày), Growth ghi record vào `_shared/winner-registry.json`. SOP này đọc winner đó và **nhân bản có kiểm soát** thành 3–5 SP mới theo 3 trục, chạy qua đúng luồng design + IP/TM gate hiện có, rồi feed vào đợt promote kế. Đây là **nửa vòng còn hở** của learn-fast loop, nay khép kín.

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Niche-Research AI | Design AI | 03-Growth | 02-Merch |
|-----------|-----|-------------------|-----------|-----------|----------|
| Phát hiện winner (ghi registry) | I | I | I | **R** | C |
| Chọn trục nhân + chấm candidate lân cận | A | **R** `[AI WORKFORCE]` | C | I | I |
| Design AOP candidate | A | C | **R** `[AI WORKFORCE]` | I | I |
| IP/TM clearance (gate) | A | I | **R** `[AI WORKFORCE]` | I | I |
| Cập nhật `amplification[]` + status | **A/R** | C | C | C | I |
| Đẩy cụm SP mới vào đợt promote | A | I | I | I | **R** |

`[AI WORKFORCE]` = `vibe-eu-opc-prd-niche-research` + `vibe-eu-opc-prd-design`.

## 3. Quy Trình

### Bước 1 — Đọc winner & chọn trục nhân
| ICOM | Nội dung |
|------|----------|
| I | Record `status=WINNER` từ `_shared/winner-registry.json` |
| C | 3 trục nhân hợp lệ |
| O | Trục nhân + brief candidate |
| M | OPC + Niche-Research AI |

**3 trục nhân winner** (khớp enum `amplification.axis` trong schema):

| Trục | `axis` | Ý nghĩa | Ví dụ |
|------|--------|---------|-------|
| Cùng niche, khác design | `same_niche_new_design` | Giữ niche thắng, đổi loại AOP (tile→watercolor/funny/mandala) | Winner "German Shepherd tile" → bản watercolor + funny |
| Cùng design, niche lân cận | `same_design_adjacent_niche` | Giữ style design, sang niche cùng audience cluster | Winner "German Shepherd" → Belgian Malinois, Rottweiler (cùng dog-mom cluster) |
| Cùng cả hai, khác market | `same_both_new_market` | Nhân sang market chưa đánh — LƯU Ý BE-ROAS khác (EU ~5.3) | Winner US → thử EU nhưng chỉ khi giá EU đủ margin (unit-economics §4) |

### Bước 2 — Chấm candidate lân cận (niche-research)
| ICOM | Nội dung |
|------|----------|
| I | Trục nhân + winner niche/design |
| C | Score ≥ 70/100, audience ≥ 500k, IP/TM pre-flag |
| O | 3–5 candidate đã chấm |
| M | Niche-Research AI |

| Hành động | Ai |
|-----------|-----|
| Sinh 3–5 candidate theo trục → demand scoring + audience sizing (SOP-PRD-001) | Niche-Research AI `[AI WORKFORCE]` |
| Loại candidate score < 70 hoặc audience < 500k | Niche-Research AI |
| IP/TM pre-flag theo tên niche/breed (conservative) | Niche-Research AI |

### Bước 3 — Design + IP/TM gate (luồng chuẩn)
| ICOM | Nội dung |
|------|----------|
| I | Candidate đã chấm |
| C | 300 DPI + seamless QC 360°; gate "no IP/TM clearance → no listing" |
| O | Design print-ready + IP-clearance log |
| M | Design AI |

| Hành động | Ai |
|-----------|-----|
| AOP design print-ready 300 DPI (SOP-PRD-003) | Design AI `[AI WORKFORCE]` |
| IP/TM clearance USPTO TESS + EUIPO (SOP-PRD-004) — **REJECT khi nghi ngờ** | Design AI `[AI WORKFORCE]` |

### Bước 4 — Ghi ngược registry & handoff Merch
| ICOM | Nội dung |
|------|----------|
| I | Candidate đã CLEAR |
| C | Đóng vòng feedback |
| O | `amplification[]` cập nhật; cụm SP → đợt promote kế |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Ghi `amplification[]` (child_sku/brief, axis, created_date) vào record winner | OPC |
| Set `status=AMPLIFIED`; `updated_at` registry | OPC |
| Bàn giao cụm candidate CLEAR → 02-merch đưa vào đợt promote kế (MER-006) | OPC |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| Winner mạnh (blended ≥ 1.3× BE-ROAS) | Nhân đủ 3 trục, ưu tiên `same_design_adjacent_niche` (rẻ & nhanh nhất) |
| Winner biên (blended vừa chạm BE-ROAS) | Chỉ nhân 1 trục `same_niche_new_design`, test nhỏ trước |
| Winner ở EU | Cẩn trọng `same_both_new_market` sang US; kiểm BE-ROAS trước khi nhân ngược |
| Candidate IP/TM nghi ngờ | REJECT candidate đó, không listing (gate cứng) |
| Winner đã `FATIGUED` | Không nhân thêm; đóng record |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| Amplify SLA (winner ghi registry → candidate handoff) | ≤ 7 ngày | timestamp registry vs handoff |
| Candidate/winner | 3–5 candidate/winner | count `amplification[]` |
| IP/TM clearance rate candidate | 100% CLEAR trước listing | clearance log |
| Amplified coverage | ≥ 80% winner `status=WINNER` được xử lý ≤ 14 ngày | registry audit |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Nhân winner "lãi ảo" (blended < BE-ROAS) | Chỉ nhận record đúng định nghĩa winner (unit-economics) |
| Nhân sang market lỗ (EU giá thấp) | Kiểm BE-ROAS market đích trước khi `same_both_new_market` |
| Trademark vi phạm khi nhân breed/niche | IP/TM pre-flag (bước 2) + gate cứng PRD-004 |
| Winner bị bỏ quên | Amplified coverage SLO + registry audit |

## 6. Tài Nguyên & Links

- Template: `amplify-winner/template/`
- Registry: [`_shared/winner-registry.json`](../../../_shared/winner-registry.json) · Schema: [`_shared/winner-registry.schema.json`](../../../_shared/winner-registry.schema.json)
- Định nghĩa winner: [unit-economics](../../../_shared/unit-economics.md)
- Upstream: 03-growth [SOP-GRW-002](../../../03-growth/run-fb-ads/template/sop_grw-002_fb-ads_v1.0_2026-06-23.md) (ghi registry) · 02-merch [SOP-MER-006](../../../02-merchandising/promote-batch/template/sop_mer-006_promote-batch_v1.0_2026-06-23.md) §4
- Downstream: [SOP-PRD-003](../../design-aop/template/) (design) → [SOP-PRD-004](../../clear-ip/template/) (IP/TM gate) → 02-merchandising (MER-006)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-07-04 | Khởi tạo SOP nhân winner — khép vòng feedback Growth → Product Studio qua winner-registry |
