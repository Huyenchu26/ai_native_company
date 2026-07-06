# DAKOfits — Company Routing Map (đầy đủ)

**Cho:** vibe-dakofits-gps · **Ngày:** 2026-06-23 · **24 SOP · 5 phòng · 17 AI Worker EU-OPC**

## Tên người ↔ Mã skill (user gọi tên nào cũng map đúng)
| Tên | Skill | Tên | Skill |
|-----|-------|-----|-------|
| anh Khởi | prd-orchestrator | anh Vận | ful-orchestrator |
| chị Tầm | prd-niche-research | anh Giao | ful-order-ops |
| anh Họa | prd-design | chị Chăm | ful-cx |
| chị Hàng | mer-orchestrator | anh Quản | bck-orchestrator |
| anh Định | mer-catalog | chị Kế | bck-finance |
| chị Lời | mer-product-page | anh Luật | bck-compliance |
| anh Phát | grw-orchestrator | chị Nhân | bck-ops-hr |
| anh Quảng | grw-fb-ads | **anh Tổng** | **(chính là GPS này)** |
| chị Ý | grw-creative | | |
| chị Thư | grw-marketing | | |
(mã đầy đủ: `vibe-eu-opc-[code]`. Roster: ../../team-roster.md). Khi user gọi tên người → map sang skill tương ứng rồi route.

---

## Bảng routing đầy đủ: SOP → Skill

| SOP | Tên nghiệp vụ | Phòng | Skill (route đến) |
|-----|---------------|-------|-------------------|
| PRD-001 | Niche research & demand scoring | 01 | vibe-eu-opc-prd-niche-research |
| PRD-002 | Trend & seasonal calendar | 01 | vibe-eu-opc-prd-niche-research |
| PRD-003 | AOP design print-ready | 01 | vibe-eu-opc-prd-design |
| PRD-004 | IP/TM clearance & QC | 01 | vibe-eu-opc-prd-design |
| MER-001 | Product page copy + upsell + GPSR label | 02 | vibe-eu-opc-mer-product-page |
| MER-002 | Printify/PrintBase setup | 02 | vibe-eu-opc-mer-catalog |
| MER-003 | Variant & pricing (contribution margin) | 02 | vibe-eu-opc-mer-catalog |
| MER-004 | Catalog sync & QC (ShopBase) | 02 | vibe-eu-opc-mer-catalog |
| MER-006 | Promote theo đợt (batch) | 02 | vibe-eu-opc-mer-orchestrator |
| GRW-001 | Organic social & community | 03 | vibe-eu-opc-grw-marketing |
| GRW-002 | FB Ads campaign | 03 | vibe-eu-opc-grw-fb-ads |
| GRW-003 | Email & promotions (Klaviyo) | 03 | vibe-eu-opc-grw-marketing |
| GRW-004 | Growth report (KPI/KRI) | 03 | vibe-eu-opc-grw-fb-ads |
| GRW-005 | FB ad creative | 03 | vibe-eu-opc-grw-creative |
| FUL-001 | Order monitoring & verify | 04 | vibe-eu-opc-ful-order-ops |
| FUL-002 | Fulfillment routing & tracking | 04 | vibe-eu-opc-ful-order-ops |
| FUL-003 | CX support (EN) | 04 | vibe-eu-opc-ful-cx |
| FUL-004 | Returns, refunds & exchange | 04 | vibe-eu-opc-ful-cx |
| BCK-001 | Bookkeeping & fee reconciliation | 05 | vibe-eu-opc-bck-finance |
| BCK-002 | Profit-per-SKU & ROAS | 05 | vibe-eu-opc-bck-finance |
| BCK-003 | VAT OSS/IOSS | 05 | vibe-eu-opc-bck-finance |
| BCK-004 | GPSR compliance (clearance issuer) | 05 | vibe-eu-opc-bck-compliance |
| BCK-005 | GDPR | 05 | vibe-eu-opc-bck-compliance |
| BCK-006 | AI workforce ops/HR | 05 | vibe-eu-opc-bck-ops-hr |

> Mặc định route đến **orchestrator phòng**; chỉ gọi thẳng specialist khi task rõ ràng 1 nghiệp vụ.

## Chuỗi đa-phòng chuẩn (operating-flow, ShopBase-first)
```
[1] prd-orchestrator   niche → design → IP/TM clear        (gate: IP/TM)
        ↓ chỉ design PASS
[2] mer-orchestrator   setup+pricing → product-page         (gate: GPSR cho EU)
        + bck-compliance cấp clearance log ID
        → ĐĂNG SP LIVE LÊN SHOPBASE
        ↓ chỉ khi ShopBase live (shopbase_live_before_ads=true)
[3] grw-orchestrator   creative → FB Ads                    (gate: Meta Ad Policy)
        ↓ đơn về
[4] ful-orchestrator   route ≤24h + CX                      (gate: refund $30)
        ↓ cost/refund data
[5] bck-orchestrator   finance + compliance + workforce + CEO brief
```

## Gate ownership
| Gate | Owner cấp | Verifier |
|------|-----------|----------|
| IP/TM clearance | prd-design | prd-orchestrator (chặn handoff) |
| GPSR clearance | bck-compliance (log ID) | mer-product-page / mer-catalog |
| ShopBase-live-before-ads | mer-orchestrator (set handoff_to_growth) | grw-orchestrator |
| Meta Ad Policy | bck-compliance (pre-check) | grw-creative / grw-fb-ads |
| Refund > $30 | — | ful-cx → OPC |
| Pricing / break-even ROAS | — | mer-catalog + bck-finance |

## Legacy fallback (không còn cần — 5 phòng đã activated)
12 skill `vibe-opc-pod-*` vẫn còn cài; chỉ dùng nếu 1 skill EU-OPC lỗi. Ưu tiên luôn dùng `vibe-eu-opc-*`.

## Escalate OPC khi
- Gate fail không tự giải quyết được · budget ads > $150/ngày · refund > $30 · GDPR breach · trademark REJECT · confidence < 0.7.
