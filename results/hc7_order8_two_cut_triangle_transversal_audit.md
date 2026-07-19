# Audit of triangle-transversal structure behind a two-cut

**Verdict:** GREEN after an explicit scope correction and strengthening.

**Audited source:**
`results/hc7_order8_two_cut_triangle_transversal.md`

**Audited SHA-256:**
`7e487b3863ccbdae331a248bddfe6001b7ed97b0285e4cc945c4151e087ce43f`

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Scope

The theorem explicitly assumes two vertex-disjoint triangles in the
eight-vertex boundary.  In the promoted finite census this covers the 80
residual boundary types with a certified `(3,3)` odd-cycle packing.  It
does not claim to cover the two types whose certified packing is `(3,5)`.

## Findings

The audited small-boundary lobe theorem implies that, absent its terminal
outcomes, every lobe behind the two-cut sees at least seven boundary
vertices and at most one lobe is full.

In fact a full lobe is impossible.  If `F` is full and `L` is another
lobe, then `L` has one missed boundary vertex `a`.  One of the two disjoint
triangles avoids `a`, and at least three further boundary anchors avoid
both that triangle and `a`.  The four connected subgraphs
`F,L,Q_0,Q_1`, with three anchors added, together with the three singleton
triangle vertices, are seven pairwise adjacent branch sets.  All 21
adjacencies in the displayed `K_7`-minor model are valid.

For two defect-one lobes with missed vertices `a,b`, a boundary triangle
disjoint from `{a,b}` again leaves at least three permissible anchors.  The
displayed branch sets are disjoint and connected, and both lobes meet every
triangle vertex and every anchor.  Hence such a triangle would give a
`K_7` minor.  The pair `{a,b}` must therefore meet every boundary triangle.

If there were three defect-one lobes, every pair of their missed vertices
would meet both fixed disjoint triangles.  A two-set meeting two disjoint
triangles has one vertex in each.  Three vertices cannot have all three of
their pairs cross this bipartition.  Therefore there are at most two lobes;
a genuine two-cut provides at least two, so there are exactly two.

Their missed vertices cannot coincide, because one of the two disjoint
triangles avoids any fixed single vertex.  Since their pair meets both
triangles, one missed vertex lies in each.

## Correction history

The initial draft's dependency text overgeneralized the `(3,3)` conclusion
to all 82 census types.  The source now makes the two-disjoint-triangle
hypothesis explicit and lists the two `(3,5)` types as uncovered.  It was
then strengthened from an at-most-three-lobe conclusion to the exact
two-defect-one-lobe conclusion audited above.

## Trust boundary

The result does not eliminate the final two-lobe two-cut residue.  It does
not preserve inherited colouring partitions or branch-set labels, produce
compatible shore colourings, or close a two-component order-eight return.
Within the explicit `(3,3)` boundary scope, no mathematical gap remains.
Safe to promote with the source hash above.
