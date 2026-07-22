# Bounded-interface bridge composition

**Status:** sole exhaustive all-degree target.  Sections 1--3, 5 and 6
summarize separately audited results; the theorem in Section 4 and the
terminal decoder in Section 7 remain open.  The
degree-seven branch has a sharper conditional refinement in
[`hc7_degree7_model_separator_frontier.md`](hc7_degree7_model_separator_frontier.md),
but it does not replace this global obligation.  Nothing here proves `HC_7`.

## 1. Uniform entry from every hypothetical counterexample

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  There
exist a vertex `u`, a component `C` of `G-N[u]`, and

\[
 z\in S:=N_G(C)\subseteq N(u)
\]

such that

\[
 7\le d_G(u)\le9,
 \qquad 7\le |S|\le d_G(u),
 \qquad \chi(G-\{u,z\})=6.                       \tag{1.1}
\]

Put

\[
 A=G[C\cup S],\qquad B=G-C.                     \tag{1.2}
\]

Then `(A,B)` is an actual separation.  The connected set `C` and the
singleton `{u}` are each adjacent to every boundary vertex.  Moreover,

\[
 \chi(G[S])\le4,
 \qquad \alpha(G[S])\le4,
 \qquad \overline K_2\vee G[S]
       \text{ has no }K_7\text{ minor}.           \tag{1.3}
\]

For every nonempty independent `I subseteq S`, both closed shores have a
six-colouring in which `I` is exactly one boundary colour class.

The edge `uz` gives a named asymmetric response.  Every six-colouring of
the edge deletion `G-uz` makes `u,z` monochromatic and induces on `A` an
exact singleton boundary block `{z}`.  That complete boundary partition
does not extend to the original shore `B`.

The audited
[component-uniform alignment theorem](../results/hc7_component_uniform_boundary_alignment.md)
strengthens this entry at the same `u`: every component `D` of `G-N[u]`
has a vertex `z_D in N_G(D)` with `chi(G-{u,z_D})=6`.  Thus a later actual
component has its own named response; the old `z` need not belong to
`N_G(D)`.

The audited
[low-degree exterior-component bounds](../results/hc7_low_degree_exterior_component_bounds.md)
also give

\[
 \#\operatorname{comp}(G-N[u])\le1,2,3
 \quad\text{when}\quad d_G(u)=7,8,9,
\]

respectively.  Hence every multi-component entry has at most three literal
components before the response geometry is analysed.

## 2. What static boundary information settles

If `G[S]` is split, the two shore colourings synchronize.  Indeed, for a
split partition `S=I dotunion Q` with `I` independent and `Q` a clique,
the cylinder having `I` as an exact block consists of the unique partition

\[
                         I\mid\{q\}\ (q\in Q).
\]

Both shores attain it, so their colours align and glue.  Hence every live
boundary is nonsplit.

This is the exact limit of the static argument.  For every nonsplit graph
`H` with `chi(H)<=4`, parity of the number of blocks splits all proper
six-colour partitions into two disjoint languages, each meeting every
exact-block cylinder.  These abstract languages need not arise from an
actual contraction-critical host, but they rule out any proof using only
independent-block attainability.

One additional infinite family is closed geometrically.  If the boundary
contains adjacent vertices `p,q` complete to a two-connected remainder
`X`, both open shores are connected and full to the boundary, and
`G-{p,q}` has a `K_5` minor, then a rooted-planarity argument gives an
explicit `K_7` minor.  Thus that branch requires no colour synchronization.

## 3. Forced pole-free paths

Fix `x in S`.  Begin with a six-colouring of the edge deletion `G-ux`;
the colour of `u=x` is an exact singleton colour on `S`.  Connect its
boundary colouring, inside that exact-singleton cylinder, to a boundary
colouring extending through `B`.  Four-degeneracy of `G[S-x]` and the
Las Vergnas--Meyniel theorem make this cylinder Kempe-connected.

Not every boundary interchange can lift to `G-ux`, or the final colouring
on `A` would glue to the chosen colouring on `B`.  The first failed lift
therefore gives a bichromatic path whose ends lie in distinct two-colour
components of `G[S]`, whose internal vertices avoid `S union {u,x}`, and
whose interior lies wholly in one open shore.

If it lies on the `u`-side, it meets at most three components `D` of
`G-N[u]` other than `C`, and each satisfies

