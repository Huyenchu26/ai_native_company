# SOP-BCK-006 — AI Workforce Ops/HR (12 AI Worker)

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-ops-hr` `[AI WORKFORCE]`

---

## 0. IPO
| | |
|---|---|
| **Input** | Run log/cost của 12 AI Worker (tất cả phòng), output quality flags, escalation tickets, skill/SOP versions |
| **Process** | Track uptime/cost/quality → đánh giá năng lực → cập nhật skill/SOP → weekly report → capacity plan |
| **Output** | `workforce roster`, performance review, weekly report, capacity plan, escalation log |

## 1. Tổng quan
"HR" cho 12 AI Worker — **12 là tổng thực tế theo workforce-map (2+2+3+2+3 = 12)**, KHÔNG phải 3/phòng × 5 phòng (số worker mỗi phòng khác nhau, không đồng đều). ops-hr AI giám sát sức khỏe lực lượng số: uptime (worker có chạy đúng cron/trigger không), cost (token/API spend → feed finance), quality (tỉ lệ output bị human-review reject), capacity (đủ worker cho khối lượng đa-niche ~3.200 SP không). Weekly report cho Owner; escalation khi worker degrade.

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Track uptime/cost/quality | ops-hr AI | Owner | finance AI | — |
| Performance review | ops-hr AI | Owner | trưởng từng phòng | — |
| Cập nhật skill/SOP | ops-hr AI | Owner | — | tất cả worker |
| Weekly report | ops-hr AI | Owner | — | Owner |
| Escalation | ops-hr AI | Owner | phòng liên quan | Owner |

`[AI WORKFORCE]` ops-hr AI: thu run log, tính metric, viết review/report, đề xuất skill update, mở escalation. Owner: phê duyệt thay đổi roster/skill.

## 3. Quy trình (ICOM)
1. **Thu run log** (I: log 12 worker; M: monitoring): tổng hợp uptime, cost, success/fail.
2. **Tính metric & quality** (C: SLO mỗi worker; M: roster sheet): uptime %, cost/worker, reject rate.
3. **Đánh giá & escalate** (C: ngưỡng degrade): worker dưới SLO → performance review + escalation.
4. **Cập nhật skill/SOP** (I: SOP version mới; M: skill registry): bump skill khi SOP đổi.
5. **Weekly report + capacity** (O: report + capacity plan): so workload vs capacity, đề xuất scale.

## 4. Phân nhánh
- Worker uptime <95% → escalate Owner + root cause (cron/trigger/credential).
- Reject rate >10% → flag retrain/skill-update, tăng human-review tạm thời.
- Cost spike >20% → cảnh báo finance (feed SOP-BCK-001/002).
- Capacity thiếu (batch dồn) → đề xuất thêm worker/đổi lịch cron.

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| AI worker uptime | ≥ 99% | run log |
| Output quality (1 − reject rate) | ≥ 90% | human-review log |
| Cost per worker tracked | 100% | cost report |
| Weekly report on-time | 100%, mỗi thứ 2 | calendar |

**Error budget:** ≤1% downtime/worker/tuần. **Prevention:** monitoring tự động + alert, skill version pinned theo SOP version, escalation runbook, capacity plan rolling 4 tuần.

## 6. Tài nguyên + Links
- [_skills-agents: 3 worker matrix + roster](../../_skills-agents/README.md) · [_ai-workforce](../../../_ai-workforce/README.md)
- Feed cost → [SOP-BCK-001](../../keep-books/template/sop_bck-001_bookkeeping_v1.0_2026-06-23.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
