# Swayam — Weekly Reddit & Web Community Intelligence

**Schedule:** Weekly (recommended Monday 07:00 IST)  
**Type:** Scheduled  
**Working directory:** `AI-Scripts` repo root  
**Default branch:** `main`  
**Git commit:** Only when the user explicitly asks — do not auto-commit weekly artifacts

---

## Cursor Cloud task (paste into scheduler)

**Name:** `swayam-weekly-reddit-creative`  
**Prompt (one line):**

```
Read and execute docs/swayam-weekly-automation.md for outlet 5qy4uU63AX6jLjDYvP19.
```

---

## Role

Swayam intelligence assistant for **Swayam** (agentic CRM). Position Swayam as *a trusted voice discussing the problems people face when doing sales and marketing without expert help or tools* — not a product-pitch account.

**Research method:** Use **Exa** and public Reddit URLs (`site:reddit.com`, `old.reddit.com/.../search.json`). Rewrite findings into original insights — never copy Reddit posts verbatim.

**Production outlet:** `outletId = 5qy4uU63AX6jLjDYvP19` (Swayam / Infisoft Tech). Never use a test outlet unless explicitly overridden.

**Firestore collections:**

| Purpose | Path | Notes |
|---------|------|-------|
| Templates (read) | `OUTLET/{outletId}/AI_CONTENT` and `OUTLET/{outletId}/social-ai-poster` | Filter `showAsTemplate === true` (legacy: `showInSocialPoster === true`) |
| Weekly drafts (write) | `OUTLET/{outletId}/social-ai-poster` | Pass `"collection": "social-ai-poster"` on every `POST …/ai-content` |

Allowed `collection` values on ingest: **`AI_CONTENT`**, **`social-ai-poster`** only (not `ai-posters`).

---

## Skills & pipeline integration

This agent follows the **brand → creative pipeline** pattern: Firestore template = layout DNA, weekly copy = variable slots, `modifiedImagePrompt` = merged prompt.

### Always read (static — do not regenerate weekly)

| File | Use |
|------|-----|
| `docs/swayam-weekly-automation.md` | This runbook |
| `docs/whatsapp-skill.md` | WhatsApp length, tone, compliance patterns |
| `docs/swayam/weekly/README.md` | Weekly artifact layout |

**Brand design:** Colors, typography, and layout zones come from the selected Firestore template `imagePrompt`. Enforce Swayam voice: confident operator, revenue-first, value-not-pitch. Product: agentic CRM for Meta ads + WhatsApp + pipeline (swayamapp.com).

### Per-phase tools

| Phase | Tool / doc |
|-------|------------|
| 1 | Exa + Reddit search; never copy posts verbatim |
| 2 | `docs/whatsapp-skill.md` for community + message template tone |
| 3–4 | Firestore template pick + Creative DNA merge (below) |
| 5a | Notion MCP — child page under Reddit Swayam Research |

### Phase mapping (cloud ↔ pipeline)

| Cloud phase | Pipeline equivalent |
|-------------|---------------------|
| 1 Research | New input — feeds copy |
| 2 Content | Copy phase |
| 3 Template | Template selection |
| 4a Prompt | Prompt merge |
| 4b Image | Image generation |
| 4c–6 Publish/verify | Publish infra |

**Hard gate:** Phase 2 must complete before any image work.

**Optional (if performance-marketing-agency repo is also available):** `clients/swayam/BRAND_DNA.json`, `brand-social-creative-pipeline` skill, `post-writer-sms` / `caption-writer-sms`.

---

## Weekly artifacts (canonical paths)

All outputs for run date `{YYYY-MM-DD}` (Monday of the week):

```
docs/swayam/weekly/{YYYY-MM-DD}/
├── research-notes.md
├── whatsapp-community.md
├── whatsapp-message.md
├── poll.md
├── thought-leadership.md
├── future-education.md
├── linkedin-post.md
├── on-poster-fields.json          # headline, stat, subline, cta
├── {slug}.CREATIVE_DNA.json       # ephemeral; from Firestore template + weekly copy
├── {slug}-prompt.md               # modifiedImagePrompt + merge notes
├── {slug}.png                     # AI-generated poster
└── publish-log.md                 # Firestore docIds, GCS URLs, verify status
```

See [docs/swayam/weekly/README.md](../../docs/swayam/weekly/README.md).

---

## Image upload — canonical host

**Primary (this repo):** Save PNG to `docs/swayam/weekly/{YYYY-MM-DD}/{slug}.png`. Legacy one-off posters may also use `docs/assets/swayam/{slug}.png`.

