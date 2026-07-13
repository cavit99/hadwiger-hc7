# Common-carrier exchange from cubic rural reconstruction

## 1. Status and point of the theorem

This note closes two uniform parts of the common-carrier gate left by
`hadwiger_two_role_loss_exact_gate_exchange.md`.

1. The exceptional `K_5/K_{3,3}` atom in critical rural reconstruction
   disappears completely when the live society contains a
   three-connected shore of order at least seven and **every edge of the
   shore** may be deleted faithfully.  Contractions are not needed.
2. The exact order-eight Hall gate produced by two prescribed private
   roots already contains two adjacent, full, root-labelled carriers.
   No portal-order enumeration is needed at that gate.

Together they give a deletion-local common-carrier principle: if every
one-edge-deleted view yields either the labelled carrier split, a faithful
state splice, or the prescribed rural disk, then the unoperated minimum
shore yields the same trichotomy.  In particular there is no residual
framed Kuratowski atom in the minimum `C_6 dotcup K_1` cell.

The theorem is deliberately stated at the level at which a generalized
Two Paths/web theorem is used.  Such a theorem has to supply the
per-deletion alternative in one fixed society order.  The result below
then performs the operation-to-unoperated reconstruction uniformly; it
does not assume that a virtual torso edge is a literal graph edge.

## 2. Edge-deletion rural reconstruction in minimum degree three

Let `(J,Omega)` be a society and let `F_Omega(J)` be the fixed wheel
frame from `hadwiger_critical_rural_operation_composition.md`.  Let `D`
be a subgraph of `J`.  Call the edges of `D` live; the frame edges and
all edges outside `D` remain fixed.

### Theorem 2.1 (cubic deletion-rural reconstruction)

Assume

\[
                         \delta(D)\ge3                         \tag{2.1}
\]

and, for every `e in E(D)`, the society `(J-e,Omega)` is rural in the
displayed order.  Then either `(J,Omega)` is rural or

\[
                          |V(D)|\le6.                           \tag{2.2}
\]

In particular, if `D` is three-connected and has at least seven
vertices, then `(J,Omega)` is rural.

#### Proof

Suppose `(J,Omega)` is not rural.  By the wheel-frame equivalence, the
fixed framed graph

\[
                          F=F_\Omega(J)
\]

is nonplanar.  Choose in `F` a Kuratowski subdivision `K`, of `K_5` or
`K_{3,3}`.

Fix `e in E(D)`.  If `e` were not an edge of `K`, the same subdivision
would survive in `F-e`.  But `(J-e,Omega)` is rural, so the wheel-frame
equivalence makes `F-e` planar.  Therefore

\[
                          E(D)\subseteq E(K).                    \tag{2.3}
\]

For every `x in V(D)`, (2.1) and (2.3) give

\[
                          d_K(x)\ge d_D(x)\ge3.                  \tag{2.4}
\]

In a subdivision of `K_5` or `K_{3,3}`, the vertices of degree at least
three are precisely the branch vertices.  There are respectively five
or six of them.  Hence every vertex of `D` is a branch vertex of `K`,
and (2.2) follows.  The last assertion is immediate.  QED.

The improvement over the general critical-rural theorem is important.
There, deletion shows that every live edge belongs to one Kuratowski
subdivision and contraction is then used to suppress long branch paths.
Here minimum degree three already forbids a shore vertex from lying
internally on a branch path.  Thus deletion states alone eliminate the
atom.

### Corollary 2.2 (minimum exact-seven shore reconstruction)

Let `D` be the minimum full shore in the audited
`C_6 dotcup K_1` exact-seven cell.  Let `(J,Omega)` be any fixed-order
society containing `D` in which every edge of `D` is a live edge.  If
every `(J-e,Omega)`, `e in E(D)`, is rural, then `(J,Omega)` is rural.

#### Proof

The minimum fragment is three-connected, and Corollary 4.5 of
`hadwiger_full_deletion_propagation.md` gives `|D|>=7`.  Apply Theorem
2.1.  QED.

No boundary vertex is contracted in this argument.  Thus the conclusion
is compatible with a fixed labelled society and with the equality-state
adhesion used for crossed splicing.

## 3. Deletion-local web exchange

