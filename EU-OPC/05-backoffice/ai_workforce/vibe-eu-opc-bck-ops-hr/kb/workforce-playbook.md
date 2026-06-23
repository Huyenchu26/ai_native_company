# Workforce Playbook — vibe-eu-opc-bck-ops-hr (DAKOfits)

"HR cho đội AI Worker" theo **SOP-BCK-006**. Đây là cẩm nang vận hành: metrics, roster, capacity rule, escalation, cách cập nhật skill/SOP.

---

## 1. Metrics & SLO (SLI → SLO → cách đo)

| SLI | SLO | Cách đo | Ngưỡng escalate |
|-----|-----|---------|-----------------|
| AI worker uptime | **≥ 99%** | run log (cron/trigger chạy đúng) | < 95% → escalate Owner |
| Output quality (1 − reject rate) | **≥ 90%** (reject **< 10%**) | human-review reject log | reject > 10% → skill-update/retrain |
| Cost per worker tracked | **100%** | token/API cost report | spike > 20% → cảnh báo finance |
| Weekly report on-time | **100%**, mỗi thứ 2 | calendar | trễ → flag |

- **Error budget:** ≤ 1% downtime/worker/tuần.
- **Cost KHÔNG phải việc của ops-hr để hạch toán** — ops-hr chỉ TỔNG HỢP token/API spend per worker và **feed finance** (SOP-BCK-001/002). KHÔNG làm sổ, KHÔNG khai VAT.
- Mọi con số phải có `evidence[]`; thiếu log → `need_review: true`, KHÔNG bịa.

---

## 2. Roster — 2 lớp skill (ĐẾM THẬT, KHÔNG hard-code "12")

Công ty có **2 lớp skill** chạy song song. **Quy tắc: luôn đếm trực tiếp, không viết cứng con số vào report.**

### Lớp A — legacy `vibe-opc-pod-*`
- Cài tại `~/.claude/skills/`, dùng cho phòng **chưa có bản EU-OPC riêng**.
- Snapshot 2026-06-23 theo [workforce-map](../../../_ai-workforce/workforce-map_v1.0_2026-06-23.md): **12 worker** = 2 PRD + 2 MER + 3 GRW + 2 FUL + 3 BCK. (12 là tổng theo map, KHÔNG phải 3/phòng × 5.)
- Phủ 24/24 SOP responsible.

### Lớp B — EU-OPC-specific `vibe-eu-opc-{prd,mer,grw,ful,bck}-*`
- Build mới bởi vibe-aiworkforce theo SOP riêng EU-OPC; mỗi phòng có specialist + 1 orchestrator.
- **Cách đếm thật:** đếm folder `EU-OPC/**/ai_workforce/*/SKILL.md`. Snapshot 2026-06-23 gồm cả skill này (mới nhất).
- Khi phòng đã có bản EU-OPC → bản đó **ưu tiên** hơn legacy cho phòng đó.

### Quy tắc đếm `total_workers` cho report
1. Liệt kê roster **active thực tế**: với phòng đã migrate → tính bản EU-OPC; phòng chưa migrate → tính legacy.
2. KHÔNG đếm trùng (cùng 1 vai trò ở cả 2 lớp chỉ tính bản active).
3. Ghi **phương pháp đếm + nguồn** (workforce-map + folder count) vào `evidence[]`.
4. Nếu map và folder count lệch → `need_review: true` + action `sop-bump`/cập nhật map.

---

## 3. Capacity rule

- **Workload** = khối lượng "promote theo đợt" (batch 5–10 SP/đợt, SOP-MER-006) trên catalog đa-niche ~3.200 SP, US+EU.
- **Capacity status:**
  - **OK** — roster đủ chạy batch hiện tại trong cron window, không dồn.
  - **STRAINED** — gần trần: batch dồn, độ trễ tăng, uptime/quality bắt đầu trượt → đề xuất phòng ngừa.
  - **OVER** — thiếu: miss deadline batch, reject tăng do worker quá tải → **bắt buộc** có action.
- **Rolling 4-week capacity plan:** dự báo số batch sắp tới vs roster; đề xuất thêm worker / đổi lịch cron / tách batch.
- STRAINED hoặc OVER → đưa vào `actions[]` (`scale-worker` / `cron-reschedule`).

---

## 4. Escalation runbook

| Trigger | Hành động | Action type |
|---------|-----------|-------------|
| Uptime < 95% | Escalate Owner + root cause (cron/trigger/credential/schema) | `escalate` |
| Reject rate > 10% | Flag retrain/skill-update + tăng human-review tạm thời | `retrain` / `skill-update` |
| Cost spike > 20% | Cảnh báo finance (feed SOP-BCK-001/002) | `cost-alert` |
| Capacity OVER (batch dồn) | Đề xuất thêm worker / đổi cron / tách batch | `scale-worker` / `cron-reschedule` |
| SOP đổi version | Bump skill version pinned theo SOP, báo worker liên quan | `sop-bump` |

- Escalation luôn kèm `evidence[]` (log cụ thể) + `confidence_score`.
- Worker degraded 2 tuần liên tiếp → đưa vào performance review sâu, cân nhắc thay/đổi skill.

---

## 5. Cách cập nhật skill/SOP (version pinning)

- **Nguyên tắc:** skill version **pin theo SOP version**. SOP-BCK-006 v1.0 → skill v1.0.
- Khi một SOP bump (vd MER-003 v1.0 → v1.1):
  1. Xác định worker responsible (qua workforce-map).
  2. Tạo action `sop-bump` + `skill-update` cho worker đó.
  3. Cập nhật skill.json `version` + ghi changelog.
  4. Báo (I) tất cả worker liên quan; Owner phê duyệt thay đổi roster/skill.
- Khi build bản EU-OPC mới thay legacy → cập nhật workforce-map (đánh dấu phòng đã migrate) để `total_workers` đếm đúng lớp active.

---

## 6. Weekly report — checklist
- [ ] Uptime per worker + trung bình roster (≥99%).
- [ ] Reject rate per worker + trung bình (<10%).
- [ ] Cost summary (total + delta% + per_worker) → feed finance.
- [ ] Capacity status (OK/STRAINED/OVER) + rolling 4-week.
- [ ] total_workers đếm thật (evidence: map + folder count).
- [ ] actions[] (escalation, skill/SOP bump, scale).
- [ ] evidence[], confidence_score, need_review.
- [ ] On-time thứ 2; bàn giao `vibe-eu-opc-bck-orchestrator`.

---

## Links
- SOP-BCK-006: [manage-workforce](../../manage-workforce/template/sop_bck-006_workforce-ops_v1.0_2026-06-23.md)
- Roster canonical: [workforce-map](../../../_ai-workforce/workforce-map_v1.0_2026-06-23.md)
- Output schema: [workforce-review.schema.json](../schema/workforce-review.schema.json)
