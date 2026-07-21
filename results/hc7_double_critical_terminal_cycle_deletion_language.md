# Deletion language of an all-double-critical terminal cycle

**Status:** written proof; separate internal exact-file audit PASS. This is
a Cycle-1 result for the six-residual dominating-edge experiment. It does
not prove six-residual closure, classify a transition sink, or prove `HC_7`.

## 1. Edge strata and six-cores

Call `G` **strongly seven-contraction-critical** when `chi(G)=7` and every
proper minor of `G` is six-colourable. A **six-core** is an induced
vertex-minimal six-chromatic subgraph.

### Lemma 1.1 (edge/core equivalence)

For any two distinct vertices `p,q`,

\[
                         5\le \chi(G-\{p,q\})\le6.       \tag{1.1}
\]

For an edge `pq`:

- `pq` is six-residual, meaning `chi(G-{p,q})=6`, exactly when some
  six-core avoids both endpoints;
- `pq` is double-critical, meaning `chi(G-{p,q})=5`, exactly when
  `{p,q}` meets every six-core.

#### Proof

The upper bound follows from strong minor-criticality. A four-colouring
after deleting `p,q`, extended by two fresh colours, would six-colour `G`.
This proves the lower bound. A six-chromatic vertex-deleted graph contains
an induced vertex-minimal six-chromatic subgraph, and the converse is
immediate. The two possible values in (1.1) give the final equivalence.
\(\square\)

## 2. Complete deletion language

### Theorem 2.1

Let `C` be an induced cycle every edge of which is double-critical. For
every nonempty proper subset `S` of `V(C)`,

\[
 \chi(G-S)=
 \begin{cases}
  6,&\text{if }S\text{ is independent};\\
  5,&\text{if }S\text{ contains an edge}.
 \end{cases}                                             \tag{2.1}
\]

Moreover,

\[
 \chi(G-V(C))=
 \begin{cases}
  5,&\text{if }C\text{ is even};\\
  4\text{ or }5,&\text{if }C\text{ is odd}.
 \end{cases}                                             \tag{2.2}
\]

#### Proof

If `S` is independent, a five-colouring of `G-S` plus one fresh colour on
`S` would six-colour `G`. The upper bound six is automatic.

If `S` contains an edge `uv`, inducedness makes `uv` a cycle edge, so
`G-S` is a subgraph of the five-colourable graph `G-{u,v}`. Since a proper
induced subgraph of a chordless cycle is bipartite, a four-colouring of
`G-S` plus two fresh colours on `G[S]` would six-colour `G`. This proves
(2.1).

Deleting the whole cycle still gives the upper bound five. An even cycle
can be restored with two fresh colours, giving the lower bound five. An
odd cycle needs three fresh colours, giving only the lower bound four.
This proves (2.2). \(\square\)

### Corollary 2.2 (fixed exterior model in the five-colour case)

Put `H=G-V(C)`. If `chi(H)=5`, then `H` contains a normalized dominating
`K_5` model wholly outside `C`. That fixed model survives every deletion
supported on `C`.

If `C` is even, this always applies. For every fixed five-colouring of
`H`, each parity class of `C` contains a vertex whose neighbours in `H`
receive all five colours.

#### Proof

The model follows from Theorem 1.1 of the Dominating 4-Colour Theorem.
For the last assertion, suppose one parity class has no such vertex.
Colour the opposite parity class with a fresh sixth colour and give each
vertex of the first independent class an old colour absent from its
neighbourhood in `H`. This six-colours `G`, a contradiction. \(\square\)

### Corollary 2.3 (odd cycle with four-colour exterior)

If `C` is odd and `chi(H)=4`, then, for every `v in V(C)`, the graph
`H+v=G-(V(C)-{v})` is five-chromatic. It contains a five-vertex-critical
subgraph through `v` and hence, by Martinsson--Steiner Corollary 1.4, a
`K_5`-minor model with `{v}` as a singleton branch set. Its other four
branch sets lie in `H`.

#### Proof

The deleted set `V(C)-{v}` is proper and contains an edge, so Theorem 2.1
gives `chi(H+v)=5`. A minimal five-chromatic induced subgraph must contain
`v` because `H` is four-colourable. Apply the cited prescribed-singleton
theorem. \(\square\)

## 3. Core traces

### Theorem 3.1

Under Theorem 2.1:

1. every six-core meets `C` in a vertex cover;
2. for each `v in V(C)`, some six-core avoids `v` and contains both
   neighbours of `v` on `C`;
3. at most two six-cores are pairwise vertex-disjoint; and
4. if two disjoint six-cores exist, `C` is even and alternates between
   them. Consequently, for odd `C` every two six-cores intersect.

Thus every cycle edge is a two-vertex transversal of all six-cores, but no
single cycle vertex is a transversal.

#### Proof

Item 1 is Lemma 1.1. For each `v`, `chi(G-v)=6`: otherwise one fresh colour
on `v` would six-colour `G`. A six-core in `G-v` must meet both
double-critical edges incident with `v`, so it contains both cycle
neighbours. This proves item 2.

One edge cannot meet three pairwise disjoint cores, proving item 3. If
`Q,Q'` are disjoint, every cycle edge has one endpoint in each; walking
around `C` gives the claimed alternation and even parity. \(\square\)

## 4. Gate verdict

Let `e=xy` be six-residual and let a normalized dominating `K_5` model in
`G-{x,y}` have terminal cycle `C`. If `C` has no six-residual edge, the
theorems above give a complete deletion language and either one fixed
exterior dominating `K_5` model or rotating singleton-rooted `K_5` models.

This is real whole-cycle structure, but it does not pass the declared
closure gate. In the fixed-model case one still must allocate two disjoint
connected cycle pieces to all five named branch sets. In the rotating case
the four nonsingleton labels need not agree at consecutive roots. These are
the paired-rooted branch-set alignment obstruction already surviving in
the adjacent-pair and pentagonal-bipyramid programmes. No six-residual
successor or strict same-host parameter follows, so whole-sink
classification is not justified.

## 5. Sources

- António Girão et al., *The Dominating 4-Colour Theorem*, Theorem 1.1 and
  its normalization,
  [arXiv:2605.10112](https://arxiv.org/abs/2605.10112).
- Anders Martinsson and Raphael Steiner, *Strengthening Hadwiger's
  conjecture for 4- and 5-chromatic graphs*, Corollary 1.4,
  [JCTB 164 (2024), 1--16](https://doi.org/10.1016/j.jctb.2023.08.009).