**Upload to GCS:** `POST https://image-function-926896730665.europe-west1.run.app`

Preferred method — **base64 data URL** (no separate GitHub push required):

```json
{
  "imageUrl": "data:image/png;base64,{base64_of_png}",
  "slug": "{url-safe-slug}",
  "prompt": "Upload this image to Firebase Storage exactly as provided. Preserve all visible text verbatim. Do not replace headline, stat, subline, or CTA. Minor compression only. Aspect ratio 1:1 1080x1080."
}
```

**Fallback — raw GitHub URL** (only if base64 fails):

```
https://raw.githubusercontent.com/shivpanks19/performance-marketing-agency/{branch}/docs/swayam/weekly/{YYYY-MM-DD}/{slug}.png
```

**Never** pass the Firestore template `imageUrl` as the upload source to image-function — that reproduces baked-in template text. Template `imageUrl` is style reference only in Phase 4b.

---

## Weekly job — structured flow

Run phases **in order**. Do not generate the image before weekly copy exists.

```
Phase 0 Setup → Phase 1 Research → Phase 2 Content → Phase 3 Template → Phase 4 Image → Phase 5 Publish → Phase 6 Verify
```

---

### Phase 0 — Setup

| Item | Value |
| --- | --- |
| Outlet | `5qy4uU63AX6jLjDYvP19` (override only if user specifies) |
| Git (start of run) | `git checkout main && git pull origin main` |
| Weekly folder | `docs/swayam/weekly/{YYYY-MM-DD}/` |
| Commit artifacts | Only when the user asks |

---

### Phase 1 — Research

**Goal:** Find operator pain, trends, and discussion signals aligned with Swayam CRM capabilities.

**How**

