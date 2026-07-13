# Active rooted quadruples: facial coherence or a labelled clique

## 1. Status and purpose

This note isolates a uniform part of the first-owner/first-rotation
problem in the normalized near-`K_7` route.  It does not prove `HC_7`.
It proves that a four-connected obstruction page cannot change one
state-forcing root at a time while changing its rural rotation.  All
such one-coordinate changes live on one common face.  Consequently a
genuine first conflict must do one of two things:

1. produce the rooted `K_4` which the biportal completion turns into
   `K_7`; or
2. lose at least two state-forcing coordinates at one interface.

The second outcome is a precise capacity failure, not another rotation
case.  It is exactly the point at which a faithful minor-state theorem is
still needed.

The result is independent of the Moser labels, the orders of the portal
classes, and the number of pieces in the surrounding web.

## 2. A face-coherence theorem for rooted quadruples

Let `H` be either a four-connected graph, or a three-connected graph
with a fixed plane embedding.  An ordered quadruple

\[
                 X=(x_1,x_2,x_3,x_4)
\]

always has four distinct entries.  Write `|X|` for its underlying set.
Call two quadruples **elementarily adjacent** if their underlying sets
have at least three common vertices.  For a family `mathcal X` of
quadruples, let `Gamma(mathcal X)` be the graph with this adjacency.

### Theorem 2.1 (three-overlap facial coherence)

Let `mathcal X` be a nonempty family of quadruples in a graph `H` of one
of the following two types:

* `H` is four-connected; or
* `H` is three-connected and planar.

For every connected component `mathcal C` of
`Gamma(mathcal X)`, one of the following holds.

1. Some `X in mathcal C` has an `X`-rooted `K_4` minor in `H`.
2. `H` is planar, and there is one face `F_mathcal C` in the unique plane
   embedding of `H` whose boundary contains every vertex occurring in a
   quadruple of `mathcal C`.

In particular, all quadruples in `mathcal C` inherit one coherent facial
rotation.

#### Proof

Assume outcome 1 does not hold.  Fix `X_0 in mathcal C`.  In the
four-connected case, the rooted-`K_4` theorem says that `H` is planar and
the four vertices of `X_0` occur on one face `F_0`.  In the already
planar three-connected case, the planar case of the same rooted theorem
puts the four roots on a common face.  Since `H` is three-connected, its
plane embedding is unique up to reflection.  Also, the boundaries of two distinct faces have at
most two vertices in common.  Indeed, three common boundary vertices in
a three-connected plane graph would give two distinct facial cycles with
three common vertices, contradicting the standard face-intersection
property (equivalently, two distinct faces meet in at most one edge).

Let

\[
                 X_0,X_1,\ldots,X_m=X
\]

be a path in `Gamma(mathcal X)`.  Inductively suppose that all vertices
of `X_{j-1}` lie on `F_0`.  By the rooted-`K_4` theorem, all vertices of
`X_j` lie on some face `F_j`.  The faces `F_0,F_j` share the at least
three vertices in `|X_{j-1}| cap |X_j|`; hence `F_j=F_0`.  Thus every
quadruple in the component lies on `F_0`, proving outcome 2.  \(\square\)

The number three is sharp for this proof and for the conclusion.  Two
different faces of a three-connected plane graph may share the two ends
of an edge.

There is also a concrete disconnected-family witness.  In the
four-connected planar square-antiprism graph `C_8^2`, the four even
vertices and the four odd vertices bound its two square faces.  Neither
quadruple has a rooted `K_4`, but the two facial orders plainly do not
belong to one common face.  Their underlying sets are disjoint, so they
lie in different components of `Gamma`.  Thus some transport hypothesis
between the active tuples is indispensable even in a four-connected
planar page.

### Corollary 2.2 (four portal families collapse to one face)

Let `P_1,P_2,P_3,P_4` be pairwise disjoint nonempty vertex sets in a
graph `H` satisfying either hypothesis of Theorem 2.1.  Then either

1. some transversal `p_i in P_i` has a rooted `K_4` minor; or
2. `H` is planar and one face contains

\[
                         P_1 union P_2 union P_3 union P_4.
\]

#### Proof

