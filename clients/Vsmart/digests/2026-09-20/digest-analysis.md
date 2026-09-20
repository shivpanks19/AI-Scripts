# Vsmart — weekly digest (2026-09-20)

**Reporting window:** 8–14 Sep 2026 (IST) vs prior 1–7 Sep 2026

## Executive summary

- Google Ads spend **₹60.3k** (−26% WoW) with **2,263 conversions** (−17% WoW); **CPA improved to ₹26.64** (−11% vs ₹30.03 prior week).
- **CA Final IDT (VB Sir)** drove ~60% of conversions at the lowest CPA in the account — protect budget and creative stability there.
- **CRM, Meta, and WhatsApp delivery sections unavailable** until `outletId` and Meta ad account are configured in client webhook/config.

## Pipeline & sales

- Skipped — CRM `outletId` is `"None"`. Fix in `daily-marketing-sales-digest.webhook.json` to enable leads and activity in future digests.

## Paid media

### Google Ads (912-522-8176)

| Metric | 8–14 Sep | 1–7 Sep | WoW |
|--------|----------|---------|-----|
| Spend | ₹60,282 | ₹81,059 | −26% |
| Conversions | 2,263 | 2,700 | −17% |
| CPA | ₹26.64 | ₹30.03 | −11% |
| Clicks | 5,903 | 6,848 | −14% |
| CTR | 1.91% | 1.73% | +0.18 pp |
| Avg CPC | ₹10.21 | ₹11.84 | −14% |

**Top campaigns (by spend):**

1. CA_Final_IDT_VB_Sir_01/03/2026 — ₹6.97k, 1,357 conv (core performer)
2. CA_Inter_DT_IDT_Law_Combo — ₹6.90k, 530 conv, CPA ₹13
3. Branded_Keywords (inter) — ₹6.06k, 228 conv, CPA ₹27

**Watch:**

- CMA_Final_IDT_DT — ₹6.78k spend, ~0.6 conversions
- CA_Inter_Grp_1 — ₹2.1k spend, 0 conversions, high impressions

### Meta

- Not configured — add `accounts.meta.ad_account_id` to enable.

## WhatsApp ops

- Delivery report skipped (invalid outletId).

## Recommended actions

1. **Media:** Hold or cautiously increase budget on **CA_Final_IDT_VB_Sir**; audit **CMA_Final_IDT_DT** and **CA_Inter_Grp_1** for pause or bid/keyword cuts this week.
2. **Ops:** Set a real CRM **outletId** in Vsmart webhook/config so pipeline and MSG91 delivery stats appear in the next digest.
3. **Tracking:** Confirm conversion definitions for high-volume campaigns (conversion counts are API-reported aggregates).
4. **Meta:** Connect Meta ad account ID for cross-channel spend and CPL view.

## Data gaps

- CRM pipeline and team activity (invalid outletId)
- Meta ads (missing ad account)
- WhatsApp template delivery stats (invalid outletId)
