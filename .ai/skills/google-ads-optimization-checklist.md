```markdown
# GrowthOps — Google Ads Optimization Checklist

This checklist is a reusable, prioritized set of actions for GrowthOps account owners and operators to improve conversion performance, reduce wasted spend, and increase ad relevance. It mirrors the priorities in `google-ads-reporting.md` and translates them into concrete daily/weekly/monthly tasks and experiment templates.

---

## How to use
- Run Daily items every weekday morning.
- Run Weekly items once per week (pick a consistent day).
- Run Monthly items as part of a deeper audit and experiment planning cycle.
- Use the Experiment Template at the end for any bid, budget, or creative test.

---

## Core metrics to track
- Clicks, Impressions, CTR
- Avg CPC, Cost
- Conversions, Conversion Rate, CPA
- ROAS (where applicable)
- Quality Score / Expected CTR

---

## Daily (quick checks — 10–20 minutes)
1. Check conversion tracking status
   - Confirm conversion counts are reporting and no tracking tags are broken.
2. Glance at top KPIs (Clicks, CTR, Conversions, CPA) vs. last 7 days
   - Flag any sudden spikes or drops.
3. Scan Search Terms (top 50 by impressions)
   - Add obvious irrelevant queries to negative keywords immediately.
4. Pause or reduce spend on keywords/campaigns with high spend and zero conversions for the week.
5. Check device performance
   - If mobile drives most clicks, ensure mobile pages are not producing heavy bounce rates.

---

## Weekly (30–60 minutes)
1. Keyword triage
   - Export Search Terms for the week. Mark low-intent terms as negative, move ambiguous terms to phrase/exact match tests.
   - Identify high CPC with low conversion keywords — reduce bids or move to a research campaign.
2. Ad copy review and A/B tests
   - Create at least 1 new ad variant per ad group focused on stronger CTAs & keyword in headline.
   - Rotate evenly and run for 2 weeks or >1000 impressions before deciding.
3. Device & time-of-day adjustments
   - Review Day & Hour report and set bid adjustments for low/high performance windows.
4. Budget allocation
   - Reallocate budget from non-performing campaigns to high-converting ones by small increments (10–20%).
5. Audit landing pages for top campaigns
   - Check load speed, one-tap CTA visibility on mobile, and tracking parameters.

---

## Monthly (1–2 hours deep audit)
1. Quality Score & optimization score audit
   - Review Quality Score drivers (expected CTR, ad relevance, landing page experience). Prioritize fixes.
2. Auction insights & competitor analysis
   - Check impression share, overlap rate, and outranking competitors. Pick targeted bids or copy changes.
3. Structure review
   - Consider splitting broad campaigns into intent-aligned campaigns (brand vs. generic vs. competitor vs. bottom-of-funnel).
4. Conversion funnel review
   - Validate backend leads, form completions, and sales attribution. Check for mislabeled conversions.
5. Plan experiments for next month
   - Draft 2–3 experiments (ad copy, landing page, bidding) with measurable success criteria.

---

## Keyword & Negative Keyword workflow
1. Weekly: Export Search Terms -> Sort by Impressions and CTR -> Tag negatives
2. Apply negatives at the campaign level (not account-wide) unless the term is universally irrelevant.
3. For high-spend/low-conversion queries, consider adding as negative and creating a tightly targeted exact-match test if intent is ambiguous.

Example negative keyword categories to consider (customize to account):
- free
- cheap
- sample
- jobs
- careers
- how to

---

## Ad Copy & Creative guidelines
- Include main keyword or intent phrase in headline 1 when possible.
- Use a clear CTA (e.g., "Get a quote", "Book demo", "Apply now").
- Add urgency or a differentiator in description lines.
- Test one variable at a time: headline, CTA, or value prop.
- Keep ad groups tightly themed (3–5 keywords) to improve relevance.

---

## Device & Bidding playbook
- Start with device bid adjustments based on performance: if mobile CTR and conversions are higher, increase mobile bids after landing page checks.
- If a device shows impressions but zero clicks, lower bids or exclude until ad/landing relevance improves.
- Use portfolio bidding or Smart Bidding only when conversion volume is sufficient; otherwise prefer manual CPCs or enhanced CPC with careful monitoring.

---

## Landing page checklist (for each top-converting campaign)
1. Mobile-first layout and fast load (<3s ideally)
2. Single, above-the-fold CTA
3. Trackable form/button events (GA4/gTag + server-side where possible)
4. Clear headline matching ad intent
5. Minimal distractions and clear value proposition

---

## Experiments template (fill before launching)
- Goal: (e.g., Increase CTR by 20% / Lower CPA to $X)
- Hypothesis: (If we X, then Y will happen because Z)
- Variant A: current
- Variant B: change (be specific)
- Metrics: primary (CTR, Conversions, CPA), secondary (CPC, Impression share)
- Minimum run: 2 weeks or 1000 impressions per variant
- Success criteria: A or B meets metric improvement and statistical significance

---

## Reporting cadence & alerts
- Daily email summary: clicks, CTR, conversions, CPA (7-day rolling window)
- Weekly deep-dive: search terms, top/worst keywords, device breakdown
- Alerts: daily CPA > target by 30% or conversion tracking error detected

---

## Notes & safety/guardrails
- Avoid blindly applying Google-suggested optimization actions (especially automated bid increases) without experiments.
- Document any structural changes (campaign split/merge) and reason in a short runbook.
- Keep a changelog of negatives and experiments to revert if needed.

---

If you want, I can also:
- Auto-generate a `reports/README.md` summarizing the last report and key negatives found.
- Extract negative keywords and sample ad copy variations from your Search Terms CSV (I tried earlier but file path encoding caused an error; I can retry if you'd like).

``` 
