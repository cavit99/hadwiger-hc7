# Internal audit: opposite-shore proper-minor incompatibility

**Verdict:** GREEN for the exact revision audited.

**Audited source:** `hc_opposite_shore_minor_response_incompatibility.md`

**Source SHA-256:**
`785555426c968461055ea8d5b2fc8b7428866495310e5a17967fbecb76904df2`

**Audit date:** 17 July 2026

This is a separate internal mathematical audit, not external peer review.
It checks the definition of an internal minor operation, palette alignment
when the boundary uses fewer than all available colours, every edge in the
glued colouring, the quantifiers in Corollary 2.2, and every assertion of
Corollary 3.1.

## 1. Internal minor operations

The definition is sufficient for the proof.  Read relative to the original
separation, it permits deletion of vertices in `A` and deletion or
contraction of edges whose represented vertices lie wholly in `A`, and it
forbids contracting an `A-S` edge.  Therefore it retains every literal
vertex of `B union S` and changes no edge with both ends in `B union S`.
Consequently

\[
                         G[B\cup S]
\]

is an unchanged induced subgraph of `G mu_A`.  The symmetric statement
holds for `mu_B`.  This is exactly the property used in Theorem 2.1.

Contraction of an edge in `A` may merge parallel contacts from the
contracted image into `S`, but this does not delete or alter an edge of the
closed opposite shore.  The explicit prohibition on identifying an
`A`-vertex with an `S`-vertex also ensures that every boundary label remains
literal.  No assumption about connectedness of either open shore is used.

## 2. Boundary palettes and colour-name alignment

Suppose `c_A,c_B` induce the same equality partition of `S`.  For each
partition block, its colour under `c_B` maps to its colour under `c_A`.
This is well defined and bijective between the two subsets of the
`q`-colour palette used on `S`: distinct blocks have distinct colours in
each colouring.  The two subsets have the same order, even if fewer than
`q` colours occur on `S`.  A bijection between two equally sized subsets
of a `q`-set extends to a permutation of the whole palette by choosing an
arbitrary bijection between their complements.  The empty-boundary case is
the same argument with the empty partial bijection.

After applying this permutation to `c_B`, its restriction and the
restriction of `c_A` agree pointwise on every literal boundary vertex, not
merely blockwise.  Thus the palette-alignment step is valid in all cases.

## 3. Edge coverage in the glued colouring

The proof uses the renamed restriction of `c_B` on `A union S` and the
restriction of `c_A` on `B union S`.  Both restrictions colour original,
unmodified closed shores by Section 1 above.  Every edge of `G` has one of
the following types:

- both ends in `A union S`;
- both ends in `B union S`; or
- one end in `A` and one end in `B`.

The third type is excluded by the separation hypothesis.  Boundary edges
belong to both closed shores and receive the same endpoint colours after
alignment.  Hence every edge is covered by at least one proper restriction,
and the glued map is a proper `q`-colouring of `G`.  This proves Theorem
2.1.

The assumption that the open sides are nonempty is harmless and matches
the intended application, although the gluing argument itself does not
need it.

## 4. Quantifiers in Corollary 2.2

The collections of “specified proper minors” may be arbitrary collections
of operations internal to the corresponding shores.  If a partition lay
in both response sets, then by definition there would exist:

1. one specified operation internal to `A` and one of its `q`-colourings;
2. one specified operation internal to `B` and one of its `q`-colourings;
3. the same induced boundary partition.

Those two witnesses contradict Theorem 2.1.  Thus the universal conclusion
over all pairs of specified responses follows from one existential witness
to an alleged intersection.  Empty specified collections cause no issue.

In a minor-minimal non-`q`-colourable graph, every nonempty legal internal
minor operation produces a proper minor: an edge deletion reduces the edge
set, while a vertex deletion or edge contraction reduces the vertex set.
Every such proper minor is `q`-colourable by minimality.  The “in
particular” assertion therefore has the required premise.  The statement
does not claim that the original, unmodified shore response belongs to
either collection.

## 5. Corollary 3.1

The two internal edge deletions are proper minors, so minor-minimality
gives a `q`-colouring of each.  They are operations in opposite shores, and
Theorem 2.1 therefore says that **every** colouring of `G-uv` has a boundary
partition different from **every** colouring of `G-yz`.  The displayed
universal quantifiers are correct.

Fix a `q`-colouring of `G-uv`.  If `u,v` had different colours, restoring
`uv` would leave a proper colouring of `G`; hence they have one common
colour `alpha`.  For any other palette colour `beta`, suppose they lie in
different components of the subgraph induced by colours
`{alpha,beta}`.  Swapping those two colours on the component containing
`u` preserves properness of `G-uv`, changes the colour of `u` but not
`v`, and makes the restored edge proper.  This again colours `G`, a
contradiction.  Therefore the two endpoints lie in one
`alpha-beta` component for every `beta != alpha`.  This remains valid if
`beta` was initially unused; in that case the argument simply makes its
impossibility explicit.  For `q=1` the assertion over other colours is
vacuous.  The argument for `y,z` is exactly symmetric.

Thus all claims in Corollary 3.1 are correct.  In the `q=6` application,
there are five such two-colour connections for each deleted edge.

## 6. The stated `HC_7` application

The original five-clique supplies the internal edge
`ell_e ell_f` in the leaf shore.  The second five-clique `Y` supplies an
internal edge in the opposite shore: it is disjoint from the original
five-clique and hence from the three-set `R`; because `e` and `f` are
anticomplete, a clique meets endpoints of at most one of those two edges,
and it may additionally meet `x`.  Thus `|Y intersect S|<=3`, leaving at
least two adjacent vertices of `Y` in the opposite open shore.  Corollary
3.1 consequently applies exactly as described.  It gives incompatible
host-realized partitions with five Kempe connections on each deleted
edge, but no transition between the two partitions.  The source states
this limitation correctly.

## 7. Duplication and novelty boundary

No special named theorem is needed.  The basic result is the familiar
separator colour-gluing criterion: equal equality partitions can be
aligned by a palette permutation and glued.  The present note packages its
cross-proper-minor consequence cleanly, but it should not be presented as a
new deep colouring theorem.

The closest repository precedents are:

1. `archive/hadwiger_uniform_interface_linkage_and_gluing.md`, Lemma 2.1,
   which states the same boundary-partition gluing criterion.  Under its
   stronger assumption that every proper minor is colourable, Theorem 2.2
   also implies the corresponding disjointness of opposite response
   languages.
2. `active/hc7_balanced_order8_edge_critical_completion.md`, Lemma 5.2,
   which is precisely the `q=6`, two-opposite-edge instance of Theorem
   2.1.
3. `results/hc7_repaired_contact_exchange.md`, Section 3, and
   `results/hc7_near_k7_critical_pinch_state.md`, which already use the
   standard edge-critical Kempe-component argument appearing in Corollary
   3.1.

The exact contribution of the audited source is therefore consolidation
and a slightly weaker-hypothesis uniform formulation: Theorem 2.1 assumes
only that the two selected whole-host minors are `q`-colourable, rather
than that every proper minor is.  Its proof and corollaries are correct,
but the underlying gluing and Kempe mechanisms are established folklore
and already present elsewhere in the repository.
