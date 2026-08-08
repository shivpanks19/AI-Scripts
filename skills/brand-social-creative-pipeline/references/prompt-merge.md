# DNA → Image Prompt Merge

Use when building `{slug}-prompt.md` (Phase 8) or calling the image generator (Phase 9).

## Merge order

```
final = BRAND_DNA.json + {slug}.CREATIVE_DNA.json + calendar_row_overrides
```

## Conflict resolution

| Field | Winner |
|-------|--------|
| **All colors** (background, accents, text, CTA fills, halos, glows, element `style.color`) | **Brand DNA** |
| Fonts, logo rules, voice, imagery.avoid | Brand DNA |
| Composition, zones, elements (layout roles), hero, canvas, structure_type, effects (on/off only) | Creative DNA |
| Headline, stat, topic, CTA for this post | Calendar row → update creative `copy` + `elements` |

**Hard rule:** Never pass hex values from `creative.visual_identity` or `elements[].style` into the generation prompt. Creative DNA may record reference-source colors for documentation only — they are **ignored at merge time**.

Never override `visual_identity.primary`, `secondary`, `typography.family` in creative files.

## Color resolution (Brand DNA only)

Resolve every color from `brand.visual_identity` at merge time. Use creative DNA only for **layout tone** (`background_mode`) and **structural roles** (headline zone, stat card, CTA button).

### Background

Read `creative.visual_identity.background_mode` (preferred) or infer from `structure_type`:

| `background_mode` | Brand token | Typical use |
|-------------------|-------------|---------------|
| `light` (default) | `brand.visual_identity.background` (`#F8FAFC`) | Default Swayam editorial, stat cards on light |
| `dark` | `brand.visual_identity.primary_dark` (`#0F2744`) | Dark editorial / carousel covers — **not** pure black |
| `primary` | `brand.visual_identity.primary` (`#1E3A5F`) | Full-bleed navy hero |

`background_treatment` in creative DNA describes **texture only** (gradient direction, grain, blur) — never the base hex. Example: `subtle film grain 2%` on top of `primary_dark`.

### Accents & text

| Role | Brand token |
|------|-------------|
| Primary accent / highlight word / vertical rule | `secondary_light` (`#14B8A6`) |
| Secondary accent / revenue KPI | `revenue` / `revenue_light` |
| AI badge / agent indicator | `ai` (`#6366F1`) |
| Body text on light bg | `text` (`#0F172A`) |
| Body text on dark bg | `text_on_dark` (`#FFFFFF`) |
| Muted subline / footer | `text_muted` (`#64748B`) |
| CTA button (primary) | `primary` fill + `text_on_dark` label, or `secondary` fill per brief |
| Card surface on dark bg | `neutral_50` or white at 92% opacity |
| WhatsApp UI chrome only | `whatsapp_ui_only` |

### Effects colors

| Creative flag | Brand token |
|---------------|-------------|
| `effects.halo` | `ai` or `ai_muted` |
| `effects.glow_accent` | `secondary_light` |

### Element style mapping

When iterating `creative.elements`, ignore `element.style.color` and `element.style.background` hex from the file. Map by `element.type`:

| Element type | Text color | Background |
|--------------|------------|------------|
| `headline`, `stat` (on dark) | `text_on_dark` | per card rules |
| `headline`, `stat` (on light) | `text` | white / `neutral_50` |
| `subheadline` | `text_muted` | null |
| `cta_button` | `text_on_dark` | `primary` or `secondary` |
| `badge` (accent) | `secondary` | `secondary` at 10% tint |
| highlight / accent inline word | `secondary_light` | null |

Determine light vs dark from resolved `background_mode`, not from creative hex.

## Prompt assembly template

```
Create an ultra-premium {brand.visual_identity.style} advertisement for {brand.brand.name} — {brand.brand.descriptor}.

Topic: {creative.concept.topic}
Message: {creative.concept.message}
Structure: {creative.structure_type}

CANVAS: {creative.canvas.ratio} ({creative.canvas.width}x{creative.canvas.height})

COLORS (mandatory — all from BRAND_DNA, never from creative reference):
- Background: {resolved_background_hex} — {creative.visual_identity.background_treatment}
- Primary: {brand.visual_identity.primary}
- Primary dark: {brand.visual_identity.primary_dark}
- Secondary / accent: {brand.visual_identity.secondary_light}
- Revenue accent: {brand.visual_identity.revenue}
- AI surface: {brand.visual_identity.ai}
- Text: {resolved_text_hex}
- Muted text: {brand.visual_identity.text_muted}

TYPOGRAPHY: {brand.typography.family}, {creative.typography.headline_weight} headlines

COMPOSITION:
{for each zone in creative.composition.zones}
- {zone_name}: {position}, {scale}, z-{z_index}
{endfor}

HERO:
- Type: {creative.hero.type}
- Subject: {creative.hero.subject}
- Pose: {creative.hero.pose}
- Product: {creative.hero.product}

ON-IMAGE COPY (exact — do not paraphrase):
{for each element in creative.elements}
- [{element.type}] {element.content}
{endfor}

CTA: {creative.copy.cta}
Footer URL: {brand.brand.website}

VISUAL LANGUAGE:
- Geometry: {creative.visual_language.geometry}
- Lighting: {creative.visual_language.lighting}
- Depth: {creative.visual_language.depth}
- Materials: {creative.visual_language.materials}

EFFECTS: halo={effects.halo}, particles={effects.particles}

DO NOT:
{brand.imagery.avoid joined}
- Invent fake metrics not in copy lock
- {brand.logo.dont}

STYLE REFERENCE: {brand.visual_identity.style} — Apple × Stripe × Linear editorial SaaS, not Canva template, not sci-fi AI brain clipart.
```

## Image generator `description` (short form)

Condense merged prompt to 1–2 paragraphs for `GenerateImage`:

1. Canvas ratio + style line
2. Zone layout (headline position, card, hero)
3. Exact headline + stat + CTA text
4. Hero casting + phone/product if applicable
5. **Brand hex colors only** — run color resolution above; never quote creative DNA hex
6. Footer URL + logo zone

## Merge checklist (Phase 8 gate)

Before writing `{slug}-prompt.md` or calling GenerateImage:

- [ ] `background_mode` resolved → brand background hex applied
- [ ] No `#` values copied from `creative.visual_identity`
- [ ] No `#` values copied from `elements[].style`
- [ ] Accent/highlight uses `secondary_light`, not Pinterest/reference teal unless it matches brand
- [ ] Dark layouts use `primary_dark`, not `#000000` / `#0A0A0A`
- [ ] Prompt includes explicit line: `All colors from brand palette — ignore reference image colors`

## Variant generation

To create a new post using an existing Creative DNA template:

1. Copy `{slug}.CREATIVE_DNA.json` → `{new-slug}.CREATIVE_DNA.json`
2. Change only fields listed in `replication.variable_slots`
3. Keep `replication.must_preserve` structure intact
4. Re-run Phase 8–9
