# Two-block contact adhesions: linkage, webs, and a nonplanar closure

**Supersession notice.** Theorem 2.4 below is stronger than the later web
analysis in the \(\mathrm{HC}_7\) range: one full connected shore repairs
both missing boundary edges directly and gives a clique minor of order
\(|S|\). Consequently the palette-tight \(\mathrm{HC}_7\) web discussed
later cannot actually occur. The web sections remain relevant only to the
uniform subcritical range \(|S|\le t-1\), and as audited diagnostics of the
state-transfer mechanism.

## 1. Standing counterexample

Let \(t\) be the least failing parameter, let \(G\) be a
proper-minor-minimal counterexample, and put \(r=t-1\). Thus every proper
minor of \(G\) is \(r\)-colourable and \(G\) has no \(K_t\)-minor.

The one-block theorem in
hadwiger_uniform_contact_oneblock_adhesion.md treats an adhesion whose
complement has one nontrivial clique component. This note treats the next
exact boundary shape: two nontrivial independent blocks.

## 2. The weakest direct two-block linkage hypothesis

### Definition 2.1

Let \((A,B)\) be a separation with adhesion \(S=A\cap B\), and let

\[
S=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}R.
\]

An **\((P,Q)\)-realization on the \(A\)-side** is a pair of disjoint
connected sets

\[
X_P^A\subseteq (A-S)\cup P,\qquad
X_Q^A\subseteq (A-S)\cup Q
\]

such that

\[
X_P^A\cap S=P,\qquad X_Q^A\cap S=Q.
\]

Define a \(B\)-side realization symmetrically. No adjacency between the
two sets is included in the definition.

### Theorem 2.2 (two-block adhesion gluing)

Suppose:

1. \(P,Q\) are nonempty independent sets;
2. \(R\) is a clique;
3. every two vertices in different members of \(\{P,Q,R\}\) are adjacent;
4. both sides of \((A,B)\) have an \((P,Q)\)-realization; and
5. \(A-S\) and \(B-S\) are nonempty.

Then \(G\) is \(r\)-colourable, a contradiction.

#### Proof

On the \(A\)-side, contract \(X_P^A\) and \(X_Q^A\) separately and delete
every remaining vertex of \(A-S\). The two contraction sets are disjoint
and connected. Their images are adjacent because every \(P\)-\(Q\) edge
is present. Each image is adjacent to every singleton vertex of \(R\),
and \(R\) is a clique. Hence the two images and the \(|R|\) singletons
form a \(K_q\), where

\[
q=|R|+2.                                             \tag{2.1}
\]

This is a proper minor of \(G\). Colour it with \(r\) colours, retain the
colouring on \(B-S\), and expand each of \(P,Q\) monochromatically with
the colour of its image. Expansion is proper because \(P,Q\) are
independent, and every boundary-to-\(B-S\) edge was retained at the
corresponding contracted image. The exact equality partition on \(S\) is

\[
\Pi=\{P,Q\}\mathbin{\dot\cup}
       \bigl\{\{x\}:x\in R\bigr\}.                   \tag{2.2}
\]

The state is exact because its \(q\) images form a clique.

Repeat the construction from the \(B\)-side to obtain a colouring of
\(G[A]\) with the same exact state. Align the \(q\) used colours by a
palette permutation and glue across the separation.

It remains only to justify \(q\le r\). Choose \(p\in P\) and \(q_0\in Q\).
The set

\[
\{p,q_0\}\cup R
\]

is a clique of order \(|R|+2=q\). Since \(G\) has no \(K_t\)-minor,
\(q\le t-1=r\). Thus both proper-minor colourings exist with a large
enough palette, and their union is an \(r\)-colouring of \(G\), the
required contradiction. \(\square\)

### Remark 2.3 (why this is the weakest direct condition)

Pairwise adjacency of the two connected witnesses is automatic from the
complete \(P\)-\(Q\) boundary edges. Thus the only geometric demand is
that the two independent blocks can be connected by disjoint subgraphs on
each side. Connectedness of the whole shore alone cannot be substituted
for this demand, as the alternating-cycle example in the one-block note
shows.

