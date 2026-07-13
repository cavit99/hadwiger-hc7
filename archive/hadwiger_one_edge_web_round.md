# The one-edge forest cell: cover reduction and the two-paths web

This note sharpens the one-edge subcase of the degree-seven residual.  It
does not eliminate the final web obstruction.

## 1. Setup

Let \(G\) be a hypothetical proper-minor-minimal counterexample to
\(\mathrm{HC}_7\), let \(d_G(v)=7\), put \(H=G-v\),
\(N=N_G(v)\), and suppose an accessible six-colouring has repeated pair
\(x,y\) and unique roots
\[
 U=\{r,s,t_1,t_2,t_3\}.
\]
Assume
\[
 \overline{H[U]}=\{rs\}.                              \tag{1.1}
\]
Write \(Q=\overline{G[N]}\).  Then \(Q\) is triangle-free,
\(xy,rs\in E(Q)\), and every other edge of \(Q\) is incident with
\(x\) or \(y\).  No vertex of \(U\) is adjacent in \(Q\) to both
\(x\) and \(y\).

The sole exterior component is denoted by \(C=G-N[v]\) whenever this
one-component cell is under discussion.  It is connected and
\(N_G(C)=N\).

## 2. A neighbourhood-complement cover which closes immediately

### Lemma 2.1 (two-vertex-cover certificate)

Suppose \(G-N[v]\) has one component and the vertex-cover number of
\(Q\) satisfies \(\tau(Q)\le2\).  Then \(G\) has a \(K_7\)-minor.

#### Proof

Extend a vertex cover of \(Q\), if necessary, to a two-set
\(X\subseteq N\).  Since \(X\) covers every edge of \(Q\), the five
vertices of \(N-X\) form a clique in \(G\).  The set
\[
 D=C\cup X
\]
is connected: \(C\) is connected and each vertex of \(X\) has a
neighbour in \(C\).  It is adjacent to every singleton vertex of
\(N-X\), again because \(N_G(C)=N\).  Thus \(D\), together with the
five singleton bags on \(N-X\), is an \(N\)-meeting \(K_6\)-model in
\(H\).  Add \(\{v\}\). \(\square\)

In the one-edge setting (1.1), define
\[
 A_x=\{u\in U:xu\in E(Q)\},\qquad
 A_y=\{u\in U:yu\in E(Q)\}.
\]
The sets \(A_x,A_y\) are disjoint.  Each contains at most one of
\(r,s\), since \(rs\in E(Q)\) and \(Q\) is triangle-free.

### Corollary 2.2 (forced extra leaves at both centres)

In a surviving one-component cell, each of \(A_x,A_y\) contains at
least one of \(t_1,t_2,t_3\).  In particular there are distinct indices
\(i,j\) such that
\[
 xt_i,yt_j\in E(Q).                                  \tag{2.1}
\]

#### Proof

If \(A_x\) contains no \(t_i\), then it is empty or is contained in
one of \(\{r\},\{s\}\).  In the first two cases respectively,
\(\{y,r\}\) or \(\{y,s\}\) covers every edge of \(Q\): the vertex
\(y\) covers \(xy\) and all edges incident with \(y\), the chosen
endpoint covers \(rs\), and it covers the only possible remaining edge
at \(x\).  (If \(A_x\) is empty, either endpoint may be chosen.)
Lemma 2.1 gives a contradiction.  The same argument with \(x,y\)
interchanged treats \(A_y\).  Finally, the two nominated \(t\)-vertices
are distinct because \(A_x\cap A_y=\varnothing\). \(\square\)

Thus the first genuinely locked one-edge neighbourhood has
\(\tau(Q)=3\), with a double-star edge at \(xy\), the disjoint edge
\(rs\), and at least one \(t\)-leaf at each centre.

## 3. Ordinary two-pair linkage is enough

Put
\[
 L=H-\{t_1,t_2,t_3\}.
\]
Since \(H\) is six-connected, \(L\) is three-connected.

