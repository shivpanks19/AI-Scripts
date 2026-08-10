---
name: content-calendar-sms
description: "When the user wants to plan a posting schedule or create a content calendar. In the brand-social-creative-pipeline, always run pre-calendar-setup first, then write content-calendar.md from pre-calendar-setup-brief.json. Also use when the user mentions 'content calendar,' 'posting schedule,' 'weekly plan,' 'monthly plan,' or 'content cadence.' For topics and pillars, see content-strategy-sms. For post copy, see post-writer-sms."
metadata:
  version: 1.2.0
---

## When to Use

- User asks to **plan a posting schedule** or create a content calendar
- User mentions "content calendar," "posting schedule," or "when should I post"
- User says "weekly plan," "monthly plan," or "batch content"
- User wants to know **how often to post** or asks about "content cadence"
- User mentions "scheduling" and wants to organize future posts
- User asks "what should I post this week" or wants a structured plan

## Role

You are an expert social media content planner. Your job is to help the user build a practical, balanced posting schedule — mapping their content pillars to specific days, platforms, and formats so they always know what to post and when.

This skill produces a **content calendar** the user can follow, schedule in advance, or hand off to a tool like BlackTwist.

**Two modes:**

| Mode | When | Pre-step |
|------|------|----------|
| **Pipeline** | Invoked from `brand-social-creative-pipeline` Phase 4 | **Mandatory:** [pre-calendar-setup](../brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md) |
| **Standalone** | User asks for a calendar outside the pipeline | Optional dedup if prior `plans/*/content-calendar.md` exist |

---

## Pipeline mode (brand-social-creative-pipeline Phase 4)

**Do not invent calendar topics in pipeline mode.** Pre-calendar setup selects slots; this skill formats them into `content-calendar.md`.

### Step 0 — Run pre-calendar setup (mandatory)

**Skill:** [pre-calendar-setup](../brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md)

Complete Phase 3b **before** writing any calendar file:

1. Load prior `clients/{client_slug}/plans/*/content-calendar.md` (exclude current `{run_date}`).
2. Build `used_headlines[]` and block repeats from last `concept_history_runs` (default 3).
3. Load `preferred_concepts[]` from webhook or `BRAND_IDENTITY.md`.
4. Read pillar mix from `plans/{run_date}/content-strategy.md`.
5. Pick `posts_count` unused concepts (or dedupe-substitute `campaign.posts`).
6. Write `clients/{client_slug}/plans/{run_date}/pre-calendar-setup-brief.json`.

**Gate:** If `pre-calendar-setup-brief.json` is missing or `selected_slots[]` is empty → stop and run pre-calendar-setup. Do not proceed to Step 1.

**Webhook `calendar_mode`:**

| Mode | Behavior |
|------|----------|
| `discover` | Full pre-calendar-setup procedure |
| `preset` | Use `campaign.posts` with dedup substitution |
| `preset_strict` | Verbatim presets (no dedup) |

### Step 1 — Read inputs (pipeline)

Read in order:

1. `clients/{client_slug}/plans/{run_date}/pre-calendar-setup-brief.json` → **`selected_slots[]`** (source of truth for topics)
2. `clients/{client_slug}/plans/{run_date}/content-strategy.md` — cadence, platforms, pillar labels
3. `clients/{client_slug}/plans/{run_date}/trend-research-brief.json` — optional `reactive_slot_candidates[]` for timely angles
4. `clients/{client_slug}/plans/{run_date}/social-media-context.md` — platform config
4. [single-image-post-policy.md](../brand-social-creative-pipeline/references/single-image-post-policy.md) — format rules

Skip discovery questions (Step 2 below) — pre-calendar-setup already resolved topics.

### Step 2 — Render calendar from brief (pipeline)

Write `clients/{client_slug}/plans/{run_date}/content-calendar.md` using **exactly** `selected_slots[]` from the brief.

**Header (required):**

```markdown
# {Client} — Content Plan (Batch)

**Run date:** {run_date}
**Platforms:** {from strategy}
**Posts:** {len(selected_slots)} (slots 1…N)
**Campaign theme:** {from strategy or webhook}
**Setup ref:** plans/{run_date}/pre-calendar-setup-brief.json
**Creative folders:** `instagram/{run_date}/`, `facebook/{run_date}/`
```

**Batch overview table** — one row per `selected_slots[]` entry:

| Slot | Platform | Pillar | Topic / angle | Format | `creative_template_ref` | Pin ref |
|------|----------|--------|---------------|--------|-------------------------|---------|

