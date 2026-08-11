---
name: daily-marketing-sales-digest
description: >-
  Daily or weekly marketing + sales digest for a client: pull CRM pipeline,
  Meta/Google Ads, WhatsApp delivery data; synthesize insights; send HTML email
  (Gmail MCP) and WhatsApp summary (MSG91 MCP). Use when running the daily
  digest agent, client morning brief, or marketing/sales update automation.
metadata:
  version: 1.0.0
---

# Daily marketing & sales digest

## When to use

- Cursor automation / webhook triggers the **daily-marketing-sales-digest** agent.
- User asks for a **daily brief**, **morning update**, or **marketing + sales digest** for a named client.
- Scheduled run (cron / Cursor Automations) with `client_slug` + `outletId`.

**Required MCP:** Gmail (`user-gmail`), MSG91 (`msg91-mcp`), CRM (`user-crm-mcp`). **Recommended:** Meta (`user-meta`), Google Ads (`user-google-ads-py-mcp`).

---

## Client config & intake

**Two places to set IDs and delivery targets** (webhook overrides config):

| What | Config path | Webhook path |
|------|-------------|--------------|
| CRM outlet | `accounts.crm.outletId` | `accounts.crm.outletId` |
| Google Ads account | `accounts.google_ads.customer_id` | same |
| Meta ad account | `accounts.meta.ad_account_id` | same |
| Email sender (Gmail) | `delivery.email.from` | same |
| Email recipients | `delivery.email.to[]` | same |
| WhatsApp sender (MSG91) | `delivery.whatsapp.integrated_number` | same |
| WhatsApp recipients | `delivery.whatsapp.recipient_numbers[]` | same |

Schema: [references/client-digest-config.schema.json](./references/client-digest-config.schema.json).  
Example: [clients/_template/daily-digest-config.example.json](../../clients/_template/daily-digest-config.example.json).  
Full webhook: [agents/daily-marketing-sales-digest.webhook.example.json](../../agents/daily-marketing-sales-digest.webhook.example.json).

### Phase 0 — Merge and validate

1. Load webhook + `clients/{client_slug}/daily-digest-config.json`.
2. Normalize legacy keys (`outletId`, `google_customer_id`, `meta_ad_account_id`).
3. Write `clients/{client_slug}/digests/{run_date}/run-config.json`.
4. Reject placeholders: `REPLACE`, `0000000000`, `client@example.com`, `act_REPLACE`.
5. If validation fails → `intake-error.md` and **stop** (no send, no data pull).

**Gmail `from`:** Must be the inbox authenticated in `user-gmail` MCP, or a verified send-as alias for that inbox. Log `from` in `delivery-log.md`.

**MSG91 `integrated_number`:** Pass to every `msg91_send_text` / bulk send call. Defaults to MSG91 env only if config omits it — prefer explicit config.

---

## Phase 1 — Collect (parallel where possible)

Run only integrations enabled in config (`integrations.*: true`).

### CRM (`user-crm-mcp`)

| Tool | Args | Extract |
|------|------|---------|
| `crm_firebase_ping` | `{ outletId: run_config.accounts.crm.outletId }` | Confirm connectivity |
| `crm_report_recent_leads_by_stage` | `{ outletId, daysBack: window_days }` | Leads by stage, counts |
| `crm_report_latest_leads` | `{ outletId, maxSample: 10 }` | Newest leads (name, source, stage) |
| `crm_report_lead_activity_digest` | `{ outletId, daysBack: window_days }` | Activity by type/assignee |
| `crm_saved_read_run` | per config `saved_reads[]` | Custom reports if defined |

Store under `digest-data.json` → `crm`.

### Meta (`user-meta`)

When `integrations.meta` and `run_config.accounts.meta.ad_account_id` set:

| Tool | Args | Extract |
|------|------|---------|
| `get_meta_campaign_performance` | `ad_account_id`, date preset matching window | Spend, results, CPL |
| `get_creative_fatigue_insights` | account + window | Ads needing refresh |
| `get_meta_conversion_tracking_status` | account | Pixel/CAPI health flags |

Store under `digest-data.json` → `meta`.

For cross-channel context, follow `~/.cursor/skills/cross-channel-ads-report/SKILL.md` Steps 4–5 (abbreviated — top 5 campaigns by spend/results only).

### Google Ads (`user-google-ads-py-mcp`)

When `integrations.google_ads` and `run_config.accounts.google_ads.customer_id` set:

| Tool | Args | Extract |
|------|------|---------|
| `get_campaign_performance` | `{ customer_id: run_config.accounts.google_ads.customer_id, days: window_days }` | Spend, clicks, conversions, CPL |
| `get_account_currency` | `{ customer_id }` | Currency label |

Store under `digest-data.json` → `google_ads`.

### WhatsApp delivery (`msg91-mcp`)

When `integrations.whatsapp_delivery`:

| Tool | Args | Extract |
|------|------|---------|
| `msg91_whatsapp_delivery_report` | `{ outletId, days_back: window_days }` | Sent, delivered, failed |
| `msg91_get_outlet_config` | `{ outletId, type: "simple" }` | Active template config (no secrets) |

Store under `digest-data.json` → `whatsapp`.

### Optional: Microsoft Clarity (`user-clarity-{client}`)

When `integrations.clarity` and `clarity_project` set — run **3–4 simple queries** only:

