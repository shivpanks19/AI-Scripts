# Vsmart — weekly digest (2026-08-11)

**Report window:** Mon 4 Aug – Sun 10 Aug 2026 (vs prior week 28 Jul – 3 Aug)

## Executive summary

- Google Ads spend reached **₹84,579** (+24% WoW) with **1,491 conversions** (+31%) at **₹57 CPA** (−5% — efficiency improved).
- **Branded Keywords** and **CA_Final_IDT_VB_Sir** drove the bulk of efficient volume (CPA ₹11–23); several faculty campaigns burned budget with near-zero returns.
- **#1 action:** Pause or restructure **Vijay_Sarda_CMA_Inter**, **Pavan_Karmele**, and **CMA_Final_IDT** — combined ₹24.3k spend with only ~5 conversions last week.

## Pipeline & sales

- CRM not connected (`outletId` missing) — pipeline metrics unavailable this run.
- Configure `accounts.crm.outletId` in webhook/config to include leads, stage movement, and team activity next week.

## Paid media

### Google Ads (912-522-8176)

| Metric | Last week | Prior week | Δ |
|--------|-----------|------------|---|
| Spend | ₹84,579 | ₹68,116 | +24% |
| Impressions | 258,924 | 178,786 | +45% |
| Clicks | 5,048 | 3,873 | +30% |
| CTR | 1.95% | 2.17% | −0.22pp |
| Avg CPC | ₹16.75 | ₹17.59 | −5% |
| Conversions | 1,491 | 1,141 | +31% |
| CPA | ₹56.71 | ₹59.69 | −5% |
| Conv. value | ₹1,17,052 | ₹75,556 | +55% |

**Top performers (by efficiency at scale):**
1. CA_Final_IDT_VB_Sir — ₹7,255 spend, 650 conv, CPA **₹11**
2. Branded_Keywords — ₹8,518 spend, 378 conv, CPA **₹23**
3. CA_Inter_DT_IDT_Law_Combo — ₹7,106 spend, 357 conv, CPA **₹20**

**Underperformers (high spend, poor CPA):**
1. CMA_Final_IDT_DT — ₹11,909 spend, 2.6 conv, CPA **₹4,592**
2. Pavan_Karmele — ₹7,211 spend, 2.1 conv, CPA **₹3,451**
3. Vijay_Sarda_CMA_Inter — ₹5,199 spend, **0 conversions**
4. Shubham_Singhal — ₹5,023 spend, 1 conv, CPA **₹4,929**

### Meta

- Not configured — add `accounts.meta.ad_account_id` to include Meta spend and CPL.

## WhatsApp ops

- Delivery report skipped (no CRM outlet configured).

## Recommended actions

1. **Today:** Pause **Vijay_Sarda_CMA_Inter** (₹5.2k / 0 conv) and review search terms + landing page for **Pavan_Karmele** and **CMA_Final_IDT**.
2. **This week:** Shift ~15% budget from worst CPA campaigns into **Branded_Keywords** and **CA_Final_IDT_VB_Sir** (proven CPAs under ₹25).
3. **Before next digest:** Add CRM `outletId` and Meta ad account to webhook config for full marketing + sales view.

## Data gaps

- CRM pipeline: outletId not set
- Meta Ads: ad_account_id not set
- WhatsApp delivery report: requires CRM outletId
- Prior digest baseline: first Vsmart digest run — WoW from live Google Ads API only
