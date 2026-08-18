# SOP-BCK-002 — Profit & ROAS Reconciliation (US)
**Version:** 1.0 · **Date:** 2026-08-04 · **Responsible AI:** `vibe-us-warm-bck-finance`
## Mục tiêu: đối soát profit thật per-SKU theo contribution + BE-ROAS (unit-economics). KHÔNG hard-code ROAS 2.5. US no VAT.
## IPO: Input books + ad-spend + BE-ROAS → Output profit-report.json. Gate: profit dùng contribution sau ad+fee (no VAT), BE-ROAS per-SKU.
## RACI: R bck-finance · C grw (spend), mer (BE-ROAS). Links: [unit-economics](../../../_shared/unit-economics.md).
## History: 1.0 2026-08-04 khởi tạo — contribution/BE-ROAS US (không lặp bug EU gross/2.5).
