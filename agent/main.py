"""CLI: health-check official program pages and score a manual listing export."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import yaml
from rich.console import Console
from rich.table import Table

from agent.scorer import score_listing
from agent.sources import healthcheck_programs, load_manual_csv

console = Console()


def load_config(path: Path) -> dict:
    if not path.exists():
        example = path.parent / "config.example.yaml"
        return yaml.safe_load(example.read_text()) if example.exists() else {}
    return yaml.safe_load(path.read_text()) or {}


def cmd_health(cfg: dict) -> None:
    rows = healthcheck_programs(cfg.get("user_agent", "permitted-path-sd-housing"))
    table = Table(title="Official source health")
    table.add_column("url")
    table.add_column("status")
    table.add_column("ok")
    for row in rows:
        table.add_row(row["url"], str(row.get("status")), str(row.get("ok")))
    console.print(table)


def cmd_score(cfg: dict, out: Path | None) -> None:
    src = cfg.get("sources", {}).get("manual_csv", "agent/data/manual_listings.csv")
    listings = load_manual_csv(src)
    scored = [score_listing(row, cfg) for row in listings]
    scored.sort(key=lambda r: r["score"], reverse=True)

    table = Table(title="Permitted-path deal scores")
    for col in ("address", "city", "price", "units", "score", "decision", "vetoes"):
        table.add_column(col)
    for row in scored:
        table.add_row(
            str(row.get("address", "")),
            str(row.get("city", "")),
            str(row.get("price", "")),
            str(row.get("units", "")),
            str(row.get("score", "")),
            str(row.get("decision", "")),
            str(row.get("vetoes", "")),
        )
    console.print(table)

    if out:
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            if scored:
                writer = csv.DictWriter(f, fieldnames=list(scored[0].keys()))
                writer.writeheader()
                writer.writerows(scored)
        console.print(f"Wrote {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Permitted-path San Diego housing scout")
    parser.add_argument("--config", default="agent/config.yaml")
    parser.add_argument("--out", default="agent/data/out/scored.csv")
    parser.add_argument("--health", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    cfg = load_config(Path(args.config))

    if args.health:
        cmd_health(cfg)
        return
    if args.json:
        src = cfg.get("sources", {}).get("manual_csv", "agent/data/manual_listings.csv")
        print(json.dumps([score_listing(r, cfg) for r in load_manual_csv(src)], indent=2))
        return
    cmd_score(cfg, Path(args.out))


if __name__ == "__main__":
    main()
