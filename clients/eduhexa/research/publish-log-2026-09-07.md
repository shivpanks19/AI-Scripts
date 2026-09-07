# Publish Log — 2026-09-07

**Run date:** 2026-09-07  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across Google Gemini student rollout, APA engagement-vs-learning report (3 September 2026), NY teachers analog classroom reset, teacher assessment redesign discourse, EdTech fatigue surveys, and India CBSE competitive-integration updates (31 August – 7 September 2026).

**Strongest trend:** AI Literacy Gap — student AI access outpaced school policy, training, and prove-it assessment design.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `8K4MSUTPUIQP69dd1j45` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8K4MSUTPUIQP69dd1j45` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788751906225-image.png` ✅ |
| `slug` | `ai-literacy-gap-sep-2026` ✅ |
| `title` | The AI Literacy Gap: When Student Access Outruns School Readiness ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788751906225-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "8K4MSUTPUIQP69dd1j45",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8K4MSUTPUIQP69dd1j45"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — AI Literacy Gap (7 September 2026)](https://app.notion.com/p/3d4c45f0da5d81eb9290c32f46275e1d)
- **Page ID:** `3d4c45f0-da5d-81eb-9290-c32f46275e1d`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-07.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-ai-literacy-gap-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-ai-literacy-gap-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-ai-literacy-gap-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_ai_literacy_gap.py` | Image generator script |
