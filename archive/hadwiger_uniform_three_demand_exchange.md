# A uniform three-demand exchange theorem for packet shores

## Status

This note proves a fixed-linkage capture-or-web trichotomy and its exact
separator and operation-state consequences.  It does not compare two
different realizations of a common demand.  In the packet-triangle
application, web--web, capture--web, and capture--capture exchanges all
remain open.

## 1. Portal demands

Let `C` be a connected graph lying behind a boundary `S`.  Fix six
nonempty portal sets

\[
 A_i,B_i\subseteq V(C)\qquad(i=1,2,3).             \tag{1.1}
\]

An **`i`-carrier** is a connected vertex set meeting both `A_i` and
`B_i`.  An `I`-linkage, for `I subseteq {1,2,3}`, is a family of
pairwise disjoint `i`-carriers, one for every `i in I`.

This set-terminal formulation is the one actually supplied by a cyclic
packet at a full shore.  No representative is chosen in advance, and a
carrier is allowed to contain portals belonging to an omitted demand.
That last point is essential.

## 2. The rail-web theorem

### Theorem 2.1 (third carrier, capture, or alternating rail web)

Suppose `C` contains an `{i,j}`-linkage.  Then the two carriers may be
enlarged to disjoint connected adjacent sets `L_i,L_j`.  Let `k` be the
remaining index.  At least one of the following holds.

1. **Triple linkage.**  There is a `k`-carrier disjoint from
   `L_i union L_j`.
2. **Portal capture.**  One of the residual portal sets

   \[
      U=A_k-(L_i\cup L_j),\qquad
      V=B_k-(L_i\cup L_j)                           \tag{2.1}
   \]

   is empty.
3. **Alternating rail web.**  Both `U,V` are nonempty and disjoint.
   Contract `L_i,L_j` to adjacent vertices `ell_i,ell_j`, and add
   artificial terminals `alpha,beta` adjacent to the images of `U,V`.
   Suppress loops and parallel edges.  The resulting simple
   four-terminal graph is crossless for the cyclic frame

   \[
                         (\alpha,\ell_i,\beta,\ell_j),             \tag{2.2}
   \]

   and hence has a same-vertex completion to a generalized Two Paths
   web with that alternating frame.

The alternatives are certificates with actual carriers and actual
residual portal sets; (2.2) is not a symbolic ordering of independently
chosen representatives.

#### Proof

Join the two original carriers by a shortest path
`p_0...p_m` in `C`, where only `p_0,p_m` lie in the old carriers.  If
`m=1` they are already adjacent.  Otherwise choose `0<=t<m`, absorb
`p_1,...,p_t` into the first carrier and
`p_{t+1},...,p_{m-1}` into the second, allowing either list to be empty.
The edge across the cut between those two portions (using an old-carrier
endpoint when a portion is empty) makes the enlarged sets adjacent.  They
remain disjoint and connected and retain all terminal contacts.

If a vertex belongs to `U intersect V`, its singleton is a `k`-carrier
disjoint from the rails, giving outcome 1.  If one residual set is empty,
outcome 2 holds.  Assume therefore that `U,V` are nonempty and disjoint.

If `C-(L_i union L_j)` contained a `U`--`V` path, its vertex set would be
a `k`-carrier disjoint from the rails, again giving outcome 1.  Thus no
such path exists.

In the contracted graph, an `(alpha,beta)` path disjoint from an
`(ell_i,ell_j)` path avoids both contracted rail vertices.  Lifting its
interior would give precisely the forbidden `U`--`V` path outside the
rails.  In particular the direct edge `ell_i ell_j` may serve as the
second path.  Hence the four-terminal tuple is crossless.  The four
vertices `alpha,ell_i,beta,ell_j` are distinct, and its alternating pairs
are exactly `(alpha,beta)` and `(ell_i,ell_j)`.  The generalized Two
Paths Theorem (Humeau--Pous, Theorem 1.5) says that a graph with a
crossless tuple embeds, by adding edges on the same vertex set, in a web
whose frame is that tuple.  This is the asserted completion. \(\square\)

