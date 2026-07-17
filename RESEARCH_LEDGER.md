# $HC_7$ research ledger

**Last updated:** 17 July 2026
**Authoritative status:** $HC_7$ is not proved here.

This file records the current mathematical dependency chain. The concise
list of live files is [`active/INDEX.md`](active/INDEX.md), and the current
technical statement is
[`active/hc7_adjacent_pair_palette_model_frontier.md`](active/hc7_adjacent_pair_palette_model_frontier.md).
If an archived note conflicts with this ledger, this ledger governs the
current programme. The balanced order-eight, two-root, and support-six
sections retain developed dependency chains but are not by themselves the
current engine.

## Current strategic frontier: adjacent-pair colouring and rooted models

A new audited reduction supplies a uniform entry point in every hypothetical
minor-minimal counterexample.  Kawarabayashi--Pedersen--Toft's theorem for
double-critical seven-chromatic graphs implies that some edge `zu` has

\[
                         \chi(G-\{z,u\})=6.
\]

For `H=G-{z,u}`, the proved case `HC_6` and five-connectivity give a
spanning `K_6` model.  A six-colouring of the edge deletion `G-zu` has one
common pole colour whose nonempty colour class in `H` is anticomplete to
both poles, while both poles see each of the other five colours.  Choosing
one neighbour of every such colour at each pole and applying Menger's
theorem yields five simultaneous vertex-disjoint paths.  Their endpoint
colours form the two complete five-colour palettes, paired by a
permutation.  This is a uniform theorem, not a balanced-boundary case.

Relative to any spanning `K_6` model, four common pole-contact branch sets
now give an explicit `K_7` model or an actual separator.  After excluding
that separator mechanism, the three-common-branch-set profile is exact:
three common singleton pole portals, one exclusive branch set per pole,
and one branch set contacted by neither pole.  The two exclusive branch
sets contain at least two required palette colours each and are joined by
two disjoint selected paths.

A new audited theorem replaces each relevant arbitrary path by a sharper
colouring-space fork.  For every nonbuffer colour, either its pole support
is diffuse and the full neighbourhood of a two-colour component, together
with one or both poles, is an actual separator, or the support is
concentrated in one component.  In the concentrated case one Kempe
interchange rotates the common missing colour exactly, and the root-facing
side meets every other four colour classes.  In the three-common-branch-set
profile this fork is available for at least two colours joining the two
exclusive branch sets.  The theorem does not bound a returned separator
from above and does not identify colour classes with prescribed minor-model
branch sets.

An audited barrier fixes the exact scope of this improvement.  A
seven-connected `K_7`-minor-free planar-join construction realizes the
entire static three-common-singleton profile, including an exactly
six-chromatic adjacent-pair deletion, all five buffer-colour Kempe
connections, and the two disjoint exclusive-to-exclusive paths.  No
contact-increasing model change is possible.  The construction instead has
an order-seven separator and a fixed two-vertex planarizing set, and the
host itself is only six-chromatic.  Thus the next theorem must use the
nonextendability forced by `chi(G)=7`, while retaining both structural exits.

The colouring mechanism has also been extracted in a uniform,
label-preserving form.  Let `Q` be any nontrivial connected induced
bipartite subgraph of a minor-minimal `k`-chromatic graph.  After contracting
`Q`, both bipartition sides see every other colour, and every such colour
has a common two-colour component adjacent to both sides.  Concentrated
support rotates the contracted colour exactly and has contacts in every
untouched colour; diffuse or one-sided support exposes the full literal
separator of a support component.  Choosing `Q` inside one branch set of a
clique-minor model preserves that model label and all pre-existing row
adjacencies.  The theorem does not yet make the two bipartition sides
connected branch sets or align the five support components with five named
external model rows.

The exact rotation normal form prevents a false global invariant.  Once a
concentrated pole transition is normalized back to the original buffer
name, it swaps only inactive two-colour components.  Every such component
is anticomplete to the poles and lies behind a four-coloured-boundary
separator of order at least seven.  If no inactive component occurs
anywhere in the orbit, all rotations are merely global colour relabellings
and leave every coordinate of the fixed model/path score unchanged.

A second uniform theorem couples the colours different from the contracted
colour.  For every pair of them, nonextendability forces one diagonal
bichromatic component.  Components selected for the two edges of a colour
matching are automatically vertex-disjoint.  At `k=7`, together with the
common component for the fifth colour this gives three disjoint connected
subgraphs adjacent to the two bipartition sides.  If the boundary contacts
for one colour pair occupy more than one component, each such component
lies behind an actual separator.  This removes the shared-contracted-colour
overlap, but the planar-join barrier shows that set-theoretic coverage of
all five model labels still does not produce a label-preserving split.

The separator-free colouring residue now has a sharper compression.  If
all five full two-colour graphs through the missed colour are connected,
then for every other colour their union `X` is a connected dominating
induced bipartite subgraph.  The graph `Q=G-X` is five-chromatic and
`K_6`-minor-free; deleting either pole leaves a five-chromatic graph.
Martinsson--Steiner's prescribed-singleton `K_5` theorem therefore gives
two oppositely rooted near-`K_7` models.  This result is independent of the
original spanning `K_6` model.

At a fixed adjacent-pair colouring, this gives an exhaustive top-level
dichotomy.  If a full two-colour graph is disconnected, the diffuse,
one-sided, or inactive-component argument exposes an actual separator.  If
all five are connected, the connected-dominating compression applies.  The
remaining difficulty is no longer existence of five colour contacts; it is
either reducing the returned separator to a colour-compatible order-seven
interface or synchronizing two rooted models.

The primary open theorem is to turn this dichotomy into one of:

1. an explicit `K_7`-minor model;
2. an actual order-seven separation carrying a named boundary colouring
   from both sides;
3. a new valid instance of the same eligible setup with a declared
   host-level parameter strictly smaller.

The former two-vertex terminal is no longer independent.  An audited
lemma proves that, in the hypothetical counterexample, two vertices meeting
every `K_5` model force a vertex of degree seven and hence an actual
order-seven separation.  This supplies a raw exact separation, but not the
compatible shore colourings required by item 2; it enters rather than
closes the order-seven colour-gluing branch.

The first concrete milestone is now four-chromatic.  In the
connected-dominating branch put `R=Q-{z,u}` and

\[
                       S=N_R(z),\qquad T=N_R(u).
\]

The graph `R` is four-chromatic and each of `S,T` is colourful.  A `K_4`
model whose every branch set meets both sets, together with `z,u,X`, gives
an explicit `K_7` model.  In a contact-maximal `S`-rooted model, every
missed branch set lies in a component `C` disjoint from `T` whose full
neighbourhood is

\[
             N_R(C)\mathbin{\dot\cup}N_X(C)
                         \mathbin{\dot\cup}\{z\}.
\]

This is an actual separator of order at least seven.  Contraction collapses
that boundary to a few model labels and forces `u` to repeat a missed
label, but a sharp `K_6`-minor-free example proves that this repeated colour
does not itself reroute the model, even with a unique deficiency.  The
unique-deficiency case has nevertheless been compressed further.

A neighbour of `z` in the deficient component and a same-coloured
neighbour of `u` are joined by a two-colour path.  Absorbing that path into
the two nonadjacent branch sets either gives an explicit `K_7` model or
exposes the full neighbourhood of a connected residual piece of one of the
other four branch sets as an actual separator.  Thus there is no additional
finite component-compatibility case.  Varying the cut edge of the path gives
an exact interval criterion for every residual component.

The path calculation also gives a global density relaxation.  Seven
candidate sets need not be connected individually: after contracting each
of their connected components, Mader's exact `K_7` extremal bound gives a
`K_7` minor whenever

\[
 \sum_{i<j}\bigl(c(B_i\cup B_j)-1\bigr)
 \;\le\;
 \sum_i\bigl(c(B_i)-1\bigr),                         \tag{*}
\]

where `c(H)` is the number of connected components of `H`.  Pairwise
connected unions are the special quasi-`K_7` case.  The original
`K_7`-minus-one-edge model misses (*) by exactly one, so the repair problem
has a scalar **component defect**.  A successful exchange removes its
single unit.  The joined-planar barrier shows that changing the path cut
may instead move that unit from the missing pole adjacency to a different
pair of branch sets.  The live task is to use the compulsory proper-minor
colourings to make the defect vanish or show that every defect-preserving
move concentrates behind an order-seven separator.

The exact two-tree classification has a narrower scope.  It assumes the
unique-deficiency setup, a fixed admissible cut of the colour-matched path,
nonempty selected collections from all four protected branch sets, every
selected residual component adjacent to `z` and adjacent to both path-side
anchor sets at that cut, and a `K_4`-minor-free component-contact graph.  Under
those hypotheses, defect one is equivalent to the contact graph being a
two-tree.  The present chain does not prove that unique deficiency, such an
eligible four-part selection, or defect one occurs in every
connected-dominating residue.  It also does not yet supply a well-founded
host-level parameter for iterating a defect-preserving exchange.

Independently, contracting a shortest admissible path produces a canonical
list-colouring obstruction: an odd subpath has singleton endpoint lists and
paired two-element internal lists.  This statement is uniform in the
chromatic number.  It supplies saturated endpoints, but its colours are not
yet identified with named branch sets.  A seven-chromatic join family shows
that an invariant based only on the shortest locked interval can cycle while
an order-seven separator is present, so separator detection must be a direct
outcome rather than a consequence of local lock monotonicity.

