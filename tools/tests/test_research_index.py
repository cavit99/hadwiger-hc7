from __future__ import annotations

import hashlib
import sqlite3
import subprocess
import sys
import tempfile
import textwrap
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
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
            "# Index\n\n## Primary target\n\n[Target](target.md)\n\n"
            "Selected audited inputs used across the active programme:\n\n"
            "- [Theorem](../results/theorem.md)\n\n"
            "Immediate barriers:\n\n## Other work\n",
        )
        self.write("archive/history.md", "# History\n\nA unique archival helicoid phrase.\n")
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

    def test_valid_fixture(self) -> None:
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

    def test_missing_required_manifest_section_fails_cleanly(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        self.repo.manifest.write_text(
            manifest.replace("verifiers = []\n", ""), encoding="utf-8"
        )
        errors = "\n".join(self.errors())
        self.assertIn("missing required top-level keys", errors)
        self.assertIn("verifiers", errors)

    def test_negative_green_mentions_are_not_positive_verdicts(self) -> None:
        digest = hashlib.sha256(
            (self.repo.root / "results/theorem.md").read_bytes()
        ).hexdigest()
        for verdict in (
            "Not GREEN.",
            "No GREEN verdict yet.",
            "GREEN is not the verdict.",
            "GREEN? No.",
            "GREEN / RED pending.",
            "GREEN. Not actually.",
            "GREEN. This verdict is not GREEN.",
            "GREEN for no audited claims.",
            "Verdict: GREEN / RED pending.",
        ):
            with self.subTest(verdict=verdict):
                self.repo.write(
                    "results/theorem_audit.md",
                    f"# Audit\n\n## Verdict\n\n{verdict}\n\nSource hash: `{digest}`\n",
                )
                errors = "\n".join(self.errors())
                self.assertIn("lacks an unambiguous opening GREEN verdict", errors)

    def test_explicit_positive_green_verdict_formats(self) -> None:
        for verdict in (
            "## Verdict\n\nGREEN.",
            "Final verdict: GREEN.",
            "Overall Verdict – GREEN.",
            "**Verdict:** **GREEN after repair.**",
            "**Verdict:** **GREEN.** The audited claim is correct.",
            "The GREEN verdict below applies.\n\n## Verdict\n\nGREEN.",
        ):
            with self.subTest(verdict=verdict):
                self.assertTrue(index._has_explicit_green_verdict(verdict))

    def test_link_to_untracked_file_fails_but_untracked_prose_is_not_indexed(self) -> None:
        self.repo.write("active/untracked.md", "# Secret\n\nUntracked quasar phrase.\n")
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n## Primary target\n\n[Target](target.md)\n\n"
            "Selected audited inputs used across the active programme:\n\n"
            "- [Theorem](../results/theorem.md)\n"
            "- [Untracked](untracked.md)\n\n"
            "Immediate barriers:\n\n## Other work\n",
        )
        errors = "\n".join(self.errors())
        self.assertIn("missing or untracked", errors)
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n## Primary target\n\n[Target](target.md)\n\n"
            "Selected audited inputs used across the active programme:\n\n"
            "- [Theorem](../results/theorem.md)\n\n"
            "Immediate barriers:\n\n## Other work\n",
        )
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        self.assertEqual([], index.search_index(database, '"Untracked quasar"', None, 10))

    def test_authored_artifact_link_in_historical_document_must_be_tracked(self) -> None:
        self.repo.write("barriers/untracked.md", "# Untracked barrier\n")
        self.repo.write(
            "archive/history.md",
            "# History\n\n[Barrier](../barriers/untracked.md)\n",
        )
        errors = "\n".join(self.errors())
        self.assertIn("archive/history.md:3: authored artifact reference", errors)
        self.assertIn("barriers/untracked.md", errors)
        self.assertIn("missing or untracked", errors)

    def test_inline_code_and_plain_authored_paths_must_be_tracked(self) -> None:
        self.repo.write(
            "archive/history.md",
            "# History\n\nUse `barriers/inline.md`.\n\nSee results/plain.md for details.\n",
        )
        errors = "\n".join(self.errors())
        self.assertIn("barriers/inline.md", errors)
        self.assertIn("results/plain.md", errors)

    def test_reference_style_authored_link_must_be_tracked(self) -> None:
        self.repo.write(
            "archive/history.md",
            "# History\n\nSee [the missing note][note].\n\n[note]: ../active/missing.md\n",
        )
        errors = "\n".join(self.errors())
        self.assertIn("archive/history.md:5: authored artifact reference", errors)
        self.assertIn("active/missing.md", errors)

    def test_fenced_code_math_and_external_urls_do_not_create_artifact_references(self) -> None:
        self.repo.write(
            "archive/history.md",
            textwrap.dedent(
                r"""
                # History

                ```text
                barriers/fenced-example.md
                ```

                $results/inline-math.md$

                $$barriers/same-line-display.md$$

                \[tools/same-line-tex.md\]

                $$
                archive/display-math.md
                $$

                https://example.invalid/results/external.md

                The tracked file is `results/theorem.md`.
                """
            ).lstrip(),
        )
        self.assertEqual([], self.errors())

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

    def test_uses_dependency_must_be_audited_green(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        manifest = manifest.replace('status = "audited-green"', 'status = "active-target"', 1)
        self.repo.manifest.write_text(manifest, encoding="utf-8")
        self.assertIn("must be audited-green", "\n".join(self.errors()))

    def test_primary_input_requires_direct_manifest_relation(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        relation = textwrap.dedent(
            """
            [[relations]]
            source = "target"
            target = "theorem"
            kind = "uses"
            """
        )
        self.repo.manifest.write_text(manifest.replace(relation, ""), encoding="utf-8")
        self.assertIn(
            "primary proved input results/theorem.md lacks a direct uses relation",
            "\n".join(self.errors()),
        )

    def test_primary_input_requires_active_audited_claim(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        manifest = manifest.replace(
            'source = "results/theorem.md"\nactive = true',
            'source = "results/theorem.md"\nactive = false',
        )
        self.repo.manifest.write_text(manifest, encoding="utf-8")
        self.assertIn(
            "primary proved input results/theorem.md lacks an active audited-green manifest claim",
            "\n".join(self.errors()),
        )

    def test_primary_barrier_requires_claim_and_guard_relation(self) -> None:
        self.repo.write("barriers/example.md", "# Barrier\n\nA warning.\n")
        subprocess.run(["git", "add", "barriers/example.md"], cwd=self.repo.root, check=True)
        index_text = (self.repo.root / "active/INDEX.md").read_text(encoding="utf-8")
        self.repo.write(
            "active/INDEX.md",
            index_text.replace(
                "Immediate barriers:\n",
                "Immediate barriers:\n\n- [Example](../barriers/example.md)\n",
            ),
        )
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        self.repo.manifest.write_text(
            manifest
            + textwrap.dedent(
                """

                [[claims]]
                id = "example-barrier"
                title = "Example barrier"
                kind = "barrier"
                status = "barrier"
                source = "barriers/example.md"
                active = true
                """
            ),
            encoding="utf-8",
        )
        self.assertIn(
            "primary barrier barriers/example.md lacks a direct guard relation",
            "\n".join(self.errors()),
        )

    def test_manifest_requires_exactly_one_active_target(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        self.repo.manifest.write_text(
            manifest.replace('status = "active-target"', 'status = "frozen"', 1),
            encoding="utf-8",
        )
        self.assertIn(
            "manifest must contain exactly one active target, found 0",
            "\n".join(self.errors()),
        )

    def test_primary_navigation_markers_must_be_ordered(self) -> None:
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n## Primary target\n\n[Target](target.md)\n\n"
            "Immediate barriers:\n\n"
            "Selected audited inputs used across the active programme:\n\n"
            "- [Theorem](../results/theorem.md)\n\n## Other work\n",
        )
        self.assertIn(
            "Selected audited inputs must precede Immediate barriers",
            "\n".join(self.errors()),
        )

    def test_stale_direct_uses_relation_must_remain_in_navigation(self) -> None:
        self.repo.write(
            "active/INDEX.md",
            "# Index\n\n## Primary target\n\n[Target](target.md)\n\n"
            "Selected audited inputs used across the active programme:\n\n"
            "Immediate barriers:\n\n## Other work\n",
        )
        self.assertIn(
            "direct uses relation target->theorem is absent from the primary proved-input list",
            "\n".join(self.errors()),
        )

    def test_stale_direct_guard_relation_must_remain_in_navigation(self) -> None:
        self.repo.write("barriers/example.md", "# Barrier\n\nA warning.\n")
        subprocess.run(["git", "add", "barriers/example.md"], cwd=self.repo.root, check=True)
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        self.repo.manifest.write_text(
            manifest
            + textwrap.dedent(
                """

                [[claims]]
                id = "example-barrier"
                title = "Example barrier"
                kind = "barrier"
                status = "barrier"
                source = "barriers/example.md"
                active = true

                [[relations]]
                source = "target"
                target = "example-barrier"
                kind = "guarded_by"
                """
            ),
            encoding="utf-8",
        )
        self.assertIn(
            "direct guard relation target->example-barrier is absent from the primary barrier list",
            "\n".join(self.errors()),
        )

    def test_context_pack_labels_manifest_closure_as_curated(self) -> None:
        manifest = index.load_manifest(self.repo.manifest)
        rendered = index.context_pack(manifest, "target")
        self.assertIn("## Curated proved-dependency closure", rendered)
        self.assertIn("not an independent completeness claim", rendered)
        self.assertNotIn("## Full proved dependency closure", rendered)

    def test_authoritative_document_paths_cannot_be_redirected(self) -> None:
        manifest = self.repo.manifest.read_text(encoding="utf-8")
        manifest = manifest.replace('navigation_root = "active/INDEX.md"', 'navigation_root = "archive/history.md"')
        self.repo.manifest.write_text(manifest, encoding="utf-8")
        self.assertIn("navigation_root must remain active/INDEX.md", "\n".join(self.errors()))

    def test_device_path_in_tracked_shell_script_fails(self) -> None:
        self.repo.write("tools/check.sh", "#!/bin/sh\ncd /" + "home/example/project\n")
        subprocess.run(["git", "add", "tools/check.sh"], cwd=self.repo.root, check=True)
        self.assertIn("device-specific path", "\n".join(self.errors()))

    def test_index_includes_archive_and_searches_sections(self) -> None:
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        rows = index.search_index(database, '"archival helicoid"', "archive", 10)
        self.assertEqual("archive/history.md", rows[0][0])
        with closing(sqlite3.connect(database)) as connection:
            paths = {row[0] for row in connection.execute("SELECT path FROM documents")}
        self.assertNotIn("active/untracked.md", paths)

    def test_query_index_rebuilds_when_tracked_corpus_changes(self) -> None:
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        self.repo.write("archive/history.md", "# History\n\nA newly discovered octahedral phrase.\n")
        index.ensure_fresh_index(database, self.repo.root, self.repo.manifest)
        rows = index.search_index(database, '"octahedral phrase"', "archive", 10)
        self.assertEqual("archive/history.md", rows[0][0])

    def test_concurrent_builds_use_isolated_temporary_databases(self) -> None:
        database = self.repo.root / "index.sqlite"
        with ThreadPoolExecutor(max_workers=2) as executor:
            outputs = list(
                executor.map(
                    lambda _item: index.build_index(
                        self.repo.root, self.repo.manifest, database
                    ),
                    range(2),
                )
            )
        self.assertEqual([database, database], outputs)
        with closing(sqlite3.connect(database)) as connection:
            schema_version = connection.execute(
                "SELECT value FROM meta WHERE key='schema_version'"
            ).fetchone()[0]
        self.assertEqual("2", schema_version)
        self.assertEqual([], list(database.parent.glob(f".{database.name}.*.tmp")))

    def test_discovery_source_provenance_drift_is_rejected(self) -> None:
        source = self.repo.root / "archive/history.md"
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        self.repo.write(
            "tools/research_discovery.toml",
            textwrap.dedent(
                f'''\
                schema_version = 1
                non_authoritative = true
                connections = []

                [[aliases]]
                id = "history-term"
                term = "helicoid"
                meaning = "test meaning"
                source_path = "archive/history.md"
                source_heading = "History"
                start_line = 1
                end_line = 3
                source_sha256 = "{digest}"
                extraction_method = "source-verified"
                confidence = 0.9
                review_status = "needs-review"
                evidence = "A unique archival helicoid phrase."
                false_positive_warning = "Do not expand unrelated geometry."
                '''
            ),
        )
        subprocess.run(
            ["git", "add", "tools/research_discovery.toml"],
            cwd=self.repo.root,
            check=True,
        )
        self.assertEqual([], self.errors())
        discovery = (self.repo.root / "tools/research_discovery.toml").read_text()
        self.repo.write(
            "tools/research_discovery.toml",
            discovery.replace(digest, "0" * 64),
        )
        self.assertIn("hash drift", "\n".join(self.errors()))

    def test_discovery_schema_rejects_unknown_keys_and_wrong_container_types(self) -> None:
        for body, expected in (
            (
                "schema_version = 1\nnon_authoritative = true\n"
                "connections = []\naliases = []\nconnectons = []\n",
                "top-level schema",
            ),
            (
                "schema_version = 1\nnon_authoritative = true\n"
                'connections = "not-an-array"\naliases = []\n',
                "connections must be an array of tables",
            ),
            (
                "schema_version = 1.0\nnon_authoritative = true\n"
                "connections = []\naliases = []\n",
                "schema_version must be integer 1",
            ),
        ):
            with self.subTest(expected=expected):
                self.repo.write("tools/research_discovery.toml", body)
                subprocess.run(
                    ["git", "add", "tools/research_discovery.toml"],
                    cwd=self.repo.root,
                    check=True,
                )
                self.assertIn(expected, "\n".join(self.errors()))

    def test_discovery_schema_rejects_misspelled_record_key_and_wrong_field_type(self) -> None:
        source = self.repo.root / "archive/history.md"
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        valid = textwrap.dedent(
            f'''\
            schema_version = 1
            non_authoritative = true
            connections = []

            [[aliases]]
            id = "history-term"
            term = "helicoid"
            meaning = "test meaning"
            source_path = "archive/history.md"
            source_heading = "History"
            start_line = 1
            end_line = 3
            source_sha256 = "{digest}"
            extraction_method = "source-verified"
            confidence = 0.9
            review_status = "needs-review"
            evidence = "A unique archival helicoid phrase."
            false_positive_warning = "Do not expand unrelated geometry."
            '''
        )
        for body, expected in (
            (
                valid.replace("source_heading", "source_headng"),
                "keys missing=['source_heading'] unknown=['source_headng']",
            ),
            (
                valid.replace("start_line = 1", 'start_line = "1"'),
                "aliases[1].start_line must be an integer",
            ),
        ):
            with self.subTest(expected=expected):
                self.repo.write("tools/research_discovery.toml", body)
                subprocess.run(
                    ["git", "add", "tools/research_discovery.toml"],
                    cwd=self.repo.root,
                    check=True,
                )
                self.assertIn(expected, "\n".join(self.errors()))

    def test_relation_evidence_heading_and_hash_drift_are_rejected(self) -> None:
        digest = hashlib.sha256((self.repo.root / "results/theorem.md").read_bytes()).hexdigest()
        evidence_sha = hashlib.sha256((self.repo.root / "archive/history.md").read_bytes()).hexdigest()
        relation = textwrap.dedent(
            f'''\
            [[relations]]
            source = "theorem"
            target = "target"
            kind = "related_to"
            evidence_source = "archive/history.md"
            evidence_heading = "History"
            evidence_start_line = 1
            evidence_end_line = 3
            evidence_sha256 = "{evidence_sha}"
            '''
        )
        self.repo.write_manifest(digest, relation)
        self.assertEqual([], self.errors())
        manifest = self.repo.manifest.read_text()
        self.repo.manifest.write_text(
            manifest.replace('evidence_heading = "History"', 'evidence_heading = "Missing"'),
            encoding="utf-8",
        )
        self.assertIn("evidence heading", "\n".join(self.errors()))
        self.repo.manifest.write_text(
            manifest.replace(evidence_sha, "0" * 64), encoding="utf-8"
        )
        self.assertIn("evidence hash drift", "\n".join(self.errors()))

    def test_evidence_interval_must_lie_in_unique_declared_heading_subtree(self) -> None:
        self.repo.write(
            "archive/history.md",
            "# History\n\n## Evidence\n\n### Detail\n\nNested.\n\n## Other\n\nOutside.\n",
        )
        evidence_sha = hashlib.sha256(
            (self.repo.root / "archive/history.md").read_bytes()
        ).hexdigest()
        theorem_sha = hashlib.sha256(
            (self.repo.root / "results/theorem.md").read_bytes()
        ).hexdigest()
        relation = textwrap.dedent(
            f'''\
            [[relations]]
            source = "theorem"
            target = "target"
            kind = "related_to"
            evidence_source = "archive/history.md"
            evidence_heading = "Evidence"
            evidence_start_line = 3
            evidence_end_line = 7
            evidence_sha256 = "{evidence_sha}"
            '''
        )
        self.repo.write_manifest(theorem_sha, relation)
        self.assertEqual([], self.errors())
        self.repo.manifest.write_text(
            self.repo.manifest.read_text().replace(
                "evidence_end_line = 7", "evidence_end_line = 11"
            ),
            encoding="utf-8",
        )
        self.assertIn("outside heading subtree", "\n".join(self.errors()))

        self.repo.write(
            "archive/history.md",
            "# History\n\n## Evidence\n\nFirst.\n\n## Evidence\n\nSecond.\n",
        )
        duplicate_sha = hashlib.sha256(
            (self.repo.root / "archive/history.md").read_bytes()
        ).hexdigest()
        self.repo.write_manifest(
            theorem_sha,
            relation.replace(evidence_sha, duplicate_sha).replace(
                "evidence_end_line = 7", "evidence_end_line = 5"
            ),
        )
        self.assertIn("heading is ambiguous", "\n".join(self.errors()))

    def test_report_generation_is_deterministic_across_clean_builds(self) -> None:
        first = self.repo.root / "first" / "index.sqlite"
        second = self.repo.root / "second" / "index.sqlite"
        manifest = index.load_manifest(self.repo.manifest)
        index.build_index(self.repo.root, self.repo.manifest, first)
        first_reports = index.generate_reports(self.repo.root, manifest, first)
        first_content = {path.name: path.read_bytes() for path in first_reports}
        index.build_index(self.repo.root, self.repo.manifest, second)
        second_reports = index.generate_reports(self.repo.root, manifest, second)
        second_content = {path.name: path.read_bytes() for path in second_reports}
        self.assertEqual(first_content, second_content)

    def test_report_generation_removes_only_owned_stale_contexts(self) -> None:
        database = self.repo.root / "index.sqlite"
        manifest = index.load_manifest(self.repo.manifest)
        index.build_index(self.repo.root, self.repo.manifest, database)
        index.generate_reports(self.repo.root, manifest, database)
        owned = database.parent / "context_target.md"
        self.assertTrue(owned.exists())
        unrelated = database.parent / "context_research_notes.md"
        unrelated.write_text("human-authored cache note\n", encoding="utf-8")
        legacy = database.parent / "context_retired_target.md"
        legacy.write_text(
            "# Context: Retired target\n\n"
            "> Non-authoritative; generated from the curated manifest.\n",
            encoding="utf-8",
        )

        manifest["claims"][0]["active"] = False
        index.generate_reports(self.repo.root, manifest, database)
        self.assertFalse(owned.exists())
        self.assertFalse(legacy.exists())
        self.assertEqual(
            "human-authored cache note\n", unrelated.read_text(encoding="utf-8")
        )

    def test_duplicate_report_filters_generic_titles_and_confirms_evidence(self) -> None:
        self.repo.write("archive/generic_a.md", "# A\n\n## Theorem 1.1 (computer-assisted)\n\nAlpha only.\n")
        self.repo.write("archive/generic_b.md", "# B\n\n## Theorem 1.1 (computer-assisted)\n\nBeta only.\n")
        common = "Let G be a seven-connected graph with a full boundary and two connected shores."
        self.repo.write("archive/hc7_duplicate_a.md", f"# A\n\n## Theorem 2 (boundary absorption)\n\n{common}\n")
        self.repo.write("archive/hc7_duplicate_b.md", f"# B\n\n## Theorem 4 (boundary absorption)\n\n{common}\n")
        subprocess.run(["git", "add", "archive"], cwd=self.repo.root, check=True)
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        report = index.duplicate_supersession_candidates(database)
        self.assertNotIn("generic_a.md", report)
        self.assertNotIn("generic_b.md", report)
        self.assertIn("hc7_duplicate_a.md", report)
        self.assertIn("hc7_duplicate_b.md", report)

    def test_candidate_records_and_all_required_reports_are_generated(self) -> None:
        self.repo.write("results/orphan.md", "# Orphan\n\n## Theorem 2\n\nA candidate result.\n")
        digest = hashlib.sha256((self.repo.root / "results/orphan.md").read_bytes()).hexdigest()
        self.repo.write(
            "results/orphan_audit.md",
            f"# Audit\n\n## Verdict\n\nGREEN.\n\nSource hash: `{digest}`\n\n[Source](orphan.md)\n",
        )
        self.repo.write(
            "results/declared.md",
            "# Declared result\n\n## Theorem 3\n\nAnother candidate result.\n",
        )
        declared_digest = hashlib.sha256(
            (self.repo.root / "results/declared.md").read_bytes()
        ).hexdigest()
        self.repo.write(
            "results/nonadjacent_audit.md",
            f"# Review\n\n**Audited source:** [declared result](declared.md)\n\n"
            f"**Source SHA-256:** `{declared_digest}`\n\n"
            "**Verdict:** GREEN.\n\n**Audit scope:** entire source document.\n",
        )
        subprocess.run(
            [
                "git", "add", "results/orphan.md", "results/orphan_audit.md",
                "results/declared.md", "results/nonadjacent_audit.md",
            ],
            cwd=self.repo.root,
            check=True,
        )
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        with closing(sqlite3.connect(database)) as connection:
            candidate = connection.execute(
                "SELECT source_heading,start_line,end_line,source_sha256,review_status FROM candidate_claims WHERE source_heading='Theorem 2'"
            ).fetchone()
            pair = connection.execute(
                "SELECT source_sha256,audit_sha256,green_verdict,source_hash_bound,review_status FROM audit_pairs ap JOIN documents d ON d.id=ap.source_document_id WHERE d.path='results/orphan.md'"
            ).fetchone()
        self.assertEqual(("Theorem 2", 3, 5, digest, "needs-review"), candidate)
        self.assertEqual((digest, hashlib.sha256((self.repo.root / "results/orphan_audit.md").read_bytes()).hexdigest(), 1, 1, "needs-review"), pair)
        reports = index.generate_reports(self.repo.root, index.load_manifest(self.repo.manifest), database)
        names = {path.name for path in reports}
        self.assertTrue(
            {
                "proof_dag.md", "trust_boundaries.md", "barrier_matrix.md",
                "orphaned_audited_results.md", "duplicate_supersession_candidates.md",
                "terminology_aliases.md", "connection_candidates.md",
                "audit_source_drift.md", "corpus_coverage.md", "context_target.md",
            } <= names
        )
        orphan_report = (self.repo.root / "orphaned_audited_results.md").read_text()
        self.assertIn("results/orphan.md", orphan_report)
        self.assertIn("results/declared.md", orphan_report)

    def test_audit_dependency_citations_do_not_create_audit_pairs(self) -> None:
        self.repo.write("results/consumer.md", "# Consumer\n\n## Theorem 2\n\nUses the dependency.\n")
        consumer_sha = hashlib.sha256((self.repo.root / "results/consumer.md").read_bytes()).hexdigest()
        dependency_sha = hashlib.sha256((self.repo.root / "results/theorem.md").read_bytes()).hexdigest()
        self.repo.write(
            "results/review_audit.md",
            textwrap.dedent(
                f'''\
                # Consumer audit

                **Audited source:** [consumer](consumer.md)

                **Source SHA-256:** `{consumer_sha}`

                **Verdict:** GREEN.

                **Audit scope:** entire source document.

                ## Dependencies checked

                [Dependency](theorem.md), dependency source hash `{dependency_sha}`.
                '''
            ),
        )
        subprocess.run(
            ["git", "add", "results/consumer.md", "results/review_audit.md"],
            cwd=self.repo.root,
            check=True,
        )
        database = self.repo.root / "index.sqlite"
        index.build_index(self.repo.root, self.repo.manifest, database)
        with closing(sqlite3.connect(database)) as connection:
            pairs = connection.execute(
                """SELECT ds.path,da.path FROM audit_pairs ap
                   JOIN documents ds ON ds.id=ap.source_document_id
                   JOIN documents da ON da.id=ap.audit_document_id
                   WHERE da.path='results/review_audit.md' ORDER BY ds.path"""
            ).fetchall()
        self.assertEqual([("results/consumer.md", "results/review_audit.md")], pairs)


class MarkdownParserTests(unittest.TestCase):
    def test_audit_scope_resolves_one_named_theorem_and_rejects_ambiguous_partial_scope(self) -> None:
        sections = index.extract_sections(
            "# Source\n\n## Theorem 4.3\n\nStatement.\n\n### Proof\n\nDetails.\n\n"
            "### Auxiliary case\n\nMore.\n\n## Section 5\n\nOpen.\n"
        )
        self.assertEqual(
            ("Theorem 4.3", 3, 14, "explicit named-theorem subtree audit"),
            index._audited_source_scope(
                sections,
                ("Background paragraph.\n\n" * 80) + "Audit scope is limited to Theorem 4.3.",
            ),
        )
        self.assertIsNone(
            index._audited_source_scope(sections, "This audit covers Sections 2-4 and 7."),
        )
        self.assertIsNone(
            index._audited_source_scope(sections, "Verdict: GREEN for Sections 2-4, 7, and 8."),
        )
        vague = "GREEN.\n\nThe proof discussion below compares Sections 2-4 of another paper."
        self.assertIsNone(index._audited_source_scope(sections, vague))
        self.assertEqual(
            ("Source", 1, 17, "adjacent-filename whole-document convention"),
            index._audited_source_scope(
                sections, vague, allow_adjacent_full_document=True
            ),
        )
        self.assertEqual(
            ("Source", 1, 17, "explicit whole-document audit"),
            index._audited_source_scope(
                sections, "Audit coverage includes the entire source document."
            ),
        )

    def test_common_partial_audit_wording_never_becomes_whole_document_scope(self) -> None:
        sections = index.extract_sections(
            "# Source\n\n## Theorem 1\n\nProof.\n\n## Appendix\n\nComputation.\n"
        )
        for wording in (
            "Audit verdict: GREEN except for the appendix.",
            "This audit does not verify the computation.",
            "Audit coverage is partial; the appendix remains unaudited.",
            "The appendix is outside the audit scope.",
            "Verdict: GREEN for Sections 1 and 2.",
            "The checked material consists of Theorem 1 and Lemma 3.",
            "GREEN for Theorem 1; Theorem 2 remains open.",
            "The appendix was not checked.",
            "The appendix is excluded.",
            "This audit covers Theorem 2.1 and Corollary 2.2.",
            "Only the proof is checked.",
            "# Audit\n\n## Limitations\n\nThe computation needs separate review.",
            "# Audit\n\n## Exclusions\n\nAppendix A.",
        ):
            with self.subTest(wording=wording):
                self.assertIsNone(index._audited_source_scope(sections, wording))

        self.assertEqual(
            ("Theorem 1", 3, 6, "explicit named-theorem subtree audit"),
            index._audited_source_scope(sections, "This audit checks Theorem 1."),
        )
        self.assertEqual(
            ("Theorem 1", 3, 6, "explicit named-theorem subtree audit"),
            index._audited_source_scope(
                sections,
                "I checked only Theorem 1.",
                allow_adjacent_full_document=True,
            ),
        )
        self.assertIsNone(
            index._audited_source_scope(
                sections,
                "Theorem 1 was checked; Appendix A was not.",
                allow_adjacent_full_document=True,
            )
        )
        self.assertIsNone(
            index._audited_source_scope(
                sections,
                "# Audit\n\n## Unresolved assumptions\n\nThe appendix is not audited.",
                allow_adjacent_full_document=True,
            )
        )

    def test_status_and_claim_extraction_are_section_scoped_and_fence_masked(self) -> None:
        text = """# Document

**Status:** written proof

```text
Status: false fenced marker
```

## Theorem 1 (sample)

Exact statement.
"""
        sections = index.extract_sections(text)
        statuses = index.extract_explicit_statuses(text, sections)
        claims = index.extract_candidate_claims("results/sample.md", sections)
        self.assertEqual(1, len(statuses))
        self.assertEqual(("Document", 3, "written proof"), (statuses[0]["heading"], statuses[0]["start_line"], statuses[0]["value"]))
        self.assertEqual(("Theorem 1 (sample)", 9, 11, "theorem"), (claims[0]["heading"], claims[0]["start_line"], claims[0]["end_line"], claims[0]["kind"]))

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