\[
                         |N_G(D)\cap S|\ge |S|-2\ge5. \tag{3.1}
\]

This result holds for every `x in S`.  It converts arbitrary movement in
the boundary-colouring space into literal host paths with bounded contact
defect.

## 4. Primary open theorem

### Pole-free bridge composition theorem

Under the setup above, use the family of paths forced in Section 3 to
obtain at least one of:

1. an explicit `K_7`-minor model in `G`;
2. one equality partition of `S` induced by six-colourings of both `A`
   and `B`; or
3. another instance satisfying Sections 1--3 in the same graph, with a
   strictly smaller chosen anti-neighbourhood component, equipped with its
   own component-local edge-deletion response.

The third outcome must decrease the order of the literal connected
component in `G`; auxiliary path length, quotient size, or an unlabelled
minor model is not a valid rank.

The first two outcomes contradict the definition of `G`, while the third
permits finite descent.  A terminal singleton component is impossible:
in a six-colouring of the opposite shore, the colour of `u` is absent from
`S` and can be assigned to that one vertex, six-colouring `G`.  Hence this
theorem, together with the audited entry reduction, would prove `HC_7`.

## 5. Audited multi-component exchange

Suppose `G-N[u]` has at least two components and put `X=N(u)`,
`H=G[X]`.  The audited
[component-deletion exchange theorem](../results/hc7_component_deletion_kempe_exchange.md)
proves that `H` is four-degenerate.  For each labelled proper
five-colouring `phi` of `H`, let `R(phi)` be the set of exterior components
through which `phi` does not extend.  Every `R(phi)` is nonempty, and each
component `D` has a private colouring `phi_D` with `R(phi_D)={D}`.

One failed-lift path can be chosen through every exterior component
simultaneously.  If `f_D` is its boundary endpoint nonedge, then

\[
 K_6\not\preccurlyeq
 H+\{f_D:D\text{ is a component of }G-N[u]\}.        \tag{5.1}
\]

The paths may come from unrelated Kempe moves and their boundary endpoints
may overlap.  Their open interiors remain disjoint and anticomplete because
they lie in different literal components; this is enough for the simultaneous
minor lift establishing (5.1).

The rejection map gives two structural branches.

1. Some one boundary colouring is rejected by at least two components.
   Those components contain simultaneous minimal list-critical kernels and
   simultaneous failed-lift paths for the same fixed trace.  The kernels
   have the proved degree and chromatic lower bounds, but their boundary
   contacts are not yet sufficient for branch-set allocation.
2. Every rejection set is a singleton.  One Kempe move transfers the unique
   rejector from one component to another and has failed-lift paths in both.

In the second branch, the audited
[full-component common-root theorem](../results/hc7_full_exterior_component_common_root_exchange.md)
adds a dichotomy.  If a component `E` is not full to `X`, its boundary has
order between seven and `d(u)-1` and carries its own component-local response.
This lowers boundary order but is not by itself a strict component descent.
If every exterior component is full to `X`, then exactly two remain, `H` is
three-degenerate, and one legal recolouring at a vertex `x` transfers the
unique rejector.  The two failed lifts have the same literal root `x`,

\[
 \chi(G-x)=6,
\]

and the two supported nonedges still form a `K_6`-minor-free augmentation.
The established case `HC_6` gives an unrooted `K_6` minor in `G-x`; the
missing inference is a model whose six bags all meet `N(x)`, so that the
singleton `{x}` can be added.  No universal rooted-minor assertion is made.

The audited
[antipodal flip-cube fork](../results/hc7_common_root_flip_cube_fork.md)
sharpens the full two-component outcome in two independent ways.  First, the
spliced six-colouring has exclusive exchanged-colour contacts in the two
exterior components, and criticality joins them by an induced odd cycle
through `x`.  Second, complement symmetry of the unique-rejector map on the
two-colour flip cube forces one cube vertex with rejector-changing edges in
two coordinates.  For the corresponding one fixed accepted extension,
either both operated boundary components lie in one full two-colour
component, or two disjoint full two-colour components supply two disjoint
paths through one exterior component.  A separately obtained path through
the other component then gives either:

1. three distinct supported boundary nonedges whose augmentation is
   `K_6`-minor-free; or
