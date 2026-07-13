# Two-anchor elimination of the one-cross-edge Moser cell

## 1. Scope and standing hypotheses

This note proves one local reduction in the degree-seven analysis of a
proper-minor-minimal counterexample to \(\mathrm{HC}_7\).  It does not prove
\(\mathrm{HC}_7\).

Let \(G\) be a graph such that

* \(\chi(G)=7\);
* every proper minor of \(G\) is six-colourable; and
* \(G\) is seven-connected.

Fix a vertex \(v\) of degree seven and put
\[
 N=N_G(v).
\]
Assume that
\[
 G-N[v]=C_1\mathbin{\dot\cup}C_2
\]
has exactly two components.  Each component has the whole of \(N\) as its
neighbourhood:
\[
 N_G(C_i)=N\qquad (i=1,2). \tag{1.1}
\]
Indeed, \(N_G(C_i)\subseteq N\), and if a vertex of \(N\) were missing then
\(|N_G(C_i)|\leq6\); deleting this set would separate the nonempty component
\(C_i\) from \(v\), contrary to seven-connectivity.

Write
\[
 L_i=G[N\cup C_i].
\]
The boundary-state families for these two boundaried graphs are developed
in `hadwiger_two_component_boundary_strengthening.md`.  The argument below
can be read as a direct way of forcing the same two-pair boundary state on
both sides.

## 2. The two-anchor contraction lemma

### Lemma 2.1

Let \(ab\) and \(cd\) be vertex-disjoint nonedges of \(G[N]\), and set
\[
 R=N-\{a,b,c,d\}.
\]
For each \(i\in\{1,2\}\), the graph \(L_i\) has a proper six-colouring
\(\varphi_i\) satisfying
\[
 \varphi_i(a)=\varphi_i(b),\qquad
 \varphi_i(c)=\varphi_i(d),\qquad
 \varphi_i(a)\ne\varphi_i(c), \tag{2.1}
\]
and every vertex of \(R\) avoids both colours in (2.1).

If \(G[R]\cong K_3\), then the equality partition induced on \(N\) is
exactly
\[
 ab\mid cd\mid r_1\mid r_2\mid r_3, \tag{2.2}
\]
where \(R=\{r_1,r_2,r_3\}\).  In particular, exactly five colours occur on
\(N\).

#### Proof

Fix \(i\), and let \(j\ne i\).  In \(G\), contract each of the following
two vertex-disjoint connected sets to one vertex:
\[
 A=\{v,a,b\},\qquad B=C_j\cup\{c,d\}. \tag{2.3}
\]
The set \(A\) is connected through \(v\).  The set \(B\) is connected
because \(C_j\) is connected and, by (1.1), each of \(c,d\) has a neighbour
in \(C_j\).  Denote the two contracted vertices by \(z\) and \(w\),
respectively, and denote the resulting minor by \(J_i\).

The minor \(J_i\) is proper: contracting \(A\) alone reduces the number of
vertices by two, and the second contraction reduces it further.  It
therefore has a proper six-colouring \(\psi_i\).

The vertices \(z,w\) are adjacent in \(J_i\), since the original edge
\(vc\) (and also \(vd\)) runs between the two contracted sets.  Moreover,
for every \(u\in R\),

* \(uz\in E(J_i)\), through the original edge \(uv\); and
* \(uw\in E(J_i)\), because (1.1) gives an edge from \(u\) to \(C_j\).

Consequently \(\psi_i(z)\ne\psi_i(w)\), and every vertex of \(R\) avoids
both of these colours.

Obtain a colouring of \(L_i\) by retaining \(\psi_i\) on
\(C_i\cup R\), assigning \(\psi_i(z)\) to both \(a,b\), and assigning
\(\psi_i(w)\) to both \(c,d\).  This expansion is proper.  Within the two
expanded pairs there is no edge, since \(ab,cd\notin E(G[N])\).  Every edge
from one of the four expanded vertices to a retained vertex, and every edge
between the two pairs, was represented in \(J_i\) by the corresponding edge
incident with \(z\) or \(w\).  Thus (2.1) holds and all vertices of \(R\)
avoid the two pair colours.

If \(G[R]\cong K_3\), its three vertices receive pairwise distinct colours.
Those colours are also distinct from the two pair colours, so (2.2) follows.
\(\square\)

## 3. The gluing contradiction

### Corollary 3.1

Under the standing hypotheses, there do not exist two vertex-disjoint
nonedges \(ab,cd\) of \(G[N]\) for which
\[
 G[N-\{a,b,c,d\}]\cong K_3. \tag{3.1}
\]

#### Proof

Apply Lemma 2.1 on both sides.  Each colouring induces the same five-block
partition (2.2) on \(N\).  Permute the six colour names in the colouring of
\(L_2\) so that its colour on each of the five boundary blocks agrees with
the corresponding colour in \(L_1\).  This is possible because the five
blocks have five distinct colours; the bijection between the five used
boundary colours extends to a permutation of all six colours.

The two side colourings now agree on \(N\).  They glue to a proper
six-colouring of
\[
 G-v=L_1\cup_N L_2,
\]
because there are no edges between \(C_1\) and \(C_2\).  Exactly one of the
six colours is absent from \(N\).  Assign that colour to \(v\).  This is
proper because every neighbour of \(v\) lies in \(N\), and it gives a
six-colouring of \(G\), contrary to \(\chi(G)=7\). \(\square\)

In the notation of the boundary-state framework, (2.2) says that the
two-edge matching \(\{ab,cd\}\) lies in both extension families
\(\mathcal E_1\) and \(\mathcal E_2\).  Corollary 3.1 is therefore also the
direct colouring-gluing proof of the resulting forbidden intersection.

## 4. The one-cross-edge Moser extension

Use the following numerical labelling of the Moser spindle \(M\):
\[
 E(M)=
 \{01,02,03,04,12,16,26,34,35,45,56\}. \tag{4.1}
\]
The one-cross-edge extension that occurs in the existing seven-vertex
classification is represented by
\[
 M+13. \tag{4.2}
\]
In this graph,

* \(25\) is a nonedge;
* \(46\) is a nonedge;
* these two nonedges are vertex-disjoint; and
* the remaining vertices \(\{0,1,3\}\) induce a triangle, since
  \(01,03\in E(M)\) and \(13\) is the added edge.

Taking \(ab=25\) and \(cd=46\) in Corollary 3.1 excludes
\[
 G[N]\cong M+13 \tag{4.3}
\]
in the two-exterior-component case.

The alphabetical labelling used elsewhere in the workspace is recovered by
\[
 (a,b,c,d,e,p,q)=(0,1,2,3,4,6,5).
\]
Thus the graph denoted there by \(M+bd\) is exactly the graph \(M+13\) in
(4.2).

## 5. Exact consequence and limitation

An existing seven-vertex neighbourhood classification, combined with the
earlier small-support \(K_4\)-model elimination, reduces the
two-exterior-component degree-seven cell to the following two exact
isomorphism types:
\[
 G[N]\cong M
 \quad\hbox{or}\quad
 G[N]\cong M+13.
\]
Subject to that classification input, (4.3) leaves only the **pure Moser
spindle** as the two-component degree-seven residual.

This conclusion is deliberately narrow.  It does not assert that every
arbitrary graph obtained by adding one missing edge to \(M\) is isomorphic
to \(M+13\), and it does not close the pure-Moser cell, the degree-seven
case, or \(\mathrm{HC}_7\).
