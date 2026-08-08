# DNA → Image Prompt Merge

Use when building `{slug}-prompt.md` (Phase 8) or calling the image generator (Phase 9).

## Three-layer merge (mandatory when reference prompt exists)

Phase 8 builds the final image prompt from **three layers** — not from Creative DNA prose alone:

```
final_prompt = reference_regeneration_prompt
             + brand_dna_color_resolution
             + calendar_content_overlay
```

| Layer | Source | What it supplies | What it must NOT supply |
|-------|--------|------------------|-------------------------|
| **1 — Reference layout** | `{pin}-reference-prompt.md` via `creative._meta.reference_prompt_ref` | Zones, margins, typography placement, decorative structure, **hero subject (person/object/pose/placement)**, `must_preserve` | Final hex colors, brand copy, campaign headline |
| **2 — Brand theme** | `BRAND_DNA.json` | All resolved hex colors, typography family, logo rules, `imagery.avoid`, voice constraints | Layout zones, composition changes |
| **3 — Content** | `{slug}.CREATIVE_DNA.json` → `elements[]` + calendar row | On-image copy (headline, subheadline, footer URL), CTA label | Layout structure, colors |

**If `reference_prompt_ref` is missing:** fall back to legacy merge (`BRAND_DNA.json` + `{slug}.CREATIVE_DNA.json` only) — but Phase 6a should run for every Pinterest-backed creative to avoid layout drift.

---

## Merge algorithm (Phase 8)

### Step 1 — Load inputs

```bash
BRAND_DNA.json
{slug}.CREATIVE_DNA.json
{reference_prompt_ref}   # e.g. ../../references/pinterest/pin-01-*-reference-prompt.md
content-calendar.md row  # optional overrides
```

### Step 2 — Start from reference regeneration prompt

