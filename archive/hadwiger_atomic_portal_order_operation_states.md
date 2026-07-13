# Atomic support webs: portal order and two-operation states

## 1. The local split problem

Let \(D\) be a connected support piece, and let
\(T_1,\ldots,T_m\) be disjoint connected retained carriers outside
\(D\).  Put

\[
                         P_i=N_D(T_i).                    \tag{1.1}
\]

A connected bipartition of \(D\) means
\(D=X\mathbin{\dot\cup}Y\), with \(X,Y\) nonempty, connected, and
adjacent.  The following elementary extension fact will be used
repeatedly.

### Lemma 1.1 (two cores extend to a split)

If \(L_X,L_Y\) are disjoint nonempty connected subgraphs of \(D\), then
there is a connected bipartition \(D=X\dot\cup Y\) with
\(L_X\subseteq X\) and \(L_Y\subseteq Y\).

#### Proof

Contract the two cores, take a spanning tree of the resulting connected
graph, and delete one edge on the tree path between the two contracted
vertices.  The two tree components lift to the required connected,
adjacent partition. \(\square\)

This lemma does not require either half to retain the old root.  In the
packing applications below each half is paired with a retained rooted
carrier, so both resulting branch groups are contacted.

## 2. The missing-triangle motif is an \(\mathcal S\)-path packing

Assume \(m=3\).  Form \(\widehat D\) by adjoining, for every incidence
\(p\in P_i\), a new leaf \(p_i\) adjacent only to \(p\).  Partition the
new leaves into the three classes \(\widehat P_1,\widehat P_2,
\widehat P_3\).  An \(\mathcal S\)-path has its two ends in distinct
classes and no new leaf internally.

### Theorem 2.1 (triangle split or exact Mader capacity web)

Exactly one of the following structural outcomes holds.

1. The graph \(\widehat D\) contains two vertex-disjoint
   \(\mathcal S\)-paths.  Then \(D\) has a connected bipartition in
   which each half meets at least two of the three portal classes.
2. The maximum number of disjoint \(\mathcal S\)-paths is one.  In the
   Mader min--max certificate there is a partition

   \[
               U_0,U_1,\ldots,U_n=V(\widehat D)          \tag{2.1}
   \]

   such that every \(\mathcal S\)-path disjoint from \(U_0\) traverses
   an edge with both ends in some \(U_i\), and, writing \(B_i\) for the
   vertices of \(U_i\) which are terminals or have a neighbour outside
   \(U_0\cup U_i\), one of the following exact capacity patterns holds:

   * \(|U_0|=1\) and \(|B_i|\le1\) for every \(i\); or
   * \(U_0=\varnothing\), exactly one cell has
     \(2\le|B_i|\le3\), and every other cell has \(|B_j|\le1\).

#### Proof

Remove the artificial leaf ends from two disjoint \(\mathcal S\)-paths.
The remaining cores are disjoint connected subgraphs of \(D\), each
meeting two different portal classes.  Lemma 1.1 extends them to a
connected bipartition.  Since the two halves cover \(D\), their portal
supports together contain all three classes, while each already contains
two.

If there is no such packing, connectedness of \(D\) and nonemptiness of
the three portal classes give packing number exactly one.  Mader's
\(\mathcal S\)-paths theorem says that this number equals

\[
                 |U_0|+\sum_i\left\lfloor |B_i|/2\right\rfloor.
                                                               \tag{2.2}
\]

The nonnegative integer in (2.2) equals one.  If \(|U_0|=1\), every
summand is zero.  If \(U_0\) is empty, exactly one summand equals one
and the others vanish.  These are precisely the two displayed patterns.
\(\square\)

When the old support graph is exactly \(K_{r+1}-K_3\) and \(D\) is an
old universal support piece, outcome 1 gives the rooted \(K_r\)-model of
Corollary 5.2 in `hadwiger_one_surplus_rooted_model_principle.md`.
Outcome 2 is therefore a label-free **capacity-state web**, not a new
list of Moser cases.

### Lemma 2.2 (the Mader cells have gates of order at most three)

For a certificate in Theorem 2.1, put

\[
 C_i=(U_i\cap V(D))-(U_0\cup B_i).
\]

Then

\[
            N_D(C_i)\subseteq (U_0\cup B_i)\cap V(D).    \tag{2.3}
\]

Consequently, in the first capacity pattern every nonempty cell interior
lies behind a gate of order at most two.  In the second pattern every
ordinary cell lies behind a gate of order at most one, and the unique
exceptional cell lies behind a gate of order at most three.

#### Proof