Take as `mathcal X` all ordered transversals.  Any two transversals can
be joined by changing one coordinate at a time, so
`Gamma(mathcal X)` is connected.  Apply Theorem 2.1.  \(\square\)

This is a set-rooted strengthening of the usual cofacial alternative.
It requires no finiteness assumption on the four portal sets.

The pairwise-disjointness of the portal sets can be removed.  What is
really needed is a system of distinct representatives.

### Theorem 2.3 (SDR facial coherence)

Let `P_1,...,P_4` be nonempty, possibly overlapping vertex sets in a
graph `H` satisfying Theorem 2.1.  Let `mathcal B` be the family of
four-element sets which are the images of systems of distinct
representatives of `(P_1,...,P_4)`.  If `mathcal B` is nonempty, then
either

1. some representative quadruple has a rooted `K_4`; or
2. `H` is planar and one face contains every portal vertex which occurs
   in at least one full system of distinct representatives.

#### Proof

The partial transversals of `(P_1,...,P_4)` are the independent sets of
its transversal matroid.  Hence `mathcal B` is the set of bases of a
rank-four matroid.  The basis-exchange graph is connected: from bases
`B,B'`, if `B ne B'`, basis exchange gives

\[
             x in B-B',\qquad y in B'-B,
             \qquad (B-x) union \{y\}\text{ a basis},
\]

and this strictly increases the intersection with `B'`; iteration joins
the two bases by one-element exchanges.  Choose an SDR ordering for each
basis.  Consecutive bases give quadruples whose underlying sets share
three vertices, so all such quadruples lie in one component of
`Gamma`.  Theorem 2.1 proves the dichotomy.  \(\square\)

For completeness, the invoked exchange fact can be obtained directly by
superposing matchings from the four index vertices to `B` and to `B'`:
an alternating component starting at an element of `B'-B` ends at an
element of `B-B'`, and flipping that component gives the displayed
one-element basis exchange.

### Corollary 2.4 (fixed disjoint lobes give the full active product)

Let `D_1,...,D_4` be pairwise disjoint connected subgraphs outside `H`,
and put

\[
                         P_i=N_H(D_i).
\]

Suppose there are common sets `B,T,R,U`, disjoint from `H` and the
`D_i`, such that `B,R,U` are connected, `T` is nonempty, and all
hypotheses of the biportal completion concerning `B,T,R,U` hold; also
suppose every `D_i` is adjacent to `B,T,U`.  If `p_i in P_i` are
distinct, then

\[
                         E_i=D_i union \{p_i\}
\]

are private extensions: they are connected, pairwise disjoint, and meet
`H` exactly in their named roots.  Therefore every SDR is an active
quadruple.  If the portal family has rank four, Theorem 2.3 gives `K_7`
or puts every usable portal of all four fixed lobes on one face.

#### Proof

Connectivity follows from the definition of `P_i`; disjointness follows
from disjointness of the lobes and of the representatives.  The external
contacts are unchanged when the root is adjoined.  Apply Theorem 2.3 and
the definition of active.  \(\square\)

This is the promised product principle.  No independent choice of portal
roots has to be postulated: it is supplied by the fixed lobes.  A failure
of the product has exactly two forms--Hall rank below four, or two desired
coordinate roles living in one connected lobe rather than in disjoint
lobes.

## 3. The labelled `K_7` completion

The face theorem becomes a near-`K_7` exchange only for roots whose
rooted bags can be expanded without losing their labels.  The following
definition makes that requirement explicit.

Let `G` contain a subgraph `H` satisfying either hypothesis of Theorem
2.1.  Call a quadruple
`X=(x_1,x_2,x_3,x_4)` **active** if there are connected extensions
`E_1,...,E_4` and disjoint connected sets `B,R,U`, together with a
nonempty set `T`, satisfying all hypotheses of the uniform biportal
rooted-core theorem, with

\[
                     E_i cap V(H)=\{x_i\}.
\]

Thus every `X`-rooted `K_4` model in `H`, after adjoining its four
private extensions, completes with the three reserve/pool bags to a
literal `K_7` model in `G`.  The extensions and reserve data may depend
on `X`; only their existence for the selected tuple is used.

