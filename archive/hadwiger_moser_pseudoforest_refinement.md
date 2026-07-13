# Pseudoforest refinement of the degree-seven Moser residual

This note sharpens, but does not eliminate, the two-component degree-seven
cell.  It uses the notation and standing hypotheses of
`hadwiger_degree7_kempe.md`.

## 1. Accessible repeated pairs contain a matching

Let \(N=N_G(v)\), where \(d(v)=7\), and let \(R\) be the graph on \(N\)
whose edges are the pairs that receive the repeated colour in at least one
proper six-colouring of \(G-v\).  Then
\[
  R\subseteq \overline{G[N]}\qquad\text{and}\qquad \nu(R)\ge2.       \tag{1}
\]

Indeed, for every \(w\in N\), a six-colouring of \(G/vw\) expands to a
colouring of \(G-v\) in which \(w\) is unique in one colour.  The other six
vertices of \(N\) use five colours, so their repeated pair is an edge of
\(R\) avoiding \(w\).  Thus no vertex meets every edge of \(R\).  Since
\(R\) is triangle-free, an intersecting family of its edges is a star;
hence \(\nu(R)\ge2\).

## 2. The pure Moser spindle

Label the Moser spindle \(M\) by
\[
 V(M)=\{a,b,c,d,e,p,q\}
\]
and
\[
 E(M)=\{ab,ac,bc,bp,cp,ad,ae,de,dq,eq,pq\}.
\]
Its complement has edge set
\[
 \{ap,aq,bd,be,bq,cd,ce,cq,dp,ep\}.                       \tag{2}
\]

If the repeated pair is \(xy\), the missing-edge graph on the five unique
roots is
\[
 F=\overline M-\{x,y\}.
\]
Direct inspection of (2) gives:

- for \(xy\in\{ap,aq\}\), \(F\cong K_{2,3}\);
- for \(xy\in\{bd,be,cd,ce\}\), \(F\cong C_5\);
- for \(xy\in\{bq,cq,dp,ep\}\), \(F\) is connected with degree sequence
  \((3,2,2,2,1)\) and exactly one cycle.

The two exceptional edges \(ap,aq\) meet at \(a\).  By (1), they cannot be
all the accessible repeated pairs.  Therefore some six-colouring has a
repeated pair for which \(F\) is a connected unicyclic graph.

## 3. The one-cross-edge extension

All one-cross-edge extensions are isomorphic; take \(M+bd\).  Its
complement is obtained from (2) by deleting \(bd\).  Inspecting its nine
possible repeated edges shows that deleting the ends of any one leaves a
connected graph on five vertices with at most five edges.  Thus every
accessible repeated pair gives a tree or a connected unicyclic graph.

Consequently, in both two-component residual neighbourhoods one may choose
a six-colouring for which the five-root missing-edge graph \(F\) is a
connected pseudoforest.  The rooted \(K_5\) certificate may therefore be
obtained from the more structured Kriesell--Mohr unicyclic theorem
(Theorem 5), rather than the full five-vertex six-edge theorem.

## 4. Remaining issue

The pseudoforest certificate is topologically a cycle with attached trees,
but its bags may still use vertices of both components of \(G-N[v]\).  The
refinement does not by itself leave a component available for the sixth bag.
The next precise target is:

> Given the accessible pseudoforest colouring above, choose its rooted
> property-\((*)\) certificate so that one exterior component is avoided,
> or so that the repeated pair remains connected after deleting the five
> bags.

Any proof must use contraction-critical colouring information: internal
connectivity of a boundaried component alone is insufficient (a single
universal helper already gives an internally seven-connected pair after
completing the boundary, but need not root the required \(K_5\)).

