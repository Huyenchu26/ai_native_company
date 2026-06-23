# Compliance Playbook — DAKOfits (GPSR + IP/TM + GDPR + Meta Ad Policy)

> GATE issuer cho cả công ty. Conservative-by-default: nghi ngờ → FAIL/REJECT. Error budget legal = 0%.
> Bind: SOP-BCK-004 (clear-gpsr), SOP-BCK-005 (manage-gdpr).

---

## 1. GPSR clearance checklist (EU 2023/988, hiệu lực 13/12/2024)
SP bán cho consumer EU PHẢI có đủ 3 nhóm:

### 1a. Responsible Person (RP) đặt tại EU
- [ ] **Name** — pháp nhân/cá nhân chịu trách nhiệm.
- [ ] **Address** — địa chỉ thực tại EU (không PO box ngoài EU).
- [ ] **Email** — contact hợp lệ.
- Thiếu bất kỳ trường → `gpsr_status = FAIL`, **block publish EU** (không ngoại lệ tự động).

### 1b. Nhãn an toàn EU (label) — `label_ready=true` chỉ khi đủ
- [ ] Manufacturer info
- [ ] Product ID / model
- [ ] Material (composition) + care
- [ ] Warning / care instruction (EN)
- [ ] Traceability (batch/provider EU)

### 1c. IP/TM clearance (xem mục 2)

**Gate cứng:** `market=EU` → `gpsr_status` PHẢI = PASS để `label_ready=true`. Merch chỉ publish EU khi clearance log PASS. **No GPSR → No publish.**
**Chỉ US (không EU):** GPSR không bắt buộc; IP/TM vẫn bắt buộc.

---

## 2. IP/TM check (USPTO + EUIPO)
- **US**: USPTO TESS search theo tên breed/niche.
- **EU**: EUIPO trademark search.
- Mapping kết quả → `ip_tm_status`:
  - **PASS** — không trùng nhãn hiệu đã đăng ký.
  - **MODIFY** — trùng một phần / cần đổi tên/wording listing.
  - **REJECT** — trùng/nghi trademark → trả Product Studio re-clear (SOP-PRD-004). **Default REJECT khi nghi ngờ.**
- Breed/niche watchlist versioned; mọi search lưu evidence[].

---

## 3. GDPR (SOP-BCK-005)

### 3a. RoPA (Record of Processing Activities — Art.30)
Data inventory mọi hệ thống xử lý PII khách EU:
| Hệ thống | PII | Legal basis | Retention |
|---|---|---|---|
| ShopBase | email, ship address, order | contract | theo nghĩa vụ kế toán |
| Klaviyo | email, consent | consent (opt-in) | tới khi unsubscribe |
| Meta CAPI | hashed PII | legitimate interest / consent | theo Meta |
| Printify | ship address | contract | tới fulfill xong |
- Review ≤ quý; cập nhật khi đổi provider/flow.

### 3b. DSAR / erasure (≤ 1 tháng, 100% on-time)
1. Nhận request từ CX → **xác thực danh tính** (chống mạo danh; không xác thực được → từ chối + ghi lý do).
2. Access / export / erase qua ShopBase/Klaviyo erase API.
3. Ghi DSAR resolution log + timer SLA.
- Xung đột nghĩa vụ kế toán → giữ data tài chính tối thiểu (legal basis), erase phần marketing.

### 3c. Breach notify ≤ 72h (Art.33) — gate cứng
- Phát hiện incident → **log immutable** trong `archive/` → đánh giá rủi ro.
- Rủi ro cao → kích hoạt **72h clock NGAY** kể từ thời điểm "**become aware**" → Owner notify supervisory authority (+ khách nếu cần) ≤72h.
- Error budget 0%.

### 3d. Consent audit
- Email chỉ gửi tới opt-in. Thiếu consent → báo Growth (SOP-GRW-003) **dừng gửi** subscriber đó.

---

## 4. Meta Ad Policy pre-check (cho Growth, chống ban)
Pre-check creative/landing trước khi Growth chạy ad:
- [ ] Không claim sai / unrealistic outcome.
- [ ] Không before/after, không personal attributes ("you/your" nhắm thuộc tính cá nhân).
- [ ] Không prohibited content.
- [ ] Landing page khớp ad, có policy/contact.
- Output flag PASS/MODIFY/REJECT → `vibe-eu-opc-grw-orchestrator`. **No Meta Ad Policy → No ads.**

---

## 5. Gate cứng tổng hợp
| Gate | Điều kiện | Hậu quả nếu fail |
|---|---|---|
| No-GPSR-no-publish (EU) | market=EU → gpsr_status=PASS | Merch block publish |
| IP/TM clearance | ip_tm_status ≠ REJECT trước listing | trả Product Studio |
| Breach 72h | notify ≤72h từ become aware | legal violation |
| DSAR | resolve ≤1 tháng | legal violation |
| Meta Ad Policy | flag=PASS trước chạy ad | Growth block ad |

Mọi quyết định: `evidence[]` + `confidence_score` (min 0.7) + `need_review`. Audit trail immutable.
