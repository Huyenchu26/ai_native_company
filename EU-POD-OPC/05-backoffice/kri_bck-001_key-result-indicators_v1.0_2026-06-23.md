# KRI — 05-Backoffice (bck) · Key Risk/Result Indicators

**Version:** v1.0 · **Ngày:** 2026-06-23 · **Đo bởi:** finance / compliance / ops-hr AI
> KRI = chỉ báo sớm rủi ro. Vượt threshold → escalate Owner.

---

## Compliance KRI (gate cứng)
| KRI | Định nghĩa | Green | Amber | Red (escalate) |
|---|---|---|---|---|
| gpsr_clearance_rate | % SP EU cleared trước publish | 100% | — | < 100% → block publish |
| vat_ontime_rate | % kỳ VAT đúng hạn | 100% | — | < 100% → legal risk |
| breach_response_time | giờ tới notify | ≤ 72h | 48–72h | > 72h → vi phạm GDPR |
| dsar_ontime_rate | % DSAR ≤ 1 tháng | 100% | 90–99% | < 90% |
| iptm_clearance_rate | % SP có IP/TM clear trước listing | 100% | — | < 100% → takedown risk |
| meta_ad_policy_pass | % campaign pass policy review | ≥ 99% | 95–99% | < 95% → ban risk |

## Finance KRI
| KRI | Định nghĩa | Green | Amber | Red |
|---|---|---|---|---|
| net_margin | Net profit / revenue | ≥ 20% | 15–20% | < 15% |
| bookkeeping_accuracy | % giao dịch khớp | ≥ 99.9% | 99–99.9% | < 99% |
| blended_roas | Revenue / ad-spend (feed Growth) | ≥ 2.5 | 2.0–2.5 | < 2.0 |
| fee_discrepancy | % chênh fee vs kỳ vọng | < 1% | 1–2% | > 2% → escalate |
| fx_traceability | % figure có nguồn tỷ giá | 100% | — | < 100% |
| brief_ontime | % CEO brief đúng hạn | 100% | 90–99% | < 90% |

## Workforce KRI
| KRI | Định nghĩa | Green | Amber | Red |
|---|---|---|---|---|
| ai_worker_uptime | % uptime TB 12 worker | ≥ 99% | 95–99% | < 95% |
| output_reject_rate | % output bị human-review reject | < 10% | 10–20% | > 20% → retrain |
| cost_per_worker_variance | chênh cost vs tuần trước | < 20% | 20–30% | > 30% → cost alert |
| workforce_report_ontime | % tuần có report | 100% | 90–99% | < 90% |
| capacity_headroom | % công suất còn dư | > 20% | 10–20% | < 10% → scale |

## Escalation
Bất kỳ KRI **Red** → ops-hr/compliance/finance AI mở escalation ticket → Owner trong 24h (gate cứng compliance: ngay lập tức).
