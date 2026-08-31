# Publish Log — 2026-08-31

**Run date:** 2026-08-31  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (EduHexa)  
**Source:** `eduhexa-automation`  
**Status:** ✅ Complete (Firestore via fallback endpoint)

---

## Research note

Exa MCP hit free-tier rate limit on first attempt. Research supplemented via web search across educator policy discourse, MIT AI and Education report, Florida K-12 through PhD AI regulation (Aug 28), NEET Round 1 counselling data, phone-ban national study, and university syllabus governance guides (Aug 24–31, 2026).

---

## Verification

| Check | Result |
| --- | --- |
| `documentId` | `ciokZcS14R4mZwZ19Sb3` ✅ |
| `collection` | `AI_CONTENT` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/ciokZcS14R4mZwZ19Sb3` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788147194308-image.png` ✅ |
| `slug` | `syllabus-first-aug-2026` ✅ |
| `title` | The Syllabus-First Era: When Disclosure Replaces Detection ✅ |
| `templateName` | `eduhexa_image_post_weekly` ✅ |

---

## Image upload

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1788147194308-image.png"
}
```

---

## Firestore publish

**Primary endpoint (failed):** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → `404 Cannot POST /ai-content` (retried once)

**Successful endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`

```json
{
  "success": true,
  "documentId": "ciokZcS14R4mZwZ19Sb3",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "AI_CONTENT",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/AI_CONTENT/ciokZcS14R4mZwZ19Sb3"
}
```

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [EduHexa Intelligence — Syllabus-First Era (31 August 2026)](https://app.notion.com/p/3cdc45f0da5d81b0b431e888c08e5c37)
- **Page ID:** `3cdc45f0-da5d-81b0-b431-e888c08e5c37`

---

## Local artifacts

| File | Purpose |
| --- | --- |
| `clients/eduhexa/research/community-pulse-2026-08-31.md` | Full research synthesis + content |
| `clients/assets/eduhexa/eduhexa-message-syllabus-first-aug-2026.png` | WhatsApp image (1080×1080) |
| `clients/assets/eduhexa/imagePrompt-eduhexa-message-syllabus-first-aug-2026.txt` | Image generation prompt |
| `clients/eduhexa/research/firestore-publish-syllabus-first-aug-2026.json` | Firestore payload |
| `scripts/generate_eduhexa_image_syllabus_first.py` | Image generator script |

---

## Strongest trend

**Syllabus-First Era** — AI governance moving from detection stacks to syllabus-level disclosure; Florida mandating AI lines in every syllabus pre-K through PhD; MIT students reporting inconsistent rules; NEET counselling exposing marks-versus-ranks honesty gap; phone bans reducing usage without year-one score gains.
