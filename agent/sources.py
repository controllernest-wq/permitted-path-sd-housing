"""Public and manual sources. No ToS-violating MLS scrapers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import httpx

HUD_HOMESTORE = "https://www.hudhomestore.gov/"
CALHFA_MYHOME = "https://www.calhfa.ca.gov/homebuyer/programs/myhome.htm"
SDHC_FTHB = "https://sdhc.org/housing-opportunities/first-time-homebuyers/"
GSFA_PLATINUM = "https://www.gsfahome.org/programs/dpa/platinum.shtml"
SD_IB400 = "https://www.sandiego.gov/development-services/forms-publications/information-bulletins/400"

PROGRAM_PAGES = {
    "calhfa_myhome": CALHFA_MYHOME,
    "sdhc_fthb": SDHC_FTHB,
    "gsfa_platinum": GSFA_PLATINUM,
    "sd_adu_ib400": SD_IB400,
    "hud_homestore": HUD_HOMESTORE,
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