1. Read the **Regeneration prompt** section from `{pin}-reference-prompt.md`.
2. Copy `must_preserve` and zone map into `{slug}-prompt.md`.
3. Keep all layout/composition language verbatim unless it conflicts with `single-image-post-policy.md`.
4. Copy `## Hero subject (must preserve)` from the reference prompt into `{slug}-prompt.md` when present.
5. Append [reference fidelity block](./reference-fidelity.md#phase-8--prompt-merge) to the Generation prompt.

### Step 3 — Resolve color roles → Brand DNA hex

Replace every `{{ROLE}}` placeholder in the reference prompt with Brand DNA values:

| Placeholder | Brand DNA path | Notes |
|-------------|----------------|-------|
| `{{BACKGROUND}}` | See [background_mode](#background) below | `primary_dark` for dark editorial |
| `{{TEXT_PRIMARY}}` | `visual_identity.text_on_dark` or `text` | Based on `background_mode` |
| `{{TEXT_SECONDARY}}` | `visual_identity.text_on_dark` or `secondary_light` | Subhead on dark often accent |
| `{{TEXT_MUTED}}` | `visual_identity.text_muted` | Footer, counters |
| `{{ACCENT}}` | `visual_identity.secondary_light` | Rules, highlight words |
| `{{ACCENT_SECONDARY}}` | `visual_identity.revenue_light` or `primary_light` | Optional second highlight |

Also inject a **COLORS** block after role substitution:

```
COLORS (mandatory — all from BRAND_DNA.json):
- Background: {resolved_background_hex}
- Primary: {brand.visual_identity.primary}
- Primary dark: {brand.visual_identity.primary_dark}
- Secondary / accent: {brand.visual_identity.secondary_light}
- Text on dark: {brand.visual_identity.text_on_dark}
- Muted text: {brand.visual_identity.text_muted}
All colors from brand palette — ignore reference image colors.
```

**Hard rule:** Never pass hex values from the Pinterest pin or from `creative.visual_identity` in the reference image. Creative DNA may document source hex for audit only — Phase 8 ignores them.

### Step 4 — Overlay latest content

Replace reference **variable_slots** with this post's copy from `creative.elements[]`:

| Element type | Source | Prompt instruction |
|--------------|--------|-------------------|
| `headline` | `elements[].content` where `type=headline` | Exact string — do not paraphrase |
| `subheadline` | `elements[].content` where `type=subheadline` | Exact string |
| `footer` | `elements[].content` or `brand.brand.website` | Exact string |
| `stat` | calendar row only if provided | Never invent |
| `cta_button` | `creative.copy.cta` | Label only if zone exists in reference |

Write an **ON-IMAGE COPY — MANDATORY** table in `{slug}-prompt.md` with resolved Brand DNA hex per zone.

Remove or strike through the reference prompt's "Reference copy (replace in Phase 8)" block in the final generation prompt — only merged copy appears in **Generation prompt**.

### Step 5 — Append brand constraints

From `BRAND_DNA.json`:

- `typography.family` (+ fallback)
- `imagery.avoid` → **Do not** section
- `logo.dont` + overlay workflow if applicable
- `brand.brand.name` / `descriptor` for context line only

### Step 6 — Write `{slug}-prompt.md`

```markdown
# {Title}

**Creative ID:** `{slug}`
**DNA merge:** reference-prompt + BRAND_DNA.json + {slug}.CREATIVE_DNA.json
**Reference prompt:** {reference_prompt_ref}
**Calendar ref:** content-calendar.md → [date row]

## ON-IMAGE COPY — MANDATORY (exact)
[Table: zone | text | brand hex]

## Zone map
[From reference prompt — unchanged]

## must_preserve
[From reference prompt]

## Generation prompt
[Merged: reference layout prose + resolved colors + overlaid copy]

## Do not
[brand imagery.avoid + reference must_not_change layout rules]

## Post / caption
[{slug}-post.md]
```

---

## Legacy merge (no reference prompt)

When `reference_prompt_ref` is absent:

```
final = BRAND_DNA.json + {slug}.CREATIVE_DNA.json + calendar_row_overrides
```

Use the [Prompt assembly template](#prompt-assembly-template-legacy) below.

### Conflict resolution (legacy)

| Field | Winner |
|-------|--------|
| **All colors** | **Brand DNA** |
| Fonts, logo rules, voice, imagery.avoid | Brand DNA |
| Composition, zones, hero, structure_type | Creative DNA |
| Headline, stat, topic, CTA | Calendar row → `elements[]` |

---

## Color resolution (Brand DNA only)

Resolve every color from `brand.visual_identity` at merge time. Use creative DNA only for **layout tone** (`background_mode`) and **structural roles**.

### Background

Read `creative.visual_identity.background_mode` (preferred) or infer from `structure_type`:

| `background_mode` | Brand token | Typical use |
|-------------------|-------------|-------------|
| `light` (default) | `brand.visual_identity.background` (`#F8FAFC`) | Light editorial |
| `dark` | `brand.visual_identity.primary_dark` | Dark editorial — **not** pure black |
| `primary` | `brand.visual_identity.primary` | Full-bleed brand hero |

`background_treatment` describes **texture only** (gradient direction, grain) — never the base hex.

### Accents & text

| Role | Brand token |
|------|-------------|
| Primary accent / highlight word / vertical rule | `secondary_light` |
| Secondary accent / revenue KPI | `revenue` / `revenue_light` |
| AI badge / agent indicator | `ai` |
| Body text on light bg | `text` |
| Body text on dark bg | `text_on_dark` |
| Muted subline / footer | `text_muted` |
| CTA button (primary) | `primary` fill + `text_on_dark` label |

### Element style mapping

When iterating `creative.elements`, map by `element.type` and `color_role` — ignore `element.style.color` hex from Creative DNA files.

---

## Prompt assembly template (legacy)

Use only when no `reference_prompt_ref` exists:

```
Create an ultra-premium {brand.visual_identity.style} advertisement for {brand.brand.name} — {brand.brand.descriptor}.

Topic: {creative.concept.topic}
Structure: {creative.structure_type}
CANVAS: {creative.canvas.ratio}

COLORS (all from BRAND_DNA):
[resolved hex block]

COMPOSITION:
[zones from creative.composition]

ON-IMAGE COPY (exact):
[elements[]]

DO NOT:
[imagery.avoid]
```

---

## Image generator (Phase 9)

### Description build

1. Use **Generation prompt** section from merged `{slug}-prompt.md` (already includes reference layout + brand colors + content).
2. **Always** pass the reference pin image:

```
reference_image_paths: [creative._meta.reference_asset]
```

3. Start the generator `description` with: `Recreate the attached reference image layout closely. Same composition and hero subject placement. Apply brand colors and replace text only.`
4. Condense to 1–2 paragraphs if needed, but **never drop** hero subjects, objects, exact on-image copy, or `must_preserve` layout rules.

See [reference-fidelity.md](./reference-fidelity.md).

---

## Merge checklist (Phase 8 gate)

Before writing `{slug}-prompt.md` or calling GenerateImage:

- [ ] `reference_prompt_ref` loaded (or legacy path documented)
- [ ] All `{{COLOR_ROLE}}` placeholders resolved to Brand DNA hex
- [ ] No `#` values from pin or `creative.visual_identity`
- [ ] On-image copy matches `elements[]` exactly — reference pin copy removed
- [ ] `must_preserve` from reference prompt included in final prompt
- [ ] Prompt includes: `All colors from brand palette — ignore reference image colors`
- [ ] Dark layouts use `primary_dark`, not `#000000`

---

## Variant generation

1. Keep same `reference_prompt_ref` for layout consistency
2. Copy `{slug}.CREATIVE_DNA.json` → change only `variable_slots` (headline, subheadline)
3. Re-run Phase 8–9 — reference layout + brand colors auto-merge; only content changes