The corresponding connectivity-only shortcut is formally blocked.  The
assertion that every eight-connected graph with a
`K_7`-minus-one-edge minor has a `K_7` minor would imply the open statement
that every seven-connected graph has a `K_6` minor.  Any completion theorem
used here must retain the minor-critical colouring hypotheses.

Those hypotheses now give an exact one-step dichotomy.  After any vertex
deletion, edge deletion, or edge contraction wholly inside the
five-chromatic core, the new core is four- or five-chromatic.  In the
four-chromatic branch, the intersection of the attachment sets of the two
bipartition classes of `X` is colourful and roots a `K_4` model meeting
both attachment sets.  This does not split the bipartition classes into
connected branch sets, does not align them with the pole-neighbourhoods
`S=N_R(z)` and `T=N_R(u)`, and therefore does not yet construct `K_7`.
The five-chromatic branch supplies only the exact common-hole law.  Both
branches still require a host-level exchange or colour-gluing step.

The current chain uses the following results with separate GREEN audits:

- [`hc7_global_adjacent_pair_palette_frame.md`](results/hc7_global_adjacent_pair_palette_frame.md)
- [`hc7_adjacent_pair_palette_linkage.md`](results/hc7_adjacent_pair_palette_linkage.md)
- [`hc7_adjacent_pair_bichromatic_support_dichotomy.md`](results/hc7_adjacent_pair_bichromatic_support_dichotomy.md)
- [`hc_bipartite_contraction_palette_dichotomy.md`](results/hc_bipartite_contraction_palette_dichotomy.md)
- [`hc_bipartite_contraction_bichromatic_components.md`](results/hc_bipartite_contraction_bichromatic_components.md)
- [`hc7_concentrated_rotation_normalization.md`](results/hc7_concentrated_rotation_normalization.md)
- [`hc7_star_kempe_five_core_compression.md`](results/hc7_star_kempe_five_core_compression.md)
- [`hc7_adjacent_pair_separator_or_five_core.md`](results/hc7_adjacent_pair_separator_or_five_core.md)
- [`hc7_maximal_rooted_k4_deficient_component_separator.md`](results/hc7_maximal_rooted_k4_deficient_component_separator.md)
- [`hc7_atomic_two_pole_contact_trichotomy.md`](results/hc7_atomic_two_pole_contact_trichotomy.md)
- [`hc7_colour_matched_repair_path.md`](results/hc7_colour_matched_repair_path.md)
- [`hc7_colour_matched_path_component_exchange.md`](results/hc7_colour_matched_path_component_exchange.md)
- [`hc7_colour_matched_path_exchange_or_separator.md`](results/hc7_colour_matched_path_exchange_or_separator.md)
- [`hc7_colour_matched_path_all_cut_interval_exchange.md`](results/hc7_colour_matched_path_all_cut_interval_exchange.md)
- [`hc7_component_contact_defect_theorem.md`](results/hc7_component_contact_defect_theorem.md)
- [`hc7_star_core_one_step_minor_dynamics.md`](results/hc7_star_core_one_step_minor_dynamics.md)
- [`hc_contracted_path_list_lock.md`](results/hc_contracted_path_list_lock.md)
- [`hc7_k5_transversal_order7_separator.md`](results/hc7_k5_transversal_order7_separator.md)

The canonical outer-edge result locates the balanced order-eight laboratory within this
uniform problem.  Its canonical deletion model has exact joint contact five
but is reversibly coupled to the pre-existing singleton-centred
near-complete model.  Thus model regeneration and contact maximization add
no strict rank there; the six-colouring response is the genuinely new
information.

An independent audited consequence also rules out the smallest possible
eight-connected host: every eight-connected `K_7`-minor-free graph has at
least 17 vertices.  The proof combines the exact Mader--Jorgensen extremal
case with a new elementary complement obstruction at order 16; it uses no
finite search.  See
[`hc7_eight_connected_order_bound.md`](results/hc7_eight_connected_order_bound.md).
This order bound is not an additional step in the palette-to-model
dependency chain.

The exact current formulation and trust boundary are in
[`active/hc7_adjacent_pair_palette_model_frontier.md`](active/hc7_adjacent_pair_palette_model_frontier.md),
with the immediate four-chromatic reduction in
[`active/hc7_two_colorful_sets_rooted_k4_frontier.md`](active/hc7_two_colorful_sets_rooted_k4_frontier.md).

## Developed laboratory: balanced order-eight completion

The earlier global intermediate target was the maximal-pair support-height
exchange at level six, equivalently the two-vertex transversal theorem for
compact `K_5` models.  Its most developed labelled branch is the exact
order-eight outcome of the five-leaf star in the graph of globally
support-maximal private pairs.  It remains the principal label-rich
laboratory for the adjacent-pair rooted-model theorem above.

### Current checkpoint: the matching is aligned

The balanced branch has now been reduced by three audited, unbounded
arguments rather than by another census of boundary graphs.

First, if the complement of the eight-vertex boundary has a perfect
matching, then either the host already contains an explicit `K_7`-minor
model or some perfect matching contains an edge joining the two specified
anticomplete defect edges.  The remaining three matching edges pair the
distinguished boundary vertex and the two unused defect endpoints with the
three vertices of the common clique.  The same branch-set construction
also proves that some clique vertex `r` is missed both by the distinguished
boundary vertex `x` and by the connected leaf-side interior.

Second, a Hall-type matching argument gives an exact dichotomy relative to
that prescribed nonedge `xr`.  Either the cross-pair matching can be chosen
to contain `xr`, or a different clique vertex `p` is nonadjacent only to
`x` in the boundary complement.  In host language, `p` is adjacent to
every boundary vertex except `x`, and deleting `{p,x}` leaves a labelled
six-vertex theta graph.

Third, the latter Hall alternative is now eliminated, conditional on the
standing support-at-most-six response.  The key new theorem is uniform in
`k`: across a boundary of order `k+1`, a support-at-most-`k-1`
`K_{k-2}` model which uses exactly one vertex of one open component, in a
branch set also containing a safe boundary vertex, can be anchored to an
almost-universal boundary vertex.  One Menger linkage then gives a `K_k`
minor; failure gives an actual order-`k` separation.  A separate
common-neighbour version handles a singleton open component.  This theorem
does not use the theta graph, Moser labels, or a finite list of component
contact patterns.

Consequently, in the absence of a `K_7` minor or an actual order-seven
separation, the complement has a perfect matching containing both the
prescribed edge `xr` and a cross edge between the two defect edges.  This
is the **aligned four-pair boundary partition**.  The exact remaining
local problem is to lift that host-realized partition through the two
closed shores: obtain compatible six-colourings, the already promoted
split-edge linkage, or a ranked order-seven separation.

The attempted shortcut through a labelled Mader-path delta-matroid has
also been resolved.  A written, audited counterexample shows that the
split and contracted endpoint systems need not admit a graph-realizable
symmetric exchange, and that fixed twists or static auxiliary direct sums
do not repair this.  This blocks endpoint-only algebraic enrichments, not
a representation which couples feasible sets to the actual host paths.

The endpoint geometry has also been compressed into two audited allocation
theorems.  They give an explicit seven-branch-set model whenever the
leaf-side connected subgraph and the two defect edges can jointly cover the
clique contacts it misses, and classify equality in the failed cover.  In
the unique leaf--endpoint equality case, minor-criticality gives a further
chromatic dichotomy: deleting that adjacent pair leaves either a spanning
`K_6` model, or a five-colouring with two distinctly coloured common
neighbours in the connected leaf-side interior.  This does not yet align
the regenerated model with those neighbours, so it is a secondary input to
aligned-trace lifting rather than a completion theorem.

In the canonical web branch, the five-chromatic half of that endpoint
dichotomy is now eliminated.  The unique leaf--endpoint edge becomes an
actual outer edge of the planar web skeleton.  Two common neighbours in
the leaf-side interior would give two distinct bounded facial triangles on
that one outer edge, which is impossible.  Hence, after excluding the
already permitted `K_7` and order-seven outputs, deleting the adjacent
leaf--endpoint pair is six-chromatic and regenerates a spanning `K_6`
model.  That unrooted model may be the canonical model already obtained by
discarding one deficient row of the spanning near-`K_7` frame and absorbing
it into an adjacent row.  The substantive new information is therefore the
six-chromatic proper-minor response; the remaining issue is to couple that
response to a noncanonical labelled model exchange.

An independently audited realization barrier fixes the other side of the
trust boundary.  There is a seven-connected, seven-chromatic host with the
same aligned boundary and two full shores in which **every** independent
boundary set is realized as an exact colour class by an actual proper-minor
shore contraction, yet the two closed-shore extension languages are
disjoint.  Simultaneously contracting two shore--pair sets is also
informationless: it leaves a six-vertex quotient.  The example is neither
`K_7`-minor-free nor fully contraction-critical, so it proves that one of
those global hypotheses must enter the next theorem; it does not refute the
aligned-trace target.

### New audited closure

The endpoint-rigid, no-perfect-matching arm has reached a genuine terminal
construction.  Its audited chain produces a compact `K_5` model and a
shifted order-eight separator.  Component exchanges force all residual
components to miss the same boundary vertex `y`.  The final anchoring
argument now handles both possibilities:

