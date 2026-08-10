# Client File Structure

Canonical layout for any brand under `clients/{client_slug}/`. Worked examples: `clients/swayam/`, `clients/eduhexa/`.

**Every pipeline invocation creates a new `{run_date}` folder** — never overwrite prior runs.

```
clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md              # regenerated each run (Phase 1)
├── BRAND_DNA_SCHEMA.json
├── BRAND_DNA.json                 # regenerated each run (Phase 5)
├── CREATIVE_DNA_SCHEMA.json
│
├── references/
│   └── pinterest/{run_date}/      # Phase 1b + 6a
│       ├── README.md
│       ├── search-brief.json
│       ├── pinterest-manifest.json
│       ├── pin-01-{layout}.png … pin-05-{layout}.png
│       └── pin-01-{layout}-reference-prompt.md … pin-05-*   # Phase 6a
│
├── plans/{run_date}/              # Phase 2–4 — new folder per run
│   ├── social-media-context.md
│   ├── trend-research-brief.md        # Phase 2a
│   ├── trend-research-brief.json      # Phase 2a — input to strategy + calendar
│   ├── content-strategy.md
│   ├── pre-calendar-setup-brief.json   # Phase 3b — dedup + selected slots
│   └── content-calendar.md          # Phase 4 — from brief only
│
├── instagram/{run_date}/     # Phase 6–9b — same run_date as plans
│   ├── {slug}.CREATIVE_DNA.json
│   ├── {slug}-prompt.md           # Phase 8 — merged reference + brand + content
│   ├── {slug}-background.png      # Phase 9 — AI visual (when logo composition enabled)
│   ├── {slug}.layout.json         # Phase 9a — normalized layout + resolved pixels
│   ├── {slug}-debug.png           # Phase 9a — optional debug overlay
│   ├── {slug}-post.md
│   ├── {slug}-caption-scores.json
│   ├── {slug}.png
│   └── publish-log.md
│
├── facebook/{run_date}/
│   ├── {slug}-post.md
│   └── {slug}.png
│
├── linkedin/{run_date}/
│   ├── {slug}-post.md
│   └── {slug}.png
│
└── runs/{run_date}/
    └── PIPELINE-HANDOFF.md        # Phase 10 — one handoff per run
```

## Run date resolution

| Variable | Value |
|----------|-------|
| `run_date` | UTC date when the agent is invoked (`YYYY-MM-DD`) — **only** folder key for plans, references, creatives, and runs |
| `posts_count` | Number of creatives this run (`run.posts_per_week` or `run.posts_count`; default **3**) |
| Creative folders | `instagram/{run_date}/`, `facebook/{run_date}/` — same `run_date` as `plans/{run_date}/` |

**Deprecated:** `calendar_week`, `calendar_start_date` — do not use for folder names or slot assignment.

Prior runs remain on disk under their own folders.

## Naming rules

**Format policy:** [single-image-post-policy.md](./single-image-post-policy.md) — all feed creatives are single dark editorial images.

| Artifact | Pattern |
|----------|---------|
| Creative slug | `{topic-kebab}-editorial` only |
| Reference prompt (per pin) | `pin-0N-{layout}-reference-prompt.md` |
| Creative DNA | `{slug}.CREATIVE_DNA.json` |
| Final prompt | `{slug}-prompt.md` (merged) |
| Image | `{slug}.png` |
| Post (IG, FB, LinkedIn) | `{slug}-post.md` |
| Caption scores | `{slug}-caption-scores.json` |

## DNA file pairing

Every generated visual should have **linked files** (+ publish record after Phase 9b):

1. `{pin}-reference-prompt.md` — layout regeneration spec (Phase 6a)
2. `{slug}.CREATIVE_DNA.json` — content + pointer to reference prompt
3. `{slug}-prompt.md` — merged generation spec (Phase 8)
4. `{slug}-post.md` — caption body
5. `{slug}-caption-scores.json` — scored copy (Phase 7b)
6. `{slug}.png` — asset
7. `publish-log.md` — Firestore record

`_meta` in Creative DNA must point to `reference_asset`, `reference_prompt_ref`, and `prompt_ref`.

## Three-layer prompt merge

Phase 8 merges:

1. **Reference prompt** — pin layout fidelity
2. **Brand DNA** — color theme only
3. **Creative DNA `elements[]`** — latest on-image copy

See [prompt-merge.md](./prompt-merge.md).

## Pinterest references (Phase 1b + 6a)

- Phase 1b: fetch pins → [pinterest-reference-fetch/SKILL.md](./pinterest-reference-fetch/SKILL.md)
- Phase 6a: reverse-engineer each pin → [reference-creative-prompt/SKILL.md](./reference-creative-prompt/SKILL.md)

## Firestore publish (Phase 9b)

After each `{slug}.png` is generated, run [firestore-creative-publish/SKILL.md](./firestore-creative-publish/SKILL.md).

Phase 7b ([caption-score/SKILL.md](./caption-score/SKILL.md)) must complete before Phase 9b.

## Pre-calendar setup (Phase 3b)

Before `content-calendar.md`, run [pre-calendar-setup/SKILL.md](./pre-calendar-setup/SKILL.md) then [content-calendar-sms](../../../content-calendar-sms/SKILL.md) (pipeline mode):

- Pre-calendar-setup scans prior calendars and writes `pre-calendar-setup-brief.json`
- content-calendar-sms renders `content-calendar.md` from `selected_slots[]` exactly

## Schema copies

On first client setup:

```bash
cp skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json clients/{slug}/
cp skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json clients/{slug}/
```
