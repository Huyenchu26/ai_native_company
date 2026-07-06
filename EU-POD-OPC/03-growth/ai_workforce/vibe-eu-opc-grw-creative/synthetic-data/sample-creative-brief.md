# Sample Creative Brief (synthetic) — DAKOfits

Brief mẫu để chạy smoke test / prompt. Dữ liệu giả lập, không phải đơn thật.

---

## Brief #1 — French Bulldog AOP Leggings

| Field | Value |
|-------|-------|
| **Niche / Breed** | French Bulldog (dog-mom, US, nữ 28–45) |
| **Product + link** | DAKOfits AOP Leggings — French Bulldog Watercolor / `dakofits.com/p/frenchie-watercolor-leggings` |
| **Angle** | Identity ("for French Bulldog lovers") |
| **Format** | video (9:16, 15–20s) |
| **Signal** | Winner cũ frequency cao (ad fatigue) → cần variant hook mới giữ angle |
| **Niche evidence** | Niche research: French Bulldog demand score cao, FB audience ~4.2M US; competitor đang chạy identity angle |
| **Social proof** | "320+ sold last drop", rating 4.8/5 |

### Gợi ý hook (để test ≥ 2 variant)
- Variant A: "POV: your leggings finally match your Frenchie 🐾" + close-up mẫu watercolor.
- Variant B: "These Frenchie leggings sold out 3× — here's why" + 360° xoay khoe all-over-print.

### Lưu ý policy
- Angle identity/gift — KHÔNG dùng claim sức khỏe / before-after cơ thể.
- Tên "French Bulldog" là breed phổ thông, IP risk thấp; nếu thêm tên nhãn/quote có TM → flag 05-compliance.

### Expected output
1 `creative-package` JSON: `format=video`, hook_0_3s (variant A/B), body_360 (360° + close-up vải + lifestyle tập + social proof "320+ sold"), cta ("Shop your Frenchie →" + link), `variant_count>=2`, `policy_self_check=true`, `evidence[]` đủ, `confidence_score>=0.7`, `need_review=false`.
