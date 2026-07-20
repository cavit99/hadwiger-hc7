from __future__ import annotations

import hashlib
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tools import independent_labs as labs
from tools import proof_round as proof


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout.strip()


class IndependentLabsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        git(self.repo, "init", "--quiet")
        git(self.repo, "config", "user.name", "Test")
        git(self.repo, "config", "user.email", "test@example.invalid")

        target = "# Target\n\n## Exact theorem\n\nProve the frozen statement.\n"
        subtree = "## Exact theorem\n\nProve the frozen statement.\n"
        target_hash = hashlib.sha256(subtree.encode()).hexdigest()
        (self.repo / "target.md").write_text(target, encoding="utf-8")
        (self.repo / "brief.md").write_text("Solve the theorem completely.\n", encoding="utf-8")
        (self.repo / "context.md").write_text("A proved input.\n", encoding="utf-8")
        (self.repo / ".gitignore").write_text(".cache/\n", encoding="utf-8")
        config = f'''schema_version = 1
id_prefix = "test"
brief_file = "brief.md"
max_context_bytes = 65536
context_files = ["target.md", "context.md"]

[target]
file = "target.md"
heading = "Exact theorem"
sha256 = "{target_hash}"

[providers.codex]
model = "codex-test"
effort = "ultra"

[providers.grok]
model = "grok-test"
effort = "high"
'''
        (self.repo / "config.toml").write_text(config, encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "--quiet", "-m", "fixture")

        self.old_labs_root = labs.REPO_ROOT, labs.LAB_ROOT
        self.old_proof_root = proof.REPO_ROOT, proof.ROUND_ROOT
        labs.REPO_ROOT = self.repo
        labs.LAB_ROOT = self.repo / ".cache" / "research" / "labs"
        proof.REPO_ROOT = self.repo
        proof.ROUND_ROOT = self.repo / ".cache" / "research" / "rounds"

    def tearDown(self) -> None:
        labs.REPO_ROOT, labs.LAB_ROOT = self.old_labs_root
        proof.REPO_ROOT, proof.ROUND_ROOT = self.old_proof_root
        self.temporary.cleanup()

    def test_prepare_creates_independent_symmetric_clones(self) -> None:
        lab_id = labs.prepare(self.repo / "config.toml", "pair-one")
        labs.provision(lab_id, "codex")
        labs.provision(lab_id, "grok")
        root, manifest = labs.load_lab(lab_id)
        self.assertEqual(manifest["base_commit"], git(self.repo, "rev-parse", "HEAD"))

        prompts = []
        goals = []
        workspaces = {}
        for provider in labs.PROVIDERS:
            workspace = root / provider / "workspace"
            workspaces[provider] = workspace
            prompts.append((workspace / labs.PROMPT).read_bytes())
            goals.append((workspace / labs.GOAL).read_bytes())
            self.assertEqual(git(workspace, "remote"), "")
            self.assertEqual(
                git(workspace, "branch", "--show-current"),
                f"experiment/pair-one-{provider}",
            )
            self.assertFalse((workspace / ".git" / "objects" / "info" / "alternates").exists())
            self.assertTrue((workspace / ".git").is_dir())
            self.assertEqual(git(workspace, "status", "--porcelain"), "")

        self.assertEqual(prompts[0], prompts[1])
        self.assertEqual(goals[0], goals[1])
        self.assertNotIn(b"structural", prompts[0])
        self.assertNotIn(b"falsifier", prompts[0])
        self.assertIn(b"Public web research is permitted", prompts[0])
        self.assertIn(b"Python experiments", prompts[0])
        self.assertIn(b"Evidence gates required before `no_result`", goals[0])

        (workspaces["codex"] / "private-note.md").write_text("codex only\n", encoding="utf-8")
        self.assertFalse((workspaces["grok"] / "private-note.md").exists())

    def test_dirty_source_and_duplicate_id_are_refused(self) -> None:
        (self.repo / "untracked.txt").write_text("dirty\n", encoding="utf-8")
        with self.assertRaises(proof.RoundError):
            labs.prepare(self.repo / "config.toml", "dirty")
        (self.repo / "untracked.txt").unlink()

        labs.prepare(self.repo / "config.toml", "duplicate")
        with self.assertRaises(labs.LabError):
            labs.prepare(self.repo / "config.toml", "duplicate")

    def test_commands_are_symmetric_primary_research_launches(self) -> None:
        lab_id = labs.prepare(self.repo / "config.toml", "commands")
        labs.provision(lab_id, "codex")
        labs.provision(lab_id, "grok")
        root, manifest = labs.load_lab(lab_id)
        codex = labs.provider_command(
            "codex",
            root / manifest["lanes"]["codex"]["workspace"],
            manifest["provider_settings"]["codex"],
        )
        grok = labs.provider_command(
            "grok",
            root / manifest["lanes"]["grok"]["workspace"],
            manifest["provider_settings"]["grok"],
        )
        self.assertIn("codex-test", codex)
        self.assertIn("grok-test", grok)
        self.assertIn("workspace-write", codex)
        self.assertIn("strict", grok)
        self.assertEqual(codex[-1], grok[-1])
        self.assertIn(labs.GOAL, codex[-1])
        self.assertNotIn("review", codex[-1].lower())
        self.assertNotIn("fals", grok[-1].lower())

        output = io.StringIO()
        with redirect_stdout(output):
            labs.show_goal("commands", "grok")
        self.assertIn("**Status:** active", output.getvalue())
        self.assertIn("- [ ] Search relevant primary literature", output.getvalue())

        grok_workspace = root / manifest["lanes"]["grok"]["workspace"]
        (grok_workspace / labs.RESULT).write_text(
            "# Result\n\n**Outcome:** `no_result`\n", encoding="utf-8"
        )
        output = io.StringIO()
        with redirect_stdout(output):
            labs.show_status("commands")
        self.assertIn("premature no_result: evidence gates incomplete", output.getvalue())

        goal = grok_workspace / labs.GOAL
        goal.write_text(
            goal.read_text(encoding="utf-8")
            .replace("**Status:** active", "**Status:** exhausted")
            .replace("- [ ]", "- [x]"),
            encoding="utf-8",
        )
        output = io.StringIO()
        with redirect_stdout(output):
            labs.show_status("commands")
        self.assertNotIn("premature no_result", output.getvalue())

    def test_each_provider_can_be_provisioned_without_the_other(self) -> None:
        lab_id = labs.prepare(self.repo / "config.toml", "one-lane")
        labs.provision(lab_id, "codex")
        _, manifest = labs.load_lab(lab_id)
        self.assertIn("codex", manifest["lanes"])
        self.assertNotIn("grok", manifest["lanes"])

        labs.provision(lab_id, "grok")
        _, manifest = labs.load_lab(lab_id)
        self.assertEqual(set(manifest["lanes"]), {"codex", "grok"})

    def test_legacy_lab_command_does_not_reference_missing_goal(self) -> None:
        lab_id = labs.prepare(self.repo / "config.toml", "legacy")
        labs.provision(lab_id, "grok")
        root, manifest = labs.load_lab(lab_id)
        workspace = root / manifest["lanes"]["grok"]["workspace"]
        (workspace / labs.GOAL).unlink()

        output = io.StringIO()
        with redirect_stdout(output):
            labs.show_commands("legacy", "grok")
        self.assertIn(f"Read {labs.PROMPT} completely", output.getvalue())
        self.assertNotIn(labs.GOAL, output.getvalue())

    def test_runtime_prepares_isolated_python_environment(self) -> None:
        lab_id = labs.prepare(self.repo / "config.toml", "runtime")
        labs.provision(lab_id, "grok")
        root, manifest = labs.load_lab(lab_id)
        workspace = root / manifest["lanes"]["grok"]["workspace"]

        with patch.object(labs.subprocess, "run") as run:
            output = io.StringIO()
            with redirect_stdout(output):
                labs.setup_runtime(lab_id, "grok")

        self.assertEqual(run.call_count, 2)
        self.assertEqual(
            run.call_args_list[0].args[0],
            [labs.sys.executable, "-m", "venv", str(workspace / ".venv")],
        )
        self.assertEqual(
            run.call_args_list[1].args[0][0],
            str(workspace / ".venv" / "bin" / "python"),
        )
        self.assertIn(str(workspace / ".venv"), output.getvalue())

    def test_cleanup_requires_marker_and_removes_only_one_pair(self) -> None:
        first = labs.prepare(self.repo / "config.toml", "first")
        second = labs.prepare(self.repo / "config.toml", "second")
        labs.cleanup(first)
        self.assertFalse(labs.safe_lab_path(first).exists())
        self.assertTrue(labs.safe_lab_path(second).exists())

        marker = labs.safe_lab_path(second) / labs.MARKER
        marker.write_text("wrong\n", encoding="utf-8")
        with self.assertRaises(labs.LabError):
            labs.cleanup(second)


if __name__ == "__main__":
    unittest.main()
