# swayam — weekly Reddit & web community intelligence

**Role:** Swayam intelligence assistant for **Swayam** (vertical proof point for **Swayam** — agentic CRM). Position swayam as *a trusted voice discussing the problems people face when they are doing sales and marketing without any expert help or expert tool*, not a product pitch account.

**Research method:** Use **exa** and public Reddit URLs (`site:reddit.com`, `old.reddit.com/.../search.json`). Rewrite findings into original insights — never copy Reddit posts verbatim.

**Production outlet (Firestore `AI_CONTENT`):** `outletId = 5qy4uU63AX6jLjDYvP19` (swayam / Infisoft Tech). Never use a test outlet unless explicitly overridden.

---

## Weekly job — structured flow

Run phases **in order**. Do not generate the image before weekly copy exists.

```
Phase 1 Research → Phase 2 Content → Phase 3 Template → Phase 4 Image → Phase 5 Publish → Phase 6 Verify
```

### Phase 0 — Setup

| Item | Value |
| --- | --- |
| Outlet | `5qy4uU63AX6jLjDYvP19` (override only if user specifies) |
| Git (start of run) | `git checkout main && git pull origin main` |
| Commit artifacts | Only when the user asks |

---

### Phase 1 — Research

**Goal:** Find operator pain, trends, and discussion signals aligned with Swayam CRM capabilities.

**How**

