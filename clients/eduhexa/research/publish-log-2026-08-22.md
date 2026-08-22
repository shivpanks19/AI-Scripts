# Publish Log — 2026-08-22

**Run date:** 2026-08-22  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search, educator forum analysis, NEET counselling news, parent surveys, and assessment pedagogy discourse (Aug 15–22, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `Mw4O0Ni1eKSa6J92cznt` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/Mw4O0Ni1eKSa6J92cznt` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1787369543011-image.png` ✅ |
| `slug` | `process-proof-shift-aug-2026` ✅ |
| `title` | The Process Proof Shift: Stop Policing AI, Start Demonstrating Thinking ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1787369543011-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "Mw4O0Ni1eKSa6J92cznt",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/Mw4O0Ni1eKSa6J92cznt"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Process Proof Shift (22 August 2026)](https://app.notion.com/p/3c4c45f0da5d8121be0fe9e7c3494b23)
- **Page ID:** `3c4c45f0-da5d-8121-be0f-e9e7c3494b23`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-22.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-process-proof-shift-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-process-proof-shift-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-process-proof-shift-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_process_proof_shift.py` | Image generator script |

---

## Strongest trend

**Process Proof Shift** — teacher communities abandoning unreliable AI detectors for conversation-based verification, draft trails, and tiered assignment labels; parallel NEET Round 1 counselling trust crisis ("does effort still matter?"); schools issuing AI rules faster than AI literacy instruction.
