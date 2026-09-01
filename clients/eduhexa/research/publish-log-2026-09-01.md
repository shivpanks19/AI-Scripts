# Publish Log — 2026-09-01

**Run date:** 2026-09-01  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across educator surveys (Wisconsin AI in education sample), teacher and professor forum discourse, employer hiring shifts, phone-ban studies, CBSE dummy-school enforcement, and NEET/JEE counselling threads (25 August – 1 September 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `TQmwqva4M1mQvTkWEFRp` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/TQmwqva4M1mQvTkWEFRp` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788233929123-image.png` ✅ |
| `slug` | `proof-over-polish-sep-2026` ✅ |
| `title` | Proof Over Polish: When AI Finishes the Assignment but Not the Learning ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788233929123-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "TQmwqva4M1mQvTkWEFRp",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/TQmwqva4M1mQvTkWEFRp"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Proof Over Polish (1 September 2026)](https://app.notion.com/p/3cec45f0da5d81f4aa69cff4340c3f5a)
- **Page ID:** `3cec45f0-da5d-81f4-aa69-cff4340c3f5a`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-01.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-proof-over-polish-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-proof-over-polish-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-proof-over-polish-sep-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_proof_over_polish.py` | Image generator script |

---

## Strongest trend

**Proof Over Polish** — educators shifting from AI cheating debates to evidence-of-learning redesign; polished AI output no longer signals understanding; in-class checkpoints and oral proof rising; employers screening for thinking skills; CBSE dummy-school crackdown pushing integrated programs; phone bans reclaiming attention without solving homework AI polish.