1. if `y` is not the universal boundary vertex `s`, anchor the five model
   branch sets on `S-{s,y}` and use the residual component together with
   `{s}`;
2. if `y=s`, anchor the five model branch sets on five distinct vertices
   of `S-{s}`, absorb one unused boundary vertex into the residual
   component, and take `{s}` as the seventh branch set.

In the second case the seven branch sets are explicitly

`M'_1,...,M'_5, C union {z}, {s}`.

The failed anchoring linkage would expose a cut of order at most six, so
seven-connectivity supplies the required paths.  All branch-set
adjacencies are written and separately audited.  Thus the terminal shifted
residue is eliminated by a `K_7` minor, modulo any order-seven-separation
exit already returned upstream.  This is an unbounded hand proof, not a
finite boundary census.

The same mechanism has been extracted as an all-parameter theorem.  In a
`k`-connected graph, a support-at-most-`k-1` `K_{k-2}` model positioned
across an order-`k` boundary can be completed by one boundary-full component
and one universal boundary vertex, under the precise one-support-vertex and
first-hit hypotheses in the theorem.  The sharper count uses the unique
model vertex in the opposite exterior component in addition to the
unanchored model rows; after anchoring, one of the `k-1` nonuniversal
boundary vertices remains unused.  The theorem gives an explicit `K_k`
model and is independently audited.  Its boundary order now matches an
actual minimum cut at parameter `k`, but no claim is made that every earlier
order-seven output has the required compact-model placement.

The balanced branch has also acquired an audited rooted structure.  The
quotient obtained after deleting the common three-clique and contracting
the two defect edges is a spanning subgraph of the canonical four-root web;
the missing linkage is the same-index crossing pairing.  The image of the
second disjoint five-clique is contained in the unique facial triangle on
the virtual outer edge together with that triangle's permitted attachment
clique; its vertices outside the triangle lie in the opposite component.
Lifting the triangle gives the exact order-eight boundary with two
boundary-full components.

The planar skeleton of this canonical web is four-connected, and adding
either outer diagonal gives a four-connected plane triangulation.  This
new structural fact is independently audited.  It does not make the
missing linkage available: the demanded terminal pairs alternate on the
outer face, while Hamilton paths in the completion may use edges absent
from the literal quotient.  Hamiltonian-connectedness is therefore a
guardrail and a structural normalization here, not the composition engine.

Two explicit branch-set constructions close infinite subfamilies of this
web obstruction.  Most importantly, deleting the two leaf vertices of the
original five-clique cannot disconnect their open shore unless a `K_7`
minor or an actual order-seven separation already exists.  The same theorem
excludes the case in which all contacts from the distinguished boundary
vertex to that shore end at the two leaves.  Consequently the remaining
leaf-side interior is one connected near-full graph, met by both leaves and
the distinguished boundary vertex, contacting both defect edges and
missing one or two boundary vertices including a vertex of the common
three-clique.  This is an unbounded hand closure; it does not eliminate the
last connected web obstruction.

### Exact open theorem

The no-perfect-matching branch is closed, and the perfect matching is now
normalized to the aligned form described above.  Equivalently, `S` has a
proper partition into four independent pairs in which one pair is the
prescribed common miss `xr` and one pair crosses the two specified defect
edges.  This boundary partition still does not by itself extend compatibly
through both shores.  State-free examples show that four-colourability,
full boundary contact, the join-minor exclusion, and even the aligned
matching are insufficient without the host's proper-minor transitions.

The target is now an **aligned-trace lifting theorem** inside the
label-preserving balanced order-eight completion.  It combines:

- the exact four-pair matching, including `xr` and the cross-defect pair;
- exact single-pair traces obtained by contracting either full shore with
  one matched nonedge;
- the original five-clique and its labelled defect edges;
- the second disjoint five-clique; and
- proper-minor six-colourings of two edges in opposite shores.

Let `g` be the edge between the two leaf vertices and let `h` be an edge of
the second five-clique internal to the opposite shore.  Boundary partitions
returned by all six-colourings of `G-g` are disjoint from those returned by
all six-colourings of `G-h`; otherwise the unmodified halves cross-glue to
a six-colouring of `G`.  This opposite-shore incompatibility is an audited
uniform separator-gluing fact.  It is useful consolidation, not a novel
deep theorem.

For the common deletion `H=G-{g,h}`, the two one-edge restorations give the
opposite signatures `(equal,proper)` and `(proper,equal)`, the signature
`(proper,proper)` is forbidden, and double contraction supplies
`(equal,equal)`.  The graph `H` also has a spanning `K_6` model.  The
immediate transition problem is therefore exhaustive:

1. some colouring of one response type is adjacent by one Kempe
   interchange to a colouring of the other type;
2. no such adjacency exists, but one Kempe component contains both types,
   so every path between them in that component passes through an
   `(equal,equal)` colouring; or
3. no Kempe component contains both types.

A direct switch forces two disjoint bichromatic components pairing the
ends of `g` with the ends of `h`, but those paths have not yet been absorbed
label-faithfully into a `K_7` model.  The second branch still needs a split
of the spanning `K_6` model, and the third needs an actual order-seven
separator or a pair of support height at least seven.  No general
Kempe-equivalence theorem presently justifies discarding the third branch.

An audited sixteen-vertex barrier shows that the second branch is genuine
under all the tempting local hypotheses: it is eight-connected, has a full
order-eight separation, realizes all three allowed signatures, contains a
literal `K_6` in the common deletion, and has a shortest response path of
length two through `(equal,equal)`.  It nevertheless has no direct switch
and no common restorable boundary response.  The example contains a `K_7`
minor and is not minor-minimal, so it identifies exactly where the true
host hypotheses still have to enter; it is not a counterexample to the
target theorem.

The simultaneous-equality branch now has a more useful global normal form.
The generalized two-edge Kempe fork works for every number of colours and
every prescribed cyclic palette: it either produces the appropriate
one-edge-restoration colouring or a fixed-end cyclic path.  Maximizing the
reachable set makes this process well founded; unless a response occurs,
the reachable set is the whole induced three-colour component, and paths
in both cyclic orders put the named edge ends in its unique source strong
component.  With two disjoint natural palettes, two response rotations
would commute to the forbidden `(proper,proper)` signature.  Consequently
one of the two named clique edges has fixed-end paths in both cyclic
orders.  All three statements are written and independently audited.

This colouring progress has been coupled to the literal separator.  For a
fixed simultaneous-equality boundary partition, the two opposite closed
shores cannot both repair their deleted edge while preserving that
partition.  A nonrepairable side contains, for every alternate colour,
either a literal endpoint path or two disjoint first-hit paths to distinct
boundary vertices.  It also contains a minimal induced fixed-boundary
list-critical core.  On the planar leaf side, the tight vertices of that
core form a Gallai forest and its exact Euler/list identity is

`sum c(v) = 6|K|-2|E(K)|+sum epsilon(v) >= 12+sum epsilon(v)`.

The equality case is now genuinely reduced, not merely enumerated: a
zero-slack four-clique core always gives an explicit `K_7`-minor model.
The two-vertex core is also closed.  A boundary-endpoint selection lemma
chooses at most one endpoint of each defect edge to repair every
three-clique vertex missed by the connected leaf-side remainder.  Together
with the opposite boundary-full shore, the two leaf singletons, and the
three clique singletons, those choices form seven explicit branch sets.
The exact remaining core forms are:

1. the leaf edge plus the unique third vertex of the bounded facial
   triangle at the opposite outer edge, with one common two-element list;
   or
2. positive Euler/list slack, in which the total boundary-colour incidence
   is at least thirteen and the tight subgraph is a Gallai forest.

The facial-triangle case now has an unbounded path normalization.  The
removable-path theorem of Du--Li--Xie--Yu gives a path from the third
triangle vertex to a first vertex of `R`, avoiding the two leaves and the
other two vertices of `R`, whose deletion leaves the host connected.  If
that path can be split so that its triangle-side subpath retains the two
other `R` adjacencies and its complement retains one connected subgraph
adjacent to all six reserved branch sets, the seven sets are an explicit
`K_7` model.  The exact unresolved condition is this labelled split, not
path existence.

This closes an infinite host family, but not the balanced order-eight
configuration.  Four audited barriers fix the new trust boundary.  A
`K_7`-minor-free canonical-web quotient can realize both opposite cyclic
paths in a strongly connected three-colour component; two disjoint
five-cliques can realize all four disjoint-palette paths in a graph of
treewidth five; and an eight-connected seven-chromatic graph can realize
the full boundary locks and a planar list-critical core while still
containing a `K_7` minor and failing minor-minimality.  Thus ordered paths,
palette disjointness, planarity, and local criticality are not separate
completion mechanisms.  The next theorem must use the canonical missing
linkage jointly with `K_7`-minor exclusion and proper-minor boundary
responses.

A [verified sixteen-vertex barrier](barriers/hc7_facial_triangle_static_completion_barrier.md)
makes this last qualification exact.  It has the balanced boundary, two
boundary-full shores, both five-cliques,
endpoint rigidity, the common-two-list facial triangle, and the canonical
missing linkage, but no `K_7` minor.  Its host connectivity is only three,
its quotient has noncanonical three-cuts, and it is six-colourable.
Therefore static triangle/web data cannot replace seven-connectivity or
the proper-minor response constraints.