The following form is the interface with a Two Paths/web theorem.  A
**labelled split certificate** means two disjoint adjacent connected
role carriers retaining every required neutral/model row.  By the
full-state shore theorem it may be enlarged to a full typed shore pair.
A **splice certificate** means two opposite boundary-faithful proper
operations inducing the same equality state on their common adhesion.

### Theorem 3.1 (deletion-local carrier/web trichotomy)

Let `G` be proper-minor-minimal non-six-colourable, let `D` be the
minimum shore of Corollary 2.2, and fix two singleton labels `p,q`.
Assume the retained material of `G-{p,q}` consists of

* a fixed plane quotient;
* already rural pieces in their prescribed face orders; and
* one society `(J,Omega)` containing all of `D`.

Assume also that, for every edge `e in E(D)`, at least one of the
following has been proved in the edge-deleted view.

1. There is a labelled split certificate; its branch sets avoid the
   deleted edge and lift unchanged to `G`.
2. There is a splice certificate with an operation in the opposite open
   shore.
3. `(J-e,Omega)` is rural in the prescribed quotient order.

Then at least one of the following holds in `G`.

1. The two common-carrier roles split label-faithfully (and hence the
   retained near-clique completion gives `K_7`).
2. A faithful equality state cross-splices, so `G` is six-colourable.
3. `G-{p,q}` is planar; in particular `G` is coherently two-apex and
   six-colourable.

#### Proof

If outcome 1 or 2 of the edge-deleted analysis occurs for any `e`, its
certificate already gives conclusion 1 or 2.  Indeed edge deletion does
not identify labels, and every edge present in the certificate is an
edge of the original graph.  In the splice case the
boundary-faithful crossed-minor theorem applies by definition.

We may therefore assume that outcome 3 occurs for every `e in E(D)`.
Corollary 2.2 makes the unoperated society `(J,Omega)` rural in the same
prescribed order.  Substitute that rural disk and the already rural
pieces into their named quotient faces.  The prescribed rural-disk
composition lemma draws all of `G-{p,q}` in the plane.  This is
conclusion 3.  QED.

### Corollary 3.2 (two-path representable common carrier)

In Theorem 3.1, suppose the two carrier roles have been reduced, after
the protected rows are fixed, to a four-terminal network with the
following certified implication for every `e in E(D)`:

* the desired two-linkage expands to the labelled split certificate;
* failure of the linkage gives the prescribed rural/web view, unless a
  named web adhesion carries the faithful splice certificate.

Then the common-carrier gate has exactly the three conclusions of
Theorem 3.1.  In particular a `K_5` or `K_{3,3}` operation-minimal
nonrural residue cannot remain.

#### Proof

Apply the certified Two Paths/web implication separately to every
edge-deleted view, and then apply Theorem 3.1.  QED.

The certification clause is essential: a generic web may contain
clique-filled facial pieces and virtual edges.  They have to be expanded
through the named lobes, or converted to a faithful adhesion state,
before the second bullet is valid.

## 4. The exact order-eight gate has a literal carrier split

The next lemma is independent of rurality and closes the exact-eight
alternative whenever it comes from two prescribed private root labels.

Let `S` be a cut and let `D,H` be distinct components of `G-S`, with
`H` full to `S`.  Let `p,q in S` be any two distinct private role
labels.  Take

\[
                    A\subseteq S,\qquad
                    U=\bigcup_{a\in A}N_D(a).                    \tag{4.1}
\]

Let `C` be a component of `D-U` such that

\[
                    N_G(C)=U\mathbin{\dot\cup}(S-A).             \tag{4.2}
\]

Thus (4.2) is the order-`|S|+1` gate supplied by the tight Hall failures
in the full-deletion and two-role-loss notes.  The private labels may
belong to `A`; this makes no difference to the split.

### Theorem 4.1 (root-absorbing exact-eight split)

Under (4.1)--(4.2), the two sets

\[
             L_p=C\cup U\cup\{p\},\qquad
             L_q=H\cup\{q\}                                  \tag{4.3}
\]

are disjoint, connected and adjacent.  Moreover, for every
`s in S-{p,q}`, each of `L_p,L_q` has an edge to `s` (unless it contains
that label), so both carriers retain every common literal row.

