# Smoke test — mer-catalog
1. skill.json valid vs skill-meta → ok.
2. sample-pricing-output.json --run-all → ok, evidence 3/3.
3. sample-pricing-violation.json (contribution 0.08, below_floor=false) → FAIL (gate enforce).
4. listing-package live_status=live nhưng images_on_disk=false → FAIL.
5. cost_basis=assumption ⇒ need_review=true (fail-closed).
