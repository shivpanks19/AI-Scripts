# Publish Log — 2026-08-28

**Run date:** 2026-08-28  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search, Common Sense Media survey coverage, Reddit Sentiment Analyzer snapshots (r/Professors, r/Teachers), educator forum analysis, and India parliamentary panel / CBSE curriculum discourse (Aug 21–28, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `7vXp73FW0LdG8p9plHpj` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/7vXp73FW0LdG8p9plHpj` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1787887959500-image.png` ✅ |
| `slug` | `conversation-gap-aug-2026` ✅ |
| `title` | The 70-30 Conversation Gap: Students Use AI, Teachers Haven't Had the Talk ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1787887959500-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "7vXp73FW0LdG8p9plHpj",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/7vXp73FW0LdG8p9plHpj"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — 70-30 Conversation Gap (28 August 2026)](https://app.notion.com/p/3cac45f0da5d8105abd7c9074bfc024e)
- **Page ID:** `3cac45f0-da5d-8105-abd7-c9074bfc024e`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-28.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-conversation-gap-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-conversation-gap-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-conversation-gap-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_conversation_gap.py` | Image generator script |

---

## Strongest trend

**70-30 Conversation Gap** — 70% of teens use AI for schoolwork; only 30% had a teacher safety conversation; mandates arriving without implementation; students passing with AI but not retaining; India school-coaching split with CBSE foundation integration and Assam coaching reforms.
