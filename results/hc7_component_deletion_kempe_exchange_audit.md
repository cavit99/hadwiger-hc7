# Separate internal audit: component-deletion Kempe exchange

**Verdict:** GREEN.

This is a separate internal cold audit, not external peer review.  The
source theorem does not prove `HC_7`; it gives an operation-faithful
dichotomy for the case in which `G-N[u]` has at least two components.

## Exact revisions audited

The mathematical theorem and verifier were audited at

```text
f2dcd7f81c7994b5344748bcd29f6b685f02cfb50c776816ea7d16bfad61b21b  audited theorem content
27d3ab4a63d0c7bfa42a0d5b4ef4b5e3e0c6648e35e0953f5caffa7db30a28e2  results/hc7_component_exchange_five_core_verifier.py
```

Promotion changed only the theorem's status paragraph.  The promoted
source hash is

```text
e659b2765053c34415cad0c6e9dcec78a250e751dd80d79f8e077d064d24835f  results/hc7_component_deletion_kempe_exchange.md
```

Any mathematical change to the theorem or verifier invalidates this audit
until the affected checks are renewed.

## Claim checked

For a hypothetical minor-minimal counterexample, a vertex `u` of degree
seven through nine, and at least two components outside `N[u]`, the source
proves that `H=G[N(u)]` is four-degenerate.  Its labelled proper
five-colourings therefore form one Kempe class.  Component deletion gives
each exterior component a colouring rejected by exactly that component.

For every exterior component `D`, the source chooses a failed-lift path
whose nonempty open interior lies in `D`.  All these paths coexist
literally, and adding all their endpoint nonedges to `H` still gives a
`K_6`-minor-free graph.  It further follows that either:

1. one fixed labelled boundary colouring is rejected by at least two
   literal exterior components; or
2. one Kempe interchange changes the unique rejecting component, and the
   same interchange has failed-lift paths through both literal components.

In the second outcome the two path interiors are disjoint and anticomplete,
endpoint overlap is allowed, and the surviving augmented neighbourhood has
no `K_6` minor.  In the first outcome the source obtains simultaneous
minimal list-critical kernels with the displayed degree and chromatic
bounds, as well as one simultaneously retained failed-lift path for every
component rejecting that trace.  These conclusions are established.

## 1. Four-degeneracy and equality cases

If an induced subgraph `F` of `H` has minimum degree five, contracting two
distinct exterior components gives two nonadjacent support vertices.  The
audit checked every edge class in the resulting quotient.  For
`d_G(u)<=8` the lower bound is strictly larger than Mader's
`5|V|-15` bound.  At degree nine, orders six and nine close analytically;
the only equality layers are

```text
|V(F)|=7, |E(F)|=18, two supports of order 5;
|V(F)|=8, |E(F)|=20, two supports of order 6.
```

The retained verifier exhausts these layers.  `geng` supplies every
unlabelled graph with the prescribed order and edge count, after which the
minimum-degree filter leaves one graph at order seven and three at order
eight.  Every unordered pair, with repetition, of two-vertex miss sets is
checked: 231 marks in the first layer and 1,218 in the second.

The model search is exhaustive.  A seven-branch model on ten or eleven
vertices has at least four or three singleton branch sets, respectively.
The program enumerates every possible singleton clique and every disjoint
family of connected, mutually adjacent remaining branch sets, permitting
unused vertices.  Every returned model is then checked for disjointness,
connectedness, and all 21 branch-set adjacencies.

A fresh run returned

```text
layer h=7 e=18 graphs=1 marks=231 residues=0
layer h=8 e=20 graphs=3 marks=1218 residues=0
total_marks=1449 residues=0
catalogue_sha256=0ef56bb5ba5a44e5c699f2d0a81c1f74cc9eb35e5a52aed4dc6846817948900d
witness_sha256=b5af511f5eccf17baf6bd2dc8affa792d1391eb3128bc57111d4703227277caa
PASS component-exchange five-core classification
```

