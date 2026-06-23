# Charter: Phòng 02-Merchandising — DAKOfits

**Dept code:** `mer` · **Layer:** L2 Vận hành · **Ngày:** 2026-06-23 · **Version:** v1.0
**Owner/Accountable:** OPC · **Mechanism:** AI Workforce (2 worker)

---

## 1. Mission

Biến **cleared design + GPSR clearance** thành **live product bán được** trên ShopBase (AOP leggings & activewear, đa niche ~3.200 SP) — setup đúng provider, pricing đúng margin, product page tối ưu conversion, catalog sạch — rồi điều phối **promote theo đợt** để Growth scale winner. Đóng góp trực tiếp mục tiêu **500tr VND/tháng (~$20k)**.

## 2. Scope

**In-scope:**
- Setup product Printify/PrintBase (US + EU provider), variant size XS–3XL / color.
- Pricing variant theo gross margin 45–55%.
- Viết product page copy + upsell/bundle sports-bra (mobile CRO, social proof), chèn **nhãn GPSR** cho đơn EU.
- Sync ShopBase + catalog QC.
- Promote theo đợt (chọn 5–10 SP → tối ưu listing → bàn giao Growth ads → đọc kết quả → scale winner / cắt loser).

**Out-of-scope:**
- Niche research, design, IP/TM clearance → phòng 01.
- GPSR clearance, Responsible Person, VAT, GDPR → phòng 05.
- Chạy FB Ads, creative video, email → phòng 03.

## 3. Boundaries & Gate

| Gate | Quy tắc | Hệ quả |
|------|---------|--------|
| **GPSR (EU)** | No GPSR clearance từ phòng 05 → **no publish** với SP bán EU | Block publish, escalate phòng 05 |
| **Pricing floor** | Gross margin < 45% → không publish | Re-price hoặc đổi provider |
| **Design QC** | Design chưa cleared/360° fail → trả lại phòng 01 | Không setup |

## 4. Authority (Decision Rights)

| Quyết định | Quyền |
|-----------|-------|
| Chọn provider (Printify vs PrintBase, US vs EU) | OPC (AI đề xuất) |
| Set giá trong khung margin 45–55% | AI tự quyết; ngoài khung → OPC |
| Publish SP | OPC (sau gate GPSR + QC) |
| Chọn SP vào đợt promote, scale/cut | OPC |

## 5. KPI cam kết (xem `kpi_mer-001`)

Sync accuracy ≥99% · GPSR label EU =100% · Gross margin ≥45% · Mobile CRO ≥95% · Time-to-publish ≤48h · Batch winner rate ≥20%.

## 6. Interfaces

| Hướng | Phòng | Handoff |
|-------|-------|---------|
| Upstream | 01-product-studio | Cleared design print-ready + mockup |
| Upstream | 05-backoffice | GPSR clearance log (gate) |
| Downstream | 03-growth | Batch promote package (live SP + listing tối ưu) |
| Feedback | 03-growth → mer | Kết quả ROAS/CPA để scale/cut |

## 7. AI Workforce

| Worker | Skill | SOP phụ trách |
|--------|-------|---------------|
| Catalog-Sync AI | `vibe-opc-pod-merch-catalog-sync` | MER-002, 003, 004 |
| Product-Page AI | `vibe-opc-pod-merch-product-page` | MER-001 |

## 8. Lịch sử

| Version | Ngày | Thay đổi |
|---------|------|----------|
| v1.0 | 2026-06-23 | Khởi tạo charter phòng Merchandising |
