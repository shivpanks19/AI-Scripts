# Reference Fidelity (mandatory)

**Applies to:** Phase 6a, Phase 6, Phase 8, Phase 9.

Pinterest / uploaded reference images are **layout + composition anchors** — not typography-only templates unless the reference truly has no photo hero.

---

## What to preserve from the reference image

| Category | Preserve in reference prompt + Creative DNA | Recolor? |
|----------|---------------------------------------------|----------|
| **Layout zones** | Text blocks, margins, alignment, relative scale | N/A |
| **Hero subject** | Person pose, crop, gaze, clothing silhouette, placement | Yes — brand palette only |
| **Objects / props** | Books, devices, masks, illustrations, badges, buttons | Yes |
| **Decorative structure** | Accent bars, curves, split panels, grain, shapes | Yes |
| **Background treatment** | Gradient direction, split color blocks, photo bleed | Yes — use Brand DNA hex |
| **On-image copy** | **Replace** with calendar `elements[]` | Brand text colors |

**Do not preserve:** competitor logos, reference pin hex colors, reference pin headline text.

---

## Phase 6a — Reference prompt rules

1. **Visually inspect** every `pin-*.png` — never assume typography-only.
2. If the pin contains a **person, photo, or illustrated subject**, document under `## Hero subject (must preserve)`:
   - Subject type (photo / illustration / 3D)
   - Pose, crop (waist-up, full-body), gaze direction
   - Clothing / props (book, laptop, etc.)
   - Exact zone placement (% of canvas or left/right split)
3. `must_preserve` **must include** hero traits when present — never write "typography-only" if the pin has a subject.
4. `variable_slots` = **text only** — hero is fixed unless calendar explicitly overrides `hero.description`.

---

## Phase 6 — Creative DNA rules

Copy from reference prompt into each `{slug}.CREATIVE_DNA.json`:

```json
"hero": {
  "type": "photo_subject | illustration_subject | abstract_vector | typography_only",
  "description": "Verbatim layout description from reference prompt",
  "placement": "right-half | left-half | center | bottom-third",
  "match_reference": true
},
"replication": {
  "must_preserve": ["...include every hero + layout trait from reference prompt..."],
  "reference_fidelity": "high"
}
```

Set `_meta.reference_asset` to the **actual pin file** used for that calendar row.

---

## Phase 8 — Prompt merge

After color resolution, append to **Generation prompt**:

```
REFERENCE FIDELITY (mandatory):
- Match the reference image composition as closely as possible.
- Preserve hero subject type, pose, crop, and zone placement from the reference.
- Preserve decorative structure (split panels, curves, accent bars, props).
- Recolor only — use Brand DNA hex; do not drop subjects or objects present in the reference.
- Replace on-image text only with the copy lock below.
```

Include a `## Hero subject (must preserve)` section copied from the reference prompt.

---

## Phase 9 — Image generation

1. **Always** pass `reference_image_paths: [creative._meta.reference_asset]`.
2. Description must start with: `Recreate the attached reference image layout closely. Same composition, same hero subject placement. Apply brand colors and replace text only.`
3. If output drops the hero subject, re-run with stronger fidelity language — do not accept typography-only drift when reference has a subject.

---

## Quality gate

- [ ] Reference image was visually inspected
- [ ] Hero documented when present (person / object / illustration)
- [ ] `must_preserve` does not say "typography-only" when reference has a subject
- [ ] Phase 9 used `reference_image_paths`
- [ ] Generated PNG still shows hero zone matching reference (spot-check)
