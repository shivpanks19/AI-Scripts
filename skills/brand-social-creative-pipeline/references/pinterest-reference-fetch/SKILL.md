---
name: pinterest-reference-fetch
description: >-
  Fetch 5 Pinterest social-design reference pins after BRAND_IDENTITY.md exists.
  Derives search keywords from brand identity (product category, industry, audience),
  searches Pinterest, downloads pin images to gdrive/clients/{slug}/references/pinterest/{run_date}/,
  and writes a manifest for Phase 6 Creative DNA. Use when bootstrapping a new client
  in brand-social-creative-pipeline or when the user asks for Pinterest layout references.
---

# Pinterest Reference Fetch

Runs **immediately after Phase 1** (`BRAND_IDENTITY.md` exists). **Do not run before brand identity.** Do not use generic SaaS queries unless the brand identity is SaaS.

**Pipeline position:** Phase 1b — after `design-brand-guardian`, before Phase 2 (social context).

**Downstream:** Phase 6 reads `gdrive/clients/{client_slug}/references/pinterest/{run_date}/pinterest-manifest.json` and each `pin-*.png` to author `{slug}.CREATIVE_DNA.json`.

**Storage:** Upload all outputs to Google Drive via MCP. See [google-drive-storage.md](../google-drive-storage.md).

**Format policy:** [single-image-post-policy.md](../single-image-post-policy.md) — select pins with **dark editorial / contrarian headline** layouts only. Skip stat-hero, carousel-cover, kpi-grid, dashboard-split, phone-mockup.

**Run policy:** Always fetch into a **new** `{run_date}` folder. Never reuse pins from prior runs.

---

## Inputs

| Input | Path | Required |
|-------|------|----------|
| Brand identity | `gdrive/clients/{client_slug}/BRAND_IDENTITY.md` | Yes |
| Client slug | `gdrive/clients/{client_slug}/client.json` → `client_slug` | Yes |
| Run date | `client.json` → `pipeline.run_date` | Yes |

---

## Outputs

```
gdrive/clients/{client_slug}/references/pinterest/{run_date}/
├── README.md                 # human summary + how pins were chosen
├── search-brief.json         # keywords derived from BRAND_IDENTITY
├── pinterest-manifest.json   # machine-readable index (Phase 6 input)
├── pin-01-{layout-slug}.png
├── pin-02-{layout-slug}.png
├── pin-03-{layout-slug}.png
├── pin-04-{layout-slug}.png
└── pin-05-{layout-slug}.png
```

Update `client.json`:

```json
"folders": {
  "references_pinterest": "gdrive/clients/{client_slug}/references/pinterest/{run_date}"
}
```

---

## Procedure

### Step 1 — Extract brand signals from BRAND_IDENTITY.md

Read the full file. Extract **only what is stated** — do not invent categories.

| Signal | Where to look | Examples |
|--------|---------------|----------|
| `product_category` | Positioning, product name, pillars | CRM, CSR, EdTech platform, coaching, fintech |
| `industry` | Industry/niche, market | B2B SaaS, education, nonprofit, healthcare |
| `audience` | ICP, personas | founders, admissions heads, CSR leads |
| `visual_tone` | Imagery guidelines, personality | editorial, dashboard/UI, lifestyle, minimal |
| `platforms` | GTM, social (default LinkedIn + Instagram) | linkedin, instagram |

Write `search-brief.json`:

```json
{
  "_meta": {
    "source": "./BRAND_IDENTITY.md",
    "client_slug": "{slug}",
    "created": "YYYY-MM-DD"
  },
  "brand_signals": {
    "product_category": "CRM",
    "industry": "B2B SaaS",
    "audience": "revenue leaders, admissions directors",
    "visual_tone": "editorial dashboard, operator-grade",
    "platforms": ["linkedin", "instagram"]
  },
  "search_queries": []
}
```

### Step 2 — Build Pinterest search queries (3–5 queries, 5 pins total)

Compose queries from **brand signals**. Pattern:

```
{industry} {product_category} social media post design
{product_category} {platform} carousel design B2B
{product_category} instagram post template {audience hook word}
```

