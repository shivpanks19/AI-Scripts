# EduHexa Weekly Publish Log — 10 November 2026

## Research
- **Period:** 3–10 November 2026
- **Sources:** Exa MCP (needs auth); cursor WebSearch across r/Teachers, r/education, r/edtech, r/Professors, r/CBSE, r/JEENEETards, r/Parenting, r/college, and adjacent threads
- **Theme:** Teacher Touch Before AI Slop (mandated volume, policy hypocrisy, questioning gap in tutoring, Class 11 burnout)

## Image upload (image-function)
- **Slug:** `teacher-touch-before-ai-slop-nov-2026`
- **Local:** `clients/assets/eduhexa/eduhexa-message-teacher-touch-before-ai-slop-nov-2026.png`
- **imagePrompt:** `clients/assets/eduhexa/imagePrompt-eduhexa-message-teacher-touch-before-ai-slop-nov-2026.txt`
- **Status:** **FAILED** — `POST https://image-function-926896730665.europe-west1.run.app` returned HTTP 503 / 500 on multiple retries (base64 PNG and GitHub raw URL). Firebase `imageUrl` not obtained. Per workflow, image upload step blocked downstream Firestore save with production asset URL.

## Notion
- **Page:** https://app.notion.com/p/414c45f0da5d8109980dd568d1cf1ea5
- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)

## Firestore
- **Outlet:** `5qy4uU63AX6jLjDYvP19`
- **Primary endpoint:** `POST https://msg91whatspp-454181684966.europe-west1.run.app/ai-content` → HTTP 503/500 (retried twice)
- **Fallback endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content` → HTTP 500/503 (retried twice)
- **documentId:** *(not saved — APIs unavailable)*
- **title (prepared):** Teacher Touch Before AI Slop
- **slug (prepared):** `teacher-touch-before-ai-slop-nov-2026`
