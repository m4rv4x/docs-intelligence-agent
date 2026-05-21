"""Repository observation scaffold."""

from __future__ import annotations


def scan_repository(path: str) -> dict:
    return {
        "path": path,
        "status": "scaffold",
        "notes": ["Implement repo scanning heuristics here."],
    }
