You were triggered by a webhook. Read the full webhook payload first before doing anything else.

You are in the AI-Scripts repo root on branch main. Do not create a new branch.

---

## Stateless runs (mandatory — do not carry state to the next run)

**Each webhook invocation is an isolated run.** The next trigger must not be affected by this run's memory, shortcuts, or leftovers.

### Do not persist or reuse run state

1. **No automation Memories** — do not read or write Cursor Memories, `MEMORIES.md`, `.cursor/automation-memory.md`, or any cross-run notes.
2. **No prior-run shortcuts** — do not skip phases because `clients/{client_slug}/` already has files from an earlier date. Default: **run Phases 0–10 fresh every time** (see skill Run policy). **Exception:** Phase 3b **must** read prior `plans/*/content-calendar.md` for headline dedup — that is research, not reuse.
3. **No prior handoffs as instructions** — do not treat `runs/*/PIPELINE-HANDOFF.md`, old `PIPELINE-HANDOFF.md`, or `publish-log.md` from prior dates as input for decisions in this run.
4. **No stale `client.json` shortcuts** — do not read `pipeline.last_run`, `outletId`, or folder paths from a previous run to skip intake or publish. Use **only** fields in **this** webhook payload (`outletId`, `client_slug`, etc.).
5. **No conversation carryover** — do not assume context from a previous automation run, background agent, or unfinished task. Inputs = **this webhook payload** + repo files you create/read **during this run**.
6. **Dated folders only** — write outputs under `{run_date}` subfolders (below). Never overwrite another run's `plans/{run_date}/`, `instagram/{run_date}/`, or `references/pinterest/{run_date}/`.

### Run date (set once at start)

| Variable | Resolution |
|----------|------------|
| `run_date` | UTC date of this invocation (`YYYY-MM-DD`) — used for all run-scoped folders |
| `posts_count` | From webhook `run.posts_per_week` or `run.posts_count`; default **3** |

**No publish dates in pipeline mode.** Ignore `calendar_start_date` and `calendar_week` if present in the webhook — scheduling happens outside the pipeline (BlackTwist, manual).

`client.json` may record `pipeline.run_date` and `pipeline.last_run` **for audit only** — never use those fields to skip work on a later run.

---

## Webhook intake (Phase 0)

Parse these fields from the webhook payload. If a field is missing, use the fallback noted.

| Field | Required | Use |
|-------|----------|-----|
| website | Yes | Re-fetch and analyze every run |
| client_slug | No | Folder under `clients/`; derive from domain if omitted |
| platforms | Yes | e.g. `["instagram"]`, `["instagram","facebook"]` |
| `posts_count` | No | `run.posts_per_week` or `run.posts_count` — how many creatives to produce; default **3** |
| calendar | No | `weekly` / `monthly` — batch label only; does **not** assign publish dates |
| brand_brief | No | Inline text — merge with fresh site research |
| brand_brief_url | No | Re-fetch if `brand_brief` empty or short |
| reference_files | No | Re-download URLs each run |
| reference_file_url | No | Alias for `reference_files[0]` |
| pinterest_urls | No | Download into `references/pinterest/{run_date}/`; auto-search to fill 5 if needed |
| goals | No | Awareness, leads, demos, etc. |
| mode | No | `full` (default) or `dry_run` (Phases 0–8 + 7b; skip Phase 9/9b) |
| outletId | No | Required for Phase 9b publish — **from payload only**; do not reuse from `client.json` |
| collection | No | Firestore collection override (default `social-ai-poster`) |
| skip_phases | No | **Ignore unless explicitly in this payload.** Never inherit from prior runs. |
| calendar_mode | No | `discover` (default) \| `preset` (when `campaign.posts` present) \| `preset_strict` |
| concept_history_runs | No | Prior plan folders to scan for used headlines; default **3** |
| campaign.posts | No | Preset week slots — dedup in `preset` mode; see Phase 3b |
| `creative_layout` | Optional | `default_template`, `reference_image_url` — see [creative-layout-templates.md](../brand-social-creative-pipeline/references/creative-layout-templates.md) |
| `run.creative_layout_template` | Optional | Alias for `creative_layout.default_template` |

Do not ask clarifying questions — the webhook payload is the intake. Proceed with best-effort defaults.

**Calendar dedup (Phase 3b):** Reading prior `plans/*/content-calendar.md` for headline dedup is **required research**, not forbidden run-state reuse.

---

## Runbook — read and follow in order

