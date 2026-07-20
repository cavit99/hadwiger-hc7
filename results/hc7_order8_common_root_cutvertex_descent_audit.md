# Independent internal audit of the common-root cutvertex descent

**Verdict:** GREEN for the exact theorem revision with SHA-256
`921a5a16f9790174715f21e078b88297b9e11a825c74a74a4eb82e00ba386c5b`.

This audit checks the whole source file
[`hc7_order8_common_root_cutvertex_descent.md`](hc7_order8_common_root_cutvertex_descent.md),
including Theorems 2.1 and 4.1, Corollary 3.1, and the trust-boundary
statements.
It is an independent internal mathematical audit, not external peer review.

## 1. Hypotheses and dependency check

The hypotheses now include every ambient condition required by the project's
definition of a generic exact-seven response interface: seven-connectivity,
`K_7`-minor-freeness, non-six-colourability, and six-colourability of every
proper minor.  Non-six-colourability together with vertex-deletion
minimality also implies `chi(G)=7`, although the proof does not need to invoke
that equality separately.

The final exclusion of the three-subgraph outcome uses exactly Theorem 2.1
of the audited root-connector reflection theorem.  Its three connected
subgraphs are instantiated as `{q}`, `K`, and `Q_j`; no unproved conversion
of a colour into a branch-set label is used.

## 2. Component and support dichotomy

If `R-q` is disconnected, the connected subgraph `Q_j`, which is disjoint
from `q`, lies wholly in one component `W_*`.  Any other component `K` is
nonempty, connected, and disjoint from both `{q}` and `Q_j`.

If `K` supports one of `X,Y`, then `{q}`, `K`, and `Q_j` meet the three
requirements of the reflection theorem:

- `{q}` has neighbours at both `d,e`;
- `K` supports the selected bipartition class; and
- the boundary-full subgraph `Q_j` supports the other class.

Thus outcome 2 follows exactly.  Interchanging `X,Y` is legitimate.

## 3. Exact order-seven separator

In the remaining case, `K` misses at least one vertex `x` of `X` and one
vertex `y` of `Y`.  Since `K` is a component of `R-q` and the original open
shores are anticomplete,

```text
N_G(K) is contained in {q} union S and misses x,y.
```

The set outside `K union N_G(K)` is nonempty because it contains `L` (and
also contains `x,y`).  Hence `N_G(K)` is a genuine vertex separator.
Seven-connectivity gives the lower bound seven, while the displayed
containment gives the upper bound

```text
1 + |S-{x,y}| = 7.
```

Equality forces all of the following simultaneously:

- `q` is adjacent to `K`;
- every vertex of `S-{x,y}` is adjacent to `K`;
- no other boundary vertex is missed.

Therefore the missed vertices are exactly one member of each of `X,Y`, so
the asserted `x,y` are unique for the selected component `K`.  This proves
the exact neighbourhood identity and an actual order-seven separation; it
is not merely a quotient or lower-bound separator.

## 4. Operation-specific colouring response

Connectivity of `R` ensures that every component of `R-q`, in particular
`K`, has an edge `qv` to `q`.  Edge deletion is a proper minor, so `G-qv`
has a proper six-colouring.

The restriction of that colouring to the closed shore opposite `K` is
proper in the intact graph: the only deleted edge has its other endpoint
`v` inside `K`.  Let `Pi_K` be its exact equality partition on `N_G(K)`.
If the intact closed `K`-shore also realised `Pi_K`, a permutation of the
six colour names would align the two boundary colourings block by block.
There are no edges between the open shores, so they would glue to a proper
six-colouring of `G`, a contradiction.

Thus the data satisfy the definition of a generic exact-seven response
interface.  The descent is strict relative to the old open shore because
`K` is disjoint from the nonempty component `W_*` containing `Q_j`, and
hence `K` is a proper subset of `R`.  The argument works independently for
every edge `qv` from `q` into `K`; the resulting partition is allowed to
depend on the selected edge.

