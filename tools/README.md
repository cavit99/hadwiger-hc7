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
curated proved-dependency closure, trust boundaries, barrier hypotheses, orphaned
hash-current audit candidates, duplicate/supersession candidates, terminology
aliases, source-cited connection candidates, audit/source drift, and corpus
coverage statistics. Candidate reports are discovery aids, never proof-status
evidence.  The curated closure is not an exhaustive substitute for the
dependency lists in [`../active/INDEX.md`](../active/INDEX.md) or the live
technical frontier; it is exactly the transitive closure of explicit `uses`
relations in the manifest.  The integrity check requires every immediate
proved input and barrier under the primary target in `active/INDEX.md` to
have a corresponding active manifest claim and direct target relation.

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

## Bounded multi-provider proof rounds

[`proof_round.py`](proof_round.py) runs the repository's bounded `3-1-2`
research protocol: three blind laboratories, at most one provider-neutral
selection prompt, and two cold referees from providers other than the selected
candidate's author. It is an orchestration and evidence-capture tool, not a
proof checker. Provider identity is omitted from the selector prompt, but this
is protocol-level blinding rather than an operating-system security boundary.
A GREEN result is an internal audit only.

The first frozen brief targets the
[paired-rooted pentagonal-bipyramid theorem](proof_rounds/hc7_pentagonal_bipyramid_brief.md).
Its configuration is
[`proof_rounds/hc7_pentagonal_bipyramid.toml`](proof_rounds/hc7_pentagonal_bipyramid.toml).
The runner verifies the exact theorem-heading hash and every context file,
resolves the clean checkout to a full commit, and then works only from that
frozen snapshot.

### Remote worker setup

Use a dedicated, non-privileged account or disposable VM containing no
unrelated secrets and no GitHub credentials.  The repository is public, so
the worker does not need push access.  Install provider CLIs from their
official distributions; the project deliberately does not install or pin
them.

```bash
git clone https://github.com/cavit99/hadwiger-hc7.git
cd hadwiger-hc7
git switch main
git pull --ff-only

python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r tools/requirements-verifiers.txt
python -m unittest discover -s tools/tests -p 'test_*.py' -v
python tools/research_index.py ci
```

Python 3.11 or newer is required.  Authenticate each provider interactively;
do not put tokens in this repository, a command line, or a committed `.env`.

```bash
codex login --device-auth
claude auth login
grok login --device-auth

codex login status
claude auth status
grok models
```

The default pilot uses `gpt-5.6-sol` at `ultra` effort, Claude Opus at `max`
effort with a USD 20 per-invocation ceiling, and `grok-4.5` at `high` effort
with a 60-turn ceiling. A normal round makes six provider calls in total; a
vetoed candidate plus the single permitted repair makes at most nine. Depending
on which provider authored the selected candidate, Codex can be called at most
four times, Claude three times, and Grok three times. The committed Claude
ceiling therefore permits at most USD 60 in one repaired round. Review the
configuration and account limits before starting.

### Prepare and run

```bash
CONFIG=tools/proof_rounds/hc7_pentagonal_bipyramid.toml
python tools/proof_round.py doctor "$CONFIG"
python tools/proof_round.py dry-run "$CONFIG"
ROUND_ID=$(python tools/proof_round.py prepare "$CONFIG")
python tools/proof_round.py run "$ROUND_ID"
python tools/proof_round.py status "$ROUND_ID"
```

The three laboratories—Codex, Claude, and Grok—run concurrently. This is the
normal way to let all three providers work on the theorem at the same time;
there is no need to start three commands manually. Provider-native nested
agent behaviour is not relied upon by the protocol, so one provider invocation
always counts as one laboratory regardless of its internal implementation.
The selector sees opaque candidate identifiers, not their provider mapping.
If either referee returns a concrete RED finding, one repair is available:

```bash
python tools/proof_round.py repair "$ROUND_ID"
```

Run the command inside `tmux` or another remote supervisor so an SSH disconnect
does not interrupt paid calls. Version 1 deliberately has no retry or resume
operation: interruption or provider failure terminates that round rather than
silently repeating paid laboratories or referees. Inspect it with `status`,
then preserve it or clean it up and prepare a new ID.

Different round IDs have independent locks and can run concurrently, but use
that only for deliberately different frozen briefs or role rotations. Running
duplicate copies of the same target multiplies cost without satisfying the
project's bounded-round stopping rule.

Generated prompts, one standalone detached snapshot, raw outputs, normalized JSON,
and summaries live only under `.cache/research/rounds/<round-id>/`.  The
directory is ignored by Git.  The runner uses fixed provider adapters,
argument-vector subprocesses with no shell interpolation, process-group
timeouts, a per-round lock, closed configuration and response contracts, and
a sanitized environment that does not forward common API or GitHub token
variables.  Provider authentication still makes the provider process trusted;
the dedicated worker account is the actual credential boundary.

Raw logs can contain provider or account metadata. They are ignored by Git and
must be inspected before being copied or shared.

The runner never stages, commits, pushes, merges, opens a pull request, or
promotes a mathematical claim.  A human must inspect any selected package and
move it through the ordinary theorem-plus-audit workflow on a new short-lived
branch.  To remove only one marked generated round:

```bash
python tools/proof_round.py cleanup "$ROUND_ID"
```

The integrity check fails on audit/source hash drift, broken inline Markdown
links in current-spine documents, non-GREEN `uses` dependencies,
device-specific paths in the selected tracked prose, source, configuration,
and script formats, and verifier hash or output drift.  Reference-style and
HTML links are not currently validated.  Broken historical links remain
searchable metadata but do not fail the current-spine check.
