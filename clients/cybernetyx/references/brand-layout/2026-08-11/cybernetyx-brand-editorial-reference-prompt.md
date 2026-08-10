# Reference Prompt — cybernetyx-brand-editorial-full

**Reference file:** `./cybernetyx-brand-editorial-reference.png`  
**Layout:** `brand-editorial-full`  
**Source:** Webhook `creative_layout.reference_image_url`

## Regeneration prompt

Create a 1080×1080 single-frame premium B2B education editorial social post. Full-bleed {{BACKGROUND}} deep navy canvas with subtle grain and soft cinematic lighting.

**Header zone (top-left):** Cybernetyx logo mark + wordmark "CYBERNETYX™" in {{TEXT_PRIMARY}} bold sans-serif. Below logo: tagline line in small caps {{TEXT_MUTED}} — exact tagline from variable_slots.

**Top-right decorative zone:** Subtle electric blue network linework — concentric circles and radiating paths with small education icons (graduation cap center node, chart, people, screen, lock) at 15–25% opacity using {{ACCENT}}.

**Primary headline zone (upper-left, below header):** Large bold sans-serif two-part headline — prefix in {{TEXT_PRIMARY}}, emphasized phrase in {{ACCENT}} (display scale, 4–10 words total). Strong negative space to the right.

**Body zone (mid-left):** 1–2 sentence supporting thought in {{TEXT_PRIMARY}} at body scale, max 160 characters, left-aligned.

**Insight callout (mid-left, below body):** Small icon (two people or educator motif) + single line: prefix in {{TEXT_MUTED}}, one emphasized word in {{ACCENT}}, suffix in {{TEXT_MUTED}}.

**Hero photo (right half, full height):** Confident Indian educator in professional attire, arms crossed or teaching posture, direct gaze. Cinematic classroom or auditorium background with blurred audience. Subject lit warmly; background desaturated navy. Human is secondary visual focus — headline dominates.

**Footer feature row (bottom-left):** Three icon+label pairs in a horizontal row — shield/check, chart-up, educator-star icons in {{ACCENT}} with short labels in {{TEXT_MUTED}} small caps.

**Footer URL (bottom-right):** Thin horizontal rule leading to URL in {{ACCENT}} small sans-serif.

No carousel indicators. No product hero shot. No generic AI brain graphics.

## Hero subject (must preserve)

Confident educator (Indian professional context), right-half composition, cinematic lighting, blurred classroom audience behind, human-centered not stock-smile tablet pose.

## Zone map

```
┌─────────────────────────────────────────┐
│ [Logo] CYBERNETYX™          [network]   │
│ TAGLINE                                 │
│                                         │
│ Headline prefix                         │
│ HIGHLIGHT phrase.                       │
│                                         │
│ Body copy paragraph...                  │
│ [icon] Callout prefix HIGHLIGHT suffix  │
│                                         │
│ [icon] Label  [icon] Label  [icon] Label│
│                              ─ url.com  │
│              [educator hero photo]      │
└─────────────────────────────────────────┘
```

## Color roles

| Role | Use |
|------|-----|
| {{BACKGROUND}} | Full canvas — primary_dark navy |
| {{TEXT_PRIMARY}} | Logo, headline prefix, body |
| {{ACCENT}} | Headline highlight, callout emphasis, icons, URL |
| {{TEXT_MUTED}} | Tagline, callout prefix/suffix, feature labels |

## must_preserve

- Cybernetyx logo + tagline header top-left
- Two-part headline with blue highlight phrase
- Body paragraph + insight callout with icon
- Three-icon feature row bottom-left
- URL bottom-right with rule
- Educator hero right half — cinematic, human-centered
- Subtle blue network graphics top-right
- Single frame — no slide counter

## variable_slots

- Tagline
- Headline prefix + highlight
- Body copy
- Insight callout (icon, prefix, highlight, suffix)
- Icon row (3 items)
- Footer URL

## Reference copy (replace in Phase 8)

TAGLINE: SMART. SECURE. FUTURE READY.
HEADLINE: Smart boards aren't / intelligent classrooms.
BODY: Intelligence in education comes from empowered educators, insightful systems, and inspired learners—working together.
CALLOUT: Technology is the enabler. / Educators / are the differentiator.
ICON ROW: Secure by Design | Data that Drives Impact | Built for Educators. Focused on Learners.
FOOTER: cybernetyx.com