2. a bilateral realization of one boundary nonedge through both exterior
   components, together with the other fixed-extension path.

The separately audited
[alternating full-component cycle theorem](../results/hc7_common_root_alternating_trace_cycle.md)
replaces the remaining isolated-path view by a coherent cyclic invariant.
For either rejector-changing coordinate, fix one extension on the accepting
shore before the switch and one on the other shore after the switch.  The
full two-colour components in these fixed extensions partition the boundary
two-colour components.  Arbitrary unions of partition blocks are independently
switchable.  If the two resulting affine switch spaces intersected, the same
labelled boundary colouring would extend through both shores and six-colour
`G`.

Equivalently, form the bipartite multigraph whose vertices are the two sets
of full-component blocks and whose edges are the boundary two-colour
components.  The operated coordinate is outside the incidence cut space,
so it is not a bridge and lies on a cycle.  A parallel-edge two-cycle is a
bilateral full-trace outcome.  Every longer shortest cycle is an alternating
sequence of literal full two-colour components from the two fixed extensions;
same-shore members are disjoint and anticomplete, and nonconsecutive members
are disjoint and anticomplete.  No clean internal path or branch-set split is
inferred.

The separately audited
[short-trace classification](../results/hc7_common_root_short_trace_classification.md)
now applies the sharp neighbourhood independence bound.  The trace
multigraph has at most three edges in degree eight and at most four in
degree nine.  Therefore:

1. in degree eight every trace cycle is a parallel pair, and the two fork
   coordinates lie in one common full component of the fixed accepted
   extension; this is either a bilateral pair or an atomic three-trace
   configuration, and the fork can be chosen to retain the original
   singleton root `x` as one operated trace;
2. in degree nine every trace cycle is a parallel pair or one exact
   four-cycle; if the two fixed components are distinct, their traces form
   an exact `2+2` partition and each separately chosen opposite-shore
   response is bilateral or transverse to it; and
3. in the four-cycle case all four boundary traces are `K_1` or `K_2`, the
   carrier paths have clean alternating shore interiors, and they form an
   odd cycle with two crossing same-shore connectors.  This gives an
   `X`-meeting `K_4` model in `G-u` and an explicit `K_5` model after adding
   `{u}`; and
4. in either tight atomic case, one representative per trace is a maximum
   independent set.  Contracting its star with `u` forces the other five
   boundary vertices to use the five remaining colours individually on
   `G-u`, while every exact-block colouring of the pole-containing shore
   must merge at least one pair of those five reserve vertices.

The separately audited
[parallel-cycle normalization](../results/hc7_common_root_parallel_two_cycle_normalization.md)
gives the exact internal geometry of the bilateral case.  Among all parallel
partners and connectors in the two fixed shore extensions, a lexicographic
minimum has no repeated trace and no incidental trace on both shores.  Its
open-shore sectors are induced and pairwise anticomplete, and joining the
two connectors inside their endpoint traces gives a literal odd cycle using
both shores.  There are at most three sectors in degree eight and four in
degree nine; hence one degree-eight connector is boundary-clean, and the
root-retaining choice puts `x` on the cycle.

The clean connector produced by normalization is not automatically
compatible with the independent-block response data.  If its endpoints do
admit the required partition

\[
                  S=I\mathbin{\dot\cup}T
                        \mathbin{\dot\cup}\{p,q\},
\]

and root contacts, a carrier disjoint from the connector for either `I` or
`T` forces both merged and split `{p,q}` responses on the other shore.  Thus
any aligned survivor splits both blocks across their component-incidence
graphs after the connector interior is
deleted.  For a residual component `D`, seven-connectivity yields only

\[
 h_D\ge m_D-1\quad(d(u)=8),\qquad
 h_D\ge m_D-2\quad(d(u)=9),
\]

where `m_D` is the number of missed boundary vertices and `h_D` the number
of neighbours on the deleted connector.  These are lower bounds; they do
not bound the separator or turn `D` into an actual component of `G-N[u]`.
This conditional statement is now unconditional outside one degree-eight
boundary type.  The separately audited
[nonedge-bipartition classification](../results/hc7_degree8_nonedge_bipartition_classification.md)
proves that every admissible degree-eight boundary is either
`K_1 vee C_7` or has a nonedge `pq` for which `S-{p,q}` is the disjoint
union of independent triples `I,T`, with every root-to-block contact.

