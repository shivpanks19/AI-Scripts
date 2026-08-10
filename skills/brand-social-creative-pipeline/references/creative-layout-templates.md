# Creative Layout Templates

**Purpose:** Plug-and-play on-image copy structure via webhook JSON. The pipeline default is `editorial-minimal` (headline + subheadline + footer). Some brands need **multi-zone brand editorials** (logo, tagline, body, insight callout, feature row) — select a template in the webhook instead of changing code.

---

## Why the default is headline + subheadline

The constraint is **policy**, not schema limitation:

| Source | Rule |
|--------|------|
| [single-image-post-policy.md](./single-image-post-policy.md) | Phase 4 default: headline + subheadline + footer |
| [SKILL.md](../SKILL.md) Phase 4 | Same unless `creative_layout` overrides |
| [pre-calendar-setup/SKILL.md](./pre-calendar-setup/SKILL.md) | `selected_slots[]` shape depends on `layout_template` |
| Phase 1b Pinterest fetch | Default pins favor **contrarian 2-line** layouts |
| Phase 8 [prompt-merge.md](./prompt-merge.md) | Maps all `elements[]` types when template is set |

`CREATIVE_DNA_SCHEMA.json` already supports `logo`, `badge`, `icon_row`, `card`, etc. — the pipeline authors them only when **`creative_layout.default_template`** is not `editorial-minimal`.

**Common mismatch:** A brand uploads a full reference creative (logo + tagline + body + feature row) but omits `creative_layout` in the webhook — the agent then picks minimal Pinterest pins and collapses copy to 2 lines. Fix: set `default_template: brand-editorial-full` and pass `reference_image_url`.

---

## Webhook field

```json
{
  "creative_layout": {
    "default_template": "brand-editorial-full",
    "reference_image_url": "https://storage.example.com/brand/reference-layout.png",
    "per_slot_override": true
  }
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `default_template` | No | Layout for all slots; default `editorial-minimal` |
| `reference_image_url` | Recommended when using `brand-editorial-full` | Brand's canonical layout reference — saved to `references/brand-layout/{run_date}/` and used for Phase 6a reverse-engineering |
| `per_slot_override` | No | When `true`, each slot in `campaign.posts[]` or `selected_slots[]` may set its own `layout_template` |

**Alias (run level):** `run.creative_layout_template` → same as `creative_layout.default_template`.

---

## Templates

### `editorial-minimal` (default)

Pinterest contrarian / dark-bold / quote-hero pins. **2–3 text zones.**

| Zone | Element type | Required |
|------|--------------|----------|
| Headline | `headline` | Yes |
| Subheadline | `subheadline` | Yes |
| Footer | `url` | Yes |

`structure_type`: `contrarian-editorial-hero` | `dark-bold-editorial` | `editorial-quote-hero`

---

### `brand-editorial-full`

Full multi-zone brand card. **Matches uploaded reference creatives** with logo, body copy, and feature strip.

| Zone | Element type | Required | Source |
|------|--------------|----------|--------|
| Header logo | `logo` | Yes | Brand assets / `BRAND_IDENTITY.md` |
| Header tagline | `tagline` | Yes | Webhook `brand.tagline` or identity doc |
| Primary headline | `headline` | Yes | `concept` — `{prefix, highlight}` object |
| Body | `body` | Yes | `creative_generation_rules` + concept |
| Insight callout | `insight_callout` | Recommended | `messaging_principles` or strategy |
| Feature row | `icon_row` | Recommended | `product.core_capabilities` or brand value props (3 items) |
| Footer URL | `url` | Yes | `brand.website` host |
| Hero | `hero` (photo) | Yes | `visual_identity` / reference image |

`structure_type`: `brand-editorial-full`

**Headline object shape:**

```json
{
  "type": "headline",
  "content": {
    "prefix": "{setup phrase} ",
    "highlight": "{contrasting phrase}",
    "highlight_color_role": "primary_light"
  }
}
```

**Feature row shape:**

```json
{
  "type": "icon_row",
  "zone": "footer_features",
  "content": {
    "items": [
      { "icon": "{icon_key}", "label": "{value prop 1}" },
      { "icon": "{icon_key}", "label": "{value prop 2}" },
      { "icon": "{icon_key}", "label": "{value prop 3}" }
    ]
  }
}
```

Icon keys are semantic placeholders (`shield_check`, `chart_up`, `users`, etc.) — map to brand-appropriate visuals at render time.

---

## Per-slot webhook override

In `campaign.posts[]` or after pre-calendar setup in brief `selected_slots[]`:

```json
{
  "slot_index": 1,
  "layout_template": "brand-editorial-full",
  "concept": "{contrarian concept from preferred_concepts}",
  "on_image": {
    "tagline": "{brand tagline}",
    "headline": {
      "prefix": "{headline setup} ",
      "highlight": "{emphasized payoff}"
    },
    "body": "{1–2 sentence supporting thought}",
    "insight_callout": {
      "icon": "{icon_key}",
      "prefix": "{callout prefix} ",
      "highlight": "{emphasized word}",
      "suffix": "{callout suffix}"
    },
    "icon_row": [
      { "icon": "{icon_key}", "label": "{value prop 1}" },
      { "icon": "{icon_key}", "label": "{value prop 2}" },
      { "icon": "{icon_key}", "label": "{value prop 3}" }
    ],
    "footer_url": "{brand-domain.com}"
  }
}
```

When `on_image` is **omitted**, Phase 6 expands from `concept` + `BRAND_IDENTITY.md` + webhook brand fields using the template zone map.

---

## Pipeline behavior by template

| Phase | `editorial-minimal` | `brand-editorial-full` |
|-------|---------------------|------------------------|
| 1b Pinterest | Use fetched contrarian pins | **Also** download `reference_image_url` → `references/brand-layout/{run_date}/` |
| 6a | Pin reference prompt | Pin prompt **or** reverse-engineer brand layout reference |
| 3b brief | `headline`, `subheadline` | `layout_template`, `on_image` object |
| 6 Creative DNA | 3 elements | Full `elements[]` per zone table above |
| 8 prompt merge | 3-zone copy lock table | Full zone map + all element strings |
| 9 GenerateImage | Short headline stack | Full layout prose from merged prompt |

---

## Dedup rule

Headline dedup (Phase 3b) uses **normalized primary headline text** only:

- `editorial-minimal`: `headline` + `subheadline` joined
- `brand-editorial-full`: `headline.prefix` + `headline.highlight` (ignore body, callout, feature row for dedup)

---

## Adding a new template

1. Add a row to this file with zone → element type map.
2. Add `structure_type` to allowed list in [single-image-post-policy.md](./single-image-post-policy.md).
3. Optional: ship a `references/brand-layout/{client_slug}/` reference prompt for Phase 6a.

---

## Example webhook snippet

```json
{
  "client": {
    "client_slug": "{client_slug}",
    "website": "https://www.example.com"
  },
  "creative_layout": {
    "default_template": "brand-editorial-full",
    "reference_image_url": "https://storage.example.com/{client_slug}/reference-layout.png"
  },
  "run": {
    "posts_per_week": 3,
    "creative_layout_template": "brand-editorial-full"
  }
}
```
