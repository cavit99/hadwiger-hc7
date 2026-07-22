# Degree-seven boundary-labelled near-clique composition

**Status:** active conjectural target.  Every result described below as
proved has a separate adjacent audit.  The generic exact-seven terminal
theorem in Section 7 is open.  Nothing here proves `HC_7`.

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

The audited
[tight-pole edge-localization theorem](../results/hc7_degree7_tight_pole_edge_localization.md)
now shows that the pole transition is automatic in this exact matching
language, rather than a separate transition-selection obstruction.  Choose
three disjoint boundary nonedges `e_0,e_1,e_2` and the exact-`e_0`
colouring above.  For each of the two disjoint bichromatic components
joining the ends of `e_1,e_2`, either there are two internally
vertex-disjoint routes or an internal articulation has a connected root
side `W` with

\[
                              |W|<|C|,
                              \qquad |N_G(W)|\ge7.       \tag{2.2}
\]

Any crossing edge from `W` to `N_G(W)` supplies a proper-minor response.
Equality in (2.2) is a strict generic exact-seven selected-response descent.
After excluding that outcome, each returned smaller side has boundary at
least eight.  When
the articulation is witnessed by a separating bichromatic edge, its
edge-deletion colouring retains the prescribed matching `\{e_0,e_i\}` and
all five endpoint Kempe locks.  If both layers have such edges, the two
swaps commute and retain the exact triple matching under double deletion.
Thus each layer independently has either two internally vertex-disjoint
root-to-root routes or a response-bearing smaller side; after excluding
order seven, each returned side has boundary at least eight.  Mixed
route/separator outcomes are included, and none of these outcomes is
terminal.

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
does not by itself align the two closed-shore colourings.  The new
full-component Kempe-transition theorem supplies the missing dynamic
coupling: the boundary is five-degenerate, and, after fixing any nonempty
independent boundary set as one exact colour class, every labelled boundary
colouring lies in one Kempe component.  A shortest transition between the
two disjoint shore-extension sets has a literal bichromatic obstruction
path in the first component at one end and in the other component at the
opposite end.  If the transition has length one, the same boundary
interchange is obstructed on both sides.  The paths are not yet proved to
meet the inherited branch sets in the required labelled pattern.

There is now a complete positive-linkage closure in this two-component
normal form.  If one named full component contains a nontrivial path
between the `d`- and `e`-portal sets, disjoint from a connected subgraph
meeting every portal of one bipartition class, the other full component
supplies the second class.  Three- and four-block contractions realize both
root equality responses on the opposite shore; one response therefore
matches and the two shore colourings glue.  When the selected class has
order two, the exact survivor is a negative set-terminal Two Paths
instance in each named full component: either the root portal sets share a
degenerate first hit or the four portals have a crossless web obstruction.
For a class of order three, the unresolved analogue is the failure of a
root path disjoint from a connected subgraph meeting all three portal sets.

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
containing two vertex-disjoint odd cycles.  The same transition theorem now
turns this finite normal form into literal host geometry.  Every survivor
has a three-colouring `A|B|{p,q}` for some local nonedge `pq` of the new
boundary.  This local pair is not automatically the inherited old pair
`r,z`.  Either that exact three-block partition
extends through all three component-sides and glues, or one component is
locked in the split partition `A|B|{p}|{q}` and contains a bichromatic
`p`--`q` path.  Deleting the first boundary--component edge of that path
forces a different, demand-at-least-three response and five colour-indexed
paths from the internal endpoint back to the boundary.  The five paths are
edge-disjoint and can meet only at vertices of their common endpoint colour,
but the paths as originally selected need not be internally disjoint.

There are now two complementary normalizations.  Globally, the edge `vp`
and the five colour-indexed first edges extend to six pairwise internally
disjoint paths ending at every vertex of any prescribed six-set.  This
removes endpoint concentration only when the paths may traverse the whole
host; they can cross unselected boundary vertices or protected branch sets.
If the original boundary targets are retained inside the named component,
a vertex-capacitated Menger argument instead returns either five paths
disjoint outside their base and the boundary, or an actual order-seven
separation.  In the latter outcome the edge-deletion colouring is proper on
one closed shore and has a named exact boundary colour class `J` of order at
least two.  The opposite shore also realizes `J` exactly, and all exact-`J`
boundary colourings lie in one Kempe class.  A clique outside `J` already
synchronizes the shores; every live separator output has a nonedge outside
`J`.

The nonedge now has a simultaneous host-level consequence.  Either one
shore contains its bichromatic path, or the two shore colourings can be
normalized with a common non-`J` colour absent from the boundary.  In the
latter case there are two vertex-disjoint paths: one joins the deleted-edge
endpoints and meets the seven-boundary only in `J`; the other passes through
the opposite shore and joins two distinct bichromatic components outside
`J`.  Equivalently, after recolouring the exterior deleted-edge endpoint
with the fresh colour and adjoining it to the boundary, a shortest
eight-vertex boundary transition gives a common trace, an actual order-seven
separation, or one selected component adjacent to all eight boundary
vertices.  The theorem does not yet allocate either path to the inherited
minor-model labels, and only the selected component is asserted to be
eight-boundary-full.

There is also a well-founded normalization on the minor-model side.
Contract the deleted edge and choose a `K_6`-minor model containing its
image so that the containing branch set is first as small as possible and
then the whole model covers as many vertices as possible.  Removing the
contraction image leaves at most two components of that branch set.  Every
detachable component is solely responsible for contacts with at least two
of the other five branch sets, and different components are responsible
for disjoint label sets.  A component outside the model attaches only to
the contraction-image branch set; a six-vertex attachment set lifts to a
full exact order-seven separator.  Splitting the lifted branch set across
the deleted edge gives an explicit `K_7` model whenever both sides retain
all five foreign contacts.  A connected subgraph wholly outside the model
cannot repair a missing foreign contact.

That model-side normalization can now be made stable under one proper-minor
response.  After safely absorbing every unused component, the lifted
`K_7`-minus-one-edge model is spanning.  Seven-connectivity distributes the
neighbourhood of a deficient branch set among only five other branch sets,
so one of them contains two distinct attachment vertices.  Deleting one of
the corresponding model edges leaves the same labelled near-complete model,
while contracting it gives a rooted `K_6` model.  In the edge deletion all
five bichromatic endpoint paths therefore coexist with the fixed spanning
model.  This removes the former unique-portal and model-edge-destruction
obstructions, but the paths are still palette-labelled rather than
branch-set-labelled.

The colouring side now has an exhaustive dynamic reduction.  On a boundary
of order at most eight, take a shortest Kempe path between the two disjoint
sets of boundary colourings extending through the two shores.  If its
length is one, the same boundary interchange is obstructed by a literal
two-colour path through each open shore.  If its length is larger, an
intermediate boundary colouring is rejected by both shores and produces an
induced vertex-minimal list-critical subgraph in each.  For a fixed rejected
trace on the asymmetric order-eight interface, a proper list-critical
subgraph transfers the same rejected trace to a strictly smaller
complementary connected subgraph.  If it fills its shore instead, every
vertex deletion has a six-colouring inducing that same boundary trace.

At an actual order-seven boundary there is an independent well-founded
reduction.  A critical boundary edge gives five colour-distinguished first
edges and a six-ended fan inside its open component.  When the original
targets occupy at most five boundary vertices, either the five prescribed
first edges extend to a clean target-retaining packing or a strictly smaller
component lies behind another actual order-seven boundary.  The smaller
boundary has one exact colour block of order at least two attained on both
closed shores.  This is a genuine component-order descent, but it does not
retain a common full boundary partition or the five minor-model labels.

Contracting the distinguished edge in the asymmetric order-eight interface
also gives a precise exact-seven normal form.  Both open components become
adjacent to all seven boundary vertices.  The contracted boundary is
four-degenerate.  Its only five-chromatic form is `K_2 join C_5`; in that
case the contracted graph has a planarizing pair.  Undoing the contraction
leaves one adjacent vertex split of the planar graph, and every relevant
`K_5` model uses the two split vertices in different branch sets.  This
split-planar alternative is a normalized residue, not a two-apex conclusion
in the original graph.

### First-hit compression and the remaining label-preserving exit

The common-endpoint rooted model-reselection part of the former alignment
problem is now solved.
Let `g=xv` be the critical boundary edge, with `{x}` the protected singleton
branch set, and minimize the common labelled branch set `R` containing `v`
among spanning labelled `K_7`-minus-one-edge models which retain that
singleton and edge.  At least two distinct edges incident with `v` are
deletion-persistent for the same model.  In particular a persistent edge
can be chosen distinct from `g`, and `G[R]-v` has at most two components.
The parameter-uniform version permits several protected singleton branch
sets and correspondingly lowers the component bound.

There is also an exact simultaneous-deletion dichotomy.  Either two
incident edges at `v` can be deleted together while the same spanning
labelled model survives, or

\[
                        R=\{v\},\qquad d_G(v)=7,
\]

and `N_G(v)` is the boundary of an actual order-seven separation with both
open sides nonempty.  In a hypothetical minor-minimal counterexample, the
common two-edge deletion in the first outcome is six-colourable as well as
model-preserving.  It remains essential that the colouring and the model
now coexist in one graph; a palette colour still does not identify a named
branch set.

At the deficient singleton itself the persistence structure is exact.  If
the five common branch sets meet `{x}` in `n_1,...,n_5` edges, a maximum
simultaneous model-preserving incident-edge deletion has order

\[
                              d_G(x)-5.
\]

Every prescribed persistent edge belongs to such a maximum deletion, and
the pairs which are not jointly persistent form a matching, one pair for
each common branch set with exactly two neighbours of `x`.  Degree seven
is already an actual order-seven singleton-side separation.  For a
nonadjacent maximum pair at that degree, the five surviving neighbours are
simultaneously one per named common branch set and one per alternate
colour, so palette-to-label allocation is genuinely bijective there.

The dense alternative is now much smaller than the earlier generic bound.
If every jointly persistent pair has adjacent outer endpoints, then
`d_G(x)<=8`.  The two provisional degree-nine equality patterns each give
an explicit `K_7` model: one by a path after deleting five vertices, the
other by a five-fan in `G-x`.  Consequently degree at least nine forces a
jointly persistent pair with nonadjacent outer endpoints.  At degree eight,
a maximum three-edge deletion has triangle outer endpoints.  The uniform
clique-star response theorem then gives either one Kempe transition and a
common-boundary connected bipartite subgraph, or a connected
four-chromatic subgraph containing the whole four-vertex clique.  A
nondominating subgraph in either outcome exposes an actual separator; a
dominating one has a `K_6`-minor-free complement of the stated lower
chromatic number.  This replaces the finite degree-eight Hall pattern by
an unbounded separator-or-dominating-subgraph dichotomy, but it does not
yet align colours with model labels.

