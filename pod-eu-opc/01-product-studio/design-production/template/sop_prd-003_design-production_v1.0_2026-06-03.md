# SOP-PRD-003 — Design brief & production (AOP)

**Department:** Product Studio (prd) · **AI Worker:** Design AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-08** · **ACTIVE**

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Biến validated breed-niche thành **AOP design print-ready** đúng chuẩn kỹ thuật, đủ biến thể (4 loại design). |
| **Phạm vi** | Brief → tạo → export print-ready. QC AOP 360° & IP/TM clearance là PRD-004. |
| **Trigger** | Có validated breed từ PRD-001 / opportunity từ PRD-002. |

### IPO
| | |
|---|---|
| **Input** | Validated niche list (breed) từ PRD-001, brand guidelines, print spec AOP leggings (Printify) |
| **Control** | Print-ready AOP spec, brand voice/visual ("dog mom" identity), phù hợp full-bleed leggings |
| **Output** | AOP design file print-ready + design brief + concept variations (4 loại) |
| **Mechanism** | Design AI + Claude API (brief/prompt), image-gen (Midjourney/Firefly/Ideogram), Canva (tile), Printify mockup |

## 2. AOP Print-ready spec (Knowledge)
- **Độ phân giải:** ≥ 300 DPI
- **Định dạng:** PNG/JPEG full-bleed (AOP — phủ kín mặt vải)
- **Kích thước:** theo template AOP leggings Printify (full coverage)
- **Vùng in:** AOP full-bleed; bố cục liền mạch (seamless) khi mặc trực tiếp, không lỗi đối xứng quanh chân/đường may
- **Màu:** RGB; lưu ý chênh màu in; AOP full-bleed (khác DTG có nền)
- **4 loại design:**
  - **Tile / Pattern Repeat** — lặp hình breed khắp mặt quần (Canva tile, dễ nhất, bán chạy nhất)
  - **Watercolor + Florals** — premium, justify giá cao (Midjourney/Firefly)
  - **Funny / Quote** — viral organic (tránh quote dính TM)
  - **Mandala / Geometric** — silhouette breed trong mandala (EU mạnh, cross-sell yoga)

## 3. RACI
| Hoạt động | Founder | Design AI |
|---|---|---|
| Tạo & export AOP design | I | **R** |
| Duyệt hướng sáng tạo lớn | C | R |

## 4. Đầu vào
- [ ] Validated breed (PRD-001) · [ ] Brand guidelines · [ ] Print spec AOP leggings Printify

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Brief | Soạn design brief từ breed (thông điệp "dog mom", design type, audience US+EU) | [AI AUGMENT] | Brief template chuẩn |
| 5.2 | Concept | Sinh nhiều concept AOP theo 4 loại (prompt image-gen / Canva tile) | [AI AUGMENT] | ≥ N concept để chọn |
| 5.3 | Chọn & refine | Chọn concept tốt nhất, tinh chỉnh seamless | [AI AUGMENT] | Đối chiếu brand fit |
| 5.4 | Export | Xuất print-ready AOP đúng spec §2 (300 DPI full-bleed) | [AI WORKFORCE] | Auto-check DPI/size/format trước khi lưu |
| 5.5 | Handoff QC | Chuyển design + brief sang PRD-004 | [AI WORKFORCE] | Không qua MER khi chưa QC |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Kỹ thuật | DPI/size/format đúng AOP spec | 100% | ☐ |
| 2 | Seamless | pattern liền mạch full-bleed | 100% | ☐ |
| 3 | Số concept | đủ tối thiểu để chọn | đạt | ☐ |
| 4 | Brand fit | đúng visual/voice "dog mom" | đạt | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/design_[breed]_[YYYY-MM-DD]/ (file + brief) → archive/
- **Downstream:** PRD-004 (QC + IP/TM) → MER-001 (Product Page) / MER-002 (Catalog-Sync); asset → FB Creative AI (GRW-005)

## 8. Phụ lục
Knowledge: ../_knowledge/ · Policy brand: ../../../_shared/policies/brand-policy.md · Niche strategy §3 (4 loại design): ../../../docs/08-niche-dog-breed-leggings-shopbase.md
