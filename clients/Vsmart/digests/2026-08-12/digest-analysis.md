# Vsmart — weekly digest (2026-08-12)

**Report window:** Mon 4 Aug – Sun 10 Aug 2026 (IST)  
**Source:** Google Ads account 912-522-8176

## Executive summary

- **₹88,789** spent across Google Ads last week — **+31% vs prior week** (est. ₹68,045) with conversions up ~28% to **1,511**.
- **Blended CPL ₹59** held steady (prior week ~₹58); efficiency did not degrade despite higher spend.
- **CA Final IDT (VB Sir)** and **Branded Keywords** drove the majority of conversions at **₹10–25 CPL** — protect and scale these.
- **₹11k+ wasted** on Vijay Sarda CMA campaigns with near-zero conversions — immediate review needed.

## Pipeline & sales

- CRM not connected (`outletId` missing) — pipeline metrics unavailable this run.
- Google Ads recorded **1,511 conversion actions** (includes branded/navigational and lead events as configured in account).

## Paid media — Google Ads

| Metric | Last week | Prior week (est.) | Change |
|--------|-----------|-------------------|--------|
| Spend | ₹88,789 | ₹68,045 | +31% |
| Clicks | 5,279 | 3,970 | +33% |
| Conversions | 1,511 | 1,178 | +28% |
| CPL | ₹59 | ₹58 | +2% |
| CPC | ₹17 | — | — |
| CTR | 1.89% | — | — |

### Top performers (by conversions)

1. **CA_Final_IDT_VB_Sir** — 708 conv, ₹7,239 spend, **CPL ₹10**
2. **Branded_Keywords** — 345 conv, ₹8,511 spend, **CPL ₹25**
3. **CA_Inter_DT_IDT_Law_Combo** — 360 conv, ₹7,068 spend, **CPL ₹20**
4. **VB_Sir_Inter_GST** — 66 conv, ₹7,050 spend, CPL ₹107

### Underperformers (watch list)

| Campaign | Spend | Conversions | CPL |
|----------|-------|-------------|-----|
| CMA_Final_IDT_DT (VB BB) | ₹13,065 | 2.6 | ₹5,026 |
| Pavan_Karmele | ₹7,282 | 2.1 | ₹3,476 |
| CA Final Combo (VB+BB) | ₹7,165 | 2.8 | ₹2,516 |
| Vijay Sarda CMA Inter | ₹5,061 | 0 | — |
| Vijay Sarda CMA Final | ₹2,926 | 0 | — |

## Recommended actions

1. **Pause or cap Vijay Sarda CMA Inter + Final** — ₹7,986 combined spend with 0 conversions last week.
2. **Shift 15–20% budget** from CMA Final IDT DT and Pavan Karmele into CA Final IDT VB Sir and Branded Keywords (proven ₹10–25 CPL).
3. **Audit conversion tracking** on high-CPL Final/Combo campaigns — confirm lead events vs page views before further scale.
4. **Connect CRM outletId** in webhook config to include pipeline and stale-lead data in future digests.
5. **Add Meta ad account ID** if running Facebook/Instagram ads alongside Google.

## Data gaps

- CRM pipeline: skipped (no valid `outletId`)
- Meta ads: skipped (no `ad_account_id`)
- Prior-week comparison: estimated from 14-day API window (no saved digest baseline)
- `get_account_currency` MCP call failed (credentials); currency assumed INR from account context
