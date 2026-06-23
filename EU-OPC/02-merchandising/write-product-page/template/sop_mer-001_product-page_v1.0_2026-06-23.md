# SOP-MER-001 — Product Page Copy + Upsell + GPSR Label

**Dept:** 02-merchandising (`mer`) · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-merch-product-page` · **Accountable:** OPC

---

## 0. IPO Analysis

| | |
|---|---|
| **Input (I)** | Product blueprint (variant XS–3XL/color) từ MER-002; mockup; cleared design info từ phòng 01; **GPSR clearance log + nhãn an toàn** từ phòng 05; brand voice DAKOfits |
| **Control (C)** | Gate **no-GPSR-no-publish** (EU); mobile CRO checklist 12 elements; brand voice; ShopBase PDP schema; social proof policy |
| **Output (O)** | Product page copy publish-ready (EN): title, bullets, description, size guide XS–3XL, upsell/bundle sports-bra, social proof, **GPSR label block (đơn EU)** |
| **Mechanism (M)** | Product-Page AI + OPC review |
| **Upstream** | MER-002 (blueprint), 05-backoffice (GPSR clearance) |
| **Downstream** | MER-004 (catalog sync) → publish |

---

## 1. Tổng Quan

Viết product page copy cho AOP leggings/activewear tối ưu mobile conversion (traffic 100% FB Ads → ~80% mobile), kèm upsell/bundle sports-bra, và **chèn nhãn GPSR cho đơn EU** trước khi cho phép publish. Tham chiếu phong cách Gearbunch.

## 2. Vai Trò & RACI + AI Roles

| Hoạt động | OPC | Product-Page AI | 05-Backoffice | MER-002 |
|-----------|-----|-----------------|---------------|---------|
| Viết copy + CRO + upsell | A | **R** `[AI WORKFORCE]` | I | C |
| Cung cấp GPSR clearance/label | I | C | **R** | — |
| Chèn GPSR label vào PDP | A | **R** `[AI WORKFORCE]` | C | — |
| Approve publish (gate) | **A/R** | I | C | I |

`[AI WORKFORCE]` = skill `vibe-opc-pod-merch-product-page` chạy.

## 3. Quy Trình

### Bước 1 — Nhận input & kiểm GPSR gate
| ICOM | Nội dung |
|------|----------|
| I | Blueprint, mockup, GPSR clearance log ID (SOP-BCK-004) |
| C | Gate no-GPSR-no-publish **fail-closed** — verify clearance log ID status=PASS, không chỉ check string |
| O | Go/No-go cho SP EU |
| M | Product-Page AI |

| Hành động | Ai |
|-----------|-----|
| Đọc blueprint + xác định thị trường (US / EU / cả hai) | AI |
| **Verify clearance log ID hợp lệ** từ SOP-BCK-004: tra log có **status = PASS** cho đúng SP/design — KHÔNG chỉ check string nhãn trên page (nhãn rỗng vẫn pass string) | AI |
| **Fail-closed:** thiếu clearance log ID / không tìm thấy bản ghi / status ≠ PASS → **block publish**, escalate phòng 05. Mặc định BLOCK khi không xác nhận được. | AI |

### Bước 2 — Viết copy + Mobile CRO
| ICOM | Nội dung |
|------|----------|
| I | Design info, brand voice, CRO checklist |
| C | 12 CRO elements, brand voice |
| O | Title + bullets + description + size guide |
| M | Product-Page AI |

| Hành động | Ai |
|-----------|-----|
| Title (benefit + niche), 5 bullet scannable, description story | AI `[AI WORKFORCE]` |
| Size guide XS–3XL (đo cm/inch), care info AOP 360° | AI |
| CRO mobile: above-fold CTA, badge trust, ảnh mockup, urgency nhẹ | AI |

### Bước 3 — Social proof + Upsell/Bundle
| ICOM | Nội dung |
|------|----------|
| I | Review pool, sports-bra SKU |
| C | Social proof policy, bundle rule |
| O | Review block + bundle sports-bra |
| M | Product-Page AI |

| Hành động | Ai |
|-----------|-----|
| Chèn social proof (rating, review snippet, UGC) | AI |
| Tạo upsell/bundle leggings + sports-bra (cùng AOP) | AI `[AI WORKFORCE]` |

### Bước 4 — Chèn nhãn GPSR (đơn EU)
| ICOM | Nội dung |
|------|----------|
| I | GPSR label text + Responsible Person từ phòng 05 |
| C | GPSR Regulation (EU) 2023/988 |
| O | GPSR label block trên PDP |
| M | Product-Page AI |

| Hành động | Ai |
|-----------|-----|
| Chèn block: tên+địa chỉ Responsible Person (EU), cảnh báo an toàn, care/material, mã SP | AI `[AI WORKFORCE]` |
| Verify label render đúng trên PDP EU; SP US không bắt buộc nhưng giữ care info | AI |

### Bước 5 — OPC review & approve
| ICOM | Nội dung |
|------|----------|
| I | Draft PDP hoàn chỉnh |
| C | Quality Gate MER-001 |
| O | PDP approved → MER-004 |
| M | OPC |

| Hành động | Ai |
|-----------|-----|
| Review copy + CRO completeness + GPSR label | OPC |
| Approve → bàn giao sync (MER-004) | OPC |

## 4. Phân Nhánh

| Điều kiện | Nhánh |
|-----------|-------|
| SP bán EU & clearance log ID thiếu / không tìm thấy / status ≠ PASS | **BLOCK publish** (fail-closed) → escalate 05 |
| SP chỉ bán US | Bỏ qua GPSR label block (giữ care info) |
| CRO completeness < 95% | Trả AI bổ sung elements |
| Không có sports-bra cùng niche | Upsell SKU generic activewear |

## 5. Checklist

**Quality Gate (SLI/SLO)**
| SLI | SLO | Đo |
|-----|-----|-----|
| GPSR clearance verified (EU) | = 100% | verify clearance log ID status=PASS (SOP-BCK-004), KHÔNG chỉ check string |
| GPSR label present rate (EU) | = 100% | check string PDP **+** khớp nội dung với clearance log (nhãn rỗng = fail) |
| Mobile CRO completeness | ≥ 95% (/12) | checklist |
| Upsell block present | = 100% PDP | check |
| Size guide XS–3XL | đủ size | check |

**Prevention**
| Rủi ro | Phòng ngừa |
|--------|-----------|
| Publish EU thiếu GPSR (phạt) | Gate bước 1 verify clearance log ID PASS, **fail-closed**, không bypass |
| Nhãn rỗng/giả vẫn pass string | Gate dựa vào clearance log ID, không tin string trên page |
| Copy không mobile-friendly | CRO checklist bắt buộc |
| Quên upsell → mất AOV | Bundle là element bắt buộc |

## 6. Tài Nguyên & Links

- Template: `write-product-page/template/`
- Upstream: [SOP-MER-002](../../setup-printify/template/sop_mer-002_printify-setup_v1.0_2026-06-23.md)
- GPSR clearance: phòng 05-backoffice (SOP-BCK-004)
- Downstream: [SOP-MER-004](../../sync-catalog/template/sop_mer-004_catalog-sync-qc_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

## 7. Lịch Sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo SOP product page + GPSR label |
| v1.1 | 2026-06-23 | GPSR gate fail-closed: verify clearance log ID status=PASS (SOP-BCK-004) thay vì chỉ check string nhãn; thiếu/không-PASS → block publish |
