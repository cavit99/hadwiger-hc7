# Independent audit: star-contraction traces and the three-support Hall obstruction

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.  It
checks Lemma 2.0, Theorem 2.1, Proposition 2.2, Theorem 3.1, the boundary
tableau in Section 4, and Proposition 5.1.  The result is conditional and
does not prove `HC_7`.

## Audited revision

The audited source is
[`hc7_order8_star_contraction_trace_and_lobe_hall.md`](hc7_order8_star_contraction_trace_and_lobe_hall.md)
at SHA-256

```text
8eb309036157ab63c4cf3d4fd2d27a886e4bcc90743589fbb32790aa495a0644
```

The dependency revisions inspected for their uses in the source are:

```text
86f53c727b7855b8ddea420a957320a188b61570924d8508f5dd8806ab138d20
  ../results/hc7_order8_rooted_partition_contact_concentration.md
e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4
  ../results/hc7_transported_partition_hall_reflection.md
9bd560eafc0072aa40d75946d5aabb44c6e78cc7c812997ee0bca51797c5d9ad
  ../results/hc7_minimal_contraction_forest_saturation.md
```

Each dependency has an adjacent GREEN internal audit.  Proposition 2.2 uses
only the elementary two-colour component interchange proved explicitly in
its proof.

During this audit the source was repaired in three places before the revision
above was frozen.  First, the additional live-interface hypothesis
`de notin E(G)` is now explicit wherever it is needed.  It is not attributed
to the self-contained contact-concentration theorem.  Second, Proposition
5.1 now distinguishes the `K_6` visible in its exact quotient from the
palette-saturation conclusion of the minimal-contraction theorem; it does
not invoke that theorem's stronger critical-image corollary.  Third, Lemma
2.0 now assumes `|E|>=2`, which is exactly what makes contraction of a
spanning tree of `E` a proper minor.  The unconditional Theorem 2.1 does not
need that assumption because `E union I` contains a boundary-crossing edge.

## 1. Lemma 2.0: a boundary colour is absent

Under its explicit hypothesis `|E|>=2`, a spanning tree of the connected
set `E` contains an edge, so contracting it gives a proper minor.  Its image
`a` is adjacent to every boundary vertex because `B=N_G(E)`.  Thus a proper
six-colouring uses the colour of `a` nowhere on `B`, and its restriction to
`G[C union B]` induces at most five boundary blocks.  The standard alignment
argument proves rejection by the intact `E`-side.

If `|W|=2`, then `|B|=9`.  Five nonempty blocks partitioning nine vertices
cannot all have order at least two, so there is a singleton block.  A maximum
clique among singleton blocks has order at least one and the demand is at
most `5-1=4`.  With at most four blocks, demand is at most four directly.
No claim is made for singleton `E`.

## 2. Theorem 2.1: exact independent-set traces

Let `I` be a nonempty independent set in `G[B]`.  Since
`B=N_G(E)`, every vertex of `I` has a neighbour in the connected set `E`.
Thus `G[E union I]` is connected and has at least one edge.  Contracting a
spanning tree of this graph is consequently a proper minor, not merely a
quotient isomorphic to `G`.

Write `a` for its contracted image.  On expanding a six-colouring of the
minor to `G[C union B]`:

1. vertices of `I` may all receive the colour of `a`, because `I` is
   independent;
2. every edge from `I` to a retained vertex was represented by an edge at
   `a`, so expansion is proper; and
3. every vertex of `B-I` is adjacent to `a` through its original edge to
   `E`, so none receives the colour of `a`.

The equality block on `B` is therefore exactly `I`.  If the same boundary
partition extended through the intact `E`-side, a permutation of the six
colour names would align the two boundary colourings.  The two open
components `E,C` are anticomplete, so gluing would six-colour `G`.  Rejection
by the intact side follows.

Finally `W subseteq D` and `D` has no neighbour at `d`, so every
`{d} union J` with `J` independent in `G[W]` is indeed independent.  The
contact-concentration theorem gives one boundary-full rooted part and one
part missing exactly `W`.  Therefore a rejected response has demand at
least two; at demand two both required sets must meet `W`.  This consequence
applies to the star-contraction colourings even though they are not
edge-deletion colourings.

## 3. Proposition 2.2: block-count descent or colour-indexed paths

In the exact-singleton response, let `alpha` be the colour of `d` and let
`C_i` have colour `beta`, with `C_i` containing neither `x_d` nor `y_d`.
The exact neighbourhood hypothesis gives no boundary edge from `d` to
`C_i`.

If no `alpha`--`beta` component meets both `d` and `C_i`, interchange the
two colours on the union of all such components meeting `C_i`.  The exact
singleton property says that `d` is the only `alpha`-coloured boundary
vertex, while `C_i` is the complete `beta`-coloured boundary block.  The
interchange therefore merges exactly `C_i` with `{d}` and fixes every other
boundary block.  It decreases the block count by one.  The switched
colouring remains proper on the `C`-side, and the usual boundary-gluing
argument proves that its new partition is rejected by the intact `E`-side.

Otherwise a shortest path in the common bichromatic component joins `d` to
`C_i`.  Choosing its first vertex in `C_i` as the endpoint leaves no internal
boundary vertex: the only boundary vertices using the two colours belong to
`{d}` and `C_i`.  The path has an internal vertex because the selected block
has no neighbour at `d`.  Its interior lies in `C`.  The identities

