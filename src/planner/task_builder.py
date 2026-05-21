"""Task proposal helpers for small docs-intelligence actions."""

from __future__ import annotations


def build_next_task(observations: dict) -> dict:
    missing_docs = observations.get("missing_public_docs", [])
    if missing_docs:
        first_batch = ", ".join(missing_docs[:3])
        return {
            "status": "ready",
            "recommended_action": "add_missing_public_docs",
            "risk_level": "low",
            "reviewability": "high",
            "summary": f"Add or improve missing public docs: {first_batch}",
            "observations": observations,
        }

    return {
        "status": "noop",
        "recommended_action": "no_small_docs_gap_found",
        "risk_level": "low",
        "reviewability": "high",
        "summary": "No obvious missing public-docs gap found.",
        "observations": observations,
    }