### Theorem 3.1 (active-family rotation exchange)

Let `mathcal X` be a family of active quadruples in a graph `G`, all
rooted in the same subgraph `H` satisfying Theorem 2.1.  If `G` has no `K_7`
minor, then for every connected component `mathcal C` of
`Gamma(mathcal X)` there is one face of `H` containing every active root
which occurs in `mathcal C`.

Consequently two active quadruples which differ in at most one root can
never prescribe incompatible rural rotations in a target-free graph.

#### Proof

If an active quadruple had a rooted `K_4` in `H`, the private extensions
and the uniform biportal rooted-core theorem would give a `K_7` minor.
Hence outcome 1 of Theorem 2.1 is impossible for every component of
`Gamma(mathcal X)`, and outcome 2 gives the asserted common face.
\(\square\)

### Corollary 3.2 (one-coordinate owner changes are harmless)

Suppose consecutive rural pieces expose active four-owner states
`X_0,...,X_m` in one four-connected or planar three-connected obstruction
page, and each transition
retains at least three actual active roots.  If `G` has no `K_7` minor,
all the states use one common facial order (up to the one global
reflection of the page).

Thus the first owner-set change which genuinely breaks rural coherence
must simultaneously destroy at least two of the four active-root
coordinates, or must leave the selected page.

#### Proof

The sequence is a path in `Gamma(mathcal X)`.  Apply Theorem 3.1.  A
transition which cannot be represented by adjacent active quadruples has
lost at least two coordinates.
\(\square\)

In the normalized applications, leaving a planar three-connected page is
recorded by its named three-separator or by a portal-deficient lobe.  The
corollary deliberately does not count a contracted carrier as one
separator vertex in the original graph.

## 4. Annular composition and the exact first conflict

The preceding theorem composes with the existing literal-column and
disk-expansion theorems as follows.

### Theorem 4.1 (active rural-chain trichotomy)

Consider a retained chain of rural pages in a normalized near-`K_7`
model.  Assume:

1. every page obstruction is four-connected or planar three-connected;
2. at each interface four actual disjoint columns join an active
   quadruple on one page to an active quadruple on the next, and these
   columns have the common pool/reserve contacts required by the
   biportal four-column completion; and
3. the union outside two fixed singleton labels is exactly the pages,
   the column annuli, and their rural expansions.

Then one of the following holds.

1. `G` contains a labelled `K_7` minor;
2. all page orders and column permutations are compatible, and deleting
   the two fixed labels leaves a planar graph;
3. at the first failed interface fewer than four state-forcing columns
   exist, or the active tuple on one side cannot be changed to the one on
   the other through three-overlap active tuples.

In outcome 3 every such active-tuple route loses at least two coordinates
at one transition.

#### Proof

At an interface with four columns, contract the columns.  If the two
facial orders, after applying the column bijection, differ, the two-cycle
rotation exchange gives a rooted `K_4` whose bags contain the four named
columns.  The pool/reserve contacts assumed in item 2 and the biportal
four-column completion give outcome 1.

Otherwise the interface is an annulus with compatible boundary orders.
Within a page, Theorem 3.1 shows that changing one active coordinate does
not change the distinguished face or its rotation.  If this succeeds at
every interface, glue the rural disks to the compatible annuli.  The
port-labelled disk-expansion theorem gives a plane drawing after deleting
the two fixed labels, which is outcome 2.

If the construction stops for the first time, either the four columns do
not exist or the active states lie in different components of the
three-overlap graph.  In the latter case every route between them has a
step sharing at most two coordinates.  This is exactly outcome 3.
\(\square\)

Outcome 2 is the coherent two-apex alternative and is six-colourable.
The theorem therefore removes rotation as an independent obstruction in
the active-overlap-saturated family.

## 5. Exact remaining axiom and sharpness

Theorem 4.1 identifies the missing statement without referring to a
Moser label or to a finite portal catalogue:

> **Two-coordinate state-forcing exchange.**  At the first interface at
> which at least two active coordinates disappear, either the missing
> private extensions can be rerouted to restore a four-column active
> tuple, or the failed extensions lie on opposite sides of one actual
> adhesion and faithful proper-minor operations on those sides realize a
> common full-boundary equality state.

