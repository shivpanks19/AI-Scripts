# Vsmart — weekly digest (2026-08-23)

**Report window:** 16 Aug – 22 Aug 2026 (IST) · Google Ads account 912-522-8176

## Executive summary

- **Spend down 7.8%** to ₹85.8k while **conversions up 7.5%** to 1,869 — efficiency improved.
- **CPA improved 14.2%** week-on-week (₹53.48 → ₹45.89); best driver is CA_Final_IDT_VB_Sir at ₹6.10 CPA.
- **3 campaigns burned ₹20k+ with near-zero conversions** — immediate budget review recommended.

## Pipeline & sales

- CRM data unavailable — `outletId` is set to `None` in webhook config.
- Configure a valid CRM outlet to include leads, pipeline stages, and team activity in future digests.

## Paid media

### Google Ads (16–22 Aug)

| Metric | This week | Prior week | Δ |
|--------|-----------|------------|---|
| Spend | ₹85,774 | ₹93,009 | -7.8% |
| Impressions | 331,545 | 363,555 | -8.8% |
| Clicks | 5,645 | 5,663 | -0.3% |
| Conversions | 1,869 | 1,739 | +7.5% |
| CPA | ₹45.89 | ₹53.48 | -14.2% |
| CTR | 1.70% | 1.56% | +0.14pp |
| Avg CPC | ₹15.19 | ₹16.42 | -7.5% |

**Top campaigns by spend:**

1. Branded_Keywords — ₹8,766 · 222 conv · CPA ₹39
2. CMA_Final_IDT_DT — ₹8,158 · 1 conv · CPA ₹7,880 ⚠️
3. VB_Sir_Inter_GST — ₹7,541 · 56 conv · CPA ₹135
4. CA_Final_IDT_VB_Sir — ₹7,498 · 1,229 conv · CPA ₹6 ✅
5. CA_Inter_DT_IDT_Law_Combo — ₹7,028 · 338 conv · CPA ₹21

**Watch list:**

- Vijay_Sarda_CMA_Final — ₹6,582 spend, 0 conversions
- Pavan_Karmele — ₹6,904 spend, 3 conversions (CPA ₹2,328)
- VB+BB Final DT/IDT Combo — ₹6,795 spend, 1 conversion (CPA ₹6,523)

### Meta

- Not configured — add `accounts.meta.ad_account_id` to include Meta performance.

## WhatsApp ops

- Delivery report skipped (no valid CRM outletId).

## Recommended actions

1. **Scale CA_Final_IDT_VB_Sir** — 1,229 conversions at ₹6 CPA; consider +15–20% budget if impression share is capped.
2. **Pause or cut budget 50% on Vijay_Sarda_CMA_Final and CMA_Final_IDT_DT** — combined ₹14.7k spend with ~1 conversion total.
3. **Review Pavan_Karmele and VB+BB combo bids** — ₹13.7k spend for 4 conversions; reallocate to CA_Inter_DT_IDT_Law_Combo (CPA ₹21).
4. **Protect Branded_Keywords budget** — strong 50% CTR and ₹39 CPA; do not reduce during exam season.
5. **Fix webhook config** — set valid `outletId`, `google_ads.customer_id` (9125228176), and Meta ad account for full cross-channel digest.

## Data gaps

- CRM, Meta, and WhatsApp delivery sections skipped due to config placeholders.
- `get_account_currency` MCP call failed; INR assumed from account billing.
