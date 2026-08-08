---
name: firestore-creative-publish
description: >-
  Upload generated PNGs to GCS via image-function and publish weekly social
  creatives to Firestore OUTLET/{outletId}/social-ai-poster (Swayam Phase 4c + 5b).
  Run immediately after Phase 9 image generation in brand-social-creative-pipeline.
  outletId comes from the triggering webhook (or explicit run prompt) — not client.json.
  Use when saving pipeline creatives to CRM or Social AI Poster.
---

# Firestore Creative Publish

Runs **immediately after Phase 9** (`{slug}.png` exists). Mirrors [Swayam weekly automation Phase 4c + 5b + 6](../../../../clients/swayam/swayam-weekly-automation.md#phase-5--publish).

**Pipeline position:** Phase **9b** — after `{slug}.png` is saved, before Phase 10 handoff.

**Downstream:** Social AI Poster UI reads `OUTLET/{outletId}/social-ai-poster/{documentId}`.

---

## Inputs

| Input | Path / source | Required |
|-------|---------------|----------|
| Generated PNG | `{creative_folder}/{slug}.png` | Yes |
| Prompt | `{creative_folder}/{slug}-prompt.md` | Yes |
| Post copy | `{creative_folder}/{slug}-post.md` (preferred) or `{slug}-caption.md` (legacy / TikTok) | Yes |
| Creative DNA | `{creative_folder}/{slug}.CREATIVE_DNA.json` | Recommended |
| **Outlet ID** | **Webhook payload** `outletId` (or `outlet_id`) | Yes |
| Run metadata | Webhook, user prompt, calendar row, or folder date | Yes |

**Creative folder examples:**

- Pipeline: `clients/{client_slug}/instagram/{YYYY-MM-DD}/`
- Swayam weekly: `clients/swayam/weekly/{YYYY-MM-DD}/`

---

## Webhook context (outlet + publish metadata)

`outletId` is **not** stored in `client.json`. It is supplied by the **triggering webhook** when the pipeline run starts.

### Expected webhook fields

```json
{
  "outletId": "5qy4uU63AX6jLjDYvP19",
  "collection": "social-ai-poster",
  "templateName": "swayam_image_post_weekly",
  "source": "brand-social-creative-pipeline"
}
```

| Field | Required | Default if omitted |
|-------|----------|-------------------|
| `outletId` / `outlet_id` | **Yes** | — (stop publish) |
| `collection` | No | `social-ai-poster` |
| `templateName` | No | Derive from client slug: `{slug}_image_post_weekly` (e.g. `eduhexa_image_post_weekly`) |
| `source` | No | `brand-social-creative-pipeline` |

### Resolution order for `outletId`

1. **Webhook payload** — primary source (`outletId` or `outlet_id`)
2. **Explicit run prompt** — e.g. cloud scheduler: `… for outlet 5qy4uU63AX6jLjDYvP19` (Swayam weekly pattern)
3. **Stop** — do not guess, do not read from `client.json`

Persist the resolved `outletId` in `publish-log.md` for the run audit trail only.

**Example reference outlets (webhook values, not client config):**

| Brand | Typical `outletId` | Typical `templateName` |
|-------|-------------------|------------------------|
| Swayam | `5qy4uU63AX6jLjDYvP19` | `swayam_image_post_weekly` |
| EduHexa | *(from webhook)* | `eduhexa_image_post_weekly` |

---

## Firestore paths

| Purpose | Path |
|---------|------|
| Templates (read only) | `OUTLET/{outletId}/AI_CONTENT`, `OUTLET/{outletId}/social-ai-poster` where `showAsTemplate === true` |
| Weekly drafts (write) | `OUTLET/{outletId}/social-ai-poster` |

Allowed `collection` on `POST /ai-content`: **`AI_CONTENT`**, **`social-ai-poster`** only.

**Never** set `showAsTemplate: true` on weekly pipeline drafts.

---

## Outputs

Per creative folder:

```
{creative_folder}/
├── publish-log.md              # append or create — one section per slug
└── firestore-publish-{slug}.json   # optional — raw API responses
```

Update `publish-log.md` from [publish-log.template.md](./publish-log.template.md).

---

## Procedure

Run **per `{slug}.png`** generated in Phase 9. Do not batch-upload before verifying each PNG exists.

### Step 0 — Preflight

1. Resolve `outletId` from **webhook payload** (or explicit run prompt). **Stop** if missing — do not publish to a guessed outlet.
2. Resolve `collection`, `templateName`, `source` from webhook (apply defaults above if omitted).
3. Confirm files exist: `{slug}.png`, `{slug}-prompt.md`, and post copy via resolution below.
4. **Resolve post copy file** (Phase 7 output):

```bash
# Prefer post-writer-sms output (Instagram, Facebook, LinkedIn)
if [ -f "${FOLDER}/${SLUG}-post.md" ]; then
  COPY_FILE="${FOLDER}/${SLUG}-post.md"
elif [ -f "${FOLDER}/${SLUG}-caption.md" ]; then
  COPY_FILE="${FOLDER}/${SLUG}-caption.md"   # legacy or caption-writer platforms
else
  echo "Missing ${SLUG}-post.md or ${SLUG}-caption.md"; exit 1
fi
```

5. Read prompt file → extract on-image copy lock for verification later.
6. Confirm PNG is the **generated** asset — not a Pinterest reference or Firestore template `imageUrl`.

### Step 1 — Upload PNG to GCS (Phase 4c equivalent)

**Endpoint:** `POST https://image-function-926896730665.europe-west1.run.app`

**Preferred body** — base64 data URL (no GitHub push required):

```json
{
  "imageUrl": "data:image/png;base64,{BASE64_OF_PNG}",
  "slug": "{url-safe-slug}",
  "prompt": "Upload this image to Firebase Storage exactly as provided. Preserve all visible text verbatim. Do not replace headline, stat, subline, or CTA. Minor compression only. Aspect ratio 1:1 1080x1080."
}
```

**Shell (from repo root):**

```bash
SLUG="behaviour-engagement-stat"
PNG="clients/eduhexa/instagram/2026-08-11/${SLUG}.png"
B64=$(base64 -i "$PNG" | tr -d '\n')

curl -sS -X POST "https://image-function-926896730665.europe-west1.run.app" \
  -H "Content-Type: application/json" \
  -d "$(jq -n \
    --arg b64 "$B64" \
    --arg slug "$SLUG" \
    '{
      imageUrl: ("data:image/png;base64," + $b64),
      slug: $slug,
      prompt: "Upload this image to Firebase Storage exactly as provided. Preserve all visible text verbatim. Do not replace headline, stat, subline, or CTA. Minor compression only. Aspect ratio 1:1 1080x1080."
    }')"
```

**Capture:** `imageUrl` from response (GCS HTTPS URL). **Fail** if missing.

**Never** pass a Firestore template `imageUrl` as upload source — that bakes in stale template text.

**Fallback:** raw GitHub URL to committed PNG — only if base64 fails:

```
https://raw.githubusercontent.com/{org}/{repo}/{branch}/{path-to-png}
```

### Step 2 — Build Firestore payload (Phase 5b)

**Endpoint:** `POST https://crm-demo-2fc0c.web.app/ai-content`  
**Header:** `x-api-key: hexa-ai-content-666`  
**Content-Type:** `application/json`

**Minimum body** (see [ai-content-payload.template.json](./ai-content-payload.template.json)):

| Field | Source |
|-------|--------|
| `outletId` | Webhook `outletId` / `outlet_id` (or explicit run prompt) |
| `collection` | Webhook `collection` (default `social-ai-poster`) |
| `title` | Calendar topic or first line of caption (human-readable) |
| `content` | Full resolved post copy file (`{slug}-post.md` preferred, else `{slug}-caption.md`) |
| `excerpt` | First 1–2 sentences of post copy |
| `imagePrompt` | Full text from `{slug}-prompt.md` (Generation prompt section) |
| `imageUrl` | GCS URL from Step 1 — **not** template reference |
| `slug` | `{slug}` (url-safe, matches filename) |
| `templateName` | Webhook `templateName` (or `{client_slug}_image_post_weekly`) |
| `source` | Webhook `source` (default `brand-social-creative-pipeline`) |

**Do not include:** `showAsTemplate`, template placeholder copy, or Pinterest reference URLs as `imageUrl`.

**Shell:**

```bash
OUTLET_ID="${WEBHOOK_OUTLET_ID}"   # from webhook payload — not client.json
SLUG="paid-leads-leak-15-30-percent"
FOLDER="clients/swayam/weekly/2026-08-08"
GCS_URL="https://storage.googleapis.com/..."

curl -sS -X POST "https://crm-demo-2fc0c.web.app/ai-content" \
  -H "Content-Type: application/json" \
  -H "x-api-key: hexa-ai-content-666" \
  -d "$(jq -n \
    --arg outletId "$OUTLET_ID" \
    --arg slug "$SLUG" \
    --arg imageUrl "$GCS_URL" \
    --arg imagePrompt "$(cat "${FOLDER}/${SLUG}-prompt.md")" \
    --arg content "$(cat "${FOLDER}/${SLUG}-post.md" 2>/dev/null || cat "${FOLDER}/${SLUG}-caption.md" 2>/dev/null || echo "")" \
    --arg title "Swayam Intelligence — Paid Leads Leak (4–11 August 2026)" \
    --arg excerpt "Paid leads do not die in your ad funnel." \
    --arg templateName "swayam_image_post_weekly" \
    --arg source "swayam-automation" \
    '{
      outletId: $outletId,
      collection: "social-ai-poster",
      slug: $slug,
      title: $title,
      content: $content,
      excerpt: $excerpt,
      imagePrompt: $imagePrompt,
      imageUrl: $imageUrl,
      templateName: $templateName,
      source: $source
    }')"
```

### Step 3 — Verify response (Phase 6 equivalent)

Confirm JSON response includes:

- [ ] `success` === true (or `documentId` present)
- [ ] `documentId`
- [ ] `collection` === `social-ai-poster` (or configured collection)
- [ ] `path` === `OUTLET/{outletId}/social-ai-poster/{documentId}`
- [ ] `imageUrl` === GCS URL from Step 1
- [ ] `slug` === `{slug}`

**Image text check:** Visually confirm on-image copy in PNG matches prompt copy-lock table. If mismatch → do **not** mark complete; revise prompt and re-run Phase 9, then republish.

### Step 4 — Write publish log

Append to `{creative_folder}/publish-log.md`:

- Run date, webhook `outletId`, slug
- GCS `imageUrl`, Firestore `documentId`, `path`
- Verify pass/fail on image text
- Raw responses (optional) → `firestore-publish-{slug}.json`

---

## Pipeline integration

When `brand-social-creative-pipeline` Phase 9 completes for a slug:

```
Webhook → outletId (+ optional publish metadata)
Phase 9  → {slug}.png saved locally
Phase 9b → this skill (upload + Firestore + verify + publish-log)
Phase 10 → handoff summary includes documentId + path
```

**Skip Phase 9b only when:**

- User says "local only" or "do not publish"
- Webhook (and run prompt) did not include `outletId`

**Swayam weekly automation:** Phase 4c + 5b + 6 should invoke this skill; outlet comes from scheduler prompt (`for outlet …`) as webhook-equivalent input.

---

## Error handling

| Failure | Action |
|---------|--------|
| Missing `outletId` in webhook / prompt | Stop; do not publish to wrong outlet |
| image-function 4xx/5xx | Retry base64 once; then try GitHub raw URL if committed |
| `/ai-content` rejects payload | Log body; check `collection` and required fields |
| GCS URL missing in response | Do not POST to Firestore |
| Text mismatch on PNG | Regenerate image; do not publish wrong copy |

---

## Security

- API key `hexa-ai-content-666` is shared ingest key — do not commit additional secrets.
- Never publish unless `outletId` came from webhook or an explicit authorized run prompt.

---

## See also

- [clients/swayam/swayam-weekly-automation.md](../../../../clients/swayam/swayam-weekly-automation.md) — canonical weekly runbook
- [clients/swayam/weekly/2026-08-08/publish-log.md](../../../../clients/swayam/weekly/2026-08-08/publish-log.md) — example verify log
- [../file-structure.md](../file-structure.md) — creative folder layout
- [ai-content-payload.template.json](./ai-content-payload.template.json)
- [publish-log.template.md](./publish-log.template.md)
