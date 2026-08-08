---
name: brand-social-creative-pipeline
description: >-
  End-to-end pipeline from website/brief to brand identity, social context,
  strategy, calendar, copy, Brand DNA, Creative DNA, image prompts, and generated
  creatives. Use when the user wants a full social media setup for a brand,
  brand DNA, creative DNA, social calendar with visuals, or to replicate the
  Swayam brand-to-creative workflow from website + brand identity (Pinterest
  references are auto-fetched in Phase 1b — no manual reference images required).
---

# Brand → Social → Creative Pipeline

Orchestrates the full workflow: **brand identity → Pinterest references → social context → strategy → calendar → copy → Brand DNA → Creative DNA → prompts → generated images**.

Run phases in order. Skip only phases the user explicitly says are done. After each phase, save deliverables to the client folder before continuing.

**Reference implementation:** `clients/swayam/` (BRAND_IDENTITY.md, BRAND_DNA.json, instagram/*/*.CREATIVE_DNA.json)

---

## Phase 0 — Intake

Collect from the user (ask only for missing items):

| Input | Required | Notes |
|-------|----------|-------|
| Website URL | Yes | Fetch homepage, product, pricing if available |
| Client slug | Optional | take it fromwebsite given `swayamapp.com` → `clients/swayamapp/` |
| Brand files | Optional | Existing decks, logos, ICP docs, feature lists |
| Platforms | Yes | Instagram, LinkedIn, Meta ads, etc. |
| Calendar horizon | Yes | `weekly` or `monthly` |
| Reference creatives | **No** — not required | Phase 1b auto-fetches 5 Pinterest pins from `BRAND_IDENTITY.md`. Optional: user may upload extra refs to merge in Phase 6 |
| Goals | Optional | Awareness, leads, demos, community |

Create client scaffold:

```
clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md          # Phase 1
├── BRAND_DNA_SCHEMA.json      # copy from templates/
├── BRAND_DNA.json             # Phase 5
├── CREATIVE_DNA_SCHEMA.json   # copy from templates/
├── references/
│   └── pinterest/             # Phase 1b — 5 fetched pin images + manifest
├── instagram/
├── linkedin/
└── plans/
    ├── social-media-context.md    # Phase 2 (or clients/swayam/social-media-context-sms.md if global)
    ├── content-strategy.md        # Phase 3
    └── content-calendar.md        # Phase 4
```

Initialize `client.json` with `website`, `display_name`, `folders`, `channels`.

**Reference creatives:** Do not ask the user for Pinterest URLs or layout images at intake. Phase 1b supplies the default reference set after brand identity.

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

**Gate:** User approves brand identity before Phase 1b (unless they say proceed).

---

## Phase 1b — Pinterest reference fetch

**Skill:** [references/pinterest-reference-fetch/SKILL.md](references/pinterest-reference-fetch/SKILL.md)

Runs **only after** `BRAND_IDENTITY.md` exists. Replaces manual “paste 5 Pinterest URLs” intake.

1. Read `BRAND_IDENTITY.md` — extract product category, industry, audience, visual tone.
2. Build category-specific Pinterest search queries (e.g. CRM → SaaS CRM pins; CSR → CSR campaign pins). See [search-keywords.md](references/pinterest-reference-fetch/search-keywords.md).
3. Search Pinterest (WebSearch + WebFetch); select **5 pins** with layout diversity.
4. Download pin images to `clients/{client_slug}/references/pinterest/pin-01-{layout}.png` … `pin-05-{layout}.png`.
5. Write `search-brief.json`, `pinterest-manifest.json`, and `README.md`.

**Outputs:** `clients/{client_slug}/references/pinterest/` (5 PNGs + manifest). Phase 6 consumes this folder.

**Skip only if:** user explicitly provided ≥5 reference images in Phase 0 and says skip Pinterest fetch.

**Gate:** Manifest lists 5 valid PNGs before Phase 2.

---

## Phase 2 — Social Media Context

**Skill:** `social-media-context-sms`

1. Read `BRAND_IDENTITY.md` + `client.json`.
2. Map brand voice → social voice; positioning → audience; pillars → content pillars.
3. Write context file. Prefer client-scoped path:
   - `clients/{client_slug}/plans/social-media-context.md`
   - Or update `clients/swayam/social-media-context-sms.md` if user wants one global profile.

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

**Merge rule:** Brand DNA wins on **all colors** (background, accents, text, CTA fills, effect colors), typography, logo, voice, imagery constraints. Creative DNA never supplies final hex values at render time — only layout roles and `background_mode` (light | dark | primary).

---

## Phase 6 — Creative DNA (per reference image)

**Schemas:** `templates/CREATIVE_DNA_SCHEMA.json` → copy to client root.

For **each** pin in `clients/{client_slug}/references/pinterest/pinterest-manifest.json` (Phase 1b), plus any user-supplied references from Phase 0:

1. Analyze the image: map zones, elements, exact on-image copy, hero, canvas, effects.
2. Write one file per image:

```
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}.CREATIVE_DNA.json
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}.png          # reference or generated
```

Naming: `{slug}.CREATIVE_DNA.json` (not a shared registry).

3. Populate `replication.must_preserve` and `replication.variable_slots` so future variants keep structure.

**Color authoring rule:** When reverse-engineering a reference (e.g. Pinterest), record layout and zones in Creative DNA. Set `visual_identity.background_mode` to `light`, `dark`, or `primary` — do **not** treat reference hex (e.g. `#0A0A0A` pure black) as the render color. Optional `visual_identity.*` hex fields are documentation of the source image only; Phase 8 ignores them and resolves from Brand DNA. See [references/prompt-merge.md](references/prompt-merge.md#color-resolution-brand-dna-only).

**If Phase 1b was skipped and no user references:** create Creative DNA from brief + brand identity for each calendar visual format (stat-hero, editorial-search-hero, myth-truth, etc.) before Phase 8.

---

## Phase 7 — Copy (posts & captions)

For each calendar slot, **invoke the sub-skill** — do not improvise copy outside it.

| Platform type | Skill | Output file |
|---------------|-------|-------------|
| LinkedIn, X, Threads, Bluesky, **Instagram, Facebook** | `post-writer-sms` | `{slug}-post.md` |
| TikTok, Pinterest, YouTube | `caption-writer-sms` | `{slug}-caption.md` |

1. Read `plans/social-media-context.md` + brand voice from `BRAND_DNA.json`.
2. Invoke **post-writer-sms** for Instagram and Facebook (visual feed posts with paired image) — follow that skill's Facebook and Instagram sections in `skills/post-writer-sms/SKILL.md`.
3. Write copy aligned to pillar, topic, and CTA from brand DNA (`voice.cta_primary`).
4. Save alongside the creative:

```
clients/{client_slug}/instagram/{YYYY-MM-DD}/{slug}-post.md
clients/{client_slug}/facebook/{YYYY-MM-DD}/{slug}-post.md
clients/{client_slug}/linkedin/{YYYY-MM-DD}/{slug}-post.md
clients/{client_slug}/tiktok/{YYYY-MM-DD}/{slug}-caption.md   # caption-writer only
```

Update `copy.post_ref` (or `copy.caption_ref` for caption-writer platforms) in the Creative DNA when the visual and copy are paired.

**Legacy:** Older runs may have `{slug}-caption.md` on Instagram/Facebook — Phase 9b publish resolves `-post.md` first, then falls back to `-caption.md`.

---

## Phase 8 — Prompt build (per calendar visual)

For each calendar entry with a visual:

1. Load `BRAND_DNA.json` + matching `{slug}.CREATIVE_DNA.json`.
2. Merge per `CREATIVE_DNA_SCHEMA.json` merge rules — **resolve all colors from Brand DNA** (see [references/prompt-merge.md](references/prompt-merge.md#color-resolution-brand-dna-only)).
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
[Merged prompt: **brand colors only** (resolved background_mode + brand tokens) + creative structure/hero/elements — never creative hex]

## Do not
[brand imagery.avoid + creative constraints]

## Post / caption
[From Phase 7 — `{slug}-post.md` for Instagram/Facebook/LinkedIn; `{slug}-caption.md` for TikTok/Pinterest/YouTube]
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
3. Build `description` from merged prompt: headline, stat, hero casting, **brand palette hex only** (run color resolution — no creative DNA hex), style, CTA, footer URL.
4. Save output to `{slug}.png` next to Creative DNA.
5. Update `_meta.reference_asset` in Creative DNA if first generation.

**Color gate:** If the prompt or description contains hex values not present in `BRAND_DNA.json`, stop and re-run Phase 8 merge.

**Quality loop:** If generated copy drifts from the copy lock, note in prompt that exact text must appear; offer Figma composite for pixel-perfect type.

**Do not** invent fake metrics unless provided in the calendar brief.

---

## Phase 9b — Publish to Firestore (after each image)

**Skill:** [references/firestore-creative-publish/SKILL.md](references/firestore-creative-publish/SKILL.md)

Runs **immediately after** each `{slug}.png` is saved in Phase 9. Mirrors Swayam weekly [Phase 4c + 5b + 6](../../../clients/swayam/swayam-weekly-automation.md#phase-5--publish).

**Prerequisite:** Webhook (or explicit run prompt) must include `outletId`. Optional: `collection`, `templateName`, `source`. **Stop** if `outletId` is missing — do not read from `client.json`.

Per slug:

1. **Upload** PNG to GCS via `POST https://image-function-926896730665.europe-west1.run.app` (base64 data URL).
2. **Publish** draft to `OUTLET/{outletId}/social-ai-poster` via `POST https://crm-demo-2fc0c.web.app/ai-content`.
3. **Verify** response: `documentId`, `path`, `imageUrl`, `slug`; confirm on-image text matches prompt copy lock.
4. **Log** to `{creative_folder}/publish-log.md`.

**Inputs:** `{slug}.png`, `{slug}-prompt.md`, `{slug}-post.md` (or `{slug}-caption.md` fallback), `outletId` from webhook.

**Skip only when:** user says local-only / do not publish, or webhook did not include `outletId`.

**Do not** set `showAsTemplate` on weekly pipeline drafts.

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
| Date | Platform | Slug | Asset | Firestore path | Status |
...

## Publish log
- `instagram/{YYYY-MM-DD}/publish-log.md` — documentId, GCS imageUrl per slug (Phase 9b)

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
- [ ] Phase 1b: 5 Pinterest pins → references/pinterest/ (pinterest-reference-fetch)
- [ ] Phase 2: social-media-context (social-media-context-sms)
- [ ] Phase 3: content-strategy.md (content-strategy-sms)
- [ ] Phase 4: content-calendar.md (content-calendar-sms)
- [ ] Phase 5: BRAND_DNA.json
- [ ] Phase 6: {slug}.CREATIVE_DNA.json per reference/template
- [ ] Phase 7: captions/posts per calendar slot
- [ ] Phase 8: {slug}-prompt.md per visual
- [ ] Phase 9: {slug}.png generated
- [ ] Phase 9b: GCS upload + Firestore publish per slug (firestore-creative-publish)
- [ ] Phase 10: Handoff summary
```

---

## Partial runs

| User request | Start at |
|--------------|----------|
| "Brand only" | Phase 1 → 1b → 5 |
| "Pinterest refs only" | Phase 1b (requires BRAND_IDENTITY.md) |
| "Calendar + creatives" | Phase 4 (requires 1–1b–3, 5–6) |
| "New creative from reference" | Phase 6 → 9 (sources: references/pinterest/) |
| "New variant of existing template" | Phase 8 → 9 (swap variable_slots) |
| "Copy only" | Phase 7 |
| "Publish existing PNG" | Phase 9b only (requires `outletId` in webhook or run prompt) |

---

## Boundaries

- Does not replace sub-skills — invoke them for their domain steps.
- Does not commit to git unless user asks.
- Does not publish unless webhook (or explicit run prompt) supplies `outletId`. Does not schedule to social unless BlackTwist MCP is connected and user confirms.
- Brand DNA = one per client; Creative DNA = one per image. Never use a shared creative registry.

## See also

- [references/file-structure.md](references/file-structure.md) — folder conventions
- [references/pinterest-reference-fetch/SKILL.md](references/pinterest-reference-fetch/SKILL.md) — fetch 5 Pinterest pins after brand identity
- [references/prompt-merge.md](references/prompt-merge.md) — DNA → prompt merge
- [references/firestore-creative-publish/SKILL.md](references/firestore-creative-publish/SKILL.md) — GCS upload + Firestore publish after Phase 9
- `clients/swayam/` — canonical example
