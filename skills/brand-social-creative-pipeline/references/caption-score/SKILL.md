---
name: caption-score
description: >-
  Score social post copy before Firestore publish. Produces captionScore (0–100)
  and captionScores dimension breakdown for OUTLET/{outletId}/social-ai-poster.
  Run in brand-social-creative-pipeline Phase 7 after post-writer-sms or
  caption-writer-sms output.
---

# Caption Score

Scores **ready-to-post copy** before Phase 9b Firestore publish. Social AI Poster reads `captionScore` and `captionScores` on each `social-ai-poster` document.

**Pipeline position:** end of **Phase 7** — immediately after `{slug}-post.md` or `{slug}-caption.md` is written.

---

## Inputs

| Input | Path | Required |
|-------|------|----------|
| Post copy | `{creative_folder}/{slug}-post.md` or `{slug}-caption.md` | Yes |
| Platform | Calendar row / Creative DNA channel | Yes |
| Brand voice | `BRAND_DNA.json` → `voice` | Yes |
| Social context | `plans/social-media-context.md` | Recommended |

---

## Outputs

```
{creative_folder}/{slug}-caption-scores.json
```

Use [caption-scores.template.json](./caption-scores.template.json). Update Creative DNA `copy.caption_scores_ref` when paired.

---

## Scoring rubric (0–100 each)

Score the **caption body only** (exclude hashtag line). Be strict — average pipeline copy should land **70–85**, not 95+.

| Dimension | What to evaluate |
|-----------|------------------|
| `hook` | First 1–2 lines earn the "...more" tap; no throat-clearing |
| `clarity` | One clear idea; readable line breaks; no jargon pile-up |
| `cta` | Obvious next step aligned to `voice.cta_primary` |
| `hashtagFit` | Tags match pillar, platform norms, and copy (if hashtags present) |
| `brandVoice` | Matches `BRAND_DNA.json` tone, vocabulary, audience |
| `platformFit` | Length, structure, emoji/hashtag count fit the platform rules in `post-writer-sms` / `caption-writer-sms` |

**`captionScore` (overall):** weighted average — hook 25%, clarity 20%, cta 15%, hashtagFit 10%, brandVoice 20%, platformFit 10%. Round to nearest integer.

**Quality gate:** If `captionScore` < 65, revise the post (Phase 7) and re-score before Phase 9. Do not publish weak copy unless the user explicitly overrides.

---

## Procedure

1. Read the post file. Split **caption body** vs **hashtags** (last line(s) starting with `#`).
2. Read `BRAND_DNA.json` voice + `plans/social-media-context.md` platform rules.
3. Score each dimension 0–100 with one-line `notes` per dimension (optional but recommended in JSON).
4. Compute `captionScore` using weights above.
5. Write `{slug}-caption-scores.json`:

```json
{
  "slug": "{slug}",
  "platform": "instagram",
  "captionScore": 82,
  "captionScores": {
    "overall": 82,
    "hook": 85,
    "clarity": 80,
    "cta": 78,
    "hashtagFit": 75,
    "brandVoice": 88,
    "platformFit": 84
  },
  "notes": {
    "hook": "Strong contrarian opener.",
    "cta": "CTA present but could be more specific."
  },
  "rubricVersion": "1.0",
  "scoredAt": "2026-08-09T00:00:00+05:30",
  "sourceFile": "{slug}-post.md"
}
```

6. If below quality gate, revise copy and repeat from step 1.

---

## Phase 9b handoff

Phase 9b (`firestore-creative-publish`) **must** read `{slug}-caption-scores.json` and include `captionScore` + `captionScores` in the `POST /ai-content` body alongside parsed `caption` and `hashtags`.

**Skip scoring only when:** user says "skip caption score" or re-publishing an existing doc without re-running Phase 7.

---

## See also

- [../firestore-creative-publish/SKILL.md](../firestore-creative-publish/SKILL.md) — publish payload fields
- [../../SKILL.md](../../SKILL.md) — Phase 7 and 9b
