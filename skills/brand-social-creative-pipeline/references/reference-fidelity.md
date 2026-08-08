# Prompt-Driven Generation (mandatory)

**Applies to:** Phase 6a, Phase 6, Phase 8, Phase 9.

The reference pin image is **not** passed to the image generator. It is used **only in Phase 6a** to reverse-engineer a complete text regeneration prompt. All layout, hero, and composition detail must live in that prompt prose.

---

## Flow (correct)

```
Phase 6a:  reference PNG  →  visual analysis  →  {pin}-reference-prompt.md (full prose spec)
Phase 8:   reference prompt + BRAND_DNA.json (colors) + Creative DNA elements[] (copy)  →  {slug}-prompt.md
Phase 9:   GenerateImage(description = Generation prompt section ONLY)  →  {slug}.png
```

**Do not** pass `reference_image_paths` to the image generator.  
**Do not** instruct the model to "match", "recreate", or "copy" the attached reference image.

---

## Phase 6a — Reverse-engineer everything into text

Visually inspect the pin once. Write `{pin}-reference-prompt.md` so a model **without seeing the image** could recreate the layout.

Capture in prose:

| Category | Document in regeneration prompt |
|----------|----------------------------------|
| Canvas | Ratio, margins, safe zones |
| Zones | Every text block, panel, footer — position + scale |
| Hero | Person/object type, pose, crop, clothing, props, placement |
| Decorative | Accent bars, curves, split panels, grain, shapes |
| Background | Flat / gradient / split panels — use `{{COLOR_ROLE}}` placeholders |
| Typography | Alignment, relative scale, line breaks |
| must_preserve | Layout traits that stay fixed across variants |
| variable_slots | On-image text replaced in Phase 8 |

Use `{{BACKGROUND}}`, `{{TEXT_PRIMARY}}`, `{{ACCENT}}`, etc. — never pin hex.

---

## Phase 8 — Three-layer text merge

```
final Generation prompt =
    regeneration prose from {pin}-reference-prompt.md   (layout + hero + zones)
  + resolved Brand DNA hex colors                         (replace all {{ROLE}} placeholders)
  + calendar elements[] copy                            (replace variable_slots text)
```

1. Start from the **Regeneration prompt** section — keep layout/hero language verbatim.
2. Resolve every `{{COLOR_ROLE}}` to `BRAND_DNA.json` hex.
3. Overlay `elements[]` on-image copy — exact strings, reference pin text removed.
4. Copy `must_preserve` and zone map into `{slug}-prompt.md`.

The `{slug}-prompt.md` **Generation prompt** section must be **self-contained** — sufficient to generate without the pin file.

---

## Phase 9 — Generate from merged prompt only

```bash
# Correct
GenerateImage(description: <Generation prompt section from {slug}-prompt.md>)

# Wrong — do not do this
GenerateImage(reference_image_paths: [pin.png], description: "match reference...")
```

Rules:

- Build `description` **only** from the **Generation prompt** section of `{slug}-prompt.md`.
- Include hero subject, zones, and `must_preserve` as **written prose** from Phase 6a — not from re-attaching the pin.
- `reference_asset` in Creative DNA is an **audit trail** / Phase 6a input — not a Phase 9 input.

---

## Phase 6 — Creative DNA

- `_meta.reference_prompt_ref` → pin regeneration prompt (required for Phase 8)
- `_meta.reference_asset` → pin PNG (Phase 6a input only; document path, do not use in Phase 9)
- `hero.description` → copied from reference prompt prose
- `elements[]` → this post's on-image copy only

---

## Quality gate

- [ ] Phase 6a prompt describes every zone + hero in prose (no "see reference image")
- [ ] Phase 8 merged prompt is self-contained with Brand DNA hex + new copy
- [ ] Phase 9 did **not** pass `reference_image_paths`
- [ ] Generated layout follows regeneration prompt prose, not pixel-matching the pin
