# Binary attained duties: a facial cycle or a labelled gate

**Status:** proved and independently audited after the explicit attainment
and disjoint-packet scope repairs below.  The abstract theorem
is label-free.  It converts every 4-connected binary-duty packet obstruction
into one literal alternating facial cycle, and otherwise exposes a labelled
gate of order at most three.  Its pure-Moser corollary is an independent
structural route through a subfamily which is already subsumed by the
stronger audited complete two-component Moser closure; novelty is claimed
for the uniform cycle-or-gate mechanism, not for that Moser conclusion.

## 1. The graph-theoretic theorem

Let `J` be a graph with six pairwise distinct terminals

\[
        a_0,a_1,b_0,b_1,d_0,d_1.
\]

Call

\[
        A=\{a_0,a_1\},\qquad
        B=\{b_0,b_1\},\qquad
        D=\{d_0,d_1\}
\]

the three **binary duties**.  A linkage for two duties is a pair of
vertex-disjoint paths, one joining the two terminals of each duty.  This is
equivalent to two vertex-disjoint connected carriers for those two fixed
terminal pairs: take a path inside each carrier in one direction, and the
two paths themselves in the other.

### Theorem 1.1 (three binary duties on one face)

Suppose `J` is 4-connected and none of the three pairs of duties
`(A,B),(A,D),(B,D)` has a linkage.  Then `J` is planar and, in its unique
plane embedding, one facial cycle contains all six terminals.  On that
cycle the two terminals of every two duties alternate.  Consequently its
duty word is, up to rotation, reversal, and renaming the duties,

\[
                         A\ B\ D\ A\ B\ D.              \tag{1.1}
\]

#### Proof

Apply the Two Paths Theorem to the ordered four-tuple

\[
                         (a_0,b_0,a_1,b_1).              \tag{1.2}
\]

The missing `A,B` linkage says precisely that this tuple is crossless.
In the web-completion form of the theorem, `J` is a spanning edge-subgraph
of a 4-web whose frame is (1.2).  Such a web consists of a plane rib, with
frame (1.2) bounding the outer face, and a clique inserted into any facial
triangle, each inserted vertex having no neighbour outside that clique and
the three vertices of the triangle.

No inserted clique can contain a vertex of `J`.  Indeed, let `T` be its
attachment triangle.  At least one of the four frame vertices lies outside
`T`.  If the inserted clique were nonempty, deleting the three vertices of
`T` would separate its vertices from that frame vertex in the spanning
subgraph `J`, contrary to 4-connectivity.  Thus every vertex of `J` is a
rib vertex.  The inherited plane embedding of `J` has one face containing
`a_0,b_0,a_1,b_1` in that alternating order.  Indeed, deleting rib edges
can only merge the old outer face with inner faces.  Each frame vertex
remains incident with the resulting outer face; because `J` is
2-connected its boundary is one Jordan cycle, and four points inherited
from the old frame cannot change their circular order on that cycle without
a crossing.  Call this facial cycle `F_AB`.

Repeat the argument for `(a_0,d_0,a_1,d_1)` and
`(b_0,d_0,b_1,d_1)`.  It gives facial cycles `F_AD` and `F_BD`, possibly
first presented in different plane embeddings.  The graph `J` is
3-connected and planar, so Whitney uniqueness identifies all three
embeddings up to reflection.

The vertices `a_0,a_1` are nonadjacent.  Otherwise the edge `a_0a_1`
together with a `b_0-b_1` path in the connected graph
`J-\{a_0,a_1\}` would be an `A,B` linkage.  Similarly, the two members of
each of `B,D` are nonadjacent.

In a 3-connected plane graph, two distinct facial cycles meet in at most
one edge; in particular, they cannot contain the same two nonadjacent
vertices.  The cycles `F_AB,F_AD` both contain the nonadjacent pair
`a_0,a_1`, so they are equal.  The cycles `F_AB,F_BD` both contain the
nonadjacent pair `b_0,b_1`, so they too are equal.  Denote the common
facial cycle by `F`.

The respective web completions show on `F` that `A,B` alternate, that
`A,D` alternate, and that `B,D` alternate.  Fix the two occurrences of
`A`.  Each open `A-A` arc contains one `B` and one `D`.  After interchanging
`B,D` if necessary, their order on the first arc is `B,D`; alternation of
`B,D` forces the same order on the second arc.  This is exactly (1.1).
\(\square\)