The required output remains an explicit `K_7` model, a common boundary partition
which glues the two shore colourings, a pair of support height at least
seven, or an actual order-seven separation preserving the named data and
strictly decreasing a host rank.  A transition among abstract boundary
partitions or an unranked near-complete-model rotation is not progress.
The exact statement and guardrails are in
[`active/hc7_balanced_order8_frontier.md`](active/hc7_balanced_order8_frontier.md).

This target closes neither the earlier order-seven exits nor the other
private-pair kernels.  Even its success would not by itself prove the full
support-six transversal theorem or `HC_7`.

Principal new audited results:

- [`hc7_balanced_cross_matching_normalization.md`](results/hc7_balanced_cross_matching_normalization.md)
- [`hc7_balanced_aligned_matching_dichotomy.md`](results/hc7_balanced_aligned_matching_dichotomy.md)
- [`hc_almost_universal_straddling_completion.md`](results/hc_almost_universal_straddling_completion.md)
- [`hc7_balanced_endpoint_allocation.md`](results/hc7_balanced_endpoint_allocation.md)
- [`hc7_balanced_endpoint_mate_exchange.md`](results/hc7_balanced_endpoint_mate_exchange.md)
- [`hc7_unique_leaf_endpoint_chromatic_dichotomy.md`](results/hc7_unique_leaf_endpoint_chromatic_dichotomy.md)
- [`hc7_outer_edge_common_neighbour_completion.md`](results/hc7_outer_edge_common_neighbour_completion.md)

Principal new audited barrier:

- [`hc7_labelled_mader_delta_enrichment_barrier.md`](barriers/hc7_labelled_mader_delta_enrichment_barrier.md)
- [`hc7_aligned_matching_exact_trace_parity_barrier.md`](barriers/hc7_aligned_matching_exact_trace_parity_barrier.md)

Earlier audited dependencies retained by this frontier:

- [`hc7_shifted_boundary_completion.md`](results/hc7_shifted_boundary_completion.md)
- [`hc_uniform_boundary_repair_completion.md`](results/hc_uniform_boundary_repair_completion.md)
- [`hc7_star_order_eight_rooted_web.md`](results/hc7_star_order_eight_rooted_web.md)
- [`hc7_canonical_web_skeleton_four_connected.md`](results/hc7_canonical_web_skeleton_four_connected.md)
- [`hc7_star_order_eight_split_edge_completion.md`](results/hc7_star_order_eight_split_edge_completion.md)
- [`hc7_star_order_eight_disconnected_leaf_side_completion.md`](results/hc7_star_order_eight_disconnected_leaf_side_completion.md)
- [`hc_opposite_shore_minor_response_incompatibility.md`](results/hc_opposite_shore_minor_response_incompatibility.md)
- [`hc7_opposite_critical_edge_transition.md`](results/hc7_opposite_critical_edge_transition.md)
- [`hc7_common_host_double_contraction_lock_allocation.md`](results/hc7_common_host_double_contraction_lock_allocation.md)
- [`hc7_two_deleted_edge_generalized_kempe_fork.md`](results/hc7_two_deleted_edge_generalized_kempe_fork.md)
- [`hc7_reachability_maximal_kempe_normal_form.md`](results/hc7_reachability_maximal_kempe_normal_form.md)
- [`hc7_disjoint_palette_two_edge_coupling.md`](results/hc7_disjoint_palette_two_edge_coupling.md)
- [`hc7_double_equality_boundary_criticality.md`](results/hc7_double_equality_boundary_criticality.md)
- [`hc7_planar_boundary_critical_core_tight_case.md`](results/hc7_planar_boundary_critical_core_tight_case.md)
- [`hc7_two_vertex_fixed_boundary_core_completion.md`](results/hc7_two_vertex_fixed_boundary_core_completion.md)
- [`hc7_facial_triangle_removable_path_normalization.md`](results/hc7_facial_triangle_removable_path_normalization.md)
- [`hc7_theta_two_defect_exchange.md`](results/hc7_theta_two_defect_exchange.md)
- [`hc7_mixed_shore_two_component_exchange.md`](results/hc7_mixed_shore_two_component_exchange.md)
- [`hc7_boundary_anchored_model_completion.md`](results/hc7_boundary_anchored_model_completion.md)

## Previous two-root frontier (frozen)

### Clean target

The present target is the following strict subproblem of `HC_7`.

> Let `G` be seven-connected and strongly seven-contraction-critical. If
> `G` has a spanning `K_7`-minus-one-edge minor model whose two deficient
> branch sets are nonadjacent singleton vertices, then `G` contains a
> `K_7` minor or has an actual separation of order seven.

Write the two singleton roots as `a,b`, put `J=G-{a,b}`, and write the other
five branch sets as `B_1,...,B_5`. Then `chi(J)=6`. Every six-colouring of
`J` makes at least one root adjacent to every colour class, and both
exclusive root orientations occur. A direct orientation-changing Kempe
interchange already yields an actual order-seven separation at the sharp
boundary size. The stronger claims that all witnesses lie in one Kempe
class or that two transitions produce an uncovered colouring are false.

### New uniform rooted-model input

The ordered-clique form of the Dominating 4-Colour Theorem yields the
following written result in this repository.

> If `H` has chromatic number at least `r+4` and `X` is a nonempty connected
> induced `r`-colourable subgraph, then `H` has a normalized dominating
> `K_5` model `(T_1,T_2,T_3,{v},{w})` such that either `X subseteq T_1`, or
> the model avoids `X` and `T_2 union T_3 union {v,w}` separates `X` from
> `T_1`. Here `T_3 union {v,w}` induces a cycle. A marked version avoids
> `X` together with any prescribed neighbour, and a two-subgraph version
> aligns a pointwise adjacent pair with the first two ordered branch sets.

For the clean target, take `H=J` and let `X` be the internal path of a
shortest `a`--`b` route through one named branch set `B_i`. The result gives
either a named first-branch alignment or a separator

`S=T_2 union C`,

where `C` is an induced cycle, `T_1` dominates every vertex of `S`, and
`T_2` dominates every vertex of `C`. Let `E` be the `T_1`-side component of
`J-S` and let `R_E` be the roots adjacent to `E`. Then `S union R_E`
separates `G`, so `|S|+|R_E|>=7`; equality is an actual order-seven
separation. This weighted boundary order is sharper than `|S|` alone.

This is a genuine uniform rooted-model principle rather than a finite
boundary classification. It does not finish the clean target: the aligned
model remains unaligned with the other four old branch sets, while the
structured separator can have unbounded order.

### New general complete-factor theorem

For every `r>=0`, the following is proved and separately audited:

> If `K_r join F` is `(r+5)`-connected, then it contains a `K_{r+5}` minor
> or has an actual separation of order `r+5`. Every `K_{r+5}`-minor-free
> graph of this join form is `(r+4)`-colourable.

This eliminates the coherent complete-factor join family for all relevant
Hadwiger parameters and explains the sharp `K_2`-plus-planar order-seven
obstruction. It is independent progress, but it does not cover arbitrary
near-complete minor models.

### Immediate open theorem

Choose an absorption-or-separator outcome minimizing the lexicographic
signature consisting of the weighted boundary order, the order of the
`T_1`-side component, and the order of the component containing the
prescribed path. The next theorem must show that strong
contraction-criticality and the old five-bag model give one of:

1. an explicit `K_7`-minor model;
2. weighted boundary order seven, hence an actual order-seven separation;
   or
3. another normalized outcome with a strict decrease of the displayed
   pair.

The aligned-path branch requires the corresponding label-preserving
exchange with `B_1,...,B_5`. Connectivity alone, minimum model size, Kempe
class connectivity, branch-set rotations, and abstract boundary colouring
languages have all been shown insufficient. The required new mechanism is
high-connectivity compression of the ordered separator together with a
proper-minor transition; further Moser or attachment-pattern enumeration is
frozen.

Principal current files:

- [`hc7_two_root_colouring_space_frontier.md`](active/hc7_two_root_colouring_space_frontier.md)
- [`hc7_chromatic_subgraph_capture_or_avoid.md`](results/hc7_chromatic_subgraph_capture_or_avoid.md)
- [`hc7_join_near_clique_dichotomy.md`](results/hc7_join_near_clique_dichotomy.md)
- [`hc7_two_root_kempe_class_icosahedron_barrier.md`](barriers/hc7_two_root_kempe_class_icosahedron_barrier.md)
- [`hc7_two_root_kempe_causal_support.md`](barriers/hc7_two_root_kempe_causal_support.md)
- [`hc7_normalized_separator_icosahedron_barrier.md`](barriers/hc7_normalized_separator_icosahedron_barrier.md)

## 1. Frozen support-six counterexample framework

Suppose that $G$ is a minor-minimal counterexample to $HC_7$.  The programme
uses the following standard consequences:

- $\chi(G)=7$ and $G$ has no $K_7$ minor;
- every proper minor of $G$ is six-colourable; and
- $G$ is seven-connected.

A minor model's **support** is the union of its branch sets.  A
**six-vertex $K_5$ model** is necessarily a $K_5$-minor model with four
singleton branch sets and one two-vertex branch set; the latter is called
the model's two-vertex branch set below.

Let

$$
 \mathcal F_6(G)=\{V(M):M\text{ is a }K_5\text{-minor model using at most
 six vertices}\}.
$$

The first intermediate theorem sought is

$$
                         \tau(\mathcal F_6(G))\le2.       \tag{1}
$$