### Corollary 2.2 (pairwise packets have three certified failures)

If all three two-demand subfamilies are linkable but no triple linkage
exists, applying Theorem 2.1 to each packet gives, for every omitted
demand, either portal capture or an alternating rail web.  If only two
packets sharing one demand are known, it gives two such certificates
whose rail systems share a demand label but need not share the same
carrier.

The common carrier cannot be identified without an additional exchange
argument.  Different two-linkages may realize the shared portal demand
in disjoint or crossing parts of the shore.

## 3. What seven-connectivity adds

Return to a seven-connected graph `G` with a seven-boundary `S`, two
full shores `C,D`, and no nested exact seven-cut inside `C`.  From this
point assume that the portal sets are actual boundary classes,

\[
 A_i=N_C(a_i),\qquad B_i=N_C(b_i)
 \quad(a_i,b_i\in S).                              \tag{3.0}
\]

In the matching-packet application the six labels are distinct.  For every
nonempty proper `Y subset C`,

\[
 \partial_S(Y)=(N_C(Y)-Y)\mathbin{\dot\cup}N_S(Y)                \tag{3.1}
\]

separates `Y` from `D`.  Hence

\[
                         |\partial_S(Y)|\ge8.                     \tag{3.2}
\]

Indeed, order below seven contradicts connectivity and order seven is
the excluded nested adhesion.  Any order-seven cut here is a minimum cut;
the standard minimum-cut argument makes every component behind it full to
the cut.

### Lemma 3.1 (capture has genuine multiplicity)

Assume `|C|>=2`.  Under (3.2), every boundary label has at least two
portal vertices in `C`.  Thus a capture outcome of Theorem 2.1 captures a
set of order at least two in the union of the two actual rails.

#### Proof

If a boundary label `s` had the unique portal `z`, take
`Y=C-{z}`.  Then

\[
 |N_C(Y)-Y|\le1,qquad |N_S(Y)|\le6,
\]

contrary to (3.2).
\(\square\)

### Lemma 3.2 (off-rail web cells are large or descend)

Consider the set `K` of original, nonterminal vertices inserted in one
clique cell of the web in Theorem 2.1, excluding its supporting facial
triangle `T`, and suppose `T` contains neither contracted rail vertex.
Let `P=N_S(K)`.  Then one of the following holds.

1. `|P|>=5`;
2. `G` has a vertex cut of order at most six; or
3. `N_G(K)` is an exact seven-cut nested inside `C`, and every component
   behind it is full to that cut.

Consequently, in the strict seven-connected no-descent row, every
off-rail cell contacts at least five boundary labels.  Every remaining
low-contact cell is incident with a contracted rail and is therefore a
genuine rail bridge, not an arbitrary planar insertion.

#### Proof

Lift each ordinary vertex of `T` to itself.  If `T` uses `alpha` or
`beta`, replace that artificial terminal by the corresponding boundary
label.  Because `T` avoids the contracted rails, this produces a set
`hat T` of order at most three accounting for all neighbours of `K`
inside `C` represented by the web.  Every other neighbour of `K` is a
boundary contact.  Therefore

\[
                         N_G(K)\subseteq\widehat T\cup P.         \tag{3.3}
\]

The opposite full shore lies beyond this set.  If `|P|<=3`, (3.3) gives
a cut of order at most six.  If `|P|=4`, either the union still has order
at most six or it has order seven; seven-connectivity forces equality in
(3.3) in the latter case, giving the nested exact cut.  Since it is a
minimum cut, every component behind it is full: if one missed a cut
vertex, the other six would already separate that component.  These
exhaust the cases with `|P|<5`. \(\square\)

