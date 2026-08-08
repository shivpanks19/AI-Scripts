# Hexanovate — Pipeline Complete

**Client:** www.hexanovate.com  
**Platforms:** Instagram, Facebook  
**Cadence:** Weekly (3 posts)  
**Calendar week:** 2026-08-11  
**Run date:** 2026-08-08  
**Outlet ID:** `OCnD41LsRXTKPgnR1CDu`  
**Mode:** Full (Phases 0–10)

---

## Pipeline checklist

```
- [x] Phase 0: Intake + client scaffold
- [x] Phase 1: BRAND_IDENTITY.md (design-brand-guardian)
- [x] Phase 1b: 5 Pinterest pins → references/pinterest/2026-08-08/
- [x] Phase 6a: {pin}-reference-prompt.md per pin
- [x] Phase 2: plans/2026-08-08/social-media-context.md
- [x] Phase 3: plans/2026-08-08/content-strategy.md
- [x] Phase 4: plans/2026-08-08/content-calendar.md
- [x] Phase 5: BRAND_DNA.json
- [x] Phase 6: 3× CREATIVE_DNA.json
- [x] Phase 7: 3× posts (IG + FB)
- [x] Phase 7b: 3× caption scores
- [x] Phase 8: 3× prompts (brand-color merged)
- [x] Phase 9: 3× PNG generated
- [x] Phase 9b: 3× Firestore publish
- [x] Phase 10: This handoff
```

---

## Files

### Brand
| File | Purpose |
|------|---------|
| `client.json` | Intake + pipeline metadata |
| `BRAND_IDENTITY.md` | Full brand foundation |
| `BRAND_DNA.json` | Render tokens (#0A0A0A + #FF5500 + #FFB800) |
| `BRAND_DNA_SCHEMA.json` | Schema copy |
| `CREATIVE_DNA_SCHEMA.json` | Schema copy |

### Pinterest (Phase 1b + 6a)
| File | Purpose |
|------|---------|
| `references/pinterest/2026-08-08/pin-01` … `pin-05` | 5 layout references |
| `references/pinterest/2026-08-08/pinterest-manifest.json` | Pin registry |
| `references/pinterest/2026-08-08/*-reference-prompt.md` | Phase 6a regeneration specs |

### Strategy
| File | Purpose |
|------|---------|
| `plans/2026-08-08/social-media-context.md` | Voice, pillars, anti-patterns |
| `plans/2026-08-08/content-strategy.md` | Weekly mix + differentiation |
| `plans/2026-08-08/content-calendar.md` | 3-slot week plan |

### Week 2026-08-11 creatives
| Slug | DNA | Post | Scores | Prompt | PNG | Firestore |
|------|-----|------|--------|--------|-----|-----------|
| `not-agency-system-editorial` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `effort-outcome-gap-editorial` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `three-markets-editorial` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

All in `instagram/2026-08-11/` (Facebook copy in `facebook/2026-08-11/`)

---

## Calendar execution

| Date | Platform | Slug | Topic | Firestore path | Status |
|------|----------|------|-------|----------------|--------|
| 2026-08-11 | instagram + facebook | not-agency-system-editorial | Anti-agency positioning | OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/PD2oS1YBx88Gjg7wcdP8 | published |
| 2026-08-13 | instagram + facebook | effort-outcome-gap-editorial | Effort–outcome gap | OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/HgxMz2AG2Q1pHOnllZxM | published |
| 2026-08-15 | instagram + facebook | three-markets-editorial | Three verticals | OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/kOcpdmoZ09fDoZHgJtWJ | published |

---

## Publish log

See `instagram/2026-08-11/publish-log.md` for GCS URLs, documentIds, and caption scores.

---

## Brand notes

1. **Website:** hexanovate.com is SPA shell — brand identity merged from meta tags, public LinkedIn/Linktree research, and webhook brief ("marketing agency").
2. **Positioning:** Anti-agency growth systems partner — B2B (ThirdMeta), FMCG (NativeUnit), Education (EduHexa).
3. **Colors:** Dark canvas `#0A0A0A`, growth orange `#FF5500`, highlight `#FFB800`.
4. **Pinterest:** Webhook URLs returned placeholders in CI; pin-03 used for split-layout + photo hero fidelity (v2 regen 2026-08-08).
5. **Reference fidelity:** Pipeline updated — Phase 9 always passes `reference_image_paths`; hero subjects preserved when present in pin.

---

## Next steps

- Review drafts in Social AI Poster UI for outlet `OCnD41LsRXTKPgnR1CDu`
- Schedule posts via connected scheduler
- Composite Hexanovate logo bottom-right post-generation if required
- A/B variants: change `variable_slots` only, keep `must_preserve`
