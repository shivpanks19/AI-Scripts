# WhatsApp digest format

Output plain text to `digest-whatsapp.txt`. MSG91 `msg91_send_text` accepts the full string.

## Constraints

| Rule | Value |
|------|-------|
| Target length | **≤ 900 characters** (single screen scroll) |
| Hard max | 1200 characters — truncate with "…full report in email" |
| Emoji | 0–2 max (📊 ✅ ⚠️ only when meaningful) |
| Links | At most **1** URL (dashboard or CRM deep link from config) |
| PII | Respect `delivery.whatsapp.redact_pii` — use first names only |

## Structure

```
*{display_name} — {cadence} brief ({run_date})*

*Summary*
• {bullet_1}
• {bullet_2}
• {bullet_3}

*Pipeline*
Leads: {new_leads} ({delta})
Top stage: {stage} ({count})
Stale (>48h): {stale_count}

*Ads*
Spend: {currency}{spend} | CPL: {currency}{cpl}
Best: {top_campaign}
Watch: {underperformer}

*Actions*
1. {action_1}
2. {action_2}
3. {action_3}

{cta_line}
```

## CTA lines (pick one)

- Internal ops: `Reply here if you want me to dig into any number.`
- Client-facing: `Full breakdown is in your email. Reply YES for a 10-min review call.`
- Agency handoff: `Logged in CRM — tag me if anything looks off.`

## Template fallback (outside 24h window)

When `msg91_send_text` is not allowed, compress to **template body variable** (≤ 300 chars):

```
{run_date}: {new_leads} new leads. Spend {spend}, CPL {cpl}. Top action: {action_1}. Full report emailed.
```

Use `msg91_send_configured_bulk` with outlet `MESSAGING_CONFIG` type from config (`digest.whatsapp.template_type`, default `simple`).

## Example (eduhexa-style, ~650 chars)

```
*EduHexa — daily brief (11 Aug)*

*Summary*
• 12 new leads (↑4 vs yesterday)
• Meta CPL ₹412 — best week this month
• 6 leads untouched >48h in Qualified

*Pipeline*
New: 12 | Won: 2 | Lost: 1
Sources: Meta 7, Website 3, Referral 2

*Ads*
Spend ₹18.4k | 45 leads | CPL ₹409
Best: Hexa_LeadGen_Schools_Aug
Watch: Demand Gen — CTR 0.4%

*Actions*
1. Call 6 stale Qualified leads today
2. Pause ad set with 0 leads / ₹3k spend
3. Refresh creative on fatigued carousel

Full tables in your email. Reply if you want a walkthrough.
```

## Multi-recipient

Send the **same** `digest-whatsapp.txt` to each number in `delivery.whatsapp.recipient_numbers[]`. Personalize with `[Name]` only when config provides `recipients[]` objects with `name` + `phone`.
