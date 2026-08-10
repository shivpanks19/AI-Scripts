---
name: svg-logo-layer-experiment
description: >-
  Experimental path — composite real SVG logo as a design layer after AI generation.
  Isolated from production Phase 9a. Run via experiments/svg-logo-layer/run_svg_logo_experiment.py
---

# SVG Logo Layer Experiment

**Status:** Experimental — does not replace production `compose_brand_assets.py`.

## Hypothesis

| Layer | Responsibility |
|-------|----------------|
| AI image model | Creative visual, typography, composition |
| SVG asset | Brand logo (source of truth) |
| `svg_logo_layer.py` | Placement, size, rotation, opacity, treatment |

## Run

```bash
cd AI-Scripts
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python experiments/svg-logo-layer/run_svg_logo_experiment.py
```

## Outputs

`clients/cybernetyx/experiments/svg-logo-layer/{run_date}/{slug}/`

| File | Purpose |
|------|---------|
| `background.png` | AI visual without logo |
| `existing-ai-logo.png` | Baseline from git (AI-drawn logo) |
| `svg-composited-logo.png` | Primary SVG composite (TOP_LEFT, MEDIUM) |
| `svg-composited-logo-debug.png` | Zone/bbox overlay |
| `svg-{position}-{size}.png` | Placement grid (15 variants) |
| `svg-top_right-medium-{treatment}.png` | Container treatment tests |
| `manifest.json` | All pixel coordinates + layout resolved |

## SVG asset

`clients/cybernetyx/references/brand-assets/cybernetyx-logo-white.svg`

Rendered at compose-time via CairoSVG at final pixel dimensions (vector until export).

## AI prompt rule (Phase 8 experiment)

Generation prompt must reserve logo zone and explicitly forbid logo rendering. See `teacher-most-important-technology-editorial-prompt.md` LOGO SAFE ZONE block.

## Production integration

When validated, merge `svg_logo_layer.compose_svg_experiment` into Phase 9a behind `logo.composition.format: svg`.
