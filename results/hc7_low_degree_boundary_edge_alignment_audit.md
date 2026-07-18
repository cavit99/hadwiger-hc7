# Independent audit: boundary-aligned low-degree adjacent pair

**Verdict:** GREEN.

This verdict is conditional on the already GREEN-audited low-degree
adjacent-pair theorem, its computer-assisted degree-nine local-completion
lemma, Mader's exact extremal bound for `K_7` minors, and the established case
`HC_6`.  The source does not prove `HC_7` and does not synchronize the two
closed-shore colourings.

## Exact revision audited

```text
a18789eac9d259d8c091364e2dc6431fb09d5b8e0f0d78308e1f5328f467652f  audited theorem content before status-only promotion
```

Promotion changed only the status line.  The promoted source hash is

```text
424bfaeaa9023a2be0b2c8817608d28e38d8b2f7893284f46b733e1f21de513b  results/hc7_low_degree_boundary_edge_alignment.md
```

The principal promoted dependencies were checked at these current revisions:

```text
263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca  results/hc7_low_degree_adjacent_pair_alignment.md
dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08  results/hc7_degree9_pole_verifier.md
b4bab9be44feb5dc749dc8ba3f41a85094896d4b3de8a7d8246342b2729c9c59  results/hc7_degree9_pole_verifier.py
```

The first two sources have adjacent GREEN audits.  The degree-nine verifier
was rerun during this audit and returned all `4608` rooted instances with
`bad=0` and the documented final line

```text
PASS degree-nine local completion
```

Any mathematical change to the audited source, or any change to the finite
local-completion statement or verifier, invalidates this audit until the
affected checks are renewed.

## Claim checked

Under the source hypotheses, there exist a vertex `u`, a component `C` of
`G-N[u]`, and a boundary vertex `z in N_G(C)` such that

```text
7 <= d_G(u) <= 9,
chi(G-{u,z}) = 6.
```

Writing `S=N_G(C)`, `A=G[C union S]`, and `B=G-C`, the source also proves:

1. `7<=|S|<=d_G(u)<=9`, and both open shores contain a connected subgraph
   adjacent to every vertex of `S`;
2. every six-colouring of `G-uz` makes `u,z` monochromatic and induces on
   `A` an exact singleton boundary block `{z}` whose full equality partition
   does not occur in a six-colouring of `B`;
3. when `d_G(u)=7`, the `A`-side partition has one further two-vertex block
   and four further singleton blocks; and
4. at degree seven, the singleton-`z` matching languages of the two closed
   shores are nonempty and disjoint.

All four conclusions are established.

## 1. The exterior-contact set is a genuine separator

Mader's exact bound and seven-connectivity give a vertex `u` with degree
seven, eight, or nine.  The universal-vertex exclusion is sound: proper-minor
minimality gives `chi(G-u)<=6`, while `chi(G-u)<=5` would extend to a
six-colouring of `G`; hence `chi(G-u)=6`, and `HC_6` plus a universal
singleton would give a `K_7` minor.  Therefore `G-N[u]` is nonempty.

Define

```text
T = {x in N(u): x has a neighbour in G-N[u]},
R = N(u)-T.
```

After deleting `T`, the nonempty set `{u} union R` and the nonempty exterior
`G-N[u]` lie on different sides.  There is no edge between them: `u` has no
exterior neighbour, and the definition of `R` excludes every such edge from
`R`.  Thus `T` is a literal vertex cut and seven-connectivity gives
`|T|>=7`.  This remains valid when `R` is empty, since `{u}` is still a
nonempty side.

## 2. The restricted double-critical assumption still controls all of `H`

This is the main new point relative to the audited low-degree theorem.
Assume that every `x in T` satisfies `chi(G-{u,x})=5`.  A five-colouring of
`G-{u,x}` must contain a common neighbour of `u,x` in every colour.  If
colour `i` had no such common neighbour, recolour all colour-`i` neighbours
of `u` with a new sixth colour, colour `u` with `i`, and colour `x` with the
new colour.  The recoloured vertices are independent and none is adjacent to
`x`; this would six-colour `G`.  Hence

```text
d_{G[N(u)]}(x) >= 5  for every x in T.
```

For `x in R`, every neighbour of `x` lies in `N[u]`.  Seven-connectivity
gives `d_G(x)>=7`, and one of these neighbours is `u`, so

```text
d_{G[N(u)]}(x) = d_G(x)-1 >= 6.
```

