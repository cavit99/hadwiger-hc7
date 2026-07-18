# Research integrity tools

These tools make the large research corpus searchable and enforce a small
set of current-spine integrity rules.  They are infrastructure, not a second
research ledger: [`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md) remains the
sole authority for mathematical status.

The index is rebuilt from `git ls-files`, so unrelated or unclassified local
files are excluded.  Every tracked Markdown document—including the archive—is
full-text indexed.  Only current claims and their typed relationships are
curated in [`research_manifest.toml`](research_manifest.toml); lexical search
matches are never inferred to be proof dependencies.

The optional [`research_discovery.toml`](research_discovery.toml) contains a
small set of source-verified but still non-authoritative terminology and
connection candidates. Every entry is hash- and line-pinned and remains
`needs-review`. Generated heading, status, audit-pair, dependency-link, and
near-duplicate candidates are stored only in the disposable database.
The discovery file has a closed schema: misspelled top-level or record keys,
wrong container types, and evidence intervals outside the uniquely named
heading subtree fail validation rather than disappearing silently.

## Commands

```bash
python3 tools/research_index.py check
python3 tools/research_index.py build
python3 tools/research_index.py search '"component defect"'
python3 tools/research_index.py report
python3 tools/research_index.py context hc7.target.degree7_model_separator
python3 tools/research_index.py verify
python3 tools/research_index.py ci
```

Generated SQLite and Markdown reports live under `.cache/research/`.  They
are disposable, ignored by Git, and can always be regenerated.  The reports
include the current proof dependency graph, active-target context packs with
full dependency closure, trust boundaries, barrier hypotheses, orphaned
hash-current audit candidates, duplicate/supersession candidates, terminology
aliases, source-cited connection candidates, audit/source drift, and corpus
coverage statistics. Candidate reports are discovery aids, never proof-status
evidence.

Automatic audit pairing is deliberately conservative. It records adjacent,
explicitly declared, or exact-hash associations. Non-adjacent links and hashes
count only in a local declaration such as “audited source” or “theorem revision”;
dependency citations inside an audit do not create pairs. The extractor resolves
a single named theorem when the audit says it covers only that theorem, including
its complete nested subsection tree. Duplicate headings and ambiguous or
non-contiguous partial audits are omitted. Common limiting language such as
“except”, “not audited”, or “outside scope” cannot become whole-document
coverage. Whole-document candidates require explicit whole-file wording, except
for the deterministic adjacent `theorem.md`/`theorem_audit.md` filename
convention. Shared legacy audits without exact hashes remain full-text discovery
leads and require manual review.

Builds use a unique temporary database followed by an atomic replacement, so
overlapping rebuilds cannot corrupt one another. Near-duplicate discovery is
blocked on informative title terms and confirmed against statement text; the
compact report prioritizes HC7-specific and non-archive material.
Report contents are prepared in a unique staging directory, then each report file
is atomically replaced. The report family is not a transactional batch under
concurrent report commands. When an active target disappears, the generator
removes only stale `context_*.md` files bearing its own marker; unrelated cache
files are not swept.

The verifier whitelist is intentionally small and deterministic.  Install
its one pinned dependency with

```bash
python3 -m pip install -r tools/requirements-verifiers.txt
```

Run the infrastructure tests with

```bash
python3 -m unittest discover -s tools/tests -p 'test_*.py' -v
```

The integrity check fails on audit/source hash drift, broken inline Markdown
links in current-spine documents, non-GREEN `uses` dependencies,
device-specific paths in the selected tracked prose, source, configuration,
and script formats, and verifier hash or output drift.  Reference-style and
HTML links are not currently validated.  Broken historical links remain
searchable metadata but do not fail the current-spine check.
