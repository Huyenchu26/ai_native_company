# Prompt — make mockup set (MER-002)
INPUT: design-spec (layout + variable slots), pricing, personalization fields.
DO: liệt kê images cần; nếu có render tool → render + tải local + set rendered; nếu không → not-generated + null + need_review=true. Emit mockup-set.json đúng schema.
FAIL-CLOSED: KHÔNG khai local_file nếu file không có trên đĩa.
