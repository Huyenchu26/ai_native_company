# script/ — Shared harness (không copy validator per-skill)

Skill này KHÔNG có validator riêng. Dùng CHUNG:
`../../../../_shared/script/validator.py`

Lý do: bài học EU pipeline test — mỗi skill 1 bản validator copy gây drift + bug hệ thống
(evidence-contract lệch, gate if/then bị nuốt). 1 validator dùng chung = 1 nguồn sự thật, fix 1 chỗ.

Gọi: `python3 ../../../../_shared/script/validator.py --run-all --artifact <out.json> --schema schema/<x>.schema.json`
