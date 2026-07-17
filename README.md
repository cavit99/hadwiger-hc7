# Hadwiger's Conjecture at $t=7$

> **Research status:** $HC_7$ is not proved in this repository.

This is an open research workspace on the first unresolved case of
Hadwiger's Conjecture.  It contains partial theorems, proof attempts,
computer-assisted finite results, internal audits, and counterexamples to
intermediate claims.  The audits are not external peer review.

## The problem

A $K_t$-minor model in a graph $G$ consists of $t$ pairwise disjoint
connected branch sets, with an edge between every pair.  Hadwiger's
Conjecture asserts

$$
K_t\not\preccurlyeq G\quad\Longrightarrow\quad \chi(G)\le t-1.
$$

The conjecture is known for $t\le6$; the $t=6$ case is due to
[Robertson, Seymour, and Thomas](https://doi.org/10.1007/BF01202354),
building on the Four-Colour Theorem.  This repository studies

$$
HC_7:\qquad K_7\not\preccurlyeq G\quad\Longrightarrow\quad\chi(G)\le6.
$$

## Current programme

Assume that $G$ is a minor-minimal counterexample.  Then $G$ is
seven-connected, $\chi(G)=7$, has no $K_7$ minor, and every proper minor is
six-colourable.

The present proof spine reduces every such $G$ to a bounded, literal graph
separation.  There are a vertex $u$ of degree seven, eight, or nine, a
component $C$ of $G-N[u]$, and

$$
S=N(C)\subseteq N(u),\qquad 7\le |S|\le9,
$$

such that both open sides contain a connected subgraph adjacent to every
vertex of $S$.  The boundary $G[S]$ is four-colourable.  Both closed shores
realize every independent subset of $S$ as one exact boundary colour class,
and the second endpoint of the adjacent-pair colouring framework can be
chosen on this same boundary.

Several infinite branches are now closed:

- every split boundary has compatible shore colourings and glues;
- a boundary with an adjacent pair complete to a two-connected remainder
  forces a $K_7$ minor under the full-shore hypotheses; and
- the earlier induced-cycle completion is a special case of that theorem.

For every $x\in S$, the exact-singleton boundary-colouring space is
Kempe-connected.  Attempting to lift a transition from a colouring of the
edge deletion $G-ux$ to the opposite shore must fail at a literal
bichromatic path.  That path avoids $u,x$, lies wholly in one open shore,
and on the $u$-side uses at most three other exterior components, each
adjacent to all but at most two boundary vertices.

The open step is to compose these forced paths into an explicit $K_7$-minor
model, a common boundary partition, or a strictly smaller bounded interface
that preserves the named colouring response.  Static boundary partitions
cannot suffice: every nonsplit four-colourable boundary admits an abstract
even/odd parity obstruction.  The remaining theorem must therefore use
literal path placement, operation endpoints, or labelled branch sets.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Authoritative research status and exact open gap |
| [`active/INDEX.md`](active/INDEX.md) | Navigation map for live proof work |
| [Bounded-interface bridge frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Current theorem and immediate constructive milestone |
| [Low-degree bounded-interface theorem](results/hc7_low_degree_adjacent_pair_alignment.md) | Uniform entry from a hypothetical counterexample |
| [Boundary-edge alignment](results/hc7_low_degree_boundary_edge_alignment.md) | Places the adjacent-pair endpoint on the same boundary |
| [Exact-block Kempe reduction](results/hc7_bounded_interface_exact_block_kempe_reduction.md) | Produces the literal pole-free bridge |
| [Research integrity tools](tools/README.md) | Search, dependency metadata, audit hashes, and CI checks |

Read a theorem in [`results/`](results/) together with its adjacent
`_audit.md` file.  Refuted intermediate principles and their exact scope are
kept in [`barriers/`](barriers/).  Superseded work remains in
[`archive/`](archive/) for provenance.

## Claim labels

- **Written proof:** a proof with explicit hypotheses and conclusion.
- **Separate internal audit:** an independent agent checked that revision;
  this is not peer review.
- **Computer-assisted finite result:** an exact finite reduction with
  retained code and, where practical, checkable certificates.
- **Conjectural target:** an unproved next theorem.
- **Barrier:** a counterexample to an intermediate claim, not to Hadwiger's
  Conjecture.

Finite computation is used to test conjectured lemmas and settle explicitly
finite subproblems.  It is never substituted for an unbounded proof.

## Finding prior work

Every tracked Markdown file, including archived work, is searchable through
the disposable SQLite/FTS index:

```bash
python3 tools/research_index.py build
python3 tools/research_index.py search '"bounded interface"'
python3 tools/research_index.py context hc7.target.bounded_interface_bridge
```

The generated index is a discovery aid.  Markdown remains authoritative,
and `RESEARCH_LEDGER.md` is the sole status authority.

## Repository layout

```text
.
├── README.md            # public overview
├── RESEARCH_LEDGER.md   # authoritative research status
├── AGENTS.md            # workflow and proof-integrity rules
├── tools/               # generated index and integrity checks
├── results/             # proved claims and adjacent audits
├── active/              # current proof targets and live scripts
├── barriers/            # counterexamples to intermediate claims
└── archive/             # superseded work retained for provenance
```

See [`AGENTS.md`](AGENTS.md) before contributing.  Prefer standard
graph-theoretic language, state exact trust boundaries, and do not modify an
audited theorem without renewing its audit.

## Licence

Repository materials are available under the [MIT License](LICENSE).  The
licence permits reuse; it does not certify the mathematical claims.
