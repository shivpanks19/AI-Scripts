# Vsmart — weekly digest (2026-09-05)

**Report window:** 25 Aug – 31 Aug 2026 (IST)  
**Comparison:** 18 Aug – 24 Aug 2026 (prior week)

## Executive summary

- Google Ads spent **₹72.9k** with **1,808 conversions** at **₹40 CPA** — efficiency improved **8.8%** vs prior week despite **9.3% lower spend**.
- **CA_Final_IDT_VB_Sir** drove **73% of conversions** at just **₹5 CPA** — clear scale candidate.
- **₹9.8k wasted** on Vijay Sarda CMA campaigns with **zero conversions** — pause or restructure immediately.

## Pipeline & sales

- CRM not connected (`outletId` = None) — pipeline metrics unavailable this run.

## Team activity

- CRM activity digest skipped — no outlet configured.

## Paid media

### Google Ads (912-522-8176)

| Metric | This week | Prior week | WoW |
|--------|-----------|------------|-----|
| Spend | ₹72.9k | ₹80.4k | ↓9.3% |
| Conversions | 1,808 | 1,819 | ↓0.6% |
| CPA | ₹40 | ₹44 | ↓8.8% |
| Impressions | 260,846 | 353,200 | ↓26.1% |
| Clicks | 4,808 | 5,520 | ↓12.9% |
| CTR | 1.84% | — | — |
| CPC | ₹15 | — | — |

**Top performers (by volume):**
1. CA_Final_IDT_VB_Sir_01/03/2026 — ₹6.2k spend, 1,324 conv, ₹5 CPA
2. CA_Inter_DT_IDT_Law_Combo_19/02/2026 — ₹6.4k spend, 319 conv, ₹20 CPA
3. Branded_Keywords_30/01/2026 — ₹7.6k spend, 93 conv, ₹82 CPA

**Underperformers (zero conversions, spend > ₹1k):**
- Vijay_Sarda_CMA_Final_03/08/2026 — ₹6.5k, 0 conv
- VIjay_Sarda_CMA_Inter_23/07/2026 — ₹3.3k, 0 conv
- CA_Inter_Grp_1_15/02/2026 — ₹2.0k, 0 conv

**High CPA watch:**
- CMA_Final_IDT_DT_31/07/2026 — ₹6.4k spend, 1 conv (₹6.4k CPA)
- Pavan_Karmele_06/01/2026 — ₹6.4k spend, 2 conv (₹3.1k CPA)

### Meta

- Not configured — no Meta ad account ID in client config.

## WhatsApp ops

- Delivery report skipped — CRM outlet not configured.

## Recommended actions

1. **Pause** Vijay Sarda CMA Final & Inter campaigns (₹9.8k combined, 0 conversions last week).
2. **Increase budget** on CA_Final_IDT_VB_Sir — best CPA at ₹5 with 1,324 conversions; room to scale.
3. **Audit** CMA_Final_IDT_DT campaign — ₹6.4k for 1 conversion; review targeting and creative.
4. **Configure CRM outletId** in webhook config to enable pipeline + WhatsApp delivery sections.
5. **Add Meta ad account** to unlock cross-channel spend/CPL comparison.

## Data gaps

- CRM: `outletId` is placeholder "None"
- Meta: `ad_account_id` not set
- WhatsApp delivery report: requires valid outletId
- `get_account_currency` MCP call failed (credentials); currency assumed INR from account history
