# Publish Log — 2026-08-10

**Run date:** 2026-08-10  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search, Reddit discourse studies (arXiv preprints), and education news sources (Aug 3–10, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `NQn2FBn1gwlaj2zdBaVB` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/NQn2FBn1gwlaj2zdBaVB` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786332791126-image.png` ✅ |
| `slug` | `proof-by-process-aug-2026` ✅ |
| `title` | Beyond Detection: Schools Enter the Process-Based Proof Era ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786332791126-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "NQn2FBn1gwlaj2zdBaVB",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/NQn2FBn1gwlaj2zdBaVB"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Proof by Process (10 August 2026)](https://app.notion.com/p/3b8c45f0da5d81e4a468f954be0f22ce)
- **Page ID:** `3b8c45f0-da5d-81e4-a468-f954be0f22ce`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-10.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-proof-by-process-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-proof-by-process-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-proof-by-process-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_proof_by_process.py` | Image generator script |

---

## Strongest trend

**Post-Detection Era** — education discourse shifts from AI surveillance to process-based proof (in-class writing, staged drafts, oral defence).

**Image headline:** Proof by Process. Not Detection.
