# Brand Social Pipeline — Webhook Automation Prompt

**Cursor Automation instructions** (paste into webhook-triggered cloud agent).  
**Repo branch:** `brand-gdrive` (do not create a new branch).  
**Storage:** Google Drive MCP — not repo `clients/`.

---

You were triggered by a webhook. Read the full webhook payload first before doing anything else.

You are in the AI-Scripts repo on branch **brand-gdrive**. Do not create a new branch. Do not switch to `main`.

## Webhook intake (Phase 0)

Parse these fields from the webhook payload. If a field is missing, use the fallback noted.

| Field | Required | Use |
|-------|----------|-----|
| website | Yes | Fetch and analyze the site |
| client_slug | No | Folder under `gdrive/clients/`; derive from domain if omitted (e.g. eduhexa.in → eduhexa) |
| platforms | Yes | e.g. `["instagram"]`, `["instagram","linkedin"]` |
| calendar | Yes | `weekly` or `monthly` |
| calendar_start_date | No | ISO date for first calendar week folder (e.g. 2026-08-11); default = next Monday from run date |
| brand_brief | No | Inline text — merge with site research |
| brand_brief_url | No | Fetch and merge if brand_brief is empty or short |
| reference_files | No | Array of URLs — download decks/PDFs/images and use as brand inputs |
| reference_file_url | No | Single-file alias for reference_files[0] |
| pinterest_urls | No | If ≥3 URLs: fetch those pins; if empty: run Pinterest auto-fetch (Phase 1b) |
| goals | No | Awareness, leads, demos, etc. |
| mode | No | `full` (default) or `dry_run` (Phases 0–8 only; skip Phase 9 image generation) |
| skip_phases | No | Array of phase numbers to skip if client already bootstrapped (e.g. `[1,"1b",5]`) |
| outletId | No | If present: run Phase 9b Firestore publish after each PNG |

Do not ask clarifying questions — the webhook payload is the intake. Proceed with best-effort defaults.

## Storage — Google Drive (mandatory)

All client artifacts are saved on **Google Drive**, not in the git repo.

| Setting | Value |
|---------|-------|
| MCP server | `google-drive` (`plugin-google-drive-google-drive`) |
| Root folder ID | `1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ` |
| Root URL | https://drive.google.com/drive/folders/1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ |
| Path prefix | `gdrive/clients/{client_slug}/` |

Use Google Drive MCP for all read/write/create-folder operations.  
Read [skills/brand-social-creative-pipeline/references/google-drive-storage.md](../skills/brand-social-creative-pipeline/references/google-drive-storage.md) before Phase 0.

**Do not** write pipeline outputs under `clients/` in the git repo. Legacy repo `clients/` is read-only reference only.

## Runbook — read and follow in order

1. [skills/brand-social-creative-pipeline/SKILL.md](../skills/brand-social-creative-pipeline/SKILL.md) — master pipeline; execute all applicable phases in order.
2. [skills/brand-social-creative-pipeline/references/google-drive-storage.md](../skills/brand-social-creative-pipeline/references/google-drive-storage.md) — Drive root, MCP ops, path notation.
3. [skills/brand-social-creative-pipeline/references/file-structure.md](../skills/brand-social-creative-pipeline/references/file-structure.md) — folder and naming conventions (Drive paths).
4. [skills/brand-social-creative-pipeline/references/pinterest-reference-fetch/SKILL.md](../skills/brand-social-creative-pipeline/references/pinterest-reference-fetch/SKILL.md) — Phase 1b (or use `pinterest_urls` from payload).
5. [skills/brand-social-creative-pipeline/references/prompt-merge.md](../skills/brand-social-creative-pipeline/references/prompt-merge.md) — Phase 8 color merge rules.
6. Reference example: `gdrive/clients/swayam/` on Drive; repo example shape in [skills/brand-social-creative-pipeline/references/example-swayam.md](../skills/brand-social-creative-pipeline/references/example-swayam.md).

## Execute pipeline

