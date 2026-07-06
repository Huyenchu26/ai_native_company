# _rules — 01-Product Studio

**Ngày:** 2026-06-23 · **Dept:** prd · Hard gates, quality gates, escalation, decision authority.

## 1. Hard Gates (cứng — vi phạm = chặn)
| ID | Rule | Vị trí | Hệ quả khi vi phạm |
|----|------|--------|--------------------|
| G1 | **No IP/TM clearance → no listing** | PRD-004 | Chặn handoff sang 02-merch |
| G2 | **No 300 DPI → no print-ready** | PRD-003 | Design bị reject |
| G3 | **No dual-market lookup (USPTO+EUIPO) → not CLEAR** | PRD-004 | Status không được CLEAR |
| G4 | **AOP seam lộ → no handoff** | PRD-003 | Quay lại tạo seamless tile |

## 2. Quality Gates (operational, có error budget)
| Rule | SLO | Budget |
|------|-----|--------|
| AOP 360° pass | ≥ 98% | 2% |
| Audience qualified | ≥ 90% niche ≥ 500k | 10% |
| Design turnaround | ≤ 24h | — |
| Seasonal deadline hit | ≥ 95% | 5% |

## 3. Escalation
| Trigger | Mức | Tới ai | SLA |
|---------|-----|--------|-----|
| IP pre-flag = HIGH | Bắt buộc | OPC + PRD-004 trước design hoàn thiện | Ngay |
| Clearance uncertain | Conservative default | OPC review | 24h |
| KRI ip_clearance_rate < 99% (critical) | Freeze | Dừng listing pipeline, RCA | 24h |
| tm_takedown_rate > 3% | Critical | RCA + siết rubric | 24h |
| SLI operational vượt budget | Freeze feature SOP đó | OPC | Weekly review |

## 4. Decision Authority
| Quyết định | R | A |
|-----------|---|---|
| Niche pass/fail | AI niche-research | OPC |
| Style design | AI product-design | OPC |
| CLEAR / MODIFY / REJECT (IP) | AI product-design | OPC (HIGH-risk) |
| Approve handoff downstream | OPC | OPC |

## 5. Non-negotiables
- KHÔNG listing bất kỳ SP nào chưa CLEAR IP/TM (cả US và EU).
- KHÔNG upscale ảnh để "đạt" 300 DPI — phải re-generate ở canvas đúng.
- Khi không chắc về IP → mặc định **conservative** (không cho qua), đẩy human.
- Tuân thủ chỉ là 1 trong 4 style chuẩn (tile/watercolor/funny/mandala), không phát sinh style ngoài brand guide khi chưa duyệt.

## Liên kết
- Cross-ref company gates: [../../00-company/README.md](../../00-company/README.md) (Gate #3 IP/TM thuộc phòng này)
- Backoffice GPSR (gate listing EU) bổ sung tại 05-backoffice SOP-BCK-004.
