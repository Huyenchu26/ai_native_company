# SOP-PRD-003 — AOP Design Print-Ready (300 DPI, 4 loại)

| Trường | Giá trị |
|--------|---------|
| **Mã SOP** | SOP-PRD-003 |
| **Phiên bản** | 1.0 |
| **Ngày** | 2026-06-23 |
| **Chủ sở hữu** | Product Studio (dept: prd) |
| **Department** | 01-product-studio |
| **AI Workforce** | `[AI WORKFORCE]` — chạy bởi **vibe-opc-pod-product-design** |

---

## 0. IPO Analysis

| Loại | Mục |
|------|-----|
| **Input (I)** | Validated niche list + seasonal calendar (PRD-001/002), brand style guide, print provider spec (Printify/PrintBase AOP legging template, EU+US) |
| **Control (C)** | 300 DPI bắt buộc, AOP 360° wrap QC (seam/crotch/waistband alignment), 4 loại design (tile / watercolor / funny / mandala), color profile (sRGB/CMYK theo provider) |
| **Output (O)** | **AOP design print-ready** (file + mockup) qua QC → handoff PRD-004 (clearance) trước listing |
| **Mechanism (M)** | AI Worker `product-design` + provider mockup generator; human QC |

**Upstream:** SOP-PRD-001/002 (niche + timing)
**Downstream:** SOP-PRD-004 (IP/TM clearance) → 02-merchandising (catalog setup)

---

## 1. Tổng Quan

- **Mục đích:** Biến mỗi validated niche thành AOP design dán full-print lên legging/activewear, đạt chuẩn kỹ thuật in 360° và 1 trong 4 phong cách chuẩn của DAKOfits.
- **Phạm vi:** Từ niche brief → file print-ready + mockup. KHÔNG publish (đó là 02-merch sau khi PRD-004 clear).
- **Định nghĩa:**
  - **AOP (All-Over-Print):** in phủ toàn bộ vải, phải seamless tile để không lộ mối nối.
  - **300 DPI:** mật độ điểm ảnh tối thiểu tại kích thước in thật.
  - **4 loại:** tile (pattern lặp), watercolor (loang màu), funny (graphic vui), mandala (đối xứng).

## 2. Vai Trò & Trách Nhiệm

**RACI**

| Hoạt động | OPC | AI product-design | AI niche-research | 02-merch |
|-----------|:----:|:----:|:----:|:----:|
| Chọn style + tạo design | A | R | C | I |
| QC kỹ thuật AOP 360° | A | R | I | I |
| Tạo mockup | A | R | - | C |
| Approve print-ready | R/A | C | - | I |

**AI Roles**

| AI Worker | Skill | Trách nhiệm |
|-----------|-------|-------------|
| vibe-opc-pod-product-design | AOP design 4 loại, 300 DPI, QC 360° | Responsible |

## 3. Quy Trình

### Bước 1 — Brief → chọn style
| I | C | O | M |
|---|---|---|---|
| Niche brief + calendar | 4-style rule + brand guide | Style brief | AI product-design |

| # | Hành động | Output |
|---|-----------|--------|
| 1.1 | Đọc niche + intent mua | Brief |
| 1.2 | Chọn 1–2 trong 4 style phù hợp niche | Style chosen |

### Bước 2 — Tạo design print-ready
| I | C | O | M |
|---|---|---|---|
| Style brief | 300 DPI + seamless tile + provider template | Design file | AI product-design |

| # | Hành động | Output |
|---|-----------|--------|
| 2.1 | Generate artwork theo provider canvas | PNG/PDF 300 DPI |
| 2.2 | Tạo seamless tile (nếu tile/mandala) | Tile file |
| 2.3 | Đặt theo color profile provider | Color-correct file |

### Bước 3 — QC AOP 360° + mockup
| I | C | O | M |
|---|---|---|---|
| Design file | QC checklist 360° | Print-ready + mockup | AI + human QC |

| # | Hành động | Output |
|---|-----------|--------|
| 3.1 | Kiểm seam/crotch/waistband alignment | QC report |
| 3.2 | Render mockup XS–3XL đại diện | Mockup set |
| 3.3 | Ghi ra `output/` handoff PRD-004 | File |

## 4. Phân Nhánh & Xử Lý Đặc Biệt

| Tình huống | Xử lý |
|-----------|-------|
| DPI < 300 sau scale | Re-generate ở canvas lớn hơn, không upscale |
| Seam lộ mối nối | Quay lại tạo seamless tile |
| Niche IP pre-flag = HIGH | Giữ ở draft, chờ PRD-004 clear mới hoàn thiện |
| Color lệch giữa US vs EU provider | Tách 2 profile, QC từng provider |

## 5. Checklist

**Quality Gate**

| Tiêu chí | SLI | SLO | Check Method | Pass |
|----------|-----|-----|-------------|:----:|
| Độ phân giải | % design ≥ 300 DPI | 100% | File metadata | ☐ |
| AOP 360° pass | % design pass QC 360° (no seam) | ≥ 98% | QC report | ☐ |
| Bleed & canvas khớp provider | % design có bleed ≥ spec provider VÀ canvas đúng kích thước template px thật của Printify/PrintBase (tránh lỗi cắt-may AOP) | 100% | File metadata vs provider template | ☐ |
| Đúng 4 loại style | % design thuộc 1/4 style chuẩn | 100% | Style tag | ☐ |
| Turnaround | Design turnaround time | ≤ 24h/design | Timestamp | ☐ |

**Prevention Measures**

| Rủi ro | Phòng ngừa |
|--------|-----------|
| In ra lộ seam | QC 360° bắt buộc trước handoff |
| File mờ khi in | Lock canvas 300 DPI từ đầu |
| Listing trước clearance | Handoff PRD-004 là cổng bắt buộc |

## 6. Tài Nguyên & Tham Chiếu

- **Upstream:** [SOP-PRD-001](../../research-niche/template/sop_prd-001_niche-research_v1.0_2026-06-23.md) · [SOP-PRD-002](../../analyze-trend/template/sop_prd-002_trend-seasonal_v1.0_2026-06-23.md)
- **Downstream:** [SOP-PRD-004](../../clear-ip/template/sop_prd-004_ip-tm-clearance_v1.0_2026-06-23.md) · 02-merchandising/setup-printify
- **AI Skill:** vibe-opc-pod-product-design

## 7. Lịch Sử Thay Đổi

| Phiên bản | Ngày | Thay đổi | Tác giả |
|-----------|------|----------|---------|
| 1.0 | 2026-06-23 | Khởi tạo SOP | Company Architect |
