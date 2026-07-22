# Hadwiger's Conjecture for $K_7$-minor-free graphs

> **Research status:** $HC_7$ is not proved in this repository.

This repository is an open research workspace on the first unresolved case
of Hadwiger's Conjecture. It contains written partial results, conjectural
proof targets, computer-assisted finite results, internal audits, and
counterexamples to intermediate claims. Internal audits are not external
peer review.

The notation `$HC_7$` used in historical filenames and internal claim IDs
indexes the excluded clique `K_7`. In Seymour's convention, where `HC(t)`
means that every `K_{t+1}`-minor-free graph is `t`-colourable, this is
`HC(6)`.

## The problem

A $K_t$-minor model in a graph $G$ consists of $t$ pairwise disjoint
connected branch sets, with an edge between every pair. Hadwiger's
Conjecture asserts

$$
K_t\not\preccurlyeq G\quad\Longrightarrow\quad \chi(G)\le t-1.
$$

The conjecture is known for $t\le6$; the $t=6$ case is due to
[Robertson, Seymour, and Thomas](https://doi.org/10.1007/BF01202354),
building on the Four-Colour Theorem. This repository studies

$$
HC_7:\qquad K_7\not\preccurlyeq G\quad\Longrightarrow\quad\chi(G)\le6.
$$

## Scope and headline progress

The project works from a hypothetical minor-minimal counterexample. Such a
graph is seven-connected, is seven-chromatic, has no $K_7$ minor, and every
proper minor is six-colourable.

The main internally audited reductions currently establish that:

- every hypothetical counterexample has a vertex `u` of degree seven,
  eight, or nine and an actual separation of order between seven and
  `d(u)`, with each open side containing a connected subgraph adjacent to
  every boundary vertex; at the same `u`, every component outside `N[u]`
  has its own boundary vertex `z_D` with `chi(G-{u,z_D})=6`;
- in the degree-seven case the exterior of the closed neighbourhood is
  connected, and its boundary-colouring constraints admit an exact
  matching description;
- those constraints produce five-rooted minor models and a boundary-labelled
  model of $K_7$ with either one missing edge or two adjacent missing edges;
- several unbounded boundary families, including split boundaries and the
  induced-cycle completion family, are closed by explicit minor-model or
  planarity arguments; and
- failed branch-set reroutings and colouring transfers can often be converted
  into actual full-neighbourhood separations or smaller list-critical
  subgraphs.

These results substantially constrain a counterexample, but they do not yet
synchronize the required branch-set labels and boundary colourings. The
remaining work is to turn proper-minor colouring responses into either an
explicit $K_7$-minor model, a common complete boundary partition on the
resulting order-seven, -eight, or -nine separation, or a genuine same-host
descent. The degree-seven programme is a sharper conditional refinement of
this exhaustive bounded-interface problem.

The exact live theorem changes as new reductions are proved. Its
authoritative status is maintained in the research ledger, and its full
hypotheses and trust boundary are stated in the technical frontier rather
than duplicated here.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current research status |
| [`active/INDEX.md`](active/INDEX.md) | Concise navigation to live proof work |
| [Live case verification map](active/hc7_live_case_dag.md) | Exhaustive global chain, conditional refinements, and every missing descent arrow |
| [Bounded-interface technical frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Primary all-degree theorem, direct inputs, and trust boundary |
| [Degree-seven technical frontier](active/hc7_degree7_model_separator_frontier.md) | Conditional exact-seven refinement and residual cases |
| [Low-degree bounded-interface entry](results/hc7_low_degree_adjacent_pair_alignment.md) | Uniform entry from a hypothetical counterexample |
| [Component-uniform boundary alignment](results/hc7_component_uniform_boundary_alignment.md) | A named edge-deletion response for every exterior component at one low-degree vertex |
| [Degree-seven boundary-labelled near-clique model](results/hc7_degree7_aligned_near_k7_model.md) | Principal degree-seven structural compression |
| [Research integrity tools](tools/README.md) | Search, curated dependency metadata, audit hashes, and CI checks |

Read a theorem in [`results/`](results/) together with its adjacent
`_audit.md` file. Refuted intermediate principles and their exact scope are
kept in [`barriers/`](barriers/). Superseded work remains in
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
finite subproblems. It is never substituted for an unbounded proof.

## Research memory and integrity

Every tracked Markdown file, including archived work, is searchable through
a disposable SQLite/FTS index:

```bash
python3 tools/research_index.py build
python3 tools/research_index.py search '"bounded interface"'
python3 tools/research_index.py context hc7.target.bounded_interface_bridge
python3 tools/research_index.py check
python3 tools/research_index.py report
```

The generated index and reports are retrieval and integrity aids. Markdown
proofs remain authoritative, `RESEARCH_LEDGER.md` is the sole status
authority, and the curated dependency graph is not presumed complete.

## Repository layout

```text
.
├── README.md            # durable public overview
├── RESEARCH_LEDGER.md   # authoritative current research status
├── AGENTS.md            # workflow and proof-integrity rules
├── tools/               # generated index and integrity checks
├── results/             # written claims and adjacent audits
├── active/              # current proof targets and live scripts
├── barriers/            # counterexamples to intermediate claims
└── archive/             # superseded work retained for provenance
```

See [`AGENTS.md`](AGENTS.md) before contributing. Prefer standard
graph-theoretic language, state exact trust boundaries, and do not modify an
audited theorem without renewing its audit.

## Licence

Repository materials are available under the [MIT License](LICENSE). The
licence permits reuse; it does not certify the mathematical claims.
