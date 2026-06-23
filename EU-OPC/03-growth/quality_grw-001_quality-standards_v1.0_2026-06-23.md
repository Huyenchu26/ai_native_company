# Quality Standards — 03-growth (SLI / SLO / Error Budget)

**Dept:** grw · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** OPC · **Đo bởi:** `vibe-opc-pod-growth-fb-ads` (SOP-GRW-004)

> SLI = đo được, định lượng. SLO = mục tiêu. Error budget = mức sai cho phép trước khi escalate. Mọi target mang *confidence_score* + *need_review*.

---

## SOP-GRW-002 — FB Ads
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Blended ROAS | ≥ 2.5 | ≤ 20% campaign-days dưới ngưỡng/tháng |
| CPA | < $20 | ≤ 15% ad sets vượt |
| CTR (link) | ≥ 1.0% | — |
| CAPI Event Match Quality | ≥ 6.0/10 | < 5% thời gian dưới 6 |
| BM ban rate | < 1 account/tháng; **0 sập toàn bộ** | 0 tolerance cho "sập toàn bộ" |
| Scale discipline | ≤ 20%/2 ngày | 0 vi phạm |

*evidence: ngưỡng từ Company OKR + gross margin AOP · confidence: 0.8 · need_review: false*

## SOP-GRW-005 — Creative
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Hook retention 3s | ≥ 30% | ≤ 25% creative dưới ngưỡng |
| Policy pass (handoff đầu) | ≥ 95% | ≤ 5% rework |
| Variant/SP cho ABO | ≥ 2 | 0 vi phạm |

*confidence: 0.65 · need_review: false (benchmark creative chưa nhiều)*

## SOP-GRW-003 — Email (Klaviyo)
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Deliverability | ≥ 98% | ≤ 2% |
| Spam complaint | < 0.1% | hard cap |
| Consent compliance (opt-in) | 100% | **0 tolerance (GDPR)** |
| Cart-recovery rate | ≥ 10% | — |

*confidence: 0.75 · need_review: false*

## SOP-GRW-001 — Organic
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Post cadence đúng lịch | ≥ 90% | ≤ 10% trễ |
| Community-rule compliance | 100% (0 ban) | 0 tolerance |
| Engagement rate | ≥ benchmark niche | — |

*confidence: 0.6 · need_review: false*

## SOP-GRW-004 — Report
| SLI | SLO | Error budget |
|-----|-----|--------------|
| Report đúng cadence | 100% | ≤ 1 trễ/tháng |
| Data reconcile vs 05-finance | sai lệch < 2% | hard cap |
| Alert latency (ngưỡng→báo) | < 24h | — |

*confidence: 0.8 · need_review: false*

---

## Error-Budget Policy
- Vượt error budget của bất kỳ SLO → `fb-ads` flag trong growth report, escalate OPC.
- **0-tolerance items** (BM sập toàn bộ, GDPR consent, spam cap, data reconcile) → dừng/HOLD ngay, không tiêu error budget.
- Gate cứng (Meta Ad Policy, GDPR opt-in) đứng trên mọi SLO — vi phạm = stop, không phải "trong budget".
