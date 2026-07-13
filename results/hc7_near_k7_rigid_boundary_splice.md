# Rigid-boundary contraction splice

## Status

This is a parameter-uniform finite-boundary theorem.  It converts
full-shore contraction witnesses into a colouring of the original graph
whenever one independent trace leaves a uniquely colourable boundary.
It is designed for the actual order-seven/eight adhesions arising in the
arbitrary `K_7^vee` normalization; no branch carrier is treated as a
monochromatic set in the original graph.

## Theorem 1 (rigid-boundary splice)

Let `k>=3`, and let `G` be a graph such that every proper minor of `G` is
`(k-1)`-colourable.  Let `(G_1,G_2)` be a separation with common boundary

\[
                         S=V(G_1)\cap V(G_2),
\]

and put `C_i=V(G_i)-S`.  Assume, for `i=1,2`, that:

1. `C_i` is nonempty and `G[C_i]` is connected; and
2. every vertex of `S` has a neighbour in `C_i`.

Suppose `I` is a nonempty independent subset of `G[S]` such that
`G[S-I]` has chromatic number `k-2` and has a unique proper
`(k-2)`-colouring up to permutation of colours.  Then `G` is
`(k-1)`-colourable.

### Proof

For `i=1,2`, the set `C_i union I` is connected: `C_i` is connected and
every vertex of `I` has a neighbour in it.  Contract this whole set to a
single vertex `z_i`, obtaining a proper minor `M_i` of `G`.  It is proper
because the nonempty shore `C_i` is contracted into the boundary block.
Let `c_i` be a `(k-1)`-colouring of `M_i`.

Every vertex of `S-I` is adjacent to `z_i`, through its neighbour in
`C_i`.  Therefore no vertex of `S-I` receives `c_i(z_i)`.  Expand only
the vertices of `I`, assigning all of them the colour `c_i(z_i)`, and
discard the contracted shore `C_i`.  This gives a proper colouring of
the opposite induced side `G-C_i`: the set `I` is independent, and every
edge formerly incident with a vertex of `I` became incident with `z_i`
in `M_i`.  Its trace on `S` has exactly the block `I` in the distinguished
colour and gives `S-I` a proper colouring with at most `k-2` colours.

Since `chi(G[S-I])=k-2`, both side traces use exactly `k-2` colours on
`S-I`.  By unique colourability, the two partitions of `S-I` into colour
classes are identical after a permutation.  Permute the colours on one
side so that its distinguished colour on `I` and all `k-2` boundary
classes agree with the other side.

Now use the colouring obtained from `M_2` on `G_1` and the colouring
obtained from `M_1` on `G_2`.  They agree on `S`, so their union is a
proper `(k-1)`-colouring of `G`: a separation has no edge between
`C_1` and `C_2`, and every other edge belongs to one of the two sides.
QED.

## Corollary 2 (exact seven-boundary clique trace)

Let `G` be 7-contraction-critical and let `S` be a full two-shore
separation as in Theorem 1.  If there are nonadjacent `x,y in S` such
that

\[
                           G[S-\{x,y\}]\cong K_5,           \tag{2.1}
\]

then `G` is 6-colourable.

### Proof

Take `k=7` and `I={x,y}`.  A `K_5` is uniquely 5-colourable.  Apply
Theorem 1.  QED.

## Corollary 3 (uniform uniquely-colourable trace)

The conclusion remains valid for a boundary of arbitrary order: only an
independent trace `I` and unique `(k-2)`-colourability of the remaining
boundary are required.  In particular, an order-eight adhesion is closed
whenever deleting one independent trace leaves any uniquely
5-colourable graph, not necessarily a clique.

## Audit boundary

The theorem colours the original graph by splicing restrictions of two
different proper-minor colourings.  It never expands either connected
shore as one colour.  Fullness to every boundary vertex is used twice:
to connect `C_i union I` and to exclude the distinguished colour from
`S-I`.  Unique colourability concerns the partition into colour classes,
not a preassigned list of colour names.

The theorem does not assert that every normalization adhesion contains
such a rigid trace.  The remaining P1 work is to prove that a non-rigid
order-seven/eight boundary either admits a labelled branch-set exchange
or belongs to one globally coherent planar society.
