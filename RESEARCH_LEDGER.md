# $HC_7$ research ledger

**Last updated:** 19 July 2026
**Authoritative status:** $HC_7$ is not proved here.

This file records the current mathematical dependency chain. The concise
list of live files is [`active/INDEX.md`](active/INDEX.md), and the current
technical statement is
[`active/hc7_degree7_model_separator_frontier.md`](active/hc7_degree7_model_separator_frontier.md).
If an archived note conflicts with this ledger, this ledger governs the
current programme. The balanced order-eight, two-root, and support-six
sections retain developed dependency chains but are not by themselves the
current engine.

## Current strategic frontier: degree-seven boundary-labelled near-clique composition

The bounded-interface entry theorem is global.  Every hypothetical minor-minimal
counterexample contains a vertex `u` of degree seven, eight, or nine and a
component `C` of `G-N[u]` whose full boundary `S=N(C)` has order seven,
eight, or nine.  The boundary is four-colourable, has independence number
at most four, and both closed shores realize every nonempty independent
subset of `S` as an exact boundary colour block.  Contracting `C` also
shows that `overline(K_2) join G[S]` is a `K_7`-minor-free minor.

The adjacent-pair colouring can be aligned with this same interface.  At
least seven neighbours of `u` meet the exterior.  If all those incident
edges were double-critical, those neighbours would have at least five
neighbours in `G[N(u)]`; every remaining neighbour has at least six there
because it has no exterior neighbour.  The audited degree-seven/eight/nine
local completion then gives a `K_7` minor.  Hence one may choose

\[
 z\in S,\qquad \chi(G-\{u,z\})=6.
\]

Every six-colouring of the edge deletion `G-uz` makes `u,z`
monochromatic.  On the `C`-shore it gives an exact singleton boundary
block `{z}`; its complete equality partition cannot extend through the
opposite original shore.  At degree seven this normalizes to one boundary
nonedge of the other six vertices and four further singletons.

Two unbounded branches are now closed.  If `G[S]` is split, exact-block
attainability forces both shores to realize the unique partition consisting
of the independent part and singleton clique vertices, so they glue.  This
is sharp at the static level: every nonsplit four-colourable boundary has
an abstract even/odd partition-language obstruction.  Separately, if the
boundary has an adjacent pair complete to a two-connected remainder and
the two open shores are connected and full, Martinsson--Steiner's rooted
`K_4` planarity lemma gives either an explicit `K_7` model or a planar
embedding after deleting the pair, contradicting the required `K_5`
minor.  This strictly generalizes the earlier induced-cycle completion
theorem.

The remaining nonsplit case now carries literal paths rather than only
abstract colour responses.  For every `x in S`, the exact-singleton
boundary cylinder is Kempe-connected: after deleting `x`, the boundary is
four-degenerate by Mader's density bound, and Las Vergnas--Meyniel applies
with five colours.  Starting from a six-colouring of the edge deletion
`G-ux` and lifting a boundary Kempe sequence toward an opposite-shore
colouring, the first failed lift gives a bichromatic path avoiding `u,x`.
Its interior lies wholly in one open shore.  On the `u`-side it traverses
at most three other components of `G-N[u]`, each adjacent to all but at
most two vertices of `S`.

At degree seven the interface is now substantially sharper.  A new audited
composition of the exact-seven packet theorems proves that `G-N[u]` is one
nonempty connected component `C`.  Hence

\[
                    S=N(u),\qquad A=G-u,
                    \qquad B=G[N[u]].
\]

Dirac's inequality makes every boundary colour class a singleton or a pair.
Writing `F=overline{G[S]}`, the two extension languages are exact:

\[
 \mathcal M(A)=\{\{e\}:e\in E(F)\},\qquad
 \mathcal M(B)=\{M:M\text{ is a matching of }F, |M|\ge2\}.
\]

Thus any chosen nonedge `ab` is the sole repeated pair in one six-colouring
of `A`; the remaining five boundary roots have five distinct colours.  In
that same colouring every missing root adjacency has a bichromatic path
through `C`, with paths for disjoint missing edges vertex-disjoint.  After
restricting to the five relevant colour classes, Kriesell--Mohr's Theorem 7
packages this system into a rooted `K_5`, uniformly for every `ab` and
without Moser labels.

The reserved-connector dichotomy is also audited.  Either the rooted model
and an `a-b` connector give an explicit `K_7`-minor model, or the five named
bags contain a minimal `a-b` separator `Z` of order at least six.  Both
distinguished components are full to `Z`, one bag is hit twice, and
`Z union {u}` is an actual full separation boundary in `G`.  More sharply,
either an exact full order-seven separation occurs or seven internally
vertex-disjoint `a-b` paths all traverse the five rooted bags.

The boundary graph and rooted models now admit a uniform further
compression.  The nonisolated part of `F` is one two-connected component on
six or seven vertices.  A degree-two vertex of that component gives a
boundary-labelled `K_7^-` model.  If no such vertex exists, then

\[
              F\cong K_{3,4}
       \quad\text{or}\quad
              F\cong K_{3,3}\mathbin{\dot\cup}K_1,
\]

and explicit rooted branch sets give a model of `K_7` with at most two
missing adjacencies, both incident with one singleton boundary vertex.
Thus every degree-seven survivor has a boundary-labelled model of `K_7^-`
or of `K_7` with two adjacent edges deleted.  This theorem is written and
separately audited; it is stronger than merely regenerating an unlabelled
near-clique minor.

