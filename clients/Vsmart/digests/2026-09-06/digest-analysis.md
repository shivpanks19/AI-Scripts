# Vsmart — weekly digest (2026-09-06)

**Report window:** Mon 25 Aug – Sun 31 Aug 2026 (IST)  
**Comparison:** Mon 18 Aug – Sun 24 Aug 2026

## Executive summary

- Google Ads spent **₹72.9k** (↓9.3% WoW) and drove **1,810 conversions** (flat WoW) — **CPA improved to ₹40** (↓8.8%).
- **CA_Final_IDT_VB_Sir** remains the volume engine: 1,324 conversions at ₹4.7 CPA; accounts for ~73% of weekly conversions.
- **₹19k+ wasted** across three campaigns with near-zero returns — pause or restructure Vijay_Sarda_CMA_Final, CMA_Final_IDT_DT, and Pavan_Karmele immediately.

## Pipeline & sales

- **Skipped** — CRM outletId is placeholder (`None`). Configure a valid outletId to enable pipeline metrics.

## Team activity

- **Skipped** — CRM not connected.

## Paid media

### Meta

- **Skipped** — Meta ad_account_id not configured.

### Google Ads (912-522-8176)

| Metric | This week | Prior week | Δ |
|--------|-----------|------------|---|
| Spend | ₹72,943 | ₹80,440 | ↓9.3% |
| Conversions | 1,810 | 1,820 | ↓0.6% |
| CPA | ₹40.31 | ₹44.19 | ↓8.8% |
| Clicks | 4,808 | 5,519 | ↓12.9% |
| Impressions | 260,846 | 352,887 | ↓26.1% |
| CTR | 1.84% | 1.56% | +0.28 pts |
| Avg CPC | ₹15.17 | ₹14.58 | +4.0% |

**Top campaigns by spend:**

| Campaign | Spend | Conv | CPA |
|----------|-------|------|-----|
| Branded_Keywords_30/01/2026 | ₹7,625 | 94 | ₹81 |
| CMA_Final_IDT_DT_31/07/2026 | ₹7,445 | 1 | ₹6,466 |
| Vijay_Sarda_CMA_Final_03/08/2026 | ₹6,481 | 0 | — |
| CA_Final_IDT_VB_Sir_01/03/2026 | ₹6,230 | 1,324 | ₹4.71 |
| CA_Inter_DT_IDT_Law_Combo | ₹6,351 | 319 | ₹20 |

- Combined insight: Efficiency improved despite lower volume — impression share dropped 26% but conversion volume held steady. Budget is concentrated in a few high-CPA faculty campaigns while the IDT Final campaign drives bulk conversions at very low CPA.

## WhatsApp ops

- **Skipped** — CRM outletId not configured for delivery reports.

## Recommended actions

1. **Pause Vijay_Sarda_CMA_Final** — ₹6.5k spend, zero conversions last week. Reallocate budget to CA_Final_IDT_VB_Sir or CA_Inter combo campaigns.
2. **Review CMA_Final_IDT_DT and Pavan_Karmele** — combined ₹13.9k spend for ~3 conversions (CPA >₹4,600). Tighten keywords or pause until creative/landing page is refreshed.
3. **Scale CA_Final_IDT_VB_Sir** — 1,324 conversions at ₹4.7 CPA; test +15–20% budget increase while monitoring impression share.
4. **Fix CRM outletId** — pipeline and WhatsApp delivery sections are blind until `accounts.crm.outletId` is set in webhook/config.
5. **Configure Meta ad account** — enable cross-channel view in next digest.

## Data gaps

- CRM pipeline: outletId = `None`
- Meta Ads: ad_account_id missing
- WhatsApp delivery report: outletId missing
- Google account currency API failed; INR assumed from prior runs
