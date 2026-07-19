# Independent internal audit of the singleton exact-seven terminal normal form

**Verdict:** GREEN for the exact source revisions

```text
results/hc7_singleton_exact7_terminal_normal_form.md
SHA-256 f9af9b8edc55af116151cc7c7e3b4d30532fb44c338faee6239b888f36297feb

results/hc7_singleton_exact7_boundary_census.py
SHA-256 2702e9546a8f17cb9b99cb314b7a7ca06627fb0f5d6999d1c9ef9ed212049a21
```

The theorem-source change from the initially checked revision is limited
to the opening status paragraph recording this GREEN audit; the mathematics
and census logic are unchanged; the script hash also reflects only the
updated repository-relative invocation path after promotion to `results/`.

This is a separate internal mathematical and computational audit, not
external peer review.  It checks the full-subgraph packing calculation, the
cutvertex and bridge reductions, the matching-list construction and degree
inequality, the exact scope of the Gallai-tree conclusion, and the finite
seven-vertex boundary census.

## 0. Imported setting

The source works at a degree-seven vertex `a`, with literal boundary
`S=N_G(a)` and connected anti-neighbourhood `C=G-N_G[a]`.  The promoted
inputs supply:

* seven-connectivity, seven-chromaticity and `K_7`-minor exclusion;
* six-colourability of every proper minor;
* connectedness and boundary-fullness of `C`;
* `alpha(G[S])<=2`;
* a matching of order three in the complement of `G[S]`; and
* the exact-seven full-subgraph packing and adaptive reflection theorems.

The source does not silently assume that the surviving packing-one boundary
is Moser.  The Moser classification is used only inside the contradicted
packing-two branch.

## 1. The exterior packing number is exactly one

The singleton `{a}` is one boundary-full connected subgraph on its side of
the actual order-seven separation.  The exact-seven packing theorem therefore
gives `nu(C)<=3`.  Seven-connectivity makes connected `C` adjacent to every
literal vertex of `S`, so `nu(C)>=1`.

The adaptive `(1,3)` theorem excludes `nu(C)=3`.  If `nu(C)=2`, the adaptive
`(1,2)` theorem places the boundary in its audited 129-type residual.  Dirac's
neighbourhood inequality at the degree-seven vertex supplies `alpha(G[S])<=2`.
The independently audited extraction from that residual leaves precisely the
Moser spindle and its specified one-edge extension, and the connected-rich
one-anchor construction excludes both when the rich side is the connected
graph `C`.  These are exactly the hypotheses under which that finite
extraction may be invoked.  Hence `nu(C)=1`.

## 2. Cutvertices and bridges

Let `z` be a cutvertex of `G[C]`.  Every component `D` of `C-z` has

\[
                         N_G(D)\subseteq S\cup\{z\}.
\]

Because `C` is connected, every such component is adjacent to `z`.  It is
separated from `a` and from another component of `C-z`; seven-connectivity
therefore gives at least six neighbours in `S`.  If all components were
adjacent to all seven boundary vertices, two components would be disjoint
boundary-full connected subgraphs, contrary to `nu(C)=1`.  Thus one component
has exactly six boundary neighbours, and its full neighbourhood is those six
vertices together with `z`.  This is an actual order-seven separation with
two nonempty open sides.

For an edge `zd` into that component, every six-colouring of `G-zd` makes
`z,d` monochromatic.  Its restriction to the opposite closed shore is
proper.  If its equality partition on `N_G(D)` extended through the intact
`D`-shore, a palette permutation would align the two assignments and
six-colour `G`.  Therefore the component and the selected edge form a generic
exact-seven response interface, and `D` is a proper subset of `C`.

The bridge argument is the edge analogue.  Each of the two connected sides
has at least six boundary neighbours because its full neighbourhood consists
of those neighbours and the opposite bridge endpoint.  They cannot both be
boundary-full.  One side consequently has exactly six boundary neighbours,
and the same deletion-colouring argument applies.  No two-connectivity
stronger than seven-connectivity of the host is used.

## 3. Matching-list construction and degree inequality

An order-three matching `M` in the complement of `H=G[S]` partitions six
boundary vertices into three independent pairs.  Giving each pair one
distinct colour and the unmatched vertex a fourth colour is a proper boundary
colouring.  For `v in C`, if `k=|N_S(v)|`, exactly `t_M(v)` duplicated pair
colours occur among its boundary neighbours.  Hence the number of distinct
forbidden colours is `k-t_M(v)` and