### Theorem 2.4 (one full shore repairs two missing edges)

Let

\[
S=\{p_1,p_2,q_1,q_2\}\mathbin{\dot\cup}R
\]

and suppose

\[
\overline{G[S]}=
p_1p_2\mathbin{\dot\cup}q_1q_2
\mathbin{\dot\cup}|R|K_1.                            \tag{2.3}
\]

If \(D\subseteq V(G)-S\) is connected and adjacent to every vertex of
\(S\), then \(G\) has a \(K_{|S|}\)-minor.

#### Proof

Use the following \(|R|+4=|S|\) branch sets:

\[
\{p_1\},\quad \{q_1\},\quad
\{r\}\ (r\in R),\quad
\{p_2,q_2\},\quad D.                                \tag{2.4}
\]

They are disjoint and connected. In particular \(p_2q_2\) is an edge,
because the only missing boundary edges are \(p_1p_2,q_1q_2\).

The singleton bags on \(\{p_1,q_1\}\cup R\) form a clique. The bag
\(\{p_2,q_2\}\) sees \(p_1\) through the edge \(q_2p_1\), sees \(q_1\)
through \(p_2q_1\), and sees every vertex of \(R\). Finally \(D\) is
adjacent to every boundary bag by hypothesis. Thus all bags in (2.4) are
pairwise adjacent. \(\square\)

### Corollary 2.5 (complete \(\mathrm{HC}_7\) contact-cell closure)

In the contact-maximal setup, let \(S\) be an inclusion-minimal
\(v\)-\(C\) separator contained in the contact region. If (2.3) holds,
then

\[
|S|\le t-1.                                         \tag{2.5}
\]

In particular, for \(t=7\) no such separator exists.

#### Proof

The component \(D_C\) containing the connected noncontact region \(C\)
is adjacent to every vertex of \(S\), by inclusion-minimality of the
separator. Theorem 2.4 gives a \(K_{|S|}\)-minor. Since \(G\) has no
\(K_t\)-minor, \(|S|\le t-1\).

For \(t=7\), Mader's contraction-critical connectivity theorem gives
\(|S|\ge\kappa(G)\ge7\), contradicting (2.5). \(\square\)

## 3. Pair-pair blocks and the two-paths theorem

Assume now

\[
P=\{p_1,p_2\},\qquad Q=\{q_1,q_2\}.                  \tag{3.1}
\]

For a component \(D\) of \(G-S\), put

\[
J_D=G[D\cup P\cup Q].
\]

An \((P,Q)\)-realization in \(D\) exists if and only if \(J_D\) contains
vertex-disjoint paths

\[
p_1\mathbin{-}p_2,\qquad q_1\mathbin{-}q_2.          \tag{3.2}
\]

Indeed, two paths are themselves a realization. Conversely, a connected
witness spanning two prescribed terminals contains a path between them,
and paths selected inside disjoint witnesses remain disjoint.

### Theorem 3.1 (one linked side already suffices)

Let \((A,B)\) satisfy the boundary hypotheses of Theorem 2.2 with
\(P,Q\) as in (3.1). Suppose the \(A\)-side has the disjoint linkage
(3.2), while the \(B\)-side merely contains a connected set
\(D_B\subseteq B-S\) adjacent to every vertex of \(P\cup Q\).
Then \(G\) is \(r\)-colourable, a contradiction.

#### Proof

Let \(L_P,L_Q\) be the two disjoint paths on the \(A\)-side. That side
realizes each of the following three exact boundary partitions:

\[
\begin{aligned}
\Pi_{PQ}&=P\mid Q\mid\{x\}\quad(x\in R),\\
\Pi_P&=P\mid\{q_1\}\mid\{q_2\}\mid\{x\}\quad(x\in R),\\
\Pi_Q&=\{p_1\}\mid\{p_2\}\mid Q\mid\{x\}\quad(x\in R).
\end{aligned}                                        \tag{3.3}
\]

