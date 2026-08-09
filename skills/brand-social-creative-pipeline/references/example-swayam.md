# Pipeline Example — Swayam

**Branch:** `brand-gdrive`  
**Reference client on Google Drive:** `gdrive/clients/swayam/`

## Intake

- Website: swayamapp.com
- Slug: `swayam`
- Platforms: Instagram, LinkedIn
- Calendar: weekly
- Reference creatives: editorial-search-hero, stat-hero admissions

## Phase outputs (on Google Drive)

| Phase | File |
|-------|------|
| 1 | `gdrive/clients/swayam/BRAND_IDENTITY.md` |
| 1b | `gdrive/clients/swayam/references/pinterest/{run_date}/pinterest-manifest.json` + 5 `pin-*.png` |
| 2 | `gdrive/clients/swayam/plans/{run_date}/social-media-context.md` |
| 3 | `gdrive/clients/swayam/plans/{run_date}/content-strategy.md` |
| 4 | `gdrive/clients/swayam/plans/{run_date}/content-calendar.md` |
| 5 | `gdrive/clients/swayam/BRAND_DNA.json` |
| 6 | `gdrive/clients/swayam/instagram/2026-08-08/admissions-automation-stat-hero.CREATIVE_DNA.json` |
| 7 | `gdrive/clients/swayam/instagram/2026-08-08/admissions-automation-stat-hero-post.md` (post-writer-sms) |
| 8 | `gdrive/clients/swayam/instagram/2026-08-08/admissions-automation-stat-hero-prompt.md` |
| 9 | `gdrive/clients/swayam/instagram/2026-08-08/admissions-automation-stat-hero.png` |

## Calendar row → creative mapping

```markdown
| Date | Platform | Topic | creative_template_ref | variable_slots |
|------|----------|-------|----------------------|----------------|
| 2026-08-08 | instagram | AI automation for admissions | admissions-automation-stat-hero | headline, stat, hero casting |
| 2026-08-11 | instagram | Revenue loop hub | revenue-loop-hub-hero | headline, sublines |
```

## Variant from template

User: "Same layout as admissions stat hero but for WhatsApp pipeline"

1. Copy `admissions-automation-stat-hero.CREATIVE_DNA.json` on Drive
2. Change `variable_slots` only: topic, headline, stat, hero_card content
3. Keep `must_preserve`: oversized stat, human+phone, zone map
4. Generate new prompt + image → upload to Drive
