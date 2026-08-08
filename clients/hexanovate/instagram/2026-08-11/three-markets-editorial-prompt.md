# three-markets-editorial

**Creative ID:** `three-markets-editorial`
**DNA merge:** reference-prompt + BRAND_DNA.json + three-markets-editorial.CREATIVE_DNA.json
**Reference prompt:** ../../references/pinterest/2026-08-08/pin-03-editorial-quote-hero-reference-prompt.md
**Reference fidelity:** high — match reference image composition

## ON-IMAGE COPY — MANDATORY (exact)

| Zone | Text | Brand hex |
|------|------|-----------|
| Headline line 1 | One vision. | #FFFFFF |
| Headline line 2 | Three markets. | #FFB800 |
| Subheadline | B2B · FMCG · Education — built to dominate. | #A1A1AA |
| Footer URL | hexanovate.com | #A1A1AA |

## Hero subject (must preserve)

- **Type:** photo_subject
- **Description:** Same reference hero: young woman cross-legged reading book, right half cutout, architectural bleed behind.
- **Placement:** right-half

## must_preserve

- split layout — copy left, photo hero right
- seated woman with book on right side
- curved panel boundary
- footer strip bottom
- CTA pill left panel

## Generation prompt

Recreate the attached reference image layout closely. Same composition and hero subject placement. Apply brand colors and replace text only.

COLORS (from BRAND_DNA.json):
- Background / panels: #0A0A0A and #FF5500 accents
- Accent highlight: #FFB800
- Text on dark: #FFFFFF
- Muted: #A1A1AA
All colors from brand palette — ignore reference pin hex.

MUST preserve photo hero (woman reading book) on right — match reference composition.

**Exact on-image text:**
- `One vision.` (#FFFFFF)
- `Three markets.` (#FFB800)
- `B2B · FMCG · Education — built to dominate.` (#A1A1AA)
- `hexanovate.com` (#A1A1AA)

Inter / Plus Jakarta Sans. 1:1 1080×1080. No logo in generation.

## Do not

- Remove person, book, or split-panel hero when reference has them
- Add carousel indicators, fake stats, dashboard UI
- Use hex not in Brand DNA

## Post / caption

See `three-markets-editorial-post.md`
