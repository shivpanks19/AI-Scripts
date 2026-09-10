# Publish Log — 2026-09-10

**Run date:** 2026-09-10  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across r/Teachers AI mandate backlash, phone-collection focus policies, attention-stamina discourse, stoplight AI governance threads, r/Indian_Academia NEET/JEE drop-year burnout, and r/Parenting marks-versus-skills debate (3–10 September 2026).

**Strongest trend:** Focus Before Features — schools mandating AI adoption in teacher observations while attention-stamina crisis remains unresolved.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `dp0j4tzAL5ZRXkpr3rWH` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/dp0j4tzAL5ZRXkpr3rWH` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789011085412-image.png` ✅ |
| `slug` | `focus-before-features-sep-2026` ✅ |
| `title` | Focus Before Features: When AI Mandates Meet an Attention-Stamina Crisis ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789011085412-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "dp0j4tzAL5ZRXkpr3rWH",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/dp0j4tzAL5ZRXkpr3rWH"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Focus Before Features (10 September 2026)](https://app.notion.com/p/3d7c45f0da5d81099705fafe029b1089)
- **Page ID:** `3d7c45f0-da5d-8109-9705-fafe029b1089`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-10.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-focus-before-features-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-focus-before-features-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-focus-before-features-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_focus_before_features.py` | Image generator script |
