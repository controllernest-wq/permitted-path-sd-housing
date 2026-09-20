# Permitted Playbook

## 1. Agree on the strategy (what actually works)

The request is internally consistent **if** we pick the right loan and the right property type:

- Good credit → qualifies for FHA (580+ legal floor; 640–680+ is the practical DPA floor) and conventional 3% products.
- Low personal cash → owner-occupied financing + DPA that does **not** explode when you later rent.
- Live 12 months → FHA Handbook 4000.1 occupancy (move in ~60 days, intend to occupy ~12 months).
- Then rent or sell → rent is the cleaner 12-month exit. Sell is cleaner at 24 months.
- Close-to-free housing → rent from *other legal units* offsets PITI. Your unit is not “free”; it is subsidized.

What does **not** work as a default:

- Using **SDHC or County DCCA** and moving out at month 13 (loan due immediately + default interest on several programs).
- Planning a **tax-free sale at month 12** (Section 121 is a 2-of-5-year use test).
- Buying a cheap unpermitted garage conversion and calling it an ADU.
- Scraping Zillow/Redfin against their terms and auto-offering.

## 2. Property archetypes (ranked)

### A. Best fit: 2–4 unit in FHA limit, live in one

- FHA finances 1–4 units owner-occupied at 3.5% down.
- Other units may be rented from day one.
- After 12 months you may rent your unit and keep the loan.
- FHA generally one *active owner-occupied FHA* at a time; the seasoned property can remain FHA as a rental.
- 3–4 unit properties have a self-sufficiency rental test (PITI vs. appraiser rents).
- San Diego inventory is thin. Widen to El Cajon, La Mesa, National City, Lemon Grove, Oceanside, Vista, San Marcos, Escondido — still commute-viable.

### B. Strong fit: 1-unit + legal ADU and/or JADU

- San Diego is ADU-friendly: ministerial permits, no extra parking in most of the city, ADU + JADU on many SFR lots.
- Standard ADU: owner occupancy generally **not** required.
- JADU with **shared bath**: owner occupancy still required. JADU with **separate bath**: occupancy rule relaxed under 2026 state changes — verify on the current City IB-400 and recorded Junior Unit Agreement.
- Do not rent <31 days (no STR on ADU/JADU).
- Conversion cost is real ($50k–$175k typical for JADU / garage). Only works if you have a construction reserve, a 203(k)/renovation loan, or buy a house that **already has** a permitted ADU.

### C. Acceptable: condo / townhome house-hack (roommate or legal 2-bed lease)

- Lower price, HOA risk, rental restrictions, FHA condo roster required.
- Roommate income is not the same as unit rent for underwriting.

### D. Do not default to: out-of-county “bargain” you will not occupy

- If you never move in, FHA/DPA occupancy is false. That is the bright line.

## 3. Capital stack (low cash, permitted)

Layer in this order:

1. **First mortgage:** FHA 3.5% or conventional 3% (HomeReady / HomePossible) if income fits AMI bands.
2. **DPA compatible with a later rental conversion:**
   - **GSFA Platinum** — 1–4 units; official FAQ: not required to remain after purchase and *initial* residency; repaid on sale/refi of first. Confirm current matrix with a participating lender.
   - **Chenoa Fund** (FHA DPA; no statewide income limit on some products) — occupy 60 days; forgivable variants need 36 on-time first-mortgage payments. Moving out early can kill forgiveness.
   - **CalHFA MyHome** — up to 3.5% behind a CalHFA first. First-time = no principal residence ownership in 3 years. Occupancy within 60 days. Property type on MyHome pages is **1-unit** (ADU/granny may be eligible as part of a 1-unit). Poor fit for a true duplex. Repayment on sale, refi, first-lien payoff, transfer — confirm whether a later non-occupancy event is called in the note you actually sign.
3. **Seller credits** for closing costs (negotiate; FHA has limits).
4. **Gift funds** from family (document properly).
5. **Avoid as primary if 12-month exit is the plan:** SDHC City Low/Middle, County DCCA, Chula Vista FTHB. Those notes typically accelerate when you stop occupying.

### Illustrative cash (not a quote)

On a $750,000 duplex:

- FHA 3.5% = $26,250
- Upfront MIP 1.75% usually financed
- Closing costs ~2–3% before credits
- If DPA covers the 3.5% and seller covers most closings, **your check can be reserves + prepaid interest/taxes + 1% earnest** rather than 20%.

You still need **reserves**. Lenders and reality both require it. Budget 3–6 months PITI + a vacancy month on the rental unit.

## 4. The 12-month operating plan

**Days 0–60:** Move in. Change DL, voter, insurance, utilities to the property. Keep proof. This is your occupancy file.

**Months 1–12:**
- Live in your unit. Rent only the *other* legal units.
- California lease, deposit limits, habitability, and any local rent ordinance.
- Do not treat “I sleep here twice a month” as occupancy.

**Month 13 decision tree:**

```
Keep as rental?
  yes → professional manager, insurance to landlord policy, track depreciation
       → do not buy another FHA until this file is clean
Sell?
  at month 13 → expect capital gains tax (federal + CA ordinary treatment at state)
  at month 24+ → Section 121 may shelter $250k / $500k of residence-portion gain
Repeat house hack?
  only with a new owner-occupied loan and a real move
```

## 5. How “close to free” is actually calculated

Monthly housing cost after hack =

`PITI + HOA + MIP + maintenance reserve + vacancy reserve − rent collected from other legal units`

Target: that number ≤ current rent, ideally near $0–$800 all-in for *your* housing.

Do not count appreciation or tax write-offs as cash that pays the mortgage.

## 6. Where “insane delays / deals” actually appear

San Diego does not give away houses. Edges that are legal:

- 2–4 units with ugly cosmetics and clean structure / clean title
- Seller-occupied tired landlord (not tenant-occupied if you need certain DPA)
- Price cuts >8% and DOM >45
- Permitted ADU already in place (inspect the permit, not the listing prose)
- Probate and public-auction lists (slow, lawyer required)
- HUD REO when available
- Geographic stretch inside the county, not a fantasy $300k coastal SFR

The agent in `/agent` scores those features. It does not invent inventory.

## 7. 90-day execution sequence

1. Pull credit; fix only what matters (utilization, collections).
2. HUD-approved homebuyer class (required for CalHFA / SDHC; useful anyway).
3. Interview 2 CalHFA-capable and 1 GSFA-capable lenders. Get written overlays.
4. Written budget: max PITI, min reserves, max rehab.
5. Hire a buyer-broker who has closed 2–4 unit FHA in the county.
6. Ingest listings into the scout (agent export CSV + public feeds).
7. Underwrite 10 properties on `models/cashflow_template.csv` before offering on 1.
8. Offer with FHA + DPA timeline, inspection, and permit contingency.
9. Build the occupancy file from day one.
