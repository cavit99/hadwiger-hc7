# Audit of the cofacial equal-root extension

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_planar_equal_root_extension.md`

**Audited SHA-256:**
`ddca4874ded65b93eb2dac4771c7396345b093177b0259905bcdc07fa3f6a343`

**Promoted source SHA-256:**
`435f06ad876adfe5bfd35636bac82c464aed26cd0efb7473946cc1f63c212783`

The promoted revision changes only the status line and adds this audit link;
the theorem statements, proofs, dependencies, and trust boundary audited
below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Theorem 1: planar contraction and palette

Because `d,e` are distinct nonadjacent vertices on a common face, an
auxiliary edge `de` can be drawn inside that face.  Contracting this added
edge preserves planarity.  Parallel edges created by common neighbours may
be suppressed before applying the Four Colour Theorem; they do not affect
proper vertex colouring.

A proper colouring of the contracted graph with at most four colours pulls
back to `F[C union {d,e}]` by assigning the contracted colour to both
`d,e`.  Every edge from `C` to either root was represented by an edge to
the contracted vertex, and `de` is absent in the original graph, so the
pulled-back colouring is proper.  In particular, `d,e` have one common
colour `alpha`.

Two colours outside the at-most-four-colour palette are then available.
Assigning one to all of `P` and the other to all of `R` respects every edge:

- there are no edges internal to either independent class;
- every `P`--`R` edge has differently coloured ends;
- every edge from `d` or `e` to either class has colours `alpha` and a
  fresh block colour; and
- every edge from `C` to either class is proper because neither fresh colour
  appears on `C`.

The three nonempty labelled blocks therefore receive three distinct
colours, and the equality partition on `S` is exactly
`P | R | {d,e}`.  If the planar subgraph uses fewer than four colours,
padding the palette before choosing the two fresh colours is harmless.

## Corollary 2: cofaciality inherited from the web

An attachment-free `(d,p,e,q)`-web is its embedded planar skeleton.  Since
`G[C union {d,e,p,q}]` is a spanning subgraph, deleting edges does not
invalidate that embedding, and the four nominated vertices occur on its
outer face in the order `d,p,e,q`.  Deleting `p,q` leaves both `d,e`
incident with the outer face: removing outer-face vertices and their edges
can only merge faces with the outer face.  Consequently
`G[C union {d,e}]` is planar with the roots cofacial.

Apply Theorem 1 to the whole closed `C`-side `G[C union S]`; its hypothesis
only concerns the displayed root-and-interior induced subgraph.  This
produces the equal-root partition on `S`.

Assertion 1 of the audited response-orientation theorem independently
produces the same exact labelled partition on each closed `Q_i`-side.
After permuting colour names, the three colourings agree on all three
boundary blocks.  The open components `C,Q_0,Q_1` are pairwise
anticomplete, so their union is a proper six-colouring of `G`.

## Corollary 3: exhaustiveness

For a bipartition class of order two, Theorem 4.1 of the audited
unbalanced-bipartition reduction has exactly three outcomes:

1. a six-colouring of `G`;
2. an actual order-seven separation with connected shore in `C`; or
3. an attachment-free planar web with the required cyclic terminal order.

The first two are precisely the displayed outcomes of Corollary 3, and
Corollary 2 turns the third into the first.  No additional web or linkage
case remains.

## Trust boundary

The result closes the two-vertex bipartition-class residue for web
skeletons of arbitrary order.  It does not prove the order-seven outcome
colour-compatible, and it does not treat the balanced `3+3` partition.
No virtual completion edge is used as an edge of `G`; the sole auxiliary
edge `de` is added only inside a proved planar embedding to construct a
colouring and is removed when that colouring is expanded.

Within this scope, no gap was found.
