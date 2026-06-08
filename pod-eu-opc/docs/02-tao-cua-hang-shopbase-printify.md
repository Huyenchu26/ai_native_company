# 02. Tạo Cửa Hàng – Shopbase & Printify

> Hướng dẫn thực hành mở Store chuyên nghiệp và tạo design thu hút khách hàng

---

## 1. Shopbase – Tổng Quan

### Tại sao dùng Shopbase
Shopbase là platform cross-border thương mại điện tử **do người Việt Nam sáng lập** (CEO Phuong Anh Ha – Alice), có trụ sở tại San Francisco. Được xây dựng chuyên biệt cho Dropshipping, POD và White Label – khác biệt với các platform chung như Shopify.

**3 nhánh chính:**
- **Shopbase** – store builder đầy đủ, bạn tự quản lý fulfillment
- **PrintBase** – platform POD all-in-one, PrintBase lo fulfillment + CS + thanh toán
- **PlusBase** – tập trung dropshipping, fulfillment được quản lý

**Lý do người Việt Nam ưa chuộng:**
- Hỗ trợ tiếng Việt native, cộng đồng VN seller 7,100+ thành viên
- Phí giao dịch thấp hơn Shopify ($19/tháng so với $39/tháng của Shopify)
- Conversion tools tích hợp (upsell, exit-intent popups, countdown timers) miễn phí
- Hỗ trợ Payoneer, PingPong – critical cho người Việt chưa có Stripe
- Chuyên POD từ đầu, không phải afterthought

### Bảng Giá Shopbase (2024–2025)

| Plan | Monthly | Annual | Transaction Fee | Staff |
|------|---------|--------|-----------------|-------|
| Basic Base | $19/mo | $17/mo | 2.0% | 5 |
| Standard Base | $59/mo | $53/mo | 1.0% | 10 |
| Pro Base | $249/mo | $224/mo | 0.5% | 100 |

**Người mới nên dùng: Basic Base $19/tháng.** Có 14-day free trial, không cần thẻ tín dụng.

---

## 2. Thiết Lập Shopbase Store – Từng Bước

### Bước 1: Đăng ký & Cài đặt chung
1. Vào shopbase.com → "Start free trial"
2. Nhập email và tên store (không cần thẻ)
3. Admin → Settings → General: set currency = **USD**, timezone, store email chuyên nghiệp

### Bước 2: Custom Domain (Bắt buộc trước khi nhận thanh toán)
- **Option A**: Mua qua Shopbase (Admin → Online Store → Domains → Buy new domain)
- **Option B (khuyến nghị)**: Mua tại Namecheap (~$10–15/năm) → connect qua DNS records
- Naming tips: ngắn, dễ nhớ, không dùng hyphens, không dùng keyword domains

### Bước 3: Chọn & Tùy chỉnh Theme
- Admin → Online Store → Themes → 2 themes miễn phí: Inside và Roller (đều tối ưu conversion)
- Upload logo: PNG transparent background, 400x100px
- Set 2 màu brand + 1 font display + 1 font body
- Enable sticky header bar cho free shipping announcement
- Customize checkout page: logo + brand colors + "Terms agreement" checkbox

### Bước 4: Cài PrintHub App
- Admin → App Store → "PrintHub" → Install (free)
- App POD native của Shopbase, kết nối print providers, auto-fulfill orders

### Bước 5: Cài Đặt Thanh Toán
- Admin → Settings → Payments
- **PayPal**: connect tài khoản PayPal Business
- **Payoneer hoặc PingPong**: phổ biến nhất cho người Việt Nam
- **Stripe**: nếu có entity Mỹ (xem tài liệu 06 về cổng thanh toán)

### Bước 6: Shipping Rates
- Admin → Settings → Shipping → tạo zones (US, EU, AU...)
- Options: Flat rate ($4.99 US, $7.99 international) hoặc Free shipping (build cost vào giá)
- **Free shipping = conversion rate cao hơn** nhưng cần pricing đúng

### Bước 7: Tax Settings
- Admin → Settings → Taxes → Enable auto US tax calculation
- Người Việt Nam bán thị trường Mỹ thường không cần lo về US sales tax cho đến khi đạt $100K/năm ở một state

### Bước 8: Store Pages Bắt Buộc
- **About page**: câu chuyện thương hiệu 150–250 chữ (tăng trust, tăng conversion 12%)
- **Shipping policy**: "Ships within 3–5 business days, arrives in 3–7 additional business days"
- **Refund policy**: "Accept returns for defective/wrong items within 30 days with photos"
- **Privacy policy + Terms of service**: Admin → Settings → Legal (auto-generate)
- **FAQ page**: 5–7 câu hỏi phổ biến

---

