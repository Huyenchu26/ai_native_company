# _rules — 05-Backoffice

Rules cứng + decision authority + escalation. Vi phạm rule cứng → block + escalate Owner.

---

## Rule cứng (Hard Gates)
| # | Rule | SOP | Hệ quả nếu vi phạm |
|---|---|---|---|
| R1 | **No GPSR clearance → No publish (EU)** | BCK-004 | compliance AI block Merch publish EU |
| R2 | **No Meta Ad Policy → No ads** | BCK-004/_knowledge | block Growth campaign |
| R3 | **No IP/TM clearance → No listing** | BCK-004 | block Product/Merch listing |
| R4 | **GDPR breach → notify ≤ 72h** | BCK-005 | timer cứng, Owner notify authority |
| R5 | **VAT filing 100% on-time** | BCK-003 | legal deadline, không trễ |
| R6 | **No fabricated figures/FX** | BCK-001/002 | dùng evidence + nguồn; thiếu → `need_review`, không bịa |

## Decision Authority
| Quyết định | Ai quyết | Ai thực thi |
|---|---|---|
| GPSR PASS/FAIL | compliance AI (theo checklist) | compliance AI |
| GPSR FAIL → exception | **Owner** (ký) | compliance AI |
| Nộp tờ khai VAT | **Owner** | finance AI draft |
| Khóa sổ kỳ | **Owner** | finance AI |
| Breach notify authority | **Owner** | compliance AI draft |
| Kill/scale SKU (từ profit) | **Owner** | finance AI đề xuất, Merch/Growth thực thi |
| Bump skill/SOP worker | **Owner** | ops-hr AI |

> Nguyên tắc: AI Worker **Responsible** ra quyết định kỹ thuật theo checklist; mọi quyết định **legal/tài chính/roster** cần Owner = **Accountable**.

## Escalation
| Trigger | Tới | Thời hạn |
|---|---|---|
| KRI Red bất kỳ | Owner | 24h |
| Gate cứng FAIL (R1–R5) | Owner | ngay lập tức |
| Breach rủi ro cao | Owner | trong 72h clock |
| Fee discrepancy > 2% | Owner | trong kỳ |
| AI worker uptime < 95% | Owner + root cause | 24h |
| Cost spike > 30% | Owner (qua finance) | weekly report |

## Guardrails (anti-hallucination)
- Mọi OKR/SLO mang **evidence + confidence_score + need_review** (đồng bộ vibe-company v2.0).
- Compliance SLO = 100% có evidence = legal mandate (confidence cao, need_review = false).
- Target không baseline → need_review = true → review-queue.
- Audit trail mọi clearance/breach/close trong `archive/` (immutable).
