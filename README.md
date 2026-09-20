# Permitted Path: San Diego First-Time Occupancy → Low-Cash Housing Engine

**Goal:** Use good credit and first-time / owner-occupied financing to buy a home you can actually live in for 12 months, put as little of your own cash in as is legally possible, then either (a) keep it as a rental or (b) sell and roll into the next asset — without occupancy fraud, unpermitted units, or DPA landmines.

This is a **permitted** plan. Creative does not mean illegal.

Repo: https://github.com/controllernest-wq/permitted-path-sd-housing

## The honest constraint set

| Constraint | Reality in San Diego County (2026) |
|---|---|
| Cash you front | 0–3.5% + reserves is possible; “zero money ever” is not |
| Live-in 12 months | Compatible with **FHA** occupancy. **Not** compatible with SDHC / County DCCA if you then move out |
| Sell after 12 months | Usually **taxable**. IRC 121 needs ~24 months use |
| “Insane deals” on MLS | Rare at median ~$900k+. Distressed + 2–4 unit + ADU path is the edge |
| Close-to-free housing | Possible as **offset housing cost**, not as a free lunch |
| Passive | After month 13, if you keep it, you become a CA landlord. That is a job until you professionalize it |

## Recommended stack (default)

1. **Product:** FHA owner-occupied on a **2–4 unit** *or* a 1-unit with a **legal ADU/JADU**.
2. **Down payment:** FHA 3.5% covered as much as possible by **GSFA Platinum** (1–4 units allowed; FAQ states no required stay *after initial residency*) and/or seller credits. Avoid SDHC if the plan is to vacate at month 13.
3. **Year 0–1:** You live in one unit. Other unit(s) rent from day one. That is house hacking, not fraud.
4. **Month 13+ fork:**
   - **Keep:** rent your unit, keep the FHA loan, professional property manager.
   - **Sell:** better if you can stretch to **24 months** for Section 121.
   - **Repeat:** new owner-occupied purchase only after occupancy on loan #1 is clean and documented.

## What this repo contains

| Path | What it is |
|---|---|
| [PLAN.md](PLAN.md) | Full permitted playbook and capital math |
| [ROADBLOCKS.md](ROADBLOCKS.md) | Every major failure mode, addressed in advance |
| [RESOURCES.md](RESOURCES.md) | Official programs, lenders, ADU, tax, public records |
| [LEGAL_AND_ETHICS.md](LEGAL_AND_ETHICS.md) | Occupancy, scraping, landlord, unpermitted work |
| [checklists/](checklists/) | Pre-offer and month-13 conversion |
| [agent/](agent/) | Ethical deal-scout skeleton (public sources + manual MLS ingest) |
| [models/cashflow_template.csv](models/cashflow_template.csv) | Underwriting worksheet |

## Fast start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp agent/config.example.yaml agent/config.yaml
python -m agent.main --help
```

## Status

Built as a planning + research system, not a live bidding bot. Wire it to a licensed agent’s listing export and official public-record feeds before you treat any “deal score” as real.
