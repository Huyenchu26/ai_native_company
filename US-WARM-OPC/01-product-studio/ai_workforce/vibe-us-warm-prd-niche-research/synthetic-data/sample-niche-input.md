# Sample Niche Input — PRD-001

> Synthetic input for testing `vibe-us-warm-prd-niche-research`. Owner-provided candidate + any evidence files. No live tool assumed unless a real signal file is attached.

## Candidate niche
- **niche:** pet memorial blanket for dog owners ("in loving memory of my dog")
- **axis:** recipient-special → pet-memorial (evergreen, emotional AOV)
- **relationship framing:** "for grieving fur parents", gift-to-self and gift-to-friend
- **product:** personalized fleece/sherpa blanket, own pet photo + name + dates

## Owner-provided signals (for this fixture)
- Concept uses the customer's OWN pet photo + name + message → no third-party IP in concept.
- Price target $59.95 (clears free-ship threshold; strong margin per unit-economics).
- Evergreen demand; minor lift around pet-loss awareness periods; not a hard seasonal deadline.
- Corroborating repo evidence to cite (verbatim): SOP-PRD-001 demand gate + seasonal rule, unit-economics $59.95 margin note, charter product-line (pet-memorial personalization).

## Live-tool status
- Google Trends / Meta Ad Library / marketplace best-seller / AdSpy: **not wired in repo**.
- For a production run these MUST supply measured demand + audience reach. In this fixture the demand/audience are treated as documented estimates corroborated by cited repo files.

## Expected handling
- Score via rubric (demand40/competition25/margin-fit20/ip-risk15).
- If all gates pass with verifiable evidence and confidence ≥ 0.7 → `validated` (see `sample-niche-output.json`).
- A deliberately gate-violating variant (`sample-niche-violation.json`: demand 50 but decision validated) MUST be rejected by the validator.