For \(\Pi_{PQ}\), use the two whole paths as the \(P\)- and \(Q\)-blocks.
For \(\Pi_P\), use \(L_P\) as one block and split \(L_Q\) at any edge
into two disjoint adjacent connected sets containing \(q_1,q_2\),
respectively. For \(\Pi_Q\), split \(L_P\) and retain \(L_Q\). In every
case, the boundary cross-edges and the clique \(R\) make all displayed
blocks pairwise adjacent. Hence contracting the displayed sets transfers
all three exact states to the \(B\)-side. If one of these partitions had
more than \(r\) blocks, its displayed clique minor would itself contain a
\(K_t\)-minor; therefore every needed state has at most \(r\) blocks.

Now contract the connected set \(D_B\cup P\), delete the rest of \(B-S\),
and colour the resulting proper minor. Expand on the \(A\)-side. The image
of \(P\), the vertices of \(R\), and \(q_1,q_2\) are pairwise adjacent
except possibly for \(q_1q_2\). Consequently the exact state induced on
\(S\) is either \(\Pi_P\) or \(\Pi_{PQ}\).

The \(B\)-side has a colouring with whichever of these two exact states
occurred, by the first paragraph. Align the corresponding boundary blocks
and glue. This gives an \(r\)-colouring of \(G\), a contradiction.
\(\square\)

### Corollary 3.2

In a counterexample, if both open sides contain connected subgraphs
touching all four terminals, then **neither** side has the linkage (3.2).

### Definition 3.3 (the four pair states)

For a closed side \(G[A]\), let \(\mathcal E_A\) be the exact equality
states on \(S\) induced by its \(r\)-colourings, and define
\(\mathcal E_B\) symmetrically. Among the two pair coordinates write

\[
\begin{array}{c|c}
00&\text{neither }P\text{ nor }Q\text{ is monochromatic},\\
10&P\text{ alone is monochromatic},\\
01&Q\text{ alone is monochromatic},\\
11&P,Q\text{ are both monochromatic}.
\end{array}                                          \tag{3.4}
\]

All vertices of \(R\) are singleton classes in every state, because they
are pairwise adjacent and complete to \(P\cup Q\).

### Theorem 3.4 (state polarity)

Suppose each open side contains a connected set adjacent to every vertex
of \(P\cup Q\). Then, after interchanging the sides, exactly the following
holds:

\[
\begin{aligned}
11&\in\mathcal E_A,&
10,01&\notin\mathcal E_A,\\
11&\notin\mathcal E_B,&
10,01&\in\mathcal E_B.
\end{aligned}                                        \tag{3.5}
\]

The state \(00\) may occur on at most one side.

#### Proof

No exact state belongs to both extension families: matching two side
colourings with the same equality partition by a palette permutation
would colour \(G\).

Contract a connected full shore on the \(B\)-side together with \(P\).
After expanding on the \(A\)-side, the only possible additional boundary
equality is \(q_1=q_2\). Thus

\[
\mathcal E_A\cap\{10,11\}\ne\varnothing.
\]

Contracting the same shore with \(Q\) gives

\[
\mathcal E_A\cap\{01,11\}\ne\varnothing.
\]

The symmetric two assertions hold for \(\mathcal E_B\). Therefore, if a
side lacks \(11\), it contains both \(10\) and \(01\).

The state \(11\) cannot occur on both sides. If it occurred on neither,
both sides would contain \(10\) and \(01\), again contradicting
disjointness. Hence it occurs on exactly one side, say \(A\). The other
side then contains \(10,01\), so disjointness excludes those two states
from \(A\). Finally \(00\) cannot occur on both sides for the same
reason. \(\square\)

### Corollary 3.5 (palette-tight boundary-minor criticality)

Assume additionally

\[
|S|=r+1.                                             \tag{3.6}
\]

Orient the sides as in (3.5). Then

\[
\mathcal E_A=\{11\},\qquad
\mathcal E_B=\{10,01\}.                              \tag{3.7}
\]

