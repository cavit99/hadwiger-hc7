# Independent audit of the pentagonal-bipyramid tree-expansion dichotomy

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_pentagonal_bipyramid_tree_expansion_dichotomy.md`](hc7_pentagonal_bipyramid_tree_expansion_dichotomy.md)

**Audited SHA-256:**
`aee6e0c8ec91f8fe52a86a1912f67dea6bfe7db72b0929672b55c8392d8a7295`

This is an internal mathematical audit, not external peer review.  The
source closes the unbounded family in which the seven pentagonal-bipyramid
columns are induced trees and every quotient edge is represented by one
literal inter-tree edge.  It does not close repeated inter-tree contacts,
columns with cycles, the full order-eight interface, or `HC_7`.

## 1. Setup and the alternating split

The seven sets `V(T_x)` are a genuine partition, every `T_x` is induced by
its vertex set, and the inter-tree contact relation is exactly the
pentagonal bipyramid `P`.  Deleting an edge `e` of `T_x` therefore gives
two nonempty connected sets `A_e,D_e`; every old neighbour label of `x`
has a literal contact with at least one of them.

If four distinct old neighbour labels alternate between the two sides,
splitting `x` into the adjacent quotient vertices `x_A,x_D` satisfies the
hypotheses of the audited vertex-split classifier.  The explicit `K_5`
models in that classifier have the additional property used here: each of
their five branch sets contains an old nonsplit vertex of `P`.

Replacing a nonsplit quotient vertex `y` by the whole tree `T_y`, and the
two split vertices by `A_e,D_e`, preserves disjointness, connectedness and
every required adjacency.  Each lifted `K_5` branch set contains a whole
tree `T_y` with `y ne x`, hence is adjacent to both fixed roots.  The two
roots are connected, disjoint and adjacent to one another.  They and the
five lifted sets are consequently an explicit `K_7`-minor model.  No
unstated clone-to-root adjacency is used.

## 2. Prescribed cyclic leaf orders

After cutting each inter-tree edge at its midpoint, the added incidence
vertices are genuinely pendant leaves of `T_x^+`.  For a tree, a prescribed
cyclic order of selected pendant leaves is realizable in a disc exactly
when each edge split is circular: the selected leaves on either side form a
cyclic interval.

The necessity is immediate from a plane embedding.  For sufficiency, the
components of `T-z` at any vertex have pairwise disjoint selected-leaf sets;
the edge-split hypothesis makes every nonempty such set a cyclic interval.
Ordering the incident edges by these intervals (and inserting leafless
components arbitrarily) gives a consistent plane rotation system.  Its
outer-face order is the prescribed cyclic order.  Specified leaves which
are themselves incident with the vertex contribute singleton intervals;
empty intervals cause no difficulty.

Thus Lemma 3.1 is valid at the scope used in the theorem.

## 3. Coupling the bundles

For each quotient edge `xy`, one common linear order is chosen on the
literal bundle `M_xy`.  The source uses that order at `x` and its reverse at
`y`.  In the fixed plane embedding of `P`, these are precisely the opposite
rotations needed to draw the matched half-edges as disjoint arcs in a
narrow corridor around `xy`.

Interval compatibility is required only for original edges of `T_x`.
Every artificial pendant edge has a singleton incidence-leaf side, so it
automatically satisfies the tree lemma.  Embedding the seven augmented
trees in disjoint vertex discs and the bundles in disjoint edge corridors
therefore gives a plane embedding of all internal and inter-tree edges of
`F`.  Removing the artificial leaves recovers `F`, proving Theorem 3.2.

In the stated spanning root setup, the colouring conclusion is also exact:
four colours suffice for planar `F`; the nonadjacent vertices `v,w` share a
fifth colour; and `p` receives a sixth.  The edges `vp,pw`, the absence of
`vw`, and all root-to-core edges are then proper.

## 4. The single-contact dichotomy

When every quotient edge has exactly one literal representative, each
neighbour label occurs exactly once among the incidence leaves at a
column.  Hence every original tree edge partitions the cyclically ordered
set of distinct neighbour labels.

If one side is not a cyclic interval, that side and its complement each
have at least two cyclic blocks, so four distinct labels alternate.  The
alternating-split theorem gives the explicit `K_7` model.  If every side is
an interval, the unique bundle order is interval-compatible (the pendant
edges again being automatic), and the planar-core theorem applies.  This
proves Corollary 4.1 for trees of arbitrary finite order and shape; it is
not a finite enumeration.

## 5. Repeated contacts and trust boundary

With repeated contacts, a failed interval test gives four alternating
incidence leaves, but some can carry the same old neighbour label.  In the
absence of a four-distinct-label witness, each individual failed test is
therefore supported on at most three old labels.  This is the precise sense
of the final concentration statement; it does not assert one global
three-label set works for all bundle orders.

The source correctly stops there.  Replacing an arbitrary connected column
by a spanning tree is legitimate for constructing a minor but not for
deducing planarity of the original induced core, because discarded chords
can be the source of nonplanarity.  Nor does the proof synchronize boundary
colourings across an order-seven separation.

All branch-set lifts, interval-order implications, corridor embeddings and
colouring deductions are valid at the audited hash.  **GREEN.**
