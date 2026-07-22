from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


from tools import ci_scope


def manifest(*records: dict[str, object]) -> dict[str, object]:
    return {"verifiers": list(records)}


ONE = {
    "id": "one",
    "path": "results/one_verify.py",
    "sha256": "one",
    "timeout": 10,
    "expected_stdout": ["PASS"],
}


class ScopeClassificationTests(unittest.TestCase):
    def test_prose_change_skips_tool_tests_and_verifiers(self) -> None:
        scope = ci_scope.classify_changes(
            "pull_request", {"results/proof.md"}, manifest(ONE), manifest(ONE)
        )
        self.assertFalse(scope.run_tool_tests)
        self.assertEqual("none", scope.verifier_mode)

    def test_tool_test_change_runs_tests_without_verifiers(self) -> None:
        scope = ci_scope.classify_changes(
            "pull_request",
            {"tools/tests/test_example.py"},
            manifest(ONE),
            manifest(ONE),
        )
        self.assertTrue(scope.run_tool_tests)
        self.assertEqual("none", scope.verifier_mode)

    def test_registered_script_or_record_change_selects_verifier(self) -> None:
        script_scope = ci_scope.classify_changes(
            "pull_request",
            {"results/one_verify.py"},
            manifest(ONE),
            manifest(ONE),
        )
        changed = dict(ONE, expected_stdout=["UPDATED"])
        record_scope = ci_scope.classify_changes(
            "pull_request",
            {"tools/research_manifest.toml"},
            manifest(changed),
            manifest(ONE),
        )
        self.assertEqual(
            ("selected", ("one",)),
            (script_scope.verifier_mode, script_scope.verifier_ids),
        )
        self.assertEqual(
            ("selected", ("one",)),
            (record_scope.verifier_mode, record_scope.verifier_ids),
        )

    def test_unknown_mathematical_code_fails_closed_to_full(self) -> None:
        scope = ci_scope.classify_changes(
            "pull_request",
            {"barriers/shared_helper.py"},
            manifest(ONE),
            manifest(ONE),
        )
        self.assertEqual("full", scope.verifier_mode)

    def test_runner_requirement_workflow_or_removed_record_runs_full(self) -> None:
        for path in ci_scope.FULL_VERIFIER_INPUTS:
            with self.subTest(path=path):
                scope = ci_scope.classify_changes(
                    "pull_request", {path}, manifest(ONE), manifest(ONE)
                )
                self.assertEqual("full", scope.verifier_mode)
        removed = ci_scope.classify_changes(
            "pull_request",
            {"tools/research_manifest.toml"},
            manifest(),
            manifest(ONE),
        )
        self.assertEqual("full", removed.verifier_mode)

    def test_scheduled_and_manual_runs_are_full(self) -> None:
        for event in ("schedule", "workflow_dispatch"):
            with self.subTest(event=event):
                scope = ci_scope.classify_changes(
                    event, set(), manifest(ONE), manifest(ONE)
                )
                self.assertEqual("full", scope.verifier_mode)


class ScopeGitTests(unittest.TestCase):
    def test_determine_scope_compares_committed_base(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tools").mkdir()
            (root / "results").mkdir()
            (root / "tools/research_manifest.toml").write_text(
                "[[verifiers]]\n"
                'id = "one"\n'
                'path = "results/one_verify.py"\n'
                'sha256 = "one"\n'
                "timeout = 10\n"
                'expected_stdout = ["PASS"]\n',
                encoding="utf-8",
            )
            verifier = root / "results/one_verify.py"
            verifier.write_text("print('PASS')\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(
                ["git", "config", "user.name", "Test"], cwd=root, check=True
            )
            subprocess.run(
                ["git", "config", "user.email", "test@example.invalid"],
                cwd=root,
                check=True,
            )
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=root, check=True)
            base = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip()
            verifier.write_text("print('UPDATED')\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "change"], cwd=root, check=True)

            scope = ci_scope.determine_scope(root, "pull_request", base)
            self.assertEqual("selected", scope.verifier_mode)
            self.assertEqual(("one",), scope.verifier_ids)


if __name__ == "__main__":
    unittest.main()
