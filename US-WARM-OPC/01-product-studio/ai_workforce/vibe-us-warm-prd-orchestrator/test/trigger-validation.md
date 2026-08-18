# Trigger Validation — vibe-us-warm-prd-orchestrator

Xác nhận skill kích hoạt ĐÚNG ngữ cảnh điều phối Product Studio và KHÔNG lấn việc chuyên môn.

## Phải TRIGGER (route, KHÔNG execute)
| Câu người dùng | Kỳ vọng |
|----------------|---------|
| "làm lô chăn cá nhân hoá mới từ niche tới design" | full-pipeline: route PRD-001→002→003→handoff Merch |
| "chuẩn bị batch SP mới cho Christmas" | route niche-research trước, seasonal timing |
| "pipeline niche pet-memorial" | route PRD-001 rồi PRD-002/003 |

## Phải DELEGATE (KHÔNG tự làm)
| Câu | Route tới |
|-----|-----------|
| "chấm điểm demand cho niche này" | `vibe-us-warm-prd-niche-research` (PRD-001) |
| "thiết kế layout + variable-data cho chăn" | `vibe-us-warm-prd-design` (PRD-002) |
| "tra USPTO cho slogan này" | `vibe-us-warm-prd-design` pre-check → `vibe-us-warm-bck-compliance` |
| "đăng listing + set giá" | `vibe-us-warm-mer-orchestrator` (downstream) |
| "viết ad + chạy FB Ads" | Growth — CHỈ sau khi Merch xong. KHÔNG route thẳng. |

## Enum guard (chống bug EU PASS≠CLEAR)
| Kiểm tra | Đúng |
|----------|------|
| design_status / ip_status / gate_checks.ip_clearance | `CLEAR / MODIFY / REJECT / PENDING` |
| cleared_for_handoff[].clearance_status | `CLEAR` (const) |
| Có xuất hiện `PASS` ở đâu không? | KHÔNG — `PASS` = FAIL enum guard |

## Gate guard
- design_status=PENDING/MODIFY/REJECT vào cleared_for_handoff → schema FAIL (xem smoke-test T3).
- Thiếu `clearance_id` khi clearance_status=CLEAR → schema FAIL.
- confidence < 0.7 mà need_review=false → schema FAIL.