The model-preserving deletion can also be aligned with a branch-set split.
Either the split gives an explicit `K_7` model, or one deleted edge enters a
proper connected part `L` of a common branch set while the other ends
outside it, and `N_G(L)` is an actual separator.  In the clean placement,
the two one-edge response languages lie on opposite closed shores.  A
nested full-neighbourhood step strictly lowers the same boundary, unless
the opposite endpoint component is full to it.  Minimizing over all such
oriented separators is therefore well founded and gives two endpoint
components which are both full to one common boundary.  The remaining
exception is a deleted edge lying in the boundary itself.

There is an exhaustive colouring fork for every jointly persistent pair
`va,vb`.  If `ab` is absent, contracting the induced star gives the exact
trace with colour class `{a,b}` on `N_G(v)`, followed by the existing
saturation-or-bypass alternative.  If `ab` is present, the common deletion
has exactly two critical-triangle response families.  A first transition
swaps one connected bichromatic subgraph `D`; the opposite one-edge
responses agree on `N_G(D)`.  A nondominating `D` exposes an actual commonly
coloured separator, while a dominating `D` has a five-chromatic,
`K_6`-minor-free complement.  If the response families are Kempe-separated,
the component containing the triangle is connected and exactly
three-chromatic.  It again gives an actual separator when nondominating;
when dominating its complement is `K_6`-minor-free and four- or
five-chromatic.  Thus the former unexplained Kempe-separated branch is now
a standard host-level structural alternative.

At an exact order-seven separator returned by a transition, the two open
sides have boundary-full connected-subgraph packing vector `(1,1)`, `(1,2)`
or `(2,1)`.  The common boundary partition has exact full-subgraph demand
strictly greater than the packing number on the opposite side; otherwise
connected contractions reflect the same partition and the two shore
colourings glue.  The two surviving partition forms and their clique
restrictions are explicit.  In every demand-two merge-critical subcase a
literal bichromatic path through the opposite open side is forced.  The
next operation must compose that path with the two disjoint boundary-full
connected subgraphs; further enumeration of boundary partitions is no
longer relevant.

The direct-entry equality has an independent host-level reduction.
Simultaneously contracting the two direct-entry edges and expanding a
six-colouring makes the rich shore uncolourable from its
boundary-forbidden lists.  A vertex-minimal induced obstruction is
connected.  If it is proper, its full neighbourhood is a strict
connected-side descent with the two failed edges placed exactly on the
returned closed sides.  If it fills the shore, every vertex satisfies

\[
 d_G(v)=6+\varepsilon(v)+\rho(v).
\]

Low list-degree excess plus repeated boundary-colour count gives an
order-seven or order-eight singleton-side separation.  An all-tight shore is
a Gallai tree, and the surplus-sensitive density inequality bounds many of
the remaining shores.  None of these conclusions by itself preserves the
five inherited branch-set labels.

Literal first-hit ownership is now an exact, rather than conjectural,
invariant.  In the terminal-avoiding graph, Rado's theorem for a strict
gammoid gives five response paths with distinct first-hit labels exactly
when every label subset satisfies the corresponding rank inequality.
Failure gives a deficient label set and a minimum separator.  With five
labels and at most three fixed response vertices, that certificate yields
an actual order-seven separation or two contacts with the same unused
label.  Repeating the exposure argument produces an order-seven separation,
two independent or incident persistent edges, or a connected source
subgraph of order at most four.

For the returned edge pair, the fixed-partition theorem gives exactly three
possibilities: single-side attainment; common rejection with a strict
same-partition critical subgraph; or common equality at both edge pairs.
In the common-equality branch every partition-changing two-colour component
meets the literal boundary.  The paired-boundary footprint calculation
eliminates every switch of demand at most two, including the exceptional
nonedge.  A proper total-rejection component retaining all five named
contacts is already absorbable; the unresolved branch is the one in which
contacts collide in inherited branch sets.

The collision geometry now has a well-founded label-sensitive rank.  The
response paths may overlap inside the fixed connected response subgraph but
are disjoint outside it and have distinct literal first branch-set labels.
Every zero- or one-owner transfer preserves this rank: a path formerly
ending in the transferred piece is replaced inside the response subgraph by
the persistent edge into the retained donor.  Maximizing the rank and then
minimizing the donor therefore eliminates all such transfers, including a
ranked unique owner.

More generally, let `A_i` be the portal set in a transferred piece for its
`i`th owner, and let `B` be its portal set to the retained donor.  Disjoint
paths from distinct vertices of `B` to the `A_i`, one per owner, split the
piece among all owners.  Absorbing the resulting connected parts gives an
explicit `K_7` or a strict rank- and label-preserving model descent.  In an
extremal model Rado--Menger failure therefore has a canonical form: an
inclusion-minimal owner family `I` has a transversal of order
`|I|-1<=4` inside the old branch set, while every proper subfamily is
linkable.  With two owners the obstruction is one literal bottleneck.  If
both owner portal sets are not concentrated at that vertex, a component
behind it is anticomplete to the retained donor.  Seven-connectivity then
returns either a label-transversal order-seven full-neighbourhood boundary
or two model-preserving deletion-critical edges from that component to one
outside branch set.  More generally, for any minimal deficient owner family,
either all owner portals lie in its internal transversal of order at most
four, a connected piece exposes an actual separator of order at most ten,
or one outside branch set is met twice.  The concentrated case itself gives
an incident pair of differently labelled owner contacts by pigeonhole.
Thus every owner-portal obstruction has been converted to a bounded host
separation or one of two explicit critical-edge geometries.

There is now a parameter-uniform completion theorem for the proper-subfamily
linkages supplied by a minimal owner circuit.  Let `I` have order `m`, with
`2<=m<=5`, and let `K` be its `m-1` vertex internal transversal.  If a
component `C` of the donor minus `K` is anticomplete to the retained donor,
meets all six outside branch sets, and the owners in `I-{R_0}` can be linked
to distinct retained-donor portals in the donor minus `C`, then those paths,
the retained donor, `C`, and five explicitly selected or merged outside
branch sets form a `K_7`-minor model.  It is enough more generally that the
paths leave a connected residual subgraph of `C` adjacent to their union and
to all six outside branch sets.

In the three-owner no-repeated-contact equality case, the same analysis
gives a literal order-eight normal form.  The boundary is the two-vertex
internal transversal together with one vertex from each of the six outside
branch sets.  A component missing one boundary vertex returns an actual
order-seven separation.  Otherwise the complement has two or three
boundary-full components and the boundary is four-colourable; the
three-component case lies in the audited 82-type order-eight residue.  Thus
the exact remaining static obstruction is sharp: every two-owner linkage
uses the distinguished component and leaves no connected residual with all
six outside contacts.  Only a proper-minor colouring response can now break
that obstruction or synchronize the returned boundary.

The global max-first-hit-rank/minimum-donor choice forces an additional
concentration.  The part of the donor retained outside the distinguished
component is connected.  If zero, one or two owner portal sets were
concentrated in the component, moving it wholesale or splitting it along a
proper two-owner linkage would preserve all labels and the selected response
while strictly shrinking the donor.  Therefore all three owner portal sets
are concentrated there.

That final concentrated configuration is now impossible.  If every owner
has at least two portals in the distinguished component, a minimal connected
transversal leaves a proper connected piece which can be moved to one owner
while the reduced donor remains connected and retains all three owner
contacts.  If some owner has a unique portal `s`, pairwise owner linkages
leave the other two contacts outside `s`; the exact eight-neighbour count
and seven-connectivity force every component after deleting `s` to attach
to the retained donor.  Moving `s` to its owner again preserves every
label, prescribed root, the selected response and the maximum first-hit
rank while strictly shrinking the donor.  Either move repairs the unique
missing adjacency and gives a `K_7` minor, or contradicts the minimum donor
choice.  Thus the three-owner no-repeated-contact equality-eight branch is
eliminated before any colour-compatibility problem at a returned separator.

The order-eight side is now operation-decorated as well.  For both two and
three boundary-full complementary components, a selected edge-deletion
colouring is legal on all unchanged components and rejected on the operated
one.  Its five forced two-colour paths give either a clean fan, pairwise
disjoint outside the source and the boundary, or an exact order-seven
separation.  At the exact boundary, both shores realize the same exact
colour block; if their full equality partitions differ, both orientations
have literal Kempe obstruction paths and Hall-deficient connected-support
systems.  These paths and supports are operation-specific, but they are not
yet allocated to the inherited branch-set labels.

Raw five-contact support is not a terminal substitute for that allocation.
The exact quotient classification for two adjacent connected subgraphs and
the six outside branch sets has two sharp obstruction types: crossed misses
at `X,Y`, and distinct misses among `D,F_1,F_2,F_3`.  Their quotients are
respectively `K_8` minus the edges of a four-vertex path and `K_8-3K_2`.
Every other pattern gives an explicit `K_7`-minor model, and repairing any
one of the three missing adjacencies in either obstruction is terminal.  The
correct dynamic object is therefore the family of outside branch sets usable
simultaneously by both connected subgraphs, not the number of raw contacts.

Repeated contacts alone do not lower component defect: after a split the
exact value is

\[
                    \Delta'=\kappa_2+\kappa_3+\kappa_4-3.
\]

Thus the old-contact components must be retained, not merely hit twice.  On
the separator side, mixed connected supports now have an exact Hall
criterion.  Boundary-full subgraphs are universal supports; every other
named connected subgraph is eligible exactly for the boundary blocks whose
complete duty set it meets.  Two full subgraphs close demand at most two,
and close demand three exactly when one additional named subgraph meets one
complete duty.  Failure is an explicit Hall-deficient block family.

For the label-transversal exact seven-boundary returned above, this failure
has now been calculated dynamically.  The boundary-edge critical-pinch
partition is legal on the opposite shore and rejected by the intact exposed
shore.  The opposite shore contains only `r in {1,2}` disjoint
boundary-full connected supports, and every permissible family of further
named connected supports has a nonempty block family `X` with

\[
                          r+|N(X)|<|X|.
\]

When `(r,d)=(2,3)` or `(1,2)`, every named support misses a literal vertex
of every complete duty.  The five bichromatic entrance paths returned by
the pinch lie on the wrong shore, so this is an exact operation-specific
residue rather than an automatic reflection.

The two edge-pair outcomes have also been checked against the complete
audited incident-edge calculus.  For an incident differently labelled pair,
deleting both edges leaves a six-chromatic, five-connected graph with the
two opposite one-edge equality responses and no response proper on both
edges.  Nonadjacent outer ends add the exact double-equality response and
give saturation or an outer-end bypass; adjacent outer ends give the
critical-triangle transition fork.  Only the subcase in which the two
owners are the missing model pair and their outer ends are adjacent is
immediately terminal.  For a repeated model-preserving pair, the two edges
cross the natural full-neighbourhood boundary, so the internal-shore and
opposite-shore edge theorems do not apply there.  Neither normal form yet
assigns a response path to a new named branch set.

Selecting one critical edge in each anticomplete open shore now supplies the
missing host geometry.  The common deletion host is six-chromatic and
five-connected; it contains either a `K_4` minor rooted at the four edge
endpoints or a universally orientable exact order-seven separation.  On the
same three-edge deletion host, the selected fixed-partition response is
coupled to a different opposite-shore boundary trace.