Run brand-social-creative-pipeline Phases 0–10 using webhook intake as Phase 0 inputs. All paths below are on **Google Drive** (`gdrive/clients/{client_slug}/`):

- **Phase 0:** Scaffold `gdrive/clients/{client_slug}/` + `client.json` (from [templates/client.json.template](../skills/brand-social-creative-pipeline/templates/client.json.template)); copy schemas from repo `templates/` to Drive.
- **Phase 1:** `BRAND_IDENTITY.md` (skill: design-brand-guardian)
- **Phase 1b:** `references/pinterest/{run_date}/` — 5 pins + manifest (payload URLs or auto-fetch)
- **Phase 2:** `plans/{run_date}/social-media-context.md`
- **Phase 3:** `plans/{run_date}/content-strategy.md`
- **Phase 4:** `plans/{run_date}/content-calendar.md`
- **Phase 5:** `BRAND_DNA.json` (+ schemas on Drive from templates/)
- **Phase 6a:** `{pin}-reference-prompt.md` per Pinterest pin
- **Phase 6:** `{slug}.CREATIVE_DNA.json` per calendar visual in `gdrive/clients/{client_slug}/{platform}/{calendar_week}/`
- **Phase 7:** `{slug}-post.md` (Instagram/Facebook/LinkedIn) or `{slug}-caption.md` (TikTok/Pinterest/YouTube)
- **Phase 7b:** `{slug}-caption-scores.json`
- **Phase 8:** `{slug}-prompt.md` (Brand DNA colors only — never creative hex)
- **Phase 9:** `{slug}.png` via image generation → upload to Drive — skip if `mode=dry_run`
- **Phase 9b:** Firestore publish if webhook includes `outletId` (download PNG from Drive for GCS upload)
- **Phase 10:** Write `gdrive/clients/{client_slug}/runs/{run_date}/PIPELINE-HANDOFF.md` with checklist + file table

**Calendar week folder:** use `calendar_start_date` from payload, or the first week in `content-calendar.md`.

**Pinterest rule:**
- If `pinterest_urls` present → download those pins to `gdrive/clients/{client_slug}/references/pinterest/{run_date}/`, write manifest; fill to 5 with auto-search only if fewer than 5.
- If absent → Phase 1b auto-fetch from `BRAND_IDENTITY.md`.

**Brand inputs rule:** Merge website + `brand_brief` / `brand_brief_url` + any downloaded `reference_files` before writing `BRAND_IDENTITY.md`.

**Gates:** Do not skip phases unless `skip_phases` says so or Drive artifacts already exist and are valid. If `gdrive/clients/{client_slug}/BRAND_IDENTITY.md` already exists on Drive and `skip_phases` includes `1`, reuse it.

## Output location (Google Drive)

All deliverables under `gdrive/clients/{client_slug}/`:

- `client.json`, `BRAND_IDENTITY.md`, `BRAND_DNA.json`
- `references/pinterest/{run_date}/`
- `plans/{run_date}/`
- `{platform}/{calendar_week}/` per `platforms[]` (e.g. `instagram/2026-08-11/`)
- `runs/{run_date}/PIPELINE-HANDOFF.md`

Do not write to `docs/swayam/weekly/` or repo `clients/`. This automation is client-scoped on Google Drive only.

## Git

**Do not** `git add` or commit client pipeline outputs — artifacts live on Google Drive only.

Stay on branch **brand-gdrive**. Do not commit to `main`. Do not create empty commits.

If you modified repo skills/docs during the run, commit only those skill changes separately when explicitly requested.

## Boundaries

- Invoke sub-skills per pipeline (design-brand-guardian, post-writer-sms, caption-score, firestore-creative-publish, etc.) — do not improvise outside the skill.
- Do not publish or schedule posts unless webhook includes `outletId` (Phase 9b) or user explicitly requests publish.
- Do not invent fake metrics in calendar or creatives.
- Brand DNA = one per client; Creative DNA = one per visual. Never use a shared creative registry.
