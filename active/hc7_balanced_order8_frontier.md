# Balanced order-eight completion frontier

**Status:** current conjectural target.  This file records one live
dependency chain inside the support-six programme.  It is not a proof of
`HC_7`; claim status is governed by the linked theorem and audit files and
by [`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## 1. Exact host configuration

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  The
current branch comes from the five-leaf star in the graph of globally
support-maximal private pairs.  It has an eight-vertex separator

\[
                 S=R\mathbin{\dot\cup}V(e)
                     \mathbin{\dot\cup}V(f)\mathbin{\dot\cup}\{x\},
                 \qquad |R|=3,                         \tag{1.1}
\]

with the following audited properties.

1. `R` is a clique.
2. `e` and `f` are disjoint edges and are anticomplete to one another.
3. Each of `e,f` is collectively adjacent to every vertex of `R`.
4. `G-S` has exactly two connected components `C,D`, each adjacent to
   every literal vertex of `S`.
5. The original five-clique
   `L=R union {ell_e,ell_f}`, its five labelled defect edges, and a second
   five-clique `Y` disjoint from `L` remain present in the host.
6. Unless a `K_7` minor or an actual order-seven separation has already
   occurred, every endpoint of `e` and `f` misses at least one vertex of
   `R`; for either edge its two endpoint nonneighbour sets in `R` are
   nonempty and disjoint.

The remaining branch has additional audited structure.  Write

\[
                      L=R\cup\{\ell_e,\ell_f\},
\]

where `L` is the original five-clique and `C` is the open component
containing its two displayed vertices.  After contracting `e,f` and
deleting `R`, the resulting graph is a spanning subgraph of an
`(ell_e,ell_f,z_e,z_f)`-web.  The missing two-path linkage is precisely
the same-index pairing `ell_e-z_e,ell_f-z_f`.  The image of the second
five-clique is contained in `T union X_T` for the unique facial triangle
`T` on the virtual edge `z_e z_f`, and its vertices outside `T` lie in the
opposite open component.

Moreover, after excluding a `K_7` minor and an actual order-seven
separation, the graph

\[
                         C-\{\ell_e,\ell_f\}
\]

is connected.  It is met by `x` and by both clique vertices, contacts both
`V(e)` and `V(f)`, and misses one or two boundary vertices, including a
vertex of `R`.  Thus the live obstruction is no longer an arbitrary web or
an arbitrary collection of exterior components.

Put

\[
                          F=\overline{G[S]}.
\]

The endpoint-rigid branch in which `F` has no perfect matching is now
eliminated at its terminal order-eight residue, modulo any earlier
order-seven-separation exit.  The live complementary case is

\[
                         F\text{ has a perfect matching}.           \tag{1.2}
\]

Equivalently, `S` has a proper partition into four independent pairs.
This equivalence is only boundary data; it is not yet a common extension
through `C` and `D`.

The matching is now normalized further by audited, unbounded arguments.
Let

\[
                     H=C-\{\ell_e,\ell_f\}.
\]

Unless an explicit `K_7`-minor model or an actual order-seven separation
has already occurred, there are vertices

\[
 R=\{r,p,q\},\qquad V(e)=\{a,a'\},\qquad V(f)=\{b,b'\}
\]

such that

\[
       xr,\quad ab,\quad a'p,\quad b'q                 \tag{1.3}
\]

is a perfect matching of `F`, and `r` has no neighbour in
`H union {x}`.  Thus one matching edge is the prescribed common miss
`xr`, and one joins the two anticomplete defect edges.  We call (1.3) an
**aligned matching**.

The only Hall obstruction to (1.3) makes a different vertex of `R`
adjacent in `G[S]` to every boundary vertex except `x`; deleting those two
vertices leaves an exact six-vertex theta graph.  That whole obstruction
is eliminated, conditional on the standing support-at-most-six response,
by the all-parameter almost-universal-boundary completion theorem.  The
proof uses one Menger linkage and applies to shores of arbitrary order; it
is not a boundary census.

## 2. Exact theorem sought

Prove the following host-level lifting statement.

> **Aligned-trace lifting.**  Under (1.1)--(1.3) and the full host
> hypotheses above, at least one of the following occurs:
>
> 1. `G` contains an explicit `K_7`-minor model;
> 2. the two closed shores have six-colourings inducing the same partition
>    of the literal boundary `S`, so the colourings glue to a six-colouring
>    of `G`;
> 3. there is a two-vertex set of support height at least seven; or
> 4. there is an actual order-seven separation which preserves the named
>    clique and defect-edge data and strictly decreases a declared
>    open-side rank.

The exact unresolved implication is not the existence of the four pairs:
minor-criticality realizes each pair as an exact boundary colour class
from either orientation.  It is to combine these host-realized traces into
a common full boundary partition or a label-preserving minor construction.

This would eliminate the entire honest order-eight outcome of the
five-leaf-star reduction.  It would not orient every earlier order-seven
output, close the other private-pair kernels, or prove the full support-six
transversal theorem.

## 3. Proved structural exits

Two label-preserving branch-set constructions now close infinite
subfamilies.

1. The [asymmetric shore split](../results/hc7_star_order_eight_asymmetric_shore_split.md)
   gives a `K_7` minor from two disjoint connected subgraphs having its
   stated boundary contacts.
2. The [split-edge completion](../results/hc7_star_order_eight_split_edge_completion.md)
   needs an `ell_f`--`x` connected subgraph and a disjoint
   `ell_e`--`V(e)` connected subgraph; it uses the endpoints of `f` in two
   different branch sets.

The [disconnected leaf-side theorem](../results/hc7_star_order_eight_disconnected_leaf_side_completion.md)
combines the second construction with seven-connectivity.  It proves that
deleting `ell_e,ell_f` cannot disconnect `C`, and also excludes the case in
which every `x`--`C` edge ends at those two vertices.  This is an unbounded
closure, not a finite boundary census.

The canonical web explains why the last two-path problem cannot be solved
from planar routing alone: the required terminal pairs alternate on its
outer frame.  The next step must use contraction-critical colouring data
or a different minor model.

The planar skeleton of that canonical web is now known to be
[four-connected](../results/hc7_canonical_web_skeleton_four_connected.md),
as is either maximal-planar augmentation by an outer diagonal.  This is a
uniform structural strengthening.  Thomassen's Hamiltonian-connectedness
theorem nevertheless does not lift a labelled solution: the skeleton is a
completion supergraph of the literal quotient, and the required pairing is
the alternating outer-face linkage excluded by planarity.

## 4. A secondary host-level colouring invariant

The following opposite-edge deletion framework remains a possible engine
for aligned-trace lifting.  The matching normalization, rather than the
facial-triangle critical core alone, is now the primary interface it must
respect.

Let

\[
                         g=\ell_e\ell_f
\]

and choose an edge `h` of the second five-clique with both ends in `D`.
Such an edge exists as follows.  The clique is disjoint from `R`; because
`e,f` are anticomplete it meets endpoints of at most one of them, and it
may additionally meet `x`.  It therefore has at most three vertices on
`S`.  Rooted-web localization puts all its other vertices in `D`, so at
least two adjacent clique vertices lie there.  The two edge deletions are
operations in opposite open shores.
The audited
[opposite-shore incompatibility theorem](../results/hc_opposite_shore_minor_response_incompatibility.md)
therefore gives the following global facts.

- Every six-colouring of `G-g` induces a boundary partition different
  from every partition induced by a six-colouring of `G-h`.
- In a colouring of `G-g`, the ends of `g` have one colour and are joined
  in every corresponding two-colour subgraph.  The symmetric five Kempe
  connections hold for `h` in every colouring of `G-h`.
- More generally, the boundary-partition response languages of all
  proper minor operations internal to the two opposite shores are
  disjoint.

This is the correct global invariant, but it is an elementary gluing
constraint rather than a completion theorem.  Abstract disjoint response
languages can exist.

Put `H=G-{g,h}`, with both operations interpreted as edge deletions.  The
edges `g,h` are disjoint and there is no cross-edge between their endpoint
sets because they lie in distinct components of `G-S`.  Seven-connectivity
also implies that deleting these two edges leaves a connected graph.  The
audited [common-deletion theorem](../results/hc7_common_edge_deletion_k6_fork.md)
gives `chi(H)=6`, a spanning `K_6` model, and the response signatures

\[
                  (\mathrm{equal},\mathrm{proper}),\qquad
                  (\mathrm{proper},\mathrm{equal}),
\]

while `(proper,proper)` is impossible.  The separately audited
[double-contraction theorem](../results/hc7_common_host_double_contraction_lock_allocation.md)
supplies `(equal,equal)`.

The immediate proof obligation is to close the following exhaustive
transition alternatives in the six-colouring Kempe graph of `H`:

1. some `(equal,proper)` colouring is adjacent by one Kempe interchange to
   some `(proper,equal)` colouring;
2. no such adjacency exists, but some Kempe component contains a colouring
   of each type, in which case every path between the two types in that
   component meets an `(equal,equal)` colouring; or
3. no Kempe component contains both response types.

The audited
[opposite critical-edge transition theorem](../results/hc7_opposite_critical_edge_transition.md)
handles the first alternative.  Write `g=ab` and start from the colouring in
which `a,b` have colour `alpha`.  A direct switch uses an
`alpha`--`beta` component containing exactly one of `a,b` and exactly one
end of `h`.  In `G-g=H+h`, edge-criticality puts `a,b` in one
`alpha`--`beta` component.  They lie in distinct such components in `H`,
and `h` is the only restored edge, so `h` joins those two components.
Thus two disjoint bichromatic components each contain one end of `g` and
one end of `h`.  What remains is a
label-preserving absorption of those components into a `K_7` model.  In
the second alternative the double-contraction response must be coupled to
the spanning `K_6` model.  In the third, the separation of the two
whole-host response types must yield an actual order-seven separation or
a two-vertex set of support height at least seven.

No known general Kempe-equivalence theorem applies to `H`: it need not be
five-degenerate, regular, planar, or `K_5`-minor-free.  Connectivity of the
colouring graph must therefore be proved from the exact host hypotheses or
retained as a genuine alternative.

Three audited uniform colouring results now sharpen the double-equality
branch without assuming Kempe connectivity.

1. The [generalized two-edge Kempe fork](../results/hc7_two_deleted_edge_generalized_kempe_fork.md)
   either returns one of the one-edge-restoration responses or gives a
   fixed-end path whose colours follow a prescribed cyclic permutation.
2. Maximizing its reachable set gives the
   [reachability-maximal normal form](../results/hc7_reachability_maximal_kempe_normal_form.md):
   unless a response appears, the reachable set is the entire relevant
   three-colour component; opposite cyclic paths put the edge ends in its
   unique source strong component.
3. For disjoint natural three-colour supports, the
   [two-edge palette coupling](../results/hc7_disjoint_palette_two_edge_coupling.md)
   forbids two simultaneous response rotations and forces one named edge
   to have fixed-end paths in both cyclic orders.  This is a genuine
   coupling, but its paths may still meet the other five-clique's three
   reserved vertices.

The fixed-boundary obstruction has also been made structural.  A
simultaneous-equality boundary partition is repairable on at most one
closed shore.  On a nonrepairable shore, each alternate colour gives an
endpoint path or two disjoint first-hit paths to the literal boundary, and
a minimal induced list-critical core contains the restored edge.  On the
planar leaf side, the tight vertices of this core induce a Gallai forest
and

\[
 \sum_v c(v)=6|K|-2|E(K)|+\sum_v\varepsilon(v)
             \ge 12+\sum_v\varepsilon(v),
\]

where `c(v)` counts distinct boundary colours seen and `epsilon(v)` is
list-degree excess.  The audited
[tight-core theorem](../results/hc7_planar_boundary_critical_core_tight_case.md)
eliminates the entire zero-slack `K_4` family by an explicit `K_7` model.
The independently audited
[two-vertex completion](../results/hc7_two_vertex_fixed_boundary_core_completion.md)
also eliminates the crossed-frame edge by a boundary-endpoint selection
and seven explicit branch sets.  Its exact residue is therefore the facial
triangle at the opposite outer edge or positive slack at least thirteen.

The facial-triangle branch has a further unbounded normalization.  By the
[removable-path theorem](../results/hc7_facial_triangle_removable_path_normalization.md),
there is a path from the third facial vertex to a first vertex of `R`
which avoids both leaves and the other two vertices of `R`, and whose
deletion leaves `G` connected.  Splitting this path into its facial and
`R` sides gives six of the seven required branch sets.  The exact missing
step is to choose the split so that the facial side retains both remaining
`R` adjacencies and the connected complement retains one subgraph adjacent
to all six reserved sets.

None of these conclusions alone supplies the missing labelled linkage.
The audited barriers show this sharply: opposite cyclic paths may remain
inside the planar web even when their whole three-colour component is
strongly connected; two disjoint five-cliques can realize both cyclic
paths on complementary palettes at treewidth five; and even an
eight-connected seven-chromatic local lock example can fail every
trace-preserving repair while containing a `K_7` minor.  The next theorem
must therefore combine the critical core or reachability normal form with
the canonical missing linkage and the true host hypotheses.

## 5. Exact aligned-pair traces

Fix the aligned perfect matching

\[
                         M=\{xr,ab,a'p,b'q\}
\]

from (1.3).  For every pair `{u,v} in M` and either shore, the connected
set consisting of the opposite shore together with `u,v` may be contracted
in a proper minor.  A six-colouring of that minor
restricts to the retained closed shore and has this exact boundary trace:

- `u,v` receive one common colour; and
- no other vertex of `S` receives that colour.

Thus each matched nonedge can be selected as an exact colour class from
both orientations.  The distinguished pair `xr` is simultaneously missed
by the connected leaf-side interior, while `ab` crosses the two defect
edges.  These geometrically different traces are the current source of
leverage.  A successful transition must yield a common full boundary
partition, a branch-set construction, or a strict separator.  It is not
enough to move between abstract boundary partitions.

The independently useful all-parameter completion theorem in
[`../results/hc_uniform_boundary_repair_completion.md`](../results/hc_uniform_boundary_repair_completion.md)
is the preferred branch-set endpoint: once a compact labelled
`K_{k-2}` model is anchored to the appropriate boundary and one reserved
component plus a universal boundary vertex remain, it constructs the
`K_k` minor directly.

## 6. Guardrails

- Four-colourability of `G[S]`, or the perfect matching in `F`, does not
  synchronize the two shore extensions.  The state-free counterexamples
  are recorded in
  [`../barriers/hc7_balanced_four_colour_boundary_barrier.md`](../barriers/hc7_balanced_four_colour_boundary_barrier.md).
- Generic boundary-extension languages are too flexible.  Any positive
  theorem must visibly use contraction-critical transitions and the old
  clique/defect-edge labels.
- Simultaneous singletonization gives a spanning `K_7`-minus-one-edge
  model, but an unranked near-complete-model rotation or a separator of
  order greater than seven is not a terminal outcome.
- In the planar skeleton of the canonical web the two naive split-edge
  demands join alternating terminal pairs.  Planar routing alone cannot
  supply them, and connectivity alone does not force either linkage.
- Two missing-colour paths or a static family of edge-deletion signatures
  do not by themselves align branch-set labels.  A successful transition
  must display the `K_7` branch sets, a common boundary partition, or the
  exact separator/support output.
- Oppositely ordered generalized-Kempe paths, even when their entire
  three-colour component is strongly connected, do not force the missing
  rooted linkage in a five-connected quotient; see the
  [canonical-web barrier](../barriers/hc7_balanced_order8_two_missing_colour_paths.md).
- Disjoint natural palettes and four fixed-end replacement paths across two
  disjoint five-cliques do not force a `K_7` minor; see the
  [width-five barrier](../barriers/hc7_disjoint_palette_two_edge_decoder_barrier.md).
- Planarity of the leaf side, exact boundary locks, and local
  list-criticality do not force a repair: the
  [eight-connected lock barrier](../barriers/hc7_balanced_order8_double_equality_lock_barrier.md)
  contains a `K_7` minor and is nonminimal, so the canonical web,
  `K_7`-minor exclusion, and minor-minimality remain essential.
- The common-two-list facial triangle is not a static completion theorem.
  The [verified facial-triangle barrier](../barriers/hc7_facial_triangle_static_completion_barrier.md)
  has the balanced boundary, both full shores and five-cliques, and the
  canonical missing linkage, but has no `K_7` minor.  Its noncanonical
  three-cuts and six-colourability identify precisely where cut rigidity
  or proper-minor response data must enter.
- Even Kempe connectivity between the two response families is
  insufficient: the audited
  [opposite-response barrier](../barriers/hc7_opposite_response_kempe_bridge_barrier.md)
  is eight-connected and has a shortest transition through
  `(equal,equal)` but no direct switch or common restorable boundary
  response.  It contains a `K_7` minor and is not minor-minimal, so those
  global hypotheses must perform the remaining decoding.
- Do not restart a census of eight-vertex boundary graphs.  The matching
  is already known; the missing information is how its exact traces are
  realized inside the two shores.
- The complement induced on the boundary may have large independent sets
  even under the aligned matching and the static boundary restrictions.
  No proof may assume `alpha(G[S])<=2` without deriving it from additional
  host-level transitions.
- The feasible endpoint sets of a labelled Mader-path system do not retain
  enough information for a static delta-matroid exchange.  The
  [audited counterexample](../barriers/hc7_labelled_mader_delta_enrichment_barrier.md)
  also survives fixed twists and static auxiliary direct sums.  A viable
  algebraic exchange must encode the actual host paths, not endpoints only.

## 7. Immediate dependencies

Read each promoted theorem with its adjacent audit:

- [five-leaf star structure](../results/hc7_star_private_transversal_large_kernel.md)
- [rooted-four reduction and exact order-eight output](../results/hc7_star_kernel_rooted_four_contraction.md)
- [endpoint-contact rigidity](../results/hc7_star_order_eight_endpoint_contacts.md)
- [elimination of the no-perfect-matching shifted residue](../results/hc7_shifted_boundary_completion.md)
- [canonical rooted-web localization](../results/hc7_star_order_eight_rooted_web.md)
- [four-connectivity of the canonical web skeleton](../results/hc7_canonical_web_skeleton_four_connected.md)
- [asymmetric shore split](../results/hc7_star_order_eight_asymmetric_shore_split.md)
- [split-edge completion](../results/hc7_star_order_eight_split_edge_completion.md)
- [completion after deleting the two clique vertices disconnects their shore](../results/hc7_star_order_eight_disconnected_leaf_side_completion.md)
- [opposite-shore proper-minor incompatibility](../results/hc_opposite_shore_minor_response_incompatibility.md)
- [direct Kempe transition between the opposite critical edges](../results/hc7_opposite_critical_edge_transition.md)
- [common two-edge-deletion `K_6` fork](../results/hc7_common_edge_deletion_k6_fork.md)
- [common double-contraction response](../results/hc7_common_host_double_contraction_lock_allocation.md)
- [generalized two-edge Kempe fork](../results/hc7_two_deleted_edge_generalized_kempe_fork.md)
- [reachability-maximal cyclic normal form](../results/hc7_reachability_maximal_kempe_normal_form.md)
- [disjoint-palette two-edge coupling](../results/hc7_disjoint_palette_two_edge_coupling.md)
- [boundary-preserving double-equality criticality](../results/hc7_double_equality_boundary_criticality.md)
- [planar tight-core structure and zero-slack `K_4` closure](../results/hc7_planar_boundary_critical_core_tight_case.md)
- [explicit completion of the two-vertex critical core](../results/hc7_two_vertex_fixed_boundary_core_completion.md)
- [removable-path normalization of the facial-triangle core](../results/hc7_facial_triangle_removable_path_normalization.md)
- [uniform compact-model boundary completion](../results/hc_uniform_boundary_repair_completion.md)
- [cross-pair perfect-matching normalization](../results/hc7_balanced_cross_matching_normalization.md)
- [alignment dichotomy and elimination of its Hall obstruction](../results/hc7_balanced_aligned_matching_dichotomy.md)
- [all-parameter almost-universal straddling completion](../results/hc_almost_universal_straddling_completion.md)
- [endpoint-allocation construction and exact obstruction](../results/hc7_balanced_endpoint_allocation.md)
- [endpoint-mate refinement](../results/hc7_balanced_endpoint_mate_exchange.md)
- [unique leaf--endpoint chromatic dichotomy](../results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md)

The broader dependency chain and the still-open branches are recorded in
[`hc7_support_six_frontier.md`](hc7_support_six_frontier.md).
