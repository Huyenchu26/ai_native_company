# Prompt — price a blanket SKU (MER-001)

INPUT: design CLEAR (niche, personalization), sell_price mục tiêu, cost (quote hoặc assumption), allocated_cpa.
DO:
1. Tính gross_before_ads, contribution_%, BE-ROAS theo unit-economics (US no VAT).
2. below_floor = contribution < 0.15.
3. Nếu cost là giả định → cost_basis="assumption", need_review=true.
4. Emit pricing-decision.json đúng schema, evidence trỏ unit-economics (verbatim).
FAIL-CLOSED: thiếu cost thật → không chốt production; below_floor → không scale, đề xuất bundle/tăng giá.
