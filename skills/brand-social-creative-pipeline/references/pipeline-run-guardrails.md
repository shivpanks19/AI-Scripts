# Pipeline Run Guardrails (stall prevention)

**Applies to:** All webhook/automation runs on `brand-gdrive`.

Prevents 90+ minute hangs from duplicate Drive uploads, missing Phase 9, and unbounded retries.

---

## Root causes (hexanovate 2026-08-09 postmortem)

| Failure | Symptom | Fix |
|---------|---------|-----|
| Duplicate uploads | 3× `BRAND_IDENTITY.md`, 4× same reference prompt | Search-before-create; track in progress file |
| Upload-before-generate | Hours on Drive MCP; Phase 9 never started | Local staging + phase batch upload |
| No checkpoint | Run appeared hung; no resume point | `PIPELINE-PROGRESS.json` from Phase 0 |
| Binary upload retries | Pin PNGs never landed on Drive | One attempt per file; manifest notes failures |
| Folder path drift | `instagram/{run_date}` vs `{calendar_week}` | Always `instagram/{calendar_week}/` |

---

## Mandatory workflow (every run)

### 1. Local staging first

```
/tmp/{client_slug}-{run_date}/
```

**Write all artifacts locally** during Phases 0–8. Do **not** call Drive MCP for every file as it is authored.

Upload to Drive **once per phase** (batch) or **once at Phase 8 complete** for creatives — never interleave generation with per-file uploads.

### 2. Progress checkpoint (Phase 0 — first Drive write)

Immediately after scaffold, create on Drive:

```
gdrive/clients/{client_slug}/runs/{run_date}/PIPELINE-PROGRESS.json
```

Template: [../templates/pipeline-progress.template.json](../templates/pipeline-progress.template.json)

Update after **each phase completes** with `status`, `completed_at`, and `drive_file_ids` for uploaded files.

### 3. Resume within run (mandatory on retry/continuation)

At run start, read `PIPELINE-PROGRESS.json` for this `{run_date}`:

| Progress state | Action |
|----------------|--------|
| Missing | Start Phase 0 |
| `phases["8"].status == complete` and Phase 9 not complete | **Skip to Phase 9** — do not re-upload Phases 0–8 |
| `phases["9"].status == complete` and `outletId` present | **Skip to Phase 9b** |
| `status == complete` | Phase 10 only if handoff missing |

**Never re-upload a file** whose `uploads.{filename}.file_id` is already recorded in progress for this run.

### 4. Idempotent Drive writes

Before every `create_file`:

```
search_files: title = '{exact_filename}' and parentId = '{target_folder_id}'
```

| Search result | Action |
|---------------|--------|
| 0 matches | `create_file` |
| 1 match | **Skip upload** — record existing `file_id` in progress (MCP has no content update) |
| 2+ matches | Use newest by `modifiedTime`; skip further uploads of that name to this folder |

**Hard rule:** Max **one** `create_file` per `(parentId, title)` per run. Never retry upload on uncertainty.

### 5. Phase time budgets

If a phase exceeds budget, **mark partial in progress**, proceed to next critical phase, finish in handoff.

| Phase | Budget | On timeout |
|-------|--------|------------|
| 0–1 | 10 min | Continue with brief + website curl fallback |
| 1b | 15 min | Ship manifest with ≥3 pins; note missing in progress |
| 2–8 | 25 min | Stage locally; batch-upload once |
| **9** | **20 min** | **Required** — generate PNGs even if some Drive text files pending |
| 9b | 15 min per slug | Log failures; continue next slug |
| 10 | 5 min | Write handoff with partial status |

**Phase 9 is never deferrable.** If Phases 0–8 artifacts exist locally or on Drive, start image generation before any optional re-upload.

### 6. Binary upload rules (pins + PNGs)

| Rule | Detail |
|------|--------|
| Max size | Skip MCP base64 upload if file > 400 KB — use [upload-drive-run.sh](../scripts/upload-drive-run.sh) or note in manifest |
| Attempts | **1 attempt** per binary per run |
| Order | Text manifest first, then pins 01–05, then generated PNGs |
| Failure | Record `"status": "failed"` in progress; continue pipeline |

### 7. Phase completion gates

Mark phase complete only when **required outputs exist** (local or Drive):

| Phase | Gate |
|-------|------|
| 1b | `pinterest-manifest.json` lists ≥3 pins with local paths |
| 6 | One `{slug}.CREATIVE_DNA.json` per calendar slug |
| 7b | One `{slug}-caption-scores.json` per slug |
| 8 | One `{slug}-prompt.md` per slug |
| 9 | One `{slug}.png` per slug on Drive |
| 9b | `publish-log.md` entry per slug (when `outletId` set) |

### 8. Anti-patterns (never do)

- Upload the same filename twice to the same folder in one run
- Call Drive MCP inside a loop over 20+ files without search-before-create
- Spend >30 min on Drive uploads before starting Phase 9
- Re-run Phase 1–8 because Phase 9 failed
- Block handoff (Phase 10) when partial — document what failed

---

## Batch upload order

Use [../scripts/upload-drive-run.sh](../scripts/upload-drive-run.sh) or equivalent batch:

1. `client.json`, schemas (root)
2. `BRAND_IDENTITY.md`, `BRAND_DNA.json` (root)
3. `plans/{run_date}/*`
4. `references/pinterest/{run_date}/*` (manifest + prompts, then PNGs)
5. `instagram/{calendar_week}/*` (DNA, posts, scores, prompts, PNGs)
6. `facebook/{calendar_week}/*` (posts, PNG mirrors)
7. `runs/{run_date}/PIPELINE-PROGRESS.json` → `PIPELINE-HANDOFF.md`

Update `PIPELINE-PROGRESS.json` after each batch.

---

## See also

- [google-drive-storage.md](./google-drive-storage.md) — idempotent MCP ops
- [../SKILL.md](../SKILL.md) — phase runbook
- [../templates/pipeline-progress.template.json](../templates/pipeline-progress.template.json)