The earlier three-fan, two-edge and special `5+2` exact-seven descendants
remain valid conditional theorems, but the new strict transfer shows that
they are not live descendants of the concentrated three-owner branch.  In
the other owner-circuit branches, incident or repeated contacts and bounded
separators still require a label-faithful operation-specific closure.

In the independent generic exact-seven restart, the singleton alternative
has an unbounded closure.  Its boundary
has independence number at most two and chromatic number at most four, so
it is exactly four-chromatic.  A bipartite opposite exterior, coloured with
two fresh colours, could then be combined with the boundary colouring and
the singleton pole to six-colour `G`.  Hence every surviving singleton
exterior is nonbipartite; in particular no tree exterior survives.

The simultaneous contraction response produces a connected induced
two-root list-critical subgraph `K` in the exposed shore.  Its full
neighbourhood is an actual separator of order at least seven.  A proper
`K` is strictly smaller than the shore.  If `K` fills the shore, then

\[
                       d_G(v)=6+\varepsilon(v)+\rho(v)
\]

at every vertex, and any vertex with
`\varepsilon(v)+\rho(v)\le2` yields a singleton-side separator of order
seven or eight.  This does not yet preserve the special exact-seven
normal form: the new boundary can be larger than seven, the two failed
edges can lie on opposite closed sides or one can lie in the boundary, and
the double-contraction partition can differ from both one-edge responses.
The immediate operation-specific residue is therefore the singleton
`(1,1)` case, a proper list-critical core with boundary order greater than
seven or misaligned failed edges, or a shore-filling high-excess core.

One infinite subfamily now has a well-founded response-carrying move.  If
the connected one-full-subgraph shore has a bridge, the opposite shore has
two disjoint boundary-full connected subgraphs, and the boundary graph is
bipartite, exact two-list parity forces one distinct boundary vertex to
attach only to each bridge side.  The two forced vertices have even
boundary distance and the other five boundary vertices attach to both
sides.  Each bridge side therefore has a literal full neighbourhood of
order exactly seven.  The new near packing number is one, the opposite
number is one or two, and the bridge-deletion partition is legal on the
opposite closed shore, rejected on the bridge side and of excessive
demand.  Both new connected shores are strictly smaller.  Consequently a
minimum-order interface in this bipartite `(1,2)` branch is bridgeless.
The old partition, boundary bipartition and inherited model labels are not
preserved and must not be inferred at the new boundary.

The shore-filling list-critical branch now has an exact palette-incidence
density improvement.  With shore order `r`, total list-degree excess `E`
and `\Delta=\sum_v(d_G(v)-9)`, either a degree-seven/eight vertex exposes
a singleton-side separation or

\[
                         11r+9\Delta\le128+5E.
\]

In particular the all-tight branch has order at most eleven, improving the
previous bound eighteen.  Its Gallai-tree structure is also restricted:
six boundary contacts at an endblock lobe give an exact order-seven
separation; otherwise the block-cutvertex tree is a path with two
boundary-full end lobes, and a one-block shore is only `K_4` or `K_5`.
Thus the all-tight infinite family is no longer the live unbounded
obstruction.  The remaining shore-filling theorem must control positive
total list-degree excess using the global minor exclusion or additional
proper-minor responses; the local two-root list data alone cannot do so.

Two further audited statements sharpen that positive-excess target.  First,
an actual wheel shore is impossible: five or six almost-boundary-complete
rim neighbours, the hub, and one boundary-full connected subgraph on the
opposite shore form an explicit `K_7`-minor model.  Thus sparse wheel list
obstructions remain a local sharpness example but no longer survive the
host degree and full-shore hypotheses.

Second, every internal edge of the shore-filling list-critical graph either
lowers total list-degree excess by two in the edge-deleted fixed-list
obstruction, or its fixed boundary trace yields an endpoint path or two
disjoint first-hit paths to distinct boundary vertices for every alternate
colour.  If every edge takes the latter alternative, the graph is
subgraph-minimal non-list-colourable and its tight-vertex subgraph is a
Gallai forest.  The edge-deleted obstruction is not itself another
seven-chromatic host, so this is a normalization rather than a completed
induction.

For a proper list-critical core, the original one-edge deletion colouring
now gives the correct response pullback.  More generally, if the core has
an exact order-seven full neighbourhood, it is always a strictly smaller
generic selected-response interface.  Seven-connectivity retains the
originally selected entrance edge and supplies a second vertex-disjoint
entrance edge unless the connected shore is a singleton, so the two-edge
reduction can be restarted without the special five-plus-two provenance.
The old partition and model labels need not survive.  Thus literal
inherited-vertex loss is no longer an obstruction to generic recursion;
the remaining proper-core placement obstruction is separator excess.

In the shore-filling branch, choose a double-contraction colouring which
lexicographically minimizes total boundary-colour incidence, boundary
demand, and then block count.  Every pair of boundary colours then has one
common bichromatic component in the contracted minor: otherwise a Kempe
switch merges their anticomplete blocks without increasing the first two
coordinates.  A shortest connection is internally confined to one open
shore.  This is pairwise support only; simultaneous disjointness and literal
branch-set ownership remain the missing packaging step.

The separator-excess branch now has a host-level minimum normal form.  Let
`R` be an eligible connected set with `|N_G(R)|>=8`, chosen with minimum
boundary order.  Either a component of the complement has an exact
order-seven full neighbourhood and restarts the generic recursion (with no
theorem yet making that returned shore smaller than the previously selected
minimum shore), or the complement has exactly two or three components and
every component is adjacent to every literal boundary vertex.  In a minimum generic response
shore every proper connected subset has at least eight literal neighbours;
the boundary-completed shore is consequently eight-connected.  These are
literal statements in `G`, not counts of contracted model bags.

At boundary order eight the two- and three-component cases have a uniform
operation-specific alternative.  For a non-singleton selected component,
deleting one selected
boundary-to-component edge gives either a clean five-path fan or an exact
order-seven generic restart with a strictly smaller connected component.
If that operated component is a proper subset of the minimum generic shore,
the restart contradicts minimality and the clean fan is forced; otherwise
both outcomes remain.  Independently, the boundary-labelled near-`K_7`
model supplies two disjoint boundary edges
leading to different common labels and a paired-source five-fan or another
strict order-seven restart.  What remains is not path existence: the paths
may have repeated boundary ends or first meet the wrong inherited branch
sets.

There is now an unconditional literal-host strengthening of the path
existence part.  Let `S` be an eight-vertex separator, let `C` be a
component of `G-S` with `N_G(C)=S`, and assume that `G-S` has another
component.  From every nonempty connected subgraph `P` of `C`, either
eight paths reach the eight distinct literal vertices of `S`, pairwise
disjoint outside `P`, or a nonempty connected proper subset of `C` has an
actual full neighbourhood of order seven.  Any prescribed distinct
`P-S` edges may be retained as fan limbs.  If `P` is a path and two
disjoint groups of boundary terminals are specified, the corresponding
rooted limbs lie in two vertex-disjoint connected subgraphs of the fan tree
if and only if their two minimal attachment intervals on `P` are disjoint.
Connectedness of `C` then extends them to an adjacent connected partition
of `C`.

This theorem removes repeated boundary endpoints, but not the labelled
allocation problem.  A boundary terminal is not its inherited branch set,
and the theorem neither places prescribed internal roots in `P` nor forces
the two attachment intervals to be disjoint.  Failure gives a literal
order-seven separation, but no complete equality partition is thereby
known to extend through both closed shores.

If the component `C` itself is an induced path with prescribed roots at
its two ends and two disjoint two-vertex demand sets, the rooted split is
completely determined by literal contact intervals.  Let `a` be the latest
first contact required on the left and `b` the earliest last contact
required on the right.  The two requested disjoint rooted connected
subgraphs exist exactly when `a<b`.

The overlap branch is now closed when the order-eight interface has exactly
three boundary-full components and `|C|>=2`.  Under strict reversal
`a>b`, either one of the exact tail/middle neighbourhoods has order seven,
or the two complementary one-defect path sides combine with the other two
components as follows.  A cycle in the six-vertex residual boundary gives
an explicit `K_7` model; when that residual boundary is bipartite, an
explicit three- or four-block partition colours all three closed component
sides and the colourings glue.  When `a=b`, an internal shared portal gives
an explicit `K_7` model, while a shared portal at a path endpoint gives the
same minor/colouring/order-seven alternatives.  Thus every overlap outcome
for a nontrivial induced-path component returns an actual order-seven
separation or is terminal.  Colour compatibility of the returned
separation remains open, as do singleton and non-path selected components.

The non-path branch now has a strict host-level reduction whenever the
selected component has a cutvertex.  Choose a leaf block whose interior is
not adjacent to all eight boundary vertices.  Its full neighbourhood has
order seven or eight.  Order seven is an actual separation; at order eight
every complementary component is adjacent to every new boundary vertex,
there are only two or three components, and the leaf-block interior is a
strictly smaller selected component carrying a fresh equal-endpoint
edge-deletion response.  At a three-component return the audited boundary
classification restores a boundary triangle, so iteration terminates at
order seven, a two-component order-eight interface, or a three-component
interface whose selected component is a singleton, an edge, or
two-connected.  The move does not preserve the old partition or labels.

More generally, any proper connected lobe for which the sum of its internal
and boundary neighbourhood orders is at most eight has the same
order-seven-or-strict-order-eight outcome.  Applied behind a two-vertex cut
of a two-connected selected component, this shows that every unresolved
lobe meets seven or eight boundary vertices, and at most one lobe is
boundary-full.  Hence every other surviving lobe has exactly one missing
boundary contact.  The placement and colouring response of those defects,
not low connectivity alone, is the remaining two-cut obstruction.

On the 80 residual boundaries containing two vertex-disjoint triangles,
the two-cut obstruction has an exact form.  There are precisely two lobes;
each misses exactly one boundary vertex, and the two distinct missed
vertices meet every boundary triangle.  In particular they lie one in
each member of any fixed pair of disjoint triangles.  This does not yet
eliminate the two-lobe configuration and does not cover the two residual
boundary types whose certified disjoint odd cycles have orders `(3,5)`.

The exact two-lobe residue is now closed.  Both cut vertices miss both
defect vertices; assigning the cut vertices to opposite lobes produces
adjacent connected pieces with exact defects `d,e`; the boundary minus
`d,e` is bipartite; and `de` is absent.  Proper-minor colouring orients the
two responses.  For either opposite component, distinct root portals give
a splittable root path and hence the unequal response.  Failure of distinct
portals gives one common portal; contracting it with one root and
contracting the two defect-one lobes with the two bipartition classes
produces a `K_4` of contraction images and gives the same unequal response.
Both opposite component-sides therefore align with the selected-component
colouring, so the three colourings glue.  This eliminates the two-cut case
for arbitrary lobe and component sizes.  The width-five contact quotient
remains a valid warning that the dynamic response is essential, but it is
not a survivor of the completed theorem.

