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

## Commands

```bash
python3 tools/research_index.py check
python3 tools/research_index.py build
python3 tools/research_index.py search '"component defect"'
python3 tools/research_index.py report
python3 tools/research_index.py context hc7.target.defect_one_exchange
python3 tools/research_index.py verify
python3 tools/research_index.py ci
```

Generated SQLite and Markdown reports live under `.cache/research/`.  They
are disposable, ignored by Git, and can always be regenerated.  The reports
include a current proof dependency graph, claim trust boundaries, a barrier
matrix, and compact context packs for active targets.

The verifier whitelist is intentionally small and deterministic.  Install
its one pinned dependency with

```bash
python3 -m pip install -r tools/requirements-verifiers.txt
```

Run the infrastructure tests with

```bash
python3 -m unittest discover -s tools/tests -p 'test_*.py' -v
```

The integrity check fails on audit/source hash drift, broken current-spine
links, invalid dependencies, device-specific tracked paths, and verifier
hash or output drift.  Broken historical links remain searchable metadata
but do not fail the current-spine check.
