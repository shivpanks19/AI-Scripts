# effort-outcome-gap-editorial

**Creative ID:** `effort-outcome-gap-editorial`
**DNA merge:** reference-prompt + BRAND_DNA.json + effort-outcome-gap-editorial.CREATIVE_DNA.json
**Reference prompt:** ../../references/pinterest/2026-08-08/pin-03-editorial-quote-hero-reference-prompt.md
**Reference fidelity:** high — match reference image composition

## ON-IMAGE COPY — MANDATORY (exact)

| Zone | Text | Brand hex |
|------|------|-----------|
| Headline line 1 | Reports don't close | #FFFFFF |
| Headline line 2 | the gap. | #FFB800 |
| Subheadline | Outcomes move when someone owns your vision. | #A1A1AA |
| Footer URL | hexanovate.com | #A1A1AA |

## Hero subject (must preserve)

- **Type:** photo_subject
- **Description:** Young woman seated cross-legged, white t-shirt, ripped blue jeans, smiling while reading open book. Cutout on right half overlapping split panel. Desaturated architectural photo bleed behind.
- **Placement:** right-half

## must_preserve

- split layout — copy left ~45%, photo hero right ~55%
- curved boundary between panels
- seated woman cross-legged reading book on right
- architectural photo bleed behind subject
- CTA pill in left panel
- bottom footer strip three columns

## Generation prompt

Recreate the attached reference image layout closely. Same composition and hero subject placement. Apply brand colors and replace text only.

COLORS (from BRAND_DNA.json):
- Background / panels: #0A0A0A and #FF5500 accents
- Accent highlight: #FFB800
- Text on dark: #FFFFFF
- Muted: #A1A1AA
All colors from brand palette — ignore reference pin hex.

MUST include seated woman reading book on right — same pose and placement as reference pin.

**Exact on-image text:**
- `Reports don't close` (#FFFFFF)
- `the gap.` (#FFB800)
- `Outcomes move when someone owns your vision.` (#A1A1AA)
- `hexanovate.com` (#A1A1AA)

Inter / Plus Jakarta Sans. 1:1 1080×1080. No logo in generation.

## Do not

- Remove person, book, or split-panel hero when reference has them
- Add carousel indicators, fake stats, dashboard UI
- Use hex not in Brand DNA

## Post / caption

See `effort-outcome-gap-editorial-post.md`