A vertex of \(U_i-B_i\) is not a terminal and, by the definition of
\(B_i\), has no neighbour outside \(U_0\cup U_i\).  Its neighbours in
\(U_i\) which are omitted from \(C_i\) lie in \(B_i\).  This proves
(2.3).  The numerical bounds are the two alternatives in Theorem 2.1.
Artificial terminal leaves can only reduce the size of the displayed
gate when intersecting with \(V(D)\). \(\square\)

Call a cell **proper** when \(C_i\ne\varnothing\) and
\(D-(C_i\cup((U_0\cup B_i)\cap V(D)))\ne\varnothing\).  Thus in a
six-connected ambient \(H\), every proper Mader cell has an external
bypass across its order-at-most-three gate, by Lemma 4.1 below.  A
surviving capacity web must route all of those bypasses through named
outside carriers; it cannot remain an isolated internal
cutvertex/three-cut decomposition.

### Lemma 2.3 (block-level portal order)

Let \(W\) be a maximal 2-connected block of \(D\).  Suppose that for
some permutation \((i,j,k)\) of the three portal classes, \(W\) contains
distinct vertices \(s,t\in P_i\), a vertex \(b\in P_j\), and a vertex
\(c\in P_k\), with \(b\ne c\).  Then the good bisection in
Theorem 2.1 exists.

#### Proof

Take an \(s\)-\(t\) bipolar ordering of \(W\).  Cut between \(b\) and
\(c\), orienting the ordering so that \(b\) is on the prefix side and
\(c\) on the suffix side.  Every prefix and suffix of a bipolar ordering
is connected.  The prefix meets \(P_i,P_j\), and the suffix meets
\(P_i,P_k\).

Every component of \(D-V(W)\) attaches to the maximal block \(W\) in at
most one vertex; two attachments would give an ear enlarging the
2-connected block.  Assign each component to the side containing its
attachment.  This extends the cut of \(W\) to a connected bisection of
\(D\). \(\square\)

Consequently, if every triangle bisection fails, duplicated portals in
any one block obey a strict order: once one class has two distinct
representatives, the other two classes cannot have distinct
representatives in that block.  They are absent or concentrated at one
common vertex.  Remaining duplication must be distributed along the
block-cut tree.

## 3. The missing-path motif is exactly the Two Paths problem

Assume four portal classes \(P_1,P_2,P_3,P_4\).  Form \(D^\Box\) by
adding distinct terminals \(s_i\), with \(s_i\) adjacent to every vertex
of \(P_i\).

### Theorem 3.1 (path split or web completion)

The following are equivalent.

1. The graph \(D\) has a connected bipartition \(X\dot\cup Y\) with
   \(X\) meeting \(P_1,P_2\) and \(Y\) meeting \(P_3,P_4\).
2. The graph \(D^\Box\) has disjoint paths joining \(s_1\) to \(s_2\)
   and \(s_3\) to \(s_4\).

If these conditions fail, the Two Paths Theorem embeds
\(D^\Box\) in an edge-maximal nonlinkable web, with the four terminals
in alternating outer order and the usual clique insertions in facial
triangles.

#### Proof

A bipartition supplies the two paths inside its disjoint halves.  In the
other direction, delete the artificial terminal ends from the two paths
and apply Lemma 1.1 to the two remaining connected cores.  The final
assertion is the standard Two Paths Theorem, applied to an edge-maximal
nonlinkable completion of \(D^\Box\). \(\square\)

For the exact support graph \(K_{r+1}-P_4\), outcome 1 is precisely the
path-end bisection in Corollary 5.3 of the one-surplus principle.  Thus a
persistent missing-path motif has a genuine web order; arbitrary raw
portal enumeration is unnecessary.

### Lemma 3.2 (external bridges in the saturated case)

Assume here that \(D^\Box\) itself is edge-maximal subject to having no
prescribed linkage; equivalently, it is already the saturated web rather
than merely a subgraph of a web completion.  Let \(C\) be a connected
subgraph outside \(D^\Box\), with interior disjoint from the web.  If two
attachments \(x,y\in N_{D^\Box}(C)\) are nonadjacent in \(D^\Box\), then
\(D^\Box\cup C\) contains the prescribed two disjoint paths.
Consequently every two attachments of every external bridge in a
surviving saturated obstruction are adjacent in the web; its attachment
set is a clique.

#### Proof

Take an \(x\)-to-\(y\) path through \(C\) with interior outside
\(D^\Box\).  By edge maximality, adding the missing edge \(xy\) to
\(D^\Box\) creates the
prescribed linkage.  Replace the use of \(xy\) by the external path.
The replacement has new, disjoint interior, so the linkage remains
vertex-disjoint.  The contrapositive proves the confinement statement.
\(\square\)

In a web, such a clique is either part of the planar triangulated core or
lies in one of the clique insertions supported on a facial triangle.
Thus failure converts every outside bridge into a facial/three-gate
object.  A bridge belonging to the uncontacted helper may be absorbed in
the linkage.  A bridge belonging to a retained rooted carrier is the
precise dirty-helper obstruction which must be handled by operation
states.

