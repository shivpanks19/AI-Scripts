# Vsmart — weekly digest (2026-09-12)

## Executive summary

- Google Ads delivered **2,689 conversions** on **₹81.1k spend** (1–7 Sep), with **CPA ₹30** — **24.5% lower** than the prior week (₹40).
- **CA_Final_IDT_VB_Sir** drove most conversion volume (~1,731 conv); branded and Inter GST campaigns contributed steady mid-funnel volume.
- **High spend / near-zero conversion** on combo campaigns (VB+BB CA Final DT/IDT, CMA Final IDT) needs budget or targeting review this week.

## Pipeline & sales

- Not collected — CRM `outletId` is still `None`. Configure outlet in webhook or `daily-digest-config.json` to include leads and activity.

## Paid media

### Google Ads (912-522-8176)

| Metric | 1–7 Sep | 25–31 Aug | WoW |
|--------|---------|-----------|-----|
| Spend | ₹81,059 | ₹72,943 | +11% |
| Conversions | 2,689 | 1,826 | +47% |
| CPA | ₹30 | ₹40 | −25% |
| Clicks | 6,848 | 4,808 | +42% |
| CTR | 1.73% | — | — |

**Top spend campaigns (1–7 Sep):**

1. Branded_Keywords — ₹9.1k, 278 conv (healthy)
2. CA_Final_IDT_VB_Sir — ₹8.1k, **1,731 conv** (scale candidate)
3. VB+BB CA Final combo — ₹7.7k, **2 conv** (watch)
4. CMA_Final_IDT — ₹7.7k, **2 conv** (watch)
5. VB_Sir_Inter_GST — ₹7.6k, 137 conv

### Meta

- Not configured for this client run.

## Recommended actions

1. **Hold or cut** budget on VB+BB combo and CMA Final IDT until conversion rate improves or landing/offer is fixed.
2. **Protect / test scale** on CA_Final_IDT_VB_Sir — strongest efficiency at volume this week.
3. **Keep branded** spend stable; CPA and volume are in line with account goals.
4. **Set CRM outletId** so tomorrow’s digest includes pipeline and WhatsApp delivery health.
5. **Add Meta ad account ID** for unified paid-media view.

## Data gaps

- Google Ads MCP (`google-ads-py-mcp`) exposed zero tools; metrics pulled via Google Ads API with configured service account.
- CRM, Meta, and MSG91 delivery report skipped due to config.