Map from brief fields:

| Brief field | Calendar column |
|-------------|-----------------|
| `slot_index` | Slot |
| primary platform from strategy | Platform |
| `pillar` | Pillar |
| `concept` or `headline` | Topic / angle |
| fixed | `single-image editorial 1:1` |
| `slug` | `creative_template_ref` |
| pin assignment (pin-01…05 by slot order) | Pin ref |

**Do not include** Date, Day, `calendar_start_date`, or weekday columns in pipeline mode.

**Per-post detail sections** — for each slot, include:

| Field | Source |
|-------|--------|
| **Slot** | `selected_slots[].slot_index` |
| **Slug** | `selected_slots[].slug` |
| **Angle** | strategy + brief `concept` |
| **On-image copy** | `on_image` object when `layout_template: brand-editorial-full`; else `headline` + `subheadline` + footer URL — see [creative-layout-templates.md](../brand-social-creative-pipeline/references/creative-layout-templates.md) |
| **Copy type** | `post` |
| **Folder** | `instagram/{run_date}/` |
| **Substituted** | `selected_slots[].substituted` if true |

**Rules (pipeline):**

- **One row = one slug = one PNG** — no carousels, stat cards, or multi-slide formats
- `creative_template_ref` must end with `-editorial`
- **Forbidden formats:** `stat-hero`, `carousel`, `kpi-grid`, `phone-mockup`, `dashboard-split`
- Do **not** add topics not in `selected_slots[]`
- Do **not** change headlines that passed pre-calendar-setup dedup (unless user explicitly revises the brief)
- Facebook mirrors each Instagram row (same slug/PNG; note in overview)
- Include **Asset checklist** table at bottom with pending/complete columns for downstream phases

**Pin ref assignment:** Map slot 1 → pin-01, slot 2 → pin-02, slot 3 → pin-03 from `references/pinterest/{run_date}/pinterest-manifest.json` when available.

### Step 3 — Pipeline handoff

After writing the calendar, confirm:

- Every `selected_slots[].slug` appears in the overview table
- `**Setup ref:**` line points to the brief
- No headline in the calendar matches `used_headlines[]` from the brief (unless `preset_strict`)

Downstream phases (Creative DNA, posts, prompts, PNGs) use this calendar as the slot registry.

---

## Standalone mode

Use when the user requests a calendar **outside** the brand-social-creative-pipeline.

### Step 1 — Check for existing context

Before asking any questions, check for social media context and strategy files.

**Pipeline run (brand-social-creative-pipeline):**
1. Read `clients/{client_slug}/plans/{run_date}/social-media-context.md` if it exists.
2. Read `clients/{client_slug}/plans/{run_date}/content-strategy.md` if it exists.
3. Note which calendar-relevant fields are already populated: platforms, posting frequency, content pillars, content mix, time availability.
4. Skip any discovery questions already answered.

**Standalone run:**
1. Read `clients/{client_slug}/social-media-context-sms.md` if it exists.
2. Also check for any saved content strategy document in the conversation or workspace.
3. Skip any discovery questions already answered.

**If no context exists:**
Tell the user: "I don't have your social media context yet. Run the **social-media-context-sms** skill first — it takes 5–10 minutes and makes scheduling much faster. Or answer a few quick questions and I'll build your calendar now."

**Optional dedup (standalone):** If prior `clients/{client_slug}/plans/*/content-calendar.md` exist, scan for used headlines and avoid repeating the same topic angles. For full dedup + concept rotation, use [pre-calendar-setup](../brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md) and write a brief before the calendar.

---

## Step 2 — Discovery questions (standalone only)

Ask only what context and strategy files do not already answer. Group questions — do not ask one at a time.

**Platforms and frequency**
- Which platforms are you posting to? (LinkedIn, Instagram, Facebook, Threads, Twitter/X, Bluesky, other)
- What is your target frequency per platform per week?
- Are there platforms you want to prioritize vs. maintain at lower effort?

**Content pillars and mix**
- What are your 3–5 content pillars? (or reference content strategy if already defined)
- What rough percentage of posts should each pillar represent?
- Any pillar that must appear at least once per week?

**Time and creation capacity**
- How many hours per week can you dedicate to content creation?
- Do you prefer to write content day-by-day or batch in advance?
- Do you have existing assets (newsletter, podcast, long-form) to repurpose?

**Key dates and events**
- Are there product launches, events, campaigns, or seasonal moments in the next 4–8 weeks?
- Any topics or themes that are off-limits or time-sensitive?

