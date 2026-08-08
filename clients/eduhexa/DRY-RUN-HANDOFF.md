# EduHexa — Pipeline Dry Run Complete

**Client:** eduhexa.in  
**Platform:** Instagram  
**Cadence:** 3 posts / week  
**Run date:** 2026-08-08  
**Mode:** Dry run (Phases 0–8 executed; Phase 9 image generation deferred)

---

## Pipeline checklist

```
- [x] Phase 0: Intake + client scaffold
- [x] Phase 1: BRAND_IDENTITY.md
- [x] Phase 1b: 5 Pinterest pins → references/pinterest/
- [x] Phase 2: plans/social-media-context.md
- [x] Phase 3: plans/content-strategy.md
- [x] Phase 4: plans/content-calendar.md (week of 2026-08-11)
- [x] Phase 5: BRAND_DNA.json
- [x] Phase 6: 3× CREATIVE_DNA.json (calendar week)
- [x] Phase 7: 3× captions
- [x] Phase 8: 3× prompts (brand-color merged)
- [ ] Phase 9: PNG generation — **SKIPPED (dry run)**
- [x] Phase 10: This handoff
```

---

## Files created

### Brand
| File | Purpose |
|------|---------|
| `client.json` | Intake + pipeline metadata |
| `BRAND_IDENTITY.md` | Full brand foundation |
| `BRAND_DNA.json` | Render tokens (#000000 + #0066FF) |
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

### Week 2026-08-11 creatives
| Slug | DNA | Caption | Prompt | PNG |
|------|-----|---------|--------|-----|
| `prove-it-era-editorial` | ✅ | ✅ | ✅ | ⏸ |
| `behaviour-engagement-stat` | ✅ | ✅ | ✅ | ⏸ |
| `leadership-questions-carousel` | ✅ | ✅ | ✅ | ⏸ |

All in `instagram/2026-08-11/`

---

## Calendar execution

| Date | Platform | Slug | Topic | Status |
|------|----------|------|-------|--------|
| 2026-08-11 | instagram | prove-it-era-editorial | Prove-It Era hook | ready_to_generate |
| 2026-08-13 | instagram | behaviour-engagement-stat | 3-in-4 behaviour stat | ready_to_generate |
| 2026-08-15 | instagram | leadership-questions-carousel | 3 questions carousel | ready_to_generate |

---

## Brand notes from dry run

1. **Website:** eduhexa.in is a SPA shell — brand identity sourced from Community Pulse archive + Hexanovate portfolio + existing WhatsApp creatives.
2. **Colors:** Black `#000000` + electric blue `#0066FF` (matches existing `research/image-prompt-*.txt` assets). Not Swayam navy.
3. **Logo:** Composite from `clients/eduhexa logo.png` after generation — same workflow as WhatsApp posters.
4. **Research feed:** `research/community-pulse-2026-08-07.md` (Prove-It Era) powers this week's angles.

---

## To go live (Phase 9)

For each prompt in `instagram/2026-08-11/`:

1. Run `GenerateImage` with `aspect_ratio: 1:1` from merged prompt
2. Save as `{slug}.png`
3. Composite logo bottom-right (~20% width)
4. For carousel: generate slides 2–4 from caption copy (or build in Canva/Figma)
5. Schedule via Meta Business Suite or BlackTwist if connected

**Command to resume:**  
> "Execute Phase 9 for eduhexa week 2026-08-11"

---

## Weekly automation template (future)

```markdown
Read clients/eduhexa/plans/content-calendar.md.
Pull latest `research/community-pulse-*.md` for research.
Run Phases 6–9 for the current week folder.
```

Consider adding `clients/eduhexa/eduhexa-weekly-automation.md` mirroring Swayam's runbook.

---

## Review gates before production

- [ ] Confirm Instagram handle @eduhexa
- [ ] Approve BRAND_IDENTITY positioning
- [ ] Validate stat phrasing with legal/comms if citing surveys externally
- [ ] Approve consultation CTA and bio link
