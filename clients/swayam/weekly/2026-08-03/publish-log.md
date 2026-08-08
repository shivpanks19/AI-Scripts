# Publish Log — 2026-08-03

**Run date:** 2026-08-03 (Monday of week)  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (Swayam / Infisoft Tech)  
**Source:** `swayam-automation`  
**Status:** ✅ Complete

---

## Phase 6 verification

| Check | Result |
| --- | --- |
| `documentId` | `qwb8zzwfWT9apz1OSMYK` ✅ |
| `collection` | `social-ai-poster` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/social-ai-poster/qwb8zzwfWT9apz1OSMYK` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786191237522-image.png` ✅ |
| `slug` | `leads-dont-wait-78-percent` ✅ |
| `title` | Leads Don't Wait — 78% First-Reply Insight ✅ |
| `showAsTemplate` | Not set (weekly draft) ✅ |
| Image text match | **PASS** — headline, stat, subline, CTA verified on PNG |

---

## Template selection

| Field | Value |
| --- | --- |
| `template_doc_id` | `0d434cec-4938-4e23-8dc8-878fddb11145` |
| `template_collection` | `social-ai-poster` |
| `template_title` | JEE 2026 Demo Class Launch |
| Rationale | Stat-led insight → editorial layout with hero stat badge zone |

---

## On-poster copy lock

| Field | Text |
| --- | --- |
| Headline | Leads Don't Wait |
| Stat | 78% |
| Subline | Families enroll with whoever replies first—not whoever has the best brochure. |
| CTA | How fast do you respond? |

---

## Notion

- **Parent:** Reddit EduHexa Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [Swayam Intelligence — Leads Don't Wait (28 July–4 August 2026)](https://app.notion.com/p/3b6c45f0da5d81fcb5d2d742bd747e79)
- **Page ID:** `3b6c45f0-da5d-81fc-b5d2-d742bd747e79`

---

## Firestore publish (5b)

```json
{
  "success": true,
  "documentId": "qwb8zzwfWT9apz1OSMYK",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "social-ai-poster",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/social-ai-poster/qwb8zzwfWT9apz1OSMYK"
}
```

---

## Image upload (4c)

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786191237522-image.png"
}
```

---

## Local artifacts

```
clients/swayam/weekly/2026-08-03/
├── research-notes.md
├── whatsapp-community.md
├── whatsapp-message.md
├── poll.md
├── thought-leadership.md
├── future-education.md
├── linkedin-post.md
├── on-poster-fields.json
├── leads-dont-wait-78-percent.CREATIVE_DNA.json
├── leads-dont-wait-78-percent-prompt.md
├── leads-dont-wait-78-percent.png
└── publish-log.md
```

---

## Notes

- `git pull origin main` skipped (auto-review blocked); branch was already on `main` and up to date with `origin/main`.
- Firestore template list via public REST API (3 templates in `social-ai-poster` with `showAsTemplate=true`).
- No git commit per runbook (commit only when user asks).
