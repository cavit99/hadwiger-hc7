# The all-crossless sole-exterior Moser cell is six-colourable

## 1. Setting

Let \(G\) be seven-connected, let \(v\) have degree seven, and suppose

\[
 N_G(v)=U\mathbin{\dot\cup}\{a,b\},\qquad |U|=5,
\]

where \(ab\notin E(G)\), \(G[U]\cong C_5\), and
\(G-N[v]=C\) is one connected component.  In the pure-Moser labelling
one may take \(a=1,b=3\), and the missing edges on
\(U=\{0,2,4,5,6\}\) form the complementary five-cycle.

Index \(U=\{u_0,\ldots,u_4\}\) so that the five missing edges are
\(u_i u_{i+1}\), with indices modulo five.  A **frame cross** in \(C\)
is a pair of vertex-disjoint portal paths for two vertex-disjoint missing
edges of this cycle.

### Theorem 1.1

If all five frames are crossless in \(C\), then \(G\) is six-colourable.
Consequently this configuration cannot occur in a minimal counterexample
to \(HC_7\).

## 2. One simultaneous pentagonal web

Form an auxiliary graph \(A_C\) from \(G[C]\) by adjoining five
independent terminals \(t_i\), where

\[
                 N_{A_C}(t_i)=N_C(u_i).
\tag{2.1}
\]

Put the terminals in the cyclic order in which the **present** cycle
\(G[U]\) occurs.  Equivalently, this is the pentagram order relative to
the missing cycle.  For every four terminals, the alternating pairing in
this order is exactly one pair of vertex-disjoint missing-cycle edges.
Thus

\[
 A_C\text{ has a tuple cross}
 \quad\Longleftrightarrow\quad
 \text{one of the five missing-edge frames is crossed in }C.
\tag{2.2}
\]

Under the hypothesis, apply the same-vertex generalized Two Paths
Theorem to the crossless five-terminal tuple.  It gives an edge-only
completion on the same vertex set to a five-web: a plane rib with the
five terminals on its outer frame, together with cliques inserted behind
facial triangles.

No inserted clique contains an original vertex of \(C\).  If \(X\) were
the nonempty set of original vertices in such an insertion, all its
represented neighbours would lie among at most three facial vertices.
The only original boundary labels omitted from \(A_C\) are \(a,b\).
Replacing artificial terminals among the three attachments by their
actual roots therefore gives

\[
                         |N_G(X)|\le3+2=5.
\tag{2.3}
\]

The vertex \(v\) lies on the far side, so (2.3) contradicts
seven-connectivity.  Hence every original vertex and edge of \(A_C\)
lies in the plane rib.

Delete every completion edge except the five frame edges and the
original edges of \(A_C\).  Replace \(t_i\) by \(u_i\), retaining every
portal edge.  The five frame edges are exactly the five present edges
of \(G[U]\), because the terminal order was chosen as its cycle order.
We obtain a plane disk embedding of

\[
                         G[C\cup U],               \tag{2.4}
\]

with \(G[U]\) as its boundary cycle.

## 3. Colouring

By the Four Colour Theorem, colour (2.4) with colours \(1,2,3,4\).
Give both \(a,b\) colour \(5\), and give \(v\) colour \(6\).

This is proper.  The pair \(a,b\) is independent; neither is in
\(C\cup U\), so every edge from either vertex into the four-coloured
graph has different endpoint colours.  The vertex \(v\) has no
neighbour in \(C\),
and all seven of its neighbours use colours \(1,\ldots,5\).  Thus the
displayed assignment is a six-colouring of \(G\), proving Theorem 1.1.

## 4. Structural consequence

Every surviving sole-exterior pure-Moser configuration contains a crossed
frame: for some two disjoint missing-cycle edges, \(C\) contains the two
corresponding disjoint portal paths.  This removes the entire planar
pentagonal-web family of arbitrary order.  The remaining task is to turn
one such cross, together with the full \(a,b\)-portals and the other three
root classes, into either

* a nonseparating rooted \(K_5\), or
* an exact two-shore adhesion.

No enumeration by \(|C|\) is involved.
