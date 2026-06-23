# Trigger Validation — vibe-eu-opc-prd-niche-research

Kiểm tra skill được kích hoạt ĐÚNG lúc và KHÔNG bị kích hoạt nhầm (route sang skill khác).

## SHOULD TRIGGER (5)
| # | Câu / ngữ cảnh | Lý do |
|---|----------------|-------|
| 1 | "Tìm niche mới để launch đợt tới cho DAKOfits" | Tự nhiên: tìm niche mới + ngữ cảnh cần SP mới |
| 2 | "Research thị trường xem niche nào đang hot" | Tự nhiên: research thị trường / niche nào hot |
| 3 | "Chấm demand scoring + audience sizing cho list niche này" | Thuật ngữ EN: demand scoring, audience sizing |
| 4 | "Spy competitor trên AdSpy và check Google Trends cho niche pickleball" | Thuật ngữ: AdSpy, Google Trends |
| 5 | "Sắp tới mùa nào nên đánh? Lập seasonal calendar cho mấy niche pet" | Thuật ngữ: seasonal + ngữ cảnh cơ hội mùa vụ |

## SHOULD NOT TRIGGER (5 — bẫy)
| # | Câu / ngữ cảnh | Route đúng | Vì sao KHÔNG phải skill này |
|---|----------------|-----------|------------------------------|
| 1 | "Thiết kế file AOP print-ready 300 DPI cho niche German Shepherd đã clear" | **vibe-eu-opc-prd-design** | Đây là DESIGN, không phải research niche |
| 2 | "Setup product này trên Printify, đặt giá variant XS–3XL và sync ShopBase" | **vibe-eu-opc-mer-catalog** | Catalog/pricing/sync, không phải niche research |
| 3 | "Chạy FB Ads cho batch SP mới, tối ưu ROAS và scale winner" | **vibe-eu-opc-grw-fb-ads** | Chạy/tối ưu ads thuộc Growth |
| 4 | "Viết hook 0–3s và video script UGC cho ad leggings" | **vibe-eu-opc-grw-creative** | Tạo ad creative thuộc Growth |
| 5 | "Cấp GPSR clearance và check IP/TM chính thức cho breed trước khi publish" | **vibe-opc-pod-backoffice-compliance** | Clearance chính thức ở Backoffice; ở đây chỉ pre-flag |

## Pass criteria
5/5 SHOULD kích hoạt skill; 5/5 SHOULD NOT route sang đúng skill khác (đặc biệt không nhầm design/catalog/ads/clearance).
