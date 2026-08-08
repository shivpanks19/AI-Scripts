# Publish Log — {YYYY-MM-DD}

**Run date:** {YYYY-MM-DD}  
**Outlet:** `{outletId}` (from webhook) ({display name})  
**Source:** `{firestore.source}`  
**Creative folder:** `{path/to/creative/folder}`  
**Status:** ⏳ Pending | ✅ Complete | ❌ Failed

---

## {slug}

### Phase 9b verification

| Check | Result |
| --- | --- |
| Local PNG | `{slug}.png` ✅ / ❌ |
| `documentId` | `{documentId}` ✅ |
| `collection` | `social-ai-poster` ✅ |
| `path` | `OUTLET/{outletId}/social-ai-poster/{documentId}` ✅ |
| `imageUrl` (GCS) | `{gcs_url}` ✅ |
| `slug` | `{slug}` ✅ |
| `title` | {title} ✅ |
| `showAsTemplate` | Not set (weekly draft) ✅ |
| Image text match | **PASS** / **FAIL** — {notes} |

### On-image copy lock

| Zone | Text |
| --- | --- |
| {role} | {exact text from prompt} |

### Image upload (Step 1 — image-function)

```json
{
  "success": true,
  "imageUrl": "{gcs_url}"
}
```

### Firestore publish (Step 2 — /ai-content)

```json
{
  "success": true,
  "documentId": "{documentId}",
  "outletId": "{outletId}",
  "collection": "social-ai-poster",
  "path": "OUTLET/{outletId}/social-ai-poster/{documentId}"
}
```

### Local artifacts

```
{creative_folder}/
├── {slug}.CREATIVE_DNA.json
├── {slug}-prompt.md
├── {slug}-post.md          # preferred (post-writer-sms)
├── {slug}-caption.md       # legacy or caption-writer platforms
├── {slug}.png
└── publish-log.md
```

### Notes

- {failures, retries, next actions}

---

## End summary (required when batch complete)

- Slugs published: {list}
- Firestore paths: {list}
- GCS URLs: {list}
- Verify: all PASS / {which failed}
