# Exact traces aligned with an interface-edge witness

## 1. Simultaneous contraction witness across a full shore

Let \(G\) be an \(r\)-minor-critical graph: \(G\) is not
\(r\)-colourable and every proper minor of \(G\) is \(r\)-colourable.
Let \(S\) be a separator, let \(D\) be a component of \(G-S\), and
assume that \(D\) is full to \(S\). Let \(e=xy\) be an edge outside
\(D\cup S\), and let \(I\subseteq S\) be a nonempty independent set
disjoint from \(\{x,y\}\).

### Theorem 1.1 (trace--edge alignment)

There is an \(r\)-colouring \(c\) of

\[
                 G-D-e
\]

and colours \(\sigma,\alpha\) such that

\[
 \{s\in S:c(s)=\sigma\}=I,\qquad c(x)=c(y)=\alpha .
\tag{1.1}
\]

Every component of \(G-S\) other than \(D\) remains present in this
colouring. In particular, the equality at \(e\) and the exact trace on
\(S\) occur in one and the same boundary state.

#### Proof

The set \(D\cup I\) is connected, because \(D\) is connected and every
vertex of \(I\) has a neighbour in \(D\). Contract \(D\cup I\) to a
vertex \(z\), and contract the edge \(xy\) to a vertex \(w\). The two
contracted sets are disjoint. The resulting graph is a proper minor of
\(G\), and hence has an \(r\)-colouring.

Delete the contracted interior \(D\), expand \(z\) only to the boundary
vertices of \(I\), and expand \(w\) to \(x,y\) after deleting the edge
\(xy\). Give all vertices expanded from \(z\) its colour \(\sigma\),
and give \(x,y\) the colour \(\alpha\) of \(w\). This is a proper
colouring of \(G-D-e\). All neighbours outside \(D\cup I\) of a vertex
of \(I\) were adjacent to \(z\), and all neighbours outside
\(\{x,y\}\) of either end of \(e\) were adjacent to \(w\).

Finally, every \(s\in S-I\) has a neighbour in the full shore \(D\).
It was therefore adjacent to \(z\) in the contracted minor, and cannot
receive \(\sigma\). This proves the exact trace in (1.1). \(\square\)

### Remark 1.2

The theorem is stronger than applying the independent-set trace lemma
and the edge-deletion witness separately. Those two applications may
produce unrelated boundary states. Theorem 1.1 forces both constraints
in a single colouring. It does not assert that the whole equality
partition of \(S\) is prescribed, nor that the state extends over the
contracted shore \(D\).

### Theorem 1.3 (multi-anchor trace--edge alignment)

Let \(D_1,\ldots,D_a\) be distinct full components of \(G-S\), and let
\(I_1,\ldots,I_a\) be pairwise disjoint nonempty independent subsets
of \(S\). Assume that for every distinct \(j,k\), some edge of \(G[S]\)
joins \(I_j\) to \(I_k\). Let \(e=xy\) lie outside

\[
                  S\cup D_1\cup\cdots\cup D_a .
\]

Then \(G-(D_1\cup\cdots\cup D_a)-e\) has an \(r\)-colouring \(c\)
and pairwise distinct colours \(\sigma_1,\ldots,\sigma_a\) such that

\[
 \{s\in S:c(s)=\sigma_j\}=I_j\quad(j\in[a]),
 \qquad c(x)=c(y).                                 \tag{1.2}
\]

All components of \(G-S\) not used as anchors remain present.

#### Proof

Contract each connected set \(D_j\cup I_j\) to a vertex \(z_j\), and
contract \(xy\). The contracted sets are disjoint. The vertices
\(z_1,\ldots,z_a\) form a clique, because every pair of boundary
blocks has a cross-edge. Hence they receive pairwise distinct colours
in an \(r\)-colouring of the proper minor.

