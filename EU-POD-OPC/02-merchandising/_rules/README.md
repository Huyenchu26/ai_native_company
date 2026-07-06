# _rules — Phòng 02-Merchandising

**Dept code:** `mer` · **Ngày:** 2026-06-23 · **Version:** v1.0
Guardrail & decision authority cho 2 AI worker. Vi phạm rule cứng → block + escalate.

---

## 1. Hard Gates (không bao giờ bypass)

| # | Rule | Áp dụng | Hệ quả nếu vi phạm |
|---|------|---------|--------------------|
| R1 | **No GPSR clearance → no publish** (đơn EU) | MER-001, MER-004 | Block publish, escalate phòng 05 |
| R2 | **Pricing floor: gross margin ≥ 45%** | MER-003, MER-004 | Block publish, re-price/đổi provider |
| R3 | **Design phải cleared + IP cleared + 360° QC pass** | MER-002 | Trả phòng 01 |
| R4 | **Variant XS–3XL đủ size** trước publish | MER-002, MER-004 | Đổi blueprint |
| R5 | **Catalog sync accuracy ≥ 99%** trước publish | MER-004 | Re-sync |

## 2. Pricing Authority

| Quyết định | Quyền | Ghi chú |
|-----------|-------|---------|
| Set giá trong band 45–55% | **AI tự quyết** | Không cần OPC |
| Giá ngoài band (>55% hoặc <45%) | **OPC duyệt** | <45% mặc định reject |
| Đổi provider để đạt margin | OPC | AI đề xuất |
| Discount/bundle | AI nếu vẫn ≥45%; OPC nếu phá floor | |

## 3. Decision Authority (publish & promote)

| Quyết định | Quyền |
|-----------|-------|
| Approve publish SP | **OPC** (sau gate R1–R5) |
| Chọn 5–10 SP vào đợt promote | **OPC** |
| Scale winner / cut loser | **OPC** |
| Bàn giao batch cho Growth | OPC |

## 4. Escalation Rules

| Tình huống | Escalate đến | SLA |
|-----------|--------------|-----|
| SP EU thiếu GPSR clearance/label | Phòng 05-backoffice (compliance) | ngay |
| Margin không đạt do cost provider | OPC | 24h |
| Design fail QC | Phòng 01-product-studio | ngay |
| Đợt promote toàn loser | OPC + phòng 03-growth | 48h |
| Provider OOS hàng loạt | OPC (đổi provider) | 24h |

## 5. Compliance & Brand

| Rule | Nội dung |
|------|----------|
| ShopBase TOS | Không list hàng cấm / IP vi phạm |
| Brand voice | Giữ tone DAKOfits (activewear, tự tin, niche-specific) |
| Mobile-first | PDP phải pass mobile CRO ≥95% (traffic 100% FB Ads) |
| Channel-agnostic | Đọc `_shared/channel-config`, không hard-code store |

## 6. Liên kết

- Knowledge: [`../_knowledge/README.md`](../_knowledge/README.md)
- Workflow: [`../_workflow/README.md`](../_workflow/README.md)
- Skills/Agents: [`../_skills-agents/README.md`](../_skills-agents/README.md)
- Company gate: GPSR (SOP-BCK-004), Pricing → finance (SOP-BCK-001..003)
