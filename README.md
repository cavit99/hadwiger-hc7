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

The current programme starts from a uniform adjacent-pair theorem.  A
result of Kawarabayashi, Pedersen, and Toft on double-critical
seven-chromatic graphs implies that some edge `zu` satisfies

$$
                         \chi(G-\{z,u\})=6.
$$

The five-connected remainder has a spanning `K_6` model.  An audited
proper-minor colouring argument also gives a nonempty colour class missed
by both endpoints, five other colours seen by both, and five simultaneous
vertex-disjoint paths whose endpoint colours form the two complete
five-colour palettes.  This structure exists in every hypothetical
minor-minimal counterexample, not only in one finite boundary case.

Audited colouring theorems now control every pair of colours around such a
contraction.  For a connected induced bipartite subgraph, both sides see
every other colour.  Each colour supplies a common bichromatic component,
and every pair of other colours supplies a diagonal component forced by
nonextendability.  Matchings of colour pairs therefore give simultaneous
vertex-disjoint connected witnesses.  Whenever the relevant boundary
contacts occupy more than one component, the full neighbourhood of a
component is an actual graph separator.  These separators need not yet
have order seven.

If all five full two-colour graphs through the missed colour are connected,
the structure compresses further.  The union of any one other colour with
the missed colour is a connected dominating induced bipartite subgraph
`X`.  The graph `G-X` is five-chromatic and `K_6`-minor-free, and deleting
either endpoint of the selected edge leaves a five-chromatic graph.
Martinsson--Steiner's prescribed-singleton theorem then produces two
oppositely rooted near-`K_7` models.  This compression no longer depends on
preserving the original spanning `K_6` model.

These alternatives have been combined into one audited exhaustive theorem
for the selected adjacent-pair colouring: a disconnected two-colour graph
returns a genuine separator, while the separator-free case returns all
five connected-dominating cores.  The theorem supplies no upper bound on a
returned separator and does not yet synchronize the two rooted models.

Separately, an audited hand proof shows that every eight-connected
`K_7`-minor-free graph has at least 17 vertices.  Its new elementary step
rules out a seven-regular graph on 16 vertices in which every nonadjacent
pair has four common neighbours.  This is a global order bound, not a proof
of the palette-to-model exchange.

The immediate constructive target lies in the unique-deficiency branch.
A colour-matched repair path and a component-defect theorem give an
explicit `K_7` minor whenever that defect is nonpositive.  At a fixed
admissible path cut, if all four protected component classes are represented
by eligible components—each adjacent to `z` and to both path-side anchor
sets—and the component-contact graph is `K_4`-minor-free, defect one is
equivalent to the contact graph being a two-tree.  These hypotheses have
not been proved for every connected-dominating residue.  The next target is
to use proper-minor colourings at a lifted simplicial degree-two component
to construct `K_7`, obtain a colour-compatible order-seven separation, or
produce a new valid instance of the same eligible defect-one setup with a
declared host-level parameter strictly smaller.  Finding and proving such a
well-founded parameter is part of the open theorem.

The previously developed balanced order-eight boundary remains the main
label-rich laboratory.  There the canonical regenerated `K_6` model is
reversibly coupled to the old near-complete model, proving that contact
maximization alone cannot orient the exchange.  Static boundary traces,
endpoint-only delta-matroids, and unlabelled model regeneration are also
known to be insufficient.  This is substantive uniform infrastructure,
not a proof of $HC_7$.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Authoritative current status, proved dependency chain, exact open problems, and known obstructions |
| [`active/INDEX.md`](active/INDEX.md) | Short list of current proof work and immediate dependencies |
| [Current adjacent-pair frontier](active/hc7_adjacent_pair_palette_model_frontier.md) | Colour-component dichotomy, connected-dominating compression, and immediate rooted-model theorem |
| [Paired colourful-set `K_4` frontier](active/hc7_two_colorful_sets_rooted_k4_frontier.md) | Exact four-chromatic reduction and the current constructive milestone |
| [Balanced order-eight laboratory](active/hc7_balanced_order8_frontier.md) | Label-rich special branch retained to test the uniform exchange |
| [Frozen support-six technical frontier](active/hc7_support_six_frontier.md) | Earlier developed dependency chain retained for reuse |
| [Research integrity tools](tools/README.md) | Tracked-document search, current-spine dependency graph, audit checks, and deterministic verifier CI |

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

## Finding prior work

Every tracked Markdown document, including superseded work in `archive/`, can
be searched through the disposable SQLite/FTS index:

```bash
python3 tools/research_index.py build
python3 tools/research_index.py search '"component defect"'
python3 tools/research_index.py context hc7.target.defect_one_exchange
```

The curated manifest records only the current proof spine and typed barrier
relationships.  Search results are discovery leads, not inferred
mathematical dependencies, and `RESEARCH_LEDGER.md` remains the sole status
authority.

## Repository layout

```text
.
├── README.md            # stable project overview
├── RESEARCH_LEDGER.md   # authoritative research status
├── AGENTS.md            # workflow and mathematical-writing rules
├── tools/               # generated research index and integrity checks
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