Consequently an exact order-eight gate caused by two prescribed private
root labels is already an abstract `S`-full two-carrier outcome.  It is
the labelled outcome whenever the five retained frame bags are the
shore-free rows represented by `S-{p,q}`.  If protected cores still lie
inside `D` or `H`, model-cleanliness must be checked before (4.3) is used;
the theorem does not silently preserve such cores.

#### Proof

The union in (4.2) is disjoint because `U subseteq D` and `S` is disjoint
from `D`.  Equality (4.2) says, in particular, that every vertex of `U`
has a neighbour in `C`, and that `C` has a neighbour at every vertex of
`S-A`.  If `p notin A`, it is adjacent to `C`; if `p in A`, it has a
neighbour in `U` by the definition of `U` and fullness of `D` to `S`.
Hence `C union U union {p}` is connected.
The set `H union {q}` is connected because `H` is full to `S`.

The displayed sets are disjoint: `C union U subseteq D`, the shores
`D,H` are disjoint, and `p ne q`.  If `q notin A`, they are adjacent
through an edge from `C` to `q`; if `q in A`, they are adjacent through
an edge from `U` to `q`.

Let `s in S-{p,q}`.  If `s in A`, the definition of `U` gives an edge
from `s` to `U subseteq L_p`; if `s notin A`, (4.2) gives an edge from
`s` to `C subseteq L_p`.  The full shore `H` has an edge to every
`s in S`, so `L_q` also retains the row.  This proves every assertion.
QED.

### Corollary 4.1a (literal clique completion)

If, in addition, `G[S-{p,q}]` is complete, then `G` has a `K_7` minor
when `|S|=7`.

#### Proof

Use the seven branch bags

\[
                 L_p,\quad L_q,\quad
                 \{s\}\ (s\in S-\{p,q\}).                    \tag{4.4}
\]

Theorem 4.1 supplies every adjacency involving `L_p,L_q`, and the five
singleton bags form a clique by hypothesis.  QED.

### Corollary 4.2 (Theorem 5.5 has no geometric order-eight residue)

In the minimum exact-seven cell, apply Theorem 5.5 of
`hadwiger_full_deletion_propagation.md` to distinct prescribed
occurrences of the two private role labels `p,q`.  If its SDR outcome
fails, its exact order-eight outcome gives the two carriers (4.3).

Thus, after a shore-free labelled completion is fixed, failure to retain
the two private roots cannot terminate at order eight: it either descends
to a smaller exact-seven fragment before Theorem 5.5 is applied, or it
gives the labelled carrier split directly.

#### Proof

The Hall witness in Theorem 5.5 is a set
`A subseteq S-{p,q}` and its equations are exactly (4.1)--(4.2).  Apply
Theorem 4.1.  QED.

The qualifier **private role labels** matters.  Absorbing `p` and `q`
into (4.3) is legitimate precisely because they are the roots of the two
new bags.  One must not absorb a fixed pool bag merely because its portal
row is common to both roles.

### Corollary 4.3 (the duplicated-common-row gate also splits)

Suppose the exact-eight outcome of Theorem 3.3 in
`hadwiger_two_role_loss_exact_gate_exchange.md` occurs while the two
roles have distinct private labels `p,q in S`.  Then the two carriers in
(4.3) exist, whether or not `p` or `q` belongs to the tight Hall witness
`A`.

Thus the exact-eight exception to duplicating a common literal row is a
root-capacity exception only for prescribed occurrences.  Geometrically,
once the two private role roots may be absorbed into their two new bags
and the retained frame is shore-free, the gate itself separates the
roles.

#### Proof

Theorem 3.3 supplies exactly (4.1)--(4.2), with no restriction on the
membership of `p,q` in `A`.  Theorem 4.1 was deliberately proved in that
generality.  QED.

## 5. Consequence for the sharp common-carrier gate

Combine the results as follows.

* Literal root loss is excluded by proper-subfamily contraction
  stability and by Theorem 5.5.
* An order-eight gate caused by the two private roots gives the explicit
  split (4.3).
* In the remaining exact-seven torso, a deletion-wise Two Paths/web
  analysis only has to output a labelled split, a faithful splice, or a
  prescribed rural view.  Theorem 3.1 reconstructs the unoperated view
  and eliminates the former framed Kuratowski atom.

Therefore the live common-carrier obstruction is narrower than in the
previous ledger: it must be a failure of the **per-deletion faithful web
certificate** inside one exact-seven torso.  It cannot be an exact-eight
two-root gate, and it cannot be an operation-minimal `K_5/K_{3,3}`
nonrural atom spread over the whole minimum shore.

