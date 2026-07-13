# The transferred degree-nine gate: split, bounce, and the root-absorbed lock

## 1. Setting

Continue the same-bag alternative of
hadwiger_degree9_protected_portal_peel.md.  Outside an exact
seven-adhesion, Theorem 4.7 there gives a connected set \(W\), a
connected residual \(L\subseteq L_0\) containing the bottleneck \(q\),
and

\[
 N(W)=\{h,1,2,6,q\}\mathbin{\dot\cup}A,\qquad
 A\subseteq D-\{6\},\qquad |A|\ge3,                         \tag{1.1}
\]

where \(D=L_6-K\) is connected and contains \(6\).  Every member of
\(A\) is a genuine \(W\)-portal in \(D\).  The residual \(L\) is
connected, is adjacent to \(W,R_5,R_0\), and contains all old
\(L_0\)-portals to \(R_5,R_0\).

There are two genuinely different states.

* **Root retained:** the exterior root of \(L_0\), and hence literal
  contacts to \(h,1,2\), lies in \(L\).
* **Root absorbed:** that root already lies in \(W\); \(L\) has no
  forced literal contact.

This distinction is essential.

## 2. The root-retained split closes

### Theorem 2.1 (transferred-gate split)

Assume the \(L_0\)-root lies in \(L\).  Suppose

\[
                         D=X\mathbin{\dot\cup}Y               \tag{2.1}
\]

is a partition into connected adjacent sets such that

\[
 6\in Y,\qquad X\sim W,\qquad Y\sim W,                       \tag{2.2}
\]

and \(X\) is adjacent to at least one of \(R_5,R_0\).  Then \(G\)
contains a \(K_7\)-minor.

#### Proof

If \(X\sim R_0\), use

\[
 \{h\},\quad\{1\},\quad\{2\},\quad W,\quad L,\quad
 Y\cup R_5,\quad \{v,3\}\cup X\cup R_0.                     \tag{2.3}
\]

The sixth set is connected through \(65\).  The last is connected
through the \(X\)-\(R_0\) edge, the right-root--\(3\) edge, and \(3v\).
The four nonsingleton sets form a clique: use

\[
 WL,\ WY,\ WX,\ LR_5,\ LR_0,\ v5 .
\]

Each sees \(h,1,2\): use the roots in \(W,L,R_5,R_0\), the vertex
\(6\in Y\), and \(v\) in the last set.

It remains that \(X\sim R_5\) but \(X\not\sim R_0\).  The old
\(L_6\)-\(R_0\) adjacency cannot use \(K\), which misses \(R_0\), and
must therefore have its \(D\)-endpoint in \(Y\).  Use

\[
 \{h\},\quad\{1\},\quad\{2\},\quad W,\quad L,\quad
 Y\cup R_0,\quad \{v\}\cup X\cup R_5.                       \tag{2.4}
\]

Connectivity uses the \(Y\)-\(R_0\), \(X\)-\(R_5\), and \(v5\) edges.
Among the four nonsingleton sets, use

\[
 WL,\ WY,\ WX,\ LR_0,\ LR_5,\ v6
\]

for the six adjacencies.  Their contacts to \(h,1,2\) are as above.
Thus (2.3) or (2.4) is a \(K_7\)-model. \(\square\)

### Corollary 2.2 (flexible linkage closes)

Put

\[
 C=N_D(R_5\cup R_0)-\{6\}.                                  \tag{2.5}
\]

Assume \(C\ne\varnothing\).  If \(D\) contains two vertex-disjoint
paths, one from \(A\) to \(C\) and one from a different member of
\(A\) to \(6\), then \(G\) has a \(K_7\)-minor.

#### Proof

Extend the two disjoint paths to a connected bipartition of \(D\) by
Lemma 4.1 of the preceding note.  The side containing the first path
is \(X\), the side containing \(6\) is \(Y\).  Both meet \(A\), so both
are adjacent to \(W\); \(X\) has a non-\(6\) right exit.  Apply
Theorem 2.1. \(\square\)

## 3. Failure of the linkage: a precise bounce state

Apply the flexible-start gammoid lemma to source set \(A\) and target
sets \(C,\{6\}\).  If Corollary 2.2 does not apply, there is a vertex
\(p\in D\) meeting every \(A\)-to-\((C\cup\{6\})\) path.

Let \(\mathcal D\) be the components of \(D-p\) meeting \(A-\{p\}\),
and put

\[
                         W'=W\cup\bigcup_{U\in\mathcal D}U.    \tag{3.1}
\]

### Lemma 3.1 (cross-half lobe closure)

If a member \(U\in\mathcal D\) is adjacent to \(3\) or \(4\), then
\(G\) has a \(K_7\)-minor.

#### Proof

Suppose \(U\sim3\), and put \(Y=D-U\).  The set \(Y\) is connected:
it consists of \(p\), the component of \(D-p\) containing \(6\), and
all other components of \(D-p\).  Use

\[
 \{v\},\quad\{h\},\quad\{1\},\quad\{2\},\quad
 Y\cup R_5,\quad \{3\}\cup W\cup U,\quad
 \{4\}\cup L\cup R_0.                                      \tag{3.2}
\]