The first outcome re-enters Theorem 4.1 and gives `K_7` or coherent
two-apex structure.  The second outcome six-colours the graph by the
boundary-faithful crossed-minor theorem.

This axiom cannot be weakened to class incidence, path capacity, or
ordinary rurality.

* The two-star complementary-`K_{3,3}` network in
  `../archive/hadwiger_gate_a_combined_network_round.md` has combined linkage
  surplus and nonrural cross-lobes, but loses complementary state rows
  and has no full typed split.
* The four-common-owner zero-row host in
  `../archive/hadwiger_four_common_owner_biportal_application.md` already has the
  rooted `K_4` core, but no free reserve positive on all six protected
  bags.  It shows why **active** must include private extensions and the
  reserve, rather than only a root in the torso.
* The leaf expansion of `K_7^vee` in
  `../archive/hadwiger_seven_view_state_cocycle_exchange.md` realizes the retained
  equality states independently.  It shows why colourability of the
  proper retained views is weaker than a faithful operation state at the
  failed interface.

Accordingly, the first rural conflict is no longer a general rotation
problem.  Four-connected active pages and all one-coordinate owner
changes are closed.  The exact residual is a simultaneous loss of two
state-forcing coordinates at a gate/three-separator, coupled to the full
proper-minor boundary relation.

## 6. Interface with the full-state bi-Helly theorem

The new conclusion fits the existing Gate A split exactly.

* If every retained carrier takes the full typed-shore outcome of
  `../archive/hadwiger_full_state_shore_bihelly.md`, every two-by-two contact graph
  has a perfect matching.  The signed-cocycle/matching theorem applies,
  and no rotation question remains.
* Otherwise one gate, cycle, or 3-connected torso meets every carrier of
  one state half.  In a cycle or planar 3-connected torso, any four
  state-forcing private extensions define active roots.  Theorems 3.1
  and 4.1 eliminate every rotation change connected by one-coordinate
  exchanges.
* Hence the torso branch no longer asks for arbitrary global rotation
  synchronization.  It asks for exactly one local assertion: at a named
  lobe or adhesion where two active coordinates disappear together,
  recover them as disjoint extensions or synchronize the full faithful
  boundary state.

The last bullet is still unproved.  It is also the exact feature absent
from the complementary two-star counterarchitecture, so it cannot be
replaced by ordinary Menger capacity.

## 7. In a one-complex shell every dark torso lobe is exact-seven

For the spanning one-complex normalization the two-coordinate residue
has an additional sharp property.  Put

\[
                         V(G)=L\mathbin{\dot\cup}B,
                         \qquad |L|=6,
\]

where the vertices of `L` are the six literal singleton labels and `B`
is the complex bag.  Let `W` be a bag in an adhesion-at-most-two tree
decomposition of `B`.

### Lemma 7.1 (dark-lobe exactness)

Let `G` be seven-connected and let `K` be a component of `B-W` such that

\[
                         |N_B(K)|\le2.
\]

If `K` misses at least one singleton label, then it misses exactly one
label, `|N_B(K)|=2`, and

\[
                 N_G(K)=N_B(K)\mathbin{\dot\cup}
                         (L-\{\ell\})                         \tag{7.1}
\]

for its unique missed label `ell`.  In particular `N_G(K)` is an actual
seven-vertex separator.  Every component behind this separator is full
to all seven of its vertices.

#### Proof

All neighbours of `K` lie either in `N_B(K)` or among the six literal
labels.  Since one label is missed,

\[
                         |N_G(K)|\le2+5=7.                    \tag{7.2}
\]

The missed label lies outside `K union N_G(K)`, so `N_G(K)` genuinely
separates `K` from another vertex.  Seven-connectivity gives
`|N_G(K)|>=7`; hence equality holds throughout (7.2).  Therefore the
bag adhesion has order two and precisely five labels see `K`, proving
(7.1).  In particular a lobe missing two labels would have neighbourhood
at most six and is impossible.