The genuinely two-component opposite-response branch has a new symmetric
normal form.  If its connected split-response shore contains two disjoint
connected subgraphs adjacent to every boundary vertex, then it has a
partition into two adjacent induced connected boundary-full parts.  A
connected root connector and disjoint supports for the two independent
boundary classes force the split-root partition on the opposite shore by a
proper-minor contraction.  Consequently, within either part of the cover,
every root connector intersects every support for each boundary class.

Connectedness of both open shores also removes all cycles from the
six-vertex boundary graph obtained by deleting the two roots.  A shortest
path in the merged-response shore makes its two one-defect connected
subgraphs adjacent without losing any boundary contact, while the split
shore has the adjacent boundary-full cover above.  Any residual boundary
cycle then splits into three connected arcs and, together with those four
off-boundary subgraphs and the two roots, gives an explicit `K_7`-minor
model.  Hence the residual graph is a forest.  If the boundary contains two
vertex-disjoint odd cycles, the `(3,5)` type is impossible; the survivor has
two root-containing triangles and each root has boundary degree exactly
two.  This normalizes, but does not eliminate, the remaining `(3,3)` forest
case.

This cross-intersection has a sharp small-transversal consequence.  If one
set of order at most two meets every root connector and every support for
both boundary classes, then it has order exactly two.  Each component after
its deletion misses exactly one root and one vertex from each three-vertex
boundary class, so its full neighbourhood is an actual order-seven
separator.  Every complementary component is adjacent to every new boundary
vertex, and the selected split colouring supplies one closed-shore response
on the seven-set.  A common opposite-shore partition is not yet obtained.

The separator calculation is now role-sensitive.  A set of order at most
three meeting all three support families gives an actual order-seven
separation or an exact order-eight full-neighbourhood separation missing
one root and one vertex from each boundary class.  More importantly, a set
of order at most two meeting only the two boundary-class support families
gives an actual order-seven separation or an exact order-eight
full-neighbourhood separation which retains both roots and two vertices of
each boundary class.  The selected split colouring restricts to that new
closed shore with those four inherited colour blocks, and its open shore is
a proper subset of the old one.  This does not yet transfer the opposite
response or the inherited minor-model labels, so the strict set inclusion
is not by itself a recursive descent.

The remaining high-transversal case must spend the global hypotheses.  An
explicit finite example is eight-connected and seven-chromatic, has the
same opposite merged/split responses and two disjoint boundary-full
connected subgraphs, but has neither a three-support packing nor an
order-seven separation.  It also has an explicit `K_7` minor, generated by
an edge whose two ends are adjacent to every branch set of a `K_5` model.
Thus the correct live disjunction is not packing versus separator under
connectivity alone.  It must use `K_7`-minor exclusion and the
operation-specific proper-minor colourings to obtain an explicit `K_7`
model, a colour-compatible order-seven separation, or a strict
selected-response descent.

Minor exclusion on the split closed shore does not repair the static
statement.  There is an exact four-vertex split-only shore whose two
boundary-full connected parts are adjacent, whose three support families
have no disjoint transversal and have common transversal number three, and
whose union with the eight-vertex boundary has treewidth at most five.
Therefore the next exchange must couple the split shore to the merged shore
or to a proper-minor colouring of the full host.

Equivalently, if `tau_XY` denotes the minimum order of a set meeting every
support for either three-vertex boundary class, the root-preserving
separator theorem handles `tau_XY<=2`.  The verified split-shore example has
`tau_XY=3`.  The immediate cross-shore obligation is therefore to use the
merged-shore response paths and the full-host proper-minor colourings to
force `tau_XY<=2`, construct an explicit `K_7` model, or return an
order-seven separation with one complete equality partition on both closed
shores.

The opposite merged-response shore supplies a complementary dynamic
constraint.  In every fixed merged-root six-colouring, each of the three
colours absent from the boundary gives a bichromatic path between the two
roots with all internal vertices in that shore.  The roots see all three
colours, and paths belonging to distinct absent colours intersect only at
vertices of the common root colour.  These three simultaneous Kempe locks
do not by themselves give disjoint paths or named first-hit allocation, but
they are the operation-free colouring data available to the high-transversal
exchange.

When the selected component is a singleton, low connectivity in the other
two components is now equally constrained.  Neither is a singleton;
cutvertices with at least three lobes are terminal; and at most one of the
two components can contain a cutvertex or bridge.  Every surviving bridge
or two-lobe cutvertex split has two adjacent connected sides with distinct
defects `d,e`, where `de` is absent and `G[S-{d,e}]` is bipartite.  A
surviving cutvertex itself misses both defects.  The remaining issue is the
label- and colouring-sensitive two-piece configuration, not the existence
of further lobes.

The induced-path-component hypothesis is essential: the seven-connected,
`K_7`-minor-free graph obtained as the join of `K_2` and the icosahedral
graph has an all-boundary path fan with strictly reversed demands but no
requested rooted split.  It is six-colourable and has the compatible
order-seven separation recorded by the barrier.  Thus this closure cannot
be transferred to an arbitrary fan spine without using the component's
literal off-path structure or the proper-minor response.

A label-preserving reduction applies when one boundary-full component is
contained literally in one branch set `U` of an extremal spanning labelled
`K_7`-minus-one-edge model.  Assume that deleting the component leaves `U`
connected with its prescribed root and fixed response edge, and that the
eight boundary vertices consist of two vertices in the retained part of
`U` and one vertex in each of the other six branch sets.  A six-label fan
and the maximum-first-hit-rank/minimum-`|U|` choice then give either an
actual order-seven full-neighbourhood separation or a singleton component
`{v}` with `N_G(v)=S` and `d_G(v)=8`.  Prescribed incident one-edge
responses and their literal branch-set labels survive the separation
outcome.  A simultaneous contraction response survives as a proper
opposite-shore colouring only when its two boundary terminals are
nonadjacent.  No common equality partition is obtained, the degree-eight
singleton remains open, and an arbitrary full component has not been
proved to satisfy the branch-set-containment hypotheses.

The singleton outcome has a further exact label obstruction.  Write `U`
as the disjoint union of `U_0` and `{v}`, and let `Omega` be the set of the
six foreign branch-set labels with no edge from `U_0`.  Extremality gives
`|Omega|>=2`, and `Omega` contains `X` or `Y`.  If its provenance gives
`|Omega|=3`, then, up to the natural symmetries, only two patterns remain:
both polar labels plus one further label, or one polar label plus two
further labels.  If an opposite component is adjacent to all eight
boundary vertices, then `G[S-w]` is `K_5`-minor-free for every `w in S`,
since any such model, that component, and `{v,w}` would form a `K_7`
model.  This still neither repartitions the opposite component among the
six inherited labels nor produces one equality partition common to both
closed shores.  Neither normalization proves `HC_7`.

At the raw three-component order-eight interface, a different elementary
construction rules out a tempting shortcut.  Four pairwise disjoint
connected subgraphs, each adjacent to every boundary vertex, together with
a boundary triangle and three further boundary vertices form an explicit
`K_7`-minor model.  All 82 surviving boundary types contain a triangle.
Consequently none of their three boundary-full components contains two
disjoint connected subgraphs both adjacent to every boundary vertex.  In
particular, splitting one raw component into two boundary-full pieces is
already terminal and cannot serve as an order-eight substitute for the
defect-two reflection theorem, whose input is an actual seven-vertex
separator.

Nor may a fourth boundary-full subgraph be replaced unconditionally by a
connected subgraph missing at most two boundary vertices.  There is an
explicit quotient with boundary `2K_3` plus two isolated vertices, three
boundary-full vertices, and a fourth vertex missing one vertex of each
triangle.  It has a tree decomposition of width at most five and hence no
`K_7` minor.  This refutes the raw order-eight contact-set implication, not
the active host theorem: the quotient is not seven-connected or
seven-contraction-critical and carries no operation-specific colouring
response.  Seven-connectivity, such proper-minor responses, and a split
using the internal structure of a connected subgraph remain available
extra mechanisms.

Finally, the concentrated alternative with three designated branch sets is
now eliminated without regenerating an unlabelled minor model.  A connected
transversal either supplies a proper connected transfer which retains all
three owner contacts, or one owner has a unique portal.  In the latter case
the exact order-eight contact count and seven-connectivity make the donor
minus that portal connected.  Moving the selected piece or the unique
portal to its owner preserves the selected response, every branch-set label
and the maximum first-hit rank while strictly shrinking `U`; repairing the
old missing pair instead gives a `K_7` minor.  Thus the earlier three-edge
probe is superseded in this branch.  The two-owner, repeated-contact and
non-branch-set-contained interface cases remain live.

The exact partition side is now uniform over the complete frozen
129-boundary residual.  Given a connected subgraph missing at most two
boundary vertices, one can choose a nontrivial independent boundary block
before the proper-minor colouring so that two disjoint boundary-full
connected subgraphs plus that third subgraph realize every returned
partition on one shore.  A boundary-full connected subgraph on the other
shore then reflects the same complete partition and six-colours `G`.
Accordingly, the live geometric obligation is to construct that third
subgraph from the clean fan or to allocate the fan to the five literal
branch-set labels.

For the final two-full-shore positive-excess configuration, exact-block
Kempe reconfiguration gives a second uniform entry.  Fixing any nonempty
independent boundary set as the exact sixth colour class, a shortest path
between the two shore-extension languages gives either one boundary
interchange obstructed by a literal path through each shore, or two
simultaneous vertex-minimal list-uncolourable shore subgraphs for the same
boundary trace.  Mader's bound together with the equality classification
now removes every boundary of order at least ten: it returns an exact
order-seven singleton response or a strictly smaller boundary response.
Thus, after separately excluding the fresh-response alternative returned by
a proper list-critical kernel, the unresolved long-transition endpoint has
boundary order nine, `|W|=2`, and both list-critical subgraphs spanning
their shores. At that endpoint every opposite pair deletion is six-colourable
with the same boundary trace and saturates both deleted vertices; moreover
every shore vertex has list-degree excess plus repeated-boundary-colour
count at least three, with the tight vertices inducing a Gallai forest.

For a trace using all six colours, tight vertices now have a literal
description: each is adjacent to every boundary vertex in every
nonsingleton colour class.  Cycles in both tight subgraphs therefore give
an explicit `K_7`-minor model.  Every nontrivial tight Gallai block has a
common missed set of singleton boundary vertices and satisfies the exact
full-neighbourhood formula

\[
 |N_G(H)|=|N_{G[Z]}(H)-V(H)|+9-|B-N_G(H)|.
\]

This gives an order-seven response, an order-eight response, or the sharp
residual inequality that the block has at least as many internal attachment
vertices as missed boundary vertices.  In particular, a two-connected
boundary-full spanning shore cannot be entirely tight; the remaining
full-six endpoint has genuine positive list-degree excess in each shore.