Delete each anchor interior \(D_j\), expand \(z_j\) only to \(I_j\),
and expand the contracted edge after deleting \(xy\). Every
\(s\in S-I_j\) has a neighbour in the full shore \(D_j\), so it was
adjacent to \(z_j\) and avoids \(\sigma_j\). This proves all exact
traces in (1.2); the edge contraction gives \(c(x)=c(y)\).
\(\square\)

### Corollary 1.4 (packet version)

Let \(\Pi\) be a partition of \(S\) into independent blocks with
complete block-adjacency quotient. Assign every nonsingleton block of
\(\Pi\) to an anchor shore so that, within each shore, the assigned
blocks have pairwise disjoint connected carriers, each carrier meeting
every vertex of its block. Contract each carrier together with its
assigned block, retain every singleton block as its boundary vertex, and
optionally contract an interface edge in an uncontracted target shore.
Then the target side (minus that edge, when selected) has an
\(r\)-colouring whose exact boundary state is \(\Pi\); when the edge
is selected, its two interface ends have the same colour.

Thus the shore-capacity packing theorem remains valid with an
interface-edge equality imposed simultaneously in the uncontracted
target side.

#### Proof

The carriers assigned within one shore are disjoint by the definition
of a capacity packet. Carriers in distinct shores are disjoint because
the shores are distinct components. After adjoining their disjoint
boundary blocks, all contraction sets remain disjoint. Their images and
the retained singleton blocks form a clique: every quotient edge has a
surviving boundary edge between its two representatives. Hence these
representatives receive distinct colours. Expanding each nonsingleton
block monochromatically gives exactly \(\Pi\). If the optional
interface edge was contracted, expanding it after deletion gives equal
colours at its two ends.
\(\square\)

## 2. The Dirac equality-cell apex dichotomy

Let \(G\) be a \(t\)-contraction-critical graph. Let \(s\ge0\), let
\(v\) have degree \(t+s\), and suppose that \(N_G(v)\) contains an
independent set \(I\) of order \(s+2\). Put

\[
                 H=G-v,\qquad N=N_G(v),
\]

and let \(e=xy\) be an edge of \(H-N\). Contract the connected star
\(G[\{v\}\cup I]\), and contract \(e\), as in Theorem 1.1. Notice that

\[
                         |N-I|=t-2.                \tag{2.0}
\]

### Theorem 2.1 (uniform rainbow-or-detours lemma)

There is a proper \((t-1)\)-colouring \(c\) of \(H-e\) satisfying

\[
 \{u\in N:c(u)=\sigma\}=I,\qquad c(x)=c(y)=\alpha,
\tag{2.1}
\]

and at least one of the following holds.

1. The \(t-2\) vertices of \(N-I\) have pairwise distinct colours. Thus
   (2.1) is an exact repeated-pair/rainbow trace.
2. The colouring extends to a \((t-1)\)-colouring of \(G-e\). In that same
   colouring, for every colour \(\gamma\ne\alpha\), the
   \(\alpha,\gamma\)-subgraph contains an \(x\)-\(y\) path. In
   particular all \(t-2\) edge-critical Kempe detours coexist with the
   exact trace \(I\).

#### Proof

The two contracted sets are disjoint, so the construction in Theorem
1.1 gives (2.1). The colour \(\sigma\) is absent from \(N-I\), since
the contracted star vertex is adjacent to every vertex of \(N-I\).

If the \(t-2\) vertices of \(N-I\) have pairwise distinct colours,
outcome 1 holds. Otherwise \(N\) uses at most \(t-2\) of the
\(t-1\) colours: one colour is used on \(I\), and the other
\(t-2\) vertices use at most \(t-3\) further colours. Give \(v\) a
colour absent from \(N\). This extends \(c\) to a proper
\((t-1)\)-colouring of \(G-e\), proving the first assertion of outcome
2.

