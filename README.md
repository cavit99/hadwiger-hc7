# Hadwiger's Conjecture at $t=7$

> **Research status:** $HC_7$ is not proved in this repository.

This is an open research workspace devoted to the first unresolved case of
Hadwiger's Conjecture. It contains partial theorems, proof attempts,
computer-assisted finite classifications, internal audit notes, and explicit
counterexamples to proposed intermediate lemmas. It is not a claimed proof
of $HC_7$, and the internal audits are not external peer review.

## The problem

A $K_t$-minor model in a graph $G$ consists of $t$ pairwise disjoint
connected branch sets, with an edge between every pair of branch sets.
Hadwiger's Conjecture asserts

$$
K_t\not\preccurlyeq G\quad\Longrightarrow\quad \chi(G)\le t-1.
$$

The conjecture is known for $t\le6$; the $t=6$ case is due to
[Robertson, Seymour, and Thomas](https://doi.org/10.1007/BF01202354),
building on the Four-Colour Theorem. Write $HC_7$ for the assertion at
$t=7$:

$$
K_7\not\preccurlyeq G\quad\Longrightarrow\quad \chi(G)\le6.
$$

## Current programme

Assume, for contradiction, that $G$ is minor-minimal with $\chi(G)=7$ and
no $K_7$ minor. Then every proper minor of $G$ is six-colourable, so $G$ is
7-contraction-critical; [Mader's theorem](https://eudml.org/doc/161665)
implies that $G$ is seven-connected.

The current programme studies one exact, unbounded branch of a global
two-vertex-transversal reduction.  It has an eight-vertex separator, two
connected sides adjacent to every separator vertex, two labelled
five-cliques on opposite sides, and a canonical four-root planar web after
two specified edge contractions.  The complement of the separator graph
has a perfect matching.  The immediate target is a label-preserving
completion: construct a `K_7` minor, glue two six-colourings across the
separator, increase the global support parameter, or obtain an actual
order-seven separation with a strict induction parameter.

Current work couples three kinds of data which are insufficient in
isolation: colourings after deleting or contracting two opposite clique
edges, the missing rooted linkage in the planar web, and a minimal planar
list-critical subgraph for a boundary colouring that cannot be repaired.
The zero-slack four-clique core and the two-vertex critical core are now
eliminated for hosts of arbitrary order by explicit `K_7`-minor models.
The remaining critical cores are one facial triangle or a positive-slack
Gallai-forest configuration.  In the triangular case, a removable-path
theorem produces a path from the facial vertex to the three-clique whose
deletion leaves the host connected; the unresolved step is to split that
path and its complement while preserving six named branch-set
adjacencies.  A verified finite barrier shows that the static web,
boundary, and triangle data alone do not force this split.
This is substantive progress on one infinite family, not a proof of
$HC_7$.  The broader support-six and singleton-root programmes remain
frozen dependency chains available for a justified handoff.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Authoritative current status, proved dependency chain, exact open problems, and known obstructions |
| [`active/INDEX.md`](active/INDEX.md) | Short list of current proof work and immediate dependencies |
| [Current balanced order-eight frontier](active/hc7_balanced_order8_frontier.md) | Precise hypotheses, proved inputs, barriers, and immediate open theorem |
| [Frozen support-six technical frontier](active/hc7_support_six_frontier.md) | Earlier developed dependency chain retained for reuse |

For a specific claim, read the theorem note in [`results/`](results/) together
with its adjacent `_audit.md` file when one exists. Failed intermediate
claims and concrete counterexamples are kept in [`barriers/`](barriers/).

## Claim labels

- **Written proof:** a proof is present, with explicit hypotheses and
  conclusion.
- **Separate internal audit:** another agent checked the stated proof; this
  is not peer review.
- **Computer-assisted finite result:** a finite reduction or exhaustive
  classification has retained code and, where practical, independently
  checkable certificates.
- **Conjectural target:** an unproved lemma or intended next theorem.
- **Barrier:** a counterexample to an intermediate lemma, not to Hadwiger's
  Conjecture.

Computer searches are used to test conjectured lemmas and settle explicitly
finite interfaces. They are not treated as proofs of unbounded statements.

## Repository layout

```text
.
├── README.md            # stable project overview
├── RESEARCH_LEDGER.md   # authoritative research status
├── AGENTS.md            # workflow and mathematical-writing rules
├── results/             # proved lemmas and adjacent audit notes
├── active/              # current proof work and finite verification code
├── barriers/            # counterexamples to intermediate claims
└── archive/             # superseded work retained for provenance
```

When contributing, state hypotheses and conclusions in standard
graph-theoretic language, distinguish written proofs from finite evidence,
and cite the relevant file and commit. See [`AGENTS.md`](AGENTS.md) for the
maintenance rules.

## Licence

Repository materials are available under the [MIT License](LICENSE). The
licence permits reuse; it does not certify the mathematical claims.
