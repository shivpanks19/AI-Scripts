# Client File Structure (Google Drive)

**Branch:** `brand-gdrive`  
**Storage:** [google-drive-storage.md](./google-drive-storage.md)

Canonical layout on Google Drive (Swayam reference: `gdrive/clients/swayam/`).

**Every pipeline invocation creates a new `{run_date}` folder on Drive** — never overwrite prior runs.

```
gdrive/clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md              # regenerated each run (Phase 1)
├── BRAND_DNA_SCHEMA.json
├── BRAND_DNA.json                 # regenerated each run (Phase 5)
├── CREATIVE_DNA_SCHEMA.json
├── assets/
│   └── logo.png                   # optional — user-supplied logo
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
│   ├── content-strategy.md
│   └── content-calendar.md
│
├── instagram/{calendar_week}/     # Phase 6–9b — calendar week folder
│   ├── {slug}.CREATIVE_DNA.json
│   ├── {slug}-prompt.md           # Phase 8 — merged reference + brand + content
│   ├── {slug}-post.md
│   ├── {slug}-caption-scores.json
│   ├── {slug}.png
│   └── publish-log.md
│
├── facebook/{calendar_week}/
│   ├── {slug}-post.md
│   └── {slug}.png
│
├── linkedin/{calendar_week}/
│   ├── {slug}-post.md
│   └── {slug}.png
│
└── runs/{run_date}/
    ├── PIPELINE-PROGRESS.json        # Phase 0 — checkpoint (update each phase)
    └── PIPELINE-HANDOFF.md        # Phase 10 — one handoff per run
```

## Run date resolution

| Variable | Value |
|----------|-------|
| `run_date` | UTC date when the agent is invoked (`YYYY-MM-DD`) |
| `calendar_week` | First post date in calendar (webhook `calendar_start_date`, else next Monday) |
| Creative folders | `instagram/{calendar_week}/` — not `run_date` |

Prior runs remain on Drive under their own folders.

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

Every generated visual should have **linked files on Drive** (+ publish record after Phase 9b):

1. `{pin}-reference-prompt.md` — layout regeneration spec (Phase 6a)
2. `{slug}.CREATIVE_DNA.json` — content + pointer to reference prompt
3. `{slug}-prompt.md` — merged generation spec (Phase 8)
4. `{slug}-post.md` — caption body
5. `{slug}-caption-scores.json` — scored copy (Phase 7b)
6. `{slug}.png` — asset
7. `publish-log.md` — Firestore record

`_meta` in Creative DNA must point to `reference_asset`, `reference_prompt_ref`, and `prompt_ref` (Drive-relative paths).

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

After each `{slug}.png` is generated on Drive, run [firestore-creative-publish/SKILL.md](./firestore-creative-publish/SKILL.md). Download PNG via Drive MCP for base64 GCS upload.

Phase 7b ([caption-score/SKILL.md](./caption-score/SKILL.md)) must complete before Phase 9b.

## Schema copies

On first client setup, copy from **repo templates** to Drive via MCP:

```
skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json
  → gdrive/clients/{slug}/BRAND_DNA_SCHEMA.json

skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json
  → gdrive/clients/{slug}/CREATIVE_DNA_SCHEMA.json
```

Use [templates/client.json.template](../templates/client.json.template) for initial `client.json` on Drive.