- Sessions count (current vs prior window if tool allows)
- Top landing pages
- Smart events / form submits
- Rage clicks or JS errors (if elevated)

Store under `digest-data.json` → `clarity`.

### Optional: Spur (`user-spur-eduhexa-mcp`)

When `integrations.spur`:

- `broadcast_overview_stats` — recent broadcast performance
- `broadcast_search` — campaigns in window

Store under `digest-data.json` → `spur`.

---

## Phase 2 — Analyze

Write `digest-analysis.md` with this structure:

```markdown
# {display_name} — {cadence} digest ({run_date})

## Executive summary
(3 bullets max — biggest wins, biggest risks, #1 action)

## Pipeline & sales
- New leads: {n} ({delta vs prior})
- By stage: ...
- Stale / no activity: ...
- Top sources: ...

## Team activity
- Calls / WhatsApp / notes: ...
- Assignee load: ...

## Paid media
### Meta
...
### Google
...
- Combined insight: ...

## WhatsApp ops
- Delivery rate, failures, template issues

## Recommended actions
1. ...
2. ...
3. ...

## Data gaps
- (failed MCP calls, missing config)
```

**Rules:**

- Compare to prior `digest-data.json` when available; else label metrics as "current period only".
- Flag anomalies: CPL up >25%, zero conversions with spend > threshold (config `alerts.min_spend_inr`, default 1000), leads with no activity >48h.
- Max 5 recommended actions; each must be specific (who/what/when).

---

## Phase 3 — Compose deliverables

### HTML email

Follow [references/email-html-template.md](./references/email-html-template.md). Output `digest-email.html`.

- Subject: `{display_name} daily brief — {run_date}` (or weekly variant)
- Preheader: one-line executive summary
- Inline CSS only; max width 600px; mobile-friendly tables

### WhatsApp

Follow [references/whatsapp-digest-format.md](./references/whatsapp-digest-format.md). Output `digest-whatsapp.txt`.

- Target **≤ 900 characters** for single-message readability
- Use line breaks, emoji sparingly (0–2)
- End with one CTA line (e.g. "Reply if you want the full breakdown.")

---

## Phase 4 — Send email (Gmail MCP)

Use values from `run-config.json` only.

1. `GetMcpTools` → `user-gmail` → find send tool.
2. Common schemas:
   - `send_email`: `{ from, to, cc, reply_to, subject, body, html?: true }` or `{ body_html }`
   - `gmail_send`: `{ to, subject, body }` — `from` must match authenticated account
3. Read `digest-email.html` as HTML body.
4. **From:** `delivery.email.from` (required — which Google account sends).
5. **To:** `delivery.email.to[]` (required). **Cc / reply_to:** optional from config.
6. Log `from`, `to`, message id in `delivery-log.md`.

**If send tool missing or server errored:** save draft path in log; do not retry more than once.

---

## Phase 5 — Send WhatsApp (MSG91 MCP)

Use `run-config.json` only. For each entry in `delivery.whatsapp.recipient_numbers[]`:

**Inside 24h session window (or internal ops numbers):**

```
msg91_send_text({
  recipient_number: "91XXXXXXXXXX",
  text: <contents of digest-whatsapp.txt>,
  integrated_number: <delivery.whatsapp.integrated_number>
})
```

**Outside 24h / client-facing marketing:**

Use approved template via `msg91_send_configured_bulk`:

```
msg91_send_configured_bulk({
  outletId,
  type: "simple",  // or config digest.whatsapp.template_type
  userMobileNumber: ["91XXXXXXXXXX"],
  text: <short summary for body variable>
})
```

Or `msg91_send_template_bulk` when config specifies `template_name` + `language_code`.

**Confirm:** Log MSG91 response id per recipient in `delivery-log.md`.

`dry_run` → skip all sends; note in log.

---

## Phase 6 — Delivery log

`delivery-log.md` template:

```markdown
# Delivery log — {run_date}

| Channel | Status | Detail |
|---------|--------|--------|
| Email | sent / skipped / failed | to: ... |
| WhatsApp | sent / skipped / failed | n recipients |

## MCP errors
- ...

## Artifacts
- digest-data.json
- digest-analysis.md
- digest-email.html
- digest-whatsapp.txt
```

Update `clients/{client_slug}/client.json`:

```json
"digest": {
  "last_run": "{ISO8601}",
  "last_run_date": "{run_date}",
  "cadence": "daily"
}
```

Audit only — never skip collection because `last_run` exists.

---

## Scheduling (Cursor Automations)

Minimum webhook must include **accounts** and **delivery** — see [agents/daily-marketing-sales-digest.webhook.example.json](../../agents/daily-marketing-sales-digest.webhook.example.json). Do not run with only `client_slug` and `outletId`.

Recommended schedule: **08:00 Asia/Kolkata** weekdays (covers yesterday IST for ads + CRM).

Point the automation at agent file: `agents/daily-marketing-sales-digest.md`.

---

## MCP setup reference

Example `.cursor/mcp.json` entries (project or global):

```json
{
  "mcpServers": {
    "msg91-mcp": {
      "url": "https://YOUR_PROJECT.web.app/mcp/msg91?token=YOUR_TOKEN"
    },
    "crm-mcp": {
      "command": "npm",
      "args": ["--prefix", "/path/to/CRM", "run", "mcp:crm:start"]
    }
  }
}
```

Gmail: enable `user-gmail` in Cursor Settings → MCP; authenticate when prompted.
