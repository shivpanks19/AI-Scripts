---
name: brand-composition
description: >-
  Phase 9a — deterministic brand asset composition after AI image generation.
  Composites the real logo from brand assets onto AI-generated backgrounds using
  normalized layout specs. AI plans layout; code enforces geometry.
---

# Brand Composition (Phase 9a)

Runs **after Phase 9** (AI background generation) and **before Phase 9b** (Firestore publish).

**Critical rule:** The AI image model generates the visual only. The real brand logo is **never** AI-rendered — it is composited programmatically from `BRAND_DNA.json` assets.

---

## Architecture

```
Creative Brief → Creative DNA + layout_spec
        ↓
Phase 8: prompt (logo-safe zone reserved, no logo in generation prompt)
        ↓
Phase 9: AI → {slug}-background.png
        ↓
Phase 9a: compose_brand_assets.py → {slug}.png (+ layout.json, optional debug)
        ↓
Phase 9b: publish final PNG
```

**AI decides layout intent. Code enforces geometry.**

---

## When to run

Run Phase 9a when **either**:

- `BRAND_DNA.json` → `logo.composition.enabled` is `true`, or
- `logo.overlay.enabled` is `true` (legacy alias)

Skip when composition is disabled — Phase 9 writes directly to `{slug}.png`.

---

## Inputs

| Input | Path | Required |
|-------|------|----------|
| AI background | `{slug}-background.png` | Yes |
| Brand DNA | `clients/{slug}/BRAND_DNA.json` | Yes |
| Creative DNA | `{slug}.CREATIVE_DNA.json` | Yes (unless `layout.json` provided) |
| Layout spec | `{slug}.layout.json` | Optional override |

---

## Outputs

| File | Purpose |
|------|---------|
| `{slug}.png` | Final composed creative |
| `{slug}.layout.json` | Normalized layout + resolved pixel coordinates |
| `{slug}-debug.png` | Debug overlay (zones, logo bbox) when `--debug` |

---

## Logo placement

Semantic positions (enum — do not invent arbitrary names):

`TOP_LEFT` | `TOP_CENTER` | `TOP_RIGHT` | `CENTER_LEFT` | `CENTER` | `CENTER_RIGHT` | `BOTTOM_LEFT` | `BOTTOM_CENTER` | `BOTTOM_RIGHT`

Presets live in `scripts/lib/logo_presets.py` — **single source of truth**.

Sizes: `SMALL` (0.12) | `MEDIUM` (0.17) | `LARGE` (0.22) — overridable per brand in `logo.composition.sizes`.

---

## Layout spec

See `templates/LAYOUT_SPEC_SCHEMA.json`. Store in Creative DNA as `layout_spec` or write `{slug}.layout.json`.

Example:

```json
{
  "canvas": { "width": 1080, "height": 1080, "ratio": "1:1" },
  "logo": {
    "enabled": true,
    "position": "TOP_LEFT",
    "size": "MEDIUM",
    "variant": "AUTO"
  },
  "logoZone": { "x": 0.03, "y": 0.02, "width": 0.24, "height": 0.10 },
  "composition": {
    "subjectZone": { "x": 0.45, "y": 0.12, "width": 0.52, "height": 0.75 },
    "headlineZone": { "x": 0.05, "y": 0.12, "width": 0.55, "height": 0.20 }
  }
}
```

Pixel conversion: `pixelX = normalizedX × canvasWidth`

---

## Phase 8 prompt rules (logo-safe zone)

When `logo.composition.enabled`:

1. **Do not** include logo wordmark, icon, or brand mark in the Generation prompt.
2. **Do** include logo-safe zone reservation:

```
LOGO SAFE ZONE (reserved — do not render any logo):
Reserve the top-left region (approximately x:0.03–0.27, y:0.02–0.12 normalized) as empty negative space.
Do not generate any logo, watermark, brand mark, text-based brand identity, or substitute symbol in this area.
Keep important visual subjects and critical details outside the reserved logo area.
```

3. Mark logo element in copy-lock table as `COMPOSITE ONLY — Phase 9a`.

---

## CLI

```bash
python scripts/compose_brand_assets.py \
  --background clients/{client}/instagram/{run_date}/{slug}-background.png \
  --brand-dna clients/{client}/BRAND_DNA.json \
  --creative-dna clients/{client}/instagram/{run_date}/{slug}.CREATIVE_DNA.json \
  --output clients/{client}/instagram/{run_date}/{slug}.png \
  --debug
```

Mirror final PNG to `facebook/{run_date}/`.

---

## Logo asset selection

1. Read `BRAND_DNA.logo.assets` (`light`, `dark`, `wordmark`, `primary`)
2. If `variant: AUTO` (default), sample background luminance in logo zone
3. Dark background → `light` logo; light background → `dark` logo
4. Prefer SVG when available; else highest-res PNG
5. Crop to visible (non-transparent) bounds before contain-fit
6. Never stretch — `scale = min(maxW/w, maxH/h)`

---

## Validation (fail loudly)

- Logo asset exists and was used
- Logo inside canvas and safe zone
- Aspect ratio preserved
- All normalized coords in [0, 1]
- No zero/negative zone dimensions

---

## Debug mode

`--debug` writes `{slug}-debug.png` showing:

- Canvas dimensions
- Logo safe zone (cyan)
- Actual logo bounding box (gold)
- Subject/headline zones when present

---

## Canvas formats

Presets in `logo_presets.CANVAS_PRESETS`:

| Key | Size |
|-----|------|
| instagram_square | 1080×1080 |
| instagram_portrait | 1080×1350 |
| instagram_story | 1080×1920 |
| linkedin_landscape | 1200×627 |

Same semantic `TOP_RIGHT` placement scales consistently across formats.

---

## See also

- [../../templates/LAYOUT_SPEC_SCHEMA.json](../../templates/LAYOUT_SPEC_SCHEMA.json)
- [../prompt-merge.md](../prompt-merge.md) — Phase 8 logo-safe prompt rules
- [../creative-layout-templates.md](../creative-layout-templates.md)
- `scripts/lib/logo_compositor.py` — renderer implementation
