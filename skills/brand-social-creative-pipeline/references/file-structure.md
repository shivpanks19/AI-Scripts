# Client File Structure

Canonical layout (Swayam reference: `docs/swayam/`).

```
clients/{client_slug}/
├── client.json
├── BRAND_IDENTITY.md
├── BRAND_DNA_SCHEMA.json
├── BRAND_DNA.json
├── CREATIVE_DNA_SCHEMA.json
├── FEATURES.md                    # optional product doc
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
│       ├── {slug}-caption.md
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
| Caption | `{slug}-caption.md` |

## client.json minimum

```json
{
  "client_slug": "swayam",
  "display_name": "Swayam",
  "website": "https://swayamapp.com/",
  "deliverables_root": "clients/swayam",
  "folders": {
    "instagram": "docs/swayam/instagram",
    "linkedin": "docs/swayam/linkedin",
    "plans": "docs/swayam/plans"
  },
  "channels": {
    "primary": ["instagram", "linkedin"]
  }
}
```

## DNA file pairing

Every generated visual should have **three linked files**:

1. `{slug}.CREATIVE_DNA.json` — structure
2. `{slug}-prompt.md` — generation spec
3. `{slug}.png` — asset

`_meta` in Creative DNA must point to `reference_asset` and `prompt_ref` with relative paths.

## Schema copies

On new client setup, copy from skill templates:

```bash
cp skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json clients/{slug}/
cp skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json clients/{slug}/
```
