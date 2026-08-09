# Google Drive Storage (brand-gdrive branch)

**Branch:** `brand-gdrive`  
**MCP server:** `plugin-google-drive-google-drive` (authenticated in automation — not in local dev)

All pipeline **inputs and outputs** live on Google Drive under `clients/{client_slug}/`.  
Skills, templates, and schemas stay in this repo under `skills/brand-social-creative-pipeline/`.

---

## Root folder

| Field | Value |
|-------|-------|
| Folder ID | `1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ` |
| URL | https://drive.google.com/drive/folders/1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ |
| Logical prefix | `gdrive/clients/{client_slug}/` |

Every client gets a subfolder:

```
gdrive/
└── clients/
    └── {client_slug}/
        ├── client.json
        ├── BRAND_IDENTITY.md
        ├── BRAND_DNA.json
        ├── BRAND_DNA_SCHEMA.json
        ├── CREATIVE_DNA_SCHEMA.json
        ├── references/pinterest/{run_date}/
        ├── plans/{run_date}/
        ├── instagram/{calendar_week}/
        ├── facebook/{calendar_week}/
        ├── linkedin/{calendar_week}/
        ├── assets/
        └── runs/{run_date}/
```

---

## Path notation

In skills and `client.json`, use the **`gdrive/` prefix** to distinguish Drive paths from repo paths:

| Logical path | Example |
|--------------|---------|
| Client root | `gdrive/clients/swayam/` |
| Brand identity | `gdrive/clients/swayam/BRAND_IDENTITY.md` |
| Pinterest refs | `gdrive/clients/swayam/references/pinterest/2026-08-09/` |
| Plans | `gdrive/clients/swayam/plans/2026-08-09/social-media-context.md` |
| Creative | `gdrive/clients/swayam/instagram/2026-08-11/prove-it-era-editorial.png` |
| Logo | `gdrive/clients/swayam/assets/logo.png` |

Store resolved Drive folder IDs in `client.json` → `storage.folder_ids` after first scaffold (automation).

---

## MCP operations (automation)

Use **Google Drive MCP** for all read/write. Do **not** write pipeline artifacts to `clients/` in the git repo on this branch.

**Stall prevention:** [pipeline-run-guardrails.md](./pipeline-run-guardrails.md) — local staging, progress checkpoint, search-before-create.

### Idempotent write protocol (mandatory)

Drive MCP `create_file` cannot update content in place. Prevent duplicates:

1. **Search first:** `title = '{filename}' and parentId = '{folder_id}'`
2. **0 results** → `create_file`; record `file_id` in `PIPELINE-PROGRESS.json` → `uploads.{filename}`
3. **≥1 results** → **skip upload** for this run; use newest `file_id` in progress
4. **Max 1 create per (parentId, title) per run** — never retry on uncertainty

### Local staging (mandatory)

| Step | Action |
|------|--------|
| 1 | Write artifacts to `/tmp/{client_slug}-{run_date}/` during Phases 0–8 |
| 2 | Verify with `scripts/upload-drive-run.sh` |
| 3 | Batch-upload per phase block (not per file during generation) |
| 4 | Update `runs/{run_date}/PIPELINE-PROGRESS.json` after each batch |

### Scaffold (Phase 0)

1. Ensure `clients/` exists under root folder `1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ`.
2. Create `clients/{client_slug}/` and subfolders (`references`, `plans`, `instagram`, `facebook`, `linkedin`, `assets`, `runs`).
3. Copy schema templates from repo → Drive:
   - `skills/brand-social-creative-pipeline/templates/BRAND_DNA_SCHEMA.json`
   - `skills/brand-social-creative-pipeline/templates/CREATIVE_DNA_SCHEMA.json`
4. Write initial `client.json` with `storage.backend: "google_drive"`.

### Read / write text

- **Read:** fetch file content from Drive by path or file ID (markdown, JSON, prompts).
- **Write:** create or update file at the logical `gdrive/clients/{slug}/…` path.
- **Append:** for `publish-log.md`, read → append section → write back.

### Binary (PNG, logo)

- **Download:** fetch pin images and generated PNGs to a temp path when visual analysis or base64 upload is required.
- **Upload:** after Phase 9 image generation, save `{slug}.png` to `gdrive/clients/{slug}/instagram/{calendar_week}/`.
- **One attempt** per binary per run; if MCP base64 fails (>400 KB), record failure in progress and continue.
- **Phase 9b:** download PNG from Drive → base64 → GCS `image-function` (do not rely on repo paths).

### Folder creation per run

On each invocation, create **new dated folders** on Drive (never overwrite prior runs):

- `references/pinterest/{run_date}/`
- `plans/{run_date}/`
- `instagram/{calendar_week}/`
- `facebook/{calendar_week}/`
- `runs/{run_date}/` (include `PIPELINE-PROGRESS.json` at Phase 0)

---

## client.json storage block

```json
{
  "slug": "eduhexa",
  "display_name": "EduHexa",
  "storage": {
    "backend": "google_drive",
    "root_folder_id": "1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ",
    "root_url": "https://drive.google.com/drive/folders/1mGIow4YU-8vzTeUFBtFXsNLkjg-aM1uJ",
    "path_prefix": "clients/eduhexa",
    "mcp_server": "plugin-google-drive-google-drive"
  },
  "folders": {
    "root": "gdrive/clients/eduhexa",
    "brand": "gdrive/clients/eduhexa/BRAND_IDENTITY.md",
    "brand_dna": "gdrive/clients/eduhexa/BRAND_DNA.json",
    "references": "gdrive/clients/eduhexa/references/pinterest",
    "plans": "gdrive/clients/eduhexa/plans",
    "instagram": "gdrive/clients/eduhexa/instagram",
    "assets": "gdrive/clients/eduhexa/assets",
    "logo": "gdrive/clients/eduhexa/assets/logo.png"
  }
}
```

Update `folders.*` with `{run_date}` / `{calendar_week}` suffixes each run. Persist Drive file/folder IDs in `storage.folder_ids` when the MCP returns them.

---

## Repo vs Drive

| Location | What lives there |
|----------|------------------|
| **Git repo** (`brand-gdrive` branch) | Skills, templates, schemas, docs, automation config |
| **Google Drive** | All client artifacts: identity, DNA, plans, refs, copy, prompts, PNGs, publish logs |

Legacy `clients/` folder in the repo is **read-only reference** (historical examples). New runs must not write there.

---

## Phase 9b — publish from Drive

```
1. Download gdrive/clients/{slug}/instagram/{date}/{slug}.png via Drive MCP
2. base64 encode → POST image-function
3. Read post copy + scores from same Drive folder
4. POST /ai-content
5. Append publish-log.md on Drive
```

---

## See also

- [file-structure.md](./file-structure.md) — artifact layout (Drive paths)
- [SKILL.md](../SKILL.md) — full pipeline runbook
- [../templates/client.json.template](../templates/client.json.template) — scaffold template