**Category → keyword recipes** (adapt; never copy blindly if BRAND_IDENTITY contradicts):

| Brand identity says… | Pinterest domain | Example search queries |
|----------------------|----------------|------------------------|
| CRM, pipeline, revenue ops, agentic CRM | SaaS / B2B software | `saas crm social media post design`, `B2B CRM linkedin carousel`, `sales pipeline instagram post design`, `dashboard SaaS social media creative` |
| CSR, sustainability, ESG, impact | CSR / purpose marketing | `corporate social responsibility social media design`, `CSR campaign instagram post`, `sustainability report social creative`, `ESG linkedin carousel` |
| EdTech, coaching, admissions, learning | Education marketing | `edtech social media post design`, `coaching institute instagram creative`, `admissions marketing linkedin post`, `education SaaS social media` |
| Fintech, payments, banking | Fintech B2B/B2C | `fintech social media post design`, `B2B fintech linkedin carousel`, `neobank instagram post template` |
| Healthcare, clinic, wellness | Health brand social | `healthcare social media post design`, `medical clinic instagram creative`, `wellness brand linkedin post` |
| D2C ecommerce, retail | D2C / retail social | `ecommerce instagram post design`, `D2C brand social media template`, `product launch instagram creative` |
| Agency, consulting, services | Professional services | `consulting firm linkedin carousel`, `B2B agency social media post design`, `thought leadership instagram post` |

**Rules:**

- Always include **product_category** + **format** words: `social media post design`, `carousel`, `linkedin post`, `instagram creative`.
- Run **3–5 distinct queries**; pick **5 pins total** across results (not 5 per query).
- Prefer pins with **readable layout** (typography, stat blocks, UI mockups) — not lifestyle stock with tiny text.
- Maximize **layout diversity** across the 5 picks (see Step 4).

Add final queries to `search-brief.json` → `search_queries[]`.

### Step 3 — Search Pinterest and collect pin candidates

For each query:

1. **WebSearch:** `site:pinterest.com {query}` or `pinterest {query} social media design`
2. **WebFetch** (if allowed): `https://www.pinterest.com/search/pins/?q={url_encoded_query}`
3. From results, collect candidate **pin page URLs** (`pinterest.com/pin/...`) and **image URLs** (`i.pinimg.com/...` — prefer `736x` or original).

Keep 8–12 candidates before filtering to 5.

**If Pinterest blocks fetch:** use WebSearch snippets and image URLs from search results; document limitation in `README.md`.

### Step 4 — Select exactly 5 pins (editorial diversity only)

**Mandatory:** All 5 pins must be single-frame **dark editorial** layouts per [single-image-post-policy.md](../single-image-post-policy.md). Do not select stat, carousel, dashboard, or phone-mockup pins.

Choose variation across these allowed archetypes only:

| Priority | Archetype | `inferred_layout` slug |
|----------|-----------|-------------------------|
| 1 | Dark bold editorial / quote hero | `dark-bold-editorial` |
| 2 | Contrarian / provocative headline stack | `contrarian-editorial` |
| 3 | Center-stack editorial with abstract hero | `editorial-quote-hero` |
| 4 | Split editorial (copy + abstract visual, no UI mockup) | `editorial-split-hero` |
| 5 | Gradient dark editorial card (single frame, not carousel) | `dark-editorial-card` |

Skip duplicates (same layout twice). **Reject** pins that are carousel covers, stat/KPI cards, or multi-slide templates even if visually strong.

### Step 5 — Download images and upload to Google Drive

1. Download each pin image to a temp path (curl or browser fetch).
2. Upload to `gdrive/clients/{client_slug}/references/pinterest/{run_date}/pin-01-{layout-slug}.png` via Google Drive MCP.

Naming: `pin-{01-05}-{layout-slug}.png` (layout slug from Step 4).

Verify each file is a valid image (non-empty, >10KB). If download fails, pick next candidate from same query.

### Step 6 — Write pinterest-manifest.json

