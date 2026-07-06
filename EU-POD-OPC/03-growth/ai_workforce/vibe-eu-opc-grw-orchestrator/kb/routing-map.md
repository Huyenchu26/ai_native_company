# KB — Routing Map (vibe-eu-opc-grw-orchestrator)

Manager-level routing cho phòng 03-growth, DAKOfits. Orchestrator **KHÔNG execute** — chỉ classify, route, enforce gate, đọc report.

---

## 1. Task → Worker → SOP

| # | Task signal | Route → worker | SOP | Output mong đợi |
|---|-------------|----------------|-----|-----------------|
| 1 | Chạy/build/tối ưu/scale/kill campaign · ROAS/CPA/CBO/ABO/CAPI/EMQ · "đẩy ngân sách", "cắt ad lỗ" | `vibe-eu-opc-grw-fb-ads` | GRW-002 | Campaign tối ưu + decision JSON |
| 2 | Growth report tuần · KPI/KRI · đọc signal cross-channel · on/off-track O1 | `vibe-eu-opc-grw-fb-ads` | GRW-004 | Growth report + alert |
| 3 | Viết creative · hook 0–3s · video script · UGC brief · carousel copy · "creative mới", refresh | `vibe-eu-opc-grw-creative` | GRW-005 | Creative package (image/video/carousel) |
| 4 | Email · Klaviyo · cart-abandon · post-purchase upsell · win-back · seasonal promo | `vibe-eu-opc-grw-marketing` | GRW-003 | Email campaign đã gửi (opt-in) |
| 5 | Organic social · community · IG/TikTok/FB dog-mom groups · UGC seeding | `vibe-eu-opc-grw-marketing` | GRW-001 | Organic posts/community scheduled |
| 6 | **Đợt promote 5–10 SP** (end-to-end) | **fan-out** creative → fb-ads → report | 005→002→004 | Batch điều phối + report tổng hợp |

> Khi task chứa nhiều signal (vd "tạo creative rồi chạy ads cho 8 SP") ⇒ coi là **batch** (#6), fan-out theo loop §3.

---

## 2. Gate cứng (enforce TRƯỚC khi cho worker launch)

| Gate | Điều kiện PASS | Fail ⇒ |
|------|----------------|--------|
| **No Meta Ad Policy → No ads** | creative + landing page có clearance 05-compliance | STOP launch → trả creative/05-compliance; `decision=HOLD`, `need_review=true` |
| **Email opt-in only (GDPR/CAN-SPAM)** | subscriber có explicit consent; honor unsub/erasure | BLOCK send → exclude list không opt-in |
| **Winner = Blended ROAS ≥ BE-ROAS per-SKU** (US ~2.75, EU ~5.3) | Blended ≥ BE-ROAS của SKU đó | KHÔNG scale (lãi ảo) → HOLD, đề xuất nâng giá/đổi provider. **KHÔNG dùng 2.5 cứng** |
| **Budget escalate** | tổng spend ≤ $150/ngày trong khung cap đã duyệt | > $150/ngày hoặc discount ăn margin ⇒ HOLD + escalate OPC + 05-finance |

Nguồn BE-ROAS: [`../../../_shared/unit-economics.md`](../../../_shared/unit-economics.md). Luật vận hành đầy đủ: [`../../_rules/README.md`](../../_rules/README.md).

---

## 3. Promote-theo-đợt loop (SOP-MER-006 ↔ Growth)

```
[02-merch: batch 5–10 SP]
  → CLASSIFY + lấy BE-ROAS/SKU
  → ROUTE creative (GRW-005): creative package / SP
  → ENFORCE gate Meta Ad Policy (mỗi creative+page)
  → ROUTE fb-ads (GRW-002): ABO test $10/ad set, verify CAPI (EMQ ≥ 6)
  → ROUTE fb-ads (GRW-004): đọc Blended ROAS vs BE-ROAS/SKU
        ├─ Blended ≥ BE-ROAS & CPA<$20      → SCALE (CBO +20%/2 ngày, cap $100/ngày)
        ├─ Blended < BE-ROAS (lãi ảo)        → HOLD + đề xuất nâng giá/đổi provider
        ├─ ROAS<1.5 sau 3 ngày & spend≥$40   → KILL loser
        └─ frequency>2.5 / CTR↓>30%          → REFRESH (→ creative)
  → (bổ trợ) ROUTE marketing: email post-purchase/win-back winner + organic seeding (opt-in)
  → REPORT tổng hợp: winner scale / loser kill / refresh / escalate
```

Cadence (theo `_workflow/README.md`): Daily check ROAS/CPA → mỗi 2 ngày scale +20% → Weekly trend review + creative refresh batch.

---

## 4. Escalation matrix (việc KHÔNG route nội bộ)

| Trigger | Escalate tới | Ghi chú |
|---------|--------------|---------|
| BM/ad account bị ban/flag | **OPC** (ngay) | + failover tier (fb-ads) |
| Vượt budget cap / > $150/ngày / discount ăn margin | **OPC + 05-finance** | trước khi scale |
| Off-track O1 (ROAS/revenue) | **OPC** | từ growth report |
| Meta policy / IP breed chưa clear | **05-compliance** | gate cứng #1 |
| GDPR request / email không opt-in / spam cap | **05-compliance** | gate cứng #2 |
| Số liệu cost lệch / cần reconcile | **05-finance** | source of truth |
| Đơn hàng / fulfillment / CX | **04-fulfillment-cx** | ngoài phạm vi Growth |
| Cần live product / product page mới | **02-merchandising** | upstream |
| Cần niche/audience/design | **01-product-studio** | upstream gián tiếp |

---

## 5. need_review triggers (đẩy `processing/human-review/`)
gate fail · Blended < BE-ROAS · vượt budget cap · BM/account flag · confidence_score < 0.7 · task mơ hồ không map được worker.
