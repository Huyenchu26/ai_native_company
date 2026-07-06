# Routing Map — vibe-eu-opc-mer-orchestrator

**Dept:** 02-merchandising (`mer`) · **Role:** Manager (điều phối, KHÔNG execute) · **Ngày:** 2026-06-23

Manager nhận mọi yêu cầu của phòng Merchandising, **phân loại → route** sang đúng specialist, **enforce gate cứng** rồi **handoff Growth**. Bản thân chỉ sở hữu SOP-MER-006 (promote theo đợt).

---

## 1. Bảng task → worker → SOP

| # | Task / yêu cầu người dùng | Route đến | SOP | Output mong đợi |
|---|---------------------------|-----------|-----|-----------------|
| 1 | Setup product Printify/PrintBase (blueprint, provider US+EU, variant XS–3XL/color) | `vibe-eu-opc-mer-catalog` | SOP-MER-002 | Product blueprint |
| 2 | Set/điều chỉnh pricing variant theo margin band | `vibe-eu-opc-mer-catalog` | SOP-MER-003 | Variant pricing (gross 45–55%) |
| 3 | Catalog sync ShopBase + QC accuracy | `vibe-eu-opc-mer-catalog` | SOP-MER-004 | Live product (sync ≥99%) |
| 4 | Viết/refine product page + upsell/bundle + chèn GPSR label | `vibe-eu-opc-mer-product-page` | SOP-MER-001 | Product page publish-ready (EN) |
| 5 | **Promote theo đợt** (chọn 5–10 SP → tối ưu → handoff → scale/cut) | **SELF (orchestrate)** | **SOP-MER-006** | Batch promote package → Growth |
| 6 | Chạy/tối ưu FB Ads, đọc ROAS/CPA, scale ngân sách | `vibe-eu-opc-grw-orchestrator` (downstream) | SOP-GRW-002 | Campaign + ROAS feedback |
| 7 | Tạo design / IP clearance / QC 360° | `vibe-opc-pod-product-design` (upstream) | SOP-PRD-003/004 | Cleared design (KHÔNG phải việc Merch) |

> Quy tắc vàng: Manager **không bao giờ tự** setup blueprint, viết page hay chạy ads. Mọi việc chuyên môn → route.

---

## 2. Gate cứng (enforce trước publish & trước handoff)

| Gate | Rule (từ `_rules/README.md` + `unit-economics.md`) | Fail → hành động |
|------|-----------------------------------------------------|------------------|
| **GPSR** (R1) | no GPSR clearance → no publish (đơn EU); nhãn an toàn + Responsible Person | Block, escalate **phòng 05-backoffice** ngay |
| **Contribution Margin** | pricing floor trên CM sau ads (giá−base−ship−fee−CPA−VAT−fx), KHÔNG margin ảo | Block, re-price / đổi provider |
| **Pricing floor** (R2) | gross margin 45–55%; EU tính trên giá net-of-VAT | <45% reject; ngoài band → OPC duyệt |
| **Variant đủ size** (R4) | XS–3XL đủ trước publish | Đổi blueprint (route catalog) |
| **Sync accuracy** (R5) | ≥99% trước publish | Re-sync (route catalog) |
| **Winner per-SKU** | scale chỉ khi Blended ROAS ≥ BE-ROAS riêng SKU/market (1/GM) | <BE-ROAS → cut / tối ưu 1 vòng |

---

## 3. Promote-theo-đợt loop + handoff Growth

```
[01 design + 05 GPSR] → (1)chọn 5–10 SP → (2)setup+pricing[catalog]
   → (3)product page[product-page] → (4)ENFORCE GATE
   → (5)HANDOFF package[grw-orchestrator] → (6)đọc ROAS/CPA per-SKU
   → winner≥BE-ROAS: SCALE | loser<BE-ROAS: CUT → (7)feed đợt sau
```

**Handoff package (schema `merch-batch-plan`):** batch_id, products[5–10], gate_checks (gpsr/contribution_margin/pricing_floor đều passed), routing[], `handoff_to_growth=true`, evidence[], confidence_score≥0.7, need_review=false. Nếu bất kỳ gate fail hoặc confidence<0.7 → `handoff_to_growth=false`, `need_review=true`, KHÔNG bàn giao.

---

## 4. Escalation matrix

| Tình huống | Escalate đến | SLA |
|-----------|--------------|-----|
| SP EU thiếu GPSR clearance/label | Phòng 05-backoffice (compliance) | ngay |
| Margin/contribution không đạt do cost provider | OPC (đề xuất đổi provider) | 24h |
| Design fail QC / IP chưa cleared | Phòng 01 / `vibe-opc-pod-product-design` | ngay |
| Đợt promote toàn loser | OPC + `vibe-eu-opc-grw-orchestrator` | 48h |
| Provider OOS hàng loạt | OPC (đổi provider) | 24h |
| Confidence < 0.7 / gate ambiguous | review queue (`script/review_queue.py`) → OPC | trước handoff |

---

## 5. Links
- SOP-MER-006: [`../../../promote-batch/template/sop_mer-006_promote-batch_v1.0_2026-06-23.md`](../../../promote-batch/template/sop_mer-006_promote-batch_v1.0_2026-06-23.md)
- Unit economics: [`../../../../_shared/unit-economics.md`](../../../../_shared/unit-economics.md)
- Rules: [`../../../_rules/README.md`](../../../_rules/README.md)
- Specialists: `vibe-eu-opc-mer-catalog` · `vibe-eu-opc-mer-product-page` · Downstream: `vibe-eu-opc-grw-orchestrator`