Connectivity uses \(65\), a \(W\)-\(U\) portal and the \(U\)-\(3\)
edge, and an \(L\)-\(R_0\) edge followed by the right-root--\(4\)
edge.  The last three sets meet through \(WY\), an \(L\)-\(R_5\)
edge, and \(34\).  Their contacts to \(v,h,1,2\) come from the
displayed outer vertices and the roots in \(R_5,W,L,R_0\).
Interchanging \(3,4\) proves the other case. \(\square\)

### Theorem 3.2 (six-fixed-boundary bounce)

Assume there is no \(K_7\)-minor.  Put

\[
 P_L=N(W')\cap(L-\{q\}),\qquad
 F=\{h,1,2,6,q,p\}.                                        \tag{3.3}
\]

Then

\[
                         N(W')=F\mathbin{\dot\cup}P_L,        \tag{3.4}
\]

where \(p=6\) is understood only once in the set \(F\).  Consequently:

* if \(p\ne6\), then \(|P_L|\ge1\); equality is an exact seven-cut,
  and the non-adhesion residue has \(|P_L|\ge2\);
* if \(p=6\), then \(|P_L|\ge2\); equality is an exact seven-cut,
  and the non-adhesion residue has \(|P_L|\ge3\).

#### Proof

The set \(W'\) is connected because every component in \(\mathcal D\)
contains a \(W\)-portal.  The bottleneck property of \(p\) says that
these components contain neither \(6\) nor a member of \(C\); hence
they have no right-bag neighbour.  Lemma 3.1 excludes neighbours in
\(\{3,4\}\).  Within \(D\), they can leave only through \(p\).
The original set \(W\) contributes exactly the fixed neighbours
\(h,1,2,6,q\), while every remaining contact into the residual
\(L-\{q\}\) is recorded in \(P_L\).  The spanning four-bag model
exhausts all other vertices, proving (3.4).

The set in (3.4) is a genuine separator from \(v\) and the right bags.
Seven-connectivity gives the displayed lower bounds.  Equality makes
the neighbourhood an exact seven-cut; otherwise integrality increases
the portal bound by one. \(\square\)

The fixed-boundary size therefore does **not** remain five under a
generic transfer.  A new bottleneck \(p\ne6\) enlarges it to six, and
the portal surplus drops from three to two.  Thus a monotone-transfer
termination proof cannot simply repeat Theorem 4.7 unchanged.

## 4. Root absorbed: a sharp contact-level falsifier

If the \(L_0\)-root lies in \(W\), Theorem 2.1 is false even with every
possible quotient contact present.

Take twelve vertices

\[
 v,h,1,2,3,4,W,L,X,Y,R_5,R_0,
\]

where \(6\in Y\).  Give \(W,Y\) the left contacts to \(1,2\), give
\(R_5,R_0\) the right contacts to \(3,4\), and retain all Moser
boundary edges.  Add

\[
\begin{gathered}
 WL,WX,WY,XY,\quad YR_5,\quad
 LR_5,LR_0,R_5R_0,\\
 XR_5,XR_0,YR_0 .
\end{gathered}                                               \tag{4.1}
\]

Thus both \(X,Y\) are \(W\)-adjacent, \(X\) has both non-\(6\) right
exits, and the split has the maximum conservative contact set.  Yet the
graph has treewidth at most five.  One elimination order, with at most
five later neighbours after fill, is

\[
 1,2,3,4,L,X,Y,R_0,R_5,W,h,v.                               \tag{4.2}
\]

The later-neighbour sets have respective orders

\[
 5,4,5,4,3,4,5,4,3,2,1,0.
\]

Hence this quotient has no \(K_7\)-minor.  The exact verifier
degree9_transferred_D_split_probe.py checks all contact allocations
and both choices of the side containing \(6\).

This is the minimal structural warning: after the \(L_0\)-root is
absorbed, splitting \(D\) and preserving all quotient contacts does not
recreate the missing left-type branch set.  Any closure of this state
must either split \(W\) to release that root, use the symmetric
\(R_5-5\) transfer, or invoke a contraction-critical boundary-state
transition.  Portal incidence alone cannot finish it.

## 5. Exact outcome

The transferred-gate proposal succeeds completely in the root-retained
state:

\[
 \text{flexible linkage}\Rightarrow K_7,\qquad
 \text{no linkage}\Rightarrow
 \text{exact seven-cut or a six-fixed-boundary bounce}.      \tag{5.1}
\]

It is sharply false in the root-absorbed state.  The remaining
two-sided obstruction is therefore not an arbitrary interleaving:
it is a root-ownership lock.  One side has absorbed the only spare
literal-edge root, and the opposite transferred gate must either release
that root or provide the missing branch through the symmetric bypass.

**Subsequent status.**  The exact-seven and six-fixed-boundary outcomes
in (5.1) are correct descriptions of one exchange step, but they are no
longer terminal alternatives.  Theorem 5.1 of
`hadwiger_degree9_two_carrier_capacity_exchange.md` alternates the active
carrier and continues through both equalities.  Only the root-ownership
lock in the preceding paragraph survives.
