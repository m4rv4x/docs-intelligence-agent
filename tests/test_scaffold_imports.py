from src.memory.sqlite_store import describe_store
from src.observer.github_scan import scan_repository
from src.planner.task_builder import build_next_task
from src.executor.doc_patch import draft_patch
from src.social.pr_writer import draft_pr_body


def test_scaffolds_return_structured_values():
    observations = scan_repository(".")
    task = build_next_task(observations)
    patch = draft_patch(task)
    store = describe_store()
    pr = draft_pr_body()

    assert observations["status"] == "scaffold"
    assert task["status"] == "scaffold"
    assert patch["status"] == "scaffold"
    assert store["backend"] == "sqlite"
    assert pr.startswith("## What changed")