```text
C=(D-W) dotunion {e} dotunion R,
N_G(d) cap (D-W)=emptyset,
de notin E(G)
```

force the first internal vertex to lie in `R`; the proof correctly permits
the path to pass later through `e` into `D-W`.

The blocks containing `x_d,y_d` are distinct because `x_dy_d` is an edge,
and neither is `{d}`.  Hence at least `k-3` blocks are selected.  Paths for
different selected blocks use colour sets `{alpha,beta}` and
`{alpha,gamma}` with `beta ne gamma`; their intersection can contain only
vertices of colour `alpha`.  No disjointness stronger than this is claimed.

## 4. Theorem 3.1: exact contacts and the Hall characterization

In the nonempty-lobe case, `Z=D-W` is connected and full to
`(S-{d}) union W`.  The additional hypothesis `de notin E(G)` gives the
exact boundary-contact sets

```text
N_G(P_i) cap B = B-W  (i=0,1),
N_G(Z union {e}) cap B = B-{d}.
```

The first identity uses boundary fullness of each `P_i` to `S` and the
absence of `L`--`R` edges.  The second uses fullness of `Z`, absence of a
`D`--`d` edge, and the explicit `de` nonedge.  Connectivity, disjointness,
and pairwise adjacency of the three supports follow respectively from
fullness to `e`, their locations in `L,S,R`, the given `P_0P_1` adjacency,
and the edges from each `P_i` to `e`.

For a required set, the eligible supports are therefore exactly:

| meets `W` | contains `d` | eligible supports |
|---|---|---|
| no | no | `P_0,P_1,H` |
| no | yes | `P_0,P_1` |
| yes | no | `H` |
| yes | yes | none |

For demand at most three, Hall failure is consequently equivalent to at
least one of:

1. a required set meets both `W` and `d`;
2. at least two required sets meet `W`; or
3. demand is three and all three required sets contain `d`.

The converse assignment in the source is complete.  With at most one
`W`-meeting set, assign it to `H`; it avoids `d` if alternative 1 fails.
Assign at most two remaining sets to `P_0,P_1`.  If there are three remaining
sets, failure of alternative 3 supplies one which avoids `d`; assign that
one to `H` and the other two to `P_0,P_1`.  This is exactly a saturating
matching in the audited transported-partition theorem.

As a falsification check, all four contact types above were exhaustively
enumerated for demands one, two, and three.  In every case, the existence of
an injective support assignment was equivalent to failure of all three
displayed obstruction conditions.

## 5. The static boundary tableau

With boundary edges `da,db,ab,cf`, each block in

```text
{d,w_0} | {a,c,p,w_1} | {b,f,q}
```

is independent.  There are no singleton blocks, so demand is three and the
required sets are exactly the displayed blocks.  The first has no eligible
support, and the first two both meet `W`.  The six named vertices outside
`{d} union W` induce exactly two independent edges and two isolated
vertices, hence a forest.

The source now states the scope correctly: Theorem 2.1 forces the first
block as a possible exact trace, but it does not assert that the other two
blocks occur with it in a colouring of a hypothetical counterexample.  The
tableau is static compatibility evidence, not a host construction and not a
counterexample to `HC_7`.

## 6. Proposition 5.1: the forest quotient

The four displayed branch sets cover `L union R union {d,e}` and are
pairwise adjacent and complete to `F=S-{d,e}` by the audited
contact-concentration corollary.  Contracting one spanning tree in each
therefore gives exactly `K_4 join G[F]`, with no omitted host vertices.

For a set `J` of forest edges, contraction gives
`K_4 join (G[F]/J)`.  Contracting all forest edges leaves one independent
vertex for each forest component and hence a five-colourable graph.  If
`J` is proper, an uncontracted forest edge has ends in distinct contraction
classes because a forest has a unique path between its vertices.  The
second join factor remains bipartite and has an edge, so its chromatic number
is two and that of the join is six.  This proves inclusion-minimality.

Leaving exactly an edge `xy` uncontracted collapses its tree component to
`K_2` and every other tree component to one isolated vertex.  Thus the
predecessor is exactly `K_4 join (K_2 dotunion I_{c-1})`.  Its visible
`K_4 join K_2` lifts to the four original branch sets and the two connected
sides of the tree component minus `xy`.  The minimal-contraction theorem
separately gives palette saturation at the two quotient ends; no
critical-image hypothesis is assumed.  Exhaustive checks of every nonempty
forest through order six found no exception to the contraction-minimality
calculation.

The final warning about splitting `E union {d}` is also exact under the
explicit `de` nonedge: `E` is anticomplete to `R_0,R_1`, while `{d}` is
anticomplete to `D union {e}`.  The quotient `K_6` therefore does not by
itself supply a seventh branch set.

## 7. Trust boundary

The theorem produces an exact independent-set trace family, a
block-count-or-path alternative for one specially rooted trace, and a full
Hall characterization for the three displayed supports at demand at most
three.  It does not prove that any star-contraction response has demand at
most three, remove any of the three Hall obstructions, make the colour-indexed
paths disjoint, align their first hits with model labels, or provide a
common boundary colouring, an explicit `K_7`-minor model, or a recursive
descent.  No mathematical error remains in the audited revision.
