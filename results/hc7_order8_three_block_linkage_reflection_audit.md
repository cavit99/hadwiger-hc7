# Internal audit: reserved-path boundary-response theorem

**Verdict:** GREEN.

**Audited source:**
[`hc7_order8_three_block_linkage_reflection.md`](hc7_order8_three_block_linkage_reflection.md),
SHA-256
`e7d5db7a4cd9226f7dc2f50cb15b98977dc08707f9d7649e3eb9cb29c7fe7ccc`.

This is a separate internal mathematical audit, not external peer review.
The result is an unbounded colour-gluing lemma; it does not prove `HC_7`.

## 1. The three-block contraction

The three sets in (1.5) are pairwise vertex-disjoint because `D,C_X,C_Y`
are pairwise disjoint subsets of the open shore and
`{d,e},X,Y` partition the boundary.  Each set is connected: `D` has a
neighbour at both roots, and each of `C_X,C_Y` meets every vertex of its
nonempty boundary block.  Each set contains an edge, so their simultaneous
contraction is a proper minor.

The three images form a triangle.  The root image meets the two block images
through the assumed neighbours of `d` in `X` and `Y`, and the two block
images meet through the assumed `X`--`Y` edge.  Hence the three images use
three distinct colours.  On expanding over the boundary, `X` and `Y` are
independent and `de` is absent, so the restriction to the opposite closed
shore is proper and has exactly the partition

\[
                         X\mid Y\mid\{d,e\}.
\]

## 2. The four-block contraction

Under the additional split of `D`, the four sets in (1.6) are likewise
pairwise disjoint, connected, and nontrivial.  Their six pairwise
adjacencies are:

- the edge between `D_d` and `D_e`;
- the four root-to-block adjacencies supplied by the neighbours of each of
  `d,e` in each of `X,Y`; and
- the `X`--`Y` edge.

Thus the four images form a `K_4`.  Expansion gives exactly

\[
                         X\mid Y\mid\{d\}\mid\{e\}.
\]

Restriction and expansion preserve every edge from the opposite shore, and
permuting colour names aligns any common displayed boundary partition.
Because the two open shores are anticomplete, the aligned colourings glue.

## 3. Reserved paths and connected portal sets

In Corollary 2.1 the root path has distinct ends and at least one edge.
Splitting it at any edge produces nonempty adjacent connected subpaths that
retain the required `d`- and `e`-contacts.  The second path meets the portal
sets of both literal vertices of `X`; it may harmlessly be a single common
portal vertex.  Vertex-disjointness from the root path and disjointness of
the two boundary-full connected subgraphs supply the three subgraphs in
Theorem 1.1.  The unused boundary-full subgraph supplies all `Y`-contacts.

The same argument proves Corollary 2.2 when the second path is replaced by
a connected subgraph meeting every portal set belonging to `X`.

## 4. Opposite-response application

The prior physical-orientation issue is absent in the audited revision.
The reserved configuration lies in the shore containing the two
boundary-full connected subgraphs and produces **both** equality types on
the opposite closed shore.  The response set on the first closed shore is
nonempty by the promoted opposite-response theorem.  One of the two newly
produced types therefore belongs to both response sets, so the corresponding
colourings align and glue regardless of which singleton type occurs on
which physical shore.

The additional assumption that an `X`--`Y` edge exists is stated explicitly
and is used in both contraction constructions.

## 5. Trust boundary

The audit verifies Theorem 1.1, Corollaries 2.1 and 2.2, and the Section 3
application.  It does **not** prove that a negative set-terminal Two Paths
instance yields an order-seven separation or another terminal outcome.  It
also does not prove that the connected subgraph meeting a three-vertex
bipartition class in Corollary 2.2 must exist.

The quoted finite count—66 of 124 static quotient survivors admitting a
bipartition whose smaller class has order two—was independently reproduced
by the deterministic quotient probe, together with the survivor digest
`1a2325307e7bd5c856b0a1888295b9424a738ac11a8a69c2edcdda8279221110`.
That count is motivation only and is not used in the unbounded proof.
