# Pipeline Dependency Map — SOP cross-links

> Luồng phụ thuộc giữa các SOP. Mỗi SOP nhận input từ upstream, trả output cho downstream. Platform: ShopBase + Facebook Ads | Niche: Dog Breed AOP Leggings | Market: US + EU.

```
PRD-001 niche (breed) ─┐
PRD-002 season ────────┴─> PRD-003 design (AOP) ─> PRD-004 QC+IP/TM ─┐ (gate IP/TM)
                                                                     ├─> MER-001 product page ─┐
BCK-004 GPSR clearance ──────────────────(gate GPSR, đơn EU)─────────┘                         │
MER-002 printify+EU provider ─> MER-003 pricing ──────────────────────────────────────────────┤
                                                                                               ├─> MER-004 sync/publish (ShopBase) ─> live product
                                                                                               │
live product ─> GRW-005 fb-creative ─> GRW-002 fb-ads (paid traffic) ─> traffic ─> ĐƠN HÀNG
              └ GRW-001 organic social/community + GRW-003 email (Klaviyo) ─ hỗ trợ ──┘
ĐƠN ─> FUL-001 order ─> FUL-002 tracking ─> FUL-003 CX ─> FUL-004 returns
                                                  │
doanh thu/chi phí ─> BCK-001 bookkeeping ─> BCK-002 VAT/OSS ─> BCK-003 profit-per-SKU
GRW-004 growth report (ROAS/CPA/AOV) + BCK-003 ─> Founder (OKR/strategy)
compliance xuyên suốt: BCK-004 GPSR (đơn EU) · BCK-005 GDPR · PRD-004 IP/TM · Meta Ad Policy
```

> Traffic = 100% Facebook Ads (GRW-002 paid). Organic social/community (GRW-001) + email (GRW-003) chỉ hỗ trợ, không phải kênh traffic chính. Etsy hạ xuống reference/inactive.

## Gate chặn cứng (eliminate)
| Gate | Ở SOP | Điều kiện | Nếu fail |
|---|---|---|---|
| IP/TM | PRD-004 → MER-001 | design qua IP/TM check (breed name) | BLOCK listing |
| GPSR | BCK-004 → MER-001/MER-004 | đơn EU có GPSR clearance + RP + nhãn | BLOCK publish |
| Margin | MER-003 | gross margin ~45–55% (ShopBase) | không publish |
| Consent | GRW-003 | người nhận opt-in (GDPR) | không gửi email |
| ROAS | GRW-002 | ROAS ≥ 2.5 (floor) | pause campaign |
| Meta Ad Policy | GRW-002/GRW-005 | creative + ad đạt Meta Ad Policy | không chạy ads |
