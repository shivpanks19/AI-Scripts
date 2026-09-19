# Publish Log — 2026-09-19

**Run date:** 2026-09-19  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa web research across r/Teachers, r/education, r/edtech, r/Professors, r/Indian_Academia, r/CBSE, r/JEENEETards, r/IndianTeenagers, r/Parenting, and r/college (12–19 September 2026).

**Strongest trend:** Grade the Process, Not the Paste — teachers exiting detector arms races for process-weighted assessment while policy whiplash (ban vs ChatGPT Edu) and CBSE burnout threads expose answer-first study habits.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `x1getaDfMnkgzzwE86of` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/x1getaDfMnkgzzwE86of` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789788677836-image.png` ✅ |
| `slug` | `grade-the-process-sep-2026` ✅ |
| `title` | Grade the Process, Not the Paste: When AI Integrity Becomes a Teacher Workload Crisis ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789788677836-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "x1getaDfMnkgzzwE86of",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/x1getaDfMnkgzzwE86of"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Grade the Process (19 September 2026)](https://app.notion.com/p/3e0c45f0da5d81a3b8d4f4182ec5e70f)
- **Page ID:** `3e0c45f0-da5d-81a3-b8d4-f4182ec5e70f`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-19.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-grade-the-process-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-grade-the-process-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-grade-the-process-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_grade_the_process.py` | Image generator script |
