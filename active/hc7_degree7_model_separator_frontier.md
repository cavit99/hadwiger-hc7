# Degree-seven boundary-labelled near-clique composition

**Status:** active conjectural target.  Every result described below as
proved has a separate adjacent audit.  The boundary-edge contact-exchange
or compatible-separator theorem in Section 7 is open.  Nothing here proves
`HC_7`.

## 1. The degree-seven interface is a single connected exterior

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`, and let
`u` have degree seven.  Put

\[
 S=N(u),\qquad H=G[S],\qquad F=\overline H.
\]

The anti-neighbourhood is one nonempty connected graph

\[
                         C=G-N[u].                     \tag{1.1}
\]

Thus the two closed sides of the order-seven separation at `S` are

\[
                 A=G-u=G[C\cup S],\qquad B=G[N[u]].    \tag{1.2}
\]

## 2. Exact boundary languages and one-colouring path systems

Dirac's inequality gives `alpha(H)<=2`, so a boundary equality partition
is encoded by a matching of `F`: its matching edges are the two-vertex
colour classes.  The two extension languages are exactly

\[
 \begin{aligned}
  \mathcal M(A)&=\{\{e\}:e\in E(F)\},\\
  \mathcal M(B)&=\{M:M\text{ is a matching of }F, |M|\ge2\}.
 \end{aligned}                                         \tag{2.1}
\]

Fix a nonedge `e_0=ab` of `H` and a six-colouring of `A` whose sole
repeated boundary pair is `ab`.  The five vertices

\[
                         U=S-\{a,b\}
\]

have five distinct colours.  Every edge of `F[U]` is realized by a
bichromatic path through `C` in this one fixed colouring, and paths for
vertex-disjoint edges of `F[U]` are vertex-disjoint.  Since `F[U]` is
triangle-free, it has at most six edges.  Kriesell--Mohr's Theorem 7,
applied after restricting to the five colour classes meeting `U`, packages
these paths into a `U`-rooted `K_5` model in `A-{a,b}`.

This is the required common-colouring provenance.  It is stronger than an
existential collection of paths obtained from unrelated edge deletions.

## 3. The model-carried obstruction

For every `ab in E(F)`, either `G` already has a `K_7` minor or the union
of the five rooted branch sets contains an inclusion-minimal `a-b`
separator `Z` of `A` with

\[
                              |Z|\ge6.                  \tag{3.1}
\]

The components containing `a` and `b` are each adjacent to every vertex
of `Z`, and some rooted branch set contains at least two vertices of `Z`.
The set `Z union {u}` is therefore an actual full separation boundary in
`G`.

More sharply, for each `ab` one obtains one of:

1. an explicit `K_7`-minor model;
2. a full order-seven separation `Q union {u}`, where `|Q|=6`; or
3. seven internally vertex-disjoint `a-b` paths, all meeting the union of
   the five named rooted branch sets.

The third alternative forces at least one branch set to meet two of the
paths.  Connectivity and rooted-model data alone do not split that branch
set: complete multipartite examples and `overline(K_2) join` planar
examples show that the proper-minor colouring response is indispensable.

## 4. Uniform boundary-labelled near-`K_7` model

The boundary complement and rooted models now give a stronger normal form.
There are seven disjoint connected branch sets, including `{u}` and a
singleton boundary vertex `{c}`, with every adjacency present except one or
two pairs incident with `{c}`.  Thus every degree-seven survivor has a
boundary-labelled model of `K_7^-` or of `K_7` with two adjacent edges
deleted.

This eliminates the earlier boundary-by-boundary split.  The nonisolated
part of `F` is one two-connected component on six or seven vertices.  A
degree-two complement vertex gives the one-missing-edge model directly; if
there is no such vertex, then

\[
                 F\cong K_{3,4}
        \quad\hbox{or}\quad
                 F\cong K_{3,3}\mathbin{\dot\cup}K_1,
\]

and explicit rooted bags give the two-adjacent-edge model.

## 5. The branch-set splitting step is closed

The aligned model can be made spanning while retaining its singleton pole,
singleton centre and all five boundary roots.  Spanning absorption preserves
the labels and old adjacencies, but not the colour purity or order of a
rooted bag.  The proper-minor matching response also applies to every edge
with at least one endpoint in `C`, and a degree-two vertex of `F` supplies
the two centre-preserving orientations of the one-edge defect.

The branch-set splitting problem itself is now parameter-uniform.  In a
spanning labelled `K_t^-` model with singleton centre `c`, deficient bag
`D` and `t-2` common bags, suppose one common bag contains two neighbours
of `c`.  A marked spanning-tree cut partitions that bag into adjacent
connected sets `Z,W`, both adjacent to `c`, while retaining any prescribed
root in `W`.  Then either

1. `Z` misses `D`, so `N_G(Z)` is an actual full-neighbourhood separation;
2. `W` misses another common bag, so `N_G(W)` is such a separation; or
3. `D union Z` and `W` replace the old two bags and give an explicit
   `K_t`-minor model.

For `t=7`, seven-connectivity gives `d(c)>=7`, while all neighbours of `c`
lie in only five common bags.  A multiply-hit bag is therefore automatic.
Consequently every spanning aligned one-missing-adjacency model gives

\[
                  K_7\text{ minor}\quad\text{or}\quad
                  \text{an actual full-neighbourhood separation}. \tag{5.1}
\]

This replaces the proposed unrestricted shortest-path rank.  That rank is
degenerate: the pole gives the absolute-minimum path `c-u-b`, and every
centre-to-deficient-bag path enters a common bag on its first edge.

## 6. Colour reflection and the exact residual

A second parameter-uniform theorem reflects boundary colourings.  Let
`T` separate open sides `L,R`, let `a in T`, and suppose the `R`-side has
five disjoint connected pairwise adjacent rows `Q_1,...,Q_5`, each adjacent
to `a`, which cover `T-{a}`.  A proper six-colouring of the unchanged
closed `R`-side reflects through the `L`-side whenever

1. each nonempty `T intersect Q_i` is monochromatic; and
2. either the colour of `a` occurs in one row or one row misses `T`.

The proof contracts one connected row carrier for each equality block in
the opposite shore.  It works for an arbitrary finite boundary, not only
for order seven.

Applying the marked-tree split in either orientation and merging `D` with
the opposite donor part gives five named rows satisfying all the geometric
hypotheses above.  In the non-`K_7` outcome at least one row misses the
boundary.  Simultaneous losses therefore do not create a separate
quotient case.  The exact conclusion is stronger and singular:

> every proper six-colouring of the unchanged far closed shore has a
> multicoloured nonempty row intersection.

A further audited theorem converts this universal obstruction into a
capacity condition.  Put `I_i=T intersect Q_i`, assume every `I_i` is
independent, and form the conflict graph on the nonsingleton traces by
joining two traces when a boundary edge runs between them.  If the other
open side contains `k` pairwise disjoint connected subgraphs, each adjacent
to every vertex of `T`, and the conflict graph is `k`-colourable, then
simultaneous connected contractions manufacture a far-shore colouring in
which every `I_i` is monochromatic.  Reflection then six-colours `G`.

Consequently every survivor has one of two standard graph-theoretic
obstructions:

1. some row intersection contains an edge; or
2. the chromatic number of the trace-conflict graph exceeds the maximum
   number of disjoint boundary-full connected subgraphs on the other side.

The protected-root orientation of the old double-loss configuration is
also closed directly: ownership gives five common anti-neighbours of one
boundary root; `alpha(G[N(u)])<=2` makes them a `K_5`, and the connected
full exterior supplies the remaining branch set of an explicit `K_7`
model.

## 7. The two-pair disk obstruction is now structural

At an exact order-seven boundary, the first nontrivial independent-trace
case has two disjoint independent pairs `I,J`.  Vertex-disjoint connectors
for the two pairs can be contracted simultaneously; five-row reflection
then six-colours `G`.  If those connectors do not exist, the closed shore
containing them has a genuine disk drawing with the four roots alternating
on its boundary.

The disk alternative now has an unbounded structural theorem.  If its open
side has at least two vertices, then either `G` has a `K_7` minor or one of
the paired far-side branch sets splits into a proper connected tree part
`A` and a label-preserving expanded part `X`.  The set `X` contains exactly
one nominated boundary root and misses one named residual branch set.  Both
`A` and `X` give genuine full-neighbourhood separations of order at least
seven.  Thus the residual is no longer an arbitrary web: it returns nested
host-level separators with a retained root and a retained missed label.

Two independent consequences sharpen that separator outcome.

1. Plane curvature gives an interior vertex of host degree seven or eight.
   In the degree-eight equality it has five neighbours in the disk and is
   adjacent to all three omitted boundary vertices.
2. Every nonextendable far-side six-colouring which is nonconstant on the
   four roots forces one disk vertex to see two distinct colours on the
   three omitted boundary vertices.  Deleting a boundary edge or
   contracting a common-neighbour star therefore gives a literal dynamic
   contact, not merely an abstract extension state.

The degree-eight local construction is also exact.  Let `D` be a connected
set meeting at least seven of the eight neighbours of a degree-eight
vertex `v`, split those neighbours into a three-set `B` and five cyclic
connected sets, and record adjacency between `B` and those five sets.  If
the missing adjacencies form a matching of order at most two, six explicit
branch sets all meet `D`; appending `D` gives a `K_7` minor.  A
three-connected plane graph supplies the five cyclic sets from the facial
cycle exposed by deleting `v`, provided that cycle is disjoint from `D`.

The reservation problem now has two further audited host-level reductions.

First, deleting any three vertices of the hypothetical counterexample
leaves every prescribed five-set on one cycle.  The proof is unbounded: a
noncyclable five-set after three deletions would give an actual order-seven
separation with at least five disjoint boundary-full connected subgraphs,
contradicting the exact-seven packet bound.  A separate reservation theorem
removes the chosen connected component `D`, all three omitted boundary
vertices and `v` before seeking the cycle.  If that component-deleted
residue is three-connected, Fournier's cyclability theorem gives the
required `D`-avoiding cycle.  If it is not, an order-at-most-two separator
either lifts immediately to an actual order-seven full-neighbourhood
separation or has one concentrated component containing at least `5-|Z|`
of the five nominated neighbours; every other component is contained in
that five-set.

A stronger rooted planar reduction eliminates the cycle-allocation problem
altogether.  Rooted internal four-connectivity allows one to add an
outer-face vertex `r` complete to the four roots; the result is
four-connected and planar.  Four internally disjoint `r-v` paths can be
rerouted by Tutte's stable-bridges theorem.  They use all four roots and
four of the five disk neighbours.  The unused neighbour lies in a stable
bridge whose attachments meet the two paths bounding one sector.  The
outer root cycle supplies the other three adjacencies.  Hence, for arbitrary
overlap between the root set and the five disk neighbours, there are five
pairwise-disjoint cyclically adjacent connected sets containing all five
neighbours, with the four roots in four distinct sets.  This closes both
root-clustering patterns left by the earlier Hamiltonian-cycle reduction.

Second, once five rooted cyclic connected sets are available, two distinct
boundary vertices which support the two paired traces and create independent
enlarged traces force five-row reflection.  In each of the four normalized
concentrated contact patterns, failure is therefore recorded by an explicit
set of literal boundary edges.  Contracting the two connected supports in
the original graph and deleting that boundary-edge set only in the
pulled-back far-shore colouring yields at least three absent colours.  In a
non-six-colourable host, every corresponding two-colour component joins the
boundary vertex back to the paired trace.  This uses one common colouring for
all three paths and remains valid when an obstructing boundary edge is
essential to the connected support.

Terminal-capacitated Menger now gives an exact dichotomy for those three
connections.  Either there are three paths from the selected boundary
vertex to the paired trace which are disjoint outside the prescribed
terminals, or their failure returns a connected set `A` in the open shore
whose full neighbourhood is an actual order-seven boundary.  In the latter
case the original six-colouring restricts to one closed shore of that
separation and gives a concrete equality partition: the opposite paired
trace remains monochromatic, while the selected boundary vertex shares its
colour with one of the two new separator vertices.  What remains there is
exactly to make the same partition extend through the opposite closed shore
or to build an explicit `K_7` model.

Low connectivity inside a boundary-full component is now separately
classified.  A cutvertex gives either another actual order-seven boundary
or a repair support disjoint from a boundary-full residual.  For a
two-vertex separator, an exact intersection condition on the omitted
boundary labels is necessary and sufficient for the same conclusion, and
the exceptional two-lobe and multi-lobe patterns are explicit.  A unique
portal for any boundary vertex also gives an actual order-seven boundary.
This reduction is deliberately not treated as terminal: an arbitrary
repair support need not preserve the already named far-side connected
subgraphs or the one-sided boundary colouring.  The unrestricted positive
problem is therefore concentrated in a three-connected boundary-full
component together with the listed two-cut contact concentrations.

One infinite three-connected family is also closed.  If the boundary-full
component contains a vertex adjacent to all seven boundary vertices, choose
off-centre contacts for `b` and the prescribed two-set.  Tutte's
nonseparating-path theorem gives a repair path avoiding the universal
contact vertex whose deletion leaves the component connected; that
residual is automatically boundary-full.  The endpoint degeneracies give
either the same conclusion with a one-vertex path or an actual order-seven
separation.  Hence the unrestricted geometric residue has no universal
boundary-contact vertex, apart from the still-separate obligation to
preserve the named branch sets and colouring data.

A complementary audited separator theorem handles any already-disjoint
configuration of boundary-rooted connected subgraphs and cyclic connected
sets.  Matching defects and defects confined to the unrooted fifth cyclic
set give explicit `K_7` models.  Every remaining rooted missing incidence
gives either an actual order-seven separator or a strict decrease in the
order of a literal full-neighbourhood separator, provided the missed
far-side connected subgraph meets the open shore.  The boundary-free
connected subgraph can enlarge one selected singleton-rooted subgraph, but
it may overlap the connected set reserved as the seventh branch set.

### Boundary-edge contact exchange or compatible separator

The immediate open theorem now has two exact branches.  In the
**three-path branch**, combine the packed paths with the five named
pairwise-adjacent far-side connected subgraphs, the five cyclically adjacent
disk sets supplied by stable-theta allocation, and a connected subgraph
retaining seven of the eight neighbour labels.  In the **separator branch**,
start from the concrete one-sided equality partition just described.  Prove
at least one of:

1. an explicit `K_7`-minor model;
2. an actual order-seven separation with one equality partition extending
   through both closed shores;
3. a label-preserving configuration satisfying every hypothesis of the
   audited connected-subgraph cyclic-contact allocation theorem, with
   cross-nonadjacency graph a matching of order at most two; or
4. a strict full-neighbourhood-separator descent which preserves the two
   paired traces, the selected boundary-edge response and the five named
   connected subgraphs.

The first two outcomes are terminal, and the third is terminal after the
audited contact-allocation table.  The fourth must decrease a literal host
separator, not a quotient path or an auxiliary contact graph.  Merely
returning the one-sided partition in the separator branch is not terminal;
the opposite-shore extension is the remaining colour-synchronization gate.

Neither branch closes by static composition.  A verified finite interface
has the complete stable-theta allocation, a connected subgraph meeting
seven of the eight labels and three terminal-capacitated paths, but its two
missing boundary-to-sector incidences share one boundary vertex.  Thus the
matching-defect conclusion must use seven-connectivity and the proper-minor
responses, not incidence counting.  On the separator side, two disjoint
abstract parity languages meet every one-block and every two-block exact
independent-trace query while remaining disjoint; their static two-packet
quotient is `K_7`-minor-free.  Split boundaries still synchronize by the
audited split-boundary theorem, so every live separator returned here is
nonsplit and requires a coupled host-level proper-minor transition or an
explicit labelled minor construction.

Two new barriers fix the trust boundary.  Three colour-indexed paths whose
pairwise intersections all have the common base colour may have a
three-cycle of pairwise intersection vertices: they need have neither three
internally disjoint representatives nor one common bottleneck.  Even a
common bottleneck of the selected paths need not separate the host when
other-colour bypasses are present.  Separately, a seven-connected,
`K_7`-minor-free rural example has a fully endpoint-saturated response for
every relevant incident edge but is six-colourable.  Thus the next theorem
must use the universal nonextension law and all host bypasses, not
separately chosen responses or the selected Kempe-path union alone.

Even universal nonextension for one selected boundary edge does not by
itself diversify first hits among the five named connected subgraphs: a
verified seven-connected example concentrates all three absent-colour
first hits in the boundary-free subgraph.  That example contains a `K_7`
subgraph and is not minor-minimal.  Consequently, any positive first-hit
allocation theorem must use global `K_7`-minor exclusion or proper-minor
responses away from the selected edge.

### Exact-seven first-entry and separator-excess reduction

The exact-seven separator branch now has a common orientation.  If the
six-coloured shore contains two disjoint connected subgraphs adjacent to
every boundary vertex, every boundary equality partition of demand at most
two reflects.  The only survivors are

\[
  D\mid E\mid\{r\}\mid\{z\}
  \quad(rz\notin E(G)),
  \qquad\text{and}\qquad
  D\mid E\mid\{r,z\},
  \qquad |D|=3,\ |E|=2.
\]

In either case a bichromatic `r`--`z` path exists in that shore and every
such path meets the same two named boundary-full connected subgraphs.  If
the shore has full-subgraph packing number one and a boundary-contact
transversal of order at most two, the alternative is an actual order-seven
separation, a repair subgraph disjoint from a boundary-full residual
subgraph, or a labelled alternating Two-Paths web.

For the hard exact-seven `(1,2)` case, a non-direct first-entry component
with at least five boundary contacts is closed by the audited defect-two
contraction theorem.  Hence every non-direct survivor has at most four
boundary contacts and at least three distinct attachment vertices in the
two named full subgraphs.  This is a host-level bridge condition, not an
endpoint quotient.

There is a compatible numerical reduction.  When the path avoids one named
full subgraph and leaves a connected residual `R` in the other, let
`Lambda` be the boundary contacts lost by `R` and put `U=N_G(R)-S`.  Every
failed boundary-block allocation satisfies

\[
 |U|\ge|\Lambda|\ge2,
 \qquad
 \varepsilon(R)=|N_G(R)|-7=|U|-|\Lambda|\ge0.
\]

The equality case is an actual order-seven separation.  A nested
full-neighbourhood argument strictly lowers this excess whenever a
component behind `N_G(R)` misses one of its boundary vertices.  At the
first positive value, failure of descent is exactly a boundary-full
order-eight interface.  An audited componentwise reflection theorem closes
that interface whenever it has at least four complementary components:
a boundary triangle gives an explicit `K_7` model, while a triangle-free
eight-vertex boundary is three-colourable and the other three full
components reproduce that partition on every closed component-side.  No
minimum-cut hypothesis is used.  Therefore only the two- and
three-component order-eight interfaces remain.

For the exactly-two-component remainder, the two-full-shore boundary-
absorption theorem makes the order-eight boundary four-colourable.  It
does not align the two closed-shore colourings or produce a common labelled
boundary partition.

The component-missing branch is sharper than a bare separator return.  Its
new seven-vertex boundary has exact-block-complete extension languages on
both shores.  A split boundary therefore synchronizes immediately.  In the
hypothetical counterexample the boundary is always four-colourable: the only
five-chromatic possibility from the exact-seven classification is
`K_2\vee C_5`, and its two connected full shores are eliminated by the
cycle-boundary completion theorem.  The old `D,E,r,z` labels and the
location at which the eight-set can cut the second named subgraph remain
literal; what remains open is nonsplit four-colour state transfer.

For three full components at order eight, compact boundary `K_4` models
and clique odd-cycle transversals already close.  An audited exhaustive
eight-vertex census leaves 82 boundary types, all three-colourable and all
containing two vertex-disjoint odd cycles.  This is a finite normal form,
not a proof: the selected proper-minor response need not be one of the
three-colour partitions.

Thus the next theorem has only two legitimate
forms:

1. a label-preserving nested-separation exchange which lowers the literal
   separator excess while retaining the named subgraphs and equality data;
   or
2. a proper-minor colouring or explicit minor construction closing the
   two-component interface or turning the three-component finite normal
   form into a common boundary partition.

The fixed eighteen-label quotient at the end of the three-path branch is
already closed by three explicit `K_7`-minor models.  A verified sharpness
example shows why the complete fifth labelled far-side contact is
indispensable.  The open issue is therefore compression with all five
labels, not another finite quotient census.

If curvature instead returns a degree-seven vertex, its neighbourhood is
already an exact order-seven boundary.  The remaining task there is colour
synchronization or an explicit minor, not regeneration of another
unranked degree-seven interface.  Any recursive alternative must declare a
strict host-level rank and preserve the two paired traces and named
far-side branch sets.

The earlier barriers still apply.  One response colouring, an abstract
response language, shortest-path rerouting, or web structure without
criticality cannot produce the required labelled allocation or common
partition.

Only after this one-missing-adjacency theorem is closed should the two
adjacent missing edges from the exceptional complement graphs be treated.
They share the same singleton centre and require a connected two-spoke
repair, not two unrelated paths.

The abstract deletion lattice does not close that later branch.  A verified
minimal gadget realizes exactly the all-equal response and the two exclusive
single-edge responses while forbidding the fourth equality partition and
the all-distinct partition.  Its six-colour lift contains a `K_7` minor.
Thus a positive two-edge theorem must also use global `K_7`-minor exclusion
through label-preserving contacts with the five named connected subgraphs.

## Dependencies

- [connected degree-seven anti-neighbourhood](../results/hc7_degree7_anti_neighbourhood_connectivity.md)
- [exact matching languages and simultaneous Kempe paths](../results/hc7_degree7_matching_bridge_bundle.md)
- [boundary-labelled one-/two-edge-deficient `K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
- [spanning enhancement, off-pole response and dual orientation](../results/hc7_degree7_one_spoke_bridge_corollaries.md)
- [two-mark branch-set split or separation](../results/hc7_two_mark_branch_set_split.md)
- [named-trace colour reflection across a separation](../results/hc7_five_row_separator_reflection.md)
- [full-neighbourhood separator with a multicoloured named trace](../results/hc7_universal_multicoloured_row_separator.md)
- [boundary-full connected-subgraph reflection](../results/hc7_boundary_full_subgraph_row_reflection.md)
- [disjoint trace linkage reflection](../results/hc7_disjoint_trace_linkage_reflection.md)
- [two-pair disk structure and nested separators](../results/hc7_two_pair_disk_structure.md)
- [degree-eight cyclic contact allocation](../results/hc7_degree8_contact_allocation.md)
- [five-vertex cyclability after three deletions](../results/hc7_three_vertex_deletion_five_cyclability.md)
- [reserved cycle or a low-order cut](../results/hc7_reserved_cycle_or_two_cut.md)
- [rooted Hamiltonian-cycle reduction](../results/hc7_rooted_hamiltonian_cycle_reduction.md)
- [stable-theta allocation for all four roots and five disk neighbours](../results/hc7_four_root_stable_theta_allocation.md)
- [safe-support reflection and obstructing boundary edges](../results/hc7_degree8_safe_support_reflection.md)
- [boundary-edge Kempe connections](../results/hc7_degree8_blocker_edge_kempe_fork.md)
- [three Kempe connections: disjoint packing or an exact-seven boundary](../results/hc7_kempe_fan_or_exact_seven_boundary.md)
- [boundary-rooted connected subgraphs, cyclic sets and corner separators](../results/hc7_connected_row_cyclic_corner_dichotomy.md)
- [low-order separators inside a boundary-full component](../results/hc7_boundary_full_component_low_cut_reduction.md)
- [universal boundary-contact vertex split](../results/hc7_boundary_full_universal_vertex_split.md)
- [exact-seven boundary-full connected-subgraph packing](../results/hc7_exact_seven_packet_packing.md)
- [root-protected double-loss closure](../results/hc7_root_protected_double_loss_closure.md)
- [rooted `K_5`: reserved connector or full separator](../results/hc7_exact7_rooted_k5_connector_separator.md)
- [exact-seven orientation by boundary-full connected subgraphs](../results/hc7_exact7_packet_orientation_corollary.md)
- [two-vertex boundary-contact transversal](../results/hc7_two_vertex_boundary_contact_transversal.md)
- [non-direct first-entry bridge reduction](../results/hc7_exact7_first_entry_bridge_reduction.md)
- [path-residual separator excess](../results/hc7_small_path_intersection_lobe.md)
- [nested full-neighbourhood descent](../results/hc7_nested_full_neighbourhood_descent.md)
- [degree-eight first-entry singleton peel](../results/hc7_first_entry_singleton_peel.md)
- [fixed three-path quotient completion](../results/hc7_atomic_three_path_quotient_completion.md)
- [two-full-shore boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md)
- [cycle-boundary completion](../results/hc7_cycle_boundary_completion.md)
- [exact-block bounded-interface reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md)
- [shortest-path normalization barrier](../barriers/hc7_one_spoke_shortest_path_barrier.md)
- [multicoloured-row response barrier](../barriers/hc7_multicoloured_row_response_barrier.md)
- [dynamic response-language barrier](../barriers/hc7_five_row_dynamic_response_language_barrier.md)
- [rural almost-universal-apex barrier](../barriers/hc7_two_pair_rural_almost_universal_apex_barrier.md)
- [degree-eight local allocation barrier](../barriers/hc7_degree8_contact_allocation_barrier.md)
- [curvature/contact-distribution barrier](../barriers/hc7_degree8_curvature_contact_barrier.md)
- [reserved-cycle cyclability barrier](../barriers/hc7_reserved_cycle_fournier_barrier.md)
- [saturated spoke-response barrier](../barriers/hc7_two_pair_rural_saturated_spoke_barrier.md)
- [three-path common-bottleneck barrier](../barriers/hc7_three_kempe_paths_common_bottleneck_barrier.md)
- [first-hit concentration despite universal response](../barriers/hc7_degree8_blocker_first_hit_concentration_barrier.md)
- [two-edge deletion-lattice barrier](../barriers/hc7_two_edge_deletion_lattice_barrier.md)
- [stable-theta/three-path matching-defect barrier](../barriers/hc7_stable_theta_three_path_matching_barrier.md)
- [paired-block exact-trace parity barrier](../barriers/hc7_exact7_paired_block_trace_parity_barrier.md)
- [boundary-local operation parity barrier](../barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md)
- [first-entry geometric-minimality barrier](../barriers/hc7_first_entry_packet_minimality_barrier.md)
- [missing fifth far-side contact barrier](../barriers/hc7_three_path_missing_five_row_barrier.md)
