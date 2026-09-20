# Permitted Path: Vegas / Palm Springs / Phoenix house-hack

**Goal:** Good credit, little of your own cash, live in it 12 months, then rent or sell, drive housing cost toward zero — inside **Las Vegas metro, Palm Springs metro, or Phoenix metro only**.

Repo: https://github.com/controllernest-wq/permitted-path-sd-housing

## Rank for this plan

1. **Las Vegas metro** — best shot at FHA duplex math + NV DPA that allows 1–4 units.
2. **Phoenix metro** — more buildings, strong DPA; watch 3–4 unit exclusions on Home Plus.
3. **Palm Springs metro** — CA programs and higher FHA cap; seasonal rents + CA landlord law.

Read [MARKETS.md](MARKETS.md) before [PLAN.md](PLAN.md).

## Non-negotiables

- Real occupancy (FHA: ~60 days in, ~12 months stay).
- Legal units only.
- Forgivable DPA is a *stay bonus*. Leaving at month 13 usually means **repay the second**, not “keep the grant.”
- Section 121 tax-free sale needs ~**24 months** use, not 12.
- No Zillow/MLS ToS scrapers. Agent export + official pages only.

## Repo map

| File | Use |
|---|---|
| [MARKETS.md](MARKETS.md) | Three-metro rules, DPA, FHA limits |
| [PLAN.md](PLAN.md) | Playbook |
| [ROADBLOCKS.md](ROADBLOCKS.md) | Failure modes |
| [RESOURCES.md](RESOURCES.md) | Official links |
| [LEGAL_AND_ETHICS.md](LEGAL_AND_ETHICS.md) | Occupancy + scraping |
| [checklists/](checklists/) | Offer and month-13 |
| [agent/](agent/) | Score an agent CSV |
| [models/cashflow_template.csv](models/cashflow_template.csv) | Underwrite |

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m agent.main --health
python -m agent.main
```
