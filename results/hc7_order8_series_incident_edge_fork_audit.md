# Independent audit: two crossed critical edges at a series separation

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It checks the labelled-subgraph placement, the common-deletion chromatic and
connectivity fork, the degree-seven neighbourhood corollary, the
incident-edge first-exit statement, and the stated trust boundary.  It does
not prove the remaining label-preserving exchange or `HC_7`.

## Audited revision

The audited source is
[`hc7_order8_series_incident_edge_fork.md`](hc7_order8_series_incident_edge_fork.md).

**Source SHA-256:**

```text
76c4913f81082f3593c43e221031336280b1e44ca7cdf7c0a43aaddb947717a5
```

The promoted revision differs from the audited mathematical source only in
its status line and adjacent-audit link; the theorem statement and proof are
unchanged.

## 1. Inputs, outputs, and invariants

The source works under five essential inputs: seven-connectivity and
minor-critical six-colourability; the exact two-lobe identities for
`C_d,C_e`; the disjoint adjacent labelled subgraphs `A_d,A_e`; the two
crossed neighbours `u in C_e`, `v in C_d`; and the existing
simultaneous-contraction colouring response.  In particular, `uv` is absent
because the two lobes are distinct components of `G[L]-z`.

The proof preserves three literal invariants throughout:

1. `C_d` and `C_e` have no edge between them and can communicate inside
   `L` only through `z`;
2. their full neighbourhoods are exactly
   `{z} union (S-{e})` and `{z} union (S-{d})`; and
3. palette colours are never identified with the labels
   `P_0,P_1,A_d,A_e`.

Its outputs are conditional: a rooted four-vertex model exists in the
common deletion; an order-five cut of that deletion gives a degree-seven
singleton separation which is colouring-incompatible; and the nonsaturated
incident-edge response has a literal first exit from one native lobe.  No
output is claimed to preserve all four old connected-subgraph labels.

## 2. Placement of `A_d,A_e`

The argument in source lines 85--94 is correct.  Since `A_e` is adjacent
to `d`, while `d` has no neighbour at `z` or in `C_e`, the connected set
`A_e` meets `C_d`.  Symmetrically `A_d` meets `C_e`.  A connected one of
these subgraphs which omits `z` is confined to the component that it meets.

They cannot both omit `z`, because their retained adjacency would then be
an edge between `C_d` and `C_e`; they cannot both contain `z`, because they
are disjoint.  Hence exactly one contains `z`, and the other is wholly in
the opposite named lobe, exactly as Lemma 2.1 states.  This reasoning does
not locate `u` or `v` inside either labelled subgraph, and the source does
not claim that it does.

## 3. Chromatic number, exact trace, and connectivity

The graph `H=G-{zu,zv}` is a proper minor and is therefore six-colourable.
If it were five-colourable, assigning a fresh sixth colour to `z` would
make both restored incident edges proper and would preserve every other
edge.  This would six-colour `G`, so `chi(H)=6`.

For any separation `(A,T,B)` of `H`, seven internally disjoint paths in
`G` between its open sides either consume distinct vertices of `T` or use
one of the two deleted edges.  Each deleted edge supports at most one path
in such a family, so `|T|+2>=7` and `kappa(H)>=5`.  Incidence of the two
edges at `z` cannot weaken this upper bound; at equality it supplies the
stronger singleton conclusion checked below.

Contracting the two-edge star on `z,u,v` is legitimate, and `uv` being a
nonedge makes expansion proper after deleting `zu,zv`.  Every neighbour of
`z` other than `u,v` remains adjacent to the contracted image.  It must
therefore avoid the image colour, giving precisely

```text
N_G(z) intersect kappa^{-1}(alpha) = {u,v}.
```

These steps verify (3.1)--(3.2).

## 4. Rooted model in both connectivity branches

The equality `chi(H)=6` makes `H` nonplanar by the Four Colour Theorem.
The already proved `kappa(H)>=5` is stronger than the four-connectivity
hypothesis in Jung's nonplanar two-linkage theorem.  Thus `H` is two-linked
whether its connectivity is five or at least six.

For any four distinct nominated vertices, two-linkedness supplies each of
the three possible two-path pairings.  The rooted-`K_4` characterization
for a three-connected graph then gives a `K_4` minor rooted at those four
vertices.  In particular it applies to `z,u,v,r` for every fourth vertex
`r`.  The revised source correctly states this conclusion before splitting
into the two connectivity cases; it does not incorrectly reserve it for
the high-connectivity case.

The resulting rooted branch sets are unrestricted away from their four
roots.  They can therefore consume vertices of `P_0,P_1,A_d,A_e`, so this
theorem alone does not append those old labels to a `K_7` model.

