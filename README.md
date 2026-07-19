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

The degree-seven branch now has a stronger uniform description.  The graph
$G-N[u]$ is one connected component.  Boundary equality partitions are
encoded by matchings in the complement of $G[N(u)]$: the exterior shore
realizes exactly the one-edge matchings, while the pole shore realizes
exactly the matchings of order two or three.  One fixed colouring therefore
supplies all missing-edge Kempe paths on the five uniquely coloured roots.
Kriesell--Mohr's five-root theorem packages them into a rooted $K_5$ for
every repeated boundary pair.

If the repeated pair cannot be joined disjointly from that rooted model,
the five named branch sets carry a full separator.  Either an exact
order-seven separator occurs or seven disjoint paths cross those five bags.
More strongly, every surviving degree-seven interface contains a
boundary-labelled model of $K_7$ with one edge deleted or two adjacent edges
deleted.  The missing pairs share a singleton boundary centre.  The open
one-edge branch has now been compressed further by two unbounded theorems.
A common branch set containing two neighbours of the centre can be split to
give either an explicit $K_7$ model or an actual full-neighbourhood
separation.  Across such a separation, five named pairwise adjacent rows
reflect any boundary colouring whose intersection with each row is
monochromatic.

The common-endpoint rooted model-reselection gap is now solved.  After minimizing
the branch set containing a selected critical boundary endpoint, while
retaining the singleton deficient branch set, a parameter-uniform theorem
gives at least two incident edges whose individual deletion preserves the
same spanning labelled near-clique model.  Either two such edges can be
deleted simultaneously while that model survives, or the rooted branch set
is one degree-seven vertex and its neighbourhood is an actual order-seven
separator.  The theorem also bounds the number of rooted components and has
a version preserving several singleton branch sets.

When one persistent edge crosses into the deficient branch set, a
one-extra-colour list-critical reduction gives a strict full-neighbourhood
descent, an order-seven/eight singleton-side separation, or a shore-filling
normal form of minimum degree at least nine.  Fixed-trace attainment and
total rejection are handled by separate audited theorems.  Explicit
counterexamples show that persistence alone cannot force a tight
list-critical endpoint.

The immediate target is therefore label allocation in one common
two-edge-deletion graph.  That graph is both six-colourable and contains the
same labelled $K_7$-minus-one-edge model.  Nonjoint persistent pairs form
only a matching among the persistent edges; in the dense alternative the
outer endpoints induce a complete graph minus a matching, and degree at
least thirteen forces a jointly persistent induced two-edge path.  For any
jointly persistent pair, the nonadjacent-end case has an exact contraction
trace and a saturation-or-bypass alternative.  In the adjacent-end case,
the two critical-triangle response families are either Kempe-separated or
a first transition gives a common-coloured separator or a connected
dominating bipartite subgraph whose complement is five-chromatic and
$K_6$-minor-free.

The required theorem must now turn these literal transition components and
first-hit locations into an explicit $K_7$ model, a common full colour
partition on an exact order-seven separator, or a strict label-preserving
full-neighbourhood descent.  Palette colours still do not identify
branch-set labels, Kempe-separated response families remain possible, and
obtaining an order-seven separator without synchronizing its shores is not
terminal.  The split-planar $\overline{P_7}$ model-reselection route remains
an independent secondary approach.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Authoritative research status and exact open gap |
| [`active/INDEX.md`](active/INDEX.md) | Navigation map for live proof work |
| [Degree-seven near-clique composition](active/hc7_degree7_model_separator_frontier.md) | Current theorem and immediate constructive milestone |
| [Bounded-interface bridge frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Degree-eight/nine continuation |
| [Low-degree bounded-interface theorem](results/hc7_low_degree_adjacent_pair_alignment.md) | Uniform entry from a hypothetical counterexample |
| [Boundary-edge alignment](results/hc7_low_degree_boundary_edge_alignment.md) | Places the adjacent-pair endpoint on the same boundary |
| [Exact-block Kempe reduction](results/hc7_bounded_interface_exact_block_kempe_reduction.md) | Produces the literal pole-free bridge |
| [Degree-seven anti-neighbourhood connectivity](results/hc7_degree7_anti_neighbourhood_connectivity.md) | Reduces degree seven to one exterior component |
| [Exact matching languages and rooted-model separator](results/hc7_degree7_matching_bridge_bundle.md) | Uniform degree-seven rooted-model principle |
| [Boundary-labelled near-`K_7` model](results/hc7_degree7_aligned_near_k7_model.md) | Compresses every degree-seven survivor to one/two adjacent missing edges |
| [Two-mark branch-set split](results/hc7_two_mark_branch_set_split.md) | Gives a complete minor or a full-neighbourhood separation |
| [Five-row separator reflection](results/hc7_five_row_separator_reflection.md) | Glues any row-monochromatic boundary response |
| [Universal multicoloured-row separator](results/hc7_universal_multicoloured_row_separator.md) | Removes simultaneous-loss case distinctions |
| [Boundary-full-subgraph row reflection](results/hc7_boundary_full_subgraph_row_reflection.md) | Converts disjoint boundary-full subgraphs into monochromatic row traces |
| [Disjoint trace-linkage reflection](results/hc7_disjoint_trace_linkage_reflection.md) | Closes simultaneous independent traces when their connected realizations are disjoint |
| [Two-pair disk structure](results/hc7_two_pair_disk_structure.md) | Gives a complete minor, nested labelled separators, or degree-seven/eight re-entry |
| [Degree-eight cyclic contact allocation](results/hc7_degree8_contact_allocation.md) | Converts a five-cycle with at most two independent contact defects into a `K_7` model |
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
python3 tools/research_index.py context hc7.target.degree7_model_separator
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