Every tight vertex itself has a stronger dynamic consequence.  It has
degree nine, and deleting any incident edge gives an exact full-six-colour
singleton response on its literal neighbourhood.  Deleting an internal
tight edge under the old fixed trace bijects its internal neighbours with
the missed singleton boundary colours, giving a literal one-for-one rainbow
replacement.  With the full host hypotheses, one can select an adjacent
pair and exterior component so that the returned boundary has order seven
or eight, or has order nine, is four-colourable, and has connected
boundary-full subgraphs on both sides.  This remains a one-step response:
the old exact block and inherited minor-model labels need not survive.
At the same tight pole, an exterior component can be selected so that its
literal full neighbourhood has order seven through nine and deleting the
aligned pole edge returns an exact singleton boundary block.  Deleting that
singleton from the boundary leaves a `K_5`-minor-free graph.  If the exterior
component is adjacent to all nine neighbours, the boundary graph has at most
twenty-two edges; hence one can choose the same pole edge at a boundary
vertex of internal degree at most four.  That vertex has at least two
exterior neighbours, and the host contains a rooted minor of the form
`K_2` joined with the resulting `K_5`-minor-free boundary base.  This
compresses the full-component case to a sparse labelled near-clique
obstruction but does not yet give a global two-apex pair or compatible
shore colourings.
There is no purely local replacement by a small tight-block separator: an
audited four-cycle list obstruction is two-connected, boundary-full and of
positive excess, yet its unique tight block has full neighbourhood of order
ten.  Any further descent must use the host response or global minor
exclusion.

In the distance-one branch, an obstruction path whose ends lie in one
component of the inherited boundary forest and whose deletion leaves a
boundary-full residual component gives an explicit `K_7`-minor model.
Otherwise the surviving components satisfy the exact inequality

\[
 |N_G(H)\cap V(P^\circ)|\ge |B-N_G(H)|,
\]

unless an order-seven or order-eight full-neighbourhood response already
occurs.  A cutvertex in either spanning shore similarly gives a strictly
smaller fresh connected response side, but that response need not retain
the selected exact block or inherited model labels.

If the one-move obstruction path spans its shore, every proper prefix and
suffix meets at least eight of the nine boundary vertices outside the same
response exits.  A full--full split gives an explicit `K_7` model; otherwise
the attachment intervals have one shared portal or opposite one-vertex
defects.  Four anchored branch sets and the distinguished boundary triangle
then complete `K_7` whenever those possible defects avoid the triangle.
Thus the shore-spanning residue is confined to triangle-owned defects or an
endpoint/atomic shared portal.

These are genuine host-level reductions, but not yet label allocation.  A
separate finite barrier realizes every independent exact block on both
connected full shores while keeping all fixed-block Kempe distances at
least two.  It deliberately lacks `K_7`-minor exclusion and full
minor-criticality.  Consequently varying the fixed block cannot by itself
close the endpoint.  A maximum-palette argument now supplies an exact
full-trace dichotomy: either one full-six-colour exact trace is rejected by
both shores and gives the paired list-critical endpoint, or every such trace
extends through exactly one shore.  If neither shore attains six boundary
colours, splitting a repeated boundary colour class with an unused colour
forces the first outcome.  Thus the next theorem must close the paired
positive-excess endpoint or the one-sided full-trace alternative by an
internal operation at a non-tight vertex or the literal tight-block
attachments.  In the one-move branch it must resolve the path-spanning or
boundary-location collision.  Either route must terminate in the labelled
construction or a compatible order-seven separator below.

The one-sided full-trace alternative now has a canonical dynamic form.
For every `K_5`-minor-free graph `H` of order four through eight, the graph
of proper labelled five-colourings using at least four colours is connected
under single-vertex recolourings.  Hence the full recolouring graph is also
connected.
Choose a shortest path from one shore-extension set to the other.  If its
length is at least two, every internal trace is rejected by both shores;
in the present one-sided residual it uses at most four colours on `H` and
therefore gives paired list-critical subgraphs with an unused colour.  If
the length is one, one literal boundary vertex changes colour.  When the
new colour was absent from the boundary, gluing the opposite shore
extensions after deleting that vertex forces one bichromatic path through
each shore, an odd cycle crossing the two shores, and on each side an actual
order-seven or order-eight separation or a boundary-full connected
component at the order-nine boundary.  When both endpoint traces are
surjective, the general two-shore incidence theorem instead gives an
alternating cycle of shore-supported bichromatic connections.  These
conclusions preserve the operated boundary vertex and the two colour
classes, but they do not align the remote path endpoints with the five
inherited branch-set labels.

If both shore-extension sets meet the four-or-five-colour subgraph, the
shortest path may be chosen there.  Every paired-rejected internal trace
then uses exactly four colours and leaves one common boundary-absent colour
in all lists on both kernels.  The finite theorem does not force this
endpoint condition.  The complementary low-palette case, in which one shore
attains at most three colours on `H`, remains part of the open gate.  If
`H` is four-chromatic, every trace already uses at least four colours and
the endpoint condition is automatic.  Thus the low-palette case occurs only
when `H` is three-colourable.

On a shortest transition in the four-or-five-colour subgraph, each edge
whose two ends are internal rejected traces transports the unique missing
colour.  The old hole becomes the operated vertex's new colour, while its
old uniquely carried colour becomes the new hole.  Consecutive internal
holes therefore differ.  In fact no such internal edge can survive on a
shortest opposite-shore path.  It is exactly a global transposition of the
old and new missing colours, so applying that transposition to the entire
remaining suffix removes one path edge while preserving the target shore
language.  Thus the shortest path has length at most two: it is one
oppositely owned move, or it has one four-colour trace rejected by both
shores.  The first and last transition edges still require host-level
analysis, but arbitrary transport chains and missing-colour cycles are
eliminated.

For a four-chromatic residual the distance is exactly one.  A deterministic
exhaustive check of all order-eight graphs proves that the surjective
five-colour equality-partition graph is connected whenever the residual is
`K_5`-minor-free and not three-colourable.  Each shore owns a surjective
trace, and ownership is invariant under colour-name permutations, so some
one-vertex quotient edge crosses between the two shore languages.  Hence
the common rejected four-colour trace can survive only when the residual is
three-colourable.

If one shore has no residual trace using four or five colours, choose a
maximum-palette trace with `p<=3` colours.  Splitting `5-p`
nonrepresentative vertices with the absent colours gives a Boolean response
cube.  A minimal face extending through the opposite shore is either a
one-vertex transition or has every proper nonempty face rejected by both
shores.  In the latter outcome each coordinate supplies a boundary-to-
boundary bichromatic path through each open shore.  When the residual is
three-chromatic this cube is a square; unless the colour-class sizes are
`(6,1,1)`, its two paths in each shore use disjoint colour pairs and are
therefore vertex-disjoint.  These paths still require literal first-hit
allocation to the inherited branch-set labels.

There is also a root-mobile restart family.  When the two open shores are
connected and boundary-full, `G[B-{s}]` is `K_5`-minor-free for every
literal `s in B`; otherwise a `K_5` model there together with the two shores
gives seven explicit branch sets.  Contracting either shore together with
`s` yields an exact-`{s}` trace through the opposite shore.  Hence every
boundary vertex supplies a full reconfiguration fork, and every pair of
boundary vertices occurs as two singleton classes in some full boundary
partition.  Colour-permutation-invariant abstract orientations show that
this pairwise overlap alone does not synchronize the shores.  A positive
use of root mobility must couple two roots through one literal host
operation, one shared first-hit configuration or one compatible separator.

One possible full-six reduction is now ruled out.  The graph of surjective
five-colourings under surjectivity-preserving component swaps can be
disconnected even for an eight-vertex `K_5`-minor-free graph carrying the
static forest, two prescribed edges, two added contacts and simplicial-root
data of this boundary.  Full single-vertex reconfiguration is nevertheless
connected at this order, so the obstruction is exactly the passage through
palette-deficient traces rather than the absence of all transitions.  The
orientation of those intermediate traces still requires an operation in the
seven-connected minor-critical host; boundary reconfiguration alone is
insufficient.

Nor do static exact-block queries determine that orientation.  On
`K_{2,6}` two disjoint abstract, colour-permutation-invariant families of
proper boundary partitions cover all full traces and each realize every
nonempty independent set as an exact block, yet their full-trace ownership
is constant on every surjectivity-preserving one-vertex component.  These
families are not asserted to be shore-realizable.  The example rules out
only a static partition-language proof and leaves operation-specific shore
responses as the required additional input.

Even isolated operation-specific responses are not sufficient.  There are
actual connected boundary-full shores over a nine-vertex boundary whose
disjoint extension languages each answer every independent exact-block
query.  Designated internal edge deletions and contractions on either shore
return all anchor traces from the opposite language, but no one-vertex
transition joins the two languages.  This realized barrier is
seven-chromatic, but it deliberately lacks the asserted combination of
seven-connectivity, global `K_7`-minor exclusion and six-colourability of
every proper minor.  Those host hypotheses must therefore enter the next
positive argument through a full-neighbourhood separator, a labelled
first-hit allocation or an explicit `K_7`-minor model; a collection of
operation witnesses cannot be treated as a connected response space.

The immediate order-eight theorem is therefore the following.  In the
minimum positive-excess boundary-full interface, with either two
complementary components or one of the audited 82 three-component boundary
types, use the selected proper-minor response and literal first-hit
locations to obtain one of:

1. two disjoint correctly rooted connected subgraphs meeting complementary
   sets of the five named branch sets and hence an explicit `K_7`-minor
   model;
2. an actual order-seven separation on which one complete labelled equality
   partition extends through both closed shores;
3. a strict full-neighbourhood-separator descent preserving the paired
   traces, selected boundary-edge response and every model label used by
   the claimed construction; or
4. the complete hypotheses of the audited cyclic-contact allocation
   theorem.

The two-component case now has an additional unbounded host-level
compression.  Seven prescribed response edges at a vertex in either open
component can be routed while prescribing the omitted boundary vertex; a
failure gives an actual order-seven response or a strict order-eight
crossing-edge response descent.  Independently, apply the all-boundary fan
theorem on both sides while retaining the two edges to one common boundary
vertex `p`.  Pairing the two fan tails through each member of `S-{p}` gives
seven disjoint connected columns, including when a fan limb is a direct
edge.  Together with the root sets `{v,p}` and `{w}` they form a
`K_2 join J` minor, where `J` is the literal seven-vertex column-contact
graph.  A `K_5` minor in `J` lifts to seven explicit branch sets, so every
such contact graph is `K_5`-minor-free in a survivor.  The columns need not
span the shores, and no connectedness of either side's induced contact
graph is asserted.

Choose one boundary vertex and adjacent centres in the two full open
components.  In the absence of an order-seven full-neighbourhood
separation, deletion of either centre leaves at most three components and
the two deletions leave at most five components altogether.  The
four-component case is excluded by an explicit `K_7`-minor construction;
this uses no bound on the component orders.  Thus the remaining component
count pairs are

\[
                    (1,1),(1,2),(1,3),(2,2),
\]

up to interchanging the shores.

The omitted `(2,3)` pair is now closed.  If one of its five components has
two neighbours at its deleted centre, a two-path Menger split gives either
an exact order-seven separation or seven explicit branch sets.  Otherwise
Dirac's neighbourhood-independence inequality and a complete
boundary-representative allocation give the seven branch sets directly.
The argument is unbounded in the component orders.