## 5. The order-five cut is a singleton-side order-seven separation

At an order-five separation, both deleted edges must cross: five separator
vertices account for at most five of the seven disjoint paths, and both
remaining paths require the two restored edges.  Since the edges share
`z`, orient the cut with `z in A` and `u,v in B`.

If `A-{z}` were nonempty, deleting `T union {z}` would remove both restored
edges and separate `A-{z}` from `B` in `G`, contradicting
seven-connectivity.  Hence `A={z}`.  All neighbours of `z` then lie in
`T union {u,v}`; minimum degree seven forces

```text
d_G(z)=7,  N_G(z)=T dotunion {u,v}.
```

The opposite residual side is nonempty after deleting the boundary.  If
`B={u,v}`, either outer vertex could see only `z` and the five vertices of
`T`, because `uv` is absent, contradicting minimum degree seven.  Thus
`N_G(z)` is the boundary of an actual separation with singleton open side
`{z}`.

The partition incompatibility is also correct and is not inferred merely
from one selected colouring.  Every six-colouring of `G-z` must use all
six colours on `N_G(z)`, or its missing colour could be assigned to `z`.
Every six-colouring of `G[N_G[z]]` uses at most five colours on the
boundary, because the colour of the universal-to-boundary vertex `z` is
absent there.  Therefore no equality partition occurs on both closed
shores.  In the simultaneous-contraction colouring, `u,v` have the one
common colour and the five vertices of `T` use the five other colours
once each, proving the exact partition (3.6).

## 6. Degree-seven neighbourhood corollary

The six neighbours supplied by the three merged-root paths are pairwise
distinct as assumed by the parent series theorem.  Vertices in the two
triples are anticomplete across the triples because they lie in different
components of `G[L]-z`.

Dirac's neighbourhood-independence inequality gives
`alpha(G[N(z)])<=2`.  A missing edge inside either triple, together with
any vertex of the other triple, would violate this inequality; hence both
triples are triangles.  If the seventh neighbour `w` missed one vertex in
each triangle, those two anticomplete vertices and `w` would again be an
independent triple.  Thus `w` is complete to one triangle and the
neighbourhood contains the asserted literal `K_4`.

This corollary does not claim that the boundary `K_4`, the singleton
branch, and the one remaining exterior component already form a `K_7`
model.  That stronger inference would require an additional split of the
exterior component.

## 7. Incident-edge bypass and the first exit

The nonedge `uv` is exactly the outer-leaf nonedge required by the audited
incident-edge saturation-or-bypass theorem.  Applying it to the expanded
simultaneous-contraction colouring gives either a five-colour-saturated
edge or the two switched components `K_u,K_v` with the exclusions in
(4.1), an intersection or joining edge, and the two stated one-edge
responses.

If both switched components remained inside their native lobes, they would
be disjoint and anticomplete.  This contradicts their required intersection
or joining edge.  Hence one leaves.  A path from its native root to its
first outside vertex meets the full neighbourhood of that lobe.  The
exclusion of `z` in (4.1) leaves exactly `S-{d}` for an exit from `C_e`, or
`S-{e}` for an exit from `C_d`.  Proposition 4.1 follows.

The first exit is literal but not label-allocating: lobe fullness already
provides uncoloured contacts with those boundary sets, and the contraction
colouring need not induce the selected `X|Y` boundary partition.  Thus the
switch cannot be glued through the old opposite response merely by
renaming colours.

## 8. Dependencies and trust boundary

The proof uses the exact two-lobe response-propagation theorem, the ordered
deficient-subgraph geometry, the audited incident-edge bypass theorem,
Dirac's contraction-critical neighbourhood inequality, Jung's theorem,
and the rooted-`K_4` characterization.  Each use matches its stated
hypotheses.  There is no computational or finite-enumeration input.

At the audited hash the source proves:

1. exact placement of one old deficient connected subgraph in a native
   lobe and of `z` in the other;
2. `chi(H)=6`, `kappa(H)>=5`, the simultaneous-contraction trace, and a
   rooted `K_4` at every four nominated vertices;
3. a degree-seven singleton-side separator with intrinsically disjoint
   boundary-partition languages whenever `kappa(H)=5`;
4. two anticomplete neighbourhood triangles and a literal neighbourhood
   `K_4` in that low-connectivity case; and
5. one literal boundary first exit in the nonsaturated incident-edge
   branch.

It does **not** prove that the rooted model preserves the four named
connected subgraphs, that the first exit lands in a prescribed branch-set
label, that either Kempe switch preserves the selected boundary response,
that the returned singleton separator is colour-compatible, or that `G`
has a `K_7` minor.  No unresolved gap remains inside the statements
actually made at the audited source revision.