This is the strongest connectivity consequence available without
replacing a whole rail by a bounded portal set.  A facial triangle which
contains `ell_i` lifts to the entire, potentially unbounded carrier
`L_i`; treating it as a three-vertex separator would be invalid.

## 4. Proper-minor states make the web rigid

Assume now that `G` is proper-minor-minimal non-six-colourable.  Extend a
packet crossing to a connected covering split

\[
                            C=X\mathbin{\dot\cup}Y.                \tag{4.1}
\]

Let `e in E(X,Y)`, and let `Pi_e` be the equality partition of `S`
induced by a six-colouring of `G-e`.

### Theorem 4.1 (packet transition rigidity)

For every interface edge `e`,

\[
 \Pi_e\in {\cal E}_6(C-e,S)\cap {\cal E}_6(D,S),
 \qquad
 \Pi_e\notin {\cal E}_6(C,S).                     \tag{4.2}
\]

Moreover, if the ends of `e` have common colour `gamma`, then for every
other colour `delta` either

1. the `gamma/delta` subgraph contains an internal detour joining the
   ends of `e`; or
2. the two endpoint components are distinct and both are anchored at
   `S`.

Thus no boundary-fixing sequence of switches supported in the rail web
can repair `e`: such a repair would extend `Pi_e` over the unoperated
shore, contradicting (4.2).

#### Proof

The first membership in (4.2) is the operated-side restriction of the
colouring, and the second is its unchanged opposite-side restriction.
If `Pi_e` extended over `C`, align colour names on its blocks and glue it
to the restriction on `D`; this would six-colour `G`.  Hence the last
nonmembership.

The detour-or-two-anchors assertion is Theorem 2.1 of
`hadwiger_bad_split_interface_exchange.md`: switching an unanchored
bichromatic endpoint component would separate the endpoint colours and
restore `e`.  The final statement is exactly the same repair
contradiction expressed inside the web. \(\square\)

### Corollary 4.2 (opposite packet states are disjoint)

A **faithful shore operation** here means a nontrivial proper-minor
operation supported wholly in the open shore, disjoint from `S`, which
leaves the opposite closed shore literally unchanged.  Faithful
operations in the two different shores cannot induce the same boundary
equality state.  Otherwise use the colouring operated in `D` on the
closed `C` side and vice versa; each operation is absent from the shore
we retain, and the common boundary restrictions glue to a six-colouring
of `G`.

Hence a surviving alternating rail web is not merely topological.  It is
**state-rigid**:

* every off-rail cell has at least five boundary contacts or descends;
* captured portal sets have real multiplicity on the rails;
* every interface deletion has a partition-changing or boundary-anchored
  obstruction; and
* the two shores use disjoint transition states.

This incorporates the opposite shore, but it does not yet eliminate the
rail-containing web cells.  Abstract state novelty alone cannot do so;
the transition-diamond construction in
`hadwiger_boundary_state_diamond_counterexample.md` realizes incompatible
one-shore transition families without the required clique-minor geometry.

## 5. Sharp counterexamples to stronger formulations

### Example 5.1 (portal multiplicity and all pair packets do not imply a triple)

Take two hubs `x,y`.  For each of the six endpoint labels create two
portal vertices, each adjacent to both hubs and to no other shore vertex.
Pair the six portal classes into three demands.

Any two demands have disjoint carriers, one through `x` and one through
`y`.  Every carrier contains a hub, so three disjoint carriers are
impossible.  Every portal class has order two.  The separator `{x,y}` is
therefore the sharp capacity certificate.

### Example 5.2 (a three-connected shore still needs the capture outcome)

Let `C` be the triangular prism with triangles `023` and `145` and
matching edges `01,25,34`.  Use singleton portal pairs

\[
                         02,\qquad13,\qquad45.                    \tag{5.1}
\]

Every two demands are linkable:

