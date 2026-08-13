# Publish Log — 2026-08-13

**Run date:** 2026-08-13  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search, Reddit discourse studies (arXiv preprints), education news sources, and educator forum analysis (Aug 6–13, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `ahboTp2gYPuRuStbmfom` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/ahboTp2gYPuRuStbmfom` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786591978478-image.png` ✅ |
| `slug` | `attention-stamina-reset-aug-2026` ✅ |
| `title` | The Attention Stamina Gap: Why Device Bans Are Not Enough ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786591978478-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "ahboTp2gYPuRuStbmfom",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/ahboTp2gYPuRuStbmfom"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Attention Stamina Gap (13 August 2026)](https://app.notion.com/p/3bbc45f0da5d8167aadbd36f27838e94)
- **Page ID:** `3bbc45f0-da5d-8167-aadb-d36f27838e94`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-13.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-attention-stamina-reset-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-attention-stamina-reset-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-attention-stamina-reset-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_attention_stamina_reset.py` | Image generator script |

---

## Strongest trend

**Attention Stamina Gap** — teachers removing devices (Chromebooks, screens) as grassroots response to AI shortcuts, while districts push more AI tools. Device bans reduce distraction but do not rebuild depth. Gen Alpha learned helplessness and NEET uncertainty stress run in parallel.
