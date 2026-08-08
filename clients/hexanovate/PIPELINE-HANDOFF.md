# Hexanovate — Pipeline Complete

**Client:** hexanovate.com  
**Platforms:** Instagram, Facebook  
**Cadence:** Weekly (3 posts)  
**Week:** 2026-08-11  
**Run date:** 2026-08-08  
**Mode:** Full (Phases 0–10 + 9b publish)  
**Webhook outlet:** `OCnD41LsRXTKPgnR1CDu`

---

## Pipeline checklist

```
- [x] Phase 0: Intake + client scaffold
- [x] Phase 1: BRAND_IDENTITY.md
- [x] Phase 1b: 5 Pinterest pins → references/pinterest/ (1 webhook + 4 auto-search)
- [x] Phase 2: plans/social-media-context.md
- [x] Phase 3: plans/content-strategy.md
- [x] Phase 4: plans/content-calendar.md (week of 2026-08-11)
- [x] Phase 5: BRAND_DNA.json
- [x] Phase 6: 3× CREATIVE_DNA.json
- [x] Phase 7: 3× captions (+ Facebook copies)
- [x] Phase 8: 3× prompts (brand-color merged)
- [x] Phase 9: 3× PNG generated
- [x] Phase 9b: GCS upload + Firestore publish (3 slugs)
- [x] Phase 10: This handoff
```

---

## Files

### Brand
| File | Purpose |
|------|---------|
| `client.json` | Intake + webhook metadata |
| `BRAND_IDENTITY.md` | Full brand foundation |
| `BRAND_DNA.json` | Render tokens (#0A0A0A + #0066FF) |
| `BRAND_DNA_SCHEMA.json` | Schema copy |
| `CREATIVE_DNA_SCHEMA.json` | Schema copy |

### Pinterest (Phase 1b)
| File | Purpose |
|------|---------|
| `references/pinterest/pin-01` … `pin-05` | 5 layout references |
| `references/pinterest/pinterest-manifest.json` | Pin registry |
| `references/pinterest/search-brief.json` | Query log |

### Strategy
| File | Purpose |
|------|---------|
| `plans/social-media-context.md` | Voice, pillars, anti-patterns |
| `plans/content-strategy.md` | Weekly mix + differentiation |
| `plans/content-calendar.md` | 3-slot week plan |

### Week 2026-08-11 creatives (Instagram)
| Slug | DNA | Caption | Prompt | PNG | Published |
|------|-----|---------|--------|-----|-----------|
| `not-agency-system-editorial` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `portfolio-revenue-stat` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `growth-ecosystem-carousel` | ✅ | ✅ | ✅ | ✅ | ✅ |

All in `instagram/2026-08-11/`

### Facebook
| Path | Contents |
|------|----------|
| `facebook/2026-08-11/` | Mirrored PNGs + captions |

---

## Calendar execution

| Date | Platform | Slug | Topic | Firestore path | Status |
|------|----------|------|-------|----------------|--------|
| 2026-08-11 | instagram, facebook | not-agency-system-editorial | Not an agency — growth system | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/P54TKjY5Kk7cEzWafcJc` | published |
| 2026-08-13 | instagram, facebook | portfolio-revenue-stat | ELMO 3× revenue case | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/El5pGHkuSab5nVkvMvrq` | published |
| 2026-08-15 | instagram, facebook | growth-ecosystem-carousel | Three domains carousel | `OUTLET/OCnD41LsRXTKPgnR1CDu/social-ai-poster/RDsLHR8WjeNgc1xfgPdZ` | published |

---

## Publish log

`instagram/2026-08-11/publish-log.md` — documentId + GCS imageUrl per slug

---

## Brand notes

1. **Website:** hexanovate.com is SPA — brand identity sourced from site bundle meta, portfolio case names, and webhook brief ("marketing agency").
2. **Colors:** `#0A0A0A` canvas + `#0066FF` HEXA blue (aligned with EduHexa portfolio family).
3. **Positioning:** "Not an Agency. A System." — systems framing over agency cliché.
4. **Stats:** Portfolio multiples (ELMO 3×) attributed in caption; not invented survey data.

---

## Next steps

- Schedule posts via connected scheduler (BlackTwist if available)
- Verify GCS image assets in Social AI Poster UI (upload endpoint returned shared path in this run)
- A/B variants: change `variable_slots` only, keep `must_preserve`
- Next week: reserve Wed as `[Flexible]` per calendar
