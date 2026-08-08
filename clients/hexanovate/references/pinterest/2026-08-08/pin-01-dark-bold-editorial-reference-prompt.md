# Reference Creative Prompt — pin-01-dark-bold-editorial

**Pin file:** `./pin-01-dark-bold-editorial.png`  
**Source URL:** https://in.pinterest.com/pin/2040762329647627/  
**Inferred layout:** `dark-bold-editorial`  
**Phase:** 6a

---

## Regeneration prompt

Create an ultra-premium bold editorial social feed post. Square **1:1 format, 1080×1080 px**. Typography-only layout — no photos, no UI mockups, no human subjects, no clipart.

**Background:** Solid `{{BACKGROUND}}` with subtle 2% film grain texture. Flat lighting — no gradients on text.

**Layout zones:**
- **Center-left:** Vertical accent bar — 4px wide × 120px tall, color `{{ACCENT}}`
- **Center:** Dominant left-aligned headline block with generous 80px side margins
- **Center-lower:** Muted subheadline below headline, left-aligned
- **Bottom-left:** Brand strip `Hexanovate · Growth Systems` in `{{TEXT_MUTED}}`, small caps feel
- **Bottom-right:** URL text only `hexanovate.com` in `{{TEXT_MUTED}}` — no logo icon in generation

**Typography:** Inter or Plus Jakarta Sans. Bold display headline, regular body. Editorial left alignment, tight leading on headline.

**Reference copy (replace in Phase 8):**
- Headline line 1: `Your vendor shouldn't stop at` (`{{TEXT_PRIMARY}}`)
- Headline line 2: `deliverables.` (`{{ACCENT}}` inline accent)
- Subheadline: `Reports are not a growth system. Partners own outcomes.` (`{{TEXT_MUTED}}`)
- Brand strip: `Hexanovate · Growth Systems`
- Footer URL: `hexanovate.com`

---

## Zone map

```
┌─────────────────────────────────────┐
│                                     │
│  │  HEADLINE LINE 1                 │
│  │  headline accent word.           │
│  │                                  │
│     subheadline muted               │
│                                     │
│  Brand strip          hexanovate.com│
└─────────────────────────────────────┘
```

---

## Color roles

| Role | Semantic use |
|------|----------------|
| `{{BACKGROUND}}` | Full canvas |
| `{{TEXT_PRIMARY}}` | Main headline |
| `{{TEXT_MUTED}}` | Subhead, footer, brand strip |
| `{{ACCENT}}` | Vertical bar + one headline word |

---

## must_preserve

- Left vertical accent bar beside headline
- Two-line headline with one accent-colored word
- Left-aligned editorial stack with 80px margins
- Muted subheadline below headline
- Bottom brand strip + footer URL corners
- Dark canvas, typography-only, 1:1

---

## variable_slots

- Headline lines 1–2
- Subheadline
- Brand strip text
- Footer URL