\[
                         |L_M(v)|=6-k+t_M(v).
\]

If `C` were `L_M`-colourable, that colouring would combine with the boundary
colouring and one of the two unused boundary colours on `a`, contradicting
`chi(G)=7`.  An inclusion-minimal induced non-`L_M`-colourable subgraph `K`
is connected, and the standard vertex-deletion extension argument gives

\[
                         d_K(v)\ge |L_M(v)|.
\]

Every neighbour of a vertex of `C` lies in `C union S`; it has no edge to
`a`.  Thus `d_K(v)<=d_C(v)=d_G(v)-k`.  Combining the two displayed formulas
gives the exact necessary inequality

\[
                         t_M(v)\le d_G(v)-6
                         \qquad(v\in K).
\]

If a literal exterior vertex violates this inequality, it is not in `K`, so
`K` is a proper connected subgraph of `C`.  Its full neighbourhood separates
it from `a` and has order at least seven.  At equality, any crossing edge and
its deletion colouring give a generic exact-seven selected response by the
same gluing contradiction as above.  When the boundary has order at least
eight, the source correctly records only positive separator excess, not a
descent.

The degree-seven and degree-eight contact restrictions are immediate
specializations and are stated only when the separator outcome has not
already occurred.

## 4. Exact Gallai scope

The source does not infer a Gallai tree from minimal list-uncolourability
alone.  It adds the equality hypothesis

\[
                         d_G(v)=6+t_M(v)
                         \qquad(v\in K).
\]

Under this hypothesis,

\[
 |L_M(v)|\le d_K(v)\le d_C(v)=|L_M(v)|,
\]

so equality holds and every neighbour of each vertex of `K` inside `C` also
belongs to `K`.  Connectedness of `C` then forces `K=C`.  The lists now have
order exactly the degree at every vertex of connected `C`, and the
Borodin--Erdos--Rubin--Taylor degree-choosability theorem gives that `C` is a
Gallai tree.  If `C` is two-connected, its sole block is complete or an odd
cycle.  This use of Gallai's structure theorem is valid and is sharply
separated from the general positive-excess case.

## 5. Finite census

The verifier enumerates `networkx.graph_atlas_g()`, which is the complete
unlabelled graph atlas through seven vertices, and keeps precisely the
seven-vertex members satisfying the four displayed predicates.

The predicates are encoded faithfully:

* `alpha(H)<=2` is computed as the maximum clique order in the complement;
* an order-three complement matching is tested by maximum-cardinality
  matching;
* `overline(K_2) join H` is constructed with two nonadjacent new vertices
  complete to the seven boundary vertices;
* exact `K_7`-minor detection recursively applies vertex deletion and edge
  contraction until seven vertices remain; edge deletion is unnecessary for
  clique-minor existence because extra edges do not invalidate a model; and
* the nonisolated complement core is tested for order, connectedness,
  biconnectedness and minimum degree.

The contraction routine replaces the two endpoint neighbourhoods by their
union and suppresses the contracted endpoint, so it implements simple-graph
edge contraction correctly.  Memoization affects only runtime.

The verifier was rerun with the pinned runtime and printed exactly

```text
VERIFIED singleton_exact7_boundary_types=20 degree_two_complement=18 exceptional=2 moser_types=2_not_exhaustive
```

Independent positive and negative controls also passed: `K_7` contains a
`K_7` minor, `K_6` does not, and subdividing one edge of `K_7` preserves a
detected `K_7` minor.  The 18/2 split and the identifications of the two
exceptions as `K_{3,4}` and `K_{3,3}` plus an isolated vertex are checked by
isomorphism, not inferred from graph6 names.  The standard Moser graph and
its specified one-edge extension are both verified to occur among the twenty
survivors.

The census is only a classification under four necessary boundary
conditions.  It does not assert that any survivor is realizable in a
hypothetical counterexample, and it does not infer an unbounded theorem from
the finite list.

## 6. Exact trust boundary

The source proves an unbounded packing-one reduction, removes every
cutvertex and bridge exterior by a strict exact-seven restart, and gives a
valid matching-list separator mechanism with a precisely delimited Gallai
equality cell.  The finite census narrows only the literal seven-vertex
boundary.

It does not eliminate a two-connected nonbipartite packing-one exterior,
force positive separator excess down to zero, synchronize the colourings of
an order-seven separator, split the labelled rooted-model branch sets, or
prove `HC_7`.
