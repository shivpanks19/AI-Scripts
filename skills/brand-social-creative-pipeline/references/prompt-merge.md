# DNA → Image Prompt Merge

Use when building `{slug}-prompt.md` (Phase 8) or calling the image generator (Phase 9).

## Merge order

```
final = BRAND_DNA.json + {slug}.CREATIVE_DNA.json + calendar_row_overrides
```

## Conflict resolution

| Field | Winner |
|-------|--------|
| Colors, fonts, logo rules, voice, imagery.avoid | Brand DNA |
| Composition, zones, elements, hero, canvas, structure_type, effects | Creative DNA |
| Headline, stat, topic, CTA for this post | Calendar row → update creative `copy` + `elements` |

Never override `visual_identity.primary`, `secondary`, `typography.family` in creative files.

## Prompt assembly template

```
Create an ultra-premium {creative.visual_identity.style} advertisement for {brand.brand.name} — {brand.brand.descriptor}.

Topic: {creative.concept.topic}
Message: {creative.concept.message}
Structure: {creative.structure_type}

CANVAS: {creative.canvas.ratio} ({creative.canvas.width}x{creative.canvas.height})

COLORS (mandatory):
- Primary: {brand.visual_identity.primary}
- Secondary: {brand.visual_identity.secondary}
- Revenue accent: {brand.visual_identity.revenue}
- AI surface: {brand.visual_identity.ai}
- Background: {creative.visual_identity.background_treatment}

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
5. Brand hex colors by name
6. Footer URL + logo zone

## Variant generation

To create a new post using an existing Creative DNA template:

1. Copy `{slug}.CREATIVE_DNA.json` → `{new-slug}.CREATIVE_DNA.json`
2. Change only fields listed in `replication.variable_slots`
3. Keep `replication.must_preserve` structure intact
4. Re-run Phase 8–9
