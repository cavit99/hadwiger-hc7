# Audit of the response orientation at an unresolved two-cut

**Verdict:** GREEN.

**Audited source:**
`results/hc7_order8_two_cut_response_orientation.md`

**Audited SHA-256:**
`82694014e256827aba082d40f998a1e5b6ac72027714a39fb1f09e68bf90435a`

**Promoted source SHA-256:**
`2f494477ffaf4f8f0f7e9df2835f1387bcc9aff463fa758298e8c53c08e514d8`

The promoted revision changes only the status line and adds the audit link;
the theorem, proof, scope, and trust boundary audited below are unchanged.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Boundary prerequisites

The cited two-cut opposite-response theorem supplies every datum imported
at the start: the two defect-one lobes, the absence of all four
cut-vertex--defect edges, the bipartition
`S-{d,e}=P dotcup R`, the nonedge `de`, and two nonempty opposite response
sets.  Its proof also shows that each of `d,e` has a neighbour in both
bipartition classes.

Because deletion of `d,e` leaves a bipartite graph, each boundary odd cycle
meets `{d,e}`.  The two cycles are vertex-disjoint, so each contains exactly
one of `d,e`.  Removing that distinguished vertex leaves an odd-length
path of positive length in the bipartite graph.  Its ends lie in opposite
classes, proving the actual edge condition `E(P,R) nonempty` used below.

## The three contractions

For fixed `i` and `j=1-i`, the sets

```text
Q_j union {d,e},   L_d union P,   L_e union R
```

are pairwise disjoint.  The first is connected even though `de` is absent,
because connected `Q_j` has a neighbour at both roots.  The other two are
connected because the corresponding lobe meets every literal vertex of its
boundary class.  Each set contains an edge, so their simultaneous
contraction is a proper minor.

The three images form a triangle.  The image containing `Q_j` is adjacent
to each other image through boundary-fullness, while an actual `P`--`R`
boundary edge supplies the third adjacency.  Hence their three colours are
distinct in every six-colouring of the minor.

Restricting to the untouched vertices `Q_i union S` discards all contracted
open-side interiors.  Pulling the three image colours back only to the
independent boundary blocks `P`, `R`, and `{d,e}` is proper: the blocks are
independent, their three colours are distinct, and every edge from an
untouched vertex of `Q_i` to a boundary block was represented by an edge to
the corresponding contraction image.  Thus each individual closed
component-side realizes exactly `P|R|{d,e}`.

## Orientation and path localization

The two individual equal-response colourings can be aligned on their three
labelled boundary blocks and glued across the anticomplete components
`Q_0,Q_1`.  If the closed `C`-side also realized the equal partition, its
colouring could be aligned with those two component colourings, yielding a
six-colouring of `G`.  Therefore the equal type is absent from the
`C`-shore response set.

The imported opposite-response theorem says that the two physical response
sets are nonempty, disjoint singleton subsets of `{equal,unequal}`.  It
therefore orients them uniquely: `C` is the unequal-response shore and
`Q_0 union Q_1` is the equal-response shore.

The same imported theorem supplies a bichromatic `d`--`e` path with all
internal vertices in `C` for every colouring in the prescribed unequal
response family.  Only `L_e` can contain a neighbour of `d` in `C`, and
only `L_d` can contain a neighbour of `e`, because the cut vertices miss
both roots and each opposite lobe has its displayed defect.  Every such
path therefore crosses `{x,y}`.  If a simple path contains both cut
vertices, the internal part between their occurrences is connected in
`C-{x,y}` and hence lies in one of its two components, unless `xy` itself
is the path segment.  This verifies the last assertion.

## Chromatic consequence for the selected component

The conclusion `chi(G[C])>=4` is also valid.  If `G[C]` admitted a proper
three-colouring, use three fresh colours on `C` and three other colours on
the independent blocks `P`, `R`, and `{d,e}`.  Disjoint palettes make
every `C`--`S` edge proper, so this is a six-colouring of the closed
`C`-side inducing the equal partition.  The equal-partition colourings of
the two individual `Q_i` sides constructed above then align and glue,
contrary to `chi(G)=7`.

## Trust boundary

The conclusion concerns the two prescribed response families; it does not
classify arbitrary six-colourings that do not make `P,R` monochromatic
blocks.  It neither produces the disjoint boundary-block subgraph needed by
the reserved-path contraction theorem nor makes an order-seven separator
colour-compatible.  No palette colour is identified with a branch-set
label.

Within the stated scope, no gap was found.  The theorem is safe to promote
after a metadata-only status update records this audit; that update should
be accompanied by the resulting promoted-source hash.