The separately audited
[aligned bilateral response-cycle theorem](../results/hc7_degree8_aligned_pair_bilateral_cycle.md)
then supplies new, operation-compatible boundary-clean `p`--`q` paths in
both literal shores.  They are the two failed directions of one singleton
boundary interchange between the exact partitions

\[
       I\mid T\mid\{p,q\},\qquad I\mid T\mid\{p\}\mid\{q\},
\]

and form a literal odd cycle.  In each fixed full two-colour component,
either a `p`--`q`-separating bridge gives an aligned deletion/contraction
response retaining the opposite path, or there are two edge-disjoint
`p`--`q` routes.  Every non-wheel survivor splits both triples in both
post-path incidence graphs.

The separately audited
[two-defect component closure](../results/hc7_degree8_two_defect_component_closure.md)
strengthens this in two ways.  Every literal root connector meets every
carrier for either independent triple, making each carrier a `p`--`q`
separator.  Moreover, post-path components missing exactly two boundary
vertices have one coherent missed pair in each shore.  The strengthened
finite allocation now covers every one of the `185` compact order-eight
boundaries, including the odd wheel, and every ordered pair of arbitrary
boundary-defect sets of order at most two.  All `253,265` cases have an
explicit `K_7`-minor certificate.  Thus two two-defect components in each
shore close, and after orienting a surviving non-wheel instance one shore
has at most one such component while all its other residual components miss
at least three boundary vertices.

This is the current non-wheel laboratory.  The
[shore-filling barrier](../barriers/hc7_degree8_fourfold_incidence_bridge_interval_barrier.md)
shows that the odd cycle and four incidence splits need not leave any
off-path component, even in a `K_7`-minor-free local model.  The
[unbounded-attachment barrier](../barriers/hc7_degree8_fourfold_incidence_unbounded_attachment_barrier.md)
shows that seven-connectivity and the named bridge responses do not bound
the literal attachment language when `K_7` exclusion is omitted.  Hence a
generic shortest-cycle bridge analysis or raw finite attachment search is
insufficient.

The separately audited
[four-portal reduction](../results/hc7_degree8_four_portal_reduction.md)
now carries out the highest-leverage composition with the five-terminal
two--three linkage theorem for all four pairs `(Q,B)`.  Universal
entanglement forbids every positive packing.  The exact outputs are a fresh
order-seven response interface, a shore of order at most six, a strict
order-eight lobe, or four selected positive-excess lobes, possibly repeated.
Each selected lobe is behind at most five internal vertices, has full
boundary order from nine through thirteen and old-boundary defect at most
four, retains its shore and completed-cut terminal form, and has
full-separator edge-deletion responses incompatible with the fixed aligned
shore colouring.  Globally minimizing boundary order gives either an
exact-seven response or a boundary of order eight through thirteen with
exactly two or three full components, the universal contraction profile,
and operation-specific extension/rejection responses.

The block label can disappear in a terminal-free completion cut.  The
[portal role-erasure barrier](../barriers/hc7_degree8_portal_role_erasure_barrier.md)
has the compact boundary, bilateral operation paths, four incidence splits,
universal entanglement and no two-defect residual component, yet both portal
applications return the same lobe and no common-near-full pair.  It fails
seven-connectivity and criticality, identifying exactly what a positive
theorem must spend.  The
[independent-defect barrier](../barriers/hc7_degree8_independent_two_defect_four_bag_barrier.md)
separately shows that four bags with unrelated two-vertex misses need not
give a `K_7` minor.  One common defect per shore is therefore essential for
the present four-bag allocation unless additional host geometry couples the
defects.

The primary next theorem is **minimum-boundary response coupling**, first
for an order-eight boundary with exactly two full components.  It must give
an explicit `K_7` model, one common complete equality partition, or an
exact-seven response on a strictly smaller literal connected shore.  The
three-component order-eight case comes next; when the selected tagged lobe
itself is minimum and has defect at most two, the proved third-component
exit already supplies the required adjacent pair.  Orders nine through
thirteen follow only after these base cases.  Split-terminal `I,T` cuts
remain a conditional tagged fast route, and the strengthened four-bag
theorem closes their finite allocation once one common defect is obtained.

