# DAKOfits — Operating Flow (Quy tắc chuỗi vận hành)

**Mã:** REF-FLOW-001 · **Phiên bản:** 1.0 · **Ngày:** 2026-06-23 · **Áp dụng:** toàn công ty

> Mô hình: **shop có domain riêng trên nền tảng ShopBase**. Traffic 100% Facebook Ads. Đây là quy tắc thứ tự bắt buộc giữa các phòng — mọi orchestrator phải tuân thủ.

---

## Chuỗi bắt buộc (theo thứ tự, không đảo)

```
1. PRODUCT STUDIO   niche research → AOP design → IP/TM clearance (PASS)
        │  gate: no IP/TM clearance → no listing
        ▼
2. MERCHANDISING    setup Printify → pricing (contribution margin) → product page (GPSR)
        │  → ĐĂNG SẢN PHẨM LIVE LÊN SHOPBASE
        │  gate: no GPSR clearance → no publish (đơn EU)
        ▼
   ┌─────────────────────────────────────────────────┐
   │  QUY TẮC CỨNG: Sản phẩm PHẢI live trên ShopBase  │
   │  TRƯỚC khi Growth tạo content / chạy ads.        │
   └─────────────────────────────────────────────────┘
        ▼
3. GROWTH           creative → FB Ads (page Facebook) → email/organic
        │  gate: no Meta Ad Policy → no ads
        ▼
4. FULFILLMENT & CX  route Printify ≤24h → tracking → support
        ▼
5. BACKOFFICE       finance / compliance / workforce (hỗ trợ xuyên suốt)
```

## Lý do quy tắc ShopBase-first
- Ads Facebook trỏ traffic về **landing là product page trên ShopBase**. Không có page live → ads không có đích → đốt tiền.
- CAPI/Pixel gắn trên ShopBase phải hoạt động trước khi chạy ads (đo conversion).
- GPSR label phải có trên page (đơn EU) trước khi public → tránh vi phạm trước khi quảng cáo kéo khách EU.

## Enforce ở đâu
| Orchestrator | Trách nhiệm |
|--------------|-------------|
| vibe-eu-opc-prd-orchestrator | Chỉ handoff **cleared design** cho Merch (KHÔNG thẳng Growth) |
| vibe-eu-opc-mer-orchestrator | Đăng ShopBase live xong mới set cờ `handoff_to_growth=true` |
| vibe-eu-opc-grw-orchestrator | KHÔNG nhận batch nếu sản phẩm chưa live trên ShopBase |

## Liên quan
- [unit-economics](./unit-economics.md) — pricing & ROAS
- Promote theo đợt: SOP-MER-006 (batch 5–10 SP chạy xuyên 3 phòng)
