# KB — Routing Map (vibe-eu-opc-bck-orchestrator)

Manager-level routing cho phòng 05-backoffice (L3 Support), DAKOfits. Orchestrator **KHÔNG execute** — chỉ classify, route, enforce gate legal, tổng hợp CEO brief. Phòng L3 **hỗ trợ toàn bộ L2** + phục vụ **Owner**.

---

## 1. Task → Worker → SOP

| # | Task signal | Route → worker | SOP | Output mong đợi |
|---|-------------|----------------|-----|-----------------|
| 1 | Ghi sổ · reconcile fee (ShopBase/Printify/Meta/gateway) · ledger · "khớp số liệu" | `vibe-eu-opc-bck-finance` | BCK-001 | Ledger + recon log |
| 2 | Profit-per-SKU · P&L · ROAS/CPA tracking · USD→VND · scale/kill từ profit | `vibe-eu-opc-bck-finance` | BCK-002 | Profit-per-SKU, P&L, CEO brief input |
| 3 | VAT OSS/IOSS EU · US sales tax note · "khai thuế" · tờ khai draft | `vibe-eu-opc-bck-finance` | BCK-003 | Tờ khai VAT draft + tax note |
| 4 | GPSR clearance · IP/TM breed check · nhãn an toàn EU · Meta Ad Policy clearance · Responsible Person | `vibe-eu-opc-bck-compliance` | BCK-004 | Clearance log + nhãn + IP/TM check |
| 5 | GDPR · DSAR · breach · RoPA · data inventory · ShopBase TOS | `vibe-eu-opc-bck-compliance` | BCK-005 | RoPA, DSAR log, breach log |
| 6 | AI workforce: uptime · cost · quality output · capacity · bump skill/SOP | `vibe-eu-opc-bck-ops-hr` | BCK-006 | Roster, review, weekly report, capacity |
| 7 | **CEO brief / chốt kỳ** (end-to-end) | **fan-out** finance + compliance + ops-hr → tổng hợp | 001/002/003 + 004/005 + 006 | CEO brief 1 kỳ cho Owner |

> Khi task chứa nhiều trụ (vd "chốt sổ + tình trạng tuân thủ + sức khỏe worker tháng này") ⇒ coi là **chốt kỳ** (#7), fan-out cả 3 specialist (§3).

---

## 2. Gate cứng (enforce — legal mandate, Compliance SLO=100%, error budget 0%)

| Gate | Rule | Điều kiện PASS | Fail ⇒ |
|------|------|----------------|--------|
| **No GPSR → No publish (EU)** | R1 / BCK-004 | SP chờ EU publish có GPSR clearance + Responsible Person + nhãn an toàn | `compliance_status=BLOCKED`; block Merch publish EU → trả 05-compliance; `need_review=true` + escalate Owner ngay |
| **No Meta Ad Policy → No ads** | R2 / BCK-004 | creative + landing có Meta Ad Policy clearance (+ IP/TM clear, R3 conservative REJECT khi nghi ngờ) | BLOCKED; block Growth ads → trả 05-compliance |
| **GDPR breach → notify ≤ 72h** | R4 / BCK-005 | không có breach mở; nếu có → notify trong 72h | timer cứng 72h; Owner = notify authority; quá hạn = `breach=overdue`, legal vi phạm; `need_review=true` ngay |
| **VAT filing 100% on-time** | R5 / BCK-003 | deadline VAT OSS/IOSS trong kỳ on-time 100% | `vat_ontime=late` = legal vi phạm; escalate Owner |

> Bổ sung **R6 (no fabricated figures/FX):** số liệu finance thiếu nguồn ⇒ `need_review=true`, KHÔNG bịa. Nguồn unit-economics: [`../../../_shared/unit-economics.md`](../../../../_shared/unit-economics.md). Luật đầy đủ: [`../../_rules/README.md`](../../../_rules/README.md).

---

## 3. Chốt-kỳ → CEO brief loop

```
[Cuối kỳ: data tất cả phòng L2 (cost/fee/order/ad-spend) + SP chờ EU publish + run log worker]
  → CLASSIFY: đây là chốt kỳ (CEO brief)
  → ROUTE finance (BCK-001/002/003): ledger + recon → profit-per-SKU + P&L → VAT draft + USD→VND
  → ROUTE compliance (BCK-004/005): GPSR/IP-TM clearance status + Meta policy + GDPR breach/DSAR/RoPA
  → ROUTE ops-hr (BCK-006): workforce uptime/cost/quality/capacity
  → ENFORCE 4 gate cứng:
        ├─ GPSR chưa clear SP chờ EU publish  → BLOCKED (no publish)
        ├─ Meta Ad Policy chưa clear           → BLOCKED (no ads)
        ├─ GDPR breach mở                      → timer ≤72h, Owner notify
        └─ VAT deadline trong kỳ               → on-time 100%
  → CEO BRIEF: compliance_status (CLEAR/BLOCKED) + finance_summary + workforce_health + gate_checks
        + evidence[] + confidence_score + need_review → trình Owner
```

Decision authority (theo `_rules/README.md`): GPSR PASS/FAIL = compliance AI theo checklist; **GPSR exception, nộp VAT, khóa sổ, breach notify, kill/scale SKU, bump skill = Owner (Accountable)**.

---

## 4. Escalation matrix (việc KHÔNG route nội bộ / vượt khung)

| Trigger | Escalate tới | Thời hạn |
|---------|--------------|----------|
| Gate cứng FAIL (R1–R5) | **Owner** | ngay lập tức |
| KRI Red bất kỳ | **Owner** | 24h |
| GDPR breach rủi ro cao | **Owner** | trong 72h clock |
| Fee discrepancy > 2% | **Owner** (qua finance) | trong kỳ |
| AI worker uptime < 95% | **Owner** + root cause | 24h |
| Cost spike > 30% | **Owner** (qua finance) | weekly report |
| Cần niche/audience/design | **01-product-studio** | upstream |
| Cần setup/pricing/page/publish | **02-merchandising** | downstream gate consumer |
| Chạy ads/creative/email | **03-growth** | downstream gate consumer |
| Đơn/fulfillment/CX ticket | **04-fulfillment-cx** | phòng khác |

---

## 5. CEO brief cadence
- **Daily:** compliance gate check (GPSR/Meta/breach timer) — gate cứng không chờ kỳ.
- **Weekly:** workforce report (BCK-006) + recon spot-check + alert KRI.
- **Monthly:** chốt sổ → profit-per-SKU + P&L + CEO brief đầy đủ (fan-out 3 specialist).
- **Theo deadline VAT (monthly/quarterly OSS/IOSS):** tờ khai draft → Owner nộp on-time 100%.

---

## 6. need_review triggers (đẩy `processing/human-review/`)
bất kỳ gate cứng fail · GDPR breach mở · VAT due/late · số liệu finance thiếu nguồn (R6) · confidence_score < 0.7 · task mơ hồ không map được worker.