There is also a scalar obstruction in the branch where one boundary
colouring produces spanning vertex-minimal list-uncolourable kernels on both
nontrivial shores.  If `s` is their total order, `C` the total number of
boundary colours seen at shore vertices, `E` their total list-degree excess
and `h=|E(G[S])|`, then either a degree-seven singleton-side exact response
exists or

\[
                 s\ge24,
       \qquad E\ge2s+C+2h-48\ge C+2h.                \tag{8.20}
\]

Consequently the entire paired all-tight family is eliminated.  Positive
excess remains unbounded and (8.20) is not itself a branch-set allocation
or a common boundary colouring.

The remaining two-component theorem is therefore sharply response-coupled:
use the complete family of proper-minor nonextension witnesses to force a
`K_5` minor in one common literal column/contact system, a complete equality
partition extending through both shores of an actual order-seven
separation, or a strict generic selected-response descent.  Contact graphs
from unrelated fan systems cannot be pooled, and neither ordinary
connectivity nor one response colouring supplies this conclusion.

In the connected two-component opposite-response subbranch, the same target
can equivalently be entered through the two-part cover above.  Either the
two boundary-class-support families have a common transversal of order at
most two, giving an actual order-seven separation or a strict
root-preserving order-eight separation with the selected response retained,
or their role-sensitive transversal number `tau_XY` is at least three.  The
first alternative still needs opposite-shore state transfer before it is a
recursive or colouring conclusion.  The latter is the present host-level
exchange problem: use `K_7`-minor exclusion and a selected proper-minor
response to create the missing disjoint support, a saturated edge/`K_5`
completion, a common boundary partition, or a strict response-preserving
descent.

The two component counts should be treated uniformly up to the point where
the 82-type classification supplies additional boundary information.  A
palette colour is never a branch-set label, and an unlabelled fan or another
unlabelled near-clique model is not a terminal outcome.

The merged-response shore now has a sharper ordered normal form.  Every
connected subgraph adjacent to both nonadjacent roots meets both named
one-defect connected subgraphs, and every root-to-root path meets them in
the same order.  If the local root-to-root connectivity is one, the only
survivor is an exact one-vertex series composition with two lobes.  The two
lobe boundaries have opposite equality responses, while probing two
incident critical edges yields only an incompatible singleton-side
order-seven boundary or an unlabelled rooted `K_4`.  Neither outcome
allocates the old branch-set labels.

If the local root-to-root connectivity is at least two, the two named
one-defect subgraphs extend to an induced partition

\[
                         L=E\mathbin{\dot\cup}D
\]

into adjacent connected subgraphs, where `E` is adjacent to exactly
`S-{e}` and `D` to exactly `S-{d}`.  The three merged-root Kempe paths give
three distinct `d`-portals in `E`, and local two-connectivity gives at least
two `E-D` portals.  Two disjoint connected subgraphs of `E`, one meeting
the `d` and `D` portal classes and the other meeting three named boundary
portal classes, give seven explicit `K_7` branch sets.

A Hall reduction followed by Xie's two--three linkage theorem closes this
construction whenever the corresponding five-terminal completion is
six-connected.  Failure gives an actual order-seven separator, the existing
strict order-eight full-neighbourhood descent, or a connected proper set
`C subset E` with `|N_G(C)|>=9` and an operation-specific outer boundary
partition different from the fixed inner partition.  Completion order at
most six is not a separate case: the whole part `E` has exact boundary

\[
             N_G(E)=(S-\{e\})\mathbin{\dot\cup}(N_G(E)\cap D),
\]

so it yields the same strict order-eight descent or positive-excess response
obstruction.  The order-three portal classification is sharp: all static
layouts but one endpoint-reversal pattern give explicit `K_7` models,
whereas an exact finite example shows that the endpoint reversal, all three
Kempe paths and two `D`-side contacts can coexist without a `K_7` minor when
seven-connectivity and the rejected proper-minor response are omitted.

Thus the remaining constructive issue is no longer the existence of two
connected parts or of an unlabelled two--three linkage.  It is to use the
incompatible proper-minor boundary responses at the positive-excess side to
obtain a label-preserving split, a common complete boundary partition, or a
strict selected-response descent.  Ordinary uncrossing of symmetric low
cuts is insufficient without that colouring data.

The audited
[positive-excess component theorem](../results/hc7_order8_positive_excess_frozen_outer_shore.md)
now gives a complete component normal form.  Write

\[
 B=N_G(E)=(S-\{e\})\mathbin{\dot\cup}W,
 \qquad |W|\ge2.
\]

If a component of `G-B` other than `E` misses a vertex of `B`, its full
neighbourhood gives a response interface of strictly smaller boundary
order.  If there are two such complementary components in addition to
`E`, four connected boundary-full subgraphs and the triangle
`d x_d y_d d` give an explicit `K_7`-minor model.  Otherwise `G-B` consists
exactly of `E` and one connected component `C`.  Choosing two disjoint
connected `S`-full subgraphs of `C`, containing the prescribed `P_0,P_1`,
with maximum total coverage yields an induced adjacent partition

\[
                         C=Q_0\mathbin{\dot\cup}Q_1.
\]

For every boundary partition returned by deleting an `E-B` edge, the
literal required-set incidence graph between `Q_0,Q_1` and the nonsingleton blocks
has no saturating matching; each absent incidence is witnessed by a vertex
of `W`.  If both parts are `B`-full, every returned partition has demand at
least three.  Contracting an incident two-edge path `u-w-q`, with
`u in E`, `w in W`, `q in C`, gives either five-colour bichromatic
saturation at one incident edge or two coupled one-edge responses whose
boundary partitions differ.  At least one of the two switched components
meets `B-\{w\}`.  This closes every multiple-complementary-component case
and leaves one exact two-piece Hall-deficient response obstruction.

The
[rooted-partition contact-concentration theorem](../results/hc7_order8_rooted_partition_contact_concentration.md)
uses the literal ancestry of this interface to sharpen that obstruction.
In every connected partition `C=Q_0 dotcup Q_1` retaining `P_0,P_1`, the
part containing `e` contains all of `D-W` and is full to `B`, whereas the
other part lies in `R`, has exact boundary contact `S-{e}`, and misses every
vertex of `W`.  Consequently the isolated/crossed Hall alternative is
absent; at demand two both duties meet `W` and have the same unique owner.
Every component of `D-W` returns an exact order-seven response or a strict
boundary-order response descent unless it is full to
`(S-{d}) union W`, and two equality components give an explicit `K_7`
model.  Hence the final structural survivor has `D-W` empty or one connected
equality component.  The already-audited cycle-completion theorem makes
`G[S-{d,e}]` a forest.  This rules out improving the configuration by a
symmetric repartition: the remaining theorem must split the single
`e`-rooted owner using an operation-specific response, or synchronize a
complete boundary partition.

There is now an additional unbounded restriction on the enlarged boundary
`B`.  The two components `E,C` of `G-B` are anticomplete, connected and
`B`-full.  The double-cone vertex-deletion equivalence, together with the
fact that `d` has exact boundary neighbourhood `{x_d,y_d}` and
`x_dy_d` is an edge, shows that every hypothetical `K_5` model in `G[B]`
can be rerouted into `G[B]-d` and lifted with the two full components to an
explicit `K_7` model.  Consequently

\[
                    K_5\not\preccurlyeq G[B],
                    \qquad \chi(G[B])\le4.             \tag{8.18}
\]

This conclusion is independent of `|W|`.  It strengthens the previous
finite-order colourability statements, but it does not by itself align the
two closed-shore colourings.

The operation-specific response family is also explicit.  Contracting `E`
together with any nonempty independent set of `G[B]` makes that set one
exact boundary colour class on the `C`-side, rejected by the intact
`E`-side.  For the exact singleton class `{d}`, either one Kempe interchange
strictly decreases the number of boundary blocks or each eligible alternate
colour supplies a bichromatic path whose first internal vertex lies in
`R`.  If the sole nonempty component `D-W` has equality neighbourhood
`(S-{d}) union W`, the three supports `P_0,P_1,(D-W) union {e}` reduce every
demand-at-most-three Hall failure to one of the following literal patterns:

1. one required boundary set meets both `d` and `W`;
2. at least two required boundary sets meet `W`; or
3. the demand is three and all three required sets contain `d`.

The unresolved theorem must eliminate these concentrated patterns using
the associated proper-minor paths, produce a colour-compatible order-seven
separation, or give an explicit `K_7` model.  Static star-contraction traces
alone do not force any of those outcomes.

The boundary minor exclusion also supplies a canonical dynamic comparison
between the two closed shores.  For every nonempty independent set
`I subseteq B`, contracting one full shore together with `I` gives a
colouring of the opposite closed shore in which `I` is exactly the sixth
colour class.  Since `G[B-I]` is `K_5`-minor-free, all resulting labelled
five-colour boundary traces lie in one Kempe class while `I` stays fixed.

Apply this with `I={d}`.  A shortest path between the disjoint extension
sets of the two shores has the following exact dichotomy.

1. If its length is one, the same boundary two-colour component and colour
   pair are obstructed by a path through `E` and a path through `C`; their
   nonempty interiors are disjoint.
2. If its length is at least two, every internal boundary trace is rejected
   by both shores.  Under one such trace, each shore contains a connected
   induced vertex-minimal list-uncolourable subgraph.  For a vertex `v` of
   either subgraph `K`,

   \[
       d_K(v)\ge 6-
       |\phi(N_G(v)\cap B)|.                           \tag{8.19}
   \]

This fixed-block shortest-distance theorem is the canonical global
transition invariant available in the two-shore residue.  It does not yet
bound the full neighbourhood of either list-critical subgraph or allocate
the two obstruction paths to inherited minor-model labels.  The next
proof-closing theorem must use `K_7`-minor exclusion and the operation-
specific response to close one of these two outcomes.  Boundary structure
and shore fullness alone are insufficient: an audited counterexample has
disjoint extension languages under those static hypotheses, although it
deliberately contains an explicit `K_7` minor and is not contraction-
critical.

In the exact three-vertex endpoint-reversal pattern, the
[symmetric allocation theorem](../results/hc7_order8_strict_reversal_d_side_allocation.md)
and its
[small-side closure](../results/hc7_order8_strict_reversal_small_side_closure.md)
control the five portal sets on the opposite part.  Distinct
representatives and a six-connected completion give an explicit `K_7`
model; Hall failure gives a connected proper subgraph with boundary order
seven through nine.  The opposite part has order at least five.  At order
nine the Hall equality types reduce to a four-colourable boundary or
`K_2\vee C_7`, with the universal pair localized.  The unresolved cases
are the distinct-representative parts of orders five and six, compatible
transfer at the four-colourable order-nine boundary, and promotion of the
localized cyclic pair to a global terminal conclusion.