```json
{
  "_meta": {
    "type": "pinterest_reference_manifest",
    "version": "1.0",
    "client_slug": "{slug}",
    "source": "../BRAND_IDENTITY.md",
    "search_brief": "./search-brief.json",
    "fetched": "YYYY-MM-DD",
    "pin_count": 5
  },
  "brand_signals": { },
  "searches_run": [
    {
      "query": "saas crm social media post design",
      "pinterest_search_url": "https://www.pinterest.com/search/pins/?q=...",
      "candidates_reviewed": 4
    }
  ],
  "pins": [
    {
      "id": "pin-01",
      "file": "./pin-01-dashboard-split-hero.png",
      "source_pin_url": "https://www.pinterest.com/pin/...",
      "image_source_url": "https://i.pinimg.com/...",
      "search_query": "saas crm social media post design",
      "inferred_layout": "dashboard-split-hero",
      "layout_notes": "Left headline + right dashboard mockup; stat row below",
      "suggested_structure_type": "split-dashboard-hero",
      "phase_6_status": "pending"
    }
  ],
  "selection_rationale": "One sentence: why these 5 match the brand category and layout diversity goal."
}
```

Set each pin `phase_6_status` to `pending` until Creative DNA is authored.

### Step 7 — Write README.md

Short human summary:

- Brand signals used
- Queries run (bullet list)
- Table of 5 pins: file, layout, source URL
- Note: colors in pins are **reference only** — Phase 8 resolves from `BRAND_DNA.json`

---

## Handoff to Phase 6a + Phase 6

For **each** pin in `pinterest-manifest.json`:

1. **Phase 6a:** Write `pin-0N-{layout}-reference-prompt.md` via [reference-creative-prompt/SKILL.md](../reference-creative-prompt/SKILL.md) — layout regeneration prompt with color role placeholders.
2. Update manifest: `reference_prompt_file`, `phase_6a_status: complete`.
3. **Phase 6:** For calendar rows using this pin, set Creative DNA `_meta.reference_prompt_ref` → that file.
4. Set `elements[]` to this post's on-image copy only (not the pin's original text).
5. Update manifest pin `phase_6_status` → `complete` and add `creative_dna_file` when DNA is written.

---

## Quality gate (before marking Phase 1b done)

- [ ] `BRAND_IDENTITY.md` was read; keywords match product category (not generic)
- [ ] Exactly **5** PNGs saved under `gdrive/clients/{slug}/references/pinterest/{run_date}/`
- [ ] `search-brief.json` + `pinterest-manifest.json` exist
- [ ] All 5 pins are **dark editorial** single-frame layouts (no stat/carousel/dashboard)
- [ ] Phase 6a: each pin has `{pin}-reference-prompt.md` before calendar Phase 8
- [ ] At least **2** distinct `inferred_layout` values across 5 pins (within editorial family)
- [ ] Each pin has `source_pin_url` and `search_query` recorded
- [ ] `client.json` includes `references_pinterest` folder path

---

## Examples

### Swayam (agentic CRM — B2B SaaS)

**Signals:** product_category=CRM, industry=B2B SaaS, audience=revenue/admissions operators

**Queries:**

1. `saas crm social media post design`
2. `B2B CRM linkedin carousel design`
3. `sales pipeline dashboard instagram post`
4. `whatsapp CRM social media creative`
5. `revenue operations linkedin post design`

### Hypothetical CSR brand

**Signals:** product_category=CSR program, industry=nonprofit / corporate impact

**Queries:**

1. `corporate social responsibility social media design`
2. `CSR campaign instagram post template`
3. `sustainability impact linkedin carousel`
4. `ESG report social media creative`
5. `community impact instagram post design`

---

## Boundaries

- Reference images are **layout inspiration only** — never copy on-image text or competitor branding into finals.
- Do not write to repo `clients/` — Google Drive only (`brand-gdrive` branch).
- Do not use Pinterest pin colors in generation prompts (see [prompt-merge.md](../prompt-merge.md)).
- If user supplied reference creatives in Phase 0, still run this step unless they explicitly say skip — merge user refs + Pinterest pins in Phase 6 (max 5 Pinterest + user refs).