Since \(G\) itself is not \((t-1)\)-colourable, the ends \(x,y\) must
have the same colour in every \((t-1)\)-colouring of \(G-e\); here this
is already forced by the contraction. Fix \(\gamma\ne\alpha\). If the
\(\alpha,\gamma\)-component containing \(x\) did not contain \(y\),
interchanging \(\alpha,\gamma\) on that component would give \(x,y\)
different colours. Restoring \(e\) would then produce a
\((t-1)\)-colouring of \(G\), a contradiction. Hence that component
contains an
\(x\)-\(y\) path, as claimed. \(\square\)

### Corollary 2.2 (the Moser trace can be fixed in advance)

For \(t=7,s=0\), the set \(I\) is an independent pair. In the
pure-Moser neighbourhood, take the favourable pair \(I=\{1,3\}\).
For every internal edge of a locked carrier, one may use one colouring
with this fixed trace and obtain either

* the five unique roots on \(N-\{1,3\}\), whose missing-edge graph is
  the prescribed \(C_5\); or
* all five edge-critical Kempe detours around the chosen interface edge,
  without changing the exact trace \(\{1,3\}\).

Thus a clean-gate argument no longer has to choose between the
Moser \(C_5\) witness and an unrelated edge-deletion witness. What is
not yet proved is that one of the five aligned detours has a prefix
avoiding the reserved branch sets, or that a rainbow trace alone gives
the required nonseparating rooted model.

### Corollary 2.2A (the detour branch is a fixed-trace transition)

Assume \(e\) lies in a component \(D\) of \(G-N[v]\), and outcome 2
of Theorem 2.1 holds. Let \(\Pi_e\) be the exact equality state induced
on \(N\), and write \(\mathcal E(C)\) for the exact \(N\)-states
extending over \(G[N\cup C]\). Then

\[
 \Pi_e\in\mathcal E(D-e)\cap
 \bigcap_{C\ne D}\mathcal E(C),
 \qquad
 \Pi_e\notin\mathcal E(D),                         \tag{2.2}
\]

where \(C\) ranges over the other components of \(G-N[v]\), and every
state in (2.2) has \(I\) as an exact block. The colouring also includes
the apex \(v\), whose colour is absent from \(N\).

#### Proof

Outcome 2 is a colouring of the whole graph \(G-e\). Restriction gives
all memberships in (2.2) except the nonmembership. If \(\Pi_e\)
extended over the original \(N\cup D\), align its block colours with
the fixed colouring on all other components and on \(v\), and glue.
This would colour \(G\), a contradiction. The exact \(I\)-trace was
proved in Theorem 2.1. \(\square\)

Thus every non-rainbow interface edge already supplies the
capacity--state alignment required by the critical-web programme. The
remaining alternatives are an actual clean prefix among its
\(t-2\) detours, or the rainbow rooted-minor geometry.

### Theorem 2.2B (matching normalization or an exterior support)

Assume \(t=7\), \(d(v)=7\), and \(\alpha(G[N])\le2\). Fix a nonedge
\(I\) of \(G[N]\) with the following label-free matching-extension
property:

\[
 \begin{array}{c}
 \text{for every nonedge \(J\) disjoint from \(I\), the three vertices}\\
 \text{of \(N-(I\cup J)\) contain a nonedge \(K\).}
 \end{array}                                      \tag{2.3}
\]

Let \(e\) lie in an exterior component \(D\), and suppose outcome 2 of
Theorem 2.1 holds. Then one of the following occurs.

1. The colouring of \(G-e\) can be Kempe-switched, without changing
   the exact block \(I\), so that its state on \(N\) is

   \[
                         I\mid J\mid K\mid\{r\},    \tag{2.4}
   \]

   where \(I,J,K\) are three disjoint nonedges. This state extends
   every unchanged exterior component and \(D-e\), but not \(D\).
2. There is a nonedge \(K=xy\) among the three vertices left by two
   disjoint nonedge blocks \(I,J\), and an \(x\)-\(y\) path whose
   interior lies in one component of \(G-N[v]\).

