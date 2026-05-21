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

EXPECTED_README_SECTIONS = [
    "Installation",
    "Usage",
    "Validation",
    "Architecture",
    "Roadmap",
]


def assess_readme_quality(content: str) -> dict:
    lines = [line.strip() for line in content.splitlines()]
    summary = next(
        (line for line in lines if line and not line.startswith("#")),
        "",
    )
    present_sections = [
        section for section in EXPECTED_README_SECTIONS if f"## {section}" in content
    ]
    missing_sections = [
        section for section in EXPECTED_README_SECTIONS if section not in present_sections
    ]
    score = (1 if summary else 0) + len(present_sections)

    return {
        "score": score,
        "max_score": 6,
        "summary": summary,
        "present_sections": present_sections,
        "missing_sections": missing_sections,
    }


def scan_repository(path: str) -> dict:
    root = Path(path)
    markdown_files = list(root.rglob("*.md"))
    python_files = list(root.rglob("*.py"))

    missing_public_docs = [
        doc for doc in REQUIRED_PUBLIC_DOCS if not (root / doc).exists()
    ]

    has_readme = (root / "README.md").exists()
    readme_quality = (
        assess_readme_quality((root / "README.md").read_text(encoding="utf-8"))
        if has_readme
        else {
            "score": 0,
            "max_score": 6,
            "summary": "",
            "present_sections": [],
            "missing_sections": EXPECTED_README_SECTIONS.copy(),
        }
    )

    return {
        "path": str(root),
        "status": "ok",
        "has_readme": has_readme,
        "has_docs_dir": (root / "docs").is_dir(),
        "markdown_file_count": len(markdown_files),
        "python_file_count": len(python_files),
        "missing_public_docs": missing_public_docs,
        "readme_quality": readme_quality,
    }
