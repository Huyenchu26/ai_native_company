# SOP-PRD-004 — IP/TM Clearance (Gate cứng trước listing)

| Trường | Giá trị |
|--------|---------|
| **Mã SOP** | SOP-PRD-004 |
| **Phiên bản** | 1.0 |
| **Ngày** | 2026-06-23 |
| **Chủ sở hữu** | Product Studio (dept: prd) |
| **Department** | 01-product-studio |
| **AI Workforce** | `[AI WORKFORCE]` — chạy bởi **vibe-opc-pod-product-design** |

---

## 0. IPO Analysis

| Loại | Mục |
|------|-----|
| **Input (I)** | AOP design print-ready + niche term (PRD-003), IP pre-flag (PRD-001), TM databases (USPTO TESS, EUIPO), brand/celebrity/club blocklist |
| **Control (C)** | **Gate cứng: no clearance → no listing**, clearance rubric (CLEAR / MODIFY / REJECT), thị trường US+EU |
| **Output (O)** | **IP-clearance log** (per design: status + evidence) → chỉ design CLEAR mới handoff 02-merchandising |
| **Mechanism (M)** | AI Worker `product-design` (clearance check) + USPTO/EUIPO lookup; human review HIGH-risk |

**Upstream:** SOP-PRD-003 (design) + SOP-PRD-001 (pre-flag)
**Downstream:** 02-merchandising (listing) — chỉ nhận CLEAR

---

## 1. Tổng Quan

- **Mục đích:** Chặn rủi ro pháp lý IP/TM trước khi bất kỳ SP nào lên store/ads — tên niche (breed, club, brand, character), slogan, logo, artwork không xâm phạm TM tại US+EU.
- **Phạm vi:** Mọi design trước listing. Đây là **gate cứng số 3** của công ty (no IP/TM clearance → no listing).
- **Định nghĩa:**
  - **CLEAR:** không phát hiện rủi ro → được listing.
  - **MODIFY:** sửa term/artwork rồi clear lại.
  - **REJECT:** rủi ro cao, loại bỏ.

## 2. Vai Trò & Trách Nhiệm

**RACI**

| Hoạt động | OPC | AI product-design | AI niche-research | 02-merch |
|-----------|:----:|:----:|:----:|:----:|
| TM lookup (USPTO/EUIPO) | A | R | C | I |
| Phân loại CLEAR/MODIFY/REJECT | A | R | I | I |
| Ghi clearance log | A | R | I | I |
| Approve HIGH-risk | R/A | C | I | I |

**AI Roles**

| AI Worker | Skill | Trách nhiệm |
|-----------|-------|-------------|
| vibe-opc-pod-product-design | IP/TM clearance, blocklist check, clearance logging | Responsible |

## 3. Quy Trình

### Bước 1 — Thu thập term & artwork cần check
| I | C | O | M |
|---|---|---|---|
| Design + niche term + pre-flag | Blocklist | Check item list | AI |

| # | Hành động | Output |
|---|-----------|--------|
| 1.1 | Trích term (tên niche, slogan, logo) | Term list |
| 1.2 | Ưu tiên item có pre-flag HIGH | Sorted list |

### Bước 2 — TM lookup US+EU
| I | C | O | M |
|---|---|---|---|
| Term list | Clearance rubric | Match result | AI product-design |

| # | Hành động | Công cụ |
|---|-----------|---------|
| 2.1 | Tra USPTO TESS | USPTO |
| 2.2 | Tra EUIPO | EUIPO |
| 2.3 | Đối chiếu blocklist brand/celeb/club | Blocklist |

### Bước 3 — Phân loại & log
| I | C | O | M |
|---|---|---|---|
| Match result | CLEAR/MODIFY/REJECT rubric | IP-clearance log | AI + human |

| # | Hành động | Output |
|---|-----------|--------|
| 3.1 | Gán status từng design | Status |
| 3.2 | HIGH-risk → human review | Decision |
| 3.3 | Ghi log ra `output/`, chỉ CLEAR handoff 02-merch | Clearance log |

## 4. Phân Nhánh & Xử Lý Đặc Biệt

| Tình huống | Xử lý |
|-----------|-------|
| TM exact match | REJECT |
| TM similar (cùng class) | MODIFY term/artwork → re-clear |
| Generic descriptive term | CLEAR (ghi evidence) |
| Không chắc | Default conservative → human review, không listing |

## 5. Checklist

**Quality Gate**

| Tiêu chí | SLI | SLO | Check Method | Pass |
|----------|-----|-----|-------------|:----:|
| Clearance coverage | % design có clearance trước listing | 100% (gate cứng) | Clearance log vs catalog | ☐ |
| Lookup hai thị trường | % design check cả USPTO+EUIPO | 100% | Log dual-source | ☐ |
| HIGH-risk review | % HIGH-risk qua human | 100% | Review log | ☐ |
| Clearance turnaround | Clearance time/design | ≤ 12h | Timestamp | ☐ |
| False-clear (đo lùi) | % SP listing bị TM takedown | ≤ 1% | Takedown register | ☐ |

**Prevention Measures**

| Rủi ro | Phòng ngừa |
|--------|-----------|
| Listing dính TM → takedown/ban | Gate cứng no clearance→no listing |
| Bỏ sót thị trường EU | Bắt buộc dual lookup |
| AI tự tin sai | HIGH-risk + uncertain → human, conservative default |

## 6. Tài Nguyên & Tham Chiếu

- **Upstream:** [SOP-PRD-003](../../design-aop/template/sop_prd-003_aop-design_v1.0_2026-06-23.md) · [SOP-PRD-001](../../research-niche/template/sop_prd-001_niche-research_v1.0_2026-06-23.md)
- **Downstream:** 02-merchandising (chỉ nhận CLEAR) · cross-ref Backoffice [SOP-BCK-004 GPSR]
- **AI Skill:** vibe-opc-pod-product-design
- **Rules:** [../../_rules/README.md](../../_rules/README.md) (IP/TM gate)

## 7. Lịch Sử Thay Đổi

| Phiên bản | Ngày | Thay đổi | Tác giả |
|-----------|------|----------|---------|
| 1.0 | 2026-06-23 | Khởi tạo SOP | Company Architect |