Even (1) is only the first extension step.  The final argument must produce
two vertices meeting the support of every $K_5$-minor model in $G$.  Deleting
such a pair leaves a $K_5$-minor-free graph; the known $t=5$ case then gives
a four-colouring, and two additional colours finish $G$.

## 2. Established dependency chain of the frozen programme

The following statements have written proofs in the repository.  Many have
separate internal audit notes; those audits are not external peer review.
Items explicitly marked **computer-assisted** depend on a finite exhaustive
classification or computation as well as a written reduction.

1. **Bounded critical family (computer-assisted at the sharp bound).**  If
   (1) fails, there is an inclusion-minimal
   subfamily of at most twenty-seven supports with transversal number three.
   Each member has a private two-vertex transversal for the other members.
   The bound twenty-seven uses the verified nine-vertex support
   classification; the hand Bollobás set-pairs argument gives twenty-eight.

2. **Three-model extraction.**  Three supports can be selected with pairwise
   intersection at most three when both have order five, and at most four
   otherwise.  If all three are five-vertex $K_5$ subgraphs, existing
   clique-minor results give a $K_7$ minor.  Here
   $\tau(\mathcal F_6(G))>2$ first implies that $G$ is not two-apex,
   because an apex pair would meet every $K_5$-minor support; Theorem 1.10
   of Niu--Zhang then applies.  Thus every unresolved selection contains a
   six-vertex $K_5$ model.

3. **Label-preserving additional models.**  For each private pair
   $\{p,q\}$, the criticality argument produces one prescribed $K_5$
   model containing $p$ and another containing $q$.  The corrected
   dichotomy either separates three labelled models sufficiently, or
   produces two models sharing a prescribed vertex set $X$, together with
   specified replacement models.  Several maximal-intersection
   configurations are eliminated by explicit $K_7$-minor constructions.

4. **Rooted-minor compression.**  Prescribed terminals in a three-connected
   graph can be retained while contracting to a bounded three-connected
   rooted minor.  The five-terminal case has a hand classification; the
   six-, seven-, and eight-terminal interfaces used here have finite
   classifications and retained verification code.

5. **Eliminated shared-set configurations (partly computer-assisted).**
   In the shared-set outcome of item 3, $A\cap X$ must be empty if
   $|A|=5$; this is a restriction, not an elimination of the disjoint case.
   If $|A|=6$ and the two additional models have five vertices, every
   positive value of $|A\cap X|$ is eliminated. If all three models have
   six vertices, the cases $2\le |A\cap X|\le5$ are eliminated.
   The finite compositions have retained scripts and separate internal
   audits or replays.  This does not close the separated-labelled-triple
   outcome. The shared-set residue consists of every case with
   $A\cap X=\varnothing$, together with the all-six-vertex case
   $|A\cap X|=1$.

6. **Weighted separation function.** For three disjoint six-vertex $K_5$
   models, let $e_i=x_i y_i$ be the edge spanning the two-vertex branch set
   of model $i$, put $F=\{e_1,e_2,e_3\}$, and let $K=G-F$. The function

   $$
      \lambda_F(A,B)=|A\cap B|+
      |\{e\in F:e\text{ has endpoints in opposite open sides of }(A,B)\}|
   $$

   is submodular.  Seven-connectivity of $G$ implies
   $\lambda_F(A,B)\ge7$ for every separation of $K$ with both open sides
   nonempty.  For exact weighted order seven, after fixing two roots and the
   side assignment of every prescribed model, the cardinality of the
   anchored open side is a well-founded rank under uncrossing.

7. **Connectivity-four case.**  If $K$ has a separation of order four, the
   endpoint choices of the crossing matching edges lift to a separation of
   $G$ of order seven that preserves the prescribed models.  The anchored
   open-side cardinality above closes the connectivity-four case by a strict
   reduction.

8. **Common-deletion colouring patterns.**  If the connectivity-four
   reduction is unavailable, $K$ is at least five-connected and has
   chromatic number five or six. Every nonempty subset of $F$ occurs as
   exactly the set of matching edges whose endpoints receive the same colour
   in a six-colouring of $K$; no colouring makes all three edges bichromatic.

9. **Construction of each prescribed rooted model in the common graph.**
   Let $Q_i$ be the four singleton vertices of model $i$. For each $i$,
   $Q_i$ induces a prescribed $K_4$, and $K-Q_i$ contains an
   $x_i$--$y_i$ path. The singleton branch sets indexed by $Q_i$, together
   with this path, form a $K_5$-minor model in $K$, but the three paths may
   intersect.

10. **Kempe-component alternative.**  For any specified equality pattern
    and any monochromatic matching edge $e_i$, the colour missing from its
    prescribed $K_4$ yields either the required path or a two-colour component
    whose Kempe exchange produces another legal equality pattern arising
    from a proper minor.  The first move from the all-monochromatic pattern
    decreases the number of monochromatic matching edges, but later moves
    can branch or cycle.

11. **Three-edge contraction case.**  Contracting all three matching edges
    gives three disjoint $K_5$ subgraphs with specified contracted vertices.
    A Mader-type disjoint-path argument, followed by labelled separator
    constructions, excludes the entire case in which all three edges form an
    inclusion-minimal set whose simultaneous contraction destroys
    seven-connectivity.  This is an infinite-family result, not merely a
    finite enumeration.

12. **Global maximal-pair/private-pair bridge.** Under the contradictory
    assumption $\tau(\mathcal F_6(G))>2$, there is an inclusion-minimal family of at
    most twenty-seven exact six-vertex supports over the full family of
    literal $K_5$ subgraphs. Every support $A_i$ in this family has a
    private pair $P_i$ which meets every literal $K_5$, avoids $A_i$, and
    satisfies

    $$
          \mu_G(P_i)=6=\max_{|P|=2}\mu_G(P).
    $$

    Thus the global support-height normalization and labelled private-pair
    extraction can be imposed simultaneously. Equivalently,
    $\tau(\mathcal F_6(G))>2$ if and only if the maximum support height is six.
    Producing a pair of height at least seven is already the intermediate
    transversal theorem, not a smaller monotone step.

13. **Common representation for terminal-edge contractions.** If an edge
    joins two terminals in one part of a Mader network, contracting it is
    represented by replacing the two terminal columns of a skew matrix by
    one generic linear combination. Pairwise disjoint contractions admit
    one master representation whose legal principal restrictions give all
    predecessor endpoint delta-matroids. Ordinary symmetric exchange need
    not stay in those legal restrictions. More decisively, the endpoint
    system is invariant under every change to terminal--terminal edges
    within one part, so it cannot record the designated $K_4$, split edge,
    same-model paths, or deletion-colouring data.

14. **Canonical order-eight matching obstruction.** For an eight-vertex
    boundary $J$, put $F=\overline J$. If $I_2\vee J$ has no $K_7$ minor and
    $F$ has no perfect matching, the Gallai--Edmonds set $A(F)$ has order at
    most two and $F[D]$ has at most four factor-critical components. The
    possible pairs $(|A|,o(F-A))$ are $(0,2),(0,4),(1,3),(2,4)$. This
    canonicalizes the earlier Tutte witness but does not align the two
    shore colouring languages. An exact state-realization barrier shows
    that the canonical decomposition, two named edge transitions,
    independent-block responses, seven-connectivity, and the target-free
    quotient remain insufficient without global minor exclusion or further
    labelled branch-set data.

15. **Exact six-linkage alignment and a bridge/web dichotomy.** In the
    zero-intersection branch with a six-vertex $K_5$ model and a disjoint
    $K_6^-$, contract six disjoint linking paths to a perfect matching.
    A complete finite classification proves that the resulting
    twelve-vertex quotient has a $K_7$ minor unless the missing edge of
    the $K_6^-$ is matched to a missing singleton--split-end edge of the
    six-vertex model. Thus every surviving matching aligns two labelled
    nonedges; arbitrary endpoint permutations are no longer a residue.

    For the canonical $3+1$ contact form, a clean path from the remaining
    split-end linkage path to any of three specified linkage paths gives
    seven explicit branch sets. Seven-connectivity therefore forces either
    a $K_7$ minor or a separator relation through the two exceptional
    linkage paths after deleting six named vertices. A one-vertex minimum
    separator in that relation lifts to an actual order-seven separation.
    Two crossed bridges on either exceptional cycle transpose the aligned
    endpoints and again give an explicit $K_7$ model. Finally, the
    Generalised Two Paths Theorem gives a precise structural residue: in a
    $K_7$-minor-free host, two cleaned graphs have four-web completions with
    frames sharing the remaining linkage path.

    The two completion edge sets are not host edges and need not agree.
    Their compatibility or exclusion is the live unbounded problem on this
    branch. A separate exact quotient calculation also shows why attachment
    count alone cannot replace it: one connected contracted bridge with
    seven or eight quotient neighbours can remain nonrepairing in two
    labelled eight-vertex frames. This quotient statement does not lift
    through nontrivial linkage paths without preserving distinct first-hit
    vertices.

    Minor-criticality supplies two further constraints on this branch. If
    the private pair is nonadjacent, its deletion is exactly six-chromatic;
    each endpoint is colour-dominating in a separately attained
    six-colouring; a dominating $K_5$ model can be regenerated while
    avoiding any prescribed remaining vertex; and the deletion contains an
    unlabelled $K_6$ minor. Conversely, seven-connectivity and the disjoint
    $K_6^-$ and $K_5$ supports exclude any fixed pair whose deletion is
    $K_5$-minor-free. Neither statement preserves the linkage labels, so
    both are constraints on the two-web composition problem rather than a
    solution of it.

