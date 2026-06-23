# _workflow — Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0
Index 5 SOP + dependency graph + review-queue.

---

## 1. SOP Index

| SOP | Tên | Folder | AI Responsible |
|-----|-----|--------|----------------|
| MER-001 | Product Page + Upsell + GPSR label | `write-product-page/` | product-page |
| MER-002 | Setup Printify/PrintBase | `setup-printify/` | catalog-sync |
| MER-003 | Variant Pricing (margin 45–55%) | `set-pricing/` | catalog-sync |
| MER-004 | Catalog Sync + QC | `sync-catalog/` | catalog-sync |
| MER-006 | Promote theo đợt | `promote-batch/` | OPC + 2 worker |

> (MER-005 dành cho mở rộng tương lai — chưa dùng.)

## 2. Dependency Graph (pipeline)

```
[01 cleared design] + [05 GPSR clearance]
        │
        ▼
   MER-002 (setup) ──► MER-003 (pricing) ──► MER-001 (page+GPSR) ──► MER-004 (sync+QC)
        │                                                                   │
        │                                                              live product
        │                                                                   ▼
        └──────────────────────────────────────────────────►  MER-006 (promote theo đợt)
                                                                            │
                                                                            ▼
                                                                     [03-growth ads]
                                                                            │
                                                                  feedback ROAS/CPA
                                                                            ▲
                                                                  scale/cut (vòng lặp)
```

## 3. Dependency Table

| SOP | Cần trước (upstream) | Mở khóa (downstream) | Gate |
|-----|----------------------|----------------------|------|
| MER-002 | 01 cleared design | MER-003 | Design QC |
| MER-003 | MER-002 | MER-001, MER-004 | Pricing floor 45% |
| MER-001 | MER-002 + 05 GPSR | MER-004 | **No GPSR → no publish (EU)** |
| MER-004 | MER-001, 002, 003 | MER-006, 03-growth | Sync ≥99% + GPSR gate |
| MER-006 | MER-004 (live) | 03-growth | Batch 5–10 SP |

## 4. Handoff Schema (vibe-aiworkforce contract)

| Handoff | Từ → Đến | Payload |
|---------|----------|---------|
| Inbound | 01 → mer | cleared design + mockup + IP log |
| Inbound | 05 → mer | GPSR clearance log + label text + Responsible Person |
| Internal | MER-002→003→001→004 | blueprint → pricing → page → live |
| Outbound | mer (MER-006) → 03 | batch promote package |
| Feedback | 03 → mer | ROAS/CPA per SP |

## 5. Review-queue

`need_review = true` (stretch OKR x10, target ngoài band, margin ngoại lệ) → ghi vào [`review-queue.md`](review-queue.md) để OPC duyệt.

## 6. Liên kết

- Knowledge: [`../_knowledge/README.md`](../_knowledge/README.md)
- Rules: [`../_rules/README.md`](../_rules/README.md)
- Skills/Agents: [`../_skills-agents/README.md`](../_skills-agents/README.md)
