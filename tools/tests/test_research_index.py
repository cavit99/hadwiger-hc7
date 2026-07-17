from __future__ import annotations

import hashlib
import sqlite3
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import research_index as index  # noqa: E402


class MiniRepository:
    def __init__(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="hc7-index-test-")
        self.root = Path(self.temporary.name)
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=self.root, check=True)
        (self.root / "active").mkdir()
        (self.root / "results").mkdir()
        (self.root / "archive").mkdir()
        (self.root / "tools").mkdir()
        self.write("README.md", "# Test\n\nHC_7 is not proved.\n")
        self.write("RESEARCH_LEDGER.md", "# Ledger\n\nHC_7 is not proved.\n")
        self.write("results/theorem.md", "# Theorem\n\nA proved sentence.\n")
        digest = hashlib.sha256((self.root / "results/theorem.md").read_bytes()).hexdigest()
        self.write(
            "results/theorem_audit.md",
            f"# Audit\n\n## Verdict\n\nGREEN\n\nSource hash: `{digest}`\n\n[Source](theorem.md)\n",
        )
        self.write("active/target.md", "# Target\n\nA conjectural target.\n")
        self.write(
            "active/INDEX.md",
            "# Index\n\n[Target](target.md)\n\n[Theorem](../results/theorem.md)\n",
        )
        self.write("archive/history.md", "# History\n\nA unique archival helicoid phrase.\n\n[Broken](missing.md)\n")
        self.write_manifest(digest)
        self.commit()

    def close(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_manifest(self, digest: str, relations: str = "") -> None:
        self.write(
            "tools/research_manifest.toml",
            textwrap.dedent(
                f"""
                schema_version = 1
                verifiers = []

                [project]
                status_authority = "RESEARCH_LEDGER.md"
                navigation_root = "active/INDEX.md"
                public_overview = "README.md"
                database = ".cache/research/index.sqlite"

                [[required_text]]
                file = "README.md"
                pattern = "HC_7.*not proved"

                [[required_text]]
                file = "RESEARCH_LEDGER.md"
                pattern = "HC_7.*not proved"

                [[claims]]
                id = "target"
                title = "Target"
                kind = "target"
                status = "active-target"
                source = "active/target.md"
                active = true
                allowed_exits = ["proof"]

                [[claims]]
                id = "theorem"
                title = "Theorem"
                kind = "theorem"
                status = "audited-green"
                source = "results/theorem.md"
                active = true
                audit = "results/theorem_audit.md"
                expected_source_sha256 = "{digest}"

                [[relations]]
                source = "target"
                target = "theorem"
                kind = "uses"

                {relations}
                """
            ).lstrip(),
        )

    def commit(self) -> None:
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=self.root, check=True)

    @property
    def manifest(self) -> Path:
        return self.root / "tools/research_manifest.toml"


class IntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = MiniRepository()

    def tearDown(self) -> None:
        self.repo.close()

    def errors(self) -> list[str]:
        return index.validate_repository(self.repo.root, self.repo.manifest)

    def test_valid_fixture_and_broken_archive_link(self) -> None:
        self.assertEqual([], self.errors())

    def test_changed_theorem_fails_hash_and_audit(self) -> None:
        self.repo.write("results/theorem.md", "# Theorem\n\nChanged.\n")
        errors = "\n".join(self.errors())
        self.assertIn("source hash drift", errors)
        self.assertIn("lacks current source hash", errors)

    def test_green_audit_without_exact_hash_fails(self) -> None:
        self.repo.write("results/theorem_audit.md", "# Audit\n\n## Verdict\n\nGREEN\n")
        errors = "\n".join(self.errors())
        self.assertIn("does not contain exact source hash", errors)

    def test_link_to_untracked_file_fails_but_untracked_prose_is_not_indexed(self) -> None:
        self.repo.write("active/untracked.md", "# Secret\n\nUntracked quasar phrase.\n")
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n[Target](target.md)\n[Theorem](../results/theorem.md)\n[Untracked](untracked.md)\n",
        )
        errors = "\n".join(self.errors())
        self.assertIn("missing or untracked", errors)
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n[Target](target.md)\n[Theorem](../results/theorem.md)\n",
        )
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        self.assertEqual([], index.search_index(database, '"Untracked quasar"', None, 10))

    def test_device_specific_path_anywhere_in_tracked_corpus_fails(self) -> None:
        device_path = "/" + "Users/example/private/file.md"
        self.repo.write("archive/history.md", f"See {device_path}\n")
        errors = "\n".join(self.errors())
        self.assertIn("device-specific path", errors)

    def test_proof_dependency_cycle_fails(self) -> None:
        digest = hashlib.sha256((self.repo.root / "results/theorem.md").read_bytes()).hexdigest()
        extra = textwrap.dedent(
            """
            [[relations]]
            source = "theorem"
            target = "target"
            kind = "uses"
            """
        )
        self.repo.write_manifest(digest, extra)
        self.assertIn("proof-dependency cycle", "\n".join(self.errors()))

    def test_authoritative_document_paths_cannot_be_redirected(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        manifest = manifest.replace('navigation_root = "active/INDEX.md"', 'navigation_root = "archive/history.md"')
        self.repo.manifest.write_text(manifest, encoding="utf-8")
        self.assertIn("navigation_root must remain active/INDEX.md", "\n".join(self.errors()))

    def test_index_includes_archive_and_searches_sections(self) -> None:
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        rows = index.search_index(database, '"archival helicoid"', "archive", 10)
        self.assertEqual("archive/history.md", rows[0][0])
        with sqlite3.connect(database) as connection:
            paths = {row[0] for row in connection.execute("SELECT path FROM documents")}
        self.assertNotIn("active/untracked.md", paths)

    def test_query_index_rebuilds_when_tracked_corpus_changes(self) -> None:
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        self.repo.write("archive/history.md", "# History\n\nA newly discovered octahedral phrase.\n")
        index.ensure_fresh_index(database, self.repo.root, self.repo.manifest)
        rows = index.search_index(database, '"octahedral phrase"', "archive", 10)
        self.assertEqual("archive/history.md", rows[0][0])


class MarkdownParserTests(unittest.TestCase):
    def test_fenced_links_are_ignored_and_multiline_links_are_parsed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "active").mkdir()
            (root / "results").mkdir()
            source = """# Heading

```
[Fake](../results/missing.md)
```

[A multiline
 link](../results/target.md#same-heading-1)
"""
            target = "# Same heading\n\n## Same heading\n\n## Same heading\n"
            (root / "active/source.md").write_text(source)
            (root / "results/target.md").write_text(target)
            tracked = {"active/source.md", "results/target.md"}
            anchors = {"results/target.md": {section.slug for section in index.extract_sections(target)}}
            links = index.extract_links(root, "active/source.md", source, tracked, anchors)
            self.assertEqual(1, len(links))
            self.assertTrue(links[0].valid)
            self.assertEqual("same-heading-1", links[0].fragment)


class VerifierRunnerTests(unittest.TestCase):
    def test_output_match_and_no_shell_interpretation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            script = root / "safe;touch-pwned.py"
            script.write_text("print('PASS')\n", encoding="utf-8")
            manifest = {
                "verifiers": [
                    {
                        "id": "safe",
                        "path": script.name,
                        "timeout": 2,
                        "expected_stdout": ["PASS"],
                    }
                ]
            }
            index.run_verifiers(root, manifest)
            self.assertFalse((root / "pwned.py").exists())

    def test_output_mismatch_and_timeout_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "wrong.py").write_text("print('WRONG')\n", encoding="utf-8")
            wrong = {"verifiers": [{"id": "wrong", "path": "wrong.py", "timeout": 2, "expected_stdout": ["PASS"]}]}
            with self.assertRaises(index.IntegrityError):
                index.run_verifiers(root, wrong)
            (root / "slow.py").write_text("import time\ntime.sleep(1)\n", encoding="utf-8")
            slow = {"verifiers": [{"id": "slow", "path": "slow.py", "timeout": 0.05, "expected_stdout": []}]}
            with self.assertRaises(index.IntegrityError):
                index.run_verifiers(root, slow)

    def test_unknown_selected_verifier_fails(self) -> None:
        with self.assertRaises(index.IntegrityError):
            index.run_verifiers(Path.cwd(), {"verifiers": []}, {"missing"})


if __name__ == "__main__":
    unittest.main()
