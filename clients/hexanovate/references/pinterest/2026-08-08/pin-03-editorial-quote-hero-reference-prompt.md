# Reference Creative Prompt — pin-03-editorial-quote-hero

**Pin file:** `./pin-03-editorial-quote-hero.png`  
**Source URL:** https://in.pinterest.com/pin/1039979738966705253/  
**Inferred layout:** `editorial-split-hero`  
**Phase:** 6a

---

## Regeneration prompt

Create a premium single-frame social post. Square **1:1, 1080×1080 px**. **Split editorial layout** — not typography-only.

**Background / panels:**
- Left ~45%: curved purple panel (`{{BACKGROUND}}` or brand primary-dark variant) with wavy edge separating from right zone
- Right ~55%: lighter panel with soft architectural photo bleed (Tower Bridge silhouette, desaturated) behind subject
- Bottom strip: white/light footer band with date, venue, contact placeholders

**Layout zones (left panel):**
- Top: small logo placeholder zone
- Upper: script accent word in `{{ACCENT}}`
- Center: bold headline block in `{{TEXT_PRIMARY}}` (2–3 lines, left-aligned)
- Below: body/subhead in `{{TEXT_MUTED}}`
- CTA pill button in `{{ACCENT}}` fill with dark label

**Hero subject (must preserve):**
- **Type:** photo_subject (cutout)
- **Subject:** young woman, long brown hair, white t-shirt, ripped blue jeans
- **Pose:** seated cross-legged on floor, smiling, reading open book held in hands
- **Placement:** right half of canvas, overlapping the purple/white boundary — waist-up to full seated figure
- **Gaze:** down at book
- **Props:** open book (prominent)

**Footer zone:**
- Three-column strip: date left | venue center | website + phone right
- Small country tags row above footer (rounded pills)

**Typography:** Bold sans headline, script accent for one word, clean sans body.

**Reference copy (replace in Phase 8):**
- Script accent: `International`
- Headline: `EDUCATION EXPO-2050`
- Body: lorem-style subcopy
- CTA: `Register Now`
- Footer: `www.yourweb-site.com`

---

## Zone map

```
┌──────────────────┬─────────────────────┐
│ PURPLE PANEL     │  PHOTO + SUBJECT      │
│ logo             │  (woman + book)       │
│ script accent    │  architectural bg     │
│ HEADLINE         │                       │
│ body             │                       │
│ [CTA button]     │                       │
├──────────────────┴─────────────────────┤
│ footer strip: date | venue | contact    │
└─────────────────────────────────────────┘
```

---

## must_preserve

1. Split layout — copy block left, photo hero right (~45/55)
2. Curved/wavy boundary between panels
3. Seated woman cross-legged reading book — right side, cutout style
4. Architectural photo bleed behind subject (desaturated)
5. CTA pill button in left panel
6. Bottom footer strip with three columns
7. Single frame 1:1 — not carousel

---

## variable_slots

- Headline, subhead/body, CTA label, footer URL only
- Hero subject pose and placement are **fixed** — do not remove person or book
