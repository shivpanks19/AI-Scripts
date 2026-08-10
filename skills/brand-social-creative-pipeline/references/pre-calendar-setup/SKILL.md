---
name: pre-calendar-setup
description: >-
  Phase 3b — pre-calendar setup: deduplicate topics and select slots before
  writing content-calendar.md. Loads prior calendars, tracks used headlines/concepts,
  rotates pillars, and picks unused concepts from creative territory.
---

# Pre-Calendar Setup (Phase 3b)

Runs **after Phase 3** (`content-strategy.md`) and **before Phase 4** (`content-calendar.md`).

**Purpose:** Prevent repeat posts across runs. Each new `{run_date}` batch must use **fresh headlines** unless the webhook explicitly forces presets and dedup passes.

**Scope:** Brand-agnostic. All concepts, pillars, taglines, and copy come from **this run's webhook payload**, `BRAND_IDENTITY.md`, and `content-strategy.md` — never from hardcoded client examples in this skill.

---

## Inputs

| Input | Source | Required |
|-------|--------|----------|
| Content strategy | `plans/{run_date}/content-strategy.md` | Yes |
| Trend research | `plans/{run_date}/trend-research-brief.json` | Yes in pipeline — seed concepts when pool thin |
| Social context | `plans/{run_date}/social-media-context.md` | Yes |
| Prior calendars | `plans/*/content-calendar.md` (all dated folders **except** current `{run_date}`) | Yes — scan even if empty |
| Preferred concepts | Webhook `creative_territory.preferred_concepts` **or** `BRAND_IDENTITY.md` § Creative Territory | If discover mode |
| Preset posts | Webhook `campaign.posts[]` | Only when `calendar_mode: preset` |
| `posts_count` | Webhook `run.posts_per_week`, `run.posts_count`, or strategy | Default **3** |
| History window | Webhook `concept_history_runs` | Default **3** |
| Layout template | Webhook `creative_layout.default_template` or `run.creative_layout_template` | Default `editorial-minimal` |
| Brand voice / rules | Webhook `brand`, `creative_generation_rules`, `messaging_principles` | Recommended |

**No publish dates.** Do not read or write `calendar_start_date`, `calendar_week`, or per-slot `calendar_date`. Scheduling is outside the pipeline.

**Layout templates:** See [creative-layout-templates.md](../creative-layout-templates.md). When `brand-editorial-full`, populate `on_image` in `selected_slots[]` from brand inputs — do not collapse to headline-only.

---

## Webhook calendar modes

| `calendar_mode` | When | Behavior |
|-----------------|------|----------|
| `discover` | Default when `campaign.posts` is absent | Full 7-step procedure below |
| `preset` | When `campaign.posts` is present | Use preset posts **after** dedup check; substitute duplicates from unused concepts |
| `preset_strict` | Webhook sets explicitly | Use `campaign.posts` verbatim — no dedup substitution (audit flag in brief) |

Default: `discover` if no `campaign.posts`; else `preset`.

---

## Procedure (mandatory for `discover`; dedup subset for `preset`)

### Step 1 — Load prior calendars

Glob: `clients/{client_slug}/plans/*/content-calendar.md`

For each file where folder date ≠ current `{run_date}`:

- Parse **Batch overview** (or legacy **Week overview**) table rows
- Parse **Post N** sections: `Slug`, on-image copy, **Angle**, **Pillar**, **Slot**

Sort plan folders by date descending. Keep the most recent `concept_history_runs` folders (default **3**).

### Step 2 — Build `used_headlines[]`

Normalize each headline for comparison:

1. Lowercase, trim, strip trailing punctuation
2. Collapse whitespace
3. Remove filler words only for **fuzzy match** (optional): `the`, `a`, `an`

Extract from prior calendars:

| Field | Source in calendar file |
|-------|-------------------------|
| `headline` | On-image primary headline (flat string or `prefix` + `highlight` joined) |
| `slug` | `creative_template_ref` or **Slug** field |
| `pillar` | Pillar column |
| `run_date` | Parent folder `plans/{run_date}/` |
| `slot_index` | Slot column in overview (if present) |

Also scan `instagram/{run_date}/*.CREATIVE_DNA.json` from prior runs for `elements[]` headline content when calendar file is missing — secondary source only.

**Duplicate rule:** Two headlines match if normalized strings are equal **or** one is a substring of the other (>80% token overlap).

### Step 3 — Load `preferred_concepts[]`

Priority order:

1. Webhook `creative_territory.preferred_concepts`
2. Webhook `campaign.theme` + `messaging_principles` (synthesize concepts)
3. `BRAND_IDENTITY.md` — section **Creative Territory** or **Preferred headline concepts**
4. `content-strategy.md` → **Topic clusters** (flatten bullets to concept strings)
5. `trend-research-brief.json` → `contrarian_hooks[]` and `topic_clusters_suggested[].angles` when steps 1–4 are thin

If none found, derive 10+ concepts from pillars in strategy using the brand's category and voice (contrarian or tension-based framing per `headline_style.preferred_structure` when present).

### Step 4 — Remove concepts used in last N runs

Let `N = concept_history_runs` (default 3).

For each concept in `preferred_concepts[]`:

- Mark **used** if normalized concept matches any `used_headlines[]` entry from the last N plan folders
- Mark **used** if slug stem matches a prior slug (e.g. `more-tools-not-outcomes` ≈ `tools-dont-mean-outcomes`)

Output: `available_concepts[]` (unused), `blocked_concepts[]` (used + reason).