16. **One six-terminal test replaces the first two-web compatibility
    problem.**  In the canonical `3+1` form, apply the Generalised Two
    Paths Theorem to the ordered tuple

    $$
                         (a_3,y,x,q,r,p).
    $$

    Of the fifteen possible crossing types, twelve give explicit
    `K_7`-minor models.  The exact three survivors are

    $$
              (a_3x,yq),\qquad(a_3x,yr),\qquad(a_3x,yp).
    $$

    All three endpoint quotients, and the graphs obtained by subdividing
    both crossing edges once, are `K_7`-minor-free; thus these are genuine
    repaired-contact residues rather than omissions in the decoder.  If
    the six-terminal tuple is crossless, it has one same-vertex web
    completion.  The completion edges remain auxiliary, but the earlier
    pair of unrelated four-web completions is no longer the active
    obstruction.

    An endpoint-preserving stable rerouting of the six linkage paths makes
    every nontrivial bridge attach to at least two paths.  Every exterior
    bridge component then has at least seven skeleton attachments; exactly
    seven give an actual order-seven separation.  In a `K_7`-minor-free
    host no such component can attach both to the `y`--`r` path away from
    `y` and to one of the first three linkage paths away from its right
    endpoint.

    The distinct `2+2` contact form has also been advanced without
    identifying it with `3+1`: three clean augmenting-path classes and
    both crossed-linkage classes give explicit `K_7` models, the latter
    using a rooted-`K_4` cycle-linkage theorem.  Its remaining residue is
    two four-terminal web certificates sharing one linkage path.  A path
    between the two unmatched linkage paths, internally disjoint from all
    six named paths, is now another explicit unbounded `K_7` construction.
    A verified counterexample shows that the three resulting clean-path
    patterns do not extract from every terminal crossing, so a
    label-faithful six-terminal lift retaining the full bridge structure is
    still open.

17. **A fixed support-exchange core.**  Delete one support `A` from a
    minimal exact-six critical family and let `H` be the remaining family
    together with all literal `K_5` subgraphs.  Then `tau(H)=2`.  If
    `T(H)` is the family of all two-vertex transversals of `H`, define

    $$
       Z_H=V(G)-\bigcup_{R\in T(H)}R.
    $$

    The support `A` lies in `Z_H`, and `G[Z_H]` contains no literal
    `K_5`.  Every exact six-vertex `K_5`-model support contained in `Z_H`
    may replace `A` while preserving **every** pair in `T(H)` as a private
    transversal.  Conversely, every vertex outside `Z_H` already belongs
    to a globally support-maximal private pair.  This is the first fixed
    global invariant for repeated one-vertex support replacements: private
    pairs can no longer drift arbitrarily.  It does not yet make the
    replacement graph acyclic or preserve a chosen six-linkage.

18. **Minor-critical repair and the exceptional intersection.**  A
    one-internal-vertex `a_3`--`x` repair replaces one vertex of the
    six-vertex support and admits two labelled `K_5` decompositions.
    Colourings after deleting its two edges force a second `a_3`--`x`
    path which avoids both edges and all other vertices of the original
    support.  This is a genuine palette-to-labelled-interface statement,
    although the new path may meet the linkage skeleton.

    If this simultaneous bypass meets the residual `y`--`p` or
    `y`--`q` path in one exterior component, an explicit `K_7` model
    results.  In the exceptional `y`--`r` case, all additional normalized
    endpoint contacts and all interior linkage-path contacts except those
    on the `y`--`r` path are likewise closed by explicit models.  The
    remaining component produces the actual order-seven boundary

    $$
                 X_7=\{a_3,x,y,r,b_0,b_1,b_2\}.
    $$

    Since `X_7` contains the clique
    `\{r,b_0,b_1,b_2\}`, the exact-seven packing theorem forces both open
    shores to have full-subgraph packing number exactly one.  Thus the
    unbounded attachment-order residue on the `y`--`r` path has been
    replaced by a normalized `(1,1)` exact-seven separation.  The still
    open cases are a bypass which meets the linkage skeleton before the
    residual path, a bypass disjoint from that path, or a sequence of
    support replacements inside `Z_H` with no strict rank.

    A sharp static barrier confirms that two web certificates and one
    bridge in each exceptional class do not suffice without high
    connectivity.  The examples have connectivity three.  Conversely, an
    exhaustive direct-link quotient search finds no `K_7`-free completion
    of minimum degree seven, supporting the use of seven-connectivity as
    the missing host-level input rather than further endpoint casework.

19. **Canonical private-transversal structure and endpoint saturation.**
    Hold the deleted-family hypergraph `H` of item 17 fixed, and make a
    graph whose edges are all two-vertex transversals of `H`.  Exactly one
    of the following holds:

    - it has two disjoint edges, which are two disjoint globally
      support-maximal private pairs for every exact six-vertex support in
      the fixed exchange core;
    - all edges have one common endpoint and every vertex outside the core
      lies in a fixed set of order at most seven; or
    - the graph is a triangle and the outside set has order three.

    In either bounded-locus case, deleting that locus leaves the residual
    connectivity forced by seven-connectivity.  If the locus has order
    seven and disconnects the graph, it is an actual order-seven boundary
    and every component on the other side is adjacent to all seven boundary
    vertices.

    There is a complementary global version.  Choose one private pair for
    every member of the minimal exact-six critical family.  These pairs
    are distinct.  Either two are disjoint, or the whole critical family
    has at most six members in an explicit star pattern, or it has exactly
    three members in an explicit triangle pattern.  In the star case,
    every two leaves force a literal `K_5` subgraph through the common
    centre and avoiding those leaves.  Thus the previous bound of
    twenty-seven supports is needed only in the branch that already
    supplies two disjoint maximal private pairs.

    On the labelled `3+1` linkage, a **computer-assisted finite interface**
    verifies all 252 required endpoint quotients. This supports an
    unbounded contraction argument: every connected off-linkage subgraph
    adjacent to `a_3,x` and five further normalized endpoints yields a
    `K_7` minor. The same conclusion holds when the five further contacts
    occur in five distinct linkage paths. The
    sharp six-endpoint and once-subdivided catalogues show that every
    negative pattern concentrates its contacts on very few paths.  Hence
    arbitrary support-pair drift and broadly distributed attachment are no
    longer live obstructions.  What remains is the label-preserving
    composition from two disjoint maximal pairs, or the ordered geometry of
    contacts concentrated on at most four linkage paths.

    That geometry now has a uniform two-sector form. An exterior component
    adjacent to the repaired-contact ends `a_3,x` cannot meet the interiors
    of the `a_3`--`p` or `x`--`q` linkage paths. Its other contacts lie
    either on the `y`--`r` path together with five named endpoints, or on
    the first three linkage paths together with `a_3,x,y`. With at least
    eight linkage neighbours, a nontrivial first--last interval exists on
    one named path.

    A uniform block--cutvertex lemma now controls one part of that ordered
    residue. For any fixed six-path linkage in a seven-connected graph,
    every leaf-block interior of an off-linkage component has at least six
    neighbours on the linkage; equality gives an actual order-seven
    separation preserving all six named paths. A cutvertex-free component
    has at least seven linkage neighbours, with the same separation at
    equality. The strict-inequality branch still needs the endpoint labels
    or minor-critical colouring data.

    An independently checked infinite two-fan construction fixes the trust
    boundary of this conclusion. Two distinct repaired-contact components
    may each have arbitrarily many first hits, and may each meet several
    linkage paths, while the extracted graph remains `K_7`-minor-free.
    These examples are triangle clique-sums and are not seven-connected or
    contraction-critical. Thus attachment count, first/last hit selection,
    and stable-bridge incidence cannot supply the strict rank alone; the
    next theorem must use the extra edges or colouring transitions forced
    by the full counterexample hypotheses, or return the corresponding
    order-seven separation via the promoted transversal lemma.

    Restoring the local minimum-degree and Dirac neighbourhood bounds does
    not by itself break that barrier. In the literal atomic fan, all
    degree-seven negative completions violate Dirac, and degree at least
    nine forces a `K_7` minor, but two exact degree-eight neighbourhoods
    remain. Every Rolek--Song equality-case disjoint-path demand for those
    neighbourhoods is already realizable inside the old quotient. Thus the
    missing step is genuinely global seven-connectivity or a stronger
    proper-minor colouring transition, not another local equality-path
    invocation.