Moreover:

1. after every vertex deletion, edge deletion, or edge contraction wholly
   inside \(B-S\), the modified \(B\)-side admits the exact state \(11\);
2. after every such one-step minor operation wholly inside \(A-S\), the
   modified \(A\)-side admits one of \(10,01\).

#### Proof

The state \(00\) uses \(|S|=r+1\) boundary colours and hence cannot occur
in an \(r\)-colouring. Equation (3.7) follows from Theorem 3.4.

Perform an indicated operation inside \(B-S\). The resulting whole graph
is a proper minor of \(G\), so it has an \(r\)-colouring. Its restriction
to the unchanged \(A\)-side has a state in \(\mathcal E_A=\{11\}\);
therefore the same boundary state extends to the modified \(B\)-side.
The argument with \(A,B\) interchanged gives assertion 2. \(\square\)

Thus, in the palette-tight case, the side lacking the joint state is a
minor-minimal boundaried obstruction to \(11\): every one-step internal
minor creates that state. This is substantially stronger than static
colour saturation.

We use the installed Robertson--Seymour--Thomas two-disjoint-paths theorem
in its web form:

> If (3.2) does not exist, one may repeatedly cut off terminal-free sides
> along separations of order at most three. After replacing their
> adhesions by the corresponding triangles, the terminal-bearing core has
> a drawing in a disk with
> \(p_1,q_1,p_2,q_2\) in this cyclic order.

Equivalently, a failure is a two-paths web: a cyclic disk core together
with pieces attached behind terminal-free adhesions of order at most three.
This is the same theorem and convention used in
hadwiger_one_edge_web_round.md.

## 4. Contact-separator specialization

Fix a contact-maximal \(K_{t-1}\)-model at \(v\). Let \(A\) be its contact
region and \(C\) the connected union of its noncontact bags. As proved in
the one-block note, \(A\) separates \(v\) from \(C\). Choose an
inclusion-minimal \(v\)-\(C\) separator \(S\subseteq A\). Let \(D_v,D_C\)
be the components of \(G-S\) containing \(v,C\), respectively. Every
vertex of \(S\) has a neighbour in both \(D_v,D_C\).

Assume the next exact adhesion shape

\[
\overline{G[S]}=
K_2\mathbin{\dot\cup}K_2\mathbin{\dot\cup}(|S|-4)K_1, \tag{4.1}
\]

and let \(P,Q\) be the two independent pairs and \(R=S-(P\cup Q)\).
Put

\[
J_v=G[D_v\cup P\cup Q],\qquad
J_C=G[D_C\cup P\cup Q].                              \tag{4.2}
\]

### Lemma 4.1 (a terminal-free web piece gives a global cut)

Let \(D\in\{D_v,D_C\}\). Suppose \(J_D\) has a separation \((X,Y)\)
such that

\[
P\cup Q\subseteq X,\qquad
T=X\cap Y,\quad |T|\le3,\qquad
W=Y-X\ne\varnothing.
\]

Then

\[
N_G(W)\subseteq T\cup R.                             \tag{4.3}
\]

#### Proof

The set \(W\) is terminal-free, hence \(W\subseteq D\). Within \(J_D\),
the separation forbids every edge from \(W\) to \(X-Y\). Outside \(J_D\),
a vertex of \(D\) can have neighbours only in the deleted adhesion
vertices \(R\): distinct components of \(G-S\) are anticomplete. Therefore
every neighbour of \(W\) outside \(W\) lies in \(T\cup R\). \(\square\)

### Corollary 4.2 (all small terminal-free attachments disappear)

If

\[
|R|\le\kappa(G)-4,                                   \tag{4.4}
\]

then neither \(J_v\) nor \(J_C\) has a terminal-free side behind a
separation of order at most three.

#### Proof

By Lemma 4.1, such a side would be separated from the rest of \(G\) by
\(T\cup R\), whose order is at most

\[
3+|R|\le\kappa(G)-1.
\]

