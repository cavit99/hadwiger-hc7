# AGENTS.md

Do not change this file unless the user explicitly requests it.

## Workflow

Use short-lived branches with a clear purpose:

```text
main
  ├── feature/<short-descriptor>
  ├── fix/<short-descriptor>
  ├── experiment/<short-descriptor>
  └── refactor/<short-descriptor>
```

Keep commits focused, preserve a clear mathematical narrative, and merge or
retire branches promptly.

Code and verification scripts should be simple, deterministic, efficient,
and no larger than the mathematical task requires.

## Documentation roles

- `README.md` is the stable public overview.
- `RESEARCH_LEDGER.md` is the sole authoritative current research status.
  Keep a short three-level frontier at its top: the exhaustive global
  obligation, the principal conditional refinement, and the immediate
  structural laboratory. Put detailed live residues in their technical
  frontiers and move superseded ledger snapshots to `archive/`; never append
  new live updates beneath a frozen historical section.
- `active/INDEX.md` is a navigation map only. It names exactly one primary
  target, its genuinely direct proved inputs and nearest barriers, followed
  by concise links to conditional refinements or current laboratories. A
  dependency is direct only when the target invokes it without passing
  through another listed theorem. Do not put transitive closure, frozen
  programmes, proof history, or residual case analysis in this file.
- `results/` contains written proofs and adjacent audit notes.
- `barriers/` contains counterexamples to intermediate claims.
- `archive/` preserves superseded work; do not delete it.

Do not add new status ledgers or competing proof spines.  Update the existing
authoritative document instead.

When the mathematical frontier changes, update `RESEARCH_LEDGER.md` and
whichever technical frontier or coverage files `active/INDEX.md` currently
designates.  Update `active/INDEX.md` only when the set of live targets or
their immediate dependencies changes.

Keep the README stable. Change it only when the project scope, navigation,
durable headline result, claim policy, or repository structure changes. Do
not name a fast-moving immediate lemma there.

Every live proof direction must be reachable from `active/INDEX.md`, either
directly or through one of the technical files it designates.  An unlisted
file in `active/` is not thereby false or obsolete, but it must not be treated
as part of the current proof spine until it is classified.

The generated research index is a retrieval and integrity aid, not a status
authority. Its dependency closure is curated rather than presumed complete.
In `tools/research_manifest.toml`, use `active = true` only for the sole
primary target and the small set of direct proved inputs and immediate
barriers displayed in `active/INDEX.md`; historical relevance alone is not
active status. The manifest may retain non-active claims and richer
relations for retrieval. When the primary target changes, update the ledger
frontier block, `active/INDEX.md`, manifest active flags and direct target
relations atomically in one focused commit. The integrity check enforces
this navigation-to-manifest alignment.
Run `python3 tools/research_index.py check` and
`python3 tools/research_index.py report`, then inspect the regenerated target
context pack.  Agents must still consult `RESEARCH_LEDGER.md`, `active/INDEX.md`, and
the designated technical frontier before relying on a generated context
pack.  Discovery connections remain non-authoritative until separately
reviewed and promoted as typed manifest relations.

## Mathematical language

Prefer established graph-theoretic terminology and self-contained theorem
statements.  Introduce project-specific shorthand only for a precisely
defined recurring object, define it at first use, and give its
standard-language meaning.

In public-facing documents and new theorem statements, avoid metaphorical
or overloaded terms such as *cell, decoder, carrier, handoff, lock, duty,
seam, gate, row,* and *packet* when the mathematics can instead be stated as
*case, explicit minor-model construction, branch set or connected subgraph,
separation, colouring constraint, boundary or separator, matching edge,* or
*connected subgraph adjacent to every boundary vertex*.

In particular:

- say “an explicit `K_t`-minor model in `G`,” not “a literal `K_t`,” unless
  the conclusion is genuinely a `K_t` subgraph;
- describe a colouring pattern by the boundary partition or by the set of
  matching edges with monochromatic endpoints, rather than calling it a
  “state” without definition;
- describe a reduction as an order-`k` separation preserving specified
  branch sets and colouring data, rather than an unexplained “handoff”; and
- expand “strongly contraction-critical” as the exact chromatic statement
  being used.

Historical filenames may retain old shorthand to preserve citations and
audit hashes.  Use descriptive link text so readers do not need that
shorthand.

## Claim discipline

Label every substantive claim with one or more applicable statuses:

- written proof;
- separate internal audit;
- computer-assisted finite result;
- conjectural target; or
- barrier/counterexample to an intermediate claim.

Never describe an internal agent audit as external peer review.  Never infer
an unbounded theorem from finite enumeration without a written reduction.

For established external input, cite a primary source and the exact theorem
or lemma number whenever practical.  Distinguish the cited statement from
new deductions made in this repository; do not call a result “known” without
a traceable source.

## Proof and audit integrity

- State every theorem with explicit hypotheses and conclusion before its
  proof.
- When a result is promoted to `results/`, keep its audit beside it using the
  `_audit.md` suffix.  Mark active drafts explicitly when they are unaudited.
- Directory placement does not establish claim status.  In particular, a
  legacy file in `results/` without an adjacent audit remains unaudited and
  must not be cited as a promoted result.
- Every new or materially updated audit must identify the exact theorem
  revision or content hash it checked, state a verdict, and list any
  unresolved assumptions or gaps.  Before an older audited result enters
  the current proof spine, bring its audit up to this standard.
- Do not silently alter an audited theorem.  If its mathematical content
  changes, update or replace the audit and rerun any recorded hash check.
- Separate theorem-level reasoning from computational evidence.  A finite
  verifier should output or identify a checkable certificate whenever
  practical.
- Record counterexamples to proposed lemmas in `barriers/`, including the
  exact statement they refute and the scope they do not refute.
- Preserve historical work in `archive/`; use Git history and archive notes
  rather than deleting or rewriting provenance.

The lifecycle is: develop drafts and live scripts in `active/`, promote a
written theorem to `results/` with its required audit, move refuted claims to
`barriers/`, and archive superseded work.

## Computational work

- Prefer deterministic, dependency-light scripts with documented invocation
  and expected output.
- Keep generated bulk data out of Git unless it is essential for independent
  verification and reasonably sized.
- Do not encode an unbounded mathematical assumption as a finite search
  bound without stating that limitation prominently.
- Before promoting a computer-assisted claim, test the encoding against
  known positive and negative examples and retain an independent checker
  when feasible.

## Repository hygiene

Do not add research files at the repository root beyond the documented
top-level files.  Keep audits beside their theorem, retain generating scripts
for finite claims, avoid device-specific absolute paths, and do not sweep
unclassified local files into commits.

Before committing, inspect the staged path list, run link and formatting
checks on changed documentation, and verify that `.codex/`, local runtimes,
generated caches, credentials, personal data, device-specific paths,
non-redistributable third-party material, and unrelated untracked files are
not staged.