The web-completion form used here is Theorem 1.5 of S. Humeau and D. Pous,
*On the Two Paths Theorem and the Two Disjoint Paths Problem*,
arXiv:2505.16431.  For a four-tuple it is the classical Two Paths Theorem
of Seymour and Thomassen.

## 2. Actual seven-adhesions turn failure into a labelled gate

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

be an actual separation in a 7-connected graph, with `L` nonempty.  Let
`C` be a component of `G[R]`.  Thus `C` has no neighbour outside
`C\cup S`.

### Corollary 2.1 (cycle or support-rich gate)

Fix six distinct terminals in `C`, paired into three binary duties, and
assume that no two duties have a linkage in `C`.  Then one of the following
holds.

1. `C` contains a cycle through the six terminals with duty word
   `A B D A B D`.
2. There is a vertex cut `X` of `C`, with `|X|=r<=3`, such that every
   component `K` of `C-X` satisfies

   \[
                         |N_S(K)|\ge 7-r.                \tag{2.1}
   \]

In outcome 2, `(K,X)` is a literal labelled lobe behind a gate of order at
most three.  In particular an order-three gate leaves support at least
four, an order-two gate leaves support at least five, and an order-one gate
leaves support at least six.

#### Proof

If `C` is 4-connected, Theorem 1.1 gives outcome 1.  Otherwise, since `C`
is connected, it has a vertex cut `X` of order `r<=3`.  Let `K` be any
component of `C-X`.  Every neighbour of `K` lies in `X\cup S`.  The
opposite open shore `L` is nonempty and has no edge to `K`, so `N_G(K)` is
a vertex separator in `G`.  Seven-connectivity gives

\[
  7\le |N_G(K)|
     =|N_C(K)|+|N_S(K)|
     \le r+|N_S(K)|,
\]

which is (2.1).  \(\square\)

This is the promised cycle-or-adhesion statement.  It deliberately does
not call a three-vertex gate an apex pair, and it does not claim that a
support-four lobe already reflects an arbitrary attained state.

There is, however, an exact state-specific description at a three-gate.
Suppose a legal proper-minor operation in the old opposite shore returns
the exact attained partition

\[
             \Pi=\{B_0,B_1,B_2,\{c\}\},                \tag{2.2}
\]

where the `B_i` are disjoint two-sets, every two `B_i` have a literal
boundary edge between them, and `c` has a boundary neighbour in every
`B_i`.  Thus the attained duties are exactly the three `B_i`.  Assume that
a second `S`-full packet `Q\subseteq R-C` in the same open shore as `C` is
available to fund the third duty.  (It is enough that a same-shore `Q` avoid
`K\cup K'\cup X\cup S` in the use below, but that weaker condition must be
checked rather than inferred in a connected rich shore.)

### Corollary 2.2 (the exact three-gate label certificate)

Let `C` be 3-connected, let `X` be a three-vertex cut, and for a component
`K` of `C-X` put

\[
        \mathcal F(K)=\{i:B_i\subseteq N_S(K)\}.         \tag{2.3}
\]

If the attained state (2.2) does not reflect, then:

1. every component of `C-X` is adjacent in `C` to all three vertices of
   `X`;
2. for distinct components `K,K'`, there are no distinct indices
   `i\in\mathcal F(K)` and `j\in\mathcal F(K')`; and
3. if `\mathcal F(K)` is empty, then

   \[
       N_S(K)=\{c\}\cup\{\text{one literal from each }B_i\}. \tag{2.4}
   \]

   In that case

   \[
                   \Omega_K=X\cup N_S(K)                \tag{2.5}
   \]

   is a literal separation boundary of order seven, `K` is
   `\Omega_K`-full, and the opposite open shore is nonempty.

