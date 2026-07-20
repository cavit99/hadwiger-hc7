from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile
import textwrap
import unittest
from unittest import mock

from tools import proof_round


TARGET_HEADING = "Conjectural Theorem 3.1 (chromatic or paired-rooted `K_5`)"


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


def complete_candidate(outcome: str = "proof") -> dict[str, object]:
    return {
        "outcome": outcome,
        "claim": "Frozen target",
        "hypothesis_checklist": [{"hypothesis": "all", "justification": "checked"}],
        "numbered_argument": [{"step": 1, "statement": "argument", "uses": []}],
        "dependencies": [{"source": "context.md", "exact_statement": "input"}],
        "target_implication": "This proves the frozen target.",
        "well_founded_parameter": None,
        "strict_decrease_proof": None,
        "first_unresolved_inference": None,
        "artifacts": [],
        "trust_boundary": ["internal audit only"],
    }


class ProofRoundUnitTests(unittest.TestCase):
    def test_heading_subtree_includes_nested_sections_only(self) -> None:
        text = "# A\n## Target\nbody\n### Child\nmore\n## Next\nstop\n"
        self.assertEqual(
            proof_round.extract_heading_subtree(text, "Target"),
            "## Target\nbody\n### Child\nmore\n",
        )

    def test_heading_must_be_unique(self) -> None:
        with self.assertRaises(proof_round.RoundError):
            proof_round.extract_heading_subtree("## X\n## X\n", "X")

    def test_candidate_proof_is_admissible(self) -> None:
        self.assertTrue(proof_round.validate_candidate(complete_candidate())[0])

    def test_no_result_is_never_admissible(self) -> None:
        candidate = complete_candidate("no_result")
        candidate["first_unresolved_inference"] = "gap"
        self.assertFalse(proof_round.validate_candidate(candidate)[0])

    def test_strict_reduction_requires_rank_and_decrease(self) -> None:
        candidate = complete_candidate("strict_reduction")
        self.assertFalse(proof_round.validate_candidate(candidate)[0])
        candidate["well_founded_parameter"] = "number of host vertices"
        candidate["strict_decrease_proof"] = "strictly decreases"
        self.assertTrue(proof_round.validate_candidate(candidate)[0])

    def test_proof_cannot_retain_unresolved_inference(self) -> None:
        candidate = complete_candidate()
        candidate["first_unresolved_inference"] = "not proved"
        self.assertFalse(proof_round.validate_candidate(candidate)[0])

    def test_selector_cannot_choose_inadmissible_candidate(self) -> None:
        value = {"selected": "bad", "classifications": [], "selection_reason": "x"}
        with self.assertRaises(proof_round.RoundError):
            proof_round.validate_selector(value, {"good"})

    def test_green_referee_cannot_retain_blocker(self) -> None:
        value = {
            "verdict": "GREEN",
            "reconstruction": "ok",
            "blocking_findings": [{"claim": "gap"}],
            "hypothesis_checklist": [],
        }
        with self.assertRaises(proof_round.RoundError):
            proof_round.validate_referee(value)

    def test_wrapped_provider_json_is_normalized(self) -> None:
        candidate = complete_candidate()
        wrapped = json.dumps({"result": json.dumps(candidate)})
        self.assertEqual(proof_round.parse_provider_json("claude", wrapped), candidate)

    def test_selector_prompt_is_provider_blind(self) -> None:
        prompt = proof_round.selector_prompt("brief", {"candidate-abcd": complete_candidate()})
        for provider in proof_round.PROVIDERS:
            self.assertNotIn(provider, prompt.lower())

    def test_provider_commands_use_no_dangerous_flags(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            schema = root / "schema.json"
            prompt = root / "prompt.md"
            result = root / "result.json"
            proof_round.write_json(schema, proof_round.candidate_schema())
            prompt.write_text("prompt", encoding="utf-8")
            for provider in proof_round.PROVIDERS:
                command, _ = proof_round.provider_command(
                    provider, root, prompt, schema, result, {}
                )
                joined = " ".join(command)
                self.assertNotIn("dangerously", joined)
                self.assertNotIn("always-approve", joined)
                self.assertNotIn("bypassPermissions", joined)

    def test_external_artifacts_are_disabled_in_v1(self) -> None:
        candidate = complete_candidate()
        candidate["artifacts"] = ["not permitted"]
        self.assertFalse(proof_round.validate_candidate(candidate)[0])

    def test_environment_does_not_forward_common_tokens(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"GH_TOKEN": "secret", "OPENAI_API_KEY": "secret", "PATH": "/bin"},
            clear=True,
        ):
            environment = proof_round.sanitized_environment()
        self.assertNotIn("GH_TOKEN", environment)
        self.assertNotIn("OPENAI_API_KEY", environment)
        self.assertEqual(environment["PATH"], "/bin")


class ProofRoundIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        self.root.mkdir()
        git(self.root, "init", "-q")
        git(self.root, "config", "user.email", "proof-round@example.invalid")
        git(self.root, "config", "user.name", "Proof Round Test")
        (self.root / ".gitignore").write_text(".cache/\n", encoding="utf-8")
        (self.root / "active").mkdir()
        target = self.root / "active" / "target.md"
        target.write_text(
            f"# Frontier\n\n### {TARGET_HEADING}\n\nTarget body.\n\n### Next\n\nOther.\n",
            encoding="utf-8",
        )
        (self.root / "tools" / "proof_rounds").mkdir(parents=True)
        brief = self.root / "tools" / "proof_rounds" / "brief.md"
        brief.write_text("# Brief\n\nProve the target.\n", encoding="utf-8")
        subtree = proof_round.extract_heading_subtree(target.read_text(), TARGET_HEADING)
        digest = hashlib.sha256(subtree.encode()).hexdigest()
        config = self.root / "tools" / "proof_rounds" / "round.toml"
        config.write_text(
            textwrap.dedent(
                f'''\
                schema_version = 1
                id_prefix = "test-round"
                brief_file = "tools/proof_rounds/brief.md"
                timeout_seconds = 60
                max_output_bytes = 1048576
                max_context_bytes = 1048576
                max_repairs = 1
                context_files = ["active/target.md"]

                [target]
                file = "active/target.md"
                heading = "{TARGET_HEADING}"
                sha256 = "{digest}"

                [providers.codex]
                model = "test-codex"
                [providers.claude]
                model = "test-claude"
                [providers.grok]
                model = "test-grok"

                [[labs]]
                provider = "codex"
                role = "structural"
                [[labs]]
                provider = "claude"
                role = "colouring"
                [[labs]]
                provider = "grok"
                role = "falsifier"

                [selector]
                provider = "codex"
                [review]
                provider_pool = ["codex", "claude", "grok"]
                required = 2
                exclude_selected_author = true
                '''
            ),
            encoding="utf-8",
        )
        git(self.root, "add", ".")
        git(self.root, "commit", "-qm", "fixture")
        self.config = config
        self.fake_bin = Path(self.temporary.name) / "bin"
        self.fake_bin.mkdir()
        self._install_fake_providers()
        self.path_patch = mock.patch.dict(
            os.environ,
            {"PATH": f"{self.fake_bin}:{os.environ.get('PATH', '')}"},
            clear=False,
        )
        self.path_patch.start()
        self.root_patch = mock.patch.object(proof_round, "REPO_ROOT", self.root)
        self.round_patch = mock.patch.object(
            proof_round, "ROUND_ROOT", self.root / ".cache" / "research" / "rounds"
        )
        self.root_patch.start()
        self.round_patch.start()

    def tearDown(self) -> None:
        self.round_patch.stop()
        self.root_patch.stop()
        self.path_patch.stop()
        self.temporary.cleanup()

    def _install_fake_providers(self) -> None:
        script = textwrap.dedent(
            '''\
            #!/usr/bin/env python3
            import json, os, pathlib, re, sys, time

            if "--version" in sys.argv:
                print(pathlib.Path(sys.argv[0]).name + " test-version")
                raise SystemExit(0)
            if "--prompt-file" in sys.argv:
                prompt = pathlib.Path(sys.argv[sys.argv.index("--prompt-file") + 1]).read_text()
            else:
                prompt = sys.stdin.read()
            if "OVERFLOW" in prompt:
                print("x" * 70000)
                raise SystemExit(0)
            if "SLEEP" in prompt:
                time.sleep(5)
            if "fresh, provider-blinded selector" in prompt:
                ids = re.findall(r"candidate-[0-9a-f]+", prompt)
                result = {
                    "selected": ids[0] if ids else None,
                    "classifications": [
                        {"candidate": candidate, "admissible": True, "reason": "complete"}
                        for candidate in ids
                    ],
                    "selection_reason": "select the contract-complete candidate",
                }
            elif "cold mathematical referee" in prompt:
                result = {
                    "verdict": "GREEN",
                    "reconstruction": "independently reconstructed",
                    "blocking_findings": [],
                    "hypothesis_checklist": [
                        {"hypothesis": "all", "verdict": "PASS", "reason": "checked"}
                    ],
                }
            else:
                provider = pathlib.Path(sys.argv[0]).name
                result = {
                    "outcome": "proof" if provider == "codex" else "no_result",
                    "claim": "Frozen target",
                    "hypothesis_checklist": [{"hypothesis": "all", "justification": "checked"}],
                    "numbered_argument": [{"step": 1, "statement": "argument", "uses": []}],
                    "dependencies": [{"source": "context", "exact_statement": "input"}],
                    "target_implication": "This proves the frozen target.",
                    "well_founded_parameter": None,
                    "strict_decrease_proof": None,
                    "first_unresolved_inference": None if provider == "codex" else "no proof",
                    "artifacts": [],
                    "trust_boundary": ["internal"],
                }
            payload = json.dumps(result)
            if "--output-last-message" in sys.argv:
                pathlib.Path(sys.argv[sys.argv.index("--output-last-message") + 1]).write_text(payload)
                print("event log")
            else:
                print(payload)
            '''
        )
        for provider in proof_round.PROVIDERS:
            path = self.fake_bin / provider
            path.write_text(script, encoding="utf-8")
            path.chmod(path.stat().st_mode | stat.S_IXUSR)

    def test_prepare_and_full_fake_round_leave_source_clean(self) -> None:
        frozen = proof_round.prepare_round(self.config, "test-round-001")
        self.assertEqual(frozen["base_commit"], git(self.root, "rev-parse", "HEAD"))
        clone = proof_round.ROUND_ROOT / frozen["round_id"] / "snapshot"
        self.assertEqual(git(clone, "rev-parse", "HEAD"), frozen["base_commit"])
        self.assertFalse((clone / ".git" / "objects" / "info" / "alternates").exists())
        self.assertEqual(git(clone, "remote"), "")
        proof_round.run_round(frozen["round_id"])
        state = proof_round.read_json(
            proof_round.ROUND_ROOT / frozen["round_id"] / proof_round.STATE_NAME
        )
        self.assertEqual(state["stage"], "complete_green")
        self.assertEqual(git(self.root, "status", "--porcelain=v1", "--untracked-files=all"), "")

    def test_dirty_repository_is_refused(self) -> None:
        (self.root / "untracked.txt").write_text("dirty", encoding="utf-8")
        with self.assertRaises(proof_round.RoundError):
            proof_round.prepare_round(self.config, "test-round-dirty")

    def test_target_hash_drift_is_refused(self) -> None:
        config = self.config.read_text().replace(
            re.search(r'sha256 = "([0-9a-f]+)"', self.config.read_text()).group(1), "0" * 64
        )
        self.config.write_text(config, encoding="utf-8")
        git(self.root, "add", str(self.config.relative_to(self.root)))
        git(self.root, "commit", "-qm", "drift config")
        with self.assertRaises(proof_round.RoundError):
            proof_round.prepare_round(self.config, "test-round-drift")

    def test_existing_round_id_is_refused(self) -> None:
        proof_round.prepare_round(self.config, "test-round-repeat")
        with self.assertRaises(proof_round.RoundError):
            proof_round.prepare_round(self.config, "test-round-repeat")

    def test_cleanup_removes_only_marked_round(self) -> None:
        proof_round.prepare_round(self.config, "test-round-cleanup")
        unrelated = self.root / ".cache" / "keep.txt"
        unrelated.parent.mkdir(exist_ok=True)
        unrelated.write_text("keep", encoding="utf-8")
        proof_round.cleanup_round("test-round-cleanup")
        self.assertTrue(unrelated.exists())

    def test_round_lock_refuses_concurrent_operator(self) -> None:
        proof_round.prepare_round(self.config, "test-round-lock")
        round_dir = proof_round.ROUND_ROOT / "test-round-lock"
        with proof_round.round_lock(round_dir):
            with self.assertRaises(proof_round.RoundError):
                with proof_round.round_lock(round_dir):
                    pass

    def test_output_overflow_fails_closed(self) -> None:
        stage = self.root / ".cache" / "overflow"
        prompt = stage / "prompt.md"
        schema = stage / "schema.json"
        stage.mkdir(parents=True)
        prompt.write_text("OVERFLOW", encoding="utf-8")
        proof_round.write_json(schema, proof_round.candidate_schema())
        with self.assertRaises(proof_round.RoundError):
            proof_round.invoke_provider(
                "codex", self.root, prompt, schema, stage, {}, 10, 65536
            )

    def test_timeout_terminates_provider_group(self) -> None:
        stage = self.root / ".cache" / "timeout"
        prompt = stage / "prompt.md"
        schema = stage / "schema.json"
        stage.mkdir(parents=True)
        prompt.write_text("SLEEP", encoding="utf-8")
        proof_round.write_json(schema, proof_round.candidate_schema())
        with self.assertRaises(proof_round.RoundError):
            proof_round.invoke_provider(
                "codex", self.root, prompt, schema, stage, {}, 1, 65536
            )
        self.assertFalse(proof_round.ACTIVE_PROCESSES)

    def test_unknown_configuration_key_is_refused(self) -> None:
        self.config.write_text(self.config.read_text() + "\nmisspelled = true\n", encoding="utf-8")
        with self.assertRaises(proof_round.RoundError):
            proof_round.load_config(self.config)


if __name__ == "__main__":
    unittest.main()
