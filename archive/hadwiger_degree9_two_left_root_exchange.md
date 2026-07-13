# Two-left-bag root exchange in the ordered Moser residue

## 1. Setting

Use one of the strict ordered-prefix rows from
hadwiger_degree9_ordered_spine_prefix.md.  Write

\[
 L_6=K\mathbin{\dot\cup}D,\qquad
 L_0=P\mathbin{\dot\cup}S,                                  \tag{1.1}
\]

where:

* \(e_6\in K\) and \(6\in D\);
* \(r_0\in P\);
* \(K,D,P,S\) are connected;
* \(KD,PS,PK,SK\) are present;
* \(K\) and \(P\) are anticomplete to \(R_5\cup R_0\);
* \(D\) and \(S\) each retain the old contacts to \(R_5,R_0\).

The ordered-prefix theorem also gives

\[
 A=N_K(P),\qquad |A|\ge4                                   \tag{1.2}
\]

outside the exact-seven-adhesion outcome.

## 2. The exact root exchange

### Lemma 2.1 (two-left-bag root exchange)

Suppose

\[
                         K=E\mathbin{\dot\cup}T              \tag{2.1}
\]

is a partition into connected adjacent sets such that

\[
 e_6\in E,\qquad E\sim S,\qquad T\sim P,\qquad T\sim D.      \tag{2.2}
\]

Then

\[
 \widehat L_6=P\cup T\cup D,\qquad
 \widehat L_0=S\cup E,\qquad
 \widehat R_5=R_5,\qquad \widehat R_0=R_0                  \tag{2.3}
\]

is a spanning balanced \(K_4\)-model.  The two left exterior roots
have exchanged roles: \(r_0\in\widehat L_6\), while
\(e_6\in\widehat L_0\).  The outer vertices remain
\(6\in\widehat L_6\) and \(5\in\widehat R_5\).

#### Proof

The first new left bag is connected through the \(P\)-\(T\) and
\(T\)-\(D\) edges; the second is connected through the \(S\)-\(E\)
edge.  They are adjacent through the old \(P\)-\(S\) edge (also
through \(E\)-\(T\)).  The first new bag retains both right-bag
contacts through \(D\), and the second retains them through \(S\).
The right bags and their mutual adjacency are unchanged.

All four roots remain, the two left roots are merely interchanged,
and both are still literal-left roots, complete to \(\{1,2\}\).
Equation (2.3) repartitions the same vertex set and preserves
spanning. \(\square\)

Within the ordered-prefix residue, (2.2) is the weakest direct
connected split for the displayed formulas: \(P\) has no \(D\)-edge,
so the \(P\)-side must reach \(D\) through \(T\), while the root side
\(E\) must connect to \(S\).

## 3. One additional contact gives \(K_7\)

### Lemma 3.1 (root-side \(P\)-contact closure)

Under Lemma 2.1, if \(E\sim P\), then \(G\) contains a
\(K_7\)-minor.

#### Proof

Use

\[
 \{h\},\quad\{1\},\quad\{2\},\quad P,\quad E,\quad
 \{v\}\cup S\cup R_5,\quad T\cup D\cup R_0.                 \tag{3.1}
\]

The sixth set is connected through \(S\)-\(R_5\) and \(v5\).
The last is connected through \(TD\) and \(D\)-\(R_0\).
Among the four nonsingleton sets use

\[
 PE,\quad PS,\quad PT,\quad ES,\quad ET,\quad v6
\]

for their six pairwise adjacencies.  Their contacts to \(h,1,2\)
come, respectively, from the roots in \(P,E,R_5,R_0\), from \(v\),
and from \(6\in D\). \(\square\)

Consequently, in a \(K_7\)-minor-free graph every valid exchange
partition satisfies

\[
                         E\not\sim P,\qquad A\subseteq T.     \tag{3.2}
\]

Thus all four or more prefix portals are owned by the non-root side
\(T\).

## 4. Linkage formulation

Put

\[
 B=N_K(S),\qquad C=N_K(D).                                  \tag{4.1}
\]

Both are nonempty.  A particularly useful sufficient condition for
Lemma 2.1 is a pair of disjoint connected subgraphs:

* one contains \(e_6\) and a vertex of \(B\);
* the other contains a vertex of \(A\) and a vertex of \(C\).

Indeed, two disjoint paths with those terminal requirements extend to
a connected bipartition \(K=E\dot\cup T\): contract the two paths,
take a spanning tree, and delete one edge on the path between the two
contracted vertices.  The resulting sides satisfy (2.2).

Equivalently, fix any connected core \(R\subseteq K\) containing
\(e_6\) and a vertex of \(B\).  If a component of \(K-R\) contains
both an \(A\)-vertex and a \(C\)-vertex, the protected-core peel lemma
produces (2.1)--(2.2), with \(R\subseteq E\).

Hence failure of every root exchange is an honest rooted Two Paths
obstruction inside \(K\): no root-to-\(S\) connector is disjoint from
an \(A\)-to-\(D\) connector.

## 5. A well-founded potential and the exact ownership lock

Permit the two literal-left exterior roots \(e_6,r_0\) to be
interchanged, while fixing the two right roots and requiring \(6,5\)
to remain in their indicated outer bags.  Among all such spanning
balanced models choose one minimizing

\[
 \Phi=|\text{left bag not containing }6|+|R_0|.             \tag{5.1}
\]

This is a nonempty finite family, and Lemma 2.1 stays inside it.  The
conclusion below is conditional on this global minimizer lying in the
same-bag ordered-prefix cell.  The root-free lobe exchanges used to
derive the ordered spine remain valid in this enlarged family, so the
earlier spine proof applies verbatim to such a minimizer.  If instead
the minimizer lies in another attachment cell, this argument records a
model transition rather than asserting the ordered conclusion there.

For a minimizing model in the ordered-prefix cell and its exchanged
model,

\[
 \Phi_{\rm old}=|P|+|S|+|R_0|,\qquad
 \Phi_{\rm new}=|E|+|S|+|R_0|.                             \tag{5.2}
\]

Therefore global minimality gives

\[
                              |E|\ge |P|                    \tag{5.3}
\]

for every valid root-exchange split.  Combining (3.2) and (5.3)
gives the exact minimum-model obstruction:

\[
\boxed{
\begin{array}{l}
e_6\in E,\ E\sim S,\ E\not\sim P,\ |E|\ge|P|,\\
T\sim P,D,\quad N_K(P)=A\subseteq T,\quad |A|\ge4 .
\end{array}}                                                \tag{5.4}
\]

If no valid exchange split exists, the alternative obstruction is the
rooted two-linkage failure in Section 4.  Thus, after the earlier
\(K_7\) and exact-cut outcomes have been removed, the new residue is
precisely a **root-ownership bottleneck in \(K\)**:

1. either the root-to-\(S\) and \(P\)-to-\(D\) connectors cannot be
   made disjoint; or
2. they split \(K\), but the root side owns no \(P\)-portal and is at
   least as large as the old root prefix.

The potential is well-founded, but it does not by itself rule out
(5.4); it proves the ownership and size orientation without claiming
a false descent.

## 6. Sharpness

The minimal contact quotient for (2.1)--(2.2), with no \(E\)-\(P\)
edge, is \(K_7\)-minor-free.  The verifier
degree9_two_left_root_exchange_probe.py returns false.  A width-five
elimination order is

\[
 3,4,P,E,T,1,2,v,h,S,D,R_5,R_0.                            \tag{6.1}
\]

Adding the single edge \(EP\) makes the verifier return true and gives
exactly the model (3.1).

Arbitrarily many distinct members of \(A=N_K(P)\) may be realized
without increasing treewidth: add vertices \(x_j\) adjacent to the
clique edge \(PT\), assign them to the \(T\)-bag, and retain the edge
to the \(T\)-core for connectivity.  The inequality \(|E|\ge|P|\)
may likewise be forced by enlarging \(E\) internally.  Hence neither
portal multiplicity nor the size orientation eliminates (5.4).

The next valid mechanism must use the internal rooted two-linkage
obstruction, the symmetric right-hand ownership lock, or a
contraction-critical boundary-state transition.