For the pure-Moser graph and \(I=\{1,3\}\), property (2.3) holds because
\(\overline{G[N-I]}\cong C_5\).

#### Proof

The full colouring of \(G-e\) uses a colour on \(v\) which is absent
from \(N\), and it has \(I\) as an exact block. Since every colour class
on \(N\) has order at most two, \(N\) uses either four or five colours.
With four colours its block sizes are \(2,2,2,1\), giving outcome 1
immediately.

Suppose it uses five colours. Its block sizes are
\[
                         2,2,1,1,1.
\]
Besides \(I\), let \(J\) be the other two-vertex block. By (2.3), two
of the three singleton vertices form a nonedge \(K=xy\). Let their
colours be \(\lambda,\mu\).

If \(x,y\) lie in different components of the
\(\lambda,\mu\)-subgraph, interchange \(\lambda,\mu\) on the component
containing \(x\). No other vertex of \(N\) has either colour, so this
merges exactly \(x,y\) and produces (2.4). It remains a colouring of
\(G-e\). In every such colouring the ends of \(e\) have the same
colour, since otherwise \(e\) could be restored; hence the switch does
not invalidate the edge-transition conclusion. Corollary 2.2A gives
the nonextension over \(D\).

If \(x,y\) lie in the same two-colour component, take a shortest
two-colour path between them. Its interior contains no vertex of \(N\),
because \(x,y\) are the only boundary vertices with those two colours,
and it avoids \(v\), whose colour is absent from \(N\). Therefore its
interior lies in \(G-N[v]\). Since distinct components of
\(G-N[v]\) are anticomplete, all internal vertices lie in one exterior
component. This is outcome 2.

Finally, if (2.4) holds, its block-adjacency quotient is complete.
Indeed, no two pair blocks can be anticomplete, or their union would be
an independent set of order four; and the singleton cannot be
anticomplete to a pair block, or their union would be an independent
set of order three. \(\square\)

### Corollary 2.2C (the accepting shore is totally unboosted)

Assume additionally that \(G-N[v]\) has exactly two components \(C,D\),
with \(e\subseteq D\), and outcome 1 of Theorem 2.2B holds. Then for
no two members \(A,B\in\{I,J,K\}\) does \(C\) contain disjoint
connected carriers meeting both vertices of \(A\) and both vertices of
\(B\), respectively.

#### Proof

Suppose \(C\) contained such a two-packet for \(A,B\), and let \(L\)
be the third pair block. The singleton shore \(\{v\}\) is a connected
carrier meeting both vertices of \(L\), since \(v\) is adjacent to all
of \(N\). Assign the two-block packet to \(C\), the one-block packet
\(L\) to \(\{v\}\), and take \(D\) as target. Corollary 1.4 without
the optional interface-edge contraction transfers the exact state
(2.4) to \(G[N\cup D]\).

But the fixed colouring of \(G-e\) already extends (2.4) over
\(G[N\cup C\cup\{v\}]\). Align the four boundary block colours and
glue. This gives a six-colouring of \(G\), contradicting
minor-criticality. Equivalently, Corollary 2.2A says directly that
(2.4) cannot extend over \(D\). \(\square\)

Thus the normalized branch of the smallest capacity/state mismatch is
one accepting exterior shore with three simultaneous failed
two-packets. The remaining geometric problem is to synchronize the
three Two Paths web outcomes; the path branch of Theorem 2.2B supplies
an actual rooted support instead. This is a reusable exact-adhesion
dichotomy, not a Moser-labelled case list.

### Theorem 2.3 (rainbow or aligned critical vertex)

Keep the equality-cell hypotheses and let \(p\in V(H)-N\). There is a
\((t-1)\)-colouring
\(c\) of \(H-p\) with

\[
                  \{u\in N:c(u)=\sigma\}=I
\tag{2.2}
\]