20. **The two largest star kernels have explicit graph structure.**  In
    the star alternative of item 19, write the private pairs as
    `\{p,\ell_i\}`.  If there are six leaves, every literal `K_5` contains
    `p`; compatible clique witnesses after contracting a two-vertex branch
    set feed the promoted one-split/two-clique composition theorem.

    If there are five leaves and a literal `K_5` avoids `p`, it is exactly
    the leaf clique `L`.  Each critical six-vertex support is then

    $$
       (L-\{\ell_i\})\cup e_i,
    $$

    where `e_i` is an edge outside `L`, is collectively adjacent to
    `L-\{\ell_i\}`, and is anticomplete to `\ell_i`.  The five edges are
    distinct and contain two vertex-disjoint edges.  The graph also contains
    a second literal `K_5` disjoint from `L`, and `G-L` is three-connected.
    Two disjoint connected subgraphs that contain a disjoint pair
    `e_i,e_j` and respectively meet `N(\ell_i),N(\ell_j)` would give an
    explicit `K_7` model.  A wheel construction shows that
    three-connectivity alone does not force this paired linkage.

    This five-member subcase now has a stronger rooted-minor reduction.
    Contracting a disjoint pair makes any rooted `K_4` lift to an explicit
    `K_7` model.  The rooted-`K_4` theorem otherwise gives a small cut or a
    four-connected planar cofacial quotient.  Coordinating all five
    distinguished edges and the second disjoint `K_5` eliminates the planar
    outcome simultaneously.  Therefore this branch returns either an actual
    order-seven separation, or an eight-vertex boundary `S` for which `G-S`
    has exactly two components, each adjacent to every vertex of `S`, while
    `G[S]` is four-colourable and the two distinguished edge branch sets are
    anticomplete.  The precise remaining step is to orient the order-seven
    separation with a strict model-preserving rank or synchronize the two
    shore colourings across this exact order-eight boundary.  The cases in
    which every literal `K_5` contains `p`, and the smaller star and triangle
    kernels, remain open.

The most recent end-to-end composition theorem in item 11 is
[`hc7_three_split_marked_mader_branch_closure.md`](results/hc7_three_split_marked_mader_branch_closure.md),
with its adjacent audit.  The weighted separation and Kempe-component inputs
are recorded in
[`hc7_matching_deletion_separator_lift.md`](results/hc7_matching_deletion_separator_lift.md),
[`hc7_missing_colour_matching_transition.md`](results/hc7_missing_colour_matching_transition.md),
and [`hc7_kempe_component_odd_cycle.md`](results/hc7_kempe_component_odd_cycle.md).
The direct source for the common-deletion chromatic statement and all seven
nonempty matching-edge equality patterns is Sections 7--8 of
[`hc7_three_split_cross_star_ranked_exchange.md`](active/hc7_three_split_cross_star_ranked_exchange.md),
with its [separate internal audit](active/hc7_three_split_cross_star_ranked_exchange_audit.md).
The new global normalization is
[`hc7_maximal_support_pair_private_pair_bridge.md`](results/hc7_maximal_support_pair_private_pair_bridge.md).
The algebraic projection and canonical boundary obstruction are respectively
[`hc7_mader_terminal_contraction_projection.md`](results/hc7_mader_terminal_contraction_projection.md)
and
[`hc7_eight_boundary_gallai_edmonds.md`](results/hc7_eight_boundary_gallai_edmonds.md),
each with an adjacent audit.
The exact linkage classification and the constructive bridge/web theorem
are
[`hc7_disjoint_k6minus_support6_linkage_classifier.md`](results/hc7_disjoint_k6minus_support6_linkage_classifier.md)
and
[`hc7_disjoint_k6minus_support6_bridge_augmentation.md`](results/hc7_disjoint_k6minus_support6_bridge_augmentation.md),
again with adjacent audits.
The six-terminal compression, fixed support-exchange core, repaired-contact
colouring theorem, exceptional-intersection theorem, and the independent
`2+2` bridge theorem are respectively
[`hc7_disjoint_k6minus_six_terminal_crossing_decoder.md`](results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.md),
[`hc7_one_vertex_support_exchange.md`](results/hc7_one_vertex_support_exchange.md),
[`hc7_repaired_contact_exchange.md`](results/hc7_repaired_contact_exchange.md),
[`hc7_repaired_contact_intersection.md`](results/hc7_repaired_contact_intersection.md),
and
[`hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md`](results/hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md).
The additional clean connector in the `2+2` form is
[`hc7_disjoint_k6minus_support6_two_two_connector.md`](results/hc7_disjoint_k6minus_support6_two_two_connector.md),
with its adjacent audit; its exact extraction barrier is
[`hc7_two_two_three_pattern_extraction_barrier.md`](barriers/hc7_two_two_three_pattern_extraction_barrier.md).
The new transversal-graph compression and endpoint-saturation theorem are
[`hc7_exchange_core_transversal_graph.md`](results/hc7_exchange_core_transversal_graph.md),
[`hc7_private_transversal_graph_kernel.md`](results/hc7_private_transversal_graph_kernel.md),
and
[`hc7_disjoint_k6minus_seven_attachment_decoder.md`](results/hc7_disjoint_k6minus_seven_attachment_decoder.md),
each with its adjacent audit.
The exact two-sector theorem is
[`hc7_repaired_component_attachment_concentration.md`](results/hc7_repaired_component_attachment_concentration.md),
with its adjacent audit.
The linkage leaf-block separation is
[`hc7_linkage_bridge_leaf_block_separation.md`](results/hc7_linkage_bridge_leaf_block_separation.md),
again with its adjacent audit.
The explicit five- and six-support star-kernel structure is
[`hc7_star_private_transversal_large_kernel.md`](results/hc7_star_private_transversal_large_kernel.md),
with its adjacent audit.  Its rooted-four separator reduction is
[`hc7_star_kernel_rooted_four_contraction.md`](results/hc7_star_kernel_rooted_four_contraction.md),
again with an adjacent audit.  The exact three-connectivity limitation is
[`hc7_five_defect_edges_three_connected_linkage_barrier.md`](barriers/hc7_five_defect_edges_three_connected_linkage_barrier.md).
The necessity of coordinating all five edges, rather than one planar
quotient, is recorded in
[`hc7_star_kernel_contracted_root_planar_barrier.md`](barriers/hc7_star_kernel_contracted_root_planar_barrier.md);
the smaller connectivity-only failure is
[`hc7_four_connected_edge_rooted_pair_barrier.md`](barriers/hc7_four_connected_edge_rooted_pair_barrier.md).
The exact local limitation of the Dirac and Rolek--Song inputs is
[`hc7_atomic_fan_dirac_rolek_barrier.md`](barriers/hc7_atomic_fan_dirac_rolek_barrier.md),
with its adjacent audit.
The two secondary criticality constraints are
[`hc7_nonadjacent_pair_colouring_regeneration.md`](results/hc7_nonadjacent_pair_colouring_regeneration.md)
and
[`hc7_disjoint_k6minus_k5model_two_apex_exclusion.md`](results/hc7_disjoint_k6minus_k5model_two_apex_exclusion.md).

## 3. Exact open problems

### 3.1 Label-preserving extraction of compatible $K_5$ models

Starting with the bounded exact-six family and its globally maximal private
pairs from item 12, prove one of the following:

- an explicit $K_7$-minor model in $G$;
- two vertices meeting every member of $\mathcal F_6(G)$;
- three vertex-disjoint six-vertex $K_5$ models with their prescribed
  branch-set labels; or
- a separation of $G$ of order seven preserving all specified rooted models
  and colouring data, together with a strictly decreasing induction
  parameter.

In this normalization the avoided support $A$ always has order six. The
unresolved cases are a genuinely separated labelled triple and the
following shared-set configurations: $A\cap X=\varnothing$ (with the two
additional models both of order five or both of order six), and the case in
which all three models have six vertices and $|A\cap X|=1$. A complete
eight-terminal rooted-minor classification does not by itself resolve the
latter: one finite boundary pattern defeats every choice of four vertices
held outside the rooted reduction.  A successful proof must therefore use
several compatible models constructed after different contractions, or
retain additional information from the contraction sequence.

For one-vertex replacements there is now a canonical region `Z_H` in
which all replacements preserve the same complete family of private
transversal pairs.  The graph of those pairs sharpens the exit alternative:
either it supplies two disjoint globally maximal private pairs, or every
outside vertex lies in one fixed set of order at most seven.  In the latter
case seven-connectivity either gives the corresponding residual
connectivity or makes that set an actual full order-seven boundary.  Across
the whole critical family, failure to obtain two disjoint pairs reduces the
family from at most twenty-seven supports to at most six in an explicit
star or triangle pattern.  The two live constructive branches are therefore
label-preserving composition at two disjoint pairs and rooted linkage around
the fixed bounded locus.  Another support-only extraction is not enough.

For the five- and six-member star kernels, the bounded-locus branch is no
longer purely set-theoretic.  In the five-member case with a literal clique
avoiding the centre, the former paired-linkage obstruction now has a complete
rooted-four reduction.  The simultaneous five-edge argument rules out every
four-connected planar quotient and leaves only an actual order-seven
separation or a two-shore order-eight boundary with the exact properties in
item 20.  The remaining obligation is state-preserving separator
composition, not another local linkage classification.  In the six-member
case, the remaining task is to choose two row-compatible literal cliques for
the existing one-split composition theorem.

### 3.2 Simultaneous composition in the common edge-deletion graph

Let $K=G-\{e_1,e_2,e_3\}$ be as in item 6 and assume $K$ is five-connected.
Each prescribed $K_4$ can be extended individually by a path joining the
endpoints of its deleted edge, but the three paths may intersect.  The
remaining theorem must combine these paths and the Kempe-component
alternatives into one of:

- an explicit $K_7$-minor model;
- an actual order-seven separation, including one obtained from a global
  two-vertex transversal for all $K_5$ models; or
- a model-preserving order-seven separation with a strict induction
  parameter.

