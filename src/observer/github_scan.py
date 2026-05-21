"""Repository observation helpers for docs-intelligence scoring."""

from __future__ import annotations

from pathlib import Path

REQUIRED_PUBLIC_DOCS = [
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "docs/architecture.md",
    "docs/lessons-learned.md",
    "docs/failure-analysis.md",
]


def scan_repository(path: str) -> dict:
    root = Path(path)
    markdown_files = list(root.rglob("*.md"))
    python_files = list(root.rglob("*.py"))

    missing_public_docs = [
        doc for doc in REQUIRED_PUBLIC_DOCS if not (root / doc).exists()
    ]

    return {
        "path": str(root),
        "status": "ok",
        "has_readme": (root / "README.md").exists(),
        "has_docs_dir": (root / "docs").is_dir(),
        "markdown_file_count": len(markdown_files),
        "python_file_count": len(python_files),
        "missing_public_docs": missing_public_docs,
    }