## 5. Residual-component attachment count

Let `H` be a component of
`R-({q} union V(Q_j))`.  Componenthood gives the exact **location** of its
possible neighbours outside `H`: they lie in `S`, in `Q_j`, or at `q`.
The proof does not incorrectly assume that every potential neighbour is
present.

If `H` supported either `X` or `Y`, the three disjoint connected subgraphs
`{q}`, `H`, and `Q_j` would satisfy the root-connector reflection theorem.
Thus, when that outcome is excluded, `H` misses a vertex `x_H` of `X` and
a vertex `y_H` of `Y`.  Hence

```text
N_G(H) is contained in
(S-{x_H,y_H}) union A_H union ({q} when epsilon_H=1).
```

The three terms are disjoint.  If `|A_H|+epsilon_H<=2`, this gives the
upper bound eight.  The full neighbourhood is a genuine separator because
`L` is nonempty and has no edge to `H`; seven-connectivity gives the lower
bound seven.  Since the order is integral, its only possible values are
exactly seven and eight.  Thus outcomes 1--3 of Theorem 4.1 are exhaustive,
and no equality of contact sets beyond what the argument proves is being
assumed.

In the order-eight case, every edge `hv` with `h in H` and
`v in N_G(H)` may be deleted.  It is a proper minor and therefore admits a
six-colouring.  Its restriction to the opposite closed shore is proper in
the intact graph.  The exact boundary equality partition cannot extend
through the intact `H`-shore, since alignment would six-colour `G`.  Also,
the endpoints `h,v` necessarily have the same colour in every such
colouring; otherwise restoring the edge would already six-colour `G`.
This is a genuine operation-specific response, not merely an abstract
boundary partition.  It is strict because the nonempty subgraph `Q_j` is
disjoint from `H`, so `H` is a proper subset of `R`.

Put `T=N_G(H)` in that order-eight case.  A component `D` of `G-T` which
misses a vertex of `T` has `N_G(D)` contained in `T` and of order at most
seven.  This is a genuine separator: if `D` is not `H`, then `H` lies on
the other side, while `D=H` cannot miss a vertex because `N_G(H)=T`.
Seven-connectivity therefore turns this into an actual order-seven
separation.  Absent that outcome, every component of `G-T` is literally
`T`-full.

There are at least two components of `G-T`: one is `H`, while the nonempty
old opposite shore `L`, which is disjoint from `T`, lies in another.
There cannot be four or more, because any four would satisfy the audited
four-full-component order-eight closure.  Its ambient chromatic hypothesis
is available: non-six-colourability and six-colourability of every
vertex-deleted proper minor imply `chi(G)=7`.  The other hypotheses,
proper-minor six-colourability and `K_7`-minor-freeness, are written in the
setting.  Consequently the exact component count is two or three.

## 6. Corollary and exact scope

When `q` is a cutvertex of `R`, outcome 1 is unavailable.  Under the stated
opposite-response orientation, outcome 2 would make both closed shores
realise the split-root partition and would six-colour `G`.  Therefore
outcome 3 holds.

Applying this separately to either named boundary-full subgraph proves the
correct block-cut conclusion: in a survivor with neither a descent nor a
common partition, no common-root vertex lying in either named subgraph is a
cutvertex of `R`.

The theorem does **not** localise every common-root vertex to a single
two-connected block.  Nor does it apply when the vertex is only a cutvertex
of the chosen subgraph but not of the whole shore.  The source states both
limitations correctly.  The fresh response need not preserve the old
eight-vertex boundary, the old split-root partition, or the inherited
minor-model labels.

## 7. Final assessment

The proof is unbounded in the order and number of blocks of `R`.  Every
connectivity, disjointness, separator, colouring-gluing, and strictness step
is valid under the written hypotheses.  No unresolved mathematical gap was
found within the stated scope.
