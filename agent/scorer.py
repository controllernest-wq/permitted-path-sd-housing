"""Score listings for the permitted 12-month live-in then rent/sell path."""

from __future__ import annotations

from typing import Any


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(str(value).replace(",", "").strip() or default)
    except ValueError:
        return default


def _to_int(value: Any, default: int = 0) -> int:
    try:
        return int(float(str(value).replace(",", "").strip() or default))
    except ValueError:
        return default


def _to_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def score_listing(row: dict[str, Any], cfg: dict[str, Any]) -> dict[str, Any]:
    price = _to_float(row.get("price"))
    units = _to_int(row.get("units"), 1)
    adu = _to_bool(row.get("adu"))
    dom = _to_int(row.get("dom"))
    cut = _to_float(row.get("price_cut_pct"))
    notes = (row.get("notes") or "").lower()
    text = f"{notes} {row.get('address', '')}".lower()

    score = 0.0
    reasons: list[str] = []
    vetoes: list[str] = []

    max_price = _to_float(cfg.get("max_price"), 1_104_000)
    if price <= 0:
        vetoes.append("missing price")
    elif price > max_price:
        vetoes.append(f"over max_price {max_price:.0f}")
    else:
        score += max(0, 20 * (1 - price / max_price))

    if units >= 2:
        score += 25
        reasons.append(f"{units} legal units — FHA house-hack shape")
    elif adu:
        score += 18
        reasons.append("ADU flag — verify permits")
    else:
        score += 5
        reasons.append("1 unit — only works with roommate or future ADU capital")

    if dom >= 45:
        score += 10
        reasons.append(f"DOM {dom}")
    if cut >= 8:
        score += 10
        reasons.append(f"price cut {cut}%")

    for kw in cfg.get("prefer_keywords") or []:
        if kw.lower() in text:
            score += 3
            reasons.append(f"keyword:{kw}")

    for kw in cfg.get("avoid_keywords") or []:
        if kw.lower() in text:
            score -= 15
            reasons.append(f"avoid:{kw}")
            if "unpermitted" in kw.lower():
                vetoes.append("unpermitted mentioned")

    if units > _to_int(cfg.get("max_units"), 4):
        vetoes.append("over 4 units — not FHA owner-oc 1-4")

    decision = "review" if not vetoes and score >= 25 else "pass" if vetoes else "watch"
    return {
        **row,
        "score": round(score, 1),
        "decision": decision,
        "reasons": "; ".join(reasons),
        "vetoes": "; ".join(vetoes),
    }
