# Swayam — Weekly cloud agent outputs

Artifacts written by [docs/swayam-weekly-automation.md](../swayam-weekly-automation.md) each run.

## Folder convention

One folder per run, named by **Monday of the week** (`YYYY-MM-DD`):

```
docs/swayam/weekly/{YYYY-MM-DD}/
├── research-notes.md
├── whatsapp-community.md
├── whatsapp-message.md
├── poll.md
├── thought-leadership.md
├── future-education.md
├── linkedin-post.md
├── on-poster-fields.json
├── {slug}.CREATIVE_DNA.json
├── {slug}-prompt.md
├── {slug}.png
└── publish-log.md
```

## `on-poster-fields.json` shape

```json
{
  "headline": "≤ 8 words",
  "stat": "73%",
  "subline": "Supporting line",
  "cta": "Short question or invite",
  "slug": "url-safe-slug",
  "template_doc_id": "Firestore doc id",
  "template_collection": "social-ai-poster"
}
```

## Image upload

Posters upload to GCS via `image-function` using base64 from `{slug}.png`. See `docs/swayam-weekly-automation.md`.

## Git

Commit weekly artifacts to `main` when the cloud run succeeds (poster PNG + publish-log at minimum).