For positioning, Norin and Totschnig proved that every graph with no
unlabelled `K_7`-minor with two adjacent edges deleted is six-colourable
([arXiv:2507.03244](https://arxiv.org/abs/2507.03244)).  The contribution
used here is therefore not first
existence of that unlabelled minor; it is the singleton-centre and boundary-
root alignment, exact matching-language provenance, and the stronger
one-missing-edge outcome in part of the degree-seven branch.

Three further audited theorems now close the static one-hole splitting
step.  First, the aligned model may be made spanning while retaining its
singleton pole, singleton centre and named boundary roots.  Proper-minor
matching responses apply to every edge with an endpoint outside the closed
pole shore, and a degree-two complement vertex gives two opposed
centre-preserving orientations.  Spanning absorption does not preserve
colour purity or provide a bag-size rank.

Second, a parameter-uniform two-mark branch-set theorem applies to any
spanning labelled `K_t^-` model.  If one common bag contains two neighbours
of the singleton centre, a marked tree cut gives either an explicit `K_t`
model or the full neighbourhood of a proper connected subbag as an actual
separation.  At `t=7`, minimum degree seven distributes at least seven
centre neighbours over only five common bags, so a multiply-hit bag is
automatic.  Therefore every spanning aligned one-missing-adjacency model
gives a `K_7` minor or an actual full-neighbourhood separation.

Third, a five-row reflection theorem works across a boundary of arbitrary
order.  If five pairwise adjacent connected rows on one closed shore cover
the boundary apart from the centre, then any far-shore six-colouring whose
intersection with each row is monochromatic reflects through the other
shore, provided the centre colour occurs in a row or some row misses the
boundary.  The proof constructs one connected carrier per equality block
inside the far shore and colours the resulting proper minor.

Together these results replace the proposed centre-to-deficient-bag
shortest-path programme.  That path rank is universally degenerate because
the pole gives the absolute-minimum path `c-u-b`, and every path leaves the
centre through a common bag.

The marked-tree split now has a single audited separator outcome.  In both
orientations, merging the deficient bag with the opposite donor part gives
five pairwise adjacent connected subgraphs on the far shore, all adjacent
to the boundary centre and covering the rest of the full neighbourhood.
In the non-`K_7` case at least one is boundary-free.  The five-row
reflection theorem therefore implies that every proper six-colouring of
the unchanged far closed shore multicolours at least one nonempty named
row intersection.  Simultaneous losses do not create a third geometric
case.

In the protected-root orientation of the old double-loss configuration,
ownership makes five literal boundary vertices common anti-neighbours of
the protected root.  Dirac's independence bound makes them a `K_5`, and
the connected full exterior gives an explicit `K_7` model.  The opposite
orientation is already included in the universal multicoloured-row
separator.

A second audited theorem gives the first dynamic compression of this
obstruction.  Suppose every row intersection is independent.  Form the
conflict graph on nonsingleton row intersections, joining two when a
boundary edge runs between them.  If the other open shore contains `k`
pairwise disjoint connected subgraphs each adjacent to every boundary
vertex, and the conflict graph is `k`-colourable, simultaneous connected
contractions produce an unchanged-far-shore colouring in which every row
intersection is monochromatic.  Five-row reflection then six-colours `G`.

At an exact order-seven boundary, a first nontrivial independent-trace
subcase contains two disjoint two-vertex traces.  A new audited theorem
closes this subcase whenever the two traces have vertex-disjoint connected
realizations through the other open shore: contract both realizations and
apply five-row reflection.  If no such linkage exists, rooted internal
four-connectivity and the Two Paths theorem give a genuine disk drawing
with the four roots alternating.

The disk alternative has now been compressed by a second unbounded audited
theorem.  When its open side has at least two vertices, it gives either an
explicit `K_7` model or two nested full-neighbourhood separators.  The
smaller connected set is a proper tree part of one paired far-side branch
set.  Expanding it by the corresponding rooted disk bag gives a second
connected set containing exactly one nominated boundary root and missing
one named residual branch set.  Both separator boundaries have order at
least seven.  This preserves substantially more host-level information
than the old abstract web description, but neither separator is known to
have order exactly seven or compatible shore colourings.

The same theorem package supplies two further constraints.

- Euler curvature in the four-root disk yields a host vertex of degree
  seven or eight.  In the degree-eight equality it has five disk neighbours
  and all three omitted boundary vertices as neighbours.
- Every nonextendable far-side six-colouring which is nonconstant on the
  four roots forces a disk vertex adjacent to two differently coloured
  omitted boundary vertices.  Proper star contractions and boundary-edge
  deletions therefore create literal contact transitions.

A separate audited degree-eight contact-allocation theorem closes a broad
equality family.  If a connected seventh branch set meets at least seven of
the eight labels around `v`, five cyclic connected sets contain the five
neighbours of `v`, and the missing adjacencies from the three omitted
boundary vertices to those five sets form a matching of order at most two,
then an explicit finite table gives six disjoint pairwise adjacent branch
sets meeting the seventh.  Hence `G` has a `K_7` minor.  A three-connected
plane graph supplies the cyclic connected sets from the facial cycle
exposed by deleting `v`, provided that cycle is disjoint from the proposed
seventh branch set.

Four further audited results compress the reservation and contact
obstructions.

- Deleting at most three vertices leaves every prescribed five-set on one
  cycle.  A failure would create an actual order-seven separation with at
  least five disjoint boundary-full connected subgraphs, contradicting the
  exact-seven packet bound.
- After deleting a chosen exterior component, the three omitted boundary
  vertices and the degree-eight centre, a three-connected residue contains
  a cycle through the five disk neighbours.  Otherwise a separator of order
  at most two either lifts to an actual order-seven full-neighbourhood
  separation or has one component containing at least `5-|Z|` nominated
  neighbours and no second component containing an off-neighbour vertex.
- In the rooted internally four-connected disk itself, adding one
  outer-face vertex complete to the four roots gives a four-connected
  planar graph.  Four internally disjoint paths from the new vertex to the
  degree-eight centre can be made stable in Tutte's sense.  The paths use
  all four roots and four of the five disk neighbours, while the bridge
  containing the fifth neighbour attaches to both paths bounding one
  sector.  Together with the outer root cycle this always gives five
  pairwise-disjoint cyclically adjacent connected sets, containing all five
  neighbours and placing the four roots in four distinct sets.  Thus both
  clustering patterns left by the Hamiltonian-cycle reduction are closed,
  including arbitrary overlap between roots and disk neighbours.
- Two distinct safe supports for the paired traces force five-row
  reflection.  For the four normalized concentrated contact patterns, the
  complete obstruction is a short Boolean list of literal boundary edges.
- Contracting the two connected supports in the original graph and deleting
  the whole obstructing boundary-edge set only in the pulled-back far-shore
  colouring forces at least three absent-colour Kempe components from the
  selected boundary vertex back to the paired trace.  All three paths come
  from one colouring.  When the obstructing set is one edge, deleting and
  contracting that same edge yield the same colouring space, not two
  independent states.
- Terminal-capacitated Menger applied to those three connections gives an
  exact host-level dichotomy.  Either three boundary-to-trace paths are
  disjoint outside their prescribed terminals, or a connected open-shore
  set has a full neighbourhood of order exactly seven.  In the latter case
  the original colouring restricts properly to that closed shore and gives
  a concrete boundary partition: the opposite paired trace is
  monochromatic and the selected boundary vertex shares its colour with a
  new two-cut vertex.  Extending that same partition through the other
  closed shore remains open.
- Low connectivity in a boundary-full component is completely explicit.
  A cutvertex yields either an actual order-seven boundary or a repair
  support disjoint from a boundary-full residual.  A two-vertex separator
  has an exact necessary-and-sufficient contact criterion, with all
  two-lobe and multi-lobe exceptions classified; a unique boundary portal
  also yields an exact order-seven boundary.  This does not preserve the
  already named far-side connected subgraphs or a boundary colouring, so
  the positive allocation problem is concentrated in the three-connected
  component case and the listed contact-concentration exceptions.
- A three-connected component containing one vertex adjacent to all seven
  boundary vertices also closes.  Tutte's nonseparating-path theorem gives
  a repair path avoiding that vertex whose deletion leaves a connected,
  automatically boundary-full residual.  Endpoint degeneracies give a
  one-vertex repair support or an actual order-seven separation.  Thus a
  surviving unrestricted component has no universal boundary-contact
  vertex, apart from the separate named-subgraph preservation obligation.

An additional audited conditional theorem closes the incidence problem
once three boundary-rooted far-side connected subgraphs are disjoint from
the connected seventh branch set.  Matching defects and defects confined to
the unrooted fifth cyclic connected set give explicit `K_7` models.  If a
selected rooted missing incidence has its far-side connected subgraph
meeting the open shore, it gives an exact order-seven separator or a strict
decrease in the order of a literal full-neighbourhood separator.  The
unresolved step is to obtain this disjoint configuration with the shore-
meeting condition, or to preserve a common boundary partition under the
descent.

The immediate open theorem is therefore the **boundary-edge contact
exchange or compatible-separator theorem**, with two exact branches.  In
the three-path branch, allocate the packed paths among the five named
far-side connected subgraphs while preserving the stable-theta cyclic
sets and the disjoint seventh branch set.  In the separator branch,
synchronize the concrete one-sided equality partition through the opposite
closed shore.  In either branch prove one of:

1. an explicit `K_7`-minor model;
2. an actual order-seven separation with one equality partition extending
   through both closed shores; or
3. a label-preserving configuration satisfying every hypothesis of the
   audited connected-subgraph cyclic-contact allocation theorem, with
   cross-nonadjacency graph a matching of order at most two; or
4. a strict full-neighbourhood-separator descent preserving the paired
   traces, the selected boundary-edge response and the five named
   pairwise-adjacent connected subgraphs.

The third outcome is terminal through the contact-allocation theorem.  The
fourth is admissible only when the decrease is measured on a literal host
separator and all named colouring data survive.  If curvature yields a
degree-seven vertex instead, its neighbourhood is already an exact
order-seven boundary; regeneration of another unranked interface is not a
descent, so colour synchronization or an explicit minor is required there.

The two remaining branches require genuinely coupled host information.  A
verified finite interface realizes the stable-theta allocation, a connected
seven-contact subgraph and three terminal-capacitated paths, yet its two
missing boundary-to-sector incidences share one boundary vertex.  Hence the
matching-defect conclusion does not follow by incidence counting.  On the
separator side, two disjoint abstract parity languages meet every one-block
and every two-block exact independent-trace query, while their static
two-packet quotient has no `K_7` minor.  Split boundaries synchronize by
the existing theorem, but every live nonsplit boundary requires a coupled
proper-minor transition or a labelled minor construction; further
independent-set trace queries cannot finish it.

Several complementary barriers define the trust boundary.  The
seven-connected `K_7`-minor-free join of an edge with the icosahedron has
the same five-subgraph geometry and saturated responses for every incident
contraction, but is six-colourable and has a terminal two-vertex set.  A
separate exact-seven realization shows that all internal proper-minor
response partitions plus unlabelled Kempe connectivity can remain
nonreflectable when the full connectivity and minor-exclusion geometry is
absent.  A seven-connected two-apex tube realizes the entire rural
two-pair/five-subgraph geometry but lacks criticality.  A strengthened version
even gives a fully endpoint-saturated response for every relevant spoke;
it remains six-colourable, showing that separately selected responses do
not spend the universal nonextension law.  Three colour-indexed paths can
also have a triangle of pairwise base-colour intersections, with neither
three internally disjoint representatives nor one common bottleneck; a
bottleneck of the selected paths need not separate the host when other
colours provide bypasses.  A separate verified seven-connected example has
universal nonextension and all five colour locks at one selected boundary
edge, yet all three absent-colour first hits enter the same boundary-free
named connected subgraph.  It contains a `K_7` subgraph and is not
minor-minimal; it shows that a positive allocation theorem must explicitly
use global `K_7`-minor exclusion or proper-minor responses away from the
selected edge.  Finally, an unbounded
triangulated-disc family concentrates all missing contacts in one boundary
label at mutually remote curvature vertices, while a ten-vertex local graph
remains `K_7`-minor-free even with full exterior contact.  Thus curvature,
Hall counting, web structure, static responses and the selected Kempe-path
union are insufficient: the next theorem must spend contraction-critical
colourings, every host bypass, literal first-hit locations, named branch
sets and global `K_7` exclusion.

For the later two-edge exceptional branch, the three available proper-minor
boundary partitions also have no abstract composition consequence.  A
verified minimal gadget realizes the all-equal response and both exclusive
single-edge responses while forbidding the fourth equality partition and
the all-distinct partition.  Its six-colour lift contains a `K_7` minor, so
the missing positive theorem must couple the response lattice to the named
connected subgraphs under global `K_7`-minor exclusion.

The exact-seven and minor-model sides of that coupling have now been
strengthened by audited unbounded theorems.  Contracting the distinguished
edge in the asymmetric order-eight full-component interface gives a
seven-vertex boundary with one connected boundary-full component on each
side.  Its boundary is four-degenerate.  The only five-chromatic case is
`K_2 join C_5`; deleting its universal pair makes the contracted graph
planar.  Undoing the contraction leaves an adjacent vertex split of that
planar graph in the original host, with every relevant `K_5` model using
the two split vertices in distinct branch sets.  This is a precise
split-planar residue, not yet an actual two-apex conclusion.

At an actual order-seven boundary, deleting a boundary--component edge
produces five colour-distinguished first edges.  Seven-connectivity extends
them to a six-ended fan inside the component.  If their original targets
occupy at most five boundary vertices, there is either a clean
target-retaining five-spoke packing or a strictly smaller open component
behind another actual order-seven boundary.  The returned boundary has one
exact colour block of order at least two attained on both shores.  In
parallel, a shortest boundary Kempe transition now gives either the same
two-colour obstruction path through both open shores or a vertex-minimal
list-critical subgraph in each shore.  A proper fixed-trace critical
subgraph transfers the rejected trace to a strictly smaller complementary
component; a shore-filling critical subgraph instead synchronizes all of
its vertex-deletion responses on that trace.

On the labelled-model side, safe absorption makes the
`K_7`-minus-one-edge model spanning.  Seven-connectivity then forces two
distinct attachment vertices from one neighbouring branch set to the
deficient branch set.  Deleting one corresponding model edge preserves the
same labelled model, while all five bichromatic endpoint paths coexist in
that edge-deleted graph.  Thus unique-portal concentration and destruction
of the chosen model edge are no longer obstructions.  Palette colours still
do not identify the five branch-set labels.

The common deletion can now be centred at the deficient singleton.  If its
five common branch sets have neighbour multiplicities `n_1,...,n_5`, the
exact maximum number of simultaneously deletable incident model edges is
`d(x)-5`, and every prescribed persistent edge belongs to a maximum
deletion.  Nonjoint pairs form a matching.  Degree seven is already an
exact singleton-side separation; in its nonadjacent-pair trace, the five
remaining neighbours are bijective both with the five common model labels
and with the five alternate colours.  In the dense alternative, two
explicit path/fan constructions exclude both degree-nine equality
patterns, so `d(x)<=8`; degree at least nine therefore forces a jointly
persistent nonadjacent pair.

At degree eight, a maximum three-edge deletion has triangle endpoints.  A
new parameter-uniform colouring theorem turns its three response classes
into either a single Kempe transition with a common-boundary connected
bipartite subgraph or a connected four-chromatic subgraph containing the
four-vertex clique.  Nondominating outcomes give actual separators;
dominating outcomes give `K_6`-minor-free bounded-chromatic complements.
The previously unexplained two-response Kempe-separated branch is similarly
a connected three-chromatic subgraph, with the same separator-or-dominating
alternative.

The two incident deletions can also be aligned with a split of one common
branch set.  Either this constructs `K_7`, or it returns an actual
full-neighbourhood separation with the two deleted edges on named opposite
sides.  A nested step strictly lowers that boundary unless the opposite
endpoint component is full to it.  Minimizing over all such oriented
separators is a well-founded normalization in which both endpoint
components are full to the same boundary; only a boundary-edge pinch and
the absence of a common partition remain.

At an exact order-seven transition boundary, the opposite-side equality
partition now has full-subgraph demand strictly greater than its packing
number; lower demand reflects and glues.  The two residual partition forms
are explicit, and every merge-critical singleton pair forces a literal
bichromatic path through the opposite open side.  Demand-set reflection
then converts every clean or non-direct path end into a strictly smaller
connected side behind its full neighbourhood.  The unreduced geometry has
both path ends entering the two selected boundary-full connected subgraphs
directly, or loses the old labelled partition under the smaller separator.
A six-connected verified example realizes this direct-entry obstruction,
while every admissible seven-connected augmentation of its fixed skeleton
contains a `K_7`; seven-connectivity and contraction-critical state transfer
must therefore be used together.

That proper-minor response can be spent simultaneously at the two direct
entries.  Contracting their two vertex-disjoint crossing edges and expanding
a six-colouring gives a common double-equality assignment.  A
vertex-minimal boundary-list obstruction in the rich open shore is
connected.  If it is proper, its full neighbourhood is an actual separation
with a strictly smaller connected open side and an exact placement of both
failed edges.  If it fills the shore, then every vertex satisfies

\[
 d_G(v)=6+\varepsilon(v)+\rho(v),
\]

where `epsilon` is internal list-degree excess and `rho` counts repeated
boundary-neighbour colours.  A vertex satisfying
`epsilon(v)+rho(v)<=2` gives an order-seven or order-eight singleton-side
separation.  An all-tight shore is a Gallai tree,
and the sharper surplus-sensitive inequality bounds many remaining shores.
These are genuine unbounded host-side reductions, but their smaller
separations do not automatically preserve the old five branch-set labels.

The first-hit allocation problem is now separated from that list theory.
Rado's theorem for a strict gammoid gives an exact criterion for five
pairwise disjoint response paths to reach five different named branch sets
at their first model contact.  Failure returns a deficient label set and a
small separator in the terminal-avoiding graph.  With at most three fixed
response vertices, the certificate yields either an actual order-seven
separation or two literal contacts with the same unused label.  Iterating
this observation compresses every repeated exposure to one of: an
order-seven separation, two independent or incident persistent edges, or a
connected source subgraph on at most four vertices.

The resulting two-edge response has an exact fixed-partition trichotomy.  It
either attains the selected partition on only one side, rejects it on both
sides with a strict same-partition critical subgraph, or makes both edge
endpoints monochromatic on both sides.  In the last case every
partition-changing Kempe component meets the literal boundary.  The exact
boundary-footprint calculation eliminates all demand-at-most-two switches;
static switches alone cannot synchronize the two shores.

The branch-set collision now has a well-founded labelled rank.  Response
paths may overlap inside the fixed connected response subgraph, but are
disjoint outside it and record their literal first branch-set labels.  Under
a zero- or one-owner transfer, a path lost with the transferred piece is
rerouted inside that response subgraph directly to the retained donor.
Thus the rank never falls, even when the unique owner is itself ranked.
Maximizing the rank and then minimizing the donor eliminates every such
transfer.

The same mechanism now handles an arbitrary owner set whenever its portal
sets can be linked disjointly inside the transferred piece to distinct
attachments of the retained donor.  Splitting the piece along those paths
and absorbing one part into each owner preserves the selected response,
all labels and the rank while strictly shrinking the donor.  Rado and
Menger make failure exact: an inclusion-minimal owner family `I`, with
`2<=|I|<=5`, has a vertex transversal of order `|I|-1<=4` inside the
piece, every proper owner subfamily being linkable.  For two owners the
entire obstruction is one literal bottleneck vertex, and its host exposure
has an exact fork.  Either both owner portals are concentrated at that
vertex, or a connected component behind it is anticomplete to the retained
donor.  In the latter case, seven-connectivity gives either a
label-transversal order-seven full-neighbourhood separator or two
model-preserving deletion-critical edges to the same outside branch set.
More generally, the same minimal owner circuit gives one of three host-level
outcomes for any number of owners: an incident pair of differently labelled
owner contacts, a repeated model-preserving contact to one outside branch
set, or an actual full-neighbourhood separation of order between seven and
ten.  This is the first uniform conversion from a label-allocation failure
inside one branch set to bounded host geometry.  The remaining work is to
convert one of those operation-specific edge or separator responses into
the named first-hit allocation or Hall matching.

The proper-subfamily linkage branch now has a parameter-uniform terminal
construction.  Let `I` be any inclusion-minimal deficient owner family of
order `m`, `2<=m<=5`, and let `K` be its `m-1` vertex Rado--Menger
transversal.  Suppose a component `C` of the donor minus `K` is anticomplete
to the retained donor and adjacent to all six outside branch sets.  If the
owners in `I-{R_0}` can be linked to distinct retained-donor portals while
avoiding `C`, then the retained donor plus the linkage paths, `C`, and five
explicitly selected or merged outside branch sets form a `K_7`-minor model.
The same construction works when the paths meet `C` but leave a connected
remainder adjacent to the linkage union and all six outside branch sets.

For a three-owner circuit with no repeated outside contact, equality in the
host-neighbourhood bound has also been normalized.  The separated component
has an eight-vertex literal boundary consisting of the two internal
transversal vertices and one vertex from each outside branch set.  A
component missing a boundary vertex returns an actual order-seven
separation.  Otherwise there are two or three boundary-full components and
the boundary is four-colourable; in the three-component case it belongs to
the audited 82-type order-eight residue.  Consequently, in a `K_7`-minor-free
host every proper-subfamily linkage must use the distinguished component and
must destroy every connected remainder with the six required outside
contacts.  This is a smaller dynamic obstruction than the earlier generic
owner-circuit fork, but it does not yet produce a common boundary partition.

The lexicographic model choice now sharpens that three-owner obstruction
further.  Maximize the relaxed literal first-hit rank and then minimize the
donor branch set.  The retained part of the donor outside the distinguished
component is connected.  Moving or splitting the distinguished component
would then strictly shrink the donor whenever zero, one or two owner portal
sets have all their contacts there.  Hence in the only nonterminal case all
three owner portal sets are concentrated in the same distinguished
component.  Any two owners consequently give two vertex-disjoint contact
edges with different inherited branch-set labels.  Deleting the pair admits
the three exact response signatures `(equal,equal)`, `(equal,proper)` and
`(proper,equal)`, but not `(proper,proper)`; the common deletion host either
has a `K_4` on the four endpoints or is six-chromatic with a spanning
`K_6`-minor model.  Palette colours are still not model labels, so this
two-edge response substrate is not yet terminal.

The concentrated boundary-full order-eight outcome is now eliminated by an
unbounded host-level argument.  Choose a vertex of the distinguished
component adjacent to the retained donor and seek a three-fan from it to the
three owner representatives.  Failure gives a two-vertex fan separator; the
five remaining vertices of the literal order-eight boundary then bound the
full neighbourhood of the source component by seven, and
seven-connectivity makes it an actual order-seven separation.  If the fan
exists, split the distinguished component along its three arms.  Any
nontrivial arm gives a rank-preserving model transfer with a strictly smaller
donor.  If all three arms are edges, every other component can be absorbed
into an outside branch set; extremality then forces the distinguished
component to be a singleton, contradicting the already proved existence of
two owner-contact edges with distinct ends there.  Thus every extremal
concentrated three-owner order-eight configuration has an actual order-seven
separation.  The theorem does not yet synchronize the two closed-shore
colourings on that boundary.

Independently, every remaining boundary-full order-eight interface with two
or three complementary components now has one operation-coupled normal
form.  A deletion response at an edge from the boundary into one component
is legal on every unchanged component and rejected on the operated one.  It
has an exact Hall-deficient transported partition and connected exact-block
Kempe transition space.  The five forced two-colour paths return either a
clean five-path fan, pairwise disjoint outside its source and boundary, or an
actual order-seven separation.  In the latter outcome the two closed shores
carry the same exact colour block; if their complete equality partitions do
not already agree, both orientations carry literal Kempe obstruction paths
and Hall-deficient connected-support systems.  The theorem deliberately does
not assign the clean fan to five inherited branch-set labels or preserve a
six-contact residual after that assignment.

An exact eight-object quotient classification also corrects a tempting
shortcut in that fan branch.  Two adjacent connected subgraphs which each
meet five of the six outside branch sets do not always complete the model.
Besides the crossed `X,Y` misses, a second sharp obstruction occurs when the
two connected subgraphs miss two distinct members of
`{D,F_1,F_2,F_3}`; its quotient is `K_8-3K_2`.  These and the crossed
quotient are the only exceptions under the reserved-component hypotheses,
and repairing any one of their three missing adjacencies gives an explicit
`K_7`-minor model.  Thus subsequent arguments must count mutually usable
outside branch sets, rather than raw contacts.

Repeated contacts lower the component defect only when all old contact
components are retained; the exact defect change is

\[
             \Delta'=\kappa_2+\kappa_3+\kappa_4-3.
\]

Thus multiplicity alone is not a descent invariant.  On the colouring side,
the selected-partition carrier condition is now an exact Hall problem.
Boundary-full connected subgraphs are universal supports, while each further
named connected subgraph can support exactly the blocks whose complete
literal duty set it meets.  Two full supports close every demand-at-most-two
partition and close a demand-three partition precisely when one additional
support meets one full duty set.  The only higher-demand block shapes on a
seven-vertex boundary are explicitly classified.

At the label-transversal exact seven-boundary returned by the owner-circuit
theorem, the deletion-critical boundary edge now has an exact dynamic normal
form.  Its legal opposite-shore partition sees only one or two disjoint
boundary-full connected supports.  For every legitimate family of retained
named supports, Hall has a nonempty deficient block family `X` satisfying

\[
                       r+|N(X)|<|X|,
                       \qquad r\in\{1,2\}.
\]

In the sharp cases `(r,d)=(2,3)` and `(1,2)`, no retained named support
meets even one complete duty set.  Thus the exact-seven branch is no longer
an unspecified gluing failure: it is a literal duty-contact obstruction on
the opposite shore.  The five critical-pinch entrance paths lie on the
other shore and cannot be counted as those supports.

The returned edge pairs have no further automatic closure under the current
audited Kempe calculus.  An incident differently labelled pair has exact
opposite one-edge responses and then either the nonadjacent-leaf
saturation/bypass fork or the adjacent critical-triangle fork.  A repeated
model-preserving pair crosses its natural full-neighbourhood boundary, so
the existing internal-shore and opposite-shore edge theorems do not apply
without a new placement argument.  In both cases the remaining issue is
still literal first-hit ownership, not existence of another bichromatic
path.

Finally, selecting one
critical edge from each anticomplete open shore gives a six-chromatic,
five-connected deletion host.  It contains either a `K_4` minor rooted at
the four edge endpoints or a universally orientable exact order-seven
separation.  Coupling this with the repeated-pair response on one
three-edge-deletion host is the first theorem here which converts arbitrary
opposite-shore colour drift into literal host geometry.

The immediate open theorem is consequently narrower than the original
first-hit proposal.  The concentrated three-owner order-eight geometry no
longer needs a five-label clean-fan allocation: it already descends to an
actual order-seven boundary.  The next theorem must decorate that returned
boundary with a proper-minor colouring response and prove one of:

1. one complete boundary equality partition is realized by both closed
   shores, so their six-colourings glue;
2. the operation-specific Kempe paths and named connected supports repair a
   missing branch-set adjacency and give an explicit `K_7`-minor model; or
3. a strict host-level descent preserves the selected response, the five
   inherited labels and the exact order-seven interface.

The special boundary returned by the three-fan reduction now has an audited
operation-specific normal form.  It is the disjoint union of the five
surviving order-eight boundary vertices and the two vertices of the failed
three-fan cut.  Every component off this boundary is adjacent to all seven
boundary vertices; its full-subgraph packing vector is `(1,1)` or `(1,2)`;
and the boundary graph is four-colourable.  Deleting an edge from either cut
vertex into the exposed component produces a partition which is legal on
the opposite closed shore, rejected on the exposed shore, and has demand
strictly exceeding the opposite full-subgraph packing number.  Every
admissible mixed-support system therefore has an explicit Hall-deficient
block family.  The same critical edge gives a six-ended prescribed-first-
edge fan, or a five-path packing, or a strictly smaller exact-seven
separation carrying one common exact colour block.  The fan lies on the
shore which rejects the transported complete partition, while the full
connected subgraphs used for reflection lie on the shore where that
partition is legal; they cannot be combined as one Hall system without a
new trace-preserving transfer theorem.

The two vertices of the failed three-fan cut can now be coupled rather than
treated one at a time.  Either the exposed open shore is a single
degree-seven vertex, in which case the opposite shore is connected and has
full-subgraph packing number one, or the two cut vertices have
vertex-disjoint entrance edges into the exposed shore.  In the latter case
the common two-edge deletion has all three nonterminal endpoint signatures
`(equal,proper)`, `(proper,equal)` and `(equal,equal)`, but never
`(proper,proper)`.  Every induced boundary partition is legal on the
opposite closed shore, rejected on the exposed closed shore, has demand
above the opposite full-subgraph capacity, and has a Hall-deficient family
for every admissible named support system.

The singleton alternative is no longer an arbitrary connected exterior.
Its seven-vertex boundary has independence number at most two and chromatic
number at most four, hence exactly four.  If the opposite exterior were
bipartite, colour the boundary with four colours, the exterior with two new
colours, and give the singleton pole one of the latter colours.  This would
six-colour `G`.  Therefore the sole exterior is nonbipartite and contains an
odd cycle; every tree and every bipartite exterior is eliminated at once.

Simultaneous contraction of the two entrance edges gives a connected
induced two-root list-critical subgraph `K` in the exposed shore.  Its full
neighbourhood is an actual separation boundary of order at least seven.  A
proper `K` is strictly smaller than the exposed shore; if `K` fills the
shore, every vertex satisfies the exact identity

\[
                  d_G(v)=6+\varepsilon(v)+\rho(v),
\]

where `\varepsilon` is list-degree excess and `\rho` counts repeated
boundary-neighbour colours.  A vertex with
`\varepsilon(v)+\rho(v)<=2` gives a singleton-side separation of order
seven or eight, while zero list-degree excess makes the
shore a Gallai tree.  This is a genuine host-level reduction, but not yet a
recursive copy of the special interface: a proper core may have boundary
order greater than seven, one failed edge may lie on each side or in the
new boundary, and the double-contraction partition need not equal either
selected one-edge partition.

There is now a well-founded descent in one infinite subfamily of these
interfaces.  Suppose the connected one-full-subgraph shore has a bridge,
the opposite shore contains two disjoint boundary-full connected
subgraphs, and the seven-vertex boundary is bipartite.  Exact two-list
parity forces one distinct boundary vertex to attach only to each bridge
side, with the two forced vertices at even boundary distance; the other
five boundary vertices attach to both sides.  Each bridge side consequently
has a literal full neighbourhood of order exactly seven.  Its new near
packing number is one, its opposite packing number is one or two, and
deleting the bridge gives a complete partition legal on the opposite shore,
rejected on the bridge side and of excessive demand.  Both bridge sides are
strictly smaller than the old shore.  Thus a minimum-order
operation-specific exact-seven interface in this bipartite `(1,2)` branch
is bridgeless.  The move deliberately recomputes the new packing vector; it
does not preserve the old partition, boundary bipartition or inherited
minor-model labels.

The shore-filling two-root list-critical branch now has a substantially
sharper density bound.  Let `r` be the shore order, `E` the total internal
list-degree excess and
`\Delta=\sum_v(d_G(v)-9)`.  Unless a degree-seven or degree-eight vertex
already gives a singleton-side separation,

\[
                         11r+9\Delta\le128+5E.
\]

The new coefficient comes from the operation-specific high-demand boundary
partition: no boundary colour class has order six or seven, so repeated
boundary-neighbour colours are at most four times the distinct-colour
incidences.  In the all-tight case `E=0`, the entire shore has order at most
eleven.  Its Gallai-tree structure is also exact: an endblock lobe with six
boundary contacts gives an order-seven separation; otherwise every
endblock lobe is boundary-full, so the block-cutvertex tree is a path.  If
there is only one block, it is `K_4` or `K_5`.  The remaining unbounded
obstruction is therefore positive total list-degree excess, not the
all-tight branch.  Sparse odd-wheel examples still show that this excess
cannot be bounded from the local two-root list data alone, but the actual
host wheel family is now eliminated uniformly.  A connected subgraph on
the opposite shore which is adjacent to all seven boundary vertices,
together with a wheel hub and five or six rim vertices having at least six
boundary contacts, gives seven explicit branch sets of a `K_7` model.
Minimum host degree supplies those contacts for every wheel shore with rim
order at least five.

Every internal edge of the shore-filling core now has an exact fixed-trace
dichotomy.  Either deleting it leaves a vertex-minimal non-list-colourable
core and lowers total list-degree excess by two, or the fixed boundary trace
colours the edge deletion and supplies, for each alternate colour, an
internal endpoint path or two disjoint first-hit paths to distinct boundary
vertices.  Deletion and contraction of the same edge give the identical
response family.  If all edges take the latter alternative, the core is
subgraph-minimal non-list-colourable and its tight-vertex subgraph is a
Gallai forest.  The `E-2` alternative is not a recursive counterexample, so
the remaining exchange must still preserve literal labels or return a
compatible exact-seven separation.

The response-placement part of a proper-core descent is now exact.  Choose
one entrance vertex which lies in the proper list-critical core and use its
original one-edge deletion colouring, rather than the double-contraction
assignment.  That colouring is proper on the opposite closed shore and its
complete boundary partition is rejected by the core side.  If the core's
full neighbourhood has order seven and contains the five inherited literal
vertices, then it is exactly those five vertices together with the chosen
cut vertex and one vertex of the old shore.  This is a strict generic
five-plus-two response interface carrying the same one-edge witness.  In a
bipartite bridge descent, an orientation retains all five inherited
vertices unless both exclusive old-boundary contacts lie among those five.
The remaining exact-order-seven obstruction in these pullbacks is therefore
literal inherited-vertex loss; separator excess is the preceding
obstruction.  The old boundary partition and five branch-set labels are not
claimed to survive.

There is also a canonical Kempe normalization of the shore-filling
double-contraction trace.  Minimize, in order, total boundary-colour
incidence in the shore, full-subgraph demand, and the number of boundary
blocks.  Every pair of colours used on the boundary then lies in one common
bichromatic component of the contracted minor.  Otherwise switching all
components meeting one colour class merges two anticomplete boundary blocks
without increasing either of the first two coordinates.  Shortest such
connections are internally confined to one open shore in the quotient.
They need not be mutually disjoint or label-aligned, and lifting a
contracted endpoint can restore one monochromatic distinguished edge.

The existing exact-block and Hall-reflection theorems apply once the
returned boundary carries the required operation-specific response; the new
three-fan reduction by itself does not supply that decoration.  Outside this
concentrated equality case, the incident/repeated-contact and bounded-
separator owner-circuit outcomes still require the same label-faithful
operation-specific closure.

An unlabelled rooted model, an internal portal cut, or an order-seven
boundary without one legal matching of blocks to literal connected supports
is not terminal.  The two partitions transported automatically by the
opposite colouring chambers remain incompatible.  Audited static examples
allow maximum first-hit rank, minimum donor order and no local order-seven
boundary even under seven-connectivity and `K_7`-minor exclusion.  Those
examples are six-colourable and coherently two-apex, so the missing theorem
must spend
contraction-criticality and `K_7`-minor exclusion together to convert the
new internal transversal into the exact Hall certificate; neither rank nor
boundary colour data alone suffices.

The newly promoted sources are the
[deficient-singleton deletion theorem](results/hc7_deficient_singleton_joint_persistence.md),
[split-aligned separator theorem](results/hc7_split_aligned_joint_deletion.md),
[critical-triangle Kempe-separated-component theorem](results/hc7_critical_triangle_kempe_separation.md),
[clique-star response theorem](results/hc7_clique_star_kempe_separation.md),
[exact-seven full-subgraph-demand theorem](results/hc7_exact7_critical_triangle_full_subgraph_demand.md),
[five-contact component absorption](results/hc7_five_contact_rejection_component_absorption.md),
[demand-set separator descent](results/hc7_exact7_demand_set_separator_descent.md),
[two-edge list-critical direct-entry descent](results/hc7_direct_entry_two_edge_list_core.md),
[labelled first-hit Rado reduction](results/hc7_labelled_first_hit_rado_reduction.md),
[repeated-exposure compression](results/hc7_labelled_first_hit_exposure_compression.md),
[fixed-partition two-edge fork](results/hc7_repeated_exposure_fixed_trace_fork.md),
[selected-partition preservation criterion](results/hc7_exact7_selected_response_preservation.md),
[transported-partition Hall reflection](results/hc7_transported_partition_hall_reflection.md),
[two-contact branch-set transfer](results/hc7_response_aligned_two_contact_lobe_transfer.md),
[first-hit rank preservation under branch-set transfer](results/hc7_first_hit_rank_preserving_branch_set_transfer.md),
[multi-owner portal-linkage transfer](results/hc7_multi_owner_portal_linkage_transfer.md),
[reserved-component linkage completion and the three-label order-eight normal form](results/hc7_reserved_component_linkage_completion.md),
[three-owner component concentration and its two-edge response substrate](results/hc7_three_owner_reserved_component_concentration.md),
[three-owner order-eight reduction to an actual order-seven separation](results/hc7_three_owner_order8_exact7_reduction.md),
[operation responses at the resulting special five-plus-two exact-seven boundary](results/hc7_special_five_plus_two_exact7_response.md),
[two-boundary-vertex reduction to a singleton shore or two-root list-critical core](results/hc7_special_exact7_two_edge_list_core.md),
[bipartite-boundary bridge response descent](results/hc7_exact7_bipartite_bridge_response_descent.md),
[special shore-filling density and block structure](results/hc7_special_shore_filling_density.md),
[fixed-trace internal-edge dichotomy](results/hc7_fixed_trace_internal_edge_dichotomy.md),
[six-spoke boundary completion](results/hc7_six_spoke_boundary_completion.md),
[selected-response pullback through a retained exact-seven boundary](results/hc7_special_exact7_selected_response_pullback.md),
[Kempe-minimal boundary-trace normalization](results/hc7_kempe_minimal_boundary_trace.md),
[nonbipartiteness of the singleton-shore exterior](results/hc7_singleton_shore_nonbipartite.md),
[operation-coupled colouring responses at a boundary-full order-eight separation](results/hc7_operation_coupled_order8_response.md),
[Hall obstruction at a label-transversal critical pinch](results/hc7_label_transversal_pinch_hall_obstruction.md),
[repeated-contact defect calculation](results/hc7_repeated_contact_component_defect.md),
and [opposite-shore critical-edge linkage](results/hc7_cross_shore_critical_edge_linkage.md),
each with an adjacent internal audit.

The supplementary audited constructions are the
[exact two-subgraph completion classification](results/hc7_five_contact_completion_classification.md),
[endpoint-`K_4` transfer](results/hc7_endpoint_k4_transfer_or_order7.md),
and [distinct-boundary prescribed-spoke transfer](results/hc7_distinct_boundary_spoke_owner_transfer.md).
They remain useful as labelled constructions and guardrails, but the
three-fan theorem supersedes them as the active route through the
concentrated three-owner order-eight branch.

This does not prove `HC_7`.  It closes the one-hole donor splitting problem,
the disjoint two-trace linkage branch, broad degree-eight cyclic-contact
families, the entire rooted cycle-allocation problem, the cutvertex and
generic two-cut component geometry, the universal-contact three-connected
family, the reserved-cycle/high-connectivity branch and the two-safe-support
branch by unbounded theorems.  The residual is now the label-preserving
allocation at one minimum full-neighbourhood interface, sharpened to the two
exits above, not a finite web census.  The two-adjacent-edge exceptional
complements and the remaining degree-eight bounded-interface continuation
remain after this branch.  The older
component-defect programme below is retained as a secondary source of
explicit branch-set splits, not as a competing primary spine.

## Secondary structural laboratory: adjacent-pair colouring and rooted models

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
2. an actual order-seven separation for which six-colourings of the two
   closed shores induce the same equality partition of the seven literal
   boundary vertices after a colour permutation;
3. another full valid defect-one configuration in the original fixed `G`
   whose chosen lifted simplicial component `L'` satisfies
   `|V(L')|<|V(L)|`.

A two-vertex `K_5`-model transversal is a genuine terminal contradiction.
Deleting the two vertices leaves a `K_5`-minor-free graph, which is
four-colourable by the established `t=5` case; two fresh colours then
six-colour the whole graph.  The separately audited order-seven-separation
theorem for such a pair remains valid structural information, but is not
needed for the chromatic contradiction.

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
host-level exchange.  For the conditional target, choose `L` with minimum
order over every eligible simplicial lifted component in every valid
defect-one configuration in the fixed graph `G`.  The recursive outcome
must produce another full valid defect-one configuration in `G` with a
component `L'` of smaller order (preferably `L'\subsetneq L`).
Noncanonical connector length and the order of the selected contact graph
are not rank coordinates.

A **valid defect-one configuration** means the complete tuple used in this
conditional branch: the adjacent pair and its connected-dominating
colouring frame; a uniquely deficient rooted `K_4` model; its
colour-matched path `P` and an admissible cut `q`; four nonempty labelled
selections of residual components; eligibility of every selected component
at `q`, including adjacency to `z` and both path-side anchor sets; and a
`K_4`-minor-free component-contact graph `J` with defect one.  The component
`L` is the literal connected subgraph represented by a simplicial
degree-two vertex of `J`.  An outcome with smaller `L'` must be another full
valid configuration in the original fixed graph `G`, although its rooted
model, path, cut, and selected components may change; a component produced
only in a proper minor is not an eligible outcome.

A sequence of audited results sharpens this conditional branch without claiming
that its hypotheses are exhaustive.  First, after making the defect-one
selection inclusion-maximal at the fixed path and cut, every omitted
eligible component has at most one selected-component neighbour.  The
quotient `K_3` joined with the two-tree is edge-maximal `K_7`-minor-free;
every connected subgraph outside the selected model attaches to a clique of
quotient labels.  Absorbing all outside components adjacent to a chosen
simplicial lift confines its full neighbourhood to five named branch sets,
but does not bound the number of literal boundary vertices.

Second, any distinguished sixth branch set of a local `K_6` model can be
reselected, by deletion and absorption into named branch sets, as a
singleton or an induced path.  In the path case each endpoint is the unique
contact vertex for at least two of the five named branch sets.  This is a
local model normalization only: the absorption may destroy the protected
component label, path-side role, or valid-cut data of a full defect-one
configuration.

Third, proper-minor colourings force literal attachment information.  For
an operated edge in the five-chromatic core, a colour missing from one
bipartition-side attachment set forces both original endpoints to meet the
opposite side.  A common missing colour forces both endpoints to meet both
sides.  Cross-type and one-sided edges consequently force full five-colour
attachment palettes after deletion or contraction.  These conclusions are
operation-specific but still do not identify colours with prescribed minor
branch sets.

Fourth, every simplicial lift `L` lies in a labelled `K_7^-` model.  If its
two neighbours in the two-tree are `M,N`, the edge `MN` belongs to a second
triangle `MNR`; the three path-cut anchors together with `M,N,R` form a
fixed `K_6` model disjoint from `L`, and adding `L` leaves only the
`L`--`R` adjacency missing.  Thus unrooted model regeneration after an
operation inside `L` is redundant.

Fifth, the whole labelled two-tree contains a rainbow induced `K_4^-`:
its four vertices have the four protected labels.  The shared edge of this
diamond separates its two nonadjacent vertices in the contact graph.  After
lifting and simultaneously absorbing every adjacent outside component, one
obtains a connected open shore whose full neighbourhood is contained in
the five common branch sets of the associated labelled `K_7^-` model, with
the other deficient branch set on the far side.  This is a genuine host
separation of order at least seven.  It compresses the entire infinite
two-tree equality class to a single five-branch-set-supported interface,
but supplies neither an upper bound on its order nor compatible shore
colourings.

For every internal edge `xy` of `L`, the graph `G-{x,y}` has chromatic
number five or six.  In the five-colour case `xy` is double-critical:
ordered generalized Kempe paths exist for every list of distinct colours,
and the common neighbourhood of `x,y` meets all five colour classes.  If
that common neighbourhood meets the five *named* common branch sets, a
spanning-tree split of `L` at `xy` is an explicit `K_7` model.  In the
six-colour case, every six-colouring obeys the exact two-pole
missing-colour cover, and a colouring inherited from `G/xy` has one common
missing colour.  The remaining local theorem is therefore literal
colour-to-branch-set alignment, a compatible exact-seven separation, or a
strictly smaller full valid configuration—not path existence or unrooted
minor existence.

Sixth, in the five-colour edge branch the common-neighbour set is colourful
in every five-colouring, every pair of its colour classes is joined inside
one bichromatic component, and any rainbow transversal roots
`F_5=K_1\vee P_4`.  Adjoining the two operated endpoints gives an explicit
`K_2\vee F_5` minor.  The three missing chords among the four path bags are
not forced.  Moreover the common-neighbour witnesses avoid every named
branch set privately supported by the chosen endpoint; this explains why
the rooted fan does not automatically align with the old labelled
`K_6` model.

Seventh, the five-branch-set-supported interface admits a
parameter-uniform connected-set trichotomy.  A connected deficient branch
set whose whole neighbourhood is confined to the `m-1` contacted branch
sets of a `K_m` model in an `(m+1)`-connected graph yields an explicit
`K_{m+1}` model, an actual nested separation of order at least `m+1`, or a
proper-subbag near-clique model with at most
`floor((m-1)/2)` missing spokes.  For `m=6` the last outcome is a labelled
`K_7^-` or `K_7^\vee` model.  The rotation is a strict subbag move only in
the current presentation; it is exactly reversible and does not preserve
the path-cut component labels needed for the proposed defect-one rank.

Eighth, global minimization over all oriented `K_7^-` models gives a second
unbounded normalization.  A minimum deficient branch set is a singleton or
an induced path.  In the path case its endpoint-private label sets have
sizes `2+2` or `2+3`.  If the path has an internal vertex, every five-fan
from that vertex collides first in one named common branch set.  In the
balanced `2+2` case this yields an actual full-neighbourhood separation,
which is exactly order seven when that common branch set contributes five
boundary vertices.  This is a near-clique normalization, not yet a descent
among full valid defect-one configurations.

Ninth, every reversible connected-subgraph rotation carries compulsory
colouring data on one actual separation.  Its unique donor-side attachment
edge and every contact edge to a newly missed named branch set lie on
opposite closed sides of `S=N(W)`.  Deletion and contraction give the same
boundary response language for each edge; the two languages lie in the
opposite set differences

\[
 \operatorname{Ext}(O,S)\setminus\operatorname{Ext}(C,S)
 \quad\hbox{and}\quad
 \operatorname{Ext}(C,S)\setminus\operatorname{Ext}(O,S).
\]

Any common equality partition therefore six-colours `G`.  This converts a
reversible geometric rotation into a label-faithful host-level interface,
but does not yet force the collision.

The same rotation now has a genuine host-level extremal normalization.
For seven disjoint sets, pairwise connected induced unions already force a
`K_7` minor by the component-count density theorem.  Applying this to every
component left after a connected transfer shows that each component either
completes the `K_7` model or misses a named fixed branch set and exposes its
full neighbourhood as an actual separation.  More importantly, choose a
supported one-missing-adjacency model by minimum total branch-set order and
then maximum deficient-centre order.  In every reversible outcome, strict
decrease is forced unless the transferred subgraph is itself a
vertex-minimal connected subgraph spanning the unique donor attachment, at
most two selected lost-contact portals, and every vertex with a neighbour
outside the seven old branch sets.  Thus the arbitrary rotation orbit has
been reduced to one atomic connected-subgraph equality case under a
well-founded invariant.  The theorem does not yet bound the returned
separator by seven or synchronize the two boundary response languages.

At a shared donor/contact endpoint, one simultaneous-contraction colouring
gives a complementary refinement: either one of the two named incident
edges is linked through a bichromatic component for every alternate colour,
or two explicitly coupled Kempe switches create a three-colour path bypassing
the unique donor-internal attachment.  This is label-faithful but the bypass
may first enter the wrong fixed branch set.

A scoped audited Hall extension handles any number of named edges incident
with one contracted centre, even when their other endpoints have edges among
themselves.  In one common six-colouring, either two named endpoints are
joined off the centre, or three named endpoints have a deficient Hall set:
one is bichromatically joined to the centre in all five alternate colours,
two are each joined in at least four, or all three are each joined in at
least three.  This retains literal endpoint names but still does not identify
the colour components with the five protected branch sets.

Tenth, a two-vertex `K_5`-model transversal cannot occur in any
seven-chromatic graph.  This restores the coherent global-pair alternative
as a direct proof-closing outcome, rather than a precursor to the unresolved
colour-gluing step.

Eleventh, an actual order-seven separation has a sharply constrained
boundary.  Every component of either open shore is adjacent to all seven
boundary vertices, and deleting any one boundary vertex leaves a
`K_5`-minor-free graph.  Consequently the boundary is at most
five-colourable; equality forces the canonical graph `K_2\vee C_5`.  In
that equality case strong contraction-criticality forces both open shores
to be connected (the full-packet vector is `(1,1)`).

That five-chromatic equality case is now eliminated completely by a
parameter-uniform host-level theorem.  More generally, let `C` be any
induced cycle of length at least four, let adjacent vertices `p,q` be
complete to `C`, and suppose the remainder consists of two connected open
shores that are each adjacent to every displayed boundary vertex.  If
`G-\{p,q\}` has a `K_5` minor, then `G` has a `K_7` minor.  Indeed, in
`G-\{p,q\}`, each graph
induced by `C` and one shore is three-connected, and `C` is spread out
across every order-three separation.  If either shore contains a
`C`-rooted `K_4` minor, its four branch sets, the opposite shore, and the
singletons `p,q` give an explicit `K_7` model.  Otherwise
Martinsson--Steiner's rooted-minor planarity lemma makes both shores planar
after adding a universal apex.  The wheel on that apex and `C` forces each
shore into a disc bounded by `C`; gluing the two discs makes
`G-\{p,q\}` planar, contradicting its `K_5` minor.  For the exact-seven
boundary `K_2\vee C_5`, that minor follows from minor-criticality and
`HC_5`.  Therefore any still-unresolved exact order-seven colour-gluing
output has boundary chromatic number at most four.  The separately audited
pentagonal Kempe normalizations are retained as structural tools but are
no longer needed to close the five-chromatic boundary.

The audited capped-antiprism family
`K_2\vee H_n` is a sharp barrier to strengthening this geometry alone.  It
is seven-connected, edge-maximal `K_7`-minor-free, has maximally distributed
contacts in a labelled `K_7^-` model, and has five-branch-set-supported
separators of unbounded order.  It is only six-chromatic and its two join
vertices meet every `K_5` model.  The new chromatic obstruction shows that
this is exactly why the family cannot be upgraded to a seven-chromatic
counterexample.  A complementary audited boundary-language amplifier is
seven-chromatic and has no such two-vertex transversal, but contains a
large clique minor and false twins, so it is neither `K_7`-minor-free nor
contraction-critical.  Static extension languages and geometry therefore
cannot replace the missing all-operation, label-preserving transition.

The two-tree supplies a clique tree: adjacent maximal triangles share an
edge, and their corresponding local `K_6` models share the three anchors and
two named contact components.  Colour propagation on those shared `K_5`
sets is insufficient by itself, since `K_3` joined with a two-tree supports
such a coherent pattern without a `K_7` minor.  Every transition must also
record a label map from every vertex of `J` to its protected branch-set
class, the orientation of `P` and the valid-cut interval endpoints, and
chosen literal host edges and endpoints witnessing every edge of `J` and
every contact with `z` and the two path-side anchor sets.  A transition must
retain those witnesses under lifting or provide explicit replacements.  It
must also record the source of each colouring response, preservation of
named root traces, and the exact boundary equality partition.  Failure must
return `N_G(Y)` for a named connected residual piece `Y`, with both shores
nonempty.  A deletion or contraction inside `L` is only a probe; every
terminal conclusion must lift back to the original `G`.

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
- [`hc7_defect_one_simplicial_normalization.md`](results/hc7_defect_one_simplicial_normalization.md)
- [`hc7_minimal_sixth_branch_set_path.md`](results/hc7_minimal_sixth_branch_set_path.md)
- [`hc7_edge_response_attachment_forcing.md`](results/hc7_edge_response_attachment_forcing.md)
- [`hc7_defect_one_near_k7_edge_fork.md`](results/hc7_defect_one_near_k7_edge_fork.md)
- [`hc7_defect_one_rainbow_diamond_separator.md`](results/hc7_defect_one_rainbow_diamond_separator.md)
- [`hc7_connected_one_hole_trichotomy.md`](results/hc7_connected_one_hole_trichotomy.md)
- [`hc7_double_critical_edge_rooted_fan.md`](results/hc7_double_critical_edge_rooted_fan.md)
- [`hc7_near_k7_minimal_path_fan_collision.md`](results/hc7_near_k7_minimal_path_fan_collision.md)
- [`hc7_rotation_opposite_boundary_responses.md`](results/hc7_rotation_opposite_boundary_responses.md)
- [`hc7_response_collision_quasi_transfer.md`](results/hc7_response_collision_quasi_transfer.md)
- [`hc7_shared_interface_bichromatic_bypass.md`](results/hc7_shared_interface_bichromatic_bypass.md)
- [`hc7_two_vertex_k5_transversal_chromatic_obstruction.md`](results/hc7_two_vertex_k5_transversal_chromatic_obstruction.md)
- [`hc7_exact7_no_rigid_trace.md`](results/hc7_exact7_no_rigid_trace.md)
- [`hc7_cycle_boundary_completion.md`](results/hc7_cycle_boundary_completion.md)
- [`hc7_pentagonal_separation_completion.md`](results/hc7_pentagonal_separation_completion.md)
- [`hc7_exact7_universal_edge_kempe_normalization.md`](results/hc7_exact7_universal_edge_kempe_normalization.md)
- [`hc7_exact7_exposed_sigma_kempe_paths.md`](results/hc7_exact7_exposed_sigma_kempe_paths.md)
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

21. **Exact-seven first entry now has a host-measured separator excess.**
    Orient an actual order-seven separation toward a six-coloured shore and
    write its high-demand boundary partition as

    $$
       D\mid E\mid\{r\}\mid\{z\}
       \quad\text{or}\quad
       D\mid E\mid\{r,z\},
       \qquad |D|=3,\ |E|=2.
    $$

    If that shore contains two disjoint connected subgraphs adjacent to
    every boundary vertex, every other boundary partition reflects and
    six-colours `G`; in either displayed partition a prescribed
    bichromatic `r`--`z` path exists and every such path meets the same two
    named subgraphs.  No adjacency between those two subgraphs is needed.
    If instead the shore has full-subgraph packing number one and a
    boundary-contact transversal of order at most two, it gives an actual
    order-seven separation, a repair subgraph disjoint from a boundary-full
    residual subgraph, or a labelled alternating Two-Paths web.

    In the hard `(1,2)` orientation, a non-direct first entry has a connected
    prefix component `K`.  If `K` contacts at least five boundary vertices,
    the audited defect-two contraction theorem synchronizes the shore
    colourings.  Every survivor therefore satisfies

    $$
       |N_G(K)\cap S|\le4,
       \qquad
       |N_G(K)\cap(P_1\cup P_2)|\ge3.
    $$

    Thus an entire unbounded broad-support family is closed.  A verified
    six-connected `K_7`-minor-free example shows that lexicographic
    path/subgraph minimality alone cannot peel a direct first entry; the
    seventh connectivity unit and proper-minor colour responses are
    essential.

    There is also a scalar host invariant.  Suppose a forced path avoids
    the second named boundary-full subgraph and leaves a nonempty connected
    residual `R` in the first.  Let `Lambda` be the boundary contacts lost
    by `R` and put `U=N_G(R)-S`.  Failure of the explicit boundary-block
    contractions forces

    $$
       |U|\ge|\Lambda|\ge2,
       \qquad
       \varepsilon(R)=|U|-|\Lambda|=|N_G(R)|-7\ge0.
    $$

    Equality is an actual order-seven separation.  When `|U|\le2`, the
    two lost boundary contacts are classified exactly: they are either
    `\{r,z\}` or one vertex of `D` and one of `E` in the four-block case,
    and necessarily the latter in the three-block case.

    Nested full-neighbourhoods identify the next obstruction.  For a
    connected side with boundary `X` of order `7+epsilon`, every component
    of `G-X` which misses a vertex of `X` has a full neighbourhood of
    strictly smaller excess.  At `epsilon=1`, failure of such descent is
    exactly an eight-vertex boundary for which every component of `G-X` is
    adjacent to every boundary vertex.  In a `K_7`-minor-free graph, if
    there are `m` such components and `Q` is a boundary clique, then
    `m+|Q|\le6`.

    At excess one, a component which misses one of the eight boundary
    vertices has neighbourhood exactly the other seven vertices.  Both
    closed shores then realize every prescribed independent boundary set
    as an exact colour class.  A split seven-vertex boundary therefore
    returns one common equality partition and six-colours `G`.  The new
    boundary is always four-colourable.  The exact-seven classification
    leaves `K_2\vee C_5` as the only possible five-chromatic boundary, but
    in that equality case contraction-criticality makes both open shores
    connected and the cycle-boundary completion theorem gives a `K_7`
    minor.  Nonsplit four-colour boundaries still require a dynamic
    transition.

    The boundary-full order-eight alternative is now closed whenever it
    has at least four complementary components.  Four full components and
    a boundary triangle give an explicit `K_7`-minor model.  If there is no
    boundary triangle, the eight-vertex boundary is three-colourable; the
    other three full components can realize that same labelled colour
    partition on the closed side of each component, and the side colourings
    glue.  This argument does not require the eight-set to be a minimum
    cut.  Hence the irreducible positive-excess alternative has exactly two
    or three full complementary components.

    In the exactly-two-component case, the two-full-shore boundary-
    absorption theorem makes the eight-vertex boundary four-colourable.
    This is not a closure: it neither supplies a common labelled boundary
    partition nor synchronizes the two closed-shore six-colourings.

    The three-component boundary has also been classified exactly at the
    finite boundary level.  Compact `K_4` models and clique odd-cycle
    transversals close by explicit component lifts or packet-funded
    gluing.  Among all eight-vertex graphs, precisely 82 isomorphism types
    avoid both mechanisms; all are three-colourable, all contain two
    vertex-disjoint odd cycles, and five are edge-minimal within the finite
    residue.  This computer-assisted census does not synchronize a
    proper-minor response and is not an unbounded closure.

    The remaining two component counts now share one unbounded dynamic
    reduction.  The eight-vertex boundary is five-degenerate, and deleting
    any fixed nonempty independent boundary class leaves a four-degenerate
    graph.  Hence the full six-colour boundary space, and every exact-block
    five-colour subspace, is Kempe connected.  Extension through a named
    complementary component can change across one boundary Kempe move only
    when that literal component contains a bichromatic path joining two
    boundary two-colour components.  With two full components, a shortest
    transition between the disjoint extension sets gives such a path at
    each end.  With three components, deletion or exact-block contraction
    gives three pairwise-extension anchor colourings in one connected
    transition space, and every component occurs on a signature-changing
    edge.

    For each of the 82 three-component boundary types this can be sharpened
    with a second proper-minor operation.  Choose a three-colouring
    `A|B|{p,q}` for some local nonedge `pq` of the new boundary.  This pair
    is not automatically the inherited old pair `r,z`.  Either its
    three-block partition extends through every component-side and glues,
    or a fixed component is locked in the split partition
    `A|B|{p}|{q}` and contains a bichromatic `p`--`q` path.
    Deleting the first edge of that path produces a different
    demand-at-least-three boundary response and five colour-indexed paths
    from its internal endpoint to the boundary.  Those paths are pairwise
    edge-disjoint and may intersect only at vertices of the common endpoint
    colour.

    Two complementary path normalizations are now available.  Globally,
    the edge `vp` and the five colour-indexed first edges extend to six
    pairwise internally disjoint paths ending at every vertex of any
    prescribed six-set.  These paths may traverse the whole host, including
    unselected boundary vertices and protected branch sets.  If the
    original boundary targets are retained inside the named component, a
    vertex-capacitated Menger argument instead gives either five paths
    disjoint outside their base and the boundary, or an actual order-seven
    separation.

    In the separator outcome the edge-deletion colouring is proper on one
    closed shore and supplies an exact boundary colour class `J` of order at
    least two.  Contracting the connected side together with `J` gives the
    same exact class on the opposite shore.  The exact-`J` boundary-colouring
    space is Kempe connected.  If the remaining boundary is a clique, the
    shores glue; hence every live separator output has a nonedge outside
    `J`.

    That nonedge now yields a simultaneous host-level object.  Either one
    shore contains its bichromatic path, or both shore colourings admit a
    common fresh non-`J` colour absent from the boundary.  In the latter
    case there are two vertex-disjoint paths: the first joins the endpoints
    of the deleted edge and meets the boundary only in `J`; the second runs
    through the opposite shore between two distinct bichromatic components
    outside `J`.  On the actual augmented eight-boundary, the same argument
    gives a common trace, an order-seven full-neighbourhood separator, or
    one selected component adjacent to all eight boundary vertices.  It
    does not yet allocate the paths to inherited branch-set labels or make
    every complementary component boundary-full.

    Independently, contracting the deleted edge and extremizing an
    image-containing `K_6` model gives a well-founded model-side normal
    form.  The branch set containing the contraction image has at most two
    components after the image is removed.  Each such component is solely
    responsible for contacts with at least two of the five other branch
    sets, and their responsibility sets are disjoint.  Uncovered components
    attach only to the image-containing branch set; six attachment vertices
    lift to a full exact order-seven separator.  Splitting that branch set
    across the deleted edge gives an explicit `K_7` whenever both sides
    retain all five foreign contacts.  A connected subgraph wholly outside
    the model cannot repair a missing foreign contact.

    This normalization now has a deletion-persistent version.  Safe
    absorption makes the labelled `K_7`-minus-one-edge model spanning, and
    seven-connectivity forces one neighbouring branch set to contain two
    attachment vertices to the deficient set.  Deleting one corresponding
    edge preserves the model through the other, so all five bichromatic
    endpoint paths occur in the same graph as the fixed labelled model.

    The model selection is now rooted at the actual critical boundary
    endpoint.  Minimize the common branch set containing `v` while retaining
    the protected singleton branch set `{x}` and the model edge `xv`.
    A parameter-uniform branch-set reassignment theorem gives at least two
    deletion-persistent incident edges for this same model and bounds
    `G[R]-v` by two components.  Several protected singleton branch sets can
    be retained simultaneously, with a correspondingly sharper component
    bound.  Thus singleton placement, the common endpoint and the need for
    an edge distinct from `xv` are no longer open.

    More strongly, either two incident edges can be deleted simultaneously
    while that same spanning labelled near-complete model survives, or
    `R={v}`, `d_G(v)=7`, and `N_G(v)` is an actual order-seven separation.
    In the first branch the common deletion is a proper subgraph of the
    hypothetical counterexample, so it is six-colourable and contains the
    fixed labelled model at the same time.  In the second branch the
    remaining task is exactly shore-colouring synchronization.

    The persistent edges themselves now have a sharp support-class
    structure.  Their number is given by an exact rooted-component and
    foreign-label count, and is at least `d_G(v)-5` in the common-label
    `HC_7` case.  Two persistent edges fail to be jointly deletable only
    when they form one fragile two-edge support class; consequently all
    such forbidden pairs form a matching.  If no jointly persistent pair
    has nonadjacent outer endpoints, those endpoints induce a complete
    graph minus a matching.  `K_7`-minor exclusion then bounds their number
    by seven and gives `d_G(v)<=12`; degree at least thirteen forces a
    jointly persistent induced two-edge path.

    The colouring geometry of every jointly persistent pair is also
    exhaustive.  Nonadjacent outer endpoints give the exact star-
    contraction trace and the saturation-or-bypass alternative.  Adjacent
    endpoints form a critical triangle: every colouring of the common
    deletion has exactly one of the two exclusive one-edge responses.  The
    response families are either in different Kempe components, or a first
    transition gives a connected bichromatic subgraph whose open
    neighbourhood carries the same colouring from both sides.  If that
    subgraph does not dominate, its full neighbourhood is an actual
    separator; if it dominates, its complement is five-chromatic and
    `K_6`-minor-free.  These conclusions retain the same labelled model but
    deliberately make no palette-to-label inference.

    On the colouring side, shortest Kempe distance between the two shore
    extension sets gives either one common obstructed boundary move, with a
    path through each shore, or one list-critical subgraph in each shore for
    a boundary trace rejected by both.  In the exact asymmetric interface,
    a proper fixed-trace critical subgraph transfers to a smaller connected
    component; a shore-filling one synchronizes all vertex-deletion
    responses on the fixed trace.  A persistent edge whose deletion attains
    that trace belongs to every such obstruction.  Otherwise the entire
    edge-deletion response set rejects the trace.

    The boundary-crossing placement of a persistent edge is also reduced.
    If it ends in the branch set anticomplete to `{x}`, simultaneous
    contraction of the induced two-edge path gives a common
    saturation-or-bypass colouring.  A six-colouring after deleting the
    persistent edge produces a one-extra-colour critical kernel in the full
    shore.  A proper kernel gives a strict component-order descent retaining
    the same oriented boundary partition and the model in the edge-deleted
    graph.  A shore-filling kernel gives an order-seven or order-eight
    singleton-side separation unless every vertex has list-degree excess
    plus repeated-boundary-colour count at least three; the surviving shore
    then has minimum degree at least nine.  At such a root the support count
    gives at least four persistent incident edges.  The dense alternative
    can avoid a forced induced two-edge path only in degrees nine through
    twelve; above that range the induced path and its exact contraction
    trace are forced, although their label allocation remains open.

    When the selected edge attains the fixed trace, two aligned critical
    edges give a boundary-to-boundary bypass and then an explicit `K_7`
    model or a donor-side full-neighbourhood separator carrying the exact
    lost branch-set label and opposite proper-minor responses.  When no
    colouring after deleting the edge attains the trace, total rejection
    gives paired list-critical kernels along a shortest boundary Kempe
    sequence.  Two verified counterexamples rule out the tempting claim
    that persistence forces a tight kernel endpoint, even under the static
    seven-connected aligned geometry.

    Contracting the distinguished boundary edge gives two full shores on a
    seven-vertex boundary.  The boundary is four-degenerate, and its only
    five-chromatic form is `K_2 join C_5`.  That form has a planarizing pair
    in the contracted graph; lifting leaves one adjacent vertex split and a
    prescribed two-root `K_5`-model obligation in the original graph.

    Finally, a critical edge at any actual order-seven separator gives a
    six-ended component-internal fan.  With at most five original boundary
    targets, failure of the clean five-spoke packing strictly decreases the
    open component and returns another order-seven boundary with one exact
    colour block attained on both shores.

    The precise open theorem is now a **label-allocation or compatible-
    separator theorem in one common model-preserving deletion**.  In the
    simultaneous-deletion branch, decode a six-colouring through the same
    labelled near-complete model.  If the two outer endpoints are
    nonadjacent, the induced two-edge path already gives the audited
    saturation-or-bypass alternative; if they are adjacent, the critical
    triangle has only the two exclusive one-edge responses.  One must
    either connect their Kempe components label-faithfully or use their
    separation to obtain the common full boundary partition; the possibility
    that the response families are Kempe-separated is still open.  In both
    endpoint cases the literal first hits must yield an explicit `K_7`
    model, a colour-compatible order-seven separation, or a strict descent
    retaining the labelled model and boundary response.  In the shore-
    filling branch, the extra persistent edges forced by minimum degree at
    least nine must perform the same allocation.  In the degree-seven branch
    the separator already has exact order and only synchronization remains.

    The split-planar `\overline{P_7}` reduction is retained as a secondary
    route.  Six contacted quotient bags give an explicit `K_7`; every
    survivor has at least two empty bags and a collision bag.  A verified
    example shows that fixed-bag root transfer is false, so any completion
    must globally reselect the model or return a compatible exact
    separation.

    The written sources are the
    [exact-seven orientation theorem](results/hc7_exact7_packet_orientation_corollary.md),
    [non-direct first-entry reduction](results/hc7_exact7_first_entry_bridge_reduction.md),
    [path-residual separator-excess theorem](results/hc7_small_path_intersection_lobe.md),
    and [nested full-neighbourhood descent](results/hc7_nested_full_neighbourhood_descent.md),
    together with the
    [excess-one labelled descent](results/hc7_epsilon_one_labelled_descent.md),
    [four-component order-eight closure](results/hc7_full_order8_four_component_closure.md),
    [three-component boundary classification](results/hc7_order8_three_component_boundary_classification.md),
    [full-component Kempe-transition theorem](results/hc7_order8_full_component_kempe_transition.md),
    [prescribed-spoke and coloured-separator reduction](results/hc7_order8_prescribed_spoke_reduction.md),
    [minimal contracted-edge `K_6` model](results/hc7_contracted_edge_k6_model_normalization.md),
    [fresh-colour disjoint linkages and augmented-boundary transition](results/hc7_exact7_fresh_colour_linkage.md),
    [contracted full-component interface](results/hc7_augmented_full_component_contraction_reduction.md),
    [contracted five-chromatic boundary](results/hc7_contracted_five_chromatic_boundary.md),
    [critical-edge exact-seven fan descent](results/hc7_exact7_critical_edge_fan_descent.md),
    [opposite-shore single-transition obstruction](results/hc7_opposite_shore_single_kempe_transition.md),
    [two-shore Kempe/list-critical dichotomy](results/hc7_two_shore_kempe_list_dichotomy.md),
    [fixed-trace list-critical transfer](results/hc7_boundary_list_critical_transfer.md),
    [single-portal amplification](results/hc7_single_portal_amplification.md),
    [persistent-edge fixed-trace alignment](results/hc7_persistent_edge_fixed_trace_alignment.md),
    [rooted persistent incident edges](results/hc7_rooted_persistent_model_edge.md),
    [multi-protected rooted persistence](results/hc7_multi_protected_persistent_model_edge.md),
    [joint persistence or exact-seven separation](results/hc7_joint_persistent_edge_or_exact_seven.md),
    [persistent support-class structure](results/hc7_persistent_support_class_refinement.md),
    [joint-pair colouring fork](results/hc7_joint_persistent_incident_colour_fork.md),
    [one-extra-colour critical kernel](results/hc7_one_extra_colour_boundary_kernel.md),
    [boundary-crossing persistent-edge reduction](results/hc7_boundary_crossing_persistent_edge_reduction.md),
    [total trace rejection](results/hc7_total_trace_rejection_kernel.md),
    [aligned two-edge bypass or donor separation](results/hc7_aligned_two_edge_bypass_separator.md),
    [two-full-shore boundary absorption](results/hc7_two_full_shore_boundary_absorption.md),
    and [cycle-boundary completion](results/hc7_cycle_boundary_completion.md),
    each with an adjacent internal audit.  The fixed compressed three-path
    quotient is closed by
    [three explicit minor models](results/hc7_atomic_three_path_quotient_completion.md),
    but the missing label-preserving compression into that quotient remains
    open.

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
