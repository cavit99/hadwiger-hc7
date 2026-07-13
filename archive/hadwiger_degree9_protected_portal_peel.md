# The degree-nine Moser lock: protected portal peels

This note continues `hadwiger_degree9_hub_portal_lock.md`.  We retain its
balanced spanning rooted model

\[
                         L_6,L_0,R_5,R_0,                    \tag{1.1}
\]

where (6\in L_6), (5\in R_5), the first two bags have roots
complete to ({1,2}), and the last two have roots complete to
({3,4}).  Let (K) be the component of (L_6-6) containing the
root of (L_6), and put (D=L_6-K).  Then (D) is connected, contains
(6), and is adjacent to (K).

The purpose of this note is to identify exactly which *internal* target
bag rerouting closes the strict-surplus alternatives of Theorem 5.2 of
the preceding note.  The result is not a quotient calculation: it works
for bags of arbitrary order.

## 1. A connected/co-connected hull lemma

### Lemma 1.1 (protected-core peel)

Let (T) be a connected graph and let (Q\subseteq T) be a nonempty
connected subgraph.  If two vertex sets (A,B\subseteq V(T)-V(Q))
meet the same component of (T-Q), then there is a partition

\[
                         V(T)=X\mathbin{\dot\cup}Y             \tag{1.2}
\]

such that

* (T[X]) and (T[Y]) are connected;
* (Q\subseteq T[Y]);
* (X) meets both (A) and (B); and
* (E_T(X,Y)\ne\varnothing).

#### Proof

Take an (A)-to-(B) path (P) in one component of (T-Q).  Let
(Y) be the component of (T-V(P)) containing (Q), and put
(X=V(T)-Y).  The set (Y) is connected.  Every component of
(T-V(P)) other than (Y) has a neighbour on (P), since (T) is
connected.  Consequently (T[X]), which consists of (P) together
with all those components, is connected.  It contains an (A)-vertex
and a (B)-vertex.  Finally (X\ne V(T)), and connectedness of (T)
gives an (X)-(Y) edge. \(\square\)

The lemma is the elementary core of a portal splitter: a failure of the
peel says that the protected portal core separates the two specified
portal classes.  No planarity, bounded order, or internal connectivity
of (T) beyond connectedness is used.

## 2. Peeling the ordinary right bag

### Theorem 2.1 (ordinary-right protected peel)

Assume (K) is not adjacent to (L_0).  Suppose (R_0) has a
partition into connected adjacent sets

\[
                         R_0=X\mathbin{\dot\cup}Y             \tag{2.1}
\]

such that the root of (R_0) lies in (Y), and

\[
        X\sim K,\qquad X\sim L_0,\qquad Y\sim L_0.            \tag{2.2}
\]

Then (G) contains a (K_7)-minor.

#### Proof

Put (U=K\cup X).  It is connected.  Since the old (L_6)-(L_0)
adjacency cannot have an endpoint in (K), the set (D) is adjacent
to (L_0).  Use the seven branch sets

\[
 \{h\},\quad \{1\},\quad \{2\},\quad U,\quad L_0,
 \quad Y\cup\{3,v\},\quad R_5\cup\{4\}\cup D.                \tag{2.3}
\]

They are disjoint and connected.  The last set is connected through the
right root--(4) edge and the path through (5,6) into (D).

The first five sets form a clique using the left roots, (12), and
the (X)-(L_0) edge.  The sixth sees (1,2) through (v), sees
(U) through the (X)-(Y) edge, and sees (L_0) by (2.2).  The
last sees (1,2) through (6), sees (U) through the (K)-(D)
edge, and sees (L_0) through the old (R_5)-(L_0) adjacency.
The last two sets are adjacent through (v5) (also through (34)).
Every nonsingleton set sees (h) through its appropriate exterior root.
Thus (2.3) is a (K_7)-model. \(\square\)