This contradicts the definition of vertex-connectivity. \(\square\)

Since \(S\) itself is a separator and \(|S|=|R|+4\), one always has
\(|R|+4\ge\kappa(G)\). Thus (4.4) is the sharp equality cell

\[
|S|=\kappa(G),\qquad |R|=\kappa(G)-4.                \tag{4.5}
\]

For \(\mathrm{HC}_7\), this includes the natural order-seven adhesion
with three singleton blocks.

### Lemma 4.3 (the two terminal-side graphs are 3-connected)

Under (4.1) and (4.4), both \(J_v\) and \(J_C\) are 3-connected.

#### Proof

Fix \(J=J_D\), where \(D\in\{D_v,D_C\}\). The graph has at least five
vertices: it contains the four terminals and the nonempty component \(D\).
Suppose \(T\), with \(|T|\le2\), disconnects \(J\).

The terminal graph \(G[P\cup Q]\) is \(K_{2,2}\). Unless
\(T=P\) or \(T=Q\), all terminals outside \(T\) lie in one component of
\(J-T\): deleting at most two vertices other than an entire part leaves
the surviving \(K_{2,2}\) connected. Any other component is terminal-free,
and Lemma 4.1 gives a cut \(T\cup R\) of \(G\) of order at most

\[
2+|R|\le\kappa(G)-2,
\]

a contradiction.

It remains to consider \(T=P\) or \(T=Q\). By symmetry let \(T=P\).
If \(q_1,q_2\) lie in one component, every other component is
terminal-free and the preceding argument applies. Otherwise let \(W\)
be the component of \(J-P\) containing \(q_1\). The terminal \(q_1\)
has a neighbour in \(D\), by Lemma 3.2 of the one-block note, so
\(W-\{q_1\}\ne\varnothing\). No vertex of \(W-\{q_1\}\) has a neighbour
outside

\[
W\cup P\cup R\cup\{q_1\}.
\]

Consequently \(P\cup R\cup\{q_1\}\), of order

\[
2+|R|+1\le\kappa(G)-1,
\]

separates \(W-\{q_1\}\) from the component containing \(q_2\), again a
contradiction. The case \(T=Q\) is identical. Thus no set of at most two
vertices disconnects \(J\). \(\square\)

### Theorem 4.4 (only bilateral disk webs survive)

Assume (4.1) and (4.4). Then both \(J_v\) and \(J_C\) have drawings in a
disk with \(p_1,q_1,p_2,q_2\) in this cyclic order.

#### Proof

Each of \(D_v,D_C\) is connected and adjacent to all four terminals.
By Corollary 3.2, neither \(J_v\) nor \(J_C\) has the linkage (3.2).

Apply the two-disjoint-paths theorem to \(J_v\). Lemma 4.3 permits its
3-connected form: either there is a separation of order three with all
four terminals on one side and a nonempty terminal-free open side, or
\(J_v\) has the claimed disk drawing. The first outcome is excluded by
Corollary 4.2. Thus \(J_v\) is a disk web. The same argument applies to
\(J_C\). \(\square\)

### Corollary 4.5 (sharp residual)

In the sharp pair-pair contact cell (4.1), (4.5), **both**
\(J_v,J_C\) are genuine disk webs. Every configuration with even one
linked or nonplanar side, and every failure caused by a terminal-free
piece behind a cut of order at most three, is eliminated.

This is an infinite family closure, not merely a finite boundary
enumeration.

### Corollary 4.6 (the sharp \(\mathrm{HC}_7\) web is boundary-critical)

Suppose \(t=7\), \(\kappa(G)=|S|=7\), and hence \(|R|=3\) and \(r=6\).
Then, after interchanging \(D_v,D_C\), the two disk-web sides satisfy

\[
\mathcal E_v=\{11\},\qquad
\mathcal E_C=\{10,01\}.                              \tag{4.6}
\]

Every one-step minor operation internal to the \(C\)-web creates an exact
\(11\) extension on that side. More explicitly:

1. for every \(x\in D_C\), every six-colouring of \(G-x\) induces state
   \(11\) on \(S\), and all six colours occur on \(N_G(x)\);
2. for every edge \(xy\) with both ends in \(D_C\), every six-colouring
   of \(G-xy\) induces state \(11\), gives \(x,y\) the same colour, and
   each of \(x,y\) sees every other colour.

#### Proof

Here \(|S|=r+1\), so Corollary 3.5 gives (4.6) and the exact state after
every internal minor operation.

If a six-colouring of \(G-x\) omitted a colour from \(N_G(x)\), assigning
that colour to \(x\) would colour \(G\). Thus every colour occurs on the
neighbourhood.

For an internal edge \(xy\), if a six-colouring of \(G-xy\) gave its ends
different colours, restoring the edge would colour \(G\). Hence the ends
have one common colour. If another colour were absent from the neighbours
of one endpoint in \(G-xy\), recolour that endpoint with the missing
colour and restore \(xy\), again colouring \(G\). \(\square\)

Consequently the remaining split-side disk web is not an arbitrary planar
two-paths obstruction. It is a boundaried minor-critical web in which
every internal edge deletion produces a joint-pair boundary colouring
with a saturated pair of equal-coloured endpoints.

### Theorem 4.7 (no split web with at most six interior vertices)

Orient the sides as in Corollary 4.6, so that
\(\mathcal E_C=\{10,01\}\). Then the split-side component \(D_C\) has
order at least seven.

The order-two case has the following short hand proof. Let the component
be the edge \(ab\). Since \(a,b\) have no neighbours outside
\(S\cup\{a,b\}\) and \(\delta(G)\ge7\), each is adjacent to at least six
of the seven boundary vertices.

In state \(10\), all six colours occur on \(S\). A vertex adjacent to at
least six boundary vertices is colourable only if it misses exactly one
boundary singleton from

\[
\{q_1,q_2\}\cup R;
\]

its colour is then forced to be the colour of that missed singleton.
Because \(ab\) is an edge, the two missed singletons are distinct. Applying
the same argument to state \(01\) says that each missed boundary vertex
belongs to

\[
\{p_1,p_2\}\cup R.
\]

The fixed missed vertex for each of \(a,b\) therefore lies in \(R\), and
the two missed \(R\)-vertices are distinct. In state \(11\), colour
\(a,b\) with the colours of their respective missed \(R\)-vertices.
Those colours are distinct, and each is absent from the corresponding
boundary neighbourhood. This extends state \(11\), contradicting
\(\mathcal E_C=\{10,01\}\).

Orders one and three are covered, together with an independent replay of
the order-two argument, by the dependency-free verifier
twoblock_small_web_verify.py. It enumerates:

1. every connected labelled graph on one, two, or three interior vertices;
2. every one of the \(2^7\) possible boundary neighbourhoods of each
   interior vertex;
3. the exact degree inequalities
   \(d_D(x)+|N_S(x)|\ge7\);
4. full boundary attachment \(\bigcup_{x\in D}N_S(x)=S\);
5. extension of states \(10,01\) and failure of \(11\); and
6. absence of the two disjoint paths.

The replay gives

    order 1: split/no-joint/unlinked=0
    order 2: split/no-joint/unlinked=0
    order 3: split/no-joint=288, split/no-joint/unlinked=0

Thus every order-three split/no-joint configuration already has the
linkage and is eliminated by Theorem 3.1. This proves the theorem within
the stated finite-certificate trust boundary through order three.

Orders four, five, and six are eliminated by the Z3-backed verifier
twoblock_web_sat_probe.py. Its formula retains all of the following:

1. the degree and full-attachment conditions above;
2. exact states \(10,01\), failure of \(11\), and absence of the linkage;
3. the inequalities
   \(|N_{J_C}(X)|\ge4\) for every nonempty \(X\subseteq D_C\), which are
   exactly the consequences of seven-connectivity after the three
   singleton vertices \(R\) are restored;