Consequently `H=G[N(u)]` has minimum degree at least five even though the
five-colour deletion hypothesis was imposed only on `T`.  This is exactly
the hypothesis used by the degree-seven/eight/nine local-completion argument;
no unproved double-critical assertion about vertices of `R` is being smuggled
in.

## 3. Reuse of the degree-seven/eight/nine completion

For a component `D` of `G-N[u]`, every external neighbour of `D` belongs to
`N(u)`.  Contracting `D` to `c` therefore gives the same local quotient as in
the audited low-degree theorem, with

```text
delta(H) >= 5,
|N(c) intersect H| = |N_G(D)| >= 7,
u complete to H,
uc absent.
```

The separation lower bound follows from seven-connectivity.  The previous
local proof applies without alteration:

- degree seven violates Mader's edge bound on the nine-vertex quotient;
- degree eight either violates that bound or falls into the three explicitly
  checked complementary cycle types; and
- degree nine falls into the separately verified `4608` rooted instances.

In every exceptional local model all six branch sets meet `H`.  Replacing
`c` by the original connected component preserves the model, and `{u}` is
adjacent to every branch set because each meets `H=N(u)`.  Thus the assumption
that all `x in T` give a five-chromatic double deletion produces a `K_7`
minor.  Some `z in T` therefore satisfies `chi(G-{u,z})=6`.

By the definition of `T`, this `z` has a neighbour in a component `C` of
`G-N[u]`, so `z in S=N_G(C)`.  The usual component-neighbourhood argument
gives `S subseteq N(u)` and makes `(G[C union S],G-C)` an actual separation.
Seven-connectivity gives `|S|>=7`, while `S subseteq N(u)` gives the upper
bound nine.  The component `C` is connected and adjacent to every member of
`S`; the singleton `{u}` on the opposite open side is likewise adjacent to
every member of `S`.

## 4. Exact singleton trace and nonextension

Let `phi` be any six-colouring of the proper minor `G-uz`.  Its endpoints
must receive the same colour `alpha`, since otherwise restoring `uz` would
six-colour `G`.  Every vertex of `S-{z}` is adjacent to `u`, so none has
colour `alpha`.  Since `u` does not belong to `A`, the restriction `phi|A`
is a proper colouring of the original `A`, and `{z}` is exactly its
`alpha`-block on `S`.

The restriction to `B-uz` induces the same boundary partition.  If that
partition were induced by a proper six-colouring of the original `B`, a
permutation of its colour names would make it agree with `phi|A` on every
boundary block.  The two colourings would then glue across the actual
separation and six-colour `G`.  Therefore the partition lies in `E(A,S)`
but not in `E(B,S)`.  This argument uses equality of the full partition, not
merely the fact that `{z}` is a singleton.

## 5. Degree-seven corollaries

If `d_G(u)=7`, the separation bounds force `S=N(u)`.  In `G-uz`, the six
vertices of `S-{z}` avoid `alpha`.  Every one of the other five colours must
occur there; otherwise recolouring `u` with a missing colour and restoring
`uz` would six-colour `G`.  Hence one of those five colours occurs twice and
the remaining four once.  The repeated pair is nonadjacent, giving the
displayed one-edge matching trace on the `A` shore.

The contraction-critical neighbourhood bound from the audited low-degree
theorem gives `alpha(G[S])<=2`.  Thus every singleton-`z` boundary partition
is encoded by a matching in the complement of `G[S]-z`, and the matching has
order between one and three.

The `B`-side matching family is nonempty.  Contract the connected set
`C union {z}`; it is connected because `z in S`, and fullness of `C` makes
the contracted vertex adjacent to every member of `S-{z}`.  Expanding only
`z` after restricting a six-colouring of this proper minor to `B` is proper:
every original edge at `z` appears at the contracted vertex.  It gives an
exact singleton block `{z}`.  Finally, a matching common to the two families
would encode the same complete equality partition on both shores and would
again permit colour alignment and gluing.  The families are therefore
nonempty and disjoint, with the `A` family containing the one-edge matching
from the preceding paragraph.

## 6. Trust boundary and exact remaining gap

The audit does **not** establish any of the following stronger conclusions:

1. that the full equality partition returned by `G-uz` is attainable on the
   original `B` shore;
2. that the two singleton-`z` matching families intersect;
3. that an order-eight or order-nine boundary can be reduced to order seven
   while preserving this trace; or
4. that the palette paths from the adjacent-pair theorem preserve the
   boundary labels needed to repair `uz`.

Those are precisely the live colour-synchronization and label-preserving
composition gaps.  Subject to the pinned dependencies above, there is no gap
in the theorem as stated.
