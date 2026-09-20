"""Public and manual sources. No ToS-violating MLS scrapers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import httpx

PROGRAM_PAGES = {
    "hud_limits": "https://www.hud.gov/program_offices/housing/sfh/lender/origination/mortgage_limits",
    "nv_hip": "https://www.homeispossiblenv.org/",
    "az_homeplus": "https://homeplusaz.com/",
    "calhfa_myhome": "https://www.calhfa.ca.gov/homebuyer/programs/myhome.htm",
    "rivco_hws": "https://rivcohws.org/housing-programs",
    "hud_homestore": "https://www.hudhomestore.gov/",
}


def load_manual_csv(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fetch_program_page(url: str, user_agent: str, timeout: float = 20.0) -> dict[str, Any]:
    headers = {"User-Agent": user_agent, "Accept": "text/html"}
    try:
        r = httpx.get(url, headers=headers, timeout=timeout, follow_redirects=True)
        return {
            "url": url,
            "status": r.status_code,
            "bytes": len(r.content),
            "ok": r.is_success,
        }
    except httpx.HTTPError as exc:
        return {"url": url, "status": None, "bytes": 0, "ok": False, "error": str(exc)}


def healthcheck_programs(user_agent: str) -> list[dict[str, Any]]:
    return [fetch_program_page(url, user_agent) for url in PROGRAM_PAGES.values()]
