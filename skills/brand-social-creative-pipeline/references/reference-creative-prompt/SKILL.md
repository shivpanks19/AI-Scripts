---
name: reference-creative-prompt
description: >-
  Reverse-engineer a Pinterest or uploaded reference image into a regeneration
  prompt that preserves layout, typography placement, and decorative structure.
  Run in brand-social-creative-pipeline Phase 6a after Phase 1b pins exist and
  before or alongside Phase 6 Creative DNA. Phase 8 merges this prompt with
  BRAND_DNA.json (colors) and calendar copy (on-image text).
---

# Reference Creative Prompt (Phase 6a)

Produces a **regeneration prompt** from a reference image — detailed enough that an image model could recreate the **same layout** (zones, type scale, decorative elements, hero placement) while leaving **colors as named roles** for Phase 8 to resolve from `BRAND_DNA.json`.

**Pipeline position:** Phase **6a** — after Phase 1b pins are saved; run **before** Phase 8 for every pin used by a calendar creative.

**Downstream:** Phase 8 reads `{pin}-reference-prompt.md` + `BRAND_DNA.json` + `{slug}.CREATIVE_DNA.json` `elements[]` → `{slug}-prompt.md`.

**Storage:** Read reference images from Google Drive via MCP. Write `{pin}-reference-prompt.md` back to the same Drive folder. See [google-drive-storage.md](../google-drive-storage.md).

---

## Inputs

| Input | Path | Required |
|-------|------|----------|
| Reference image | `references/pinterest/{run_date}/pin-0N-{layout}.png` (or `.jpg`) | Yes |
| Pinterest manifest row | `pinterest-manifest.json` → matching pin | Yes |
| Brand DNA (read-only) | `BRAND_DNA.json` → typography.family, canvas policy | Recommended |

---

## Outputs

Per reference image:

```
gdrive/clients/{client_slug}/references/pinterest/{run_date}/
├── pin-01-{layout}.png
├── pin-01-{layout}-reference-prompt.md    # Phase 6a — NEW
└── pinterest-manifest.json                # add reference_prompt_file per pin
```

Per calendar creative (Creative DNA links to pin prompt):

```json
"_meta": {
  "reference_asset": "../../references/pinterest/pin-01-dark-bold-editorial.jpg",
  "reference_prompt_ref": "../../references/pinterest/pin-01-dark-bold-editorial-reference-prompt.md"
}
```

---

## Procedure

### Step 1 — Open and analyze the reference image

**You must visually inspect the pin file** — do not invent layout from manifest metadata alone.

Record with pixel-level specificity:

| Dimension | What to capture |
|-----------|-----------------|
| **Canvas** | Ratio, implied safe margins (e.g. 80px sides) |
| **Background** | Flat / gradient direction / texture / grain — describe, no hex |
| **Zones** | Every text block, image area, rule, badge, footer — position + relative size |
| **Typography** | Alignment (left/center), line breaks, relative scale (display vs sub vs footer) |
| **Decorative** | Vertical rules, halftone, shapes, photo crops, icon rows |
| **Hero** | Photo / illustration / person / object / UI mockup / typography-only — exact placement, pose, crop, props |
| **On-image copy in reference** | Transcribe verbatim (will be **replaced** in Phase 8) |

**Reference fidelity:** If the pin contains a person, photo subject, or key object, document it fully in the **Regeneration prompt** prose under `## Hero subject (must preserve)`. Phase 9 generates from that text — not from attaching the pin image. See [reference-fidelity.md](../reference-fidelity.md).

Use **color roles**, not hex from the pin:

| Role | Use in reference prompt |
|------|-------------------------|
| `{{BACKGROUND}}` | Canvas fill |
| `{{TEXT_PRIMARY}}` | Main headline |
| `{{TEXT_SECONDARY}}` | Subhead / body on canvas |
| `{{TEXT_MUTED}}` | Footer, captions, slide counter |
| `{{ACCENT}}` | Rules, highlight words, badges |
| `{{ACCENT_SECONDARY}}` | Second highlight if present |

**Never** embed Pinterest hex in the reference prompt — Phase 8 resolves roles from Brand DNA.

### Step 2 — Write `{pin}-reference-prompt.md`

Use [reference-prompt.template.md](./reference-prompt.template.md). Required sections:

1. **Reference metadata** — pin file, source URL, `inferred_layout`
2. **Regeneration prompt** — full prose a model can follow to recreate layout
3. **Zone map** — ASCII diagram matching the image
4. **Color roles table** — role → semantic use (resolved in Phase 8)
5. **must_preserve** — layout traits that must not change when swapping copy
6. **variable_slots** — on-image text, brand name strip, footer URL (Phase 8 injects)

### Step 3 — Update manifest

Add to each pin in `pinterest-manifest.json`:

```json
{
  "reference_prompt_file": "./pin-01-dark-bold-editorial-reference-prompt.md",
  "phase_6a_status": "complete"
}
```

### Step 4 — Link in Creative DNA

When authoring `{slug}.CREATIVE_DNA.json` for a calendar row:

- Set `_meta.reference_prompt_ref` → the pin's `-reference-prompt.md`
- Set `replication.must_preserve` to match reference prompt's `must_preserve`
- Put **only** this post's on-image copy in `elements[]` (Phase 8 content layer)

---

## Quality gate

- [ ] Reference image was opened and analyzed visually
- [ ] Regeneration prompt describes **every visible zone** (not generic "dark editorial")
- [ ] No `#` hex values from the pin — only `{{COLOR_ROLE}}` placeholders
- [ ] `must_preserve` lists ≥4 layout traits specific to this pin
- [ ] Manifest updated with `reference_prompt_file`
- [ ] Calendar Creative DNA points to `reference_prompt_ref`

---

## Boundaries

- Reference prompt describes **layout fidelity** — not brand voice or campaign copy
- Do not copy competitor on-image text into finals — reference copy is documented then **replaced** in Phase 8
- One reference prompt per pin; multiple calendar slugs may share the same pin prompt

## See also

- [../prompt-merge.md](../prompt-merge.md) — three-layer merge (reference + brand colors + content)
- [../pinterest-reference-fetch/SKILL.md](../pinterest-reference-fetch/SKILL.md) — Phase 1b pins
- `gdrive/clients/swayam/references/pinterest/dark-bold-editorial-prompt.md` — example of layout-specific prompt quality