### Lemma 3.1 (linkage certificate)

If \(L\) has vertex-disjoint paths with ends \(x,y\) and \(r,s\),
respectively, then \(G\) has a \(K_7\)-minor.

#### Proof

Let \(P\) be the \(x\)-\(y\) path and \(R\) the \(r\)-\(s\) path.
Split \(R\) at an edge into two adjacent connected bags \(R_r,R_s\)
containing \(r,s\), respectively.  Use \(V(P)\) as a third bag.  It
is adjacent to \(R_r\) and \(R_s\): for each of \(r,s\), at least one
of its edges to \(x,y\) is present, since otherwise that root together
with the nonadjacent pair \(x,y\) would be an independent triple in
\(G[N]\).

The three singleton bags on \(t_1,t_2,t_3\) form a clique.  By (1.1)
each is adjacent to \(r,s\), hence to \(R_r,R_s\), and the same
independence-number argument makes it adjacent to \(V(P)\).  These are
six pairwise adjacent bags meeting \(N\); add \(\{v\}\). \(\square\)

This lemma is strictly weaker than the disproved colour-preserving
removable-path target: the \(r\)-\(s\) path may use arbitrary colours.

## 4. Exact web alternative

Apply the Robertson--Seymour--Thomas two-disjoint-paths theorem to the
ordered terminals
\[
 x,r,y,s.                                             \tag{4.1}
\]
If its linkage outcome holds, Lemma 3.1 closes the cell.  Therefore a
surviving graph \(L\) has one of the following two forms:

1. there is a separation \((A,B)\) of \(L\), of order exactly three,
   with \(x,r,y,s\in A\) and \(|B-A|\ge2\); or
2. \(L\) has a drawing in a disk with \(x,r,y,s\) on the boundary in
   that cyclic order.

Orders below three in the first outcome are excluded by
three-connectivity.  Repeatedly replacing a terminal-free side of a
three-separation by a rooted triangle minor reduces the obstruction to a
three-sum of pieces whose terminal-bearing core is internally
four-connected; at that core the only remaining theorem outcome is the
disk drawing.  This is the standard **two-paths web** obstruction.  The
replacement is legitimate only at the level of the rooted four-terminal
linkage problem: it is not, by itself, a branch-set construction for
\(K_7\).

## 5. The global criticality input still unused

For every edge \(ab\in E(G)\), a six-colouring of \(G-ab\) assigns
\(a,b\) the same colour.  If \(ab\) is neither incident with \(v\) nor
an edge with both ends in \(N\), then \(v\) is still adjacent to all
seven vertices of \(N\), and the deletion has not changed \(G[N]\).
The colour of \(v\) is therefore absent from \(N\), and the equality
classes on \(N\) form a matching of order at least two in \(Q\).  (For
an edge inside \(G[N]\), its two ends may form one additional equality
pair which is not an edge of \(Q\), so that case must not be folded into
this assertion.)  These edge-deletion colourings give global boundary
states unavailable in the local counterexample to colour-preserving
removal.

The exact remaining target in the one-edge cell is therefore:

> **Edge-critical web elimination.**  Show that the two-paths web in
> Section 4 is incompatible with the double boundary states supplied by
> the colourings of \(G-ab\) for edges in its terminal-bearing core,
> unless an \(N\)-meeting \(K_6\)-model already exists.

Merely invoking planarity of the terminal core is not enough: the three
deleted roots can have arbitrary neighbours in \(L\), so an ordinary
four-colouring of the disk does not automatically extend to a
six-colouring of \(G\).

## References

* N. Robertson, P. Seymour and R. Thomas, *Hadwiger's conjecture for
  \(K_6\)-free graphs*, Combinatorica 13 (1993), especially the
  two-disjoint-paths alternative quoted as Theorem 13 by Norin--Totschnig.
* S. Norin and A. Totschnig, *Every graph with no
  \(K_7^{\vee}\)-minor is 6-colorable*, arXiv:2507.03244, Theorem 13.