such that either the \(t-2\) vertices of \(N-I\) are rainbow, or \(c\)
extends to a \((t-1)\)-colouring of \(G-p\) in which \(p\) has a
neighbour of every one of the \(t-1\) colours.

#### Proof

Contract \(G[\{v\}\cup I]\), delete \(p\), and colour the resulting
proper minor. Expand only \(I\) and delete \(v\), as before. This gives
(2.2). If \(N-I\) is not rainbow, some colour of the
\((t-1)\)-palette is absent from \(N\), so give that colour to \(v\).

Now \(c\) is a \((t-1)\)-colouring of \(G-p\). If some colour were absent
from \(N_G(p)\), assigning it to \(p\) would \((t-1)\)-colour \(G\), a
contradiction. Thus every colour occurs in \(N_G(p)\). \(\square\)

For the unique-\(Q\)-portal outcome in Corollary 5.4 below, Theorem 2.3
aligns the favourable Moser trace with the full six-colour neighbourhood
of that irreplaceable portal. It still does not identify those coloured
neighbours with particular branch sets; that identification is the
remaining exchange step.

## 3. A portal skeleton for a locked carrier

Use the abstract carrier notation

\[
       (T;t,R,F,Q_1,\ldots,Q_q)
\]

from hadwiger_locked_carrier_dependency_spine.md. Choose actual
representatives

\[
 r\in R,\qquad f\in F,\qquad q_j\in Q_j\quad(j\in[q]),
\tag{3.1}
\]

and let \(K\) be an inclusion-minimal connected subgraph of \(T\)
containing \(t,r,f,q_1,\ldots,q_q\).

### Lemma 3.1 (minimal portal skeleton)

The graph \(K\) is a tree. If an edge of \(K\) separates a component
\(A\) containing \(r,f\) from a component \(B\) containing
\(t,q_1,\ldots,q_q\), then the original contact lock opens.
Consequently, in a locked carrier no such edge exists, for any choice
of the representatives (3.1).

After suppressing unmarked degree-two vertices, \(K\) has at most
\(q+3\) leaves and at most \(q+1\) branch vertices.

#### Proof

If \(K\) contained a cycle, deleting an edge of that cycle would leave a
smaller connected subgraph containing all marked vertices, contrary to
minimality. Hence \(K\) is a tree.

For the displayed edge, \(A,B\) are nonempty, connected and adjacent.
They meet the required portal classes through the selected
representatives. They are therefore a detachable rooted carrier inside
the subgraph \(K\). Discard every vertex of the old branch set outside
\(K\), and use \(A,B\) in the terminal-arm bypass construction. Branch
sets in a minor model need not contain discarded vertices, so this is a
valid improvement. A locked carrier forbids the edge.

A tree whose marked set has order \(q+3\) has at most \(q+3\) leaves in
its inclusion-minimal marked subtree, and at most \(q+1\) vertices of
degree at least three. \(\square\)

### Lemma 3.2 (exact alternating-tree certificate)

Root \(K\) at \(t\), and let \(b\) be the lowest common ancestor of
\(r,f\). A detachable edge as in Lemma 3.1 exists if and only if
\(b\ne t\) and the rooted subtree \(K_b\) contains none of
\(q_1,\ldots,q_q\).

Hence a locked choice of representatives has the following exact
certificate:

\[
 b=t\quad\hbox{or}\quad
 \{q_1,\ldots,q_q\}\cap V(K_b)\ne\varnothing .
\tag{3.2}
\]

#### Proof

An edge whose component away from \(t\) contains both \(r,f\) must lie
on the \(t\)-to-\(b\) path. If \(b=t\), there is no such edge. If
\(b\ne t\), the lowest such edge is the edge entering \(b\), and its
far component is \(K_b\). Every higher candidate component contains
\(K_b\). Thus some candidate avoids all helper representatives exactly
when \(K_b\) does. \(\square\)