A complementary contraction analysis yields the following.  After the
three-edge contraction case has been excluded, it gives either an unranked
order-seven
separation or an inclusion-minimal two-edge set whose simultaneous
contraction is not seven-connected.  In the order-two case, expansion gives
a boundary of order eight; both open sides
contain a connected subgraph adjacent to every boundary vertex, and the
boundary graph is four-colourable.  The last fact is computer-assisted, with
retained verification code and an independent replay. Four-colourability
alone does not align the two boundary colourings. The canonical
Gallai--Edmonds decomposition removes arbitrary Tutte-witness choice but
still does not transfer a colouring state. Likewise, the common Mader
delta-matroid representation preserves endpoint feasibility across the two
contractions but is blind to the same-model branch adjacencies and paths
needed for composition.

An explicit quotient also shows that six arbitrary vertex-disjoint paths
between a disjoint six-vertex $K_5$ model and a $K_6^-$ need not yield a
$K_7$ minor: the quotient has a width-five tree decomposition. A positive
continuation must retain the bridges of an extremally chosen linkage and
prove an augmenting rerouting or an order-at-most-six separator; replacing
the linkage by its endpoint matching loses essential information.

The new alignment theorem identifies exactly what that retained information
must repair. In the canonical $3+1$ ownership form, clean augmentation and
crossed bridge order are closed by explicit models.  A six-terminal decoder
now closes twelve of all fifteen crossing types and turns the other three
into a repaired `a_3`--`x` contact paired with one of three labelled
`y`-paths.  For a one-vertex repair, minor-critical colourings give a second
contact path avoiding both repair edges.  An intersection with the `p`- or
`q`-path closes by an explicit model; the exceptional `r`-intersection
returns an actual exact-seven separation whose two full-subgraph packing
numbers are both one.  The remaining obligation is to control a bypass that
meets the linkage skeleton or avoids the second residual path, and to attach
a strict rank to support replacements inside the fixed exchange core.

Broad attachment is now closed.  A connected off-linkage subgraph meeting
`a_3,x` and any five other normalized endpoints yields an explicit `K_7`
minor, as does one with contacts in five distinct linkage paths.  Exact
finite negatives show that the surviving bridge attachments must be
concentrated on at most four named paths. Thus the next theorem must use
the actual block/bridge geometry together with minor-critical data;
increasing the endpoint-contact count alone is no longer the right target.

The block--cutvertex equality cases are now uniform: a leaf-block interior
has at least six linkage neighbours and equality is an actual order-seven
separation preserving the complete linkage; a cutvertex-free component has
the corresponding threshold seven. The live residue has strict excess over
these thresholds.

The two-fan barrier shows that even arbitrarily large strict excess can be
hidden in ordered fans behind triangle adhesions. It rules out a descent
based only on first-hit count, first/last order, or the number of linkage
paths met. The missing exchange must break those triangle adhesions using
seven-connectivity or the proper-minor colouring witnesses.

A sharper finite guardrail has two components with eight contacts each in
nested intervals of the `y`--`r` path and still has treewidth five. Its
connectivity is exactly three. Thus the sector and interval theorems have
reduced the live mechanism to using seven-connectivity to force a path
across the nested intervals, or to return an actual order-seven boundary.

The other minimal ownership form, `2+2`, now has its clean augmentations,
both crossed-linkage types, a clean connector between the two unmatched
paths, and two web certificates proved.  Its remaining obligation is a
label-faithful six-terminal compression; a verified crossing example shows
that these three clean patterns do not exhaust the full six-path bridge
geometry.

The detailed formulations and all immediate dependencies are in
[`active/INDEX.md`](active/INDEX.md) and
[`active/hc7_support_six_frontier.md`](active/hc7_support_six_frontier.md).

## 4. Established obstructions to tempting shortcuts

The following approaches are known to be insufficient without additional
hypotheses:

- Seven-connectivity together with an unrooted $K_6$ model does not force a
  $K_7$ minor.  The join of $K_2$ with the icosahedron is the principal test
  example.
- A four-colourable boundary does not ensure that colourings of the two
  sides induce the same partition of the boundary.
- Regenerating an unrooted minor after a contraction does not preserve
  prescribed branch-set labels.
- Iterating only the endpoint-equality patterns of the three deleted edges
  has no well-founded rank; explicit highly connected examples branch and
  cycle.
- A single bounded rooted-minor classification does not compose the final
  one-vertex-intersection configuration.
- The Mader endpoint delta-matroid does not record terminal--terminal edges
  inside one model part, and its symmetric exchanges can leave every graph-
  realizable contraction slice.
- The canonical Gallai--Edmonds barrier and all static exact-block responses
  do not synchronize two shore colouring languages.
- Six arbitrary disjoint linking paths between the zero-overlap models do
  not suffice; an explicit quotient of treewidth five excludes $K_7$.
- One contracted external component with seven distinct quotient contacts
  also need not suffice. Seven host attachments may collapse under linkage
  contractions, so the quotient's two exceptional eight-frames cannot be
  promoted to a host separation without a first-hit argument.
- Two crossless four-terminal web certificates, with one external bridge
  in each exceptional class, can coexist without a `K_7` minor at
  connectivity three.  Their static compatibility is therefore false;
  seven-connectivity or minor-critical colouring must enter the composition.
- Replacing one vertex of an exact six-vertex support can preserve every
  private transversal pair and still cycle inside the fixed exchange core.
  The core prevents transversal drift but does not supply a descending rank.
- Two distinct repaired-contact components can each have arbitrarily many
  linkage attachments, including attachments to several linkage paths,
  without forcing a `K_7` minor in the extracted graph. The examples are
  triangle clique-sums rather than seven-connected critical hosts, so they
  show exactly where those global hypotheses must enter.
- Even two eight-contact components in the proved attachment sectors may
  occupy nested intervals in a graph of treewidth five. The verified
  example has connectivity three, so interval order without the host
  connectivity still does not compose the two components.
- A strict portal-tree reduction in a quotient obtained by contracting an
  exterior component need not lift to a smaller branch tree in the host;
  the internal connector cost can be arbitrarily large. The guaranteed
  near-`K_7` model is also not automatically aligned with a prescribed
  private pair. Any revival of that route needs a weighted connector bound
  and pair-compatible model data.
- Finite neighbourhood or Moser-spindle enumeration cannot replace an
  unbounded structural theorem.

Concrete examples and verification scripts are stored in
[`barriers/`](barriers/). They refute intermediate lemmas, not $HC_7$.

## 5. Evidence and maintenance policy

- A theorem note in [`results/`](results/) is treated as a repository proof
  only when its hypotheses, conclusion, and proof are written explicitly.
- An adjacent audit records a separate internal check, not peer review.
- Finite computer classifications retain their encodings and verification
  scripts; they are never promoted to unbounded theorems without a written
  reduction.
- [`active/`](active/) contains only current proof work and supporting
  computations.  Superseded work moves to [`archive/`](archive/), while
  false intermediate claims and their counterexamples move to
  [`barriers/`](barriers/).

Historical filenames retain some old project shorthand so that citations
and audit hashes remain stable.  Current public documents and all new work
should use standard graph-theoretic descriptions; see [`AGENTS.md`](AGENTS.md).

## 6. Principal external inputs

- W. Mader, [*Über trennende Eckenmengen in homomorphiekritischen
  Graphen*](https://eudml.org/doc/161665), Math. Ann. 175 (1968), 243--252:
  seven-connectivity of the relevant contraction-critical graph.
- J. Niu and C.-Q. Zhang, [*Cliques, minors and apex
  graphs*](https://doi.org/10.1016/j.disc.2008.12.009), Discrete Math. 309
  (2009), 4095--4107, Theorem 1.10: the three-clique minor theorem used in
  item 2.
- A. Martinsson and R. Steiner, [*Strengthening Hadwiger's conjecture for
  4- and 5-chromatic
  graphs*](https://doi.org/10.1016/j.jctb.2023.08.009), J. Combin. Theory
  Ser. B 164 (2024), 1--16: Strong Hadwiger for four colours, used in the
  rooted argument described in the technical frontier.
- M. Wahlström, [*Representative set statements for delta-matroids and the
  Mader delta-matroid*](https://arxiv.org/abs/2306.03605), especially the
  linear representation of Mader endpoint systems. The terminal-edge
  projection in item 13 is a new deduction in this repository.
- S. Humeau and D. Pous, [*On the Two Paths Theorem and the Two Disjoint
  Paths Problem*](https://arxiv.org/abs/2505.16431), Theorem 1.5 and the
  equivalent web-completion formulation in Section 5: the structural input
  used in items 15--16.
- P. Wollan, [*Bridges in Highly Connected
  Graphs*](https://doi.org/10.1137/070710214), SIAM J. Discrete Math. 24
  (2010), 1731--1741, Theorem 1.1: endpoint-preserving stable rerouting of
  the six-path system in item 16.
- R. Fabila-Monroy and D. R. Wood, [*Rooted
  $K_4$-Minors*](https://doi.org/10.37236/3476), Electron. J. Combin. 20(2)
  (2013), P64, Lemma 7: the cycle-linkage rooted model used in the `2+2`
  branch of item 16.
- A. Girão et al., [*The Dominating 4-Colour
  Theorem*](https://arxiv.org/abs/2605.10112), Theorem 1.1 and Lemmas 2.1--2.2:
  regeneration after deleting a nonadjacent pair and ordered-clique-compatible
  dominating models through contractions. The low-colour
  absorption-or-separator theorem at the current frontier is a new deduction
  in this repository.