## 3. Shopbase + Printify – Kết Hợp

### QUAN TRỌNG: Printify KHÔNG có native integration với Shopbase

**Lựa chọn thực tế:**

**Path A (Khuyến nghị): Dùng PrintHub thay Printify**
- PrintHub là app POD native miễn phí của Shopbase
- Tích hợp sâu, orders sync và auto-fulfill không cần code
- Đủ catalog cho hầu hết sellers

**Path B: Kết nối Printify qua API**
- Trong Printify: My Stores → Add New Store → chọn "API"
- Lấy API Token từ Account Settings → Connections
- Cần kỹ năng lập trình hoặc thuê freelancer
- Phù hợp nếu cần catalog hoặc print providers riêng của Printify

**Path C: Dùng Order Desk làm middleware**
- Tool no-code kết nối Shopbase ↔ Printify
- Chi phí: ~$20–35/tháng thêm

---

## 4. Printify – Tổng Quan

### Thông số

| Tiêu chí | Chi tiết |
|----------|----------|
| **Catalog** | 1,300+ sản phẩm |
| **Print providers** | 90+ providers, 140+ facilities (US, EU, UK, CA, AU) |
| **Free plan** | Kết nối 5 stores, đầy đủ catalog |
| **Premium** | $29/tháng, 10 stores, 20% discount tất cả base costs |
| **Khi nào nên Premium** | Khi savings hàng tháng > $29 (khoảng 100+ đơn/tháng) |

### Performance Score
Mỗi provider có điểm 0–10 dựa trên: quality + production speed + shipping. Luôn sort "Printify Choice" khi chọn provider. Chênh lệch 2+ điểm = khác biệt rõ rệt về review 5 sao vs return request.

### Top Providers Khuyến Nghị

| Sản phẩm | Provider | Lý do |
|----------|----------|-------|
| DTG t-shirts | Monster Digital, SwiftPOD | Print chất lượng cao, nhất quán |
| AOP hoodie/shirt | Subliminator, SPOD | Chuyên AOP |
| Mugs | Dynamic Gift, HugePOD | Ceramic drinkware chất lượng |
| Posters/Canvas | PGP, US-based providers | Màu sắc chính xác |

---

## 5. Tạo Design Thu Hút Khách Hàng

### Yêu Cầu Kỹ Thuật (Không Thể Bỏ Qua)

| Thông số | Yêu cầu |
|----------|---------|
| **Định dạng** | PNG với transparent background |
| **Resolution** | Tối thiểu **300 DPI** |
| **Color mode** | RGB hoặc sRGB |
| **Background** | Trong suốt (không fill white) |

### Kích Thước Theo Sản Phẩm

| Sản phẩm | Print area | Pixel dimensions |
|----------|-----------|-----------------|
| Adult t-shirt (full front) | 12 x 16 inches | 3600 x 4800 px |
| T-shirt (canvas size) | 15 x 18 inches | **4500 x 5400 px** |
| Hoodie (full front) | 12 x 14 inches | 3600 x 4200 px |
| Mug 11oz | 8.5 x 3.7 inches | 2550 x 1110 px |
| Poster 18x24 | 18 x 24 inches | 5400 x 7200 px |

**Luôn download template từ Printify Product Creator** cho từng sản phẩm cụ thể.

### Design Tools Theo Mục Đích

| Tool | Điểm mạnh | Giá | Dùng khi nào |
|------|-----------|-----|---------------|
| **Canva Pro** | Layout, text, brand, nhanh | $13/tháng | Typography, quote designs |
| **Kittl** | Vector, text effects, chuyên POD | Free/Paid | Fake brand, badges, logos |
| **Midjourney** | Ảnh nghệ thuật chất lượng cao | $10/tháng+ | Illustrations, artwork |
| **Adobe Illustrator** | Professional vector | $55/tháng | Nếu biết design chuyên nghiệp |
| **Photoshop** | Photo manipulation, vintage effects | $23/tháng | Distressed/vintage, AOP |
| **Remove.bg** | Xóa background | Free | Isolate subjects |

### Tips Canva Cho POD
- Tạo custom canvas 4500 x 5400 px (chọn "Custom size")
- Canva hiện 96 DPI nhưng khi download PNG, output đủ pixel (4500x5400 px = 300 DPI khi in 15x18 inch)
- Download → PNG → bật "Transparent background" nếu Canva Pro
- Font pairing: 1 display font + 1 sans-serif body, tối đa 2 fonts/design

### Tips Kittl Cho POD
- Export 300 DPI với color profiles đúng (CMYK support)
- Templates phân loại theo product type (hoodie, poster, mug)
- AI Design Assistant gợi ý layout từ brief ngắn
- Workflow: Template → customize text cho niche → AI text effects → export SVG/PNG