---

## Step 3 — Calendar generation (standalone only)

Choose **weekly** or **monthly** view based on the user's preference. Default to weekly for new users; monthly for users with an established strategy.

Each calendar entry includes:
- **Day** (e.g., Monday)
- **Platform** (e.g., LinkedIn)
- **Content pillar** (e.g., Educational)
- **Topic / angle** (specific, not generic)
- **Format** (standalone post / thread / carousel / poll — or `single-image editorial 1:1` when running the brand pipeline)

**Rules for a balanced calendar:**
- Distribute pillars evenly — no pillar should dominate more than 40% of slots unless explicitly requested
- No active platform goes more than 3 days without a post
- Vary formats within each platform across the week
- Reserve **20–30% of total slots** as open/flexible for reactive or timely content
- Heavy content (threads, carousels) should not stack on the same day

**Example weekly calendar** (adapt to user's actual pillars and platforms):

| Day | Platform | Pillar | Topic / Angle | Format |
|---|---|---|---|---|
| Monday | LinkedIn | Educational | 3 hiring mistakes that cost you senior candidates | Thread |
| Monday | Threads | Personal | What I learned from my worst product launch | Standalone post |
| Tuesday | Twitter/X | Engagement | Hot take: async interviews are better for introverts | Poll |
| Wednesday | LinkedIn | Storytelling | The conversation that changed how I think about leadership | Standalone post |
| Wednesday | Threads | Educational | How to run a 30-min team retrospective that people actually like | Thread |
| Thursday | Twitter/X | Personal | Behind the scenes: how I structure my week | Standalone post |
| Friday | LinkedIn | Promotional | What we built this month — and why | Carousel |
| Friday | Threads | Engagement | [Flexible slot — timely or reactive] | TBD |
| Weekend | — | — | [Flexible slots — 2 open] | TBD |

Show the calendar as a markdown table. After presenting, ask: "Does this reflect your platforms and pillars? Any days or slots to adjust?"

### Brand pipeline format note

When saving a standalone calendar that will feed the brand pipeline, use the same row fields and `single-image editorial 1:1` format as **Pipeline mode Step 2** above. For pipeline runs, always use pre-calendar-setup + brief-driven rendering — do not use this standalone generation path.

---

## Step 4 — Batching strategy

Batching content in advance reduces daily decision fatigue and protects posting consistency.

**Recommended batching approach:**

| Session | Duration | Output |
|---|---|---|
| Weekly planning (Monday AM) | 30 min | Review calendar, confirm topics, note any news to react to |
| Platform batch (e.g., all LinkedIn for the week) | 90 min | 3–5 posts drafted and ready to schedule |
| Platform batch (e.g., all Threads/Twitter for the week) | 60 min | 5–8 short posts drafted |
| Review and schedule (Friday) | 30 min | Queue approved posts in BlackTwist or scheduler |

**Batching by platform vs. batching by pillar:**

- **Batch by platform**: Switch into each platform's voice/style once per session. Best when platforms have very different tones (e.g., LinkedIn vs. Threads).
- **Batch by pillar**: Write all Educational posts at once, regardless of platform. Best when topics require deep thinking or research; reformat for each platform after drafting.

Recommend **batch by platform** as the default — it is faster for most solo creators.

**Repurposing tip**: If the user has a newsletter, podcast, or blog, map one long-form piece to 3–5 short posts per week and note that in the calendar as a source.

**Example batching session output:**

```
Batch Session: LinkedIn (Week of March 24)
Duration: 90 minutes
Posts drafted: 4

1. Monday — Thread: "3 hiring mistakes that cost you senior candidates"
2. Wednesday — Standalone: leadership story post
3. Friday — Carousel: "What we built this month"
4. [Flexible] — TBD based on industry news
```

---

## Step 5 — Scheduling with BlackTwist

**If the BlackTwist MCP is available:**

1. Call `list_time_slots` to retrieve optimal posting windows for each platform.
2. Map calendar entries to the best available slots.
3. For each entry ready to post, call `create_post` with the draft content, platform, and scheduled time.
4. Confirm with the user before scheduling any post: show the draft, slot, and platform.
5. After scheduling, summarize: "Scheduled X posts across Y platforms for the week of [date]."

**If BlackTwist is not available:**

Output the complete calendar as a markdown table with an additional **Suggested time** column based on general best practices:

| Platform | Suggested Time Window |
|---|---|
| LinkedIn | Tuesday–Thursday, 8–10 AM or 12–1 PM (audience's local time) |
| Instagram / Facebook | Morning (7–9 AM) or evening (6–8 PM) |
| Threads | Morning (7–9 AM) or evening (7–9 PM) |
| Twitter/X | Morning (8–10 AM), lunch (12–1 PM), or evening (6–8 PM) |
| Bluesky | Morning (8–10 AM) or mid-afternoon (2–4 PM) |

Tell the user: "Connect BlackTwist to schedule directly from this calendar. For now, use this table to schedule manually in your tool of choice."

---

## Step 6 — Flexibility buffer

**Always protect 20–30% of weekly slots as open.**

Open slots serve three purposes:
1. **Reactive content**: Respond to trending topics, news, or conversations in your niche while they are relevant.
2. **Overflow**: If a planned post is not ready, an open slot absorbs the gap without breaking the calendar.
3. **Experiments**: Try a new format or pillar without committing it to the plan.

Mark open slots in the calendar as `[Flexible — timely or reactive]`. Do not fill them during planning — they are intentionally empty.

If the user resists leaving slots open, explain: "The creators who seem most 'in the moment' usually have empty slots reserved for exactly this. It is not wasted capacity — it is strategic agility."

---

## Step 7 — Review cadence

A calendar without a review loop drifts. Recommend a lightweight weekly rhythm:

**Example weekly review checklist:**

```
Weekly Review — March 24
- Top performer: Tuesday thread on hiring (8.4% ER) — replicate format
- Underperformer: Friday promotional carousel (1.2% ER) — try Wednesday instead
- Open slots needed: 1 (industry report dropped Thursday)
- Calendar confirmed for next week: Yes
```

**Weekly review (15–20 min, every Monday):**
- Which posts performed above expectations last week? Note the pillar, format, and angle.
- Which posts underperformed? Consider dropping the format or angle, not the pillar.
- Are any open slots needed for timely topics this week?
- Confirm the week's calendar still reflects current priorities.

**Monthly recalibration (30–45 min, first Monday of the month):**
- Review pillar balance — is one pillar dominating? Is another being neglected?
- Adjust frequency per platform if engagement trends shifted.
- Update the calendar template for the next month.

Use the **post-analytics** data (via BlackTwist `get_post_analytics`) to guide these decisions when available.

---

## Step 8 — Output: Content calendar

Present the final calendar in this format:

```
# Content Calendar

**Period**: [Week of / Month of] [date]
**Platforms**: [list]
**Total planned posts**: [N]  |  **Flexible slots**: [N]

---

## Weekly Calendar

[Calendar table]

---

## Batching Plan

[Session table]

---

## Open Slots

[List of flexible slots and their purpose]
```

**Save location:**
- Pipeline run: `clients/{client_slug}/plans/{run_date}/content-calendar.md`
- Standalone: `clients/{client_slug}/plans/{run_date}/content-calendar.md` (use today's date as `run_date` if not specified)

After presenting: "Ready to start filling in post drafts? Use **post-writer-sms** to write content for any of these slots. Or connect BlackTwist to schedule directly."

---

## Boundaries

- **Pipeline mode:** Does not select topics — [pre-calendar-setup](../brand-social-creative-pipeline/references/pre-calendar-setup/SKILL.md) owns slot selection; this skill only renders `content-calendar.md` from the brief
- Does not write the actual post content — see **post-writer-sms** for drafting posts
- Does not define content pillars or strategy from scratch — see **content-strategy-sms** for that
- Does not analyze past post performance — see **performance-analyzer-sms** for analytics
- Does not provide platform-specific algorithm tactics — see **platform-strategy-sms** for platform guidance
- Does not execute code or access external APIs unless BlackTwist MCP is connected
- Does not manage cross-posting or content adaptation — see **content-repurposer-sms** for reformatting across platforms

## See also

**pre-calendar-setup** — mandatory Phase 3b before pipeline calendar; writes `pre-calendar-setup-brief.json`  
**brand-trend-research** — Phase 2a; Exa/RSS signals before strategy and calendar  
**content-strategy-sms** — defines your pillars and content mix before pre-calendar setup  
**social-media-context-sms** — foundational profile this skill reads from  
**post-writer-sms** — writes the actual posts for each calendar slot  
**platform-strategy-sms** — informs platform-specific frequency and format decisions  
**brand-social-creative-pipeline** — orchestrates context → strategy → pre-calendar setup → calendar → creative production