This is an infinite-family closure, not an incidence classification.  A
remaining proof must now establish the certified two-path implication in
Corollary 3.2 (or directly exhibit the common equality state at its named
web adhesion).  Once that implication is available, the common-carrier
gate is closed by the theorems above.

## 6. One common row is a four-root problem

There is one important case in which the certified web implication is
automatic.  Suppose all neutral/model contacts have already been made
role-private and the only row still required by both roles is one literal
row `T`.  Let `P,Q` be their two private root rows.  The four demands are

\[
                            P,\quad Q,\quad T,\quad T.            \tag{6.1}
\]

A four-element set is **feasible** if it is the image of an SDR of
(6.1).  The exact model-clean data are the following.

* `F_1,...,F_5` are pairwise disjoint, pairwise adjacent, nonempty
  connected protected bags, all disjoint from `R`.
* Every rooted model used below has all four of its bags contained in
  `R`; in particular none invades a protected bag.
* For every feasible ordered quadruple `(p,q,x,y)` and every rooted
  `K_4` model `B_p,B_q,B_x,B_y` selected for it, both unions
  `B_p union B_x` and `B_q union B_y` are adjacent to every `F_i`.

Call these conditions **clean support**.  The last bullet may be checked
row-wise before the rooted model is selected: it is enough that the
private extension attached to each of the four roots is disjoint from
the protected frame and that each of the two prescribed pairings retains
all five frame contacts.  Merely knowing that the unpaired carrier `R`
touches every `F_i` is not enough.

### Lemma 6.1 (rooted `K_4` pairs a duplicated row)

Let `(p,q,x,y)` be an SDR of (6.1).  If a graph `R` contains a rooted
`K_4` model at these four roots and the support is clean, then `R`
contains two disjoint adjacent connected role carriers, one containing
`p` and a member of `T`, the other containing `q` and a different member
of `T`.  Together with `F_1,...,F_5`, they form a literal `K_7` model.

#### Proof

Let the four rooted branch bags be `B_p,B_q,B_x,B_y`.  Put

\[
                         L=B_p\cup B_x,qquad
                         M=B_q\cup B_y.                         \tag{6.2}
\]

The bags within each displayed union are adjacent, so `L,M` are
connected.  They are disjoint, and they are adjacent because every bag
of the rooted `K_4` is adjacent to every other bag.  Their roots give
the private rows `P,Q` and two distinct occurrences of `T`.  Cleanliness
retains the already assigned neutral/model contacts.  More explicitly,
the seven branch bags are

\[
                   L,\quad M,\quad F_1,\ldots,F_5.              \tag{6.3}
\]

They are nonempty, connected and pairwise disjoint.  The five `F_i` are
pairwise adjacent by the protected-frame hypothesis; `L` and `M` are
adjacent through any edge between a bag in the first rooted pair and a
bag in the second; and each of `L,M` is adjacent to every `F_i` by the
last clean-support bullet.  Hence (6.3) is a `K_7` model.  QED.

### Theorem 6.2 (single-common-row face exchange)

Let `R` be either four-connected or planar and three-connected.  Assume
the demand family (6.1) has an SDR and has clean support.  Then one of the
following holds.

1. The two roles have the labelled carrier split of Lemma 6.1, and the
   protected frame completes it to `K_7`.
2. `R` is planar and one face contains every portal occurrence which
   belongs to at least one SDR of (6.1).

If the second set of occurrences is the whole attachment set of the
retained expansion and all other pieces are rural in the induced order,
then outcome 2 is the coherent two-apex branch.

#### Proof

Regard the two copies of `T` as two indexed members of a four-set
transversal system.  Its feasible four-sets are the bases of the
associated transversal matroid.  Apply the SDR facial-coherence theorem
(`hadwiger_near_k7_active_root_face_exchange.md`, Theorem 2.3) to the
four portal sets `P,Q,T,T`.

If one feasible quadruple has a rooted `K_4`, Lemma 6.1 gives outcome 1.
Otherwise the facial-coherence theorem gives one face containing every
occurrence in a feasible SDR.  This is outcome 2.  Under the final
coverage hypothesis, prescribed rural-disk substitution after deleting
the two fixed apex labels gives the coherent two-apex conclusion.  QED.

