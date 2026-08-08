# Reference Regeneration Prompt — {layout-slug}

**Pin file:** `{pin-file}`  
**Source URL:** {pinterest-pin-url}  
**Inferred layout:** `{inferred_layout}`  
**Created:** {YYYY-MM-DD}  
**Phase:** 6a — reference-creative-prompt

> This prompt regenerates the **reference image layout**. Phase 8 merges it with `BRAND_DNA.json` (colors) and calendar `elements[]` (on-image copy). Do not use pin hex at render time.

---

## Color roles (resolved in Phase 8 from Brand DNA)

| Role | Semantic use in this layout |
|------|----------------------------|
| `{{BACKGROUND}}` | {e.g. full-bleed canvas} |
| `{{TEXT_PRIMARY}}` | {e.g. headline lines} |
| `{{TEXT_SECONDARY}}` | {e.g. subheadline} |
| `{{TEXT_MUTED}}` | {e.g. footer URL, slide counter} |
| `{{ACCENT}}` | {e.g. vertical rule, highlight word} |
| `{{ACCENT_SECONDARY}}` | {optional second accent} |

---

## Zone map (from reference image)

```
{ASCII diagram — match actual pin proportions}
```

---

## Hero subject (must preserve)

{If reference has person / photo / illustration / key object — describe type, pose, crop, clothing, props, and exact placement. If truly typography-only, state "typography_only" explicitly.}

---

## must_preserve

Layout traits that **must not change** when swapping brand copy:

1. {e.g. left-aligned headline block with 80px margin}
2. {e.g. split panel — purple copy block left 45%, photo subject right 55%}
3. {e.g. seated person waist-up, cross-legged, reading book — right of center}
4. {e.g. footer URL strip bottom-right}
5. {add pin-specific traits — include hero when present}

---

## variable_slots (Phase 8 replaces)

| Slot | Reference had | Phase 8 source |
|------|---------------|----------------|
| Headline | `{transcribed from pin}` | `creative.elements` headline |
| Subheadline | `{transcribed}` | `creative.elements` subheadline |
| Footer | `{transcribed}` | `brand.brand.website` or calendar row |
| Brand strip | `{if any}` | `brand.brand.name` |

---

## Regeneration prompt (layout only — use color roles)

{Full prose paragraph(s) describing how to recreate this exact layout. Include: canvas size, margin/padding, each zone position, typography alignment and relative scale, decorative elements, hero type and placement, effects. Use `{{BACKGROUND}}`, `{{TEXT_PRIMARY}}`, `{{ACCENT}}`, etc. for every color mention. Transcribe reference on-image copy in a "Reference copy (replace in Phase 8)" subsection — do not treat it as final.}

**Reference copy (replace in Phase 8):**
- Headline: `{exact text from pin}`
- Subheadline: `{exact text from pin}`
- Footer: `{exact text from pin}`

**Do not:** add extra text, change zone positions, swap layout archetype, or use colors outside the role placeholders above.
