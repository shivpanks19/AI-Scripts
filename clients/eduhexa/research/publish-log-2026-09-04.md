# Publish Log — 2026-09-04

**Run date:** 2026-09-04  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across India government panel proposals (coaching caps, curriculum alignment, hybrid admissions), teacher technostress surveys, phone-ban national study, NEET/JEE counselling discourse, and educator forum patterns (28 August – 4 September 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `Hvvjuh7NheXnH7YX7PP9` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/Hvvjuh7NheXnH7YX7PP9` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788492712743-image.png` ✅ |
| `slug` | `coaching-school-reckoning-sep-2026` ✅ |
| `title` | The Coaching-School Reckoning: When Classrooms Must Own What Entrance Exams Test ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788492712743-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "Hvvjuh7NheXnH7YX7PP9",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/Hvvjuh7NheXnH7YX7PP9"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Coaching-School Reckoning (4 September 2026)](https://app.notion.com/p/3d1c45f0da5d81b9a1b4d23586a1ad3d)
- **Page ID:** `3d1c45f0-da5d-81b9-a1b4-d23586a1ad3d`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-04.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-coaching-school-reckoning-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-coaching-school-reckoning-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-coaching-school-reckoning-sep-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_coaching_school_reckoning.py` | Image generator script |

---

## Strongest trend

**Coaching-School Reckoning** — government panel proposes coaching caps and curriculum alignment with JEE/NEET; schools must own competitive foundations inside regular periods; parallel technostress from platform sprawl; phone bans reclaim attention without rebuilding teaching primacy.
