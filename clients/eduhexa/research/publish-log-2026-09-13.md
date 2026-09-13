# Publish Log — 2026-09-13

**Run date:** 2026-09-13  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across r/Teachers AI detector fatigue and prove-it pedagogy, r/Indian_Academia CBSE OSM and registration opacity, r/Professors college mental-health and accommodation threads, r/Parenting screen-homework friction, and r/edtech device-balance discourse (6–13 September 2026).

**Strongest trend:** Prove It In the Room — trust erodes when schools rely on unreliable detectors or opaque digital marks instead of visible proof-of-thinking.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `1GMiQCqJg49WJk9JmE7j` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/1GMiQCqJg49WJk9JmE7j` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789270918053-image.png` ✅ |
| `slug` | `prove-it-in-the-room-sep-2026` ✅ |
| `title` | Prove It In the Room: When Detectors Fail and Digital Marks Lose Trust ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789270918053-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "1GMiQCqJg49WJk9JmE7j",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/1GMiQCqJg49WJk9JmE7j"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Prove It In the Room (13 September 2026)](https://app.notion.com/p/3dac45f0da5d8176aa30dad2b4da8113)
- **Page ID:** `3dac45f0-da5d-8176-aa30-dad2b4da8113`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-13.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-prove-it-in-the-room-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-prove-it-in-the-room-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-prove-it-in-the-room-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_prove_it_in_the_room.py` | Image generator script |