The audited
[transfer barrier](../barriers/hc7_order8_transfer_holonomy_barrier.md)
shows that connected-piece transfers do not canonically induce a
permutation on the named branch sets.  Their literal inheritance relation
is not a function; with anchored boundary-full parts the canonical label
action is the identity, while a centre/donor transposition is
convention-dependent.  A
permutation-only holonomy invariant is therefore unavailable.  The live
transition data are the literal portal ownership, required-set incidences and
proper-minor boundary responses displayed above.
Likewise, the
[symmetric-cut barrier](../barriers/hc7_symmetric_xie_positive_excess_uncrossing_barrier.md)
rules out obtaining the needed strict descent from neighbourhood
submodularity alone.

Within the three-component branch, the selected component may now be
assumed singleton or three-connected: induced-path overlap, cutvertices,
and the complete two-lobe two-cut normal form have been eliminated or
returned one of the previously displayed separator/descent outcomes.  The
two-component branch still requires label-preserving allocation inside one
connected shore; the componentwise gluing used in the two-cut completion
does not apply when the two full connected subgraphs are merely subgraphs
of that same shore.

The contracted five-chromatic branch has an independent split-planar
reduction: a spanning `\overline{P_7}` model leaves at least two empty
quotient bags and one collision bag unless six boundary contacts already
give an explicit `K_7`.  A fixed-root transfer is false, so the remaining
operation must globally reselect that model or return a compatible exact
separator.  This remains a secondary route.

Every recursive alternative must use a host-measured strict decrease and
retain the precise boundary partition and named branch sets it claims to
preserve.  The fixed compressed quotient and the finite boundary cases are
already exhausted.  One response colouring, an abstract response language,
shortest-path rerouting, or web structure without contraction-criticality
cannot supply the missing labelled allocation.

### Pentagonal-bipyramid column obstruction

The seven-column contact graph arising in the exceptional two-component
order-eight response has now been classified.  Unless a low-degree column
gives the previously listed separator or exchange outcomes, the sole
edge-maximal `K_5`-minor-free contact graph is the pentagonal bipyramid

\[
                         C_5\vee\overline {K_2}.
\]

Maximizing the seven columns makes them span the graph outside the two fixed
root branch sets.  The induced core `F` is four-connected, nonplanar, and
has chromatic number at least five.  A four-cut of `F` lifts to an actual
order-seven separation; compatibility of the two boundary colourings is
still open.  With no four-cut, `F` is five-connected.

Several unbounded expansion families are closed.  A four-distinct-label
alternating connected split gives an explicit `K_7` model.  Compatible
portal orders give a planar core for tree expansions, and the single-contact
tree and four-connected-column families therefore satisfy the exact
minor-or-six-colouring dichotomy.  A positive adjacent-rim Two Paths
instance and a suitable simultaneous two-column absorption also give
explicit `K_7` models.

The attempted converse based only on those local tests is false.  A
five-connected fourteen-vertex expansion has all five local linkage
instances negative and has no alternating column split, but is nonplanar;
it closes by a distributed multi-column `K_5` model.  A second example has
no `K_5` model containing five distinct whole columns, but is four-colourable
and has a `K_5` model whose every branch set meets both literal
root-neighbourhood sets.  An exact finite census proves that every
two-vertex-path column expansion satisfying the same negative tests is
four-colourable.  This is evidence for, not a reduction of, the unbounded
case.

The correct no-four-cut target is therefore the
[paired-rooted `K_5` dichotomy](hc7_pentagonal_bipyramid_paired_rooted_target.md):
either `F` is four-colourable or it has a `K_5` model whose every branch set
meets both root-neighbourhood sets.  The latter model joins the two fixed
roots to give `K_7`; the former six-colours the host.  Five such two-sided
connected subgraphs may now be chosen to partition all of `F` while
maximizing their contact graph.  What remains is to prove that a missing
contact in this spanning five-part normalization forces the four-colourable
planar-expansion alternative, an exact colour-compatible order-seven
separation, or a new paired-rooted contact.

The positive model requirement has also been weakened.  It is enough that
all five `K_5` bags meet one root-neighbourhood set and at least four meet the
other: the resulting one-defect `K_7` model gives `K_7` or a genuine
full-neighbourhood separation.  In the exact type-5 enlargement census this
closes 320 of the 340 paired-rooted-negative endpoint assignments.  The 20
remaining assignments are precisely doubly confined at the retained-edge
sides of both split fibres.  This is the sole finite type-5 label residue,
but it is not a host-level closure: the returned separation is not bounded
above by seven and its two closed-shore colourings are not synchronized.

Persistent conforming planar reroutings are accordingly part of the
prospective colourable outcome, not another obstruction to enumerate.
The available enlargement and mold theorems do not yet close the argument:
the former loses the selected root labels, while ordinary root-to-column
adjacency does not provide the feasible cast required by the latter.

### Generic exact-seven restart and the remaining terminal theorem

The generic restart theorem gives a simpler well-founded spine.  At any
actual order-seven separation with a selected boundary-to-shore edge
deletion response, either the connected operated shore is a singleton, or
the selected edge can be retained and paired with a second vertex-disjoint
entrance edge.  The resulting two-root list-critical core gives one of:

1. a strictly smaller generic exact-seven selected-response interface;
2. a proper core with full-neighbourhood order at least eight; or
3. a shore-filling two-root list-critical obstruction.

Consequently old five-plus-two vertices and old near-clique labels are not
part of the recursion invariant.  They remain useful only for a particular
explicit minor-model construction.

The exact open theorem is now the following.  In a minimum-order generic
exact-seven selected-response interface, eliminate the singleton,
separator-excess and shore-filling outcomes by producing either an explicit
`K_7`-minor model or an actual order-seven separation whose two closed
shores realize one common complete equality partition.  Equivalently, any
nonterminal operation must return a strictly smaller generic interface.

The terminal modes have now been sharpened as follows.

In the original degree-seven tight-pole instance, an internal articulation
in either of two disjoint matching layers already gives the strict restart
unless its smaller side has boundary at least eight.  If there is no such
articulation, that layer has two internally vertex-disjoint root-to-root
routes.  The next intermediate response lemma should select an edge on a
nonseparating route and couple one proper-minor response simultaneously to

1. a prescribed boundary matching containing `e_0,e_i`; and
2. a label-compatible incidence or allocation in the fixed `U`-rooted
   `K_5` model,

or else give an explicit `K_7` model, a common boundary partition, or a
strict order-seven descent.  Preserving the matching alone is nonterminal,
and no such model-label coupling has yet been proved from the route
geometry.

1. In the singleton mode, cutvertices and bridges return exact order-seven
   interfaces; the surviving opposite exterior is nonbipartite and
   two-connected.
2. In the proper-core mode, a minimum positive-excess separator either
   returns an exact order-seven generic interface not known to be strict,
   or has order at least eight with exactly two or three boundary-full
   complementary components.  At order eight the non-singleton components
   lie in the all-boundary-fan/label-allocation problem above.  In the
   branch-set-contained labelled subcase a non-singleton component already
   returns an exact order-seven separation, leaving the degree-eight
   singleton; this containment has not been proved for every component.  In
   the ordered positive-excess subbranch, every instance with more than one
   complementary component now descends or gives an explicit `K_7` model.
   The exact survivor has one connected opposite component partitioned into
   two adjacent boundary-full pieces, with every operated response failing
   the corresponding required-set Hall matching.  In the endpoint-reversal
   subcase the opposite part has order at least five; the remaining bounded
   distinct-representative cases have orders five and six, while Hall
   failures have boundary order seven through nine.  In the two-component
   order-eight subbranch, paired prescribed fans, centre deletion and the
   paired excess inequality further reduce every survivor to one of the
   four component-count pairs displayed in (8.20)'s preceding paragraph,
   with a `K_5`-minor-free common column-contact graph and strictly positive
   spanning list-degree excess.  The operation-specific response families
   are not yet synchronized.
3. In the shore-filling mode, every all-tight core with at least two Gallai
   blocks is eliminated by the uniform defect-two reflection theorem.  The
   all-tight residue consists only of the bounded one-block `K_4,K_5`
   cases; positive total list-degree excess remains unbounded.

The tempting contracted-terminal fan proof does not establish this theorem.
A cut in a graph in which branch sets have been contracted counts connected
objects, not literal separator vertices; a branch-set preimage may expose
arbitrarily many vertices.  Contracting a connected kernel also does not
give five prescribed-port paths disjoint outside one root.  On the colouring
side, a positive-excess list-critical core need not be a Gallai tree,
Kempe-minimality gives pairwise support rather than a unique boundary
partition, and edge pruning lowers fixed-list excess without shrinking the
host shore.  Any successful terminal theorem must spend the actual
`K_7`-minor exclusion and all operation-specific proper-minor responses at
one of the three literal host configurations above.

## Dependencies

