# Publish Log — 2026-08-08

**Run date:** 2026-08-08  
**Outlet:** `5qy4uU63AX6jLjDYvP19` (Swayam / Infisoft Tech)  
**Source:** `swayam-automation`  
**Status:** ✅ Complete

---

## Phase 6 verification

| Check | Result |
| --- | --- |
| `documentId` | `PWQSINgjC3t60aPp9owW` ✅ |
| `collection` | `social-ai-poster` ✅ |
| `path` | `OUTLET/5qy4uU63AX6jLjDYvP19/social-ai-poster/PWQSINgjC3t60aPp9owW` ✅ |
| `imageUrl` (GCS) | `https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786192681015-image.png` ✅ |
| `slug` | `paid-leads-leak-15-30-percent` ✅ |
| `title` | Swayam Intelligence — Paid Leads Leak (4–11 August 2026) ✅ |
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
| Headline | Paid Leads Leak |
| Stat | 15-30% |
| Subline | They die in the assignment queue—not in your ad funnel. |
| CTA | Who owns new enquiries? |

---

## Notion

- **Parent:** Reddit Swayam Research (`35bc45f0da5d81e6acd2e196888b3922`)
- **Child page:** [Swayam Intelligence — Paid Leads Leak (4–11 August 2026)](https://app.notion.com/p/3b6c45f0da5d81498e7ecf96e3c74a93)
- **Page ID:** `3b6c45f0-da5d-8149-8e7e-cf96e3c74a93`

---

## Firestore publish (5b)

```json
{
  "success": true,
  "documentId": "PWQSINgjC3t60aPp9owW",
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "social-ai-poster",
  "path": "OUTLET/5qy4uU63AX6jLjDYvP19/social-ai-poster/PWQSINgjC3t60aPp9owW"
}
```

---

## Image upload (4c)

```json
{
  "success": true,
  "imageUrl": "https://storage.googleapis.com/crm-demo-2fc0c.firebasestorage.app/eduhexa/1786192681015-image.png"
}
```

---

## Local artifacts

```
clients/swayam/weekly/2026-08-08/
├── research-notes.md
├── whatsapp-community.md
├── whatsapp-message.md
├── poll.md
├── thought-leadership.md
├── future-education.md
├── linkedin-post.md
├── on-poster-fields.json
├── paid-leads-leak-15-30-percent.CREATIVE_DNA.json
├── paid-leads-leak-15-30-percent-prompt.md
├── paid-leads-leak-15-30-percent.png
└── publish-log.md
```

---

## Notes

- Exa MCP rate-limited; research via WebSearch fallback (industry blogs, operator reports).
- Firestore template list via public REST API (2 templates with `showAsTemplate=true`; used `0d434cec` stat-hero layout).
- Image generated at 1024×1024 (close to 1080×1080 target); text verified PASS.
