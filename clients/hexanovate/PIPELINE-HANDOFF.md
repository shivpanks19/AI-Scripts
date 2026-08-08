# Hexanovate — Pipeline Complete

**Client:** hexanovate.com  
**Platforms:** Instagram, Facebook  
**Cadence:** Weekly (3 posts)  
**Run date:** 2026-08-08  
**Calendar week:** 2026-08-11  
**Mode:** Full (Phases 0–10 + 9b publish)  
**Webhook outlet:** `OCnD41LsRXTKPgnR1CDu`

---

## Pipeline checklist

```
- [x] Phase 0: Intake + client scaffold (run_date folders)
- [x] Phase 1: BRAND_IDENTITY.md (regenerated)
- [x] Phase 1b: 5 Pinterest pins → references/pinterest/2026-08-08/
- [x] Phase 2: plans/2026-08-08/social-media-context.md
- [x] Phase 3: plans/2026-08-08/content-strategy.md
- [x] Phase 4: plans/2026-08-08/content-calendar.md
- [x] Phase 5: BRAND_DNA.json (regenerated)
- [x] Phase 6: 3× CREATIVE_DNA.json
- [x] Phase 7: 3× posts (+ Facebook copies)
- [x] Phase 7b: 3× caption-scores.json
- [x] Phase 8: 3× prompts (brand-color merged)
- [x] Phase 9: 3× PNG generated
- [x] Phase 9b: GCS upload + Firestore publish (3 slugs)
- [x] Phase 10: This handoff
```

---

## Run folders (this invocation)

| Path | Purpose |
|------|---------|
| `plans/2026-08-08/` | Social context, strategy, calendar |
| `references/pinterest/2026-08-08/` | 5 pin references + manifest |
| `instagram/2026-08-08/` | Creatives, prompts, posts, PNGs |
| `facebook/2026-08-08/` | Mirrored posts + PNGs |
| `runs/2026-08-08/` | Run-scoped handoff copy |

Prior exploratory run preserved at `instagram/2026-08-11/` (not overwritten).

---

## Calendar execution

| Date | Platform | Slug | Firestore path | Status |
|------|----------|------|----------------|--------|
| 2026-08-11 | instagram, facebook | not-agency-system-editorial | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/4E4FcmPvER6XUsYzCB0E` | published |
| 2026-08-13 | instagram, facebook | portfolio-revenue-stat | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/PdCRmeMiu8nCeFarvTOm` | published |
| 2026-08-15 | instagram, facebook | growth-ecosystem-carousel | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/2VrvSrh1K0XRw0BCFqIR` | published |

---

## Creatives (instagram/2026-08-08/)

| Slug | DNA | Post | Prompt | PNG | Published |
|------|-----|------|--------|-----|-----------|
| not-agency-system-editorial | ✅ | ✅ | ✅ | ✅ | ✅ |
| portfolio-revenue-stat | ✅ | ✅ | ✅ | ✅ | ✅ |
| growth-ecosystem-carousel | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Publish log

`instagram/2026-08-08/publish-log.md`

---

## Brand notes

1. **Website:** hexanovate.com — growth ecosystem for B2B, FMCG, and Education; brief merged ("marketing agency").
2. **Colors:** `#0A0A0A` canvas + `#0066FF` HEXA blue.
3. **Positioning:** "Not an Agency. A System." — systems framing over agency cliché.
4. **Stats:** Portfolio multiples (ELMO 3×) from site portfolio — attributed in captions.

---

## Next steps

- Schedule posts via connected scheduler
- A/B variants: change `variable_slots` only, keep `must_preserve`
- Next week: reserve Wed as `[Flexible]` per calendar
