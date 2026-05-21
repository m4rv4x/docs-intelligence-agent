import tempfile
import unittest
from pathlib import Path

from src.observer.github_scan import scan_repository
from src.planner.task_builder import build_next_task


class DocsIntelligenceTests(unittest.TestCase):
    def test_scan_repository_reports_docs_signal_and_missing_public_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Example\n", encoding="utf-8")
            (root / "docs").mkdir()
            (root / "docs" / "architecture.md").write_text("# Architecture\n", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / "app.py").write_text("print('hi')\n", encoding="utf-8")

            result = scan_repository(str(root))

            self.assertEqual(result["status"], "ok")
            self.assertTrue(result["has_readme"])
            self.assertTrue(result["has_docs_dir"])
            self.assertEqual(result["python_file_count"], 1)
            self.assertEqual(result["markdown_file_count"], 2)
            self.assertIn("CHANGELOG.md", result["missing_public_docs"])
            self.assertIn("ROADMAP.md", result["missing_public_docs"])
            self.assertIn("docs/lessons-learned.md", result["missing_public_docs"])

    def test_build_next_task_prioritizes_missing_public_docs_as_small_reviewable_work(self):
        observations = {
            "status": "ok",
            "path": "/tmp/example",
            "missing_public_docs": ["CHANGELOG.md", "ROADMAP.md"],
            "has_readme": True,
            "has_docs_dir": False,
            "python_file_count": 3,
            "markdown_file_count": 1,
        }

        task = build_next_task(observations)

        self.assertEqual(task["status"], "ready")
        self.assertEqual(task["recommended_action"], "add_missing_public_docs")
        self.assertEqual(task["risk_level"], "low")
        self.assertEqual(task["reviewability"], "high")
        self.assertIn("CHANGELOG.md", task["summary"])


if __name__ == "__main__":
    unittest.main()