The saturation hypothesis is essential.  For a general nonlinkable
subgraph, a linkage in an edge-maximal *supergraph* may use several added
edges which have no realization in the host.  The Two Paths Theorem alone
therefore gives a web completion, not bridge confinement.  A complete
application must either realize the relevant missing web edges by
compatible clean paths or run this lemma only in an already saturated
portal core.

### Example 3.3 (a completion cannot certify an actual bridge)

Let \(W\) be the wheel with rim in cyclic order
\(s_1,s_3,s_2,s_4\) and hub \(h\).  It is edge-maximal with no disjoint
\(s_1s_2\)- and \(s_3s_4\)-paths.  Let \(D\) consist of the rim and only
the spoke \(hs_1\), and add an external path \(s_1-c-s_2\).  The
attachments \(s_1,s_2\) are nonadjacent in \(W\), and \(W\) plus the
external path is linkable.  But \(D+s_1cs_2\) is not: after using an
\(s_1s_2\)-path, every \(s_3s_4\)-route in \(D\) meets \(s_1\) or
\(s_2\).  The missing spokes of the completion were essential.  This is
the smallest reason a stable/minimal bridge or simultaneous realization
hypothesis cannot be omitted.

## 4. Connectivity forces a bypass across every small portal gate

### Lemma 4.1 (gate or external bypass)

Let \(H\) be \(k\)-connected, let \(D\subseteq V(H)\), and let
\((L,R)\) be a separation of the induced graph \(H[D]\), with gate
\(X=L\cap R\), where both open sides are nonempty and \(|X|<k\).  Then
some component of \(H-D\)
has attachments in both \(L-X\) and \(R-X\).  Equivalently, there is an
\((L-X)\)-to-\((R-X)\) path whose interior is outside \(D\).

#### Proof

If no component has attachments on both sides, assign every component of
\(H-D\) to the side containing all its attachments (components attaching
only to \(X\) may be assigned arbitrarily).  This extends \((L,R)\) to a
separation of \(H\) of order at most \(|X|<k\), a contradiction.
\(\square\)

For the \(HC_7\) application this lemma is used in
\(H=G-v\), so \(k=6\), never seven.  In an already saturated portal
core, combining this with Lemma 3.2 says that every gate of order at most
five has a bypass, but every surviving bypass is confined to a web clique
and is therefore a named helper or owner obstruction.  Without
saturation, the rigorous output is only the bypass; compatibility with
the other virtual web edges remains to be proved.

## 5. Two faithful operations on an actual gate

The portal web becomes operation-sensitive only after its gate is an
actual separation of the ambient graph.  The following records exactly
what minor-criticality then supplies.

### Theorem 5.1 (two-operation gate state)

Let \(G\) be proper-minor-minimal non-six-colourable, put \(H=G-v\),
and let \((A,B)\) be a separation of \(H\) with adhesion \(X\).  Choose
vertex-disjoint edges

\[
 e_A\in E(H[A-X]),\qquad
 e_B\in E(H[B-X]).                                       \tag{5.1}
\]

Then all of the following hold.

1. A colouring of \(G-e_A\) and a colouring of \(G-e_B\) cannot induce
   the same marked equality state on \(X\cup\{v\}\); if they did, the
   two untouched closed shores cross-splice to six-colour \(G\).
2. Contracting both edges and colouring \(G/e_A/e_B\) gives a common
   reference state on \(X\cup\{v\}\).  Both single-edge defects cannot
   be repaired while that state is fixed.
3. On at least one side, for every colour different from the common
   colour of the operated edge ends, either there is a bichromatic
   endpoint detour avoiding the operated edge, or the two endpoint
   components are distinct and both reach \(X\cup\{v\}\).

Every operation in this theorem is strictly open-shore supported.  Hence
all retained carriers and every edge of the opposite closed shore are
preserved literally.

Here, after expanding a colouring \(f\) of the double contraction, an
\(A\)-repair means a proper colouring of the closed shore
\(G[A\cup\{v\}]\) which makes \(e_A\) proper and agrees literally with
\(f\) on \(X\cup\{v\}\); gluing it to \(f\) on \(B-X\) colours
\(G-e_B\).  Define a \(B\)-repair symmetrically.  Item 3 records the
failure of every single-component Kempe repair on one of the two sides.

#### Proof

For item 1, align equal boundary partitions by a palette permutation,
use the \(G-e_B\) colouring on the \(A\)-shore and the \(G-e_A\)
colouring on the \(B\)-shore, and align the apex colour using its marked
block.  Each deleted edge lies on the other coloured shore, giving a
proper colouring of \(G\), a contradiction.

