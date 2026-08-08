# Pipeline Example — Swayam

Reference client: `clients/swayam/`

## Intake

- Website: swayamapp.com
- Slug: `swayam`
- Platforms: Instagram, LinkedIn
- Calendar: weekly
- Reference creatives: editorial-search-hero, stat-hero admissions

## Phase outputs

| Phase | File |
|-------|------|
| 1 | `BRAND_IDENTITY.md` |
| 1b | `references/pinterest/pinterest-manifest.json` + 5 `pin-*.png` |
| 2 | `plans/social-media-context.md` |
| 3 | `plans/content-strategy.md` |
| 4 | `plans/content-calendar.md` |
| 5 | `BRAND_DNA.json` |
| 6 | `instagram/2026-08-08/admissions-automation-stat-hero.CREATIVE_DNA.json` |
| 7 | `instagram/2026-08-08/admissions-automation-stat-hero-post.md` (post-writer-sms) |
| 8 | `instagram/2026-08-08/admissions-automation-stat-hero-prompt.md` |
| 9 | `instagram/2026-08-08/admissions-automation-stat-hero.png` |

## Calendar row → creative mapping

```markdown
| Date | Platform | Topic | creative_template_ref | variable_slots |
|------|----------|-------|----------------------|----------------|
| 2026-08-08 | instagram | AI automation for admissions | admissions-automation-stat-hero | headline, stat, hero casting |
| 2026-08-11 | instagram | Revenue loop hub | revenue-loop-hub-hero | headline, sublines |
```

## Variant from template

User: "Same layout as admissions stat hero but for WhatsApp pipeline"

1. Copy `admissions-automation-stat-hero.CREATIVE_DNA.json`
2. Change `variable_slots` only: topic, headline, stat, hero_card content
3. Keep `must_preserve`: oversized stat, human+phone, zone map
4. Generate new prompt + image
