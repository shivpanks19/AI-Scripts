# Client File Structure

Canonical layout (Swayam reference: `clients/swayam/`).

```
clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md
├── BRAND_DNA_SCHEMA.json
├── BRAND_DNA.json
├── CREATIVE_DNA_SCHEMA.json
├── FEATURES.md                    # optional product doc
│
├── references/
│   └── pinterest/               # Phase 1b — 5 pin PNGs + manifest
│       ├── README.md
│       ├── search-brief.json
│       ├── pinterest-manifest.json
│       └── pin-01-{layout}.png … pin-05-{layout}.png
│
├── plans/
│   ├── social-media-context.md
│   ├── content-strategy.md
│   └── content-calendar.md
│
├── instagram/
│   └── {YYYY-MM-DD}/
│       ├── {slug}.CREATIVE_DNA.json
│       ├── {slug}-prompt.md
│       ├── {slug}-post.md         # Phase 7 — post-writer-sms
│       ├── {slug}-caption-scores.json  # Phase 7b — caption-score
│       ├── {slug}.png
│       └── publish-log.md           # Phase 9b — Firestore + GCS per slug
│
├── facebook/
│   └── {YYYY-MM-DD}/
│       ├── {slug}-post.md         # Phase 7 — post-writer-sms (mirror or adapt IG)
│       └── {slug}.png
│
├── linkedin/
│   └── {YYYY-MM-DD}/
│       ├── {slug}-post.md
│       └── {slug}.png             # if visual post
│
└── carousel/
    └── {YYYY-MM-DD}/
        ├── slide-prompts.json
        └── assets/
```

## Naming rules

| Artifact | Pattern |
|----------|---------|
| Creative slug | `{topic-kebab}-hero` or `{date}-{topic}-hero` |
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
  "folders": {
    "instagram": "clients/swayam/instagram",
    "linkedin": "clients/swayam/linkedin",
    "plans": "clients/swayam/plans",
    "references_pinterest": "clients/swayam/references/pinterest"
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

Fetched automatically after `BRAND_IDENTITY.md` via [pinterest-reference-fetch/SKILL.md](./pinterest-reference-fetch/SKILL.md). Phase 6 reverse-engineers each `pin-*.png` into `{slug}.CREATIVE_DNA.json`.

## Firestore publish (Phase 9b)

After each `{slug}.png` is generated, run [firestore-creative-publish/SKILL.md](./firestore-creative-publish/SKILL.md) — upload to GCS + `POST /ai-content` → `OUTLET/{outletId}/social-ai-poster` (includes `caption`, `captionScore`, `captionScores`).

Phase 7b ([caption-score/SKILL.md](./caption-score/SKILL.md)) must complete before Phase 9b.

## Schema copies

On new client setup, copy from skill templates:

```bash
cp skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json clients/{slug}/
cp skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json clients/{slug}/
```