1. Run **8–12 queries** per cycle (see [Web search query templates](#web-search-query-templates)).
2. Prefer **Tier A + B** subreddits for product-adjacent ops; use **Tier C** for sentiment that feeds WhatsApp copy.
3. Use the [CRM capability map](#map-crm-capabilities--what-to-listen-for-on-reddit) to filter signal vs noise.
4. Extract: major concerns, emotional patterns, emerging trends, controversial takes, operational failures, future opportunities.

**Output:** `docs/swayam/weekly/{YYYY-MM-DD}/research-notes.md` (original synthesis — not verbatim Reddit quotes).

---

### Phase 2 — Content creation

**Goal:** Produce this week's creative assets in Swayam voice **before** any image work.

**Deliverables** (original copy):

1. One WhatsApp **community discussion** post → `whatsapp-community.md`
2. One WhatsApp **message template** body (`swayam-message`) → `whatsapp-message.md` — pairs with square image in Phase 4
3. One **poll** → `poll.md`
4. One **thought-leadership** insight → `thought-leadership.md`
5. One **future-of-education** observation → `future-education.md`
6. One **LinkedIn** post idea → `linkedin-post.md`

**On-poster fields (required for Phase 4):** From items 2 and 4, define exactly and save to `on-poster-fields.json`:

| Field | Rule |
| --- | --- |
| `headline` | ≤ 8 words |
| `stat` | One sharp number or range |
| `subline` | Supporting line (may wrap) |
| `cta` | Short question or invite |

**Writing style:** Conversational WhatsApp tone — short lines, one link max, 0–1 emoji for India B2B; value-first. Match `docs/whatsapp-skill.md` patterns; Swayam voice = trusted operator on sales/marketing ops pain, not product pitch.

---

### Phase 3 — Template selection

**Goal:** Pick the best **layout plot** (visual shell) for this week's content.

**How**

1. List template-flagged docs for the production outlet from Firestore:
   - `OUTLET/{outletId}/AI_CONTENT`
   - `OUTLET/{outletId}/social-ai-poster`
2. **Filter (mandatory):** only docs with **`showAsTemplate === true`** (legacy: `showInSocialPoster === true`).
3. **Choose wisely** — match visual format to this week's insight (stat-led → data layout; opinion → quote layout; how-to → list layout).

**Read from chosen template**

| Field | Use for |
| --- | --- |
| `imagePrompt` / `prompt` | **Base generation prompt** — keep design, formatting, palette, typography, layout zones, brand mood |
| `imageUrl` | Optional **visual reference** when generating in Phase 4b — do **not** pass to image-function as upload source |
| `aspectRatio` | Carry into modified prompt; enforce **1:1** (1080×1080) on final output unless brief overrides |

**Template selection heuristic**

| This week's insight | Pick template with |
|---------------------|-------------------|
| Stat-led pain (e.g. follow-up delay %) | `stat-hero`, `stat_card` zone |
| Operator opinion / myth-bust | quote or myth-truth layout |
| Process / how-to | list or split-comparison |
| Product proof (Social AI Poster) | studio/split layout with brief-in → poster-out panels |

Past Firestore templates flagged `showAsTemplate` in the same outlet are the reference set when titles are ambiguous.

**Output:** One selected template + full outlet `imagePrompt` / `prompt` text + `template_doc_id` recorded in weekly folder.

---

### Firestore template → ephemeral Creative DNA

After template pick, build `{slug}.CREATIVE_DNA.json` in the weekly folder:

```json
{
  "_meta": {
    "source": "firestore-template",
    "template_doc_id": "…",
    "template_collection": "social-ai-poster",
    "brand_source": "firestore-template-imagePrompt"
  },
  "canvas": { "ratio": "1:1", "width": 1080, "height": 1080 },
  "structure_type": "inferred-from-template-prompt",
  "composition": { "zones": "parsed from template imagePrompt headings" },
  "elements": [
    { "type": "headline", "content": "{headline}" },
    { "type": "stat", "content": "{stat}" },
    { "type": "subline", "content": "{subline}" },
    { "type": "cta", "content": "{cta}" }
  ],
  "copy": { "cta": "{cta}" }
}
```

**Merge rule:**

```
modifiedImagePrompt = template brand tokens from imagePrompt (colors, fonts, layout)
                    + Firestore template imagePrompt (layout, zones, mood)
                    − template placeholder copy
                    + Phase 2 on-poster fields (exact text lock)
                    + render rules block (below)
```

---

### Phase 4 — Image generation

**Goal:** Build `modifiedImagePrompt`, generate poster with AI, upload via image-function.

**Critical rules**

- **Never** pass the raw outlet `imagePrompt` unchanged — it contains stale example copy.
- **Never** pass the template `imageUrl` to image-function as `imageUrl`.
- Generate the image in Phase 4b — not a Python render script (unless fallback).

#### Phase 4a — Build modified generation prompt (MANDATORY)

1. **Keep** design/formatting: canvas, palette, gradients, typography, layout zones, decorative elements, brand/footer, mood.
2. **Remove** placeholder/example copy from the template prompt.
3. **Insert** Phase 2 on-poster fields as the only visible text.
4. **Append** render rules:

```
All visible on-poster text must be exactly:
- Headline: "{headline}"
- Stat: "{stat}"
- Subline: "{subline}"
- CTA: "{cta}"

Do not reuse any placeholder wording from the original template prompt.
Preserve the original template's design system, layout structure, colors, and typography placement.
Aspect ratio: 1:1. 1080×1080.
```

Save verbatim to `{slug}-prompt.md` and use as Firestore `imagePrompt` in Phase 5.

#### Phase 4b — AI image generation

- Call **GenerateImage** with full `modifiedImagePrompt`.
- Optional: template `imageUrl` as **style reference** only.
- Save to `docs/swayam/weekly/{YYYY-MM-DD}/{slug}.png` at **1080×1080**.
- **Verify** visible text matches Phase 2 fields. On mismatch, revise prompt and regenerate — do not proceed to 4c.

#### Phase 4c — Upload via image-function

POST `https://image-function-926896730665.europe-west1.run.app` with base64 PNG (see [Image upload](#image-upload--canonical-host)).

**Optional fallback:** Regenerate with stricter copy-lock language in the prompt if AI text verification fails twice.

---

### Phase 5 — Publish

| Step | Action |
| --- | --- |
| 5a — Notion | Create child page under [Reddit Swayam Research](https://app.notion.com/p/Reddit-swayam-Research-35bc45f0da5d81e6acd2e196888b3922) with research notes + all Phase 2 copy |
| 5b — Firestore | `POST https://crm-demo-2fc0c.web.app/ai-content` · header `x-api-key: hexa-ai-content-666` · `collection: social-ai-poster` · `templateName: swayam_image_post_weekly` · `source: swayam-automation` |

**Firestore body (minimum)**

- `outletId`, `collection` (`"social-ai-poster"`), `title`, `content`, `excerpt`
- **Merged** `imagePrompt` (`modifiedImagePrompt` from Phase 4a)
- Generated `imageUrl` from Phase 4c (GCS URL, not template reference)
- `slug` (url-safe slug from weekly title)
- Do **not** set `showAsTemplate` on weekly drafts

Update `publish-log.md` with response fields.

---

### Phase 6 — Verify

Confirm response includes:

- [ ] `documentId`
- [ ] `collection` (`social-ai-poster`)
- [ ] `path` (`OUTLET/{outletId}/social-ai-poster/{documentId}`)
- [ ] `imageUrl` (GCS URL from 4c)
- [ ] `slug`
- [ ] `title`

**Image text check (mandatory):** Confirm headline, stat, subline, and CTA on the GCS image match Phase 2. If wrong, do not mark complete — revise `modifiedImagePrompt` and regenerate.

---

## Reference — research context

### Map CRM capabilities → what to listen for on Reddit

| Swayam module | Operator pain on forums | Example discussion signals |
| --- | --- | --- |
| Leads + pipeline | Enquiries lost in spreadsheets / personal WhatsApp | "leads in Excel", "pipeline stages", "assign leads" |
| Activities + follow-up aging | Slow response, missed callbacks | "follow up", "DNP", "call queue", "counsellor workload" |
| WhatsApp inbox + templates | Fragmented chats, no CRM history | "WhatsApp Business API", "bulk message", "personal number banned" |
| Meta Ads insights + UTM | Ad spend with no enrolment attribution | "Meta lead ads", "CPL", "which campaign converted" |
| CRM AI | Manual prioritisation, counsellor burnout | "prioritise callbacks", "which leads to call first" |
| Agentic MCP | Stacks glued with Zaps | "automate WhatsApp from CRM", "ad to enrolment" |
| Multi-outlet + permissions | Multi-branch coaching chains | "branch leads", "franchise admissions" |

### Subreddits — tiered (CRM-aligned)

**Tier A:** r/edtech, r/highereducation, r/k12sysadmin, r/schoolcounselors, r/smallbusiness, r/digital_marketing, r/Entrepreneur, r/startups

**Tier B:** r/Indian_Academia, r/IndiaEducation, r/CBSE, r/JEENEETards, r/Btechtards, r/NEETprep, r/CATpreparation, r/IndianTeenagers

**Tier C:** r/Teachers, r/education, r/Professors, r/Parenting, r/college, r/ApplyingToCollege, r/GradSchool

**Tier D (rotate):** r/SaaS, r/india, r/developersIndia, r/FacebookAds

### Web search query templates

```
site:reddit.com r/edtech admissions CRM pipeline WhatsApp
site:reddit.com r/edtech Meta lead ads coaching institute
site:reddit.com r/smallbusiness coaching institute leads WhatsApp follow up
site:reddit.com r/digital_marketing click to WhatsApp lead ads education
site:reddit.com r/highereducation enrollment CRM software
site:reddit.com r/k12sysadmin admissions software enquiry management
site:reddit.com r/Indian_Academia coaching institute admission
site:reddit.com r/JEENEETards coaching centre worth it OR admission
site:reddit.com r/Teachers AI classroom cheating detection OR Chromebook
reddit counselling leads spreadsheet coaching institute India
reddit school admission enquiry response time parent WhatsApp
coaching institute India leads WhatsApp CRM follow up 2026
school admission enquiry pipeline counsellor assignment India
Meta lead ads WhatsApp automation coaching institute India
edtech admissions CRM lost leads counsellor
```

---

## Weekly run checklist

```
- [ ] Phase 0: git pull; confirm outlet 5qy4uU63AX6jLjDYvP19; create weekly/{YYYY-MM-DD}/
- [ ] Phase 1: 8–12 Exa/Reddit queries; write research-notes.md
- [ ] Phase 2: 6 copy items + on-poster-fields.json
- [ ] Phase 3: list Firestore templates; pick layout; record template_doc_id; write {slug}.CREATIVE_DNA.json
- [ ] Phase 4a: modifiedImagePrompt → {slug}-prompt.md
- [ ] Phase 4b: GenerateImage 1:1; verify on-image text
- [ ] Phase 4c: POST image-function; capture GCS imageUrl
- [ ] Phase 5a: Notion child page
- [ ] Phase 5b: POST /ai-content → social-ai-poster
- [ ] Phase 6: documentId, path, slug, image text match; update publish-log.md
```

**Estimated wall time:** ~12–15 min.

---

## End summary (required each run)

- Week date folder path
- Research themes (3 bullets)
- On-poster copy lock (headline, stat, subline, cta)
- Template doc ID chosen
- GCS `imageUrl` + Firestore `path`
- Notion page URL
- Verify pass/fail on image text
- Failures or next actions
