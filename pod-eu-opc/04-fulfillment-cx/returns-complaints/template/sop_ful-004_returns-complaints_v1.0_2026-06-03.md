# SOP-FUL-004 — Returns / refund / complaint

**Department:** Fulfillment & CX (ful) · **AI Worker:** CX AI
**Loại:** OPERATIONAL · **v1.0** · **2026-06-03** · **ACTIVE**

> Mục tiêu: giữ rating ≥ 4.8. Lỗi sản xuất → Printify thường bồi thường; xử lý nhanh cho khách để bảo vệ rating.

## 1. Tổng quan
| Mục | Nội dung |
|---|---|
| **Mục đích** | Xử lý đổi/trả, hoàn tiền, khiếu nại đúng policy, bảo vệ rating & sự hài lòng. |
| **Phạm vi** | Return/refund/complaint chính thức + Etsy case/dispute. |
| **Trigger** | Yêu cầu đổi/trả, khiếu nại, hoặc Etsy case. |

### IPO
| | |
|---|---|
| **Input** | Yêu cầu khách (qua FUL-003), thông tin đơn, ảnh lỗi, policy |
| **Control** | Return policy, quyền người tiêu dùng EU, chính sách Printify lỗi sản xuất, SLA |
| **Output** | Resolution (reprint/refund/từ chối có lý do) + log + RCA nếu lỗi lặp |
| **Mechanism** | CX AI + Claude API, Printify claim, Etsy case |

## 2. Return policy (Knowledge — Founder chốt, xác nhận pháp lý)
| Tình huống | Xử lý |
|---|---|
| **Lỗi/sai/hư hỏng** (defect, wrong item, damaged) | Claim Printify + reprint hoặc refund khách (ưu tiên giữ khách) |
| **Đổi ý (change of mind)** | EU có quyền hủy 14 ngày cho mua online, **NHƯNG hàng cá nhân hóa/made-to-order thường được MIỄN TRỪ** (cần ghi rõ trong policy + xác nhận pháp lý) |
| **Sai size do khách chọn** | Theo policy size guide; thiện chí tùy trường hợp |
> ⚠️ Quyền người tiêu dùng EU phức tạp — chính sách phải được tư vấn pháp lý xác nhận; ghi rõ trong listing.

## 3. RACI
| Hoạt động | Founder | CX AI |
|---|---|---|
| Xử lý defect/refund trong hạn mức | I | **R** |
| Refund lớn / Etsy dispute / khiếu nại nặng | **A** | R (escalate) |

## 4. Đầu vào
- [ ] Yêu cầu + bằng chứng (ảnh) · [ ] Policy đã duyệt · [ ] Hạn mức refund tự xử

## 5. Quy trình
| # | Bước | Hành động | Tag AI | Prevention |
|---|---|---|---|---|
| 5.1 | Tiếp nhận | Nhận yêu cầu (từ FUL-003), thu thập bằng chứng | [AI WORKFORCE] | Yêu cầu ảnh với defect |
| 5.2 | Phân loại | Defect/wrong/damaged vs change-of-mind | [AI AUGMENT] | Theo bảng §2 |
| 5.3 | Defect path | Claim Printify + reprint/refund khách | [AI AUGMENT] | Claim đúng quy trình Printify |
| 5.4 | Change-of-mind | Áp policy (miễn trừ made-to-order) | [AI AUGMENT] | Trả lời lịch sự + dẫn policy |
| 5.5 | Etsy case | Nếu thành dispute → xử lý đúng quy trình Etsy | [AI ASSIST] | Escalate Founder |
| 5.6 | Log + RCA | Ghi resolution; lỗi lặp ≥3 → Incident Report | [AI WORKFORCE] | Pattern → RCA về gốc |

## 6. Quality Gate
| # | Tiêu chí | SLI | SLO | Pass |
|---|---|---|---|---|
| 1 | Phản hồi | thời gian phản hồi | ≤ SLA | ☐ |
| 2 | Defect claim | claim Printify đúng | 100% | ☐ |
| 3 | Backlog | quá hạn | 0 | ☐ |
| 4 | Rating | shop rating | ≥ 4.8 | ☐ |

## 7. Output & Downstream
- **Lưu:** ./output/resolution-log_[YYYY-MM].md → archive/ · **Downstream:** BCK-001/003 (hạch toán refund), _quality (RCA)

## 8. Phụ lục
Doc: ../return-shipping-policy.md · Incident: ../../_quality/ · Thiết kế §3.4