\[
 02\mid(1-4-3),\qquad 02\mid45,
 \qquad(1-0-3)\mid45.                              \tag{5.2}

There is no triple linkage.  All six prism vertices are prescribed
endpoints, so a triple would require all three demand edges, but `13` is
absent.  The prism is three-connected.  In (5.2), however, a path for
`13` consumes a portal of the omitted demand.  Thus Theorem 2.1 returns
portal capture rather than a small separator.  This proves that capture
cannot be deleted even under three-connectivity.

The first two examples are replayed by
`three_demand_exchange_counterexamples.py`.

### Example 5.3 (three-connectivity and clean packets do not remove the web)

Let `C` have vertex set `{0,...,7}` and edge set

\[
\begin{split}
\{&01,02,05,06,13,16,17,23,24,25,26,27,37,\cr
   &45,46,56,57,67\}.
\end{split}                                                   \tag{5.3}
\]

Use the singleton portal pairs

\[
                         04,\qquad12,\qquad35.                 \tag{5.4}
\]

This graph is three-connected.  All three two-demand packets have clean
linkages:

\[
 (0-6-4)\mid(1-7-2),\qquad
 (0-6-4)\mid(3-7-5),\qquad
 (1-6-2)\mid(3-7-5).                            \tag{5.5}
\]

No displayed carrier uses a terminal of the omitted demand, yet there is
no triple linkage.  In each displayed packet the two carriers are already
adjacent, the two omitted terminals remain outside them, and those omitted
terminals have no connecting path after the rails are deleted.  Thus
Theorem 2.1 returns its genuine alternating-web outcome, not capture, for
each displayed packet.  Even three-connectivity together with clean
pairwise packets therefore does not remove the web branch.  This example
is also checked exhaustively by
`three_demand_exchange_counterexamples.py`.

## 6. Application to the seven-edge packet residue

For each fully positive packet triangle in
`hadwiger_equality_seven_edge_packet_funnel.md`, Lemma 3.1 there supplies
all three two-demand packets across the two shores, while positivity
forbids a simultaneous triple linkage in either shore.  By pigeonhole,
one shore owns at least two packets sharing one demand.  Corollary 2.2
therefore gives two actual capture/rail-web certificates in that shore.

The two certificates may use different carriers for their common demand.
Theorem 2.1 leaves exactly three certificate combinations.  They are
different exchange problems; portal multiplicity does not identify their
rails or turn a capture certificate into a web certificate.

1. **Web--web.**  Both packets return alternating rail webs.  The remaining
   target is the following common-rail exchange.

> **Common-rail exchange.**  Two state-rigid alternating rail webs in one
> full shore share a portal demand.  Either their two realizations of that
> demand can be exchanged to a common rail, producing the forbidden triple
> linkage, or their nonexchangeability exposes a bounded rail-containing
> adhesion whose transition state is accepted by the opposite shore.

2. **Capture--web.**  One packet captures an endpoint portal class of its
   omitted demand in its two rails, while the other packet returns a
   state-rigid alternating web.  The required new statement is a
   **captured-rail transfer**: either transfer the multiply represented
   captured class across the other packet's web to make a triple linkage,
   or expose a bounded gluable adhesion.  Nothing proved above aligns the
   captured rails with the web rails.

3. **Capture--capture.**  Both packets capture endpoint portal classes,
   in two potentially unrelated rail systems which merely share a demand
   label.  The required new statement is a **double-capture exchange**:
   use the two multiply represented captured classes to make a triple
   linkage, or expose a bounded gluable adhesion.  Lemma 3.1 supplies at
   least two portals in each captured class, but it supplies neither a
   common carrier nor a common rail web.

The first outcome of any of these exchange statements would close all
seven fully positive packet types; the second is the exact
state-gluing/descent output needed globally.  What is proved here is the
uniform capture-or-web trichotomy for each owned packet.  What remains
unproved is all three comparisons above.  In particular, pigeonhole plus
portal multiplicity does **not** reduce the capture--web or
capture--capture branches to the common-rail web--web exchange.
