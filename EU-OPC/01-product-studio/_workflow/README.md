# _workflow — 01-Product Studio

**Ngày:** 2026-06-23 · **Dept:** prd · Index 4 SOP + assignment + dependency.

## SOP Index
| SOP | Tên | Folder | AI Worker | Output |
|-----|-----|--------|-----------|--------|
| PRD-001 | Niche Research đa-niche | research-niche/ | niche-research | Validated niche list |
| PRD-002 | Trend & Seasonal Calendar | analyze-trend/ | niche-research | Seasonal calendar |
| PRD-003 | AOP Design print-ready | design-aop/ | product-design | Design 300 DPI + mockup |
| PRD-004 | IP/TM Clearance | clear-ip/ | product-design | IP-clearance log |

## Dependency (DAG)
```
00-company strategy
        │
   ┌────▼─────┐
   │ PRD-001  │ niche-research
   └────┬─────┘
        │ validated niche list
   ┌────▼─────┐
   │ PRD-002  │ niche-research (seasonal timing)
   └────┬─────┘
        │ niche + deadline
   ┌────▼─────┐
   │ PRD-003  │ product-design (AOP 300 DPI)
   └────┬─────┘
        │ design print-ready
   ┌────▼─────┐
   │ PRD-004  │ product-design (IP/TM GATE)
   └────┬─────┘
        │ chỉ CLEAR
        ▼
   02-merchandising
```

## AI Worker Assignment
| AI Worker | SOP | Trigger |
|-----------|-----|---------|
| vibe-opc-pod-product-niche-research | PRD-001, PRD-002 | Weekly research cycle / niche pool update |
| vibe-opc-pod-product-design | PRD-003, PRD-004 | Mỗi validated niche tới deadline |

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
| PRD-003 → PRD-004 | Design pass QC 360° + 300 DPI |
| PRD-004 → 02-merch | Status = CLEAR (gate cứng) |
