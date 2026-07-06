# KB — Order-Ops Playbook (vibe-eu-opc-ful-order-ops)

Tham chiếu: SOP-FUL-001 (monitor-orders), SOP-FUL-002 (route-fulfillment). DAKOfits — POD AOP leggings/activewear đa-niche, traffic 100% Facebook Ads, khách US+EU.

---

## 1. Verify checklist (SOP-FUL-001)
Quét đơn paid **mỗi 2h** (sweep 23:00 ICT). Loại đơn `unpaid/pending/cancelled`.

| # | Check | PASS | FAIL → action |
|---|---|---|---|
| 1 | **Payment** | `financial_status = paid`, no chargeback | `authorized` chưa capture → HOLD 4.D (cancel sau 24h) |
| 2 | **Address** | đủ name/line1/city/ZIP/country + format đúng nước | thiếu/sai → HOLD 4.B → cx email khách (EN) |
| 3 | **SKU / variant** | SKU map Printify, size **XS–3XL** + color tồn tại | không map / OOS → HOLD 4.A → merch fix / cx đổi size |
| 4 | **Fraud** | risk thấp | risk cao → FRAUD 4.C → hold + escalate OPC ≤12h |
| 5 | **Duplicate** | đơn đơn nhất | trùng → 4.E merge/cancel + notify |

Pass toàn bộ → `verify_status = PASS`, đẩy verified queue + `paid_at`.
Đơn giá trị > $150 → escalate OPC review trước route (dù PASS).

## 2. Fraud flag rule
FRAUD nếu ≥1: (a) risk-score cổng thanh toán cao; (b) nhiều đơn cùng card trong thời gian ngắn; (c) billing country ≠ shipping country (mismatch); (d) email/địa chỉ trong blocklist; (e) đơn giá trị bất thường + ship address freight-forwarder.
→ `verify_status = FRAUD`, `need_review = true`, **KHÔNG tự route**, escalate OPC quyết hold/cancel ≤12h.

## 3. Provider-by-region map (SOP-FUL-002)
| Market khách | Provider | Lý do |
|---|---|---|
| **US** | Printify **US** provider | ship nội địa nhanh, no VAT/customs |
| **EU** | Printify/PrintBase **EU** provider | tránh VAT/customs/IOSS phức tạp, ship nội khối |

Quy tắc cứng: **US→US, EU→EU** ≥99% match. Cross-region **chỉ khi** variant OOS ở provider cùng vùng (4.A) — log lý do. Variant XS–3XL phải tồn tại ở provider đã chọn trước khi submit.

## 4. SLO 18h / 6h vs Ceiling 24h
| SLI | SLO nội bộ (chặt) | Ceiling / SLA (ngoài) | Đo |
|---|---|---|---|
| On-time routing | **≤18h** từ paid, ≥98% | ceiling hard-fail **≤24h**; SLA khách ≤24h | routed_at − paid_at |
| Routing avg | ≤12h | — | mean |
| Tracking sau ship | **≤6h** sau fulfilled, 100% | SLA ≤5 ngày | tracking_sent_at − fulfilled_at |
| Verification | ≤4h | ceiling ≤24h (no đơn "rơi") | verified_at − paid_at |

**Error budget:** SLO 18h → ceiling 24h. Đơn `routed_within_h > 24` = hard-fail → RCA bắt buộc + `need_review`. Theo dõi tỉ lệ vượt 18h để cảnh báo sớm trước khi chạm 24h.
SLO 18h = mục tiêu nội bộ giữ buffer; 24h = cam kết khách + lằn ranh đỏ.

## 5. Tracking flow
Poll production `in-production → fulfilled` (US ~2–5d, EU ~2–5d). Khi ship: fetch tracking# + carrier → cập nhật ShopBase fulfillment → **gửi email tracking EN** → ghi `tracking_sent_at`, `tracking_sent = true`. Không đơn nào "ship" mà chưa gửi tracking.

## 6. Cost handoff → Backoffice
Sau ship, đẩy **print cost + ship cost** từ provider invoice → **vibe-eu-opc-bck-finance** (05-backoffice) cho profit-per-SKU. Set `cost_pushed_backoffice = true`. KHÔNG tự ghi sổ/VAT/P&L — chỉ đẩy raw cost data.

## 7. Exception routing (tóm tắt SOP muc 4)
| Tag | Nguồn | Owner xử lý |
|---|---|---|
| SKU_OOS | verify 4.A | merch fix mapping / cx đổi size-refund |
| ADDRESS_INVALID | verify 4.B | cx email khách (EN) |
| FRAUD_RISK | verify 4.C | OPC quyết ≤12h |
| AUTH_NOT_CAPTURED | verify 4.D | hold ≤24h → cancel |
| DUPLICATE | verify 4.E | merge/cancel + notify |
| PROVIDER_REJECT | route 4.A | provider thay thế cùng vùng / cx |
| PRODUCTION_DELAY | route 4.C | cx proactive email + ETA mới |
| LOST_IN_TRANSIT | route 4.E | case carrier → reship/refund |

Mọi exception → vibe-eu-opc-ful-cx hoặc OPC; **không** tự trả lời ticket/refund (đó là việc của cx).
