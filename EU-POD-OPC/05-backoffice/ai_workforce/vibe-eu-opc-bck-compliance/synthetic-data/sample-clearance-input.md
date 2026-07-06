# Synthetic Data — Sample Clearance Input

1 design mẫu chờ clear cho **cả EU và US** (2 market record). Dùng cho smoke-test.

## Design #1 — "German Shepherd Mandala AOP Leggings"
- **design_id**: DSGN-2026-0623-GSD-MANDALA
- **niche / breed_name**: German Shepherd (dog breed)
- **design_type**: mandala AOP, 300 DPI, seamless tile QC PASS (từ vibe-eu-opc-prd-design)
- **prd_ip_preflag**: "no obvious conflict — breed name generic" (pre-flag, chưa chính thức)
- **product_safety_data**:
  - manufacturer: DAKOfits POD (Printify EU provider)
  - product_id: LEG-GSD-MANDALA-AOP
  - material: 82% polyester / 18% spandex
  - care: machine wash cold, do not iron print
- **provider**: Printify EU (đơn EU) + Printify US (đơn US)

### Record A — market = EU
- **responsible_person**:
  - name: DAKOfits EU Compliance Ltd.
  - address: Rua Example 12, 1000-001 Lisboa, Portugal (EU)
  - email: eu-rp@dakofits.example
- Kỳ vọng clear: gpsr_status=PASS, ip_tm_status=PASS, label_ready=true.

### Record B — market = US
- **responsible_person**: (không bắt buộc cho US — GPSR không áp dụng)
- Kỳ vọng clear: gpsr_status=PASS (GPSR n/a), ip_tm_status=PASS, label_ready=true (nhãn US tối giản).

## Biến thể test (cho smoke-test bước 3 & 4)
- **Variant FAIL-RP**: Record A nhưng xóa `responsible_person.address` → gpsr_status=FAIL, label_ready=false, block EU.
- **Variant REJECT-TM**: đổi `breed_name` thành 1 brand name đã đăng ký TM → ip_tm_status=REJECT, need_review=true, trả Product Studio.