Thus a nonreflecting three-gate is not an unlabelled support-four lobe: its
non-duty lobes have the exact `c`-plus-rainbow trace (2.4), while complete
duties cannot be distributed across two lobes with different names.
Equivalently, the family `(\mathcal F(K):K` a lobe`) has no two-set system
of distinct representatives.  Hence, if two of these funded-duty sets are
nonempty, their union is one common duty.  A single duty-bearing lobe may
fund several duties only when every other lobe is dutyless; the conclusion
does not silently assign two carriers inside that one lobe.

#### Proof

If a component `K` of `C-X` missed some `x\in X`, then the other two
vertices of `X` would separate `K` from another component of `C-X`,
contrary to 3-connectivity.  This proves item 1.

Suppose distinct lobes `K,K'` fund distinct duties `B_i,B_j`.  Choose any
`x\in X`.  The sets `K` and `K'\cup\{x\}` are connected and disjoint by
item 1, and they are adjacent because `K` also has an edge to `x`.  They
are therefore two adjacent duty-correct carriers.  The full packet `Q`
funds the remaining duty.  The literal edge between `B_i,B_j`, the
fullness of the third packet, and the assumed boundary neighbours from `c`
make the four representatives indexed by (2.2) a clique.  The audited
attained-state contraction and gluing argument reflects `Pi`, a
contradiction.  This proves item 2.

Finally, `N_C(K)=X` and `C` is a whole open-shore component, so

\[
                         N_G(K)=X\cup N_S(K).             \tag{2.6}
\]

The old opposite open shore is nonempty and anticomplete to `K`.  Hence
`N_G(K)` separates it from `K`, and seven-connectivity gives
`|N_S(K)|>=4` directly.  If no complete `B_i` lies in that support, it
contains at most one member of each of the three pairs, and hence at most
three vertices of `S-\{c\}`.  It must therefore contain `c` and one member
of every pair, with no fifth vertex available without completing a pair.
This is (2.4), and (2.6) now says `N_G(K)=\Omega_K` has order exactly seven.
Every member of `X=N_C(K)` and every member of `N_S(K)` has a literal
neighbour in connected `K`, so `K` is `\Omega_K`-full.  Deleting
`\Omega_K` leaves `K` and the old opposite shore on different nonempty
sides, proving (2.5).  \(\square\)

### Corollary 2.3 (strict exact-seven gate descent)

In the hypothetical `HC_7` counterexample, a dutyless lobe from
Corollary 2.2 is itself one open shore of a new actual exact-seven
separation with boundary `\Omega_K`.  The exact-seven packet-packing
theorem therefore applies anew.  In particular:

* every component of the new opposite open shore is `\Omega_K`-full;
* the new packing vector is, up to orientation, one of
  `(1,1),(1,2),(1,3)`; and
* the `(1,3)` outcome closes by the audited adaptive reflection theorem.

If neither direct closure occurs, the new exact-seven cell has shore `K`
strictly smaller than the old component `C`.

#### Proof

The first sentence and fullness of `K` are Corollary 2.2.  A component of
the opposite shore missing some member of `\Omega_K` would have neighbour
set of order at most six, contradicting seven-connectivity; hence every
such component is full.  Invoke the audited exact-seven packet theorem and
its `(1,3)` closure.

Finally, because `X` is a vertex cut, `C-X` has another component besides
`K`; hence `K` is a proper subset of `C`.  \(\square\)

This is a genuine descent, but not yet a proof of termination in a closed
cell: a descendant may be `(1,1)`, or its attained duties may no longer be
the binary state (2.2).  No preservation claim of that kind is hidden in
the corollary.

## 3. Exact pure-Moser consequence

Use the standard Moser boundary on `S=\{0,...,6\}` and the attained state

\[
 \Pi=\{A,B,D,\{6\}\},\qquad
 A=\{2,3\},\quad B=\{1,4\},\quad D=\{0,5\}.             \tag{3.1}
\]

Assume explicitly that a legal proper-minor operation in the thin shore
returns exactly the partition (3.1).  Nothing below infers this fixed state
from packet fullness.

The three blocks in (3.1) are pairwise adjacent in the literal boundary,
and literal `6` has a neighbour in each.  Hence two disjoint paths funding
any two of `A,B,D`, together with the other full exterior component funding
the third, reflect the exact state.  Adjacency of the first two
representatives comes from the corresponding literal block edge; their
carriers need not themselves be adjacent.

### Lemma 3.1 (specified portal matching)

Let `C` be a component of an open shore behind the actual seven-boundary,
and suppose `|C|>=m`.  Any prescribed set of `m<=7` literal boundary
vertices has `m` distinct portal representatives in `C`.

#### Proof

