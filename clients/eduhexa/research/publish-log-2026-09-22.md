# Publish Log — 2026-09-22

**Run date:** 2026-09-22  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free rate limit on this run; synthesis used targeted web research across r/Teachers, r/Professors, r/Indian_Academia, r/edtech-adjacent threads, and education media (15–22 September 2026).

**Strongest trend:** Explain It Aloud — conversational proof replacing artefact-only assessment as AI grading pushback and take-home integrity strain converge; parallel Re-NEET burnout in India.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `8nBk9KKNL2QsuVkUJbsc` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8nBk9KKNL2QsuVkUJbsc` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1790048577834-image.png` ✅ |
| `slug` | `explain-it-aloud-sep-2026` ✅ |
| `title` | Explain It Aloud: When AI Grading and Written Proof Both Miss the Point ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1790048577834-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "8nBk9KKNL2QsuVkUJbsc",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8nBk9KKNL2QsuVkUJbsc"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Explain It Aloud (22 September 2026)](https://app.notion.com/p/3e3c45f0da5d8127ae91e30e4c83d05b)
- **Page ID:** `3e3c45f0-da5d-8127-ae91-e30e4c83d05b`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-22.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-explain-it-aloud-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-explain-it-aloud-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-explain-it-aloud-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_explain_it_aloud.py` | Image generator script |
