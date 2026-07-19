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

The first-hit rank therefore leaves one precise label-faithful step.  Every
internal owner-portal obstruction has now been converted into an incident
differently labelled edge pair, a repeated model-preserving edge pair, or
an actual separator of order seven through ten.  In the rooted-`K_4`
outcome,
three inherited branch sets must still be reserved as named completing
branch sets.  In the separator outcome, the retained named supports must
satisfy the Hall duty inequalities for one legally transported partition.
The two partitions transported automatically by the opposite colouring
chambers are incompatible.  What is missing is the operation-coupled theorem
which converts excess exposure at the internal transversal into one of
those two exact certificates.

The immediate theorem must close one of the following four literal forks,
with the first-hit rank providing the primary mechanism.

1. **Owner-circuit dynamic closure.**  Apply the operation-specific
   colouring at the incident differently labelled pair, repeated
   model-preserving pair, or returned order-seven-through-ten separator.
   Prove that it gives a new named first hit, a strict compatible model
   reduction, an exact-seven descent, or a new opposite-shore support which
   violates the displayed Hall deficiency.  In the reserved-component
   normal form it is enough to reroute one proper-subfamily linkage away
   from the reserved component, leave a connected six-contact residual after
   the linkage, or return one compatible exact-seven boundary partition.
2. **Minimum oriented interface.**  At the minimum two-full-component
   boundary, eliminate a boundary-edge pinch, lower separator excess to
   zero while retaining the opposite response partitions, or split the
   two full components into correctly labelled branch sets.
3. **Exact order seven.**  In the demand-three residue, combine the forced
   bichromatic path with the two boundary-full connected subgraphs to meet
   the three exact demand sets, or extend one boundary partition through
   both closed shores.  Merely obtaining another unlabelled separator is
   not terminal.
4. **Dominating bounded-chromatic subgraph.**  Use the surviving labelled
   near-complete model and proper-minor responses to split a connected
   dominating bipartite, three-chromatic or four-chromatic subgraph into
   the missing named branch sets, or return one of the preceding separator
   outcomes.

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
