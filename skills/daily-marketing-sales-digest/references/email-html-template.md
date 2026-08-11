# HTML email template — daily digest

Use this structure for `digest-email.html`. Replace `{placeholders}` with run values. Keep **inline CSS** only (no external stylesheets).

## Design rules

- Max width **600px**, centered table layout
- Font stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`
- Brand accent: use `brand.accent_color` from config (default `#0066FF`)
- Numbers in **bold**; deltas in green (`#0a7`) for positive, red (`#c33`) for negative (pipeline metrics: more leads = green; higher CPL = red)
- No images required; optional client logo URL from config
- Footer: agency name + "Reply to this email for questions"

## Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{display_name} — Daily Brief {run_date}</title>
</head>
<body style="margin:0;padding:0;background:#f4f5f7;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f5f7;padding:24px 12px;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:8px;overflow:hidden;max-width:600px;">

          <!-- Header -->
          <tr>
            <td style="background:{accent_color};padding:20px 24px;">
              <p style="margin:0;font-size:12px;color:rgba(255,255,255,0.85);text-transform:uppercase;letter-spacing:0.05em;">{cadence} brief</p>
              <h1 style="margin:8px 0 0;font-size:22px;color:#ffffff;font-weight:600;">{display_name}</h1>
              <p style="margin:6px 0 0;font-size:14px;color:rgba(255,255,255,0.9);">{run_date_display} · {timezone}</p>
            </td>
          </tr>

          <!-- Executive summary -->
          <tr>
            <td style="padding:24px;">
              <h2 style="margin:0 0 12px;font-size:16px;color:#111;">Executive summary</h2>
              <ul style="margin:0;padding-left:20px;color:#333;font-size:14px;line-height:1.6;">
                <li>{summary_bullet_1}</li>
                <li>{summary_bullet_2}</li>
                <li>{summary_bullet_3}</li>
              </ul>
            </td>
          </tr>

          <!-- KPI row -->
          <tr>
            <td style="padding:0 24px 24px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td width="33%" style="background:#f8f9fb;border-radius:6px;padding:12px;text-align:center;">
                    <p style="margin:0;font-size:11px;color:#666;text-transform:uppercase;">New leads</p>
                    <p style="margin:4px 0 0;font-size:20px;font-weight:700;color:#111;">{new_leads}</p>
                    <p style="margin:2px 0 0;font-size:12px;color:{leads_delta_color};">{leads_delta}</p>
                  </td>
                  <td width="4"></td>
                  <td width="33%" style="background:#f8f9fb;border-radius:6px;padding:12px;text-align:center;">
                    <p style="margin:0;font-size:11px;color:#666;text-transform:uppercase;">Ad spend</p>
                    <p style="margin:4px 0 0;font-size:20px;font-weight:700;color:#111;">{ad_spend}</p>
                    <p style="margin:2px 0 0;font-size:12px;color:{spend_delta_color};">{spend_delta}</p>
                  </td>
                  <td width="4"></td>
                  <td width="33%" style="background:#f8f9fb;border-radius:6px;padding:12px;text-align:center;">
                    <p style="margin:0;font-size:11px;color:#666;text-transform:uppercase;">Cost / lead</p>
                    <p style="margin:4px 0 0;font-size:20px;font-weight:700;color:#111;">{cpl}</p>
                    <p style="margin:2px 0 0;font-size:12px;color:{cpl_delta_color};">{cpl_delta}</p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Pipeline -->
          <tr>
            <td style="padding:0 24px 24px;">
              <h2 style="margin:0 0 12px;font-size:16px;color:#111;border-bottom:2px solid {accent_color};padding-bottom:6px;">Pipeline &amp; sales</h2>
              {pipeline_html}
            </td>
          </tr>

          <!-- Paid media -->
          <tr>
            <td style="padding:0 24px 24px;">
              <h2 style="margin:0 0 12px;font-size:16px;color:#111;border-bottom:2px solid {accent_color};padding-bottom:6px;">Paid media</h2>
              {paid_media_html}
            </td>
          </tr>

          <!-- Actions -->
          <tr>
            <td style="padding:0 24px 24px;background:#f8f9fb;">
              <h2 style="margin:0 0 12px;font-size:16px;color:#111;">Recommended actions</h2>
              <ol style="margin:0;padding-left:20px;color:#333;font-size:14px;line-height:1.7;">
                <li>{action_1}</li>
                <li>{action_2}</li>
                <li>{action_3}</li>
              </ol>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:16px 24px;border-top:1px solid #eee;">
              <p style="margin:0;font-size:12px;color:#888;line-height:1.5;">
                Prepared by {agency_name}. Data window: last {window_days} day(s).<br/>
                Questions? Reply to this email.
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

## Section HTML snippets

### Pipeline table

```html
<table role="presentation" width="100%" cellpadding="8" cellspacing="0" style="font-size:13px;border-collapse:collapse;">
  <tr style="background:#f0f1f3;">
    <th align="left" style="color:#666;">Stage</th>
    <th align="right" style="color:#666;">Count</th>
    <th align="right" style="color:#666;">Δ</th>
  </tr>
  <!-- repeat rows -->
</table>
```

### Campaign mini-table (top 3)

```html
<p style="margin:0 0 8px;font-size:13px;font-weight:600;color:#444;">Meta — top campaigns</p>
<table role="presentation" width="100%" cellpadding="6" cellspacing="0" style="font-size:12px;border-collapse:collapse;">
  <tr style="background:#f0f1f3;">
    <th align="left">Campaign</th>
    <th align="right">Spend</th>
    <th align="right">Results</th>
    <th align="right">CPL</th>
  </tr>
</table>
```

## Subject line patterns

| Cadence | Pattern |
|---------|---------|
| Daily | `{display_name} daily brief — {run_date}` |
| Weekly | `{display_name} weekly marketing & sales — w/e {run_date}` |

Preheader (Gmail preview): first executive summary bullet, truncated to ~100 chars.