This is only a certificate inside a freely chosen branch-set skeleton.
It makes no assertion that deleting one skeleton vertex separates the
same portals in the ambient graph. Host edges outside \(K\) may provide
the clean prefixes in Theorem 2.1, and controlling those prefixes remains
the genuine exchange problem. The gain is that the internal carrier
obstruction itself is a bounded marked-tree order, not an arbitrary
non-tree geometry.

### Lemma 3.3 (long skeletons contain an eligible interface edge)

Let \(Z\) be any distinguished vertex set and let \(m=q+3\) be the
number of marked vertices of the portal skeleton \(K\). If every edge
of \(K\) has at least one end in \(Z\), then

\[
             |V(K)|\le 2|Z\cap V(K)|+m-1.
\tag{3.3}
\]

Consequently, in the degree-seven application, every skeleton of order
greater than

\[
             2|N\cap V(K)|+q+2\le q+16
\tag{3.4}
\]

has an edge with both ends outside \(N\). For the clean
\(K_{2,4}\) lock, \(q=4\), so every skeleton of order greater than
twenty has an edge to which Theorem 2.1 applies.

#### Proof

Put \(A=Z\cap V(K)\) and \(B=V(K)-A\). By hypothesis \(B\) is an
independent set. An unmarked leaf cannot occur in the inclusion-minimal
tree \(K\). Delete the marked vertices of \(B\) temporarily. Every
remaining vertex of \(B\) has degree at least two in the original tree.

Contract every edge with both ends in \(A\). The resulting graph is a
forest with at most \(|A|\) vertices on its contracted \(A\)-side. In a
forest whose other-side vertices all have degree at least two, their
number is at most \(|A|-1\): summing \(\deg(b)-1\) over those vertices
is at most the number of \(A\)-side vertices minus the number of
nonempty components. Restoring the contractions does not change their
number. There are at most \(m\) marked vertices in \(B\). Hence

\[
 |B|\le (|A|-1)+m,\qquad
 |V(K)|=|A|+|B|\le2|A|+m-1,
\]

which is (3.3). Now take \(Z=N\), use \(|N|=7\), and substitute
\(m=q+3\). \(\square\)

The numerical bound is deliberately coarse. Its purpose is to separate
the infinite subdivision problem from a finite marked-tree residue. It
does not enumerate that residue and it does not assert that the eligible
edge has a clean detour.

## 4. Current consequence for the clean-gate programme

For the clean \(K_{2,4}\) lock, \(q=4\). Every surviving repeated
terminal carrier therefore has a certificate which is a subdivision of
a tree with at most seven marked leaves and five branch vertices.
On every selected skeleton interface edge, Corollary 2.2 supplies either
the favourable rainbow Moser trace or five aligned Kempe detours.

The exact unresolved lemma is now:

> In a seven-contraction-critical host, an alternating marked portal
> skeleton satisfying (3.2) cannot have every aligned Kempe detour meet
> a reserved branch before it reaches the uniquely trapped helper.

A proof must use the actual first-hit attachments of the detours. It may
not infer an ambient cut from the skeleton tree alone.

## 5. Strict zero-helper surplus is a doubly hit helper

Work after all path-accessible helpers have been absorbed into the
protected residue \(B\), and let \(Q\) be one zero-access helper. Thus
the six prospective branch sets form a \(K_6\) minus the edge \(BQ\).
Name the other four branch sets

\[
                       L_1,L_2,L_3,L_4 .
\]

All fixed capture paths, the prospective arm, and the final connector
have already been assigned to these six prospective branch sets. Form
the usable repair graph by retaining \(B,Q\), and every unassigned
vertex, and deleting \(v,L_1,\ldots,L_4\). Let \(U\) be its component
containing \(B\), and put \(P=N_G(U)\).

### Lemma 5.1 (five-object compression)

\[
                  P\subseteq \{v\}\cup
                  L_1\cup L_2\cup L_3\cup L_4 .
\tag{5.1}
\]

If \(G\) is seven-connected and \(|P|\ge8\), then some \(L_i\)
contains two distinct vertices having neighbours in \(U\).

