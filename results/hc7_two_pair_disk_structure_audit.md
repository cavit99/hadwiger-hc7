# Audit of the two-pair disk-structure theorem

**Verdict: GREEN.**  This is a separate internal audit, not external peer
review.

**Audited source:**
[`hc7_two_pair_disk_structure.md`](hc7_two_pair_disk_structure.md)

**Audited SHA-256:**
`e9af096101d418e95418203fc0a2c6634aa4184dc45a42c0e14abbef00fd3254`

## Scope checked

The audit checked the literal hypotheses, all branch-set constructions,
the plane-graph curvature argument, the list-colouring reduction, and the
stated trust boundary.  In particular, it did not treat virtual completion
edges as edges of the host graph.

## The rooted-model split

Exact order-seven rooted connectivity makes `(H,I union J)` internally
four-connected, and `|L|>=2` permits Jorgensen's rooted `K_4^-` theorem.
The disk drawing excludes a rooted `K_4` and also excludes a missing
adjacency between consecutive roots.  Hence all four cross adjacencies
between an `I`-rooted bag and a `J`-rooted bag are present.

The spanning-tree splits of `Q_I` and `Q_J` preserve connectedness and
disjointness.  Expanding each tree part by its corresponding rooted bag
gives four pairwise disjoint connected sets.  Each expanded set has exactly
its nominated boundary root.  If an expanded set misses a residual
subgraph, both it and its nested tree part give genuine nontrivial
full-neighbourhood separations.  Otherwise the four expanded sets and the
three residual subgraphs have all 21 required adjacencies.  Theorem 2.1 is
correct.

## Curvature and the degree-eight equality

The proof first deletes literal edges between consecutive roots.  This
removes no edge incident with `L` and prevents a parallel virtual outer
edge.  The enclosing outer four-cycle and a same-vertex triangulation then
give the displayed Euler curvature identity.  Every outer root has
completed degree at least three, so the total interior curvature is at
least two.  Only the three omitted boundary vertices can contribute host
neighbours outside `H`.  The claimed degree-seven/eight conclusion and the
degree-four-or-two-degree-five refinement follow.

In Corollary 3.2, seven-connectivity makes the component outside `N[v]`
adjacent to at least seven of the eight neighbours of `v`.  Every generic
and exceptional six-bag template is connected, pairwise disjoint and
pairwise adjacent under the literal five-cycle, hub and complete
`B`--`C` hypotheses, and every bag contains a neighbour of the outside
component.  Appending that component gives an explicit `K_7`-minor model.

## List-colouring and the contraction response

Deleting consecutive literal root edges before adding the virtual boundary
avoids parallel edges.  Restoring them after list-colouring is safe because
their endpoints keep the colours assigned by the proper far-shore
colouring.  If no vertex of `L` sees two colours on the three omitted
boundary vertices, every such vertex has a five-element list.  Theorem 7
of Bohme--Mohar--Stiebitz applies to the resulting outer cycle of order at
most six.  Each exceptional configuration would require an interior
literal vertex to be adjacent to an artificial subdivision vertex.  The
restriction therefore glues correctly to the unchanged far shore.

Corollary 4.2 explicitly assumes that `G` is not six-colourable.  Hence the
colouring pulled back from the proper star-contraction minor is
nonextendable.  Expansion to the two nonadjacent boundary vertices is
proper, and a nonconstant colouring on the four roots forces a second
bichromatic common-neighbour pair as claimed.

## Trust boundary

No unresolved assumption remains within the theorem.  It gives a genuine
full-neighbourhood separation, bounded-degree re-entry, and a
colour-dependent common-neighbour condition.  It does **not** bound the
returned separator by seven, synchronize the two shore colourings, or
produce a strict label-preserving induction.  It therefore does not prove
`HC_7`.
