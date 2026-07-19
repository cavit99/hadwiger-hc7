# Independent audit: contracting an augmented full-component interface

**Verdict: GREEN.**

Audited source:
`results/hc7_augmented_full_component_contraction_reduction.md`

SHA-256:

```text
f5cff7a8318fd8d17a3779c23e10d568c2ee0fa2850cb6ac5f4bd153cdbcafaf
```

## 1. Contraction and component structure

Deleting

\[
S=(Y-\{v\})\cup\{x\}
\]

from `H=G/pv` corresponds exactly to deleting `X=Y union {p}` from `G`.
Thus every component of `G-X`, including `A,D`, remains a component of
`H-S`.

Because `N_G(A)=Y`, the component `A` has no neighbour at `p`, has a
neighbour at `v`, and has neighbours at every other vertex of `Y`.  After
contraction this gives `N_H(A)=S`.  Similarly, `N_G(D)=X` gives
`N_H(D)=S`.  Contracting `pv` creates no `A-D` edge, so the two components
remain disjoint and anticomplete.

## 2. Audit of Theorem 2.1(2)

Let `C in {A,D}`, and let `M_1,...,M_6` be a `K_6`-minor model in `H-C`,
each branch set meeting `S`.

The seven proposed branch sets

\[
C,M_1,\ldots,M_6
\]

are disjoint because the model lies in `H-C`.  They are connected by
hypothesis.  The six `M_i` are pairwise adjacent.  For each `i`, choose
`s_i in M_i intersect S`.  Since `C` is `S`-full, an edge joins `C` to
`s_i`, so `C` is adjacent to every `M_i`.

Thus these sets form a valid `K_7`-minor model in `H`.  Since `H` is a
minor of `G`, minor transitivity gives a `K_7` minor in `G`.  No unproved
lift of the contracted vertex is needed.

## 3. Audit of Theorem 2.1(3)

Given a `K_5`-minor model `M_1,...,M_5` in `G[Y-{y}]`, the proposed sets

\[
A,\qquad D\cup\{y\},\qquad M_1,\ldots,M_5
\]

are pairwise disjoint.  The set `D union {y}` is connected because `D`
has a neighbour at `y`.  Both `A` and `D union {y}` are adjacent to every
`M_i`, since `A,D` are adjacent to every literal vertex of `Y`.  They are
adjacent to one another through an edge from `A` to `y`.  Together with the
five old clique-model adjacencies, this verifies all adjacencies of a
`K_7`-minor model.  The construction remains valid when `y=v`.

Consequently, `K_5` is not a minor of `G[Y-{y}]` for every `y in Y`.  The
application of the established case `HC_5`, yielding four-colourability of
each such graph, is exact.

## 4. Chromatic number and connectivity of `H`

The assertion `chi(H)=6` is correct.  Because `H=G/pv` is a proper minor,
`chi(H)<=6`.  If `H` had a five-colouring, expanding the contracted vertex
would five-colour `G-pv` with `p,v` equal.  Recolouring `p` with a fresh
sixth colour would then six-colour `G`, a contradiction.

The assertion that `H` is six-connected is also correct.  If `T` separated
`H` and `|T|<=5`, then either `x notin T` and the same set separates `G`,
or replacing `x in T` by `p,v` gives a separator of `G` of order at most
six.  Either case contradicts seven-connectivity.

These justifications are implicit in the source but mathematically sound.

## 5. Regenerated `K_6` models

For `C in {A,D}`, the graph `H-C` is a proper minor of `G`, so it is at
most six-colourable.  If `chi(H-C)=6`, established `HC_6` supplies a
`K_6`-minor model.  Theorem 2.1(2) correctly excludes any such model whose
six branch sets all meet `S`.  Therefore every `K_6`-minor model in `H-C`
has at least one branch set disjoint from `S`.

The stated dichotomy is exhaustive and mutually exclusive.

## 6. Scope

The scope statements are accurate: contraction reduces the displayed
boundary from eight vertices to seven; `H` is six-colourable and is not a
recursive counterexample; and no `S`-meeting `K_6` model, common shore
colouring, or two-vertex transversal is inferred.

No branch-set overlap, hidden adjacency, unjustified contraction lift, or
misuse of `HC_5` or `HC_6` was found.
