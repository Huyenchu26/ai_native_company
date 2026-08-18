# Trigger Validation — vibe-us-warm-prd-niche-research

Checks that the `description` trigger routes correctly: fires on niche research/scoring, and does NOT fire on downstream/adjacent work.

## SHOULD trigger (WHAT / TRIGGER)
| # | User request | Why |
|---|--------------|-----|
| T1 | "Find a good gift niche for our blankets this Christmas." | occasion niche research |
| T2 | "Should we launch a pet-memorial blanket?" | recipient niche validation |
| T3 | "Score the 'to my daughter' relationship niche." | relationship scoring |
| T4 | "Build a Q4 gifting niche watchlist." | watchlist build |
| T5 | "Refresh the deployment/military niche — is it still worth it?" | niche refresh |
| T6 | prd-orchestrator dispatches PRD-001 before design | SOP coverage |

## SHOULD NOT trigger (EXCLUSION → route elsewhere)
| # | User request | Correct owner |
|---|--------------|---------------|
| N1 | "Lay out the photo + name on the blanket / fix the artwork DPI." | vibe-us-warm-prd-design (PRD-002) |
| N2 | "Is the phrase 'Best Dad Ever' trademarked? Give official clearance." | vibe-us-warm-bck-compliance (PRD-003) — this skill only PRE-FLAGS |
| N3 | "Write the Facebook ad and scale the campaign." | 03-growth |
| N4 | "Set the final retail price and bundle offer." | merchandising |
| N5 | "Check the material GSM / supplier spec." | vibe-us-warm-prd-design + merchandising |

## Boundary case (pre-flag vs clearance)
- "Can we do a Marvel-character blanket?" → **this skill FIRES** to set `ip_risk_flag: HIGH` and route to PRD-003. It does NOT itself grant clearance. Emitting `ip_risk_flag: CLEAR` as a legal sign-off is a rule violation (`_rules` #3 "No IP guess").

## Fail-closed trigger behavior
- If the request needs measured demand but no live tool is available, the skill still fires but MUST return `decision: watchlist`, `need_review: true`, `confidence < 0.7` — never `validated`.

## Pass criteria
All T# route here; all N# route to the named owner; boundary + fail-closed behave as described.
