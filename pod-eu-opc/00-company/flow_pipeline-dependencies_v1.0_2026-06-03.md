# Pipeline Dependency Map — SOP cross-links

> Luồng phụ thuộc giữa các SOP. Mỗi SOP nhận input từ upstream, trả output cho downstream.

```
PRD-001 niche ─┐
PRD-002 season ┴─> PRD-003 design ─> PRD-004 QC+IP ─┐ (gate IP)
                                                     ├─> MER-001 listing ─┐
BCK-004 GPSR clearance ──────────────────(gate GPSR)─┘                    │
MER-002 printify+EU provider ─> MER-003 pricing ─────────────────────────┤
                                                                          ├─> MER-004 sync/publish ─> live listing
                                                                          │
live listing ─> GRW-001 pinterest / GRW-002 ads / GRW-003 email ─> traffic ─> ĐƠN HÀNG
ĐƠN ─> FUL-001 order ─> FUL-002 tracking ─> FUL-003 CX ─> FUL-004 returns
                                                  │
doanh thu/chi phí ─> BCK-001 bookkeeping ─> BCK-002 VAT/OSS ─> BCK-003 profit-per-SKU
GRW-004 report + BCK-003 ─> Founder (OKR/strategy)
compliance xuyên suốt: BCK-004 GPSR · BCK-005 GDPR · PRD-004 IP
```

## Gate chặn cứng (eliminate)
| Gate | Ở SOP | Điều kiện | Nếu fail |
|---|---|---|---|
| IP | PRD-004 → MER-001 | design có IP-clearance | BLOCK listing |
| GPSR | BCK-004 → MER-001/MER-004 | có GPSR clearance + RP | BLOCK publish |
| Margin | MER-003 | margin ≥ 30% | không publish |
| Consent | GRW-003 | người nhận opt-in | không gửi email |
| ROAS | GRW-002 | ROAS ≥ 2.5 | pause campaign |