4. every internal vertex/edge deletion and every internal edge contraction
   creates state \(11\), with equal endpoints after edge deletion; and
5. absence of a \(K_7\)-minor.

The minor exclusion is checked by a CEGIS loop. For each provisional
boundary assignment, an exact connected-branch-set search either certifies
that no \(K_7\)-model exists or returns one explicit model. The Boolean
contact edges used by a spanning tree in every bag and by one edge between
every bag pair are then blocked. Thus every blocking clause is itself a
replayable branch-set certificate.

The order-five run first verifies, without an external graph atlas, that
the archived list contains exactly the 21 connected five-vertex graphs up
to isomorphism. The order-six certificate archives the 112 canonical
codes of the connected six-vertex types; all 112 were rerun in four
complete shards. The outputs are

    UNSAT order=4 labelled_connected_types=38
    UNSAT order=5 labelled_connected_types=21
    order=6: 112/112 canonical connected types UNSAT

This proves the theorem through order six within the Z3 and exact
branch-set-search trust boundary. \(\square\)

### Remark 4.8 (the smallest XOR gadget)

The alternating gadget consisting of the boundary \(K_{2,2}\), an
internal edge \(ab\), with

\[
N_S(a)=\{p_2,q_2\}\cup R,\qquad
N_S(b)=\{p_1,q_1\}\cup R
\]

does realize \(10,01\), forbids \(11\), and has no linkage. But
\(d(a)=d(b)=6\). The verifier replays this gadget before imposing the
counterexample constraints. Thus the exact hypothesis excluding it is
the counterexample minimum-degree bound \(\delta(G)\ge7\), not planarity
or six-colour saturation alone.

### Remark 4.9 (why minor exclusion is essential at order five)

There is an order-five planar, 3-connected alternating web satisfying
minimum degree seven, full attachment, the polarity
\(\{10,01\}\) versus \(11\), all local four-neighbour shore inequalities,
and every one-step internal minor transition from Corollary 4.6. One
labelled form has

\[
\begin{aligned}
E(D)=\{&01,02,03,04,12,14,23\},\\
(N_S(0),\ldots,N_S(4))={}&
(\{p_2,r_1,r_3\},\{p_1,r_1,r_2,r_3\},
 \{p_1,r_1,r_2,r_3\},\\
&\{p_1,p_2,q_2,r_1,r_3\},
 \{p_1,p_2,q_1,r_1,r_3\}).
\end{aligned}
\]

It is not a counterexample-derived side because it already has the
following \(K_7\)-model:

\[
\{p_1\},\ \{q_1\},\ \{r_1\},\ \{r_2\},\ \{r_3\},\
\{p_2,q_2\},\ \{1_D,4_D\}.                          \tag{4.7}
\]

The dependency-free script
twoblock_order5_counterarchitecture_verify.py checks all the asserted
local transition properties and the seven displayed branch sets. This
example shows that degree, connectivity-derived shore cuts, disk-web
topology, and one-step boundary criticality still do not suffice without
using \(K_7\)-minor exclusion itself.

## 5. Limits and the next mechanism

The remaining pair-pair obstruction is a pair of cyclic disk webs with
the four terminals alternating and the polarity (4.6). Static boundary
extension data do not eliminate such webs. In the sharp \(\mathrm{HC}_7\)
case the next exact target is:

> No alternating disk web can forbid state \(11\) while every internal
> edge deletion or contraction creates \(11\) with the saturation
> properties in Corollary 4.6.

A proof should find a reducible internal edge or facial configuration,
or use the remaining singleton adhesion vertices \(R\) as a source of
disjoint bridge reroutings while keeping their boundary colour classes
separate. Theorem 4.7 shows that any remaining split-side web has at least
seven interior vertices.

Coarse shore edge-cut inequalities are insufficient: a six-helper
assignment can satisfy all such inequalities and full boundary coverage
while still having no boundary-meeting \(K_6\)-model. Consequently the
next step must retain actual vertex-boundary attachments, web bridges, or
proper-minor colour states.
