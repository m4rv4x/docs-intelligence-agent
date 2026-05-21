import tempfile
import unittest
from pathlib import Path

from src.observer.github_scan import assess_readme_quality, scan_repository
from src.planner.task_builder import build_next_task
from src.social.report_writer import render_observer_report


class ReadmeReportingTests(unittest.TestCase):
    def test_assess_readme_quality_flags_missing_expected_sections(self):
        readme = """# Demo Project

Short intro.

## Installation
Run setup.
"""

        result = assess_readme_quality(readme)

        self.assertEqual(result["score"], 2)
        self.assertIn("Usage", result["missing_sections"])
        self.assertIn("Validation", result["missing_sections"])
        self.assertIn("Roadmap", result["missing_sections"])
        self.assertIn("Short intro.", result["summary"])

    def test_scan_repository_includes_readme_quality_and_report_renders_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(
                "# Demo Project\n\nOne-line pitch.\n\n## Installation\nDo this.\n\n## Usage\nUse it.\n",
                encoding="utf-8",
            )
            (root / "src").mkdir()
            (root / "src" / "app.py").write_text("print('hi')\n", encoding="utf-8")

            observations = scan_repository(str(root))
            task = build_next_task(observations)
            report = render_observer_report(observations, task)

            self.assertEqual(observations["readme_quality"]["score"], 3)
            self.assertIn("Validation", observations["readme_quality"]["missing_sections"])
            self.assertIn("## Repo signal summary", report)
            self.assertIn("README quality score: 3/6", report)
            self.assertIn("Best next task", report)
            self.assertIn("add_missing_public_docs", report)


if __name__ == "__main__":
    unittest.main()
