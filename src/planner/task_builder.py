"""Task proposal scaffold."""

from __future__ import annotations


def build_next_task(observations: dict) -> dict:
    return {
        "status": "scaffold",
        "recommended_action": "Implement ranking logic.",
        "observations": observations,
    }