### Corollary 2.2 (portal-core separation in (R_0))

Assume (G) has no (K_7)-minor, (K\not\sim L_0), and
(K\sim R_0).  Let (Q\subseteq R_0) be any connected subgraph which
contains the root of (R_0) and at least one (R_0)-portal to (L_0).
Then no component of (R_0-Q) contains both

1. a vertex adjacent to (K), and
2. a vertex adjacent to (L_0).

#### Proof

Otherwise apply Lemma 1.1 in (R_0).  Its (X,Y) satisfy (2.1)--(2.2),
contrary to Theorem 2.1. \(\square\)

Thus a strict surplus landing in (R_0) is not merely a pair of quotient
contacts: every connected protected root--(L_0) portal core separates
the (K)-portals from every further (L_0)-portal.

## 3. Peeling the outer right bag

### Theorem 3.1 (outer-right protected peel)

Assume (K\not\sim L_0) and (K\not\sim R_0).  Suppose

\[
                         R_5=X\mathbin{\dot\cup}Y             \tag{3.1}
\]

is a partition into connected adjacent sets such that the root of
(R_5) and the vertex (5) both lie in (Y), and

\[
        X\sim K,\qquad X\sim L_0,\qquad Y\sim L_0.            \tag{3.2}
\]

Then (G) contains a (K_7)-minor.

#### Proof

Again put (U=K\cup X).  Since (K\not\sim R_0), the old
(L_6)-(R_0) adjacency has its (L_6)-endpoint in (D), so
(D\cup R_0) is connected.  Use

\[
 \{h,3,4\},\quad \{v\}\cup Y,
 \quad \{1\},\quad \{2\},\quad U,
 \quad D\cup R_0,\quad L_0.                                 \tag{3.3}
\]

The first set is connected because (h34) is a triangle, and the
second is connected through (v5).  The first two are adjacent through
the root of (R_5).  Both see (1,2), the first through (h) and the
second through (v).  They see (U,D\cup R_0,L_0) through the
exterior roots, the (X)-(Y) edge, the edge (v6), and (3.2), as
appropriate.  Finally

\[
                 \{1\},\{2\},U,D\cup R_0,L_0
\]

form a clique: use (12), the left-root contacts, the (K)-(D)
edge, the (X)-(L_0) edge, and the old (R_0)-(L_0) adjacency.
Hence (3.3) is a (K_7)-model. \(\square\)

### Corollary 3.2 (portal-core separation in (R_5))

Assume there is no (K_7)-minor, (K\not\sim L_0,R_0), and
(K\sim R_5).  Let (Q\subseteq R_5) be connected and contain the
root of (R_5), the vertex (5), and at least one (R_5)-portal to
(L_0).  Then no component of (R_5-Q) contains both a (K)-portal
and an (L_0)-portal.

#### Proof

Apply Lemma 1.1 and Theorem 3.1. \(\square\)

## 4. The exact new residue

There is a complementary splitter when the surplus stays in the left
ordinary bag.  Its natural formulation is a two-linkage theorem, rather
than another contact table.

### Lemma 4.1 (two connected subgraphs extend to a bipartition)

Let (T) be connected and let (P,Q\subseteq T) be disjoint nonempty
connected subgraphs.  There is a partition (V(T)=X\dot\cup Y) into
connected sets with (P\subseteq T[X]) and (Q\subseteq T[Y]).

#### Proof

Contract (P) and (Q), take a spanning tree of the resulting connected
graph, and delete one edge of the unique tree path between the two
contracted vertices.  The two tree components give the required
partition after undoing the contractions. \(\square\)

### Theorem 4.2 (crossed two-linkage closes the same-bag surplus)

Assume

\[
              K\not\sim R_5,\qquad K\not\sim R_0.             \tag{4.1}
\]

Put

\[
 A=N_{L_0}(K),\qquad
 B=N_{L_0}(R_5),\qquad C=N_{L_0}(R_0).                        \tag{4.2}
\]