1. Read `skills/brand-social-creative-pipeline/SKILL.md` — master pipeline; **Run policy — always execute fresh** is mandatory.
2. Read `skills/brand-social-creative-pipeline/references/file-structure.md`
3. Read `skills/brand-social-creative-pipeline/references/single-image-post-policy.md`
4. Read `skills/brand-social-creative-pipeline/references/pinterest-reference-fetch/SKILL.md`
5. Read `skills/brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md` — Phase 3b
6. Read `skills/content-calendar-sms/SKILL.md` — Phase 4 (pipeline mode; renders calendar from brief)
7. Read `skills/brand-social-creative-pipeline/references/prompt-merge.md`
8. Read `skills/brand-social-creative-pipeline/references/brand-composition/SKILL.md` — Phase 9a
9. Reference shape: `clients/eduhexa/DRY-RUN-HANDOFF.md`, `clients/cybernetyx/`, `clients/swayam/`

---

## Execute pipeline (fresh every run)

Run **brand-social-creative-pipeline** Phases 0–10. Use `run_date` folders:

```
clients/{client_slug}/
├── BRAND_IDENTITY.md              # Phase 1 — rewrite each run
├── BRAND_DNA.json                 # Phase 5 — rewrite each run
├── plans/{run_date}/              # Phases 2–4
│   ├── social-media-context.md
│   ├── content-strategy.md
│   ├── pre-calendar-setup-brief.json   # Phase 3b
│   └── content-calendar.md            # Phase 4 — from brief only
├── references/pinterest/{run_date}/   # Phase 1b (+ Phase 6a reference prompts)
├── instagram/{run_date}/            # Phases 6–9b
├── facebook/{run_date}/             # Phase 7 mirror when in platforms
└── runs/{run_date}/PIPELINE-HANDOFF.md   # Phase 10 — new file per run
```

| Phase | Action |
|-------|--------|
| 0 | Scaffold / update `client.json` for this run's `run_date` paths |
| 1 | **Rewrite** `BRAND_IDENTITY.md` from website + brief + reference files |
| 1b | **New** pins under `references/pinterest/{run_date}/` (payload URLs first, then auto-search) |
| 6a | `{pin}-reference-prompt.md` per pin (reference-creative-prompt skill) |
| 2–3 | **Rewrite** `plans/{run_date}/` context + strategy |
| 3b | **Pre-calendar setup** — `pre-calendar-setup` skill → `pre-calendar-setup-brief.json` |
| 4 | **Content calendar** — `content-calendar-sms` pipeline mode (renders calendar from brief) |
| 5 | **Rewrite** `BRAND_DNA.json` |
| 6 | **New** `{slug}.CREATIVE_DNA.json` per calendar slot — dark editorial single-image only |
| 7 | **New** `{slug}-post.md` via post-writer-sms (Instagram/Facebook/LinkedIn) |
| 7b | **New** `{slug}-caption-scores.json` — revise if score < 65 |
| 8 | **New** `{slug}-prompt.md` (reference prompt + Brand DNA colors + elements) |
| 9 | **New** `{slug}-background.png` (or `{slug}.png` when composition disabled) — skip if `mode=dry_run` |
| 9a | **Compose** `{slug}.png` via `compose_brand_assets.py` when `logo.composition.enabled` |
| 9b | Publish per slug when `outletId` in **this** payload — skip if missing or `dry_run` |
| 10 | Write `runs/{run_date}/PIPELINE-HANDOFF.md` — do not overwrite other dates |

**Pre-calendar setup + calendar (Phases 3b–4):**

1. Run `skills/brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md` → write `pre-calendar-setup-brief.json`.
2. Run `skills/content-calendar-sms/SKILL.md` (pipeline mode) → render `content-calendar.md` from `selected_slots[]` only.

Do not write `content-calendar.md` without a brief. Do not invent topics outside `selected_slots[]`.

**Pinterest:** Never reuse pins from a prior `{run_date}` folder. Webhook `pinterest_urls` first; auto-search only to reach 5.

**Publish:** Phase 9b uses `outletId` from **this webhook only**. If absent, skip publish and note in handoff — do not read a stored outlet from `client.json`.

---

## Output location

All run-scoped deliverables live under `clients/{client_slug}/` with `{run_date}` as above.

Do not write to `docs/swayam/weekly/`. Do not merge this run's files into a prior run's dated folder.

---

## Git

When all phases complete (or `dry_run` stops after Phase 8):

1. `git add clients/{client_slug}/`
2. `git commit` to **main** only — do not create a new branch
3. Commit message: `Add {client_slug} pipeline run {run_date} ({posts_count} posts). Website: {website}.`

If nothing changed, do not create an empty commit.

---

## Boundaries

- Invoke sub-skills per pipeline — do not improvise outside the skill.
- Do not publish or schedule unless Phase 9b criteria met (`outletId` in payload).
- Do not invent fake metrics in calendar or creatives.
- Brand DNA = one per client root file (rewritten each run); Creative DNA = one per visual per `{run_date}`.
- **Never** optimize by reusing prior-run artifacts unless `skip_phases` is explicitly set in **this** webhook payload.
