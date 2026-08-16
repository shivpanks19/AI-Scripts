# Publish Log — 2026-08-16

**Run date:** 2026-08-16  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search, parliamentary panel reports (CBSE/NCERT), education news, parent surveys, and educator forum analysis (Aug 9–16, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `i5uhqtGtSDvyxwAEHVRK` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/i5uhqtGtSDvyxwAEHVRK` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786851095013-image.png` ✅ |
| `slug` | `curriculum-proof-gap-aug-2026` ✅ |
| `title` | The Curriculum Proof Gap: New Exams, Old Books, and the Dual AI Classroom ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786851095013-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "i5uhqtGtSDvyxwAEHVRK",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/i5uhqtGtSDvyxwAEHVRK"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Curriculum Proof Gap (16 August 2026)](https://app.notion.com/p/3bec45f0da5d819b8426de8c195cd642)
- **Page ID:** `3bec45f0-da5d-819b-8426-de8c195cd642`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-16.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-curriculum-proof-gap-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-curriculum-proof-gap-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-curriculum-proof-gap-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_curriculum_proof_gap.py` | Image generator script |

---

## Strongest trend

**Curriculum Proof Gap** — CBSE/NCERT textbook delays with application-based board exams; Dual AI Classroom (teacher AI tools accelerating while student proof standards lag); parent AI trust deficit (78% say school's AI approach matters, most cannot describe policies).
