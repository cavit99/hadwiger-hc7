# Five-row reflection across a separation

**Status:** written proof; separate internal audit GREEN.  The statement is
not restricted to an order-seven boundary.

## Theorem

Let `G` be a graph which is not six-colourable but whose every proper minor
is six-colourable.  Let

\[
             V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
             \qquad E_G(L,R)=\varnothing.                       \tag{1.1}
\]

Fix `a in T`.  Suppose that `G[R union T]-a` contains five pairwise
vertex-disjoint connected subgraphs

\[
                            Q_1,\ldots,Q_5                       \tag{1.2}
\]

which are pairwise adjacent and satisfy

\[
 T\subseteq\{a\}\cup\bigcup_{i=1}^5V(Q_i),
 \qquad E_G(a,Q_i)\ne\varnothing\quad(1\le i\le5).              \tag{1.3}
\]

Let `psi` be a proper six-colouring of `G[R union T]`, and let `Pi` be its
equality partition on the literal boundary `T`.  Assume that

1. every nonempty set `T intersect V(Q_i)` lies in one block of `Pi`; and
2. either the block of `Pi` containing `a` meets some `Q_i`, or
   `T intersect V(Q_i)` is empty for some `i`.

Then `G` is six-colourable, a contradiction.

## Proof

Write `A` for the block of `Pi` containing `a`.  For every `i` with
`T intersect V(Q_i)` nonempty, hypothesis 1 gives a unique block `B(i)`
containing that intersection; assign `Q_i` to `B(i)`.  Every block
`B ne A` receives at least one row, since each of its vertices belongs to
a row by (1.3).  If `A` has received no row, hypothesis 2 supplies a
boundary-free row, which we assign to `A`.  Assign every remaining
boundary-free row arbitrarily to one of the blocks.  For each block `B`
put

\[
       X_B=B\cup\bigcup\{V(Q_i):Q_i\text{ is assigned to }B\}.  \tag{2.1}
\]

The sets `X_B` are pairwise disjoint.  Each contains at least one row.
Rows assigned to one block are mutually adjacent, and every boundary
vertex of that block other than possibly `a` already lies in one of those
rows.  The set `X_A` is also connected because `a` is adjacent to its
assigned row.  Thus every `X_B` is connected.  Distinct sets `X_B` are
adjacent through their assigned rows.

Contract a spanning tree of every `G[X_B]`, and then delete every original
vertex of `R` outside the union of the sets `X_B`.  This is a proper minor:
the carrier `X_A` contains `a`, a nonempty assigned row and an edge between
them.  Colour the proper minor with six colours.  Its carrier
representatives form a clique, so distinct blocks of `Pi` receive distinct
colours.

Keep the resulting colours on `L`, and give each literal vertex of a block
`B subseteq T` the colour of the representative of `X_B`.  This is a
proper colouring of `G[L union T]`.  Edges inside `L` survive in the
minor; an edge from `L` to a boundary block survives as an edge to its
representative; vertices in one block of `Pi` are independent because
`psi` is proper; and representatives of different blocks have distinct
colours.  The induced equality partition on `T` is exactly `Pi`.

After permuting colour names, this colouring agrees with `psi` on `T`.
The two colourings glue because there are no edges from `L` to `R`, giving
a six-colouring of `G`.  \(\square\)

## Corollary (the exact obstruction)

In the setting of the theorem, any far-shore colouring which cannot be
reflected through the other shore has at least one of the following
properties.

1. Some named row `Q_i` meets `T` in vertices of two different colours.
2. The colour of `a` occurs nowhere else in the five row intersections,
   and every row meets `T`.

This is a labelled obstruction: it identifies the row whose boundary
contact is multicoloured, rather than only the palette partition.

## Trust boundary

The colouring `psi` must be genuinely proper on the unchanged closed shore
`G[R union T]`.  A colouring obtained after an operation wholly in the
opposite open shore has this property.  A contraction involving two
literal vertices of `T` does not automatically have the required pullback.

Only the vertices of `T` are expanded after the carrier contractions;
internal vertices of `R` are discarded.  No claim is made that a colouring
of a contracted connected row expands to that row.