Computation on the bounded separator is presently a falsification and
discovery tool.  A proof-producing exhaustive search first needs a finite-
signature replacement lemma for the unbounded full components, retaining
their colouring-extension languages, rooted-minor data and operation
provenance with a certificate lift to the unchanged host.  The small-shore
and unique odd-wheel branches also remain separate.

The separately audited
[degree-eight root-star response theorem](../results/hc7_degree8_common_root_star_response.md)
retains the literal root in proper-minor colouring responses.  Its two
opposite-shore leaf sets are nonempty and form an induced star at `x`.
Three of the four proper/monochromatic deletion signatures occur.  For each
shore, an inclusion-minimal aligned deletion set is either one edge, when
the audited clean-five-path or exact-seven restart theorem applies, or has
at least two edges and forces every deleted edge monochromatic in every
aligned response.

The separately audited
[minimal root-star response reduction](../results/hc7_degree8_minimal_root_star_response_reduction.md)
then handles that multi-edge alternative without exchanging colouring
quantifiers.  Each deleted leaf has five colour-indexed paths in the same
aligned colouring.  Retaining their inherited target information gives
either a clean fan or a strict generic exact-seven shore decrease.
Discarding only the endpoint colours allows a shore-confined rerouting to
six paths with six distinct boundary ends, including the original root
edge.  Fans belonging to different leaves are not proved disjoint.

The separately audited
[five-reserve Kempe packet](../results/hc7_common_root_five_reserve_kempe_packet.md)
strengthens both tight atomic cases.  In one fixed colouring of `G-u`, all
ten reserve pairs are bichromatically coupled and every reserve nonedge has
a literal path in one named shore.  Deleting the common colour class of the
trace transversal leaves a five-chromatic graph in which the five reserve
vertices are rainbow in every five-colouring.  If their nonedge graph has
at most six edges, the Kriesell--Mohr rooted-minor theorem gives a rooted
`K_5`; if all those nonedge paths lie in one shore, the opposite full shore
and `{u}` complete an explicit `K_7` model.  Failure even to assemble the
rooted `K_5` across both shores forces at least seven reserve nonedges to be
exclusively supported in one shore.  Any maximum independent set of order
`d(u)-5` generates a rotated five-reserve packet with the same routing and
rooted-minor alternatives.

The audited static reserve-rotation barrier shows that rotation alone is
not a well-founded descent.  The separately audited
[low-degree concentrated-reserve elimination](../results/hc7_low_degree_concentrated_reserve_elimination.md)
bypasses rotation.  A fixed-colouring path joins a complementary root pair
while two further paths carry an independent reserve triple, with
disjointness forced by their five distinct colours.  A proper-minor
contraction forces the merged root response on the other shore, while
root-connector reflection forces the split response there.  Whichever
response occurs on the first shore therefore glues and six-colours `G`.

This eliminates every concentration in degrees eight and nine.  Nine
reserve nonedges are impossible; eight force
`2K_2` disjoint-union `K_1`; seven force
`P_3` disjoint-union `K_2`.  In the latter two cases the connector and
triple carrier avoid every nonexclusive demand.  Consequently the
five-reserve dichotomy always returns an `R`-rooted `K_5` in both tight
atomic cases.  That model may use both exterior components, so it need not
leave an `I`-connected seventh branch set adjacent to `{u}` and all five
rooted bags.

The explicit audited
[boundary-only fork barrier](../barriers/hc7_common_root_boundary_only_fork_barrier.md)
shows why this does not yet close the branch.  A connected order-nine
boundary satisfies the compact independence, degeneracy and minor-exclusion
conditions and supports even two crossing shore-labelled matchings, while
the four-edge augmentation remains `K_4`-minor-free.  Hence no decoder that
remembers only the contracted boundary edges can succeed.  The next
inference need only treat the bilateral or atomic three-trace degree-eight
residue, the bilateral degree-nine residue, and the exact crossed
degree-nine four-cycle.  In degree eight the remaining response obstruction
is now simultaneous allocation of the separately clean, distinctly ended
leaf-fans while retaining the operation labels.  In either tight atomic
case the remaining packet obstruction is an `R`-rooted `K_5` that consumes
both shores; concentration is no longer a live alternative.  The precise
residue is preservation of an `I`-connected seventh branch set adjacent to
`{u}` and all five rooted bags.  Its failure must expose a
response-preserving separator of order at most nine or an actual strict
component descent.
Connectivity alone is insufficient.