For item 2, expand a six-colouring of the double contraction to a
colouring of \(G-\{e_A,e_B\}\) in which each operated pair is
monochromatic.  Repairs of both defects preserving the boundary state
would give the forbidden pair in item 1.  For a side with no repair, a
Kempe switch on an endpoint component which avoids the adhesion and apex
would repair its edge.  Therefore either the endpoints already have a
bichromatic detour or both endpoint components reach the gate.  This is
item 3. \(\square\)

The theorem deliberately does not assert that the two independently
chosen operation states agree.  Their disagreement is the exact
minor-critical lock.  A complete closure must use the Mader capacity web
or the Two Paths portal order to force a common state, a clean detour, or
a helper absorption.  Merely counting two portals does not do so.

## 6. Uniform dynamic conclusion

For the \(K_3\) and \(P_4\) atomic support motifs, every failed split now
has one of two label-free descriptions:

1. a Mader capacity-one partition or a Two Paths web in the multiply hit
   piece; in a saturated portal core, every external bridge is confined
   to a named gate/clique; or
2. an actual ambient adhesion on which two opposite faithful operations
   have disjoint marked states and a canonical double-operation Kempe
   lock.

This closes the unrestricted quotient enumeration.  It does not yet
eliminate the operation-state lock, and it gives no false claim that
six-connectivity of \(H\) is seven-connectivity.  The remaining theorem
is sharply stated: in a contraction-critical contact-maximal cell, a
capacity-one portal web cannot keep every dirty-helper operation state
disjoint across all of its facial gates.

## 7. The weakest matching-motif exchange

The third atomic certificate, \(3K_2\), has a genuine extra contact
constraint.  In this section assume the old support graph is exactly
\(K_7-3K_2\), not merely that its complement contains a matching
certificate.  Write its six nonuniversal rooted vertices as

\[
              a_1b_1,\quad a_2b_2,\quad a_3b_3          \tag{7.1}
\]

for the three missing pairs.  The seventh support piece \(D\) is
universal and rooted.  Split it into adjacent connected pieces \(X,Y\).
Assume first that \(X\) retains the root and \(Y\) does not.

### Theorem 7.1 (one-root matching-transversal exchange)

For each \(i\), orient the missing pair as \((p_i,q_i)\), so
\(\{p_i,q_i\}=\{a_i,b_i\}\).  If, after permuting the three pairs,

\[
\begin{aligned}
 &X\sim q_1,q_2,q_3,\qquad X\sim p_2\text{ or }p_3,\\
 &Y\sim p_1,q_1,
\end{aligned}                                             \tag{7.2}
\]

then the eight split pieces group to six contacted clique bags.

#### Proof

Use

\[
         Y\cup p_1,quad p_2\cup p_3,quad
         X,quad q_1,quad q_2,quad q_3.                \tag{7.3}
\]

The first two groups are connected.  The three \(q_i\)'s form a clique,
and \(X\) sees all of them.  The first group sees \(q_1\) through \(Y\)
and sees \(q_2,q_3\) through \(p_1\); it sees \(X\) through the split
edge \(XY\).  The second group sees every \(q_i\), because for each
\(i\) at least one of \(p_2,p_3\) belongs to a different missing pair;
it sees \(X\) by (7.2).  The two nonsingleton groups see one another
through an old edge between different missing pairs.

Every group in (7.3) is contacted: \(Y\) borrows the root of \(p_1\),
the second group contains two old rooted pieces, and \(X,q_1,q_2,q_3\)
retain roots. \(\square\)

If both split halves retain roots, there is a simpler triple exchange.

### Theorem 7.2 (two-root transversal exchange)

Choose one endpoint \(p_i\) of every missing pair and put
\(Q=\{q_1,q_2,q_3\}\) for the complementary transversal.  If each of
\(X,Y\) is adjacent to every \(q_i\) and has a neighbour in
\(\{p_1,p_2,p_3\}\), then

\[
              p_1\cup p_2\cup p_3,quad
              X,quad Y,quad q_1,quad q_2,quad q_3    \tag{7.4}
\]

are six contacted clique bags.

#### Proof

Both transversals induce cliques.  The three-piece union in (7.4) is
connected and sees every complementary vertex through one of the other
two pair classes.  The stated masks make it adjacent to \(X,Y\), while
\(X,Y\) see the entire complementary transversal and see one another by
the split edge.  Contact is immediate. \(\square\)

These are not quotient enumerations: they identify the exact reusable
resource in the matching motif, namely a complementary transversal seen
on both sides plus one borrowed-root repair.  Unlike the triangle and
path motifs, a split with only one rooted half cannot be repaired merely
by two generic mixed paths.  It must realize the asymmetric exchange
(7.2), or acquire a second contact through a helper/operation state.
