# Deal scout (ethical)

This is not a stealth Zillow scraper. It is a scoring loop over:

1. A CSV your licensed agent is allowed to export.
2. Health checks against official program pages.
3. Optional future connectors: county open data, HUD Home Store downloads.

## Run

```bash
pip install -r requirements.txt
python -m agent.main --health
python -m agent.main
```

Replace `agent/data/manual_listings.csv` with real rows.

## What “agentic” should mean here

A useful weekly loop:

1. Agent exports new 2–4 unit / ADU listings.
2. Scorer ranks by units, DOM, price cuts, permit language.
3. You underwrite the top 5 in `models/cashflow_template.csv`.
4. Human submits offers. The bot never signs.

Grok (this conversation) can sit in that loop as the analyst. The repo is the durable memory.