This branch bypasses equal component order and cross-operation provenance.
It does not close the common-trace kernel allocation, turn lower boundary
order into a well-founded descent, or prove the special common-root
completion.

## 6. Audited two-transition response reduction

The former same-transition target was too restrictive.  The audited
[last-pole normal form](../results/hc7_bounded_interface_pole_move_normal_form.md)
shows that the last move of a shortest exact-block transition is pole-free
unless it is a precise six-block-to-five-block move: one singleton merges
into a nonsingleton independent block, and in every final `B`-extension the
relevant two-colour component cannot reach another boundary vertex after
deleting `u`.

The audited
[two-transition theorem](../results/hc7_bounded_interface_two_transition_disjoint_response.md)
then removes both the shore-tag mismatch and boundary-endpoint overlap.  A
first failed lift in any exact-singleton transition gives a `C`-path with
boundary nonedge `e` as its endpoint pair.  Prescribe `e` itself as the
exact block for a second shortest transition.  Its pole-free last failed
lift has endpoints in `S-e` and interior in `B-(S union {u})`.  Consequently,
after excluding a common partition and any strict smaller-component restart,
one obtains either:

1. two vertex-disjoint opposite-shore paths with disjoint boundary nonedges
   `e,f`, where

   \[
                         K_6\not\preccurlyeq G[S]+e+f; \tag{6.1}
   \]

   or
2. the tight five-block/six-block pole residue above.

If the augmented boundary in outcome 1 had a `K_6` minor, replacing its two
added edges by the two paths and adding the singleton branch set `{u}` would
give an explicit `K_7`-minor model.  The paths may arise from different
colouring operations; no same-operation assertion is needed for this literal
geometric reduction.

The earlier endpoint-pair and robust-independent-triple theorems remain
valid, but they are no longer direct inputs to this reduction.  Their
set-system classification has been bypassed by using the first endpoint pair
as the second exact block.

## 7. Immediate terminal decoder

After the audited preprocessing, the primary open theorem has three explicit
residual inputs:

1. in the connected-exterior branch, disjoint opposite-shore paths with
   endpoint nonedges `e,f` satisfying the `K_6`-minor-free augmentation in
   Section 6, or the tight pole residue;
2. in the multi-rejected-trace branch, simultaneous component kernels and
   supported nonedges for one fixed boundary colouring; or
3. in the singleton-rejection branch, a lower-order component boundary or
   the exact two-component common-root residue from Section 5, now carrying
   the induced crossing cycle and the synchronized common-trace/disjoint-path
   flip-cube fork, with every changing coordinate contained in a coherent
   alternating cycle of full two-colour components from two fixed shore
   extensions.

For every input, prove one of the three conclusions in Section 4.  In the
recursive conclusion the returned set must be an actual component `D` of
`G-N[u]` with `|D|<|C|`.  The new theorem supplies `z_D`; the old `z` need
not belong to `N_G(D)`.  An arbitrary smaller connected piece, quotient, or
unbounded separator is still not enough.

### Component-uniform response and the new size gate

The component-uniform theorem removes the former response-label
obstruction.  Whenever a retained path meets an actual component `D` with
`|D|<|C|`, the edge `uz_D` gives a strict same-form restart ranked by the
literal order of `D`.

This is genuine monotonicity, but not yet a terminal decoder.  If `C` is
initially selected with maximum order among the components of `G-N[u]`,
then every component met by a nonrecursive opposite-shore path must have
the same order as `C`; otherwise the smaller one is already a strict
restart.  The irreducible path geometry is therefore confined to
maximum-order ties and the at most two vertices of `N(u)-S`, together with
the separate tight pole residue.  Turning that equality case into a model,
common partition, or further decreasing invariant is the next structural
step.

The audited
[independent-block pole-star barrier](../barriers/hc7_opposite_shore_shortest_transition_pole_barrier.md)
realizes every local exact-block response, every pole-star edge-deletion
response, shortest transitions, seven-connectivity and the sharp order-eight
independence bound, while forcing every shortest transition to end at the
pole.  It deliberately lacks global `K_7`-minor exclusion and full
proper-minor six-colourability.  Therefore further static language
classification, lexicographic transition minimization, or anchored pole-star
splicing cannot close the decoder by itself.  A successful proof must use
one of those two global host hypotheses while preserving the displayed path
or pole labels.

