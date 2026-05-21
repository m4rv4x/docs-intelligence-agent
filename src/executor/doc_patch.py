"""Documentation patch scaffold."""

from __future__ import annotations


def draft_patch(task: dict) -> dict:
    return {
        "status": "scaffold",
        "task": task,
        "next_step": "Implement minimal patch generation.",
    }
