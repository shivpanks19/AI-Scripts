# How the Brand → Social → Creative Pipeline Works

Human-readable overview of [`skills/brand-social-creative-pipeline/SKILL.md`](../skills/brand-social-creative-pipeline/SKILL.md).

**Branch:** `brand-gdrive`  
**Storage:** Google Drive (`gdrive/clients/{client_slug}/`) — see [google-drive-storage.md](../skills/brand-social-creative-pipeline/references/google-drive-storage.md)

**Canonical client examples on Drive:** `gdrive/clients/swayam/`, `gdrive/clients/eduhexa/`

---

## What it does

One ordered workflow: take a brand (website + optional files) and produce **social strategy, calendar, copy, image prompts, generated creatives**, and optionally **publish drafts to Firestore** for Social AI Poster.

All artifacts are saved to **Google Drive** under `clients/{client_slug}/` (folder ID `1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ`). Skills and templates live in the git repo on the `brand-gdrive` branch.

```
Website + intake
    → Brand identity          (Drive)
    → Pinterest layout refs   (Drive)
    → Social context & strategy (Drive)
    → Calendar                (Drive)
    → Brand DNA + Creative DNA (Drive)
    → Reference prompts (pin layout)
    → Copy + merged prompts + images (Drive)
    → Firestore publish (optional)
```

---

## Phase map

| Phase | Name | Main output (on Google Drive) | Skill / reference |
|-------|------|-------------------------------|-------------------|
| **0** | Intake | `client.json`, folder scaffold | Pipeline SKILL + [google-drive-storage.md](../skills/brand-social-creative-pipeline/references/google-drive-storage.md) |
| **1** | Brand identity | `BRAND_IDENTITY.md` | `design-brand-guardian` |
| **1b** | Pinterest refs | `references/pinterest/` (5 pins + manifest) | `pinterest-reference-fetch` |
| **2** | Social context | `plans/social-media-context.md` | `social-media-context-sms` |
| **3** | Content strategy | `plans/content-strategy.md` | `content-strategy-sms` |
| **4** | Content calendar | `plans/content-calendar.md` | `content-calendar-sms` |
| **5** | Brand DNA | `BRAND_DNA.json` | Schema in `templates/` |
| **6a** | Reference prompt | `pin-*-reference-prompt.md` per pin | `reference-creative-prompt` |
| **6** | Creative DNA | `{slug}.CREATIVE_DNA.json` per layout/post | Links to pin + calendar copy |
| **7** | Copy | `{slug}-post.md` / `{slug}-caption.md` | `post-writer-sms`, `caption-writer-sms` |
| **8** | Prompt build | `{slug}-prompt.md` | `prompt-merge.md` (reference + brand colors + content) |
| **9** | Generate images | `{slug}.png` | Image generation tool → upload to Drive |
| **9b** | Publish | `publish-log.md` + Firestore doc | `firestore-creative-publish` |
| **10** | Handoff | Summary for user | Pipeline SKILL |

Phases run **in order**. Skip only what the user says is already done.

---

## Data flow (what each phase reads)

```mermaid
flowchart LR
  subgraph intake [Phase 0 Intake]
    W[Website URL]
    BF[Optional brand files]
    G[Goals / platforms]
  end

  subgraph distill [Distilled once on Drive]
    BI[BRAND_IDENTITY.md]
    BD[BRAND_DNA.json]
  end

  subgraph plans [Planning on Drive]
    SC[social-media-context.md]
    ST[content-strategy.md]
    CAL[content-calendar.md]
  end

  subgraph refs [Reference layer on Drive]
    PIN[pin PNG]
    RP[pin-reference-prompt.md]
  end

  subgraph creative [Per post on Drive]
    CD[CREATIVE_DNA.json]
    CP[post / caption]
    PR[prompt.md merged]
    PNG[slug.png]
  end

  W --> BI
  BF --> BI
  BI --> SC
  BI --> BD
  PIN --> RP
  SC --> ST
  SC --> ST --> CAL
  CAL --> CD
  RP --> PR
  BD --> PR
  CD --> PR
  CP --> PR
  PR --> PNG
  PNG --> FS[Firestore via webhook outletId]
```

**Key idea:** Later phases do **not** re-open raw intake files. They read **artifacts on Google Drive** produced in earlier phases.

---

## Phase 0 — Intake (what you provide)

