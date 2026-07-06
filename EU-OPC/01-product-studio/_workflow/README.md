# _workflow — 01-Product Studio

**Ngày:** 2026-06-23 · **Dept:** prd · Index 4 SOP + assignment + dependency.

## SOP Index
| SOP | Tên | Folder | AI Worker | Output |
|-----|-----|--------|-----------|--------|
| PRD-001 | Niche Research đa-niche | research-niche/ | niche-research | Validated niche list |
| PRD-002 | Trend & Seasonal Calendar | analyze-trend/ | niche-research | Seasonal calendar |
| PRD-003 | AOP Design print-ready | design-aop/ | product-design | Design 300 DPI + mockup |
| PRD-004 | IP/TM Clearance | clear-ip/ | product-design | IP-clearance log |
| PRD-005 | Nhân Winner (Amplify) | amplify-winner/ | niche-research + product-design | 3–5 candidate từ SP win → design → gate |

## Dependency (DAG)
```
00-company strategy          ┌───────────────────────────────────┐
        │                    │ FEEDBACK LOOP (winner)             │
   ┌────▼─────┐              │ _shared/winner-registry.json      │
   │ PRD-001  │ niche-research│ (Growth ghi khi campaign SCALE)  │
   └────┬─────┘◄─────────────┤                                   │
        │ validated niche list│  ┌──────────┐                    │
   ┌────▼─────┐              └──│ PRD-005  │ Nhân Winner         │
   │ PRD-002  │ niche-research   │ (amplify)│ niche-research      │
   └────┬─────┘                 └────┬─────┘ chọn 3 trục lân cận │
        │ niche + deadline           │ candidate                 │
   ┌────▼─────┐◄──────────────────────┘                          │
   │ PRD-003  │ product-design (AOP 300 DPI)                     │
   └────┬─────┘                                                   │
        │ design print-ready                                     │
   ┌────▼─────┐                                                   │
   │ PRD-004  │ product-design (IP/TM GATE)                      │
   └────┬─────┘                                                   │
        │ chỉ CLEAR                                              │
        ▼                                                        │
   02-merchandising ──► 03-growth ads ──► SCALE ─────────────────┘
                                          (ghi winner-registry)
```
> **Closed-loop:** SP thắng ở Growth → ghi `_shared/winner-registry.json` → **PRD-005** đọc, nhân 3–5 candidate lân cận (cùng niche/khác design, cùng design/niche lân cận, khác market) → vào lại PRD-003/004 → Merch đợt kế.

## AI Worker Assignment
| AI Worker | SOP | Trigger |
|-----------|-----|---------|
| vibe-opc-pod-product-niche-research | PRD-001, PRD-002, PRD-005 (chấm candidate lân cận) | Weekly research cycle / niche pool update / winner mới trong registry |
| vibe-opc-pod-product-design | PRD-003, PRD-004 | Mỗi validated niche tới deadline (kể cả candidate từ PRD-005) |

## Folder I/O Convention (per SOP folder)
| Folder | Vai trò |
|--------|---------|
| input/ | Data nguồn (AdSpy/Meta/Trends export, niche brief) |
| processing/ai-draft/ | AI Worker sinh draft |
| processing/human-review/ | OPC review (HIGH-risk, sample 20%) |
| output/ | Artifact đã duyệt → handoff downstream |
| archive/ | Lưu phiên bản cũ |
| template/ | SOP .md + template artifact |

## Handoff gate
| Từ → Đến | Điều kiện |
|----------|-----------|
| winner-registry → PRD-005 | Record `status=WINNER` (Growth đã ghi, blended ≥ BE-ROAS) |
| PRD-005 → PRD-003 | Candidate score ≥ 70 + audience ≥ 500k + IP/TM pre-flag pass |
| PRD-003 → PRD-004 | Design pass QC 360° + 300 DPI |
| PRD-004 → 02-merch | Status = CLEAR (gate cứng) |
