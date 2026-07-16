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

For a minor model, its **support** is the union of its branch sets. Let
$\mathcal F_6(G)$ be the family of supports of all $K_5$-minor models using
at most six vertices. The current intermediate target is

$$
\tau(\mathcal F_6(G))\le2,
$$

where $\tau$ is the transversal number. In plain terms: find two vertices
meeting every $K_5$ model on at most six vertices. This statement alone is
not $HC_7$; the pair must ultimately be shown to meet every $K_5$-minor
model. Such a global pair would finish the proof, because deleting it leaves
a $K_5$-minor-free graph, which is four-colourable by the known $t=5$ case.

The two current technical problems are:

1. Extract several compatible, prescribed $K_5$-minor models from a bounded
   critical family, or obtain an explicit $K_7$-minor model, a global
   two-vertex transversal, or an order-seven separation preserving the
   prescribed branch sets together with a strictly decreasing induction
   parameter.
2. Given three disjoint six-vertex $K_5$ models, delete their three
   two-vertex branch-set edges. Connectivity four yields an audited
   order-seven separation with a strict rank. In the remaining
   at-least-five-connected graph, each prescribed $K_4$ extends separately
   to a $K_5$-minor model by a path, but the three paths may overlap and
   colouring information alone does not make their branch sets compatible.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Authoritative current status, proved dependency chain, exact open problems, and known obstructions |
| [`active/INDEX.md`](active/INDEX.md) | Short list of current proof work and immediate dependencies |
| [Technical formulation of the two active problems](active/hc7_support_six_frontier.md) | Precise hypotheses and target conclusions |
| [Claim-by-claim coverage map](active/hc7_support_six_coverage_checkpoint.md) | Detailed dependency and evidence record |

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