### Corollary 6.3 (strict Hall supplies the duplicated-row rank)

Let `P_s=N_D(s)` be the portal rows of the minimum exact-seven shore and
let `p,q,t in S` be distinct.  Then the four demands

\[
                         P_p,\quad P_q,\quad P_t,\quad P_t       \tag{6.4}
\]

have an SDR.  More generally the same holds after adding one copy of
each row in any set `I subseteq S-{p,q,t}` for which
`{p,q,t} union I` is a proper subset of `S`.

#### Proof

Apply Hall's theorem to the demand multiset.  A subfamily using at most
one copy of each literal row has union at least one larger than its order
by strict Hall surplus.  A subfamily using both copies of `P_t` has, say,
`k` other distinct rows.  Its distinct label set has order `k+1` and is
proper in `S`, so its union has order at least `k+2`, exactly the number
of demands in the subfamily.  Hall holds.  QED.

Thus an isolated single common literal row is not a mysterious
two-carrier object.  It is a duplicated coordinate of a rank-four
transversal matroid.  In every four-connected or planar three-connected
page, it either pairs through a rooted `K_4` or enters the already
coherent facial branch.  The residual common-carrier gate must therefore
violate at least one of the explicit hypotheses above: it has a composite
reserve rather than one literal row, its neutral support is not clean, or
it is trapped at a genuine three-separator/nonplanar torso where a
faithful state splice is still required.

## 7. Releasing contaminated protected cores

The clean-support condition in Section 6 can be weakened in exactly the
direction needed by one common reserve.  A contaminated protected bag
need not be routed off the new carriers: it may be released and replaced
by one extra group of rooted branch bags.

### Lemma 7.1 (two-core release completion)

Let `F_1,...,F_5` be a protected `K_5` frame.  Let
`I subseteq [5]`, with `|I|=k<=2`, and put

\[
                         \mathcal F=\{F_i:i\notin I\}.            \tag{7.1}
\]

Suppose `B_1,B_2,B_3,B_4` are the bags of a `K_4` model such that

1. the `B_j` are disjoint from every retained bag in `mathcal F` (they
   may contain vertices formerly assigned to the released bags `F_i`,
   `i in I`); and
2. every `B_j` is adjacent to every retained bag in `mathcal F`.

Then `G` contains a `K_7` minor.

#### Proof

Partition `{1,2,3,4}` into `k+2` nonempty parts.  This is possible for
`k=0,1,2`; the part-size patterns may be chosen as

\[
                         2+2,\qquad 2+1+1,\qquad 1+1+1+1.        \tag{7.2}
\]

For a part `J`, put `C_J=union_{j in J}B_j`.  Since the four original
bags are pairwise adjacent, each `C_J` is connected.  Different `C_J`
are disjoint and adjacent.  Assumptions 1--2 say that they are disjoint
from and adjacent to every retained `F_i`.

There are `k+2` grouped bags and `5-k` retained frame bags, for a total
of seven.  The grouped bags form a clique model, the retained bags form
a clique model, and every cross pair is adjacent.  These seven bags form
a `K_7` model.  QED.

This count is sharp for a four-bag rooted core: releasing three protected
bags would require five replacement bags, while a `K_4` supplies only
four before additional geometry is used.

### Theorem 7.2 (single-common-row exchange with core contamination)

Let `I subseteq[5]`, `|I|<=2`, be the protected bags which may be
contaminated by the common carrier/reserve.  Put

\[
             R_I=G-\bigcup_{i\notin I}V(F_i),                    \tag{7.3}
\]

and suppose one four-connected block or planar three-connected page `R`
of `R_I` contains the portal rows `P,Q,T` of (6.1).  Assume:

1. `P,Q,T,T` has an SDR in `R`;
2. for every feasible SDR, any rooted `K_4` model selected at its four
   roots is contained in `R_I` and every one of its bags is adjacent to
   every retained `F_i`, `i notin I`; and
3. all other attachment occurrences of the retained expansion are
   covered by the same page society.

Then either `G` contains a `K_7` minor or all feasible portal occurrences
lie on one face of `R`.  If the remaining pieces have the compatible
rural rotations, the latter outcome is coherent two-apex.

#### Proof