If there are distinct (a,a'\in A), vertices (b\in B,c\in C), and
vertex-disjoint paths in (L_0), one joining (a) to (b) and the
other joining (a') to (c), then (G) contains a (K_7)-minor.

#### Proof

By Lemma 4.1 extend the two paths to a connected bipartition

\[
                         L_0=X\mathbin{\dot\cup}Y.             \tag{4.3}
\]

Both (X,Y) are adjacent to (K); one sees (R_5) and the other sees
(R_0).  Rename the two sides so that the root of (L_0) lies in (Y).

First suppose (X\sim R_5) and (Y\sim R_0).  Use

\[
 \{h\},\quad\{1\},\quad\{2\},\quad K,\quad Y,
 \quad D\cup R_0,\quad \{v\}\cup X\cup R_5.                 \tag{4.4}
\]

Here (D\cup R_0) is connected because (4.1) forces the old
(L_6)-(R_0) adjacency to have its (L_6)-endpoint in (D), and
the last set is connected through the (X)-(R_5) and (v5) edges.
The five sets after the first three form a clique: use (K)-(Y),
(K)-(D), (K)-(X), (Y)-(R_0), (X)-(Y), and (v6).
The left roots, the right root in (R_0), the right root in (R_5),
(6), and (v) give their required contacts to
({h},\{1\},\{2\}).

Now suppose (X\sim R_0) and (Y\sim R_5).  Use instead

\[
 \{h\},\quad\{1\},\quad\{2\},\quad K,\quad Y,
 \quad D\cup R_5,\quad \{v,3\}\cup X\cup R_0.                \tag{4.5}
\]

The last set is connected through (X)-(R_0), the right-root--(3)
edge, and (3v); (D\cup R_5) is connected through (65).  The set
(K) sees the last set through (K)-(X), while (Y) sees it through
the (X)-(Y) edge.  The set (Y) sees (D\cup R_5) through its
(R_5)-contact, and (K) sees it through (K)-(D).  The boundary
vertices and the left roots give all contacts with
({h},\{1\},\{2\}), and the last two large sets meet through (v5)
(also through (v6)).  Hence (4.5) is a (K_7)-model. \(\square\)

### Corollary 4.3 (a genuine Two Paths obstruction)

Under (4.1), if (G) has no (K_7)-minor, then for every choice of
distinct (a,a'\in A), (b\in B), and (c\in C), the graph (L_0)
has no pair of vertex-disjoint paths joining (a) to (b) and (a')
to (c).

This is the exact point at which the Robertson--Seymour Two Paths
Theorem becomes relevant: the unbounded same-bag residue is a
four-terminal web obstruction, not an arbitrary large branch bag.

In fact the flexibility of the two starts in \(A\) makes the obstruction
strictly simpler than a general prescribed-pair Two Paths obstruction.

### Lemma 4.4 (flexible-start two-linkage or one-vertex transversal)

Let \(T\) be connected and let \(A,B,C\) be nonempty vertex sets, with
\(|A|\ge2\).  At least one of the following holds.

1. There are two vertex-disjoint paths in \(T\), one from \(A\) to
   \(B\) and one from \(A\) to \(C\), with distinct initial vertices in
   \(A\) and distinct terminal vertices.
2. There is one vertex \(q\in V(T)\) which meets every path from \(A\)
   to \(B\cup C\).

Here a path of order one is allowed when two of the displayed terminal
sets overlap.

#### Proof

Direct every edge of \(T\) both ways and impose unit vertex capacities.
On the ground set \(B\cup C\), declare \(Z\) independent when there are
pairwise vertex-disjoint paths from distinct vertices of \(A\) to the
vertices of \(Z\).  Reversing those paths, these linkable sets form the
standard strict gammoid with sink set \(A\) in the bidirected graph.

Every element of \(B\cup C\) is a nonloop, since \(T\) is connected.
Suppose outcome 1 fails.  Then every two-element set
\(\{b,c\}\), with \(b\in B,c\in C\) and \(b\ne c\), is dependent.
Dependence of a pair of nonloops is parallelism, and parallelism is
transitive in a matroid.  It follows that all elements of \(B\cup C\)
belong to one parallel class.  (If \(B\cup C\) has only one element,
this conclusion is immediate.)  Hence the maximum number of disjoint
\(A\)-to-\((B\cup C)\) paths is one.  The vertex form of Menger's
theorem now supplies a one-vertex transversal \(q\) meeting every such
path.  We use the endpoint-inclusive form of Menger: the transversal
may lie in \(A\cup B\cup C\), exactly as is necessary when the displayed
sets overlap. \(\square\)

The use of a gammoid is only a compact form of the usual
vertex-capacitated augmenting-path proof.  The assertion would be false
for two *prescribed* starts; allowing any two distinct members of \(A\)
is the decisive exchange.

### Corollary 4.5 (the same-bag residue has a literal bottleneck)

Assume (4.1), \(|A|\ge2\), and that \(G\) has no \(K_7\)-minor.  Then
there is a vertex

\[
                         q\in V(L_0)                         \tag{4.6}
\]

which meets every \(A\)-to-\((B\cup C)\) path in \(L_0\).

#### Proof

Outcome 1 of Lemma 4.4 is exactly the hypothesis of Theorem 4.2.
Therefore outcome 2 must hold. \(\square\)

Thus the same-bag residue is not an arbitrary four-terminal web.  All
four (outside an exact seven-cut) protected \(K\)-portals are separated
from both right-portal classes by one literal vertex of \(L_0\).  The
vertex \(q\) is allowed to be the unique member of \(B\cup C\); when
there is a target portal different from \(q\), it is an ordinary
cutvertex separating that target from at least one of the four
\(K\)-portals.

### Theorem 4.6 (exact adhesion or an external three-class bypass)

Retain the hypotheses of Corollary 4.5 and put

\[
                         S=\{q,h,1,2,3,4,6\}.                 \tag{4.7}
\]

Then either \(S\) is an exact seven-cut separating \(K\) from \(v\),
or \(G-S\) contains a \(K\)-to-\(5\) path.  Moreover, after such a path
first enters a component of \(L_0-q\) containing an \(A\)-vertex, its
first exit from that component (without returning to \(K\)) is through
an edge to \(D=L_6-K\).

#### Proof

Let \(Z\) be the component of \(G-S\) containing \(K\).  If \(v\notin
Z\), then \(N_G(Z)\subseteq S\).  Seven-connectivity forces equality,
so \(S\) is an exact seven-cut.

Otherwise \(Z\) contains a \(K\)-to-\(v\) path.  The only neighbour of
\(v\) outside \(S\) is \(5\), so deletion of the final edge gives a
\(K\)-to-\(5\) path in \(G-S\).  Choose one with no return to \(K\)
after its first departure.  The exact neighbourhood theorem in
hadwiger_degree9_cross_half_gate.md gives

\[
                         N(K)=\{h,1,2,6\}\dot\cup A.           \tag{4.8}
\]

Thus the path first enters \(L_0-q\) through an \(A\)-vertex.  Let \(R\)
be that component of \(L_0-q\).  By the defining property of \(q\),
\(R\) contains no member of \(B\cup C\), and hence has no edge to
\(R_5\) or \(R_0\).  It cannot leave through \(q\), through another
component of \(L_0-q\), or back through \(K\).  The spanning four-bag
model exhausts all remaining exterior vertices.  All literal boundary
vertices except \(5\) have been deleted, while an edge to \(5\) would
itself be an \(R_5\)-portal.  Therefore the first remaining exit is an
edge from \(R\) to \(D\). \(\square\)

The bottleneck \(q\) does not by itself expose an exact cut, because an
\(A\)-component may have contacts in \(D-\{6\}\).  Instead, every
non-adhesion outcome contains the forced bypass

\[
              K\longrightarrow L_0-q\longrightarrow D
              \longrightarrow (R_5\cup R_0)\longrightarrow5. \tag{4.9}
\]

The remaining operation is consequently a two-bag, label-preserving
split, not an unrestricted web theorem.

### Theorem 4.7 (portal-lobe peel or transfer into \(D\))

Let \(r_0\) be the unique exterior root in \(L_0\), and let
\(\mathcal A\) be the set of components of \(L_0-q\) which meet \(A\).
Assume that \(G\) has no \(K_7\)-minor.

1. Every member of \(\mathcal A\) is disjoint from \(B\cup C\).
2. If \(U\in\mathcal A\) and \(r_0\notin U\), then
   \(U\) is anticomplete to \(\{3,4\}\).
3. If \(r_0\in U\in\mathcal A\) and
   \(|\mathcal A|\ge2\), the same conclusion holds.

Consequently, unless \(\mathcal A=\{U\}\) with \(r_0\in U\), put

\[
 W=K\cup\bigcup_{U\in\mathcal A}U,\qquad
 P_D=N(W)\cap(D-\{6\}).
                                                               \tag{4.10}
\]

Then \(W\) is connected and

\[
             N_G(W)=\{h,1,2,6,q\}\mathbin{\dot\cup}P_D.        \tag{4.11}
\]

In particular \(|P_D|\ge2\); equality makes (4.11) an exact
seven-cut, while outside the exact-adhesion outcome

\[
                              |P_D|\ge3.                       \tag{4.12}
\]

#### Proof

Item 1 is the defining property of \(q\): a path inside one component
of \(L_0-q\) from an \(A\)-vertex to a \(B\)- or \(C\)-vertex would
avoid \(q\).

Fix \(U\in\mathcal A\) and put \(Y=L_0-U\).  The set \(Y\) is
connected: it consists of \(q\) and all the other components of
\(L_0-q\).  It contains \(B\cup C\), and \(U,Y\) are adjacent.
Suppose first that \(r_0\in Y\) and \(U\sim3\).  The seven sets

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 D\cup R_5,\quad \{3\}\cup K\cup U,\quad
 \{4\}\cup Y\cup R_0                                      \tag{4.13}
\]

form a \(K_7\)-model.  Connectivity uses \(65\), a \(K\)-\(U\)
portal and the assumed \(U\)-\(3\) edge, and a \(Y\)-\(R_0\)
portal together with the right-root--\(4\) edge.  The last three
sets are pairwise adjacent through \(K D\), an \(R_5\)-\(Y\)
edge, and \(34\), respectively.  Their contacts to
\(\{v\},\{h\},\{1\},\{2\}\) come, respectively, from \(5,6,3,4\)
and the roots in \(R_5,K,Y,R_0\).  This audits all remaining
adjacencies.  Interchanging \(3,4\) proves the same assertion from
\(U\sim4\).  This proves item 2.

Now suppose \(r_0\in U\) and \(|\mathcal A|\ge2\).  Then \(Y\) meets
\(A\), so \(K\sim Y\).  From \(U\sim3\), use

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 \{3\}\cup U,\quad D\cup R_5,\quad
 \{4\}\cup K\cup Y\cup R_0.                                \tag{4.14}
\]

The last set is connected through the \(K\)-\(Y\) and
\(Y\)-\(R_0\) edges and the right-root--\(4\) edge.
The three large sets meet through \(3\) and the right root of \(R_5\),
through \(U K\) (also through \(34\)), and through \(K D\).
The boundary contacts again come from the displayed outer vertices and
the roots.  Swapping \(3,4\) handles \(U\sim4\), proving item 3.

Assume now that the exceptional one-component root-bearing case does
not occur.  Items 2 and 3 make every member of \(\mathcal A\)
anticomplete to \(\{3,4\}\).  The set \(W\) in (4.10) is connected,
because \(K\) has a neighbour in every member of \(\mathcal A\).
All its neighbours in \(L_0-W\) are \(q\), and item 1 excludes
neighbours in \(R_5\cup R_0\).  The vertex \(v\) has no exterior
neighbour, Theorem 2.1 of
`hadwiger_degree9_cross_half_gate.md` excludes \(K\)-\(3,4\)
edges, and items 2--3 exclude the remaining \(3,4\) edges.
The spanning four-bag model therefore gives the inclusion from left to
right in (4.11).

Conversely, \(K\) sees \(h,1,2,6\), every component of \(L_0-q\)
has an edge to \(q\), and \(P_D\) was defined to contain every remaining
\(D\)-neighbour.  Hence equality holds in (4.11).  It is a genuine
separator: \(W\ne\varnothing\), while \(v,R_5,R_0\) lie on the far
side.  Seven-connectivity gives \(5+|P_D|\ge7\).  Equality is the
exact seven-cut, and otherwise integrality gives (4.12). \(\square\)

The theorem replaces a four-portal lock in \(L_0\) by either one
exceptional root-bearing lobe or at least three protected portals in
the adjacent gate piece \(D-\{6\}\).  This is a literal portal-transfer
operation, rather than further finite boundary casework.

### Corollary 4.8 (exact row of the exceptional root-bearing lobe)

In the exceptional case \(\mathcal A=\{U\}\), \(r_0\in U\), put

\[
 W_0=K\cup U,\qquad
 C_{34}=N(W_0)\cap\{3,4\},\qquad
 P_D=N(W_0)\cap(D-\{6\}).                                  \tag{4.15}
\]

Then

\[
 N_G(W_0)=
 \{h,1,2,6,q\}\mathbin{\dot\cup}C_{34}
 \mathbin{\dot\cup}P_D.                                    \tag{4.16}
\]

Consequently

\[
                  |C_{34}|+|P_D|\ge2.                       \tag{4.17}
\]

Equality in (4.17) is an exact seven-cut; outside that outcome,

\[
                  |C_{34}|+|P_D|\ge3.                       \tag{4.18}
\]

In particular \(P_D\ne\varnothing\) in the strict residue.

#### Proof

The set \(W_0\) is connected through the \(K\)-\(U\) portal edges.
Because \(U\) is the unique \(A\)-component, all neighbours of \(K\)
in \(L_0-W_0\), and all neighbours of \(U\) in another component of
\(L_0-q\), are accounted for by \(q\).  Item 1 of Theorem 4.7 excludes
edges from \(U\) to \(R_5\cup R_0\), while (4.1) excludes them from
\(K\).  The vertex \(v\) has no exterior neighbour.  The spanning model
therefore leaves only the displayed fixed vertices, possible
\(3,4\)-contacts, and vertices of \(D-\{6\}\).  Conversely
\(K\) sees \(h,1,2,6\), and \(U\) sees \(q\); hence (4.16) is equality.

It is a genuine separator, with \(v,R_5,R_0\) surviving on the far
side.  Seven-connectivity gives (4.17).  Equality makes the displayed
neighbourhood have order seven, and otherwise integrality gives (4.18).
Since \(|C_{34}|\le2\), (4.18) forces \(P_D\ne\varnothing\).
\(\square\)

## 5. The exact new residue

The sharper cross-half theorem in `hadwiger_degree9_cross_half_gate.md`
says that, outside an exact seven-cut, the gate (K) has at least four
distinct protected portals into its sole allowed attachment class.
Theorems 2.1 and 3.1 above show that these portals cannot
cohabit a detachable region with a duplicate portal to (L_0).  Thus
the surviving object is an **ordered portal lock**:

* if the surplus reaches (R_0), every connected core protecting the
  right root and one (L_0)-portal separates all (K)-portals from all
  other (L_0)-portals;
* if it reaches only (R_5), the same holds after additionally protecting
  the outer vertex (5).
* if all surplus portals lie in (L_0), Lemma 4.4 collapses all the
  crossed-linkage obstructions to one literal bottleneck \(q\).  The
  bottleneck gives either the exact cut or the forced bypass (4.9).
  Theorem 4.7 then transfers the lock to at least three portals in
  \(D-\{6\}\), except for the single root-bearing \(q\)-lobe containing
  every \(K\)-portal.

The symmetric statements hold at the (R_5-5) gate.  This is strictly
stronger than the balanced quotient lock: the quotient forgets which
portal classes are separated by the protected core.  It also identifies
the next reusable target without further finite casework: prove that two
opposite transferred locks (or the two exceptional root-bearing lobes)
in a seven-connected contraction-critical host either have crossing
detours or expose a color-gluable adhesion of order seven.

### Subsequent capacity exchange

`hadwiger_degree9_two_carrier_capacity_exchange.md` now proves the
label-preserving part of this target.  Terminal-clean opposite paths give
the minor even when they intersect, while the unreserved assertion is
refuted by a width-five quotient.  More importantly, a transferred lock
can be alternated monotonically between (D) and the residual ordinary
bag: a mixed two-target split gives an explicit (K_7)-model, and a
one-vertex bottleneck permits absorption of every source-side component.
The absorbed shore strictly grows.  The sharpened invariant in that note
shows that an exact seven-neighbourhood still leaves two active sources
(three when the bottleneck is the fixed vertex (6)).  Therefore the
process continues through every intermediate equality and terminates in
the minor or the exceptional root-bearing bottleneck lobe.  It does
**not** need, or prove, that an arbitrary exact seven-adhesion has
compatible six-colour boundary states.

The exact outcome of Theorem 4.6 is sharpened further in
`hadwiger_degree9_exact_cut_ordered_spine.md`: unless the ordinary-left
root lies in the (K)-side component, the three explicit bags

\[
 Z\cup\{3\},\qquad R_5\cup\{6\},\qquad
 R_0\cup P\cup\{4\}
\]

together with (v,h,1,2) form a (K_7)-model.  If the root instead lies
on the (K)-side, (q) literally separates it from both right portal
classes and misses (v,h,1,2).  That ordered spine is also eliminated:
either the (K)-component sees (3) or (4) and the two roots can be
exchanged, or its connected complement sees both; retaining the old
(L_6)-(R_0), (L_0)-(R_5), and (L_0)-(R_0) carrier edges then gives

\[
 \{v\},\{h\},\{3\},\{4\},R_5,
 D_0\cup R_0,\ X\cup P\cup\{1\}
\]

as a (K_7)-model.  Hence the original exact-cut outcome of Theorem 4.6
is closed completely.  This does not automatically close the different
exact adhesions which may be produced later by the alternating capacity
exchange.

The first such later equality, (4.11) with two (D-{6\}) portals, is
analyzed in `hadwiger_degree9_thm47_exact_adhesion_exchange.md`.  A mixed
(D)-to-(R_5,R_0) split gives (K_7).  Otherwise the flexible
two-target transversal is forced to be the literal vertex (6); after
absorbing the (d_1,d_2)-components, the exact boundary becomes

\[
 N(U)=\{h,1,2,6,q\}\mathbin{\dot\cup}P_Q,
 \qquad P_Q\subseteq Q,
\]

with (|P_Q|\ge2), and strict surplus (|P_Q|\ge3).  A verified
width-five quotient retaining every old rooted-model allocation shows
that this transfer alternative is statically sharp.  It is not a
terminal adhesion, however: the alternating capacity exchange works with
two sources, so it continues through equality and ends in (K_7) unless
the transferred portals enter the single root-bearing bottleneck lobe.
