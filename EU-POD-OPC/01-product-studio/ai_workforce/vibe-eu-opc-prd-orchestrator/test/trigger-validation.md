# Trigger Validation — vibe-eu-opc-prd-orchestrator

Kiểm tra description (4 phần WHAT/TRIGGER/EXCLUSION/PUSH) route đúng. 5 SHOULD +
5 SHOULD NOT.

---

## SHOULD trigger (kích hoạt skill này)
| # | Câu / ngữ cảnh | Lý do |
|---|----------------|-------|
| S1 | "Chuẩn bị lô SP mới từ niche cho DAKOfits" | TRIGGER tự nhiên: 'chuẩn bị lô SP mới' |
| S2 | "Chạy pipeline niche → design cho batch tuần này" | TRIGGER thuật ngữ: 'pipeline niche','design pipeline' |
| S3 | "Cần SP mới để bán, làm từ ý tưởng tới design" | TRIGGER ngữ cảnh: 'cần SP mới để bán' + 'từ ý tưởng tới design' |
| S4 | "Điều phối Product Studio, route research với design" | WHAT: điều phối Product Studio |
| S5 | "Làm SP mới từ niche, nhớ clear IP trước khi listing" | WHAT: niche→design→IP clearance→handoff Merch |

## SHOULD NOT trigger (phải route nơi khác)
| # | Câu / ngữ cảnh | Route đúng tới |
|---|----------------|----------------|
| N1 | "Chấm điểm demand + audience sizing cho 20 niche" | `vibe-eu-opc-prd-niche-research` (việc cụ thể, không phải điều phối) |
| N2 | "Vẽ AOP tile 300 DPI + clear USPTO/EUIPO cho breed X" | `vibe-eu-opc-prd-design` (design + clearance cụ thể) |
| N3 | "Setup Printify + đặt giá + đăng ShopBase cho batch" | `vibe-eu-opc-mer-orchestrator` (đăng ShopBase/pricing) |
| N4 | "Viết video script + chạy FB Ads cho SP winner" | Growth (`vibe-eu-opc-grw-orchestrator`) |
| N5 | "Viết product page copy + chèn nhãn GPSR" | `vibe-eu-opc-mer-product-page` (Merch) |

---

## Ghi chú phân định
- Manager này chỉ **điều phối** Product Studio; việc chuyên môn (research, design,
  clearance) phải delegate xuống specialist.
- Mọi thứ sau cleared design (ShopBase, pricing, ads) là downstream — KHÔNG xử lý
  ở đây, và đặc biệt KHÔNG handoff thẳng Growth.
