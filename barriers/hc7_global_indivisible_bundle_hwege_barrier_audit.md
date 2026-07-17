# Internal audit of the indivisible-bundle `H`-path barrier

**Verdict:** GREEN for the exact source revision identified below.

This is a separate internal audit, not external peer review.  The barrier
is hand-checkable and has no accompanying finite verifier.

## Audited revision

- barrier: `hc7_global_indivisible_bundle_hwege_barrier.md`
- barrier SHA-256:
  `ea6e54d73daf44b466888674e6ecf1b9944e68c3d81d7eb9dcbd404f08da8a56`

The audit checks the model construction, exact connectivity, path-packing
number, quotient obstruction, explicit `K_7`-minor model, and trust
boundary.

## 1. Construction and the three models

The graph has the seven-vertex set

\[
 S=\{x_1,y_1,x_2,y_2,x_3,y_3,w\}
\]

and three disjoint four-cliques `Q_i`.  Between different `Q_i` there are
no edges.  Every vertex of `S` is complete to every `Q_i`, except for the
two stated nonedges `x_i a_i` and `y_i b_i`; inside `S` only the three
edges `x_i y_i` occur.

For each `i`, the four singleton bags of `Q_i` together with the connected
edge bag `x_i y_i` form a `K_5`-minor model.  The edge bag is collectively
adjacent to every singleton bag, while its endpoint defect sets are exactly
`{a_i}` and `{b_i}`.  The three six-vertex supports are pairwise disjoint.

## 2. Connectivity

Delete at most six vertices.  Some vertex of `S` remains, and at least six
of the twelve clique vertices remain, so one `Q_k` retains at least two
vertices.  Every `S`-vertex has at most one nonneighbor in `Q_k`; hence all
remaining `S`-vertices attach to the connected clique `Q_k-R`.

Any other nonempty `Q_i-R` also attaches.  Failure could occur only if
`S-R` were the unique exceptional singleton for the sole remaining
exceptional vertex of `Q_i`.  But reducing `S` to one vertex already uses
all six deletions and leaves all four vertices of `Q_i`, a contradiction.
Thus every deletion of at most six vertices leaves a connected graph.
Deleting all seven vertices of `S` separates the three cliques, so the
connectivity is exactly seven.

## 3. Exact bag-injective packing number

The union of the three model supports is every vertex except `w`.
Consequently a model-good path is either one edge or has `w` as its only
internal vertex.  At most one path in a vertex-disjoint family can use
`w`.

There are no edges between distinct `Q_i`, and no edge inside `S` joins
distinct supports.  Hence every one-edge model-good path has an endpoint
in one of the three split bags `x_i y_i`.  Bag injectivity permits each
split bag to be used at most once, yielding at most three one-edge paths
and at most one path through `w`.

The four displayed paths

\[
 x_1c_2,\quad x_2c_3,\quad x_3c_1,\quad a_1wa_2
\]

are pairwise vertex-disjoint and use distinct branch bags at every model.
Thus the maximum is exactly four.

## 4. Quotient certificate and its lift

Contracting each `x_i y_i` produces a distinguished vertex `z_i` and a
literal clique `L_i=Q_i\cup\{z_i\}`.  The set

\[
                         W=\{z_1,z_2,z_3,w\}
\]

separates the three cliques.  Taking singleton cells
`Y_q=X_q={q}` for every `q` in their union covers the quotient outside
`W`, makes the off-boundary condition vacuous, and gives

\[
 |W|+\sum_q\lfloor |X_q|/2\rfloor=4.
\]

No path between distinct `L_i` remains after deleting `W`, so the displayed
data satisfy the ordinary `H`-path obstruction conditions used in the
project's three-model formulation.  Expanding the three `z_i` replaces
`W` by the seven vertices of `S`.  The quotient certificate therefore
lifts to an order-seven separator, not to a separator of order at most
six.  This is exactly the indivisible-bundle mismatch claimed in the note.

## 5. Explicit target minor

The seven displayed branch sets

\[
 \{a_1\},\{b_1\},\{c_1\},\{d_1\},
 \{x_2,c_2\},\{x_3,a_2\},\{w,b_2\}
\]

are disjoint and connected.  The first four form `Q_1`.  The last three
are pairwise adjacent through edges of `Q_2`, and their respective
`S`-vertices `x_2,x_3,w` are complete to `Q_1`.  They therefore form an
explicit `K_7`-minor model.

## 6. Exact scope

The graph proves that seven-connectivity and three disjoint normalized
split models do not force seven bag-injective model-good paths, and that an
ordinary quotient `H`-path obstruction can expand to order seven rather
than at most six.  It deliberately contains a `K_7` minor.  It therefore
does not refute any theorem retaining `K_7`-minor-freeness or allowing an
explicit `K_7`-minor outcome, and it is not a counterexample to `HC_7`.
No unresolved gap remains in this stated methodological barrier.