The verifier runs parser, augmentation, positive-model, and negative-model
self-tests before the census and fails if either deterministic output hash
differs.  A temporary NetworkX cross-check independently decoded every
surviving graph and validated all 1,449 certificates.

## 2. Rejection map and Kempe transition

For each component `D`, a six-colouring of the proper minor `G-D` uses at
most five colours on `X`, because the colour of `u` is absent there.  It
extends through every other exterior component.  If it also extended
through `D`, labelled gluing would six-colour `G`; hence its rejection set
is exactly `{D}`.  Conversely, a boundary colouring rejected nowhere would
extend component by component and, after assigning the sixth colour to
`u`, would also six-colour `G`.

Las Vergnas--Meyniel Proposition 2.1 applies with exactly five colours to
the four-degenerate graph `H`.  If every rejection set is a singleton,
connectedness of this Kempe graph and the existence of at least two labels
force an edge whose ends have different labels.

The forward and reverse path orientations were checked.  Starting from an
extension on the component that accepts the first endpoint colouring, the
interchange can fail only if an `alpha`--`beta` component joins the switched
boundary component to another boundary component.  A shortest route has
all internal vertices in that literal exterior component.  Reversing the
same interchange gives the second path in the other component.

## 3. Minor lift and simultaneous kernels

The universal path selection was checked component by component.  Fix
distinct `C_0,C_1`.  Along a Kempe path from `phi_{C_0}` to `phi_{C_1}`,
some step changes `C_0` from rejected to accepted; reverse lifting gives
its supported path.  For every `D ne C_0`, a Kempe path from `phi_{C_0}`
to `phi_D` starts with `D` accepted and ends with `D` rejected; forward
lifting at its first such step gives the path supported in `D`.  These
moves may be unrelated, but their open path interiors lie in distinct
components of `G-N[u]` and are therefore pairwise disjoint and
anticomplete.

Contracting all open interiors simultaneously realizes
`H+{f_D:D component of G-N[u]}` as a minor of `G-u`.  Overlapping or
repeated endpoint pairs cause no identification of distinct boundary
vertices: all interiors incident with one endpoint merely enlarge that
endpoint's connected preimage.  Thus a `K_6` model in the full
augmentation would lift to six bags each meeting `X`, and `{u}` would
complete an explicit `K_7` model.

Contracting each open path interior toward a boundary endpoint realizes
`H+e_C+e_D` as a minor of `G-u`.  If the endpoint pairs overlap, the two
interiors assigned to the common endpoint merely enlarge the same connected
preimage; distinct boundary vertices are never identified.  Every branch
set in a lifted `K_6` model still meets `X`, so the singleton `{u}` is
adjacent to all six and completes an explicit `K_7` model.

For a rejected colouring, extension through `D` is exactly the stated
list-colouring problem.  A vertex-minimal induced non-list-colourable
subgraph is connected.  Colouring after deleting one vertex proves
`d_K(v)>=|L(v)|`.  The `6-k` colours absent from the boundary occur in
every list, so a `(6-k)`-colouring would be a list-colouring; consequently
`chi(K)>=7-k`.  Kernels in distinct exterior components are literal,
disjoint, and anticomplete.

For a fixed trace rejected by several components, connect it separately to
a private colouring that accepts each rejected component.  Its first
rejected-to-accepted transition gives a path in that component.  The same
disjoint-component argument retains all of these paths simultaneously and
proves that their complete endpoint augmentation is `K_6`-minor-free.

## 4. Trust boundary

The audit does not assert that either outcome is terminal.  In particular,
the simultaneous kernels do not yet have the rooted contacts needed for a
`K_7` model, and neither the full component-supported augmentation nor its
common-trace specialization is otherwise classified.  The theorem also
says nothing about the case in which `G-N[u]` is connected, including the
tight pole residue.