Let `A\subseteq S` be the prescribed set.  For every nonempty `B\subseteq A`,
if `|N_C(B)|<=|B|-1`, then `C-N_C(B)` is nonempty because
`|C|>=|A|>=|B|`.  The set

\[
                         N_C(B)\cup(S-B)
\]

has order at most six and separates a component of `C-N_C(B)` from the
nonempty opposite shore.  This contradicts seven-connectivity.  Hall's
theorem now matches `A` into `C`.  \(\square\)

### Corollary 3.2 (conditional independent 4-connected Moser route)

Under the explicit legal-attainment hypothesis preceding this corollary,
the two rich exterior components cannot both be 4-connected.

#### Proof

Let the rich exterior components be `C_1,C_2`, and let `T` be the disjoint
thin-side `S`-full packet.  First suppose a 4-connected `C_i` has order
five.  It is `K_5`.  Lemma 3.1 matches five boundary vertices to its five
vertices.  Enlarge the five clique vertices by their matched anchors, and
use `C_{3-i}` and `T`, each enlarged by one of the two remaining boundary
vertices.  These are seven literal pairwise adjacent branch sets, so `G`
has a `K_7` minor.

We may therefore assume `|C_i|>=6`.  Lemma 3.1 chooses in each component
six distinct portal representatives for the six literals in
`A\cup B\cup D`.  If one component contains a linkage for any two duties,
the preceding state-reflection observation six-colours `G`.  Otherwise
Theorem 1.1 gives in each component a cycle through its six selected
portals with duty word `A B D A B D`.

Apply the audited Moser cyclic-duty theorem to either cycle.  A
nonexceptional literal orientation gives a six-colouring or a literal
`K_7`.  Thus in a hypothetical counterexample both cycles have the unique
exceptional literal orientation, represented by

\[
                         2,4,5,3,1,0.                    \tag{3.2}
\]

The audited exceptional cyclic-packet completion theorem now applies to
the two cycles and the third disjoint full packet `T`, and gives a literal
`K_7` minor.  This contradiction proves the stated conclusion.  \(\square\)

The repository already contains the stronger audited theorem
`../results/hc7_exact7_moser_two_component_closure.md`, which closes the
entire pure-Moser two-component branch.  Corollary 3.2 is retained only to
show how Theorem 1.1 composes with the attained-duty and cyclic-packet
machinery without finite portal casework.

## 4. Guardrails and sharp scope

* **Why 3-connectivity does not give planarity.**  Start with a wheel on a
  six-cycle and glue two new vertices into one facial triangle so that the
  triangle and the two new vertices induce `K_5`.  Opposite rim pairs have
  the three pairwise linkage failures, but the resulting graph is
  3-connected and nonplanar.  The attachment triangle is exactly the
  three-gate retained by Corollary 2.1; the rim still supplies the desired
  cycle.  Thus the proof may not replace 4-connectivity by 3-connectivity
  and simply invoke Whitney planarity.
* **Why `K_{2,6}` is not a counterexample.**  For any two terminal pairs,
  route one pair through one degree-six vertex and the other pair through
  the second.  The two duty paths are disjoint.  It nevertheless warns that
  a theorem stated only in terms of a selected tree gate must retain a
  two-vertex adhesion outcome.
* The theorem is for binary duties.  A cycle through two selected portals
  does not fund an attained duty containing a third literal label.  No such
  palette-to-carrier lift is asserted.
* An internal cut of a packet subgraph need not be an actual shore
  adhesion.  Corollary 2.1 therefore assumes `C` is a whole component of
  the open shore.  That is the situation in the pure-Moser two-exterior
  application.

The natural strengthening is to replace 4-connectivity in Theorem 1.1 by
3-connectivity.  Exhaustive falsification has found no counterexample among
all graphs through order ten (and additional cubic tests), but the proof
above does not establish it: different pairwise Two Paths completions may
place different terminal pairs behind different filled triangles.  A proof
must synchronize those three webs, not assert that any one completion is
the unique plane embedding.  The three-gate descent above is the safe
theorem available without that synchronization.

The remaining Moser route is now sharply geometric: a surviving exterior
component is 3-connected but has a literal three-gate with support-four
lobes.  The next exchange must either split one such lobe into the missing
duty carrier, synchronize its gate with the other packet, or use the gate
as an exact state-gluing adhesion.
