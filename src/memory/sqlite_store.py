"""Repo memory scaffold."""

from __future__ import annotations


def describe_store() -> dict:
    return {
        "status": "scaffold",
        "backend": "sqlite",
        "purpose": "Store repo profiles, cooldowns, and prior decisions.",
    }