- [positive boundary excess reduces to one partitioned opposite shore](../results/hc7_order8_positive_excess_frozen_outer_shore.md)
- [rooted connected partitions concentrate the enlarged-boundary contacts](../results/hc7_order8_rooted_partition_contact_concentration.md)
- [symmetric two--three allocation in the endpoint-reversal case](../results/hc7_order8_strict_reversal_d_side_allocation.md)
- [small-side closure and Hall-response reduction in the endpoint-reversal case](../results/hc7_order8_strict_reversal_small_side_closure.md)
- [connected-piece transfers do not canonically induce permutation holonomy](../barriers/hc7_order8_transfer_holonomy_barrier.md)
- [symmetric positive-excess cuts do not uncross by neighbourhood submodularity](../barriers/hc7_symmetric_xie_positive_excess_uncrossing_barrier.md)

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
- [excess-one descent with literal boundary data](../results/hc7_epsilon_one_labelled_descent.md)
- [four full components close an order-eight boundary](../results/hc7_full_order8_four_component_closure.md)
- [three-component order-eight boundary classification](../results/hc7_order8_three_component_boundary_classification.md)
- [Kempe transitions across full order-eight components](../results/hc7_order8_full_component_kempe_transition.md)
- [prescribed spokes or a coloured exact-seven separator](../results/hc7_order8_prescribed_spoke_reduction.md)
- [minimal contracted-edge `K_6` model](../results/hc7_contracted_edge_k6_model_normalization.md)
- [fresh-colour disjoint linkages and augmented-boundary transition](../results/hc7_exact7_fresh_colour_linkage.md)
- [contracting an augmented full-component interface](../results/hc7_augmented_full_component_contraction_reduction.md)
- [the contracted five-chromatic boundary and split-planar normal form](../results/hc7_contracted_five_chromatic_boundary.md)
- [a critical exact-seven boundary edge gives a fan or strict component descent](../results/hc7_exact7_critical_edge_fan_descent.md)
- [opposite-shore obstruction paths for one boundary Kempe transition](../results/hc7_opposite_shore_single_kempe_transition.md)
- [shortest boundary Kempe distance gives paths or two list-critical subgraphs](../results/hc7_two_shore_kempe_list_dichotomy.md)
- [fixed-trace list-critical transfer](../results/hc7_boundary_list_critical_transfer.md)
- [single-portal amplification and a deletion-persistent model edge](../results/hc7_single_portal_amplification.md)
- [persistent model-edge alignment with a fixed boundary trace](../results/hc7_persistent_edge_fixed_trace_alignment.md)
- [rooted incident-edge persistence with a protected singleton](../results/hc7_rooted_persistent_model_edge.md)
- [persistent incident edges with several protected singleton branch sets](../results/hc7_multi_protected_persistent_model_edge.md)
- [jointly persistent incident edges or an exact order-seven separation](../results/hc7_joint_persistent_edge_or_exact_seven.md)
- [persistent-edge support classes and the dense-alternative degree bound](../results/hc7_persistent_support_class_refinement.md)
- [colouring fork for a jointly persistent incident pair](../results/hc7_joint_persistent_incident_colour_fork.md)
- [maximum deletion capacity at a deficient singleton](../results/hc7_deficient_singleton_joint_persistence.md)
- [branch-set split aligned with a common two-edge deletion](../results/hc7_split_aligned_joint_deletion.md)
- [Kempe-separated responses at a critical triangle](../results/hc7_critical_triangle_kempe_separation.md)
- [clique-star response transition or higher-chromatic connected subgraph](../results/hc7_clique_star_kempe_separation.md)
- [full-subgraph demand at an exact-seven transition](../results/hc7_exact7_critical_triangle_full_subgraph_demand.md)
- [demand-set reflection and strict full-neighbourhood descent](../results/hc7_exact7_demand_set_separator_descent.md)
- [simultaneous direct-entry contraction and two-root list-critical descent](../results/hc7_direct_entry_two_edge_list_core.md)
- [surplus-sensitive density at an exact seven-boundary](../results/hc7_direct_entry_surplus_density.md)
- [tight-shore order bound](../results/hc7_tight_shore_order_bound.md)
- [Rado--gammoid criterion for labelled first-hit paths](../results/hc7_labelled_first_hit_rado_reduction.md)
- [rainbow first-hit linkage to a partitioned minimum boundary](../results/hc7_literal_boundary_rainbow_linkage.md)
- [rank defect gives a tight separator or a repeated literal exposure](../results/hc7_labelled_first_hit_exposure_collision.md)
- [compression of repeated labelled exposure](../results/hc7_labelled_first_hit_exposure_compression.md)
- [fixed-partition alternatives for two persistent edges](../results/hc7_repeated_exposure_fixed_trace_fork.md)
- [boundary-forced Kempe locks](../results/hc7_paired_boundary_forced_kempe_locks.md)
- [paired-boundary partial-switch calculus](../results/hc7_paired_boundary_partial_switch_calculus.md)
- [exact selected-partition preservation at a seven-separator](../results/hc7_exact7_selected_response_preservation.md)
- [two-contact label-preserving branch-set transfer](../results/hc7_response_aligned_two_contact_lobe_transfer.md)
- [reserved-component linkage completion and three-label order-eight normal form](../results/hc7_reserved_component_linkage_completion.md)
- [three-owner component concentration and two-edge response substrate](../results/hc7_three_owner_reserved_component_concentration.md)
- [the concentrated three-owner order-eight configuration is impossible](../results/hc7_three_owner_concentration_elimination.md)
- [operation-specific normal form at the resulting special five-plus-two exact-seven boundary](../results/hc7_special_five_plus_two_exact7_response.md)
- [two boundary vertices give a singleton shore or a two-root list-critical core](../results/hc7_special_exact7_two_edge_list_core.md)
- [a bridge in the bipartite-boundary thin shore gives a strict exact-seven response descent](../results/hc7_exact7_bipartite_bridge_response_descent.md)
- [density and block structure in the special shore-filling list-critical core](../results/hc7_special_shore_filling_density.md)
- [fixed-trace responses at every internal edge of the shore-filling core](../results/hc7_fixed_trace_internal_edge_dichotomy.md)
- [six almost-boundary-complete neighbours force a `K_7` minor](../results/hc7_six_spoke_boundary_completion.md)
- [a selected response pulls back through a retained exact-seven boundary](../results/hc7_special_exact7_selected_response_pullback.md)
- [generic selected-response restart at every exact order-seven core boundary](../results/hc7_generic_exact7_response_restart.md)
- [relative eight-connectivity of a minimum exact-seven response shore](../results/hc7_minimum_generic_exact7_relative_connectivity.md)
- [minimum positive-excess separator: exact-seven restart or two/three full components](../results/hc7_minimum_positive_separator_normal_form.md)
- [boundary-full order-eight response: clean fan or generic exact-seven restart](../results/hc7_order8_clean_fan_or_generic_restart.md)
- [common-label paired paths at a boundary-full order-eight separation](../results/hc7_order8_common_label_paired_fan.md)
- [all eight boundary vertices from a connected source, or an exact order-seven separation](../results/hc7_order8_all_boundary_source_fan.md)
- [exact rooted split and critical-edge normal forms for an induced-path component](../results/hc7_order8_overlapping_interval_normal_form.md)
- [completion of every overlap outcome for a nontrivial induced-path component in the exact three-component interface](../results/hc7_order8_endpoint_shared_portal_completion.md)
- [leaf-block descent for a selected order-eight component with a cutvertex](../results/hc7_order8_leaf_block_descent.md)
- [small-boundary lobe descent and the defect-one two-cut residue](../results/hc7_order8_small_boundary_lobe_descent.md)
- [triangle-transversal structure of the remaining two-cut residue](../results/hc7_order8_two_cut_triangle_transversal.md)
- [low-connectivity reduction for a singleton selected component](../results/hc7_order8_singleton_low_connectivity_reduction.md)
- [reserved path and boundary-block subgraphs realize both root responses](../results/hc7_order8_three_block_linkage_reflection.md)
- [opposite colouring responses forced by the exact two-lobe residue](../results/hc7_order8_two_cut_opposite_response.md)
- [completion of the exact two-lobe two-cut residue](../results/hc7_order8_two_cut_completion.md)
- [six-label branch-set-contained component reduction to an exact order-seven separation or a degree-eight singleton](../results/hc7_order8_six_label_donor_fan_reduction.md)
- [lost-label obstruction at the degree-eight singleton](../results/hc7_order8_singleton_label_obstruction.md)
- [four boundary-full connected subgraphs and a boundary triangle give a `K_7` minor](../results/hc7_four_boundary_full_subgraphs_triangle_completion.md)
- [three opposite-shore edge probes eliminate simultaneous five-chromatic saturation](../results/hc7_three_edge_owner_saturation_elimination.md)
- [paired-source path transfer or exact order-seven separation](../results/hc7_paired_source_path_transfer.md)
- [componentwise exchange at a forced boundary path](../results/hc7_componentwise_path_residual_exchange.md)
- [uniform defect-two reflection on all residual seven-boundaries](../results/hc7_exact7_all_residual_defect2_carrier.md)
- [closure of every all-tight multiblock exact-seven shore](../results/hc7_all_tight_block_path_internal_segment_closure.md)
- [singleton exact-seven terminal normal form](../results/hc7_singleton_exact7_terminal_normal_form.md)
- [two-shore Kempe-incidence bridge criterion](../results/hc7_two_shore_kempe_incidence_cycle.md)
- [two independent critical edges: opposite-shore placement or rooted four-terminal model](../results/hc7_two_edge_opposite_shore_or_rooted_k4.md)
- [Kempe-minimal boundary traces have pairwise bichromatic support](../results/hc7_kempe_minimal_boundary_trace.md)
- [the singleton-shore exterior is nonbipartite](../results/hc7_singleton_shore_nonbipartite.md)
- [exact completion classification for two connected subgraphs at a near-complete six-branch-set model](../results/hc7_five_contact_completion_classification.md)
- [endpoint-`K_4` transfer or an actual order-seven separation](../results/hc7_endpoint_k4_transfer_or_order7.md)
- [distinct-boundary prescribed-spoke transfer](../results/hc7_distinct_boundary_spoke_owner_transfer.md)
- [operation-coupled colouring responses at a boundary-full order-eight separation](../results/hc7_operation_coupled_order8_response.md)
- [repeated contacts and component defect](../results/hc7_repeated_contact_component_defect.md)
- [opposite-shore critical edges give a rooted four-vertex model or exact seven-separation](../results/hc7_cross_shore_critical_edge_linkage.md)
- [label-preserving absorption of a five-contact rejection component](../results/hc7_five_contact_rejection_component_absorption.md)
- [one-extra-colour critical kernel at a boundary edge](../results/hc7_one_extra_colour_boundary_kernel.md)
- [boundary-crossing persistent-edge reduction](../results/hc7_boundary_crossing_persistent_edge_reduction.md)
- [total rejection of a fixed boundary trace](../results/hc7_total_trace_rejection_kernel.md)
- [aligned two-edge bypass or labelled donor separation](../results/hc7_aligned_two_edge_bypass_separator.md)
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
- [static first-hit colours need not allocate distinct model labels](../barriers/hc7_joint_pair_first_hit_hall_barrier.md)
- [critical-triangle responses can remain Kempe-separated](../barriers/hc7_critical_triangle_kempe_separation_barrier.md)
- [clean bichromatic-path geometry alone does not force a clique minor](../barriers/hc7_exact7_clean_path_geometry_barrier.md)
- [the direct bichromatic-path/full-subgraph obstruction at connectivity six](../barriers/hc7_exact7_bichromatic_path_full_subgraphs_barrier.md)
- [a common-label paired fan is not terminal without dynamic response data](../barriers/hc7_common_label_paired_fan_k7_barrier.md)
- [same-shore edge responses and six-colourable closed shores need not synchronize](../barriers/hc7_exact7_crossing_disjoint_languages_barrier.md)
- [stable-theta/three-path matching-defect barrier](../barriers/hc7_stable_theta_three_path_matching_barrier.md)
- [paired-block exact-trace parity barrier](../barriers/hc7_exact7_paired_block_trace_parity_barrier.md)
- [boundary-local operation parity barrier](../barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md)
- [first-entry geometric-minimality barrier](../barriers/hc7_first_entry_packet_minimality_barrier.md)
- [missing fifth far-side contact barrier](../barriers/hc7_three_path_missing_five_row_barrier.md)
- [persistent edges need not have tight endpoints](../barriers/hc7_persistent_edge_tight_endpoint_barrier.md)
- [seven-connected static alignment still need not give tight endpoints](../barriers/hc7_persistent_edge_tight_endpoint_shadow.md)
- [three persistent edges need not have two nonadjacent outer endpoints](../barriers/hc7_persistent_induced_star_barrier.md)
- [seven-connectivity and `K_7`-minor exclusion do not bound first-hit exposure](../barriers/hc7_labelled_first_hit_k2_planar_exposure_barrier.md)
- [a fixed response can rotate between repeated contacts](../barriers/hc7_fixed_trace_edge_rotation_barrier.md)
- [two same-branch-set critical edges do not allocate labels](../barriers/hc7_same_bag_two_critical_edges_exact7_barrier.md)
- [repeated contacts need not lower component defect](../barriers/hc7_repeated_contact_component_defect_barrier.md)
- [split-planar `\overline{P_7}` model-reselection reduction](hc7_split_planar_pbar7_reduction.md)