Apply the SDR facial-coherence theorem to `P,Q,T,T` in `R`.  A rooted
`K_4` outcome satisfies Lemma 7.1 with precisely the released set `I`,
and therefore gives `K_7`.  Otherwise all feasible occurrences lie on
one face.  The coverage and compatibility hypotheses give the rural
disk substitution and hence the two-apex conclusion.  QED.

### Corollary 7.3 (one indispensable reserve is not model-dirty)

Suppose the only failure of clean support in Theorem 6.2 is that the
common literal carrier/reserve consumes one protected frame bag.  Release
that bag.  If the resulting rooted page retains adjacency to the other
four protected bags, Theorem 7.2 applies with `|I|=1`.

Thus protected-core contamination by the one indispensable row does not
create a new carrier gate: it gives `K_7` through the `2+1+1` grouping,
or it enters the same coherent facial branch.  No actual seven/eight
adhesion is needed for this case.

#### Proof

All four rooted bags are allowed to use the released protected material,
but remain disjoint from and adjacent to the other four protected bags.
Lemma 7.1 replaces the released bag and the two desired role bags by
three grouped rooted bags.  The facial alternative is Theorem 7.2.  QED.

The exact remaining model-clean obstruction is now explicit and
strictly smaller.  Either at least three protected bags are unavoidably
contaminated, or some rooted branch bag loses adjacency to a retained
protected core.  In the latter case choose the first lost core.  The
full-state bi-Helly theorem applied with that core's contact row gives a
labelled split or localizes the loss behind an adhesion of order at most
two; in the literal one-complex shell such an off-torso lobe lies behind
an actual exact seven/eight boundary.  What is not yet proved is that a
loss located *inside the same nonplanar three-connected torso* always
produces the faithful opposite-shore state.  That is the remaining
minor-transition branch, not contamination by the single reserve.

### Lemma 7.4 (a literal contaminated row leaves only the torso)

Let `S` be the minimum exact-seven boundary, `D` its minimum shore, and
let `Z` be a bag of an adhesion-at-most-two decomposition of `D`.  If a
component `C` of `D-Z` misses a literal required row `s in S`, then

\[
              N_G(C)\subseteq (S-\{s\})\mathbin{\dot\cup}Z_C,
              \qquad Z_C=N_D(C)\cap Z,\quad |Z_C|\le2.          \tag{7.4}
\]

Consequently `|N_G(C)|` is seven or eight.  The order-seven outcome
contradicts the minimum choice of `D`; hence every proper off-torso
literal contamination is an exact order-eight gate.

If this boundary is additionally the tight Hall gate
`N(C)=U dotunion(S-A)` of Section 4, the two desired roles have distinct
private labels, and at most two protected frame bags are released, then
it is handled by Theorem 4.1 followed by Lemma 7.1, provided the retained
frame is shore-free.  An arbitrary exact-eight boundary need not have
that Hall form.

#### Proof

The component has no neighbour in `s`, all its neighbours outside `D`
belong to `S`, and the decomposition puts all its neighbours in `Z`
inside one adhesion of order at most two.  This proves (7.4).  The missed
vertex `s` lies outside `C union N(C)`, so the displayed set is a genuine
separator.  Seven-connectivity gives

\[
                       7\le |N_G(C)|\le8.                       \tag{7.5}
\]

If equality is seven, `C` is a component behind a seven-cut and is a
proper subset of `D`, contradicting the definition of the minimum shore.
Thus only order eight remains.  Under the additional Hall-form
hypothesis, the last assertion invokes the explicit root-absorbing
carriers of Theorem 4.1 and the branch-counting release of Lemma 7.1;
its model-clean proviso is exactly their stated hypothesis.
QED.

Therefore a first literal-row contamination cannot wander through a
block tree.  It either releases through Lemma 7.1, enters one exact
order-eight model-clean gate, or is contained in the unique common torso.
This is the promised contamination-to-adhesion theorem.  It does not
claim that a nonliteral protected core is one separator vertex.

## 8. Sacrifice the common reserve instead of duplicating it

The preceding release count does not actually require the contaminated
bag to be a literal portal row.  This removes the principal distinction
between a common literal carrier and a composite reserve.

Let `F_0,F_1,F_2,F_3,F_4` be a protected `K_5` frame.  The bag `F_0` is
the one common carrier/reserve consumed by the two failed roles.  Let
`P_1,...,P_4` be the four private active-root rows after `F_0` is
released.

