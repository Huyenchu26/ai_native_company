# SOP-GRW-001 — Organic Social & Community `[AI WORKFORCE]`

**Phòng:** 03-growth (grw) · **Phiên bản:** v1.0 · **Ngày:** 2026-06-23
**Owner:** 03-growth · **Responsible AI Worker:** `vibe-opc-pod-growth-marketing`
**Folder:** `post-organic/`

> GATE: Tôn trọng rule từng community (no spam), Meta/platform policy, GDPR (không scrape data cá nhân).

---

## 0. IPO

| Thành phần | Chi tiết |
|-----------|----------|
| **Input** | Live product (02); creative/UGC (SOP-GRW-005); niche + community list (01); seasonal calendar |
| **Process** | Lên lịch post IG/TikTok/FB → seed UGC vào dog-mom & niche groups → engage community → đo organic signal |
| **Control** | Platform/community rules, brand voice, no-spam, GDPR |
| **Output** | Posts/community đã lên lịch + organic traffic/social proof; signal (→ SOP-GRW-004) |
| **Mechanism** | IG/TikTok/FB, scheduler, vibe-opc-pod-growth-marketing |

---

## 1. Tổng quan

Organic là kênh **bổ trợ FB Ads**: tạo social proof (UGC, review), nuôi community niche (dog-mom, hobby groups), và hạ blended CAC. Không thay thế ads (ads vẫn 100% traffic chính) mà **làm ads rẻ hơn & creative đáng tin hơn**. Đa-niche → mỗi niche có community riêng để seed.

---

## 2. RACI + AI Roles

| Hoạt động | R | A | C | I |
|----------|---|---|---|---|
| Content calendar | `marketing` (AI) | OPC | `fb-creative` | — |
| UGC seeding | `marketing` (AI) | OPC | `fb-creative` (brief) | — |
| Community engage | `marketing` (AI) | OPC | 04-CX (FAQ) | — |
| Policy/community-rule check | `marketing` (AI) | OPC | 05-compliance | — |

**AI Role:** `vibe-opc-pod-growth-marketing` lên lịch + đăng + engage, gom UGC làm social proof cho ads/page; escalate khi bị community flag.

---

## 3. Quy trình (ICOM, 4 bước)

### Bước 1 — Content calendar `[Input]`
- Map post theo niche + seasonal; mix: product show-off 360°, UGC repost, behind-the-scenes, community value (không bán cứng).

### Bước 2 — Post IG/TikTok/FB `[Process]`
- Lên lịch đều; format theo platform (Reels/TikTok short, IG carousel, FB community post).
- Tái dùng winning hook từ creative library.

### Bước 3 — UGC seeding vào niche groups `[Process]`
- Seed UGC + review thật vào dog-mom & niche groups, **theo đúng rule group** (xin phép admin nếu cần, không spam link).
- Thu thập UGC mới (xin consent dùng lại).

### Bước 4 — Engage & đo `[Output]`
- Reply comment/DM (phối 04-CX cho câu hỏi support).
- Đo follower growth, engagement, referral traffic, UGC thu được → feed SOP-GRW-004.

---

## 4. Phân nhánh

| Điều kiện | Hành động |
|----------|-----------|
| Vi phạm community rule | gỡ/sửa, xin lỗi admin, không spam tiếp |
| Comment support thật | route 04-CX |
| UGC chất lượng cao | đề xuất `fb-creative` đưa vào ad/page (xin consent) |
| Negative PR/complaint | escalate OPC + 04-CX |
| Tên niche rủi ro IP | flag 05-compliance |

---

## 5. Checklist + Quality Gate (SLI/SLO + Prevention)

- [ ] Tuân community rule + platform policy
- [ ] Consent khi dùng UGC người dùng
- [ ] Không spam link
- [ ] Brand voice nhất quán

| SLI | SLO | Error budget |
|-----|-----|--------------|
| Post cadence | đúng lịch ≥ 90% | ≤ 10% trễ |
| Community-rule compliance | 100% (0 ban) | 0 tolerance |
| Engagement rate | khởi điểm gợi ý **≥ 2%** (baseline + chốt sau 30 ngày) | — |
| UGC thu được/tháng | gợi ý **≥ 8 UGC/tháng** (baseline + chốt sau 30 ngày) | — |
| Referral traffic → site/tháng | baseline 30 ngày đầu, chốt số sau | — |

> **Cơ chế baseline:** các SLI chưa có số chuẩn → **baseline = 30 ngày đầu vận hành**, review & chốt ngưỡng chính thức sau đó (cập nhật vào OKR/KPI). Giá trị "gợi ý" ở trên là placeholder khởi điểm, KHÔNG phải số đã chốt.

**Prevention:** đọc rule group trước seed; consent UGC; theo dõi flag để dừng kịp.

---

## 6. Tài nguyên + Links
- Folder: `post-organic/`
- Creative: [SOP-GRW-005](../../create-creative/template/sop_grw-005_fb-creative_v1.0_2026-06-23.md)
- Report: [SOP-GRW-004](../../report-growth/template/sop_grw-004_growth-report_v1.0_2026-06-23.md)
- Rules: [`_rules/README.md`](../../_rules/README.md)

---

## 7. Lịch sử
| Version | Ngày | Thay đổi | Người |
|---------|------|----------|-------|
| v1.0 | 2026-06-23 | Khởi tạo SOP organic social & community | Company Architect |
| v1.1 | 2026-06-23 | Thêm cơ chế baseline 30 ngày cho SLI; giá trị khởi điểm engagement ≥ 2%, UGC ≥ 8/tháng | 03-growth |
