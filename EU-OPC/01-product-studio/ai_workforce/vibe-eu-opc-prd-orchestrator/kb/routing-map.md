# Routing Map — vibe-eu-opc-prd-orchestrator

**Dept:** prd (Product Studio) · **Vai trò:** Manager điều phối, KHÔNG execute.
**Ngày:** 2026-06-23

DAKOfits = shop domain riêng trên nền tảng **ShopBase**. Product Studio là điểm
đầu của value chain: tạo "nguyên liệu" SP (cleared design) cho toàn pipeline.

---

## 1. Bảng routing: task → worker → SOP

| Task / Intent | Route tới worker | SOP | Output mong đợi |
|---------------|------------------|-----|-----------------|
| Niche research, demand scoring, FB audience sizing, competitor ad spy | `vibe-eu-opc-prd-niche-research` | SOP-PRD-001 | Validated niche list |
| Trend analysis, seasonal opportunity calendar, IP/TM pre-flag | `vibe-eu-opc-prd-niche-research` | SOP-PRD-002 | Seasonal calendar |
| AOP design print-ready (tile / watercolor / funny / mandala), QC 360°, 300 DPI | `vibe-eu-opc-prd-design` | SOP-PRD-003 | Design print-ready |
| IP/TM clearance (USPTO + EUIPO), clearance logging | `vibe-eu-opc-prd-design` | SOP-PRD-004 | IP-clearance log |
| Đăng LIVE ShopBase, setup Printify, variant pricing, product page | `vibe-eu-opc-mer-orchestrator` (downstream) | SOP-MER-* | Live product ShopBase |
| Ad creative, FB Ads, email, organic social | **Growth** (chỉ SAU live ShopBase) | SOP-GRW-* | — (không route trực tiếp từ đây) |

> Phần chuyên môn LUÔN delegate. Manager KHÔNG tự research / design / clear IP.

---

## 2. IP/TM Gate (gate cứng — enforce sau PRD-004)

| Gate | Rule | Hệ quả vi phạm |
|------|------|----------------|
| G1 | **No IP/TM clearance → no listing** | Chặn handoff sang Merch |
| G3 | **No dual-market lookup (USPTO + EUIPO) → not CLEAR** | Status không được CLEAR |
| G2 | No 300 DPI → no print-ready | Design reject (quay lại PRD-003) |
| G4 | AOP seam lộ → no handoff | Quay lại tạo seamless tile |

**Quyết định clearance:**
- `CLEAR` → đủ điều kiện handoff Merch.
- `MODIFY` → quay lại PRD-003 sửa design rồi clear lại.
- `REJECT` → drop niche/design, log, **không** handoff.
- **Conservative default:** nghi ngờ trademark = **REJECT**, đẩy OPC review.

---

## 3. Pipeline niche → design → clearance → handoff Merch (ShopBase-first)

```
PRD-001 niche-research ─▶ validated niche list
PRD-002 niche-research ─▶ seasonal timing + IP pre-flag
PRD-003 design         ─▶ AOP print-ready (300 DPI, QC 360°)
PRD-004 design         ─▶ IP/TM clearance
        │ status == CLEAR ?
        ├─ CLEAR  ─▶ HANDOFF vibe-eu-opc-mer-orchestrator
        │            (Merch đăng LIVE ShopBase TRƯỚC)
        │            (chỉ KHI live, Merch mới bàn giao Growth)
        ├─ MODIFY ─▶ loop về PRD-003
        └─ REJECT ─▶ drop + log
```

**ShopBase-first rule (CỨNG):** SP phải live trên ShopBase (Merch hoàn tất)
TRƯỚC khi Growth tạo nội dung/quảng cáo. Orchestrator này bàn giao cleared
design **cho Merch**, KHÔNG bàn giao thẳng Growth.

---

## 4. Escalation Matrix

| Trigger | Mức | Tới ai | SLA |
|---------|-----|--------|-----|
| IP pre-flag = HIGH | Bắt buộc | OPC + PRD-004 trước khi design hoàn thiện | Ngay |
| Clearance uncertain | Conservative (REJECT) | OPC review | 24h |
| confidence_score < 0.7 hoặc thiếu evidence | need_review=true | `processing/human-review` | 24h |
| ip_clearance_rate < 99% (critical) | Freeze | Dừng listing pipeline + RCA | 24h |
| tm_takedown_rate > 3% | Critical | RCA + siết rubric | 24h |

---

## 5. Liên kết
- Specialists: [`vibe-eu-opc-prd-niche-research`](../../vibe-eu-opc-prd-niche-research/SKILL.md) · [`vibe-eu-opc-prd-design`](../../vibe-eu-opc-prd-design/SKILL.md)
- Downstream: [`vibe-eu-opc-mer-orchestrator`](../../../../02-merchandising/ai_workforce/vibe-eu-opc-mer-orchestrator/SKILL.md)
- Rules/gates: [`../../../_rules/README.md`](../../../_rules/README.md) · Workflow DAG: [`../../../_workflow/README.md`](../../../_workflow/README.md)
