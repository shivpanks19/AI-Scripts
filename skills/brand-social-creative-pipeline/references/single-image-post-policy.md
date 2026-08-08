# Single-Image Post Policy (mandatory)

**Applies to:** Phase 3 (content strategy), Phase 4 (content calendar), Phase 1b (Pinterest), Phase 6 (Creative DNA), Phase 8–9 (prompt + image).

All social feed visuals in this pipeline are **one PNG per post** — dark editorial hero cards. No carousels, no stat/KPI cards, no multi-slide formats.

---

## Allowed format (only)

| Field | Value |
|-------|-------|
| **Post type** | Single image feed post |
| **Canvas** | 1:1 (1080×1080) |
| **Structure** | `dark-bold-editorial` or `contrarian-editorial-hero` or `editorial-quote-hero` |
| **Background mode** | `dark` only (`brand.visual_identity.primary_dark`) |
| **Layout** | Center-stack or split editorial — headline + subheadline + optional abstract hero + footer URL |
| **Slug suffix** | `-editorial` (e.g. `not-agency-system-editorial`) |

**Reference quality bar:** `not-agency-system-editorial` — contrarian headline on dark canvas, rich but single-frame composition, brand tagline as on-image copy.

---

## Forbidden formats (do not schedule or generate)

| Format | Examples | Why excluded |
|--------|----------|--------------|
| Stat / KPI hero | `*-stat`, `stat-hero-card`, metric cards | Reads as generic SaaS template |
| Carousel | `*-carousel`, slide 1 of N, `Swipe →` | Multi-slide; only single image supported |
| Light template covers | numbered hooks on white bg | Off-brand vs dark editorial |
| Dashboard split / phone mockup | product UI hero slots | Use editorial abstract hero instead |
| KPI grids / gradient card grids | multi-metric layouts | Stat-adjacent; excluded |

---

## Phase 3 — Content strategy rules

When writing `content-strategy.md`:

1. Under **Content formats**, list only: `single-image editorial feed post (1:1, dark)`.
2. Under **Weekly content mix**, every slot must be `single-image editorial` — no carousel, stat, or mixed-format rows.
3. Do not allocate pillar share to carousel or stat formats.
4. **Posts per week:** 3 (weekly) or 12 (monthly) — each slot = one editorial image.

---

## Phase 4 — Content calendar rules

When writing `content-calendar.md`:

1. **Format column** must be exactly: `single-image editorial 1:1` (or `dark editorial 1:1`).
2. **Never** use: `stat-hero`, `carousel`, `carousel cover`, `kpi-grid`, `phone-mockup`, `dashboard-split`.
3. Each row = one slug = one PNG = one Firestore publish — no slide references.
4. On-image copy: headline + subheadline + footer URL only (2–3 lines max). No fake stats on image.
5. `creative_template_ref` must end with `-editorial`.

### Calendar row example

| Date | Platform | Pillar | Topic | Format | `creative_template_ref` |
|------|----------|--------|-------|--------|-------------------------|
| 2026-08-11 | instagram | positioning | Not an agency — growth system | single-image editorial 1:1 | `not-agency-system-editorial` |

---

## Phase 1b — Pinterest selection

When fetching 5 reference pins:

1. **Prefer** `dark-bold-editorial` and `contrarian-editorial` layouts only.
2. **Skip** stat-hero, carousel-cover, kpi-grid, dashboard-split, phone-mockup archetypes.
3. Search queries should include: `dark editorial social media post`, `bold typography agency instagram`, `contrarian brand post design` — not `carousel` or `stat`.
4. All 5 pins should be usable as single-frame editorial inspiration.

---

## Phase 6 — Creative DNA rules

- `structure_type` must be one of: `contrarian-editorial-hero`, `editorial-quote-hero`, `dark-bold-editorial`.
- `visual_identity.background_mode` must be `dark`.
- `canvas.ratio` must be `1:1`.
- No `slide_indicator`, no `stat` element type, no carousel CTA bands.

---

## Phase 8–9 — Prompt and image generation

- Prompts must describe a **single full-bleed editorial frame** — not a card on colored bg, not a carousel cover.
- Do not include: `1 / 4`, `Swipe →`, percentage stats, KPI numbers unless sourced from brief.
- Image generator: one `GenerateImage` call per calendar row → one `{slug}.png`.