1. Run **8–12 queries** per cycle (see [Web search query templates](#web-search-query-templates)).
2. Prefer **Tier A + B** subreddits for product-adjacent ops; use **Tier C** for sentiment that feeds WhatsApp copy (see [Subreddits](#subreddits--tiered-crm-aligned)).
3. Use the [CRM capability map](#map-crm-capabilities--what-to-listen-for-on-reddit) to filter signal vs noise.
4. Extract: major concerns, emotional patterns, emerging trends, controversial takes, operational failures, future opportunities.

**Output:** Research notes (original synthesis — not verbatim Reddit quotes).

---

### Phase 2 — Content creation

**Goal:** Produce this week’s creative assets in swayam voice **before** any image work.

**Deliverables** (original copy):

1. One WhatsApp **community discussion** post
2. One WhatsApp **message template** body (`swayam-message`) — pairs with the square image in Phase 4
3. One **poll**
4. One **thought-leadership** insight
5. One **future-of-education** observation
6. One **LinkedIn** post idea for swayam

**On-poster fields (required for Phase 4):** From items 2 and 4, define exactly:

| Field | Rule |
| --- | --- |
| `headline` | ≤ 8 words |
| `stat` | One sharp number or range |
| `subline` | Supporting line (may wrap) |
| `cta` | Short question or invite |

**Writing style:** Conversational WhatsApp tone — short lines, one link max, 0–1 emoji for India B2B; value-first. See `docs/whatsapp-skill.md` for length/compliance patterns.

**Output:** Full text for all six items **plus** the four on-poster fields above.

---

### Phase 3 — Template selection

**Goal:** Pick the best **layout plot** (visual shell) for this week’s content.

**How**

1. List template-flagged docs for the production outlet from Firestore:
   - `OUTLET/{outletId}/AI_CONTENT`
   - `OUTLET/{outletId}/social-ai-poster`
2. **Filter (mandatory):** only docs with **`showAsTemplate === true`** (legacy: `showInSocialPoster === true`).
3. **Choose wisely** — match visual format to this week’s insight (stat-led → data layout; opinion → quote layout; how-to → list layout).

**Read from chosen template**

| Field | Use for |
| --- | --- |
| `imagePrompt` / `prompt` | **Layout plot only** — composition, palette, typography zones; strip stale example headline/body |
| `imageUrl` | **Style reference only** — do **not** pass to image-function (see Phase 4) |
| `aspectRatio` | Inform local render palette/composition; enforce **1:1** on final output |

**Output:** One selected template + extracted layout plot fields (palette, zones, mood).

---

### Phase 4 — Image generation

**Goal:** Render a **1080×1080** poster with **exact on-poster copy** from Phase 2, then upload via image-function.

**Critical rule:** image-function reproduces reference `imageUrl` text when given a finished template thumbnail. **Always render locally first.**

#### Phase 4a — Local render (MANDATORY, before image-function)

```bash
python3 scripts/generate_swayam_image.py \
  --headline "<headline>" \
  --subline "<subline>" \
  --stat "<stat>" \
  --cta "<cta>" \
  --slug "<url-safe-slug>"
```

- Output: `docs/assets/swayam/{slug}.png` at **1080×1080**
- **Verify** visible text matches Phase 2 on-poster fields exactly (open the PNG or describe it)
- Template `imageUrl` is for palette/composition inspiration in the script only — **never** as `imageUrl` in the image-function POST

#### Phase 4b — Make local PNG publicly reachable

Push the asset to the working branch so `raw.githubusercontent.com` can serve it:

```bash
git add docs/assets/swayam/{slug}.png
git commit -m "Add swayam weekly poster {slug}"
git push -u origin <branch>
```

Public source URL pattern:

```
https://raw.githubusercontent.com/shivpanks19/AI-Scripts/<branch>/docs/assets/swayam/{slug}.png
```

Or use `scripts/publish_swayam_image.py` which orchestrates 4a + 4b + 4c.

#### Phase 4c — Upload via image-function (storage only)

`POST https://image-function-926896730665.europe-west1.run.app`

```json
{
  "imageUrl": "<public URL of locally rendered PNG from 4b>",
  "slug": "<url-safe slug from weekly title>",
  "prompt": "Upload this image to Firebase Storage exactly as provided. Preserve all visible text verbatim. Do not replace headline, stat, subline, or CTA. Minor compression only. Aspect ratio 1:1 1080x1080."
}
```

| Input | Source | Role |
| --- | --- | --- |
| **On-poster copy** | Phase 2 — headline, stat, subline, CTA | Rendered locally in 4a |
| **Layout plot** | Phase 3 — palette, zones, mood | Applied in `generate_swayam_image.py` styling |
| **imageUrl in POST** | Local PNG public URL | Upload source — **not** template thumbnail |

**Wrong:** pass template `imageUrl` to image-function and expect new text to appear.

**Right:** local PNG with correct text → image-function uploads to GCS unchanged.

**Output:** Generated `imageUrl` (GCS) + record of local path + merged `imagePrompt` (layout plot + weekly copy) for Firestore.

---

### Phase 5 — Publish

**Goal:** Persist research and assets to Notion and Firestore.

| Step | Action |
| --- | --- |
| 5a — Notion | Create child page under [Reddit swayam Research](https://app.notion.com/p/Reddit-swayam-Research-35bc45f0da5d81e6acd2e196888b3922) with research notes + all Phase 2 copy |
| 5b — Firestore | `POST …/ai-content` · header `x-api-key: hexa-ai-content-666` · `templateName: swayam_image_post_weekly` · `source: swayam-automation` |

**Firestore body (minimum)**

- `outletId`, `title`, `content`, `excerpt`
- **Merged** `imagePrompt` (layout plot + weekly copy from Phase 4)
- Generated `imageUrl` from Phase 4c (GCS URL, not local path)
- Do **not** set `showAsTemplate` on weekly drafts

---

### Phase 6 — Verify

**Goal:** Confirm ingestion succeeded.

Check response includes:

- [ ] `documentId`
- [ ] `imageUrl` (GCS URL from 4c, not template reference)
- [ ] `slug`
- [ ] `title`

**Image text check (mandatory):** Open GCS `imageUrl` and confirm headline, stat, and CTA match Phase 2. If text is wrong, do **not** mark Phase 4 complete — re-run from 4a.

---

## Reference — research context

### Map CRM capabilities → what to listen for on Reddit

| Swayam module | Operator pain on forums | Example discussion signals |
| --- | --- | --- |
| Leads + pipeline | Enquiries lost in spreadsheets / personal WhatsApp | “leads in Excel”, “pipeline stages”, “assign leads” |
| Activities + follow-up aging | Slow response, missed callbacks | “follow up”, “DNP”, “call queue”, “counsellor workload” |
| WhatsApp inbox + templates | Fragmented chats, no CRM history | “WhatsApp Business API”, “bulk message”, “personal number banned” |
| Meta Ads insights + UTM | Ad spend with no enrolment attribution | “Meta lead ads”, “CPL”, “which campaign converted” |
| CRM AI | Manual prioritisation, counsellor burnout | “prioritise callbacks”, “which leads to call first” |
| Agentic MCP | Stacks glued with Zaps | “automate WhatsApp from CRM”, “ad to enrolment” |
| Multi-outlet + permissions | Multi-branch coaching chains | “branch leads”, “franchise admissions” |

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
