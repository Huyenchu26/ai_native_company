# DAKOfits — Value Chain (Porter, 3 Layer)

**Phiên bản:** 1.0 · **Ngày:** 2026-06-23 · **Industry:** POD e-commerce (AOP activewear)

---

## ASCII Value Chain

```
[Value Chain: DAKOfits — POD AOP Activewear, US + EU]

┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: STRATEGY                                                │
│  Owner (CEO) → Strategy / OKR → Budget allocation                │
│  Output: Vision, Quarterly OKR, Ad budget, Niche bets            │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: OPERATIONS (Primary — POD value chain)                 │
│                                                                   │
│  ┌────────────┐  ┌────────────┐  ┌──────────┐  ┌──────────────┐ │
│  │ 01 Product │→│ 02 Merch-  │→│ 03 Growth │→│ 04 Fulfill   │ │
│  │ Studio     │  │ andising   │  │ (FB Ads) │  │ & CX         │ │
│  │ niche+AOP  │  │ catalog+   │  │ creative+│  │ order route  │ │
│  │ design     │  │ page+price │  │ email    │  │ + support    │ │
│  └────────────┘  └────────────┘  └──────────┘  └──────────────┘ │
│   PRD-001..004    MER-001..006    GRW-001..005   FUL-001..004   │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: SUPPORT                                                 │
│  ┌──────────────── 05 Backoffice ─────────────────┐             │
│  │ Finance (BCK-001/002/003) · Compliance GPSR/GDPR │           │
│  │ (BCK-004/005) · Ops-HR AI Workforce (BCK-006)    │           │
│  └──────────────────────────────────────────────────┘           │
│   ↑ Hỗ trợ toàn bộ Layer 2 ↑                                    │
└─────────────────────────────────────────────────────────────────┘
```

## Mermaid

```mermaid
graph TB
    subgraph L1["LAYER 1: STRATEGY"]
        CEO[Owner / Strategy / OKR]
    end
    subgraph L2["LAYER 2: OPERATIONS"]
        PRD[01 Product Studio] --> MER[02 Merchandising]
        MER --> GRW[03 Growth / FB Ads]
        GRW --> FUL[04 Fulfillment & CX]
    end
    subgraph L3["LAYER 3: SUPPORT"]
        BCK[05 Backoffice: Finance / Compliance / Ops-HR]
    end
    CEO --> L2
    BCK --> L2
```

## Cross-department flow (upstream → downstream)
- **Product Studio** → cleared niche + AOP design → **Merchandising**
- **Merchandising** → live product + product page → **Growth**
- **Growth** → đơn hàng từ ads → **Fulfillment & CX**
- **Fulfillment & CX** → fee/cost data → **Backoffice (Finance)**
- **Backoffice (Compliance)** → GPSR clearance → gate cho **Merchandising publish** & **Growth ads**
