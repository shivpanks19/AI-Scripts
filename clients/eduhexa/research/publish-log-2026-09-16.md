# Publish Log — 2026-09-16

**Run date:** 2026-09-16  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt (retried once). Research supplemented via web search across r/Teachers stoplight AI policies and verification pedagogy, responsible-use and PD-gap threads, preservice AI fatigue, r/JEENEETards and r/CBSE coaching batch anxiety and consistency advice, and college attention / phone-vigilance research (9–16 September 2026).

**Strongest trend:** Verify Before You Trust — stoplight governance spreads while classrooms still lack verification pedagogy and parent-legible exemplars.

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `8Fy4aFctbRW27BvePIJE` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8Fy4aFctbRW27BvePIJE` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789529509032-image.png` ✅ |
| `slug` | `verify-before-you-trust-sep-2026` ✅ |
| `title` | Verify Before You Trust: When Stoplight AI Policies Outrun Classroom Pedagogy ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1789529509032-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "8Fy4aFctbRW27BvePIJE",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/8Fy4aFctbRW27BvePIJE"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Verify Before You Trust (16 September 2026)](https://app.notion.com/p/3ddc45f0da5d813f858dec5911e609d1)
- **Page ID:** `3ddc45f0-da5d-813f-858d-ec5911e609d1`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-09-16.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-verify-before-you-trust-sep-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-verify-before-you-trust-sep-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-verify-before-you-trust-sep-2026.json` | Firestore payload response |
| `scripts/generate_eduhexa_image_verify_before_you_trust.py` | Image generator script |
