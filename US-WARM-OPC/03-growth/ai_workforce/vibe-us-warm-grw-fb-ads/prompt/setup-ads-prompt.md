# Prompt — setup FB ads (GRW-002)
INPUT: live-product (02), creative FTC-clean, BE-ROAS per-SKU.
DO: precheck live-product; set audience/budget; scale_decision theo blended vs BE-ROAS; kill nếu <1.8. launch=true CHỈ khi live-product ∧ ftc_clean. Thiếu Meta token → launch=false, null data.