Finally, if a component `C` of `G-N_G(K)` missed one separator vertex,
the other six vertices of the separator would separate `C` from that
vertex.  Seven-connectivity forbids this.  Thus every component is full
to the separator.  \(\square\)

### Corollary 7.2 (two-coordinate loss is bilateral exact-seven)

In the one-complex shell, apply the full-state bi-Helly theorem to a
Tutte decomposition of `B`.  Every off-torso lobe which loses a singleton
state row lies behind the exact seven-cut (7.1), and one lobe cannot lose
two distinct singleton rows.  Consequently the simultaneous loss of two
active coordinates from Section 5 must occur in two different exact-seven
lobes (or involve an intercarrier row in a multi-complex view).

Thus, in the unique-complex-bag case, the remaining exchange is narrower
again:

> **Bilateral exact-seven exchange.**  Two retained dark lobes, each full
> to its own exact seven-boundary and missing a different singleton row,
> either reroute two private active extensions, give the labelled
> `K_7`, or have opposite faithful operations with one common transported
> boundary state.

#### Proof

The bi-Helly theorem gives adhesion at most two and a named missed row.
Lemma 7.1 applies to each such lobe.  Its proof also shows that no one
lobe can account for two missed singleton rows.  \(\square\)

This does not prove the bilateral exchange.  It does show that arbitrary
portal placement and arbitrary rural rotation have disappeared from the
one-complex residue: the only dynamic obstruction is a pair of literal
minimum separators with different missing-row labels.

## 8. Collision-to-exact-core theorem

The preceding results now give a rigorous version of the suggested
"split a shared extension lobe" step.

Fix two extension roles in the one-complex bag `B`.  A connected carrier
of the first role must meet a family of singleton portal rows
`mathcal P_0`, and a carrier of the second role must meet
`mathcal P_1`; include in both families every neutral/model row which has
to survive in the final rooted bags.  Let `mathcal L,mathcal R` be the
families of inclusion-minimal connected carriers for the two roles.

### Theorem 8.1 (shared role collision: split or exact-seven core)

In a seven-connected one-complex shell, at least one of the following
holds.

1. There are disjoint carriers `L in mathcal L`, `R in mathcal R`.
   They extend to an adjacent connected shore bipartition of `B`, so the
   two colliding extension roles are separated while every row included
   in their definitions is retained.
2. One bag `W` of the Tutte decomposition of `B` meets every member of
   `mathcal L`, or meets every member of `mathcal R`.  Its torso is a
   gate of order at most two, a cycle, or a 3-connected torso.  Every
   component of `B-W` which is relevant to the obstructed family misses
   a named singleton row and lies behind an actual exact seven-cut of the
   form (7.1).

Thus a collision of two roles cannot propagate through an arbitrary
block tree.  It either resolves into two disjoint full-row extensions, or
is concentrated in one torso with all of its dark off-torso lobes already
converted into literal minimum separators.

#### Proof

Apply the full-state shore/bi-Helly theorem to the two carrier families.
If disjoint carriers exist, its spanning-tree extension lemma gives the
adjacent connected bipartition in outcome 1.  Otherwise its cross-Helly
conclusion gives one Tutte bag meeting every carrier of one family, and
each off-bag component relevant to that family misses one of its required
rows and attaches to `W` through at most two vertices.

All required rows in the present one-complex statement are literal
singleton portal rows.  Lemma 7.1 therefore turns every such dark
component into the exact seven-cut (7.1).  The standard Tutte torso types
give the displayed list.  \(\square\)

### Corollary 8.2 (the only nonexact collision is one active torso)

In outcome 2, suppose the obstruction torso is a cycle or planar
3-connected graph.  If four fixed, pairwise disjoint extension lobes at
that torso have portal rank four, then either their active roots give
`K_7`, or every usable root lies on one common face of the torso.  If,
in addition, the surrounding quotient and all other societies are already
in the compatible rural branch, and these usable roots include every
attachment occurrence in the remaining expansion after deleting two
fixed singleton labels, rural disk substitution makes the graph
two-apex.

Otherwise the failure is one of the following exact objects:

1. a Hall-deficient portal family of rank at most three in the one torso;
2. two desired roles still share one connected lobe in the torso; or
3. a named attachment occurrence is not carried by any full SDR.