---

## 6. Product Mockup Best Practices

### Tại sao Mockup Quan Trọng
Stores với 1 ảnh sản phẩm có bounce rate cao hơn 60% so với stores có 5+ ảnh. Mockup giúp khách visualize trước khi mua.

### Bộ Ảnh Chuẩn Mỗi Listing (5–7 ảnh)
1. Front lifestyle (on-model, người mặc áo)
2. Front flat lay (design rõ nét)
3. Back flat lay hoặc lifestyle
4. Design close-up (thấy chất lượng in và chi tiết)
5. Size reference (chiều cao và size người mặc)
6. Color variant (nếu có nhiều màu)
7. Lifestyle in context (outdoor, cafe, v.v.)

### Mockup Tools

| Tool | Điểm mạnh | Giá |
|------|-----------|-----|
| **Printify built-in** | Miễn phí, flat lay + lifestyle | Free |
| **Placeit.net** | Thư viện khổng lồ, video mockups | $8/tháng |
| **Mockey** | Free, 25+ categories | Free |
| **Canva Bulk Create** | Tạo 50 mockups cùng lúc từ spreadsheet | $13/tháng |

---

## 7. Listing Optimization – SEO

### Cấu Trúc Title (Shopbase & Marketplaces)

**Công thức:** `[Primary keyword] + [Secondary descriptor] + [Product type] + [Use case/Audience]`

❌ Sai: "Funny Cat Shirt Design"
✅ Đúng: "Cat Mom Gift Shirt — Funny Cat Lover T-Shirt for Women, Unisex Cotton Tee"

**Rules:**
- Lead với noun + primary keyword (thứ người ta thực sự search)
- Tối đa 60–70 ký tự cho Shopbase (Google SEO); Etsy: dùng hết 140 ký tự
- Bao gồm: product type, attribute (funny, vintage), audience (mom, dog lover), occasion (birthday gift)

### Tags (Etsy – 13 tags)
- Dùng exact phrases người mua gõ, không phải single keywords
- Audience tags: "gift for mom"
- Occasion tags: "mothers day gift"
- Style tags: "vintage graphic tee"
- Product tags: "unisex crewneck shirt"

### Cấu Trúc Description
1. **Hook**: 1–2 câu, tại sao design này đặc biệt, cho ai
2. **Details**: material, weight, fit, print method, care instructions
3. **Shipping note**: "Ships from US fulfillment partner within X-X business days"
4. **Gift suitability**: "Makes a perfect gift for..."
5. **Size guide**: measurements thực từ provider

---

## 8. Pricing Strategy

### Công Thức Cốt Lõi

```
Total Cost = Base Cost + Shipping + Platform Fees + Transaction Fees
Retail Price = Total Cost ÷ (1 - Desired Margin)
```

**Ví dụ t-shirt trên Shopbase:**
- Base cost: $10.50
- Shipping: $4.50 (include vào giá)
- Platform fee: $0.19 (tính chia đơn)
- Transaction fee 2%: $0.60
- **Total cost**: $15.79
- Target margin 40%: $15.79 ÷ 0.60 = **$26.32 → $26.99**

### Margin Targets Theo Sản Phẩm

| Category | Recommended Margin |
|----------|-------------------|
| T-shirts | 35–45% |
| Hoodies | 40–50% |
| Mugs | 45–55% |
| Posters/prints | 50–65% |
| Phone cases | 40–50% |
| Canvas prints | 55–70% |

**Nguyên tắc:**
- KHÔNG giảm giá để cạnh tranh (liên tưởng chất lượng thấp)
- Penetration pricing (5–10% dưới market) chỉ khi launch để build reviews
- Sau 20–30 reviews tốt: tăng giá 10–20%
- Luôn dùng .99 hoặc .95 (tâm lý giá)

---

## 9. Launch Sequence Chuẩn

1. Register Shopbase free trial → cài đặt General settings
2. Mua custom domain → kết nối DNS
3. Chọn theme → logo, màu, font, checkout branding
4. Cài PrintHub (hoặc setup Printify API)
5. Tạo 10–20 sản phẩm với designs 300 DPI PNG → publish
6. Setup tất cả legal pages (Shopbase Legal generator)
7. Cài đặt payment gateways (PayPal + Payoneer tối thiểu)
8. Tạo shipping zones với rates thực tế
9. Tạo mockup sets (5–7 ảnh mỗi sản phẩm)
10. Viết listings tối ưu (title formula + description structure)
11. Định giá theo công thức Total Cost ÷ (1 - target margin)
12. **Order 2–3 samples** để verify chất lượng in trước khi scale marketing
13. Launch → bắt đầu traffic (Pinterest organic, TikTok, Facebook groups)