| Input | Required | Used for |
|-------|----------|----------|
| Website URL | Yes | Phase 1 — positioning, product, audience |
| Client slug | Optional | `gdrive/clients/{slug}/` path on Drive |
| **Brand files** | Optional | **Phase 1 only** — see below |
| Platforms | Yes | Calendar + copy format |
| Calendar horizon | Yes | Weekly / monthly plan |
| Reference creatives | No | Phase 1b fetches Pinterest by default |
| Goals | Optional | Phase 3 discovery if gaps |

### Optional brand files — are they considered?

**Yes, but only if Phase 1 merges them into `BRAND_IDENTITY.md` on Drive.**

| Intake file type | When it matters | Downstream use |
|------------------|-----------------|----------------|
| Decks, ICP docs, feature lists | Phase 1 merge | Voice, audience, pillars, proof → context, strategy, copy |
| Logos | Phase 1 + Phase 5/9 | Upload to `gdrive/clients/{slug}/assets/logo.png` |
| User-uploaded layout images | Phase 6 (optional) | Creative DNA layout — not voice/topics |
| Goals (text at intake) | Phase 3 if not in identity | Strategy ratios, CTAs |

| Phase | Reads raw brand files? |
|-------|------------------------|
| 1 | **Yes** — merges into `BRAND_IDENTITY.md` on Drive |
| 2–7 | **No** — reads Drive artifacts: identity, plans, `BRAND_DNA.json` |
| 8–9 | **No** — DNA + prompts from Drive only |

---

## What the pipeline does **not** use

| Not built in | Notes |
|--------------|-------|
| Repo `clients/` folder | Legacy examples only — **do not write** new runs there on `brand-gdrive` |
| Knowledge base / RAG | No Notion KB, vector store, or product wiki phase |
| Per-user CRM data | No leads, segments, or account history |
| Post analytics loop | No Meta/Clarity feedback into calendar |

**Swayam weekly automation** is a separate partial run with Exa/Reddit research — adapt paths to `gdrive/clients/swayam/` when running on this branch.

---

## Client folder layout (Google Drive)

```
gdrive/clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md
├── BRAND_DNA.json
├── references/pinterest/          # Phase 1b + 6a
│   ├── pin-01-*.{png,jpg}
│   └── pin-01-*-reference-prompt.md
├── plans/
│   ├── social-media-context.md    # Phase 2
│   ├── content-strategy.md        # Phase 3
│   └── content-calendar.md        # Phase 4
└── instagram/{YYYY-MM-DD}/
    ├── {slug}.CREATIVE_DNA.json
    ├── {slug}-post.md
    ├── {slug}-prompt.md
    ├── {slug}.png
    └── publish-log.md             # Phase 9b
```

See also [`references/file-structure.md`](../skills/brand-social-creative-pipeline/references/file-structure.md) and [`references/google-drive-storage.md`](../skills/brand-social-creative-pipeline/references/google-drive-storage.md).

---

## Colors and layout at image generation

**Three-layer merge (Phase 8):**

1. **Reference prompt** — pin layout, zones, typography placement (from Phase 6a)
2. **Brand DNA** — all render hex colors (`{{COLOR_ROLE}}` → brand tokens)
3. **Creative DNA `elements[]`** — latest on-image copy for this post

Details: [`references/prompt-merge.md`](../skills/brand-social-creative-pipeline/references/prompt-merge.md).

---

## Phase 9b — Publish (webhook)

After each `{slug}.png` on Drive:

1. Download PNG from Drive → base64 → upload to GCS (`image-function`)
2. Parse post → `caption`, `hashtags`; load `{slug}-caption-scores.json` from Drive
3. `POST /ai-content` → `OUTLET/{outletId}/social-ai-poster`
4. Write `publish-log.md` on Drive

**Prerequisite:** Phase 7b caption scores must exist before publish.

**`outletId` comes from the triggering webhook** — not stored in `client.json`.

---

## Partial runs

| Request | Start at |
|---------|----------|
| Brand only | Phase 1 → 1b → 5 |
| Pinterest refs only | Phase 1b |
| Calendar + creatives | Phase 4 (needs 1–1b, 3, 5–6) |
| New creative from reference | Phase 6 → 9 |
| Copy only | Phase 7 |
| Publish existing PNG | Phase 9b (needs webhook `outletId`) |

---

## Related docs

| Doc | Purpose |
|-----|---------|
| [`skills/brand-social-creative-pipeline/SKILL.md`](../skills/brand-social-creative-pipeline/SKILL.md) | Agent runbook (full phase instructions) |
| [`references/google-drive-storage.md`](../skills/brand-social-creative-pipeline/references/google-drive-storage.md) | Drive root, MCP ops, path notation |
| [`skills/README.md`](../skills/README.md) | Skill index |
