# Vsmart — weekly digest (2026-09-23)

Report window: **15–21 Sep 2026** (IST). Comparison vs **8–14 Sep 2026**.

## Executive summary

- Google Ads delivered **2,208 conversions** on **₹52,356 spend** — CPA **₹23.71**, down ~10% week-on-week despite slightly lower conversion volume.
- **CA_Final_IDT_VB_Sir_01/03/2026** drove most results (~1,186 conv at ~₹5.68 CPA); protect budget and search terms on this campaign.
- **Pavan_Karmele** and **CMA_Final_IDT_DT** burned ~₹14.2k combined with minimal conversions — pause or restructure before next week’s spend.

## Pipeline & sales

- CRM not available (`outletId` placeholder). Pipeline, lead stage, and team activity sections omitted.

## Team activity

- Not collected (CRM skipped).

## Paid media

### Meta

- Not configured — no ad account ID in client webhook/config.

### Google Ads (912-522-8176)

| Metric | 15–21 Sep | 8–14 Sep | WoW |
|--------|-----------|----------|-----|
| Spend | ₹52,356 | ₹60,282 | −13% |
| Conversions | 2,208 | 2,292 | −4% |
| CPA | ₹23.71 | ₹26.30 | −10% |
| Clicks | 5,179 | 5,903 | −12% |
| Impressions | 207,423 | 309,683 | −33% |
| CTR | 2.50% | 1.91% | +0.6 pp |

**Top spend campaigns (15–21 Sep):**

1. VB_Sir_Inter_GST — ₹7.4k, 196 conv, CPA ₹37.6  
2. Pavan_Karmele — ₹7.3k, 3.5 conv, CPA ~₹2,100 ⚠️  
3. CA_Inter_DT_IDT_Law_Combo — ₹7.1k, 518 conv, CPA ₹13.8 ✅  
4. CMA_Final_IDT_DT — ₹6.8k, ~1 conv ⚠️  
5. CA_Final_IDT_VB_Sir — ₹6.7k, 1,186 conv, CPA ₹5.7 ✅  

- Combined insight: Efficiency improved account-wide (lower CPA, higher CTR) while impression volume dropped — likely budget/auction shift, not tracking loss.

## WhatsApp ops

- Delivery report skipped (invalid CRM outletId for MSG91 outlet lookup).

## Recommended actions

1. **Pause or cap** `Pavan_Karmele_06/01/2026` until creative/landing page is fixed (₹7.3k / 3 conv last week).
2. **Review** `CMA_Final_IDT_DT_31/07/2026` and `CA_Inter_Grp_1_15/02/2026` (₹6.8k+ spend, near-zero conversions).
3. **Hold or modestly increase** budget on `CA_Final_IDT_VB_Sir_01/03/2026` and `CA_Inter_DT_IDT_Law_Combo_19/02/2026` — best volume at acceptable CPA.
4. **Fix CRM outletId** in webhook/config so pipeline + WhatsApp delivery sections can run on future digests.
5. **Add Meta ad account ID** if Meta spend should appear in the combined brief.

## Data gaps

- CRM: `accounts.crm.outletId` = `None`
- Meta: missing `ad_account_id`
- WhatsApp delivery report: blocked by outletId
- `get_account_currency` MCP call failed (OAuth); currency inferred as INR from account spend formatting