#### Proof

The helper \(Q\) is retained in the usable graph but lies in a component
different from \(U\); hence no edge joins \(U\) to \(Q\). Every
unassigned vertex is also retained. Therefore a neighbour of \(U\)
which is absent from its usable component must be one of the deleted
vertices, proving (5.1).

The apex contributes at most one vertex to \(P\). Thus at least seven
vertices of \(P\) lie in the four disjoint branch sets \(L_i\).
Pigeonhole gives two in one \(L_i\). \(\square\)

### Definition 5.2 (helper peel)

For the repeated branch \(L=L_i\), a helper peel is a partition

\[
                         L=A\mathbin{\dot\cup}C
\]

into nonempty connected adjacent sets such that

* \(A\) has a neighbour in \(U\) and is adjacent to \(Q\);
* \(C\) contains the prescribed old root of \(L\);
* \(C\) is adjacent to \(Q\) and to each \(L_j\), \(j\ne i\).

### Lemma 5.3 (a helper peel repairs the defect)

If a helper peel exists, then \(G\) contains a \(K_7\)-minor.

#### Proof

Absorb \(A\), together with a shortest \(B\)-to-\(A\) path in
\(G[U\cup A]\), stopped at first entry into \(A\), into the protected
residue \(B\). The path interior lies in the usable component \(U\), so
it avoids every other branch set. The enlarged \(B\) is now adjacent to
\(Q\) through the old \(A\)-\(Q\) edge. Replace \(L\) by \(C\).

The new \(C\)-bag sees the enlarged \(B\) through the \(A\)-\(C\)
edge, retains its old root and hence its apex contact, and by definition
sees \(Q\) and the other three \(L_j\)'s. Every other old clique
adjacency is unchanged. The resulting six bags in \(G-v\) are pairwise
adjacent and all meet \(N(v)\); adjoining \(\{v\}\) gives a
\(K_7\)-model. \(\square\)

### Corollary 5.4 (strict-surplus normal form)

For a zero-access helper in the clean \(K_{2,4}\) programme, at least
one of the following holds.

1. \(|P|=7\), and the shore-capacity normalization in
   hadwiger_locked_carrier_dependency_spine.md applies.
2. \(|P|\ge8\), and a helper peel gives a \(K_7\)-minor.
3. \(|P|\ge8\), and some doubly hit \(L_i\) has a unique
   \(Q\)-portal. This is a single irreplaceable helper charge.
4. \(|P|\ge8\), and some doubly hit \(L_i\) has at least two
   \(Q\)-portals and is itself a locked rooted carrier with portal
   classes

   \[
   R=N_{L_i}(U),\quad F=N_{L_i}(Q),
   \]

   prescribed terminal equal to its old root, and helper classes
   consisting of a distinct \(Q\)-portal retained by the residue and
   its three other \(L_j\)-adjacencies. For every choice of distinct
   arm/residue \(Q\)-portal representatives it therefore has the
   alternating portal skeleton of Lemmas 3.1--3.3, with \(q=4\).

#### Proof

Seven-connectivity gives \(|P|\ge7\). The equality case is the existing
exact-adhesion theorem. In the strict case Lemma 5.1 gives a repeated
branch. If it has the displayed partition, Lemma 5.3 applies. If it
has only one \(Q\)-portal, outcome 3 holds. Otherwise choose distinct
arm and residue representatives from \(N_{L_i}(Q)\). The negation of
Definition 5.2 is then precisely the locked-carrier condition for the
listed terminal and helper requirements. Apply Lemmas 3.1--3.3.
\(\square\)

The reference to a second \(Q\)-portal in outcome 4 is substantive.
If the residue has no \(Q\)-portal, a partition whose arm sees \(Q\)
does not preserve the \(L_iQ\) clique edge and is not a helper peel.
That absence is itself one of the locked helper charges; no portal is
silently duplicated.
