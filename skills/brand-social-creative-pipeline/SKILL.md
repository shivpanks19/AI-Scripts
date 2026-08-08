---
name: brand-social-creative-pipeline
description: >-
  End-to-end pipeline from website/brief to brand identity, social context,
  strategy, calendar, copy, Brand DNA, Creative DNA, image prompts, and generated
  creatives. Use when the user wants a full social media setup for a brand,
  brand DNA, creative DNA, social calendar with visuals, or to replicate the
  Swayam brand-to-creative workflow from website + reference images.
---

# Brand → Social → Creative Pipeline

Orchestrates the full workflow: **brand identity → social context → strategy → calendar → copy → Brand DNA → Creative DNA → prompts → generated images**.

Run phases in order. Skip only phases the user explicitly says are done. After each phase, save deliverables to the client folder before continuing.

**Reference implementation:** `docs/swayam/` (BRAND_IDENTITY.md, BRAND_DNA.json, instagram/*/*.CREATIVE_DNA.json)

---

## Phase 0 — Intake

Collect from the user (ask only for missing items):

| Input | Required | Notes |
|-------|----------|-------|
| Website URL | Yes | Fetch homepage, product, pricing if available |
| Client slug | Yes | e.g. `swayam` → `docs/swayam/` |
| Brand files | Optional | Existing decks, logos, ICP docs, feature lists |
| Platforms | Yes | Instagram, LinkedIn, Meta ads, etc. |
| Calendar horizon | Yes | `weekly` or `monthly` |
| Reference creatives | Optional | Images to reverse-engineer into Creative DNA templates |
| Goals | Optional | Awareness, leads, demos, community |

Create client scaffold:

```
clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md          # Phase 1
├── BRAND_DNA_SCHEMA.json      # copy from templates/
├── BRAND_DNA.json             # Phase 5
├── CREATIVE_DNA_SCHEMA.json   # copy from templates/
├── instagram/
├── linkedin/
└── plans/
    ├── social-media-context.md    # Phase 2 (or docs/swayam/social-media-context-sms.md if global)
    ├── content-strategy.md        # Phase 3
    └── content-calendar.md        # Phase 4
```

Initialize `client.json` with `website`, `display_name`, `folders`, `channels`.

---

## Phase 1 — Brand Identity

**Skill:** `design-brand-guardian`

1. Fetch and analyze the website (copy, visuals, positioning, product, audience).
2. Merge with any user-supplied brand files.
3. Write `clients/{client_slug}/BRAND_IDENTITY.md` using the Brand Guardian deliverable template:
   - Brand foundation (purpose, vision, mission, values, personality, promise)
   - Brand architecture and positioning
   - Visual identity (colors as CSS variables, typography, logo system, UI patterns)
   - Voice & messaging (taglines, vocabulary prefer/avoid)
   - Imagery guidelines
   - Go-to-market pillars

**Gate:** User approves brand identity before Phase 2 (unless they say proceed).

---

## Phase 2 — Social Media Context

**Skill:** `social-media-context-sms`

1. Read `BRAND_IDENTITY.md` + `client.json`.
2. Map brand voice → social voice; positioning → audience; pillars → content pillars.
3. Write context file. Prefer client-scoped path:
   - `clients/{client_slug}/plans/social-media-context.md`
   - Or update `docs/swayam/social-media-context-sms.md` if user wants one global profile.

Required sections: Identity, Target Audience, Voice & Tone, Content Pillars, Platform Configuration, Content Formats, Example Posts (draft if none), Anti-Patterns.

---

## Phase 3 — Content Strategy

**Skill:** `content-strategy-sms`

1. Read social media context + brand identity.
2. Ask discovery questions only if gaps remain (goals, performance, competitors, time budget).
3. Write `clients/{client_slug}/plans/content-strategy.md`:
   - Content pillars + balance ratios
   - Topic clusters per pillar
   - Weekly content mix per platform
   - Differentiation (voice positioning, content gaps, underserved segments)

---

## Phase 4 — Content Calendar

**Skill:** `content-calendar-sms`

1. Read strategy + context.
2. Build **weekly** or **monthly** calendar per user request.
3. Write `clients/{client_slug}/plans/content-calendar.md`.

Each calendar row must include:

| Field | Example |
|-------|---------|
| Date / day | 2026-08-08 |
| Platform | instagram |
| Pillar | educational |
| Topic / angle | AI automation for admissions |
| Format | stat-hero poster |
| `creative_template_ref` | `{slug}` of matching Creative DNA |
| Copy type | caption / post |

Reserve 20–30% slots as `[Flexible]`. Map visual slots to a `creative_template_ref` when reference creatives exist.

---

## Phase 5 — Brand DNA

**Schemas:** `templates/BRAND_DNA_SCHEMA.json` → copy to client root.

1. Read `BRAND_IDENTITY.md`.
2. Extract invariant brand tokens into `clients/{client_slug}/BRAND_DNA.json` following the schema exactly.
3. Set `_meta.brand_id`, `_meta.source_ref`, `_meta.schema_ref`.

**Brand DNA is one file per client.** Never put layout, composition, or per-image copy here.

**Merge rule:** Brand DNA wins on colors, typography, logo, voice, imagery constraints.

---

## Phase 6 — Creative DNA (per reference image)

**Schemas:** `templates/CREATIVE_DNA_SCHEMA.json` → copy to client root.

For **each** reference creative image the user provides (or each distinct layout in the client's existing library):

1. Analyze the image: map zones, elements, exact on-image copy, hero, canvas, effects.
2. Write one file per image:

```
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}.CREATIVE_DNA.json
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}.png          # reference or generated
```

Naming: `{slug}.CREATIVE_DNA.json` (not a shared registry).

3. Populate `replication.must_preserve` and `replication.variable_slots` so future variants keep structure.

**If no reference images:** create Creative DNA from brief + brand identity for each calendar visual format (stat-hero, editorial-search-hero, myth-truth, etc.) before Phase 8.

---

## Phase 7 — Copy (posts & captions)

For each calendar slot:

| Platform type | Skill |
|---------------|-------|
| LinkedIn, X, Threads, Bluesky | `post-writer-sms` |
| Instagram, Facebook, TikTok, Pinterest, YouTube | `caption-writer-sms` |

1. Read social media context + brand voice from `BRAND_DNA.json`.
2. Write copy aligned to pillar, topic, and CTA from brand DNA (`voice.cta_primary`).
3. Save alongside the creative:

```
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}-caption.md
clients/{client_slug}/linkedin/{YYYY-MM-DD}/{slug}-post.md
```

Update `copy.caption` in the Creative DNA when the visual and caption are paired.

---

## Phase 8 — Prompt build (per calendar visual)

For each calendar entry with a visual:

1. Load `BRAND_DNA.json` + matching `{slug}.CREATIVE_DNA.json`.
2. Merge per `CREATIVE_DNA_SCHEMA.json` merge rules.
3. Write `{slug}-prompt.md` with:

```markdown
# {Title}

**Creative ID:** `{slug}`
**DNA merge:** BRAND_DNA.json + {slug}.CREATIVE_DNA.json
**Calendar ref:** content-calendar.md → [date row]

## ON-IMAGE COPY — MANDATORY (exact)
[Table from creative_dna.elements + copy zones]

## Zone map
[ASCII layout from composition.zones]

## Generation prompt
[Merged prompt: brand colors/fonts/style + creative structure/hero/elements]

## Do not
[brand imagery.avoid + creative constraints]

## Caption
[From Phase 7]
```

See [references/prompt-merge.md](references/prompt-merge.md) for merge algorithm.

---

## Phase 9 — Generate images

For each `{slug}-prompt.md`:

1. Use the LLM's **image generation tool** (e.g. `GenerateImage`).
2. Match `creative_dna.canvas.ratio`:
   - `4:5` → aspect_ratio `3:4` or `9:16` per tool support
   - `1:1` → `1:1`
   - `16:9` → `16:9`
3. Build `description` from merged prompt: headline, stat, hero casting, colors (hex), style, CTA, footer URL.
4. Save output to `{slug}.png` next to Creative DNA.
5. Update `_meta.reference_asset` in Creative DNA if first generation.

**Quality loop:** If generated copy drifts from the copy lock, note in prompt that exact text must appear; offer Figma composite for pixel-perfect type.

**Do not** invent fake metrics unless provided in the calendar brief.

---

## Phase 10 — Handoff

Deliver summary:

```markdown
# {Client} — Pipeline Complete

## Files
- Brand: BRAND_IDENTITY.md, BRAND_DNA.json
- Social: plans/social-media-context.md, content-strategy.md, content-calendar.md
- Creatives: [list paths with DNA + prompt + png + caption]

## Calendar execution
| Date | Platform | Slug | Asset | Status |
...

## Next steps
- Schedule posts (BlackTwist if connected)
- A/B variant: change variable_slots only, keep must_preserve
```

---

## Pipeline checklist

Copy and track:

```
- [ ] Phase 0: Intake + client scaffold
- [ ] Phase 1: BRAND_IDENTITY.md (design-brand-guardian)
- [ ] Phase 2: social-media-context (social-media-context-sms)
- [ ] Phase 3: content-strategy.md (content-strategy-sms)
- [ ] Phase 4: content-calendar.md (content-calendar-sms)
- [ ] Phase 5: BRAND_DNA.json
- [ ] Phase 6: {slug}.CREATIVE_DNA.json per reference/template
- [ ] Phase 7: captions/posts per calendar slot
- [ ] Phase 8: {slug}-prompt.md per visual
- [ ] Phase 9: {slug}.png generated
- [ ] Phase 10: Handoff summary
```

---

## Partial runs

| User request | Start at |
|--------------|----------|
| "Brand only" | Phase 1 → 5 |
| "Calendar + creatives" | Phase 4 (requires 1–3, 5–6) |
| "New creative from reference" | Phase 6 → 9 |
| "New variant of existing template" | Phase 8 → 9 (swap variable_slots) |
| "Copy only" | Phase 7 |

---

## Boundaries

- Does not replace sub-skills — invoke them for their domain steps.
- Does not commit to git unless user asks.
- Does not publish/schedule unless BlackTwist MCP is connected and user confirms.
- Brand DNA = one per client; Creative DNA = one per image. Never use a shared creative registry.

## See also

- [references/file-structure.md](references/file-structure.md) — folder conventions
- [references/prompt-merge.md](references/prompt-merge.md) — DNA → prompt merge
- `docs/swayam/` — canonical example