### Marked-edge coupling gate

The audited
[marked-edge response-coupling theorem](../results/hc7_marked_edge_response_coupling.md)
tests proper-minor colourings on endpoint edges of the two retained paths.
Deletion and contraction of one edge give the same response family. A common
simultaneous contraction of two anticomplete bipartite path interiors is
exactly six-chromatic and gives a full five-colour split on at least one
interior in one fixed colouring. The adjacent
[bilateral-exposure barrier](../barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier.md)
shows that the other interior need not be blocked in that colouring, even in
a seven-connected seven-chromatic host.

Deleting one endpoint edge on each path also gives a submodular weighted
separation order: separator size plus the number of marked edges crossing the
open sides. Its minimum lies between seven and `|S|`, the minimum separations
form a lattice, and every member lifts to a literal separation of `G` of the
same order with the three deletion operations assigned to the correct shore.
This does not pass the continuation gate. The minimum lift may be the original
separation, distinct deleted-edge separations can lift back to that same
separation, and a new separator need not expose an actual smaller component
of `G-N[u]`.  Component-uniform alignment repairs the response label only
after such a component is found. In the actual degree-seven branch the
opposite-shore path input is absent altogether.

Consequently no order-eight/nine or tight-pole continuation was begun from
this mechanism. A valid continuation must force an actual strict component
descent, preserve a complete boundary partition, or give a terminal model;
an unbounded path neighbourhood or a one-sided palette split is insufficient.

## Dependencies and guardrails

- [bounded low-degree entry](../results/hc7_low_degree_adjacent_pair_alignment.md)
- [component-uniform boundary alignment](../results/hc7_component_uniform_boundary_alignment.md)
- [sharp low-degree exterior-component bounds](../results/hc7_low_degree_exterior_component_bounds.md)
- [component-deletion Kempe exchange](../results/hc7_component_deletion_kempe_exchange.md)
- [full-component common-root exchange](../results/hc7_full_exterior_component_common_root_exchange.md)
- [common-root antipodal flip-cube fork](../results/hc7_common_root_flip_cube_fork.md)
- [common-root alternating full-component cycle](../results/hc7_common_root_alternating_trace_cycle.md)
- [low-degree concentrated-reserve elimination](../results/hc7_low_degree_concentrated_reserve_elimination.md)
- [split-boundary synchronization](../results/hc7_split_boundary_synchronization.md)
- [exact-block Kempe reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md)
- [last-pole normal form](../results/hc7_bounded_interface_pole_move_normal_form.md)
- [two-transition opposite-shore response](../results/hc7_bounded_interface_two_transition_disjoint_response.md)
- [two-connected boundary-core completion](../results/hc7_two_connected_boundary_completion.md)
- [independent-block pole-star barrier](../barriers/hc7_opposite_shore_shortest_transition_pole_barrier.md)
- [earlier endpoint-pair selection](../results/hc7_bounded_interface_endpoint_pair_selection.md)
- [earlier robust independent-triple response](../results/hc7_bounded_interface_robust_triple_response.md)
- [fixed-colouring degree-eight `P_5` stress test](../results/hc7_degree8_simultaneous_p5_certificate.md)
- [degree-eight dirty-path local-uncrossing barrier](../barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md)
- [degree-eight deleted-colour contact barrier](../barriers/hc7_degree8_deleted_colour_k4_contact_barrier.md)
- [four-colour parity-language barrier](../barriers/hc7_four_colour_parity_language_barrier.md)
- [eight-boundary state-transfer barrier](../barriers/hc7_eight_boundary_gallai_state_transfer_barrier.md)
- [marked-edge response coupling](../results/hc7_marked_edge_response_coupling.md)
- [simultaneous bilateral-exposure barrier](../barriers/hc7_simultaneous_bipartite_bilateral_exposure_barrier.md)
- [common-root boundary-only fork barrier](../barriers/hc7_common_root_boundary_only_fork_barrier.md)

Do not identify a colour class with a branch set without an explicit lift.
Do not treat a path as an extra branch set while simultaneously retaining
the connected shore containing it.  Any proper-minor operation must be
lifted back to the original fixed graph.
