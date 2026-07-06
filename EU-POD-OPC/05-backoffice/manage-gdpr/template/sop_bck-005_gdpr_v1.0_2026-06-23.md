# SOP-BCK-005 — GDPR Data Inventory, Requests & Breach

**Dept:** 05-backoffice (bck) · **Layer:** L3 Support · **Version:** v1.0 · **Ngày:** 2026-06-23
**Responsible AI:** `vibe-opc-pod-backoffice-compliance` `[AI WORKFORCE]`

---

## 0. IPO
| | |
|---|---|
| **Input** | DSAR/erasure request (CX), data flow từ ShopBase/Klaviyo/Meta/Printify, incident alert, consent records |
| **Process** | Duy trì data inventory → xử lý data subject request → log & ứng phó breach ≤72h |
| **Output** | `data inventory` (RoPA), DSAR resolution log, `breach log` + notification draft, consent audit |

## 1. Tổng quan
DAKOfits xử lý PII của khách EU (email, địa chỉ ship, order). GDPR yêu cầu: (1) **Record of Processing Activities (RoPA)** — biết dữ liệu nào ở đâu (ShopBase, Klaviyo email, Meta CAPI, Printify fulfillment); (2) đáp ứng **data subject requests** (access/erasure/portability) đúng hạn; (3) **breach notification ≤72h** tới supervisory authority. Marketing email chỉ opt-in (đồng bộ SOP-GRW-003). compliance AI là responsible.

## 2. RACI + AI Roles
| Hoạt động | R | A | C | I |
|---|---|---|---|---|
| Data inventory (RoPA) | compliance AI | Owner | finance AI | — |
| Xử lý DSAR/erasure | compliance AI | Owner | CX (fulfillment) | Owner |
| Breach log + 72h notify | compliance AI | Owner | — | Owner |
| Consent audit | compliance AI | Owner | Growth (marketing) | — |

`[AI WORKFORCE]` compliance AI: maintain RoPA, draft DSAR response, log breach + soạn notification, audit consent. Owner: quyết định notify authority/khách.

## 3. Quy trình (ICOM)
1. **Maintain inventory** (I: data flow; C: GDPR Art.30; M: RoPA template): cập nhật hệ thống/PII/legal basis/retention.
2. **Tiếp nhận request** (I: DSAR từ CX; C: 1-tháng deadline): xác thực danh tính chủ thể.
3. **Thực thi request** (M: ShopBase/Klaviyo erase API): access/export/erase + ghi resolution log.
4. **Phát hiện & log breach** (I: incident alert; C: GDPR Art.33): ghi breach log + đánh giá rủi ro.
5. **Notify ≤72h** (O: notification draft): nếu rủi ro cao → Owner notify authority/khách trong 72h.

## 4. Phân nhánh
- DSAR không xác thực được danh tính → từ chối + ghi lý do (chống mạo danh).
- Breach rủi ro cao → kích hoạt 72h clock ngay, Owner notify.
- Erasure xung đột nghĩa vụ kế toán → giữ dữ liệu tài chính tối thiểu (legal basis), erase phần marketing.
- Consent thiếu cho email → Growth dừng gửi tới subscriber đó (đồng bộ SOP-GRW-003).

## 5. Checklist — Quality Gate
| SLI | SLO | Đo |
|---|---|---|
| Breach response time | ≤ 72h notify | breach log timestamp |
| DSAR resolution on-time | ≤ 1 tháng, 100% | DSAR log |
| RoPA freshness | cập nhật ≤ quý | inventory date |
| Consent coverage email | 100% opt-in | consent audit |

**Error budget (compliance):** 0% cho 72h breach notify & DSAR deadline (legal). **Prevention:** incident alert tự động, DSAR ticket có SLA timer, RoPA review hằng quý, breach log immutable trong `archive/`.

## 6. Tài nguyên + Links
- [_knowledge: GDPR + breach 72h](../../_knowledge/README.md) · [SOP-FUL CX](../../../04-fulfillment-cx/support-customer/) · [SOP-GRW-003 email opt-in](../../../03-growth/send-email/)
- Rule: [GDPR breach 72h](../../_rules/README.md)

## 7. Lịch sử
| Version | Ngày | Thay đổi |
|---|---|---|
| v1.0 | 2026-06-23 | Khởi tạo |
