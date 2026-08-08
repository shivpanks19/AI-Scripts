# Pinterest SaaS Design References → Creative DNA

Reverse-engineered layout archetypes from Pinterest SaaS / B2B social media design trends, encoded as `{slug}.CREATIVE_DNA.json` files that follow [CREATIVE_DNA_SCHEMA.json](../../CREATIVE_DNA_SCHEMA.json).

**Merge at render time:** `BRAND_DNA.json` + `{slug}.CREATIVE_DNA.json` (brand wins on colors, logo, voice).

## Pinterest inspiration sources

| Archetype | Pinterest / design reference | File |
|-----------|------------------------------|------|
| Dashboard split hero | [SaaS Social Media Design](https://www.pinterest.com/ideas/saas-social-media-design/909970389329/) · split copy + product UI | `dashboard-split-hero.CREATIVE_DNA.json` |
| Stat overlay on dashboard | [LinkedIn Social Media Design](https://www.pinterest.com/ideas/linkedin-social-media-design/956025573749/) · metric cards over UI mockup | `stat-overlay-dashboard.CREATIVE_DNA.json` |
| Dark bold editorial | [LinkedIn Carousel Design](https://www.pinterest.com/ideas/linkedin-carousel-design/916788887085/) · black/bold thought-leadership slides | `dark-bold-editorial.CREATIVE_DNA.json` |
| Gradient KPI card grid | Analytics dashboard pins (purple gradient KPI cards) | `gradient-kpi-card-grid.CREATIVE_DNA.json` |
| Phone mockup feature | [Social media mockup pins](https://www.pinterest.com/search/pins/?q=saas%20social%20media%20post%20design) · device frame + app UI | `phone-mockup-feature.CREATIVE_DNA.json` |

## Usage

1. Pick a `structure_type` that matches the weekly insight (stat-led → `stat-overlay-dashboard` or `gradient-kpi-card-grid`; opinion → `dark-bold-editorial`; product proof → `dashboard-split-hero` or `phone-mockup-feature`).
2. Copy the matching `.CREATIVE_DNA.json` to your run folder (e.g. `weekly/{YYYY-MM-DD}/` or `instagram/{YYYY-MM-DD}/`).
3. Update `variable_slots` only — keep `must_preserve` zones intact.
4. Merge with `BRAND_DNA.json` per `CREATIVE_DNA_SCHEMA.json` merge rules before image generation.

**Colors:** All hex values resolve from `BRAND_DNA.json` at merge time. Creative DNA `visual_identity` hex fields (if present) document the Pinterest reference only — use `background_mode` (`light` | `dark` | `primary`) for layout tone. See `skills/brand-social-creative-pipeline/references/prompt-merge.md`.
