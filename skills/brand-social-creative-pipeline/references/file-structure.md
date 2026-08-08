# Client File Structure

Canonical layout (Swayam reference: `clients/swayam/`).

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
│   └── pinterest/{run_date}/      # Phase 1b — new folder per run
│       ├── README.md
│       ├── search-brief.json
│       ├── pinterest-manifest.json
│       └── pin-01-{layout}.png … pin-05-{layout}.png
│
├── plans/{run_date}/              # Phase 2–4 — new folder per run
│   ├── social-media-context.md
│   ├── content-strategy.md
│   └── content-calendar.md
│
<<<<<<< HEAD
├── instagram/
│   └── {YYYY-MM-DD}/
│       ├── {slug}.CREATIVE_DNA.json
│       ├── {slug}-prompt.md
│       ├── {slug}-post.md         # Phase 7 — post-writer-sms
│       ├── {slug}-caption-scores.json  # Phase 7b — caption-score
│       ├── {slug}.png
│       └── publish-log.md           # Phase 9b — Firestore + GCS per slug
=======
├── instagram/{run_date}/            # Phase 6–9b — new folder per run
│   ├── {slug}.CREATIVE_DNA.json
│   ├── {slug}-prompt.md
│   ├── {slug}-post.md
│   ├── {slug}.png
│   └── publish-log.md
>>>>>>> aa92519 (Require full pipeline re-run with dated folders on every invocation)
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
| `run_date` | UTC date when the agent is invoked (`YYYY-MM-DD`) |
| Post dates in calendar | From webhook `calendar_start_date`, else next Monday from `run_date` |

Prior runs remain on disk under their own `{run_date}` folders (e.g. `instagram/2026-08-11/` and `instagram/2026-08-08/`).

## Naming rules

| Artifact | Pattern |
|----------|---------|
| Creative slug | `{topic-kebab}-hero` or `{topic-kebab}-editorial` |
| Creative DNA | `{slug}.CREATIVE_DNA.json` |
| Prompt | `{slug}-prompt.md` |
| Image | `{slug}.png` |
| Post (IG, FB, LinkedIn) | `{slug}-post.md` via `post-writer-sms` |
| Caption scores | `{slug}-caption-scores.json` via `caption-score` (Phase 7b) |
| Caption (TikTok, Pinterest, YouTube) | `{slug}-caption.md` via `caption-writer-sms` |

## client.json minimum

```json
{
  "client_slug": "swayam",
  "display_name": "Swayam",
  "website": "https://swayamapp.com/",
  "deliverables_root": "clients/swayam",
  "pipeline": {
    "run_date": "2026-08-08",
    "calendar_week": "2026-08-11",
    "last_run": "2026-08-08T19:54:00Z"
  },
  "folders": {
    "instagram": "clients/swayam/instagram/2026-08-08",
    "facebook": "clients/swayam/facebook/2026-08-08",
    "plans": "clients/swayam/plans/2026-08-08",
    "references_pinterest": "clients/swayam/references/pinterest/2026-08-08"
  },
  "channels": {
    "primary": ["instagram", "linkedin"]
  }
}
```

## DNA file pairing

Every generated visual should have **four linked files** (+ publish record after Phase 9b):

1. `{slug}.CREATIVE_DNA.json` — structure
2. `{slug}-prompt.md` — generation spec
3. `{slug}-post.md` or `{slug}-caption.md` — copy
4. `{slug}-caption-scores.json` — scored copy (Phase 7b)
5. `{slug}.png` — asset
6. `publish-log.md` — Firestore `documentId` + GCS `imageUrl` (append per slug)

`_meta` in Creative DNA must point to `reference_asset` and `prompt_ref` with relative paths.

## Pinterest references (Phase 1b)

Fetched into `references/pinterest/{run_date}/` after each `BRAND_IDENTITY.md` rewrite via [pinterest-reference-fetch/SKILL.md](./pinterest-reference-fetch/SKILL.md).

## Firestore publish (Phase 9b)

After each `{slug}.png` is generated, run [firestore-creative-publish/SKILL.md](./firestore-creative-publish/SKILL.md) — upload to GCS + `POST /ai-content` → `OUTLET/{outletId}/social-ai-poster` (includes `caption`, `captionScore`, `captionScores`).

Phase 7b ([caption-score/SKILL.md](./caption-score/SKILL.md)) must complete before Phase 9b.

## Schema copies

On first client setup, copy from skill templates:

```bash
cp skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json clients/{slug}/
cp skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json clients/{slug}/
```

Schemas at client root are reused; all run-scoped deliverables go under `{run_date}` folders.