#### Proof

The rank-four assertion is Corollary 2.4.  Common-face coverage of every
remaining occurrence is precisely the hypothesis of the port-labelled
disk-expansion theorem, which gives the two-apex conclusion.  Negating
rank four, disjoint fixed lobes, and occurrence coverage gives the three
listed alternatives.  \(\square\)

Theorem 8.1 is the promised collision-to-exact-gate principle.  It closes
the entire block-tree part of the two-coordinate loss without enumerating
portals.  What remains inside the one torso is now a rank-three Hall core,
a shared-lobe core, or one unusable occurrence; outside the torso every
failure is an exact seven-interface carrying the faithful operation
relation.

## 9. Rank deficiency has only two bouquet geometries

There is a final label-free simplification when the four desired fixed
extensions are four different off-torso components.  By Lemma 7.1 every
one has exactly two torso attachments.

### Lemma 9.1 (four two-sets without an SDR)

Let `P_1,P_2,P_3,P_4` be two-element sets.  If they have no system of
distinct representatives, then at least one of the following holds.

1. Three of the sets are the same two-set.
2. The union of all four sets has order at most three.

More precisely, a minimal Hall-deficient subfamily has either three
members with union two, or four members with union three.

#### Proof

Let `I` be an inclusion-minimal Hall-deficient subfamily.  A one-member
subfamily has union two, and two two-sets have union at least two, so
`|I|>=3`.  Hall deficiency gives

\[
                         \left|\bigcup_{i in I}P_i\right|
                         \le |I|-1.
\]

If `|I|=3`, the union has order at most two; since every member has order
two, all three members are the same set.  If `|I|=4`, the union has order
at most three.  These exhaust the possibilities.  \(\square\)

### Corollary 9.2 (exact-seven bouquet reduction)

In the one-complex shell, let four pairwise disjoint dark off-torso lobes
be the proposed fixed private extensions.  If their attachment portal
family has rank below four, then either

1. three exact-seven lobes have the same two torso poles; or
2. all four exact-seven lobes attach through one set of at most three
   torso vertices.

Thus the Hall-deficient branch is a two-pole triple bouquet or a
three-pole four-bouquet.  It is not an arbitrary rank-three portal
system.

#### Proof

Lemma 7.1 says that every attachment set has order exactly two and every
lobe lies behind its displayed exact seven-cut.  Apply Lemma 9.1.
\(\square\)

Both bouquets admit coherent rural realizations, so connectivity alone
does not exclude them.  Their **full literal-row data**, however, does.

### Corollary 9.3 (bouquet rank deficiency is impossible)

In either one-complex near-`K_7` normalization, four fixed dark lobes
have portal rank four in every `K_7`-minor-free graph.

#### Proof

The six singleton labels contain `K_6-{ab,ac}`.  Theorems 3.1 and 4.3
of `../archive/hadwiger_near_k7_bouquet_static_closure.md` show that the two-pole
triple bouquet and the at-most-three-pole four-bouquet each contain a
literal `K_7` model.  These are exactly the two outcomes of Corollary
9.2.  QED.

Thus Hall rank deficiency is not a remaining state counterarchitecture.
For four distinct fixed off-torso lobes, the active-root argument always
has an SDR.

### Corollary 9.4 (every actual portal occurrence is usable)

For four distinct fixed dark lobes in a `K_7`-minor-free one-complex
shell, every actual lobe--torso portal occurrence belongs to a full
role-respecting SDR.

#### Proof

If a named occurrence were unusable, the incidence-Hall classification
in `../archive/hadwiger_near_k7_unusable_occurrence_closure.md` would produce three
near-complete connected lobe bags forming a literal triangle.  Lemma 2.2
of the bouquet closure completes those bags with the singleton core to a
`K_7` model.  QED.

Thus neither portal rank nor occurrence coverage is a remaining
state counterarchitecture for four distinct dark lobes.  The live
first-conflict residue is a genuine shared-lobe/shared-reserve collision:
two desired roles consume the same connected material.  This is not a
two-pole or three-pole bouquet and still requires a carrier-splitting or
faithful exact-seven exchange theorem.
