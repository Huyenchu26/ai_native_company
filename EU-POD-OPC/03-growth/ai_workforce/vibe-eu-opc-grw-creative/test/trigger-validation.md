# Trigger Validation — vibe-eu-opc-grw-creative

Xác nhận skill kích hoạt ĐÚNG lúc và KHÔNG cướp việc skill khác.

## SHOULD trigger (skill này nhận)
| # | Input người dùng | Lý do |
|---|------------------|-------|
| 1 | "Viết kịch bản video ad cho legging French Bulldog" | video script — owner SOP-GRW-005 |
| 2 | "Cần hook 0–3s mới, ad đang bị chai" | hook + ngữ cảnh ad fatigue → new creative |
| 3 | "Làm UGC brief cho dog-mom niche Corgi" | UGC brief — đúng phạm vi |
| 4 | "Thiết kế carousel 5 card cho SP leggings yoga" | carousel copy — đúng phạm vi |
| 5 | "Làm content quảng cáo FB cho niche mèo Maine Coon" | tạo nội dung quảng cáo FB — PUSH mặc định |

## SHOULD NOT trigger (chuyển skill khác)
| # | Input người dùng | Phải route tới | Bẫy |
|---|------------------|----------------|-----|
| 1 | "Set up campaign ABO và scale ngân sách creative này" | vibe-eu-opc-grw-fb-ads | Chạy/tối ưu ads ≠ tạo creative |
| 2 | "Tối ưu ROAS, CPA đang cao quá" | vibe-eu-opc-grw-fb-ads | Vận hành ads, không phải nội dung |
| 3 | "Thiết kế file AOP print-ready 300 DPI cho mẫu leggings" | vibe-opc-pod-product-design | Thiết kế sản phẩm AOP ≠ ad creative |
| 4 | "Viết email cart-abandon trong Klaviyo" | vibe-eu-opc-grw-marketing | Email ≠ ad creative |
| 5 | "Lên lịch post organic IG + seeding cộng đồng dog-mom" | vibe-eu-opc-grw-marketing | Organic social ≠ FB ad creative |

**Pass:** 5/5 SHOULD kích hoạt + 5/5 SHOULD NOT từ chối & route đúng. Khi mơ hồ giữa creative vs product-design vs fb-ads → hỏi rõ "tạo nội dung quảng cáo, thiết kế sản phẩm, hay chạy ads?".