### Step 5 — Read pillar mix for THIS batch

From `plans/{run_date}/content-strategy.md` → **Batch content mix**, **Weekly Content Mix**, or **Content Pillars & Balance**:

- List pillars with slot counts for this run (`posts_count` slots)
- Example pattern (labels vary by brand): Slot 1 = category positioning, Slot 2 = product capability, Slot 3 = customer / proof story

If all slots share one pillar (campaign batch), require **N distinct angles** within that pillar — never near-identical headlines across slots.

### Step 6 — Pick slots (`posts_count` concepts)

For each slot `slot_index` 1…`posts_count`:

1. Assign pillar from Step 5 rotation (or strategy-defined mix)
2. Pick the **highest-priority unused** concept from `available_concepts[]` that fits the pillar
3. Prefer concepts matching `headline_style.preferred_structure` from webhook when present
4. Reject concept if headline normalizes to a `used_headlines[]` match
5. If pool exhausted, generate **one new concept** in pillar aligned to brand voice (document in brief as `generated_concept`)

**Pillar rotation default** (only when strategy does not specify — adapt labels to brand pillars):

| Slot | Pillar role |
|------|-------------|
| 1 | Category / positioning |
| 2 | Product / capability |
| 3 | Customer / proof or thought leadership |

**Preset mode (`campaign.posts`):** For each preset post, check headline against `used_headlines[]`. If duplicate → substitute next `available_concepts[]` in same pillar; log substitution in brief.

**Layout expansion:** When `layout_template` is `brand-editorial-full` and slot has no `on_image`, derive zones from `concept` + `BRAND_IDENTITY.md` + webhook `brand.tagline`, `offer`, `product.core_capabilities`, and `creative_generation_rules` — never from examples in this skill file.

### Step 7 — Write setup brief, then calendar

Write `plans/{run_date}/pre-calendar-setup-brief.json`:

```json
{
  "_meta": {
    "run_date": "YYYY-MM-DD",
    "posts_count": 3,
    "calendar_mode": "discover",
    "layout_template": "editorial-minimal",
    "concept_history_runs": 3,
    "prior_calendars_scanned": ["YYYY-MM-DD", "YYYY-MM-DD"]
  },
  "used_headlines": [
    { "headline": "{normalized headline from prior run}", "slug": "{prior-slug}-editorial", "from_run": "YYYY-MM-DD" }
  ],
  "blocked_concepts": [{ "concept": "...", "reason": "used in run YYYY-MM-DD" }],
  "available_concepts": ["..."],
  "selected_slots": [
    {
      "slot_index": 1,
      "layout_template": "editorial-minimal",
      "pillar": "{pillar_from_strategy}",
      "concept": "{unused concept from preferred_concepts}",
      "headline": "{primary line}",
      "subheadline": "{secondary line or null}",
      "slug": "{topic-kebab}-editorial",
      "pin_ref": "pin-01",
      "source": "preferred_concepts",
      "substituted": false
    },
    {
      "slot_index": 2,
      "layout_template": "brand-editorial-full",
      "pillar": "{pillar_from_strategy}",
      "concept": "{unused concept}",
      "slug": "{topic-kebab}-editorial",
      "on_image": {
        "tagline": "{from brand.tagline or BRAND_IDENTITY}",
        "headline": { "prefix": "{line 1} ", "highlight": "{emphasized phrase}" },
        "body": "{1–2 sentence supporting thought from concept}",
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
        "footer_url": "{brand.website host}"
      },
      "pin_ref": "pin-02",
      "source": "preferred_concepts",
      "substituted": false
    }
  ]
}
```

**`editorial-minimal` slots** use flat `headline` + `subheadline` strings. **`brand-editorial-full` slots** use `on_image` object (from webhook preset or Phase 6 expansion).

**Only after** `pre-calendar-setup-brief.json` exists → invoke **content-calendar-sms** (pipeline mode) to write `content-calendar.md` from `selected_slots[]`.

Phase 4 must cite the brief: `**Setup ref:** plans/{run_date}/pre-calendar-setup-brief.json` (rendered by content-calendar-sms).

---

## Gates

| Gate | Rule |
|------|------|
| No duplicate headlines | Zero overlap between new slot headlines and `used_headlines[]` (unless `preset_strict`) |
| Distinct slugs | All slugs unique within batch and vs last N runs |
| Pillar coverage | At least 2 distinct pillars when `posts_count >= 3` unless strategy explicitly single-pillar batch |
| Brief before calendar | `pre-calendar-setup-brief.json` must exist before `content-calendar.md` |
| Brand-sourced copy only | Taglines, feature rows, and body copy must come from webhook or `BRAND_IDENTITY.md` — not skill examples |

---

## Anti-patterns

- Do **not** copy prior `content-calendar.md` rows into the new run
- Do **not** reuse slot 1's headline from the most recent prior run for slot 1 again
- Do **not** skip Step 1 because "brand is the same"
- Do **not** treat webhook `campaign.posts` as mandatory without dedup unless `preset_strict`
- Do **not** hardcode client-specific headlines, domains, or product names from this skill file

---

## See also

- [../../../content-calendar-sms/SKILL.md](../../../content-calendar-sms/SKILL.md) — Phase 4; renders `content-calendar.md` from this brief
- [../creative-layout-templates.md](../creative-layout-templates.md) — `on_image` zone map per layout template
- [../single-image-post-policy.md](../single-image-post-policy.md) — slug and format rules
- [../../SKILL.md](../../SKILL.md) — pipeline orchestration
