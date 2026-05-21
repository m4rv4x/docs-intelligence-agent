"""Markdown report generation for repository observer runs."""

from __future__ import annotations


def render_observer_report(observations: dict, task: dict) -> str:
    readme_quality = observations.get("readme_quality", {})
    missing_docs = observations.get("missing_public_docs", [])
    missing_readme_sections = readme_quality.get("missing_sections", [])

    missing_docs_text = ", ".join(missing_docs) if missing_docs else "None"
    missing_sections_text = (
        ", ".join(missing_readme_sections) if missing_readme_sections else "None"
    )

    return f"""## Repo signal summary
- Path: `{observations.get('path', '')}`
- Python files: {observations.get('python_file_count', 0)}
- Markdown files: {observations.get('markdown_file_count', 0)}
- README quality score: {readme_quality.get('score', 0)}/{readme_quality.get('max_score', 6)}

## Missing or weak public artifacts
- Missing public docs: {missing_docs_text}
- Missing README sections: {missing_sections_text}

## Best next task
- Action: `{task.get('recommended_action', 'unknown')}`
- Summary: {task.get('summary', '')}
- Risk: {task.get('risk_level', 'unknown')}
- Reviewability: {task.get('reviewability', 'unknown')}
"""