Call the release **properly supported** when, for every feasible root
quadruple and every rooted `K_4` model at it, the four rooted bags can be
expanded to bags `B_1,...,B_4` satisfying

1. `B_1,...,B_4` are pairwise disjoint, nonempty and connected;
2. they are pairwise adjacent (the rooted `K_4` supplies these
   adjacencies);
3. they are disjoint from `F_1,...,F_4`; and
4. every `B_i` is adjacent to every retained bag `F_j`, `1<=j<=4`.

No condition is imposed on adjacency to, or disjointness from, `F_0`:
that bag has been released and its vertices may be distributed among
the `B_i` only in pairwise disjoint pieces.  Proper support must therefore be checked after the
four expansions are chosen; four separate expansions which all reuse
the same vertices of `F_0` do not satisfy item 1.

### Theorem 8.1 (common-reserve sacrifice)

Let `R` be four-connected or planar and three-connected.  Suppose

1. the portal family `P_1,...,P_4` has rank four;
2. releasing `F_0` is properly supported in the preceding sense; and
3. every attachment occurrence of the retained expansion belongs to a
   rank-four SDR of the portal family.

Then either `G` contains a `K_7` minor or all usable root occurrences lie
on one face of `R`.  With compatible rural rotations of the remaining
pieces, the second outcome is coherent two-apex.

#### Proof

Apply the SDR facial-coherence theorem to `P_1,...,P_4`.  If it gives a
rooted `K_4`, expand it to `B_1,...,B_4` by proper support and release
`F_0`.  Lemma 7.1 with `I={0}` groups the four rooted bags in the pattern
`2+1+1`; together with `F_1,...,F_4` they form a literal `K_7` model.

For clarity, after relabelling the four rooted bags the seven branch bags
are

\[
           B_1\cup B_2,\quad B_3,\quad B_4,\quad
           F_1,\quad F_2,\quad F_3,\quad F_4.                  \tag{8.1}
\]

The first bag is connected through a `B_1-B_2` edge.  The first three
bags are pairwise adjacent because the `B_i` form a `K_4` model.  The
last four are pairwise adjacent because they are a protected `K_4`
subframe.  Every cross adjacency is item 4 of proper support, and all
seven bags are disjoint by items 1 and 3.  This is the complete
branch-set audit.

If there is no rooted `K_4`, facial coherence puts every occurrence in a
rank-four SDR on one face.  Item 3 covers the whole retained attachment
set, and compatible disk substitution gives the coherent two-apex
outcome.  QED.

### Corollary 8.2 (the true common-carrier gate is an expansion failure)

In the sharp two-role-loss setting, assume the four literal active roots
survive the operation and the only common object is one carrier/reserve
bag `F_0`.  If deleting `F_0` from the protected frame leaves four
pairwise disjoint private expansions satisfying items 1--4 above, then
the gate is closed by Theorem 8.1; no duplication or palette labelling
of `F_0` is required.

Thus a surviving same-torso obstruction must say something stronger than
"both roles use one reserve".  It must assert that after the reserve is
released, at least two of the four private expansions still overlap or
one loses contact with a retained protected bag.  Full-state bi-Helly
then localizes that exact expansion failure; off-torso literal losses are
the seven/eight adhesions of Lemma 7.4.  Only an overlap wholly inside the
common nonplanar torso remains eligible for a faithful minor-transition
state exchange.

### Corollary 8.3 (a pure common reserve is closed)

Suppose `F_0` is a reserve in the literal sense: before it is added, the
four private expansions are already pairwise disjoint connected sets,
already pairwise adjacent through the rooted page, and already adjacent
to each retained `F_1,...,F_4`; their only common requirement is
adjacency to the separate bag `F_0`.  Then release is properly supported
automatically, and Theorem 8.1 closes the gate.

#### Proof

Deleting `F_0` from the list of protected bags changes none of the four
private expansions or their mutual/retained-frame adjacencies.  They are
the bags `B_1,...,B_4` required in the definition of proper support.
Apply Theorem 8.1.  QED.

Hence the word "reserve" should no longer appear in the final unresolved
alternative.  A survivor must be a genuine **common carrier**: releasing
the named bag still leaves overlap or disconnection among the private
expansions.
