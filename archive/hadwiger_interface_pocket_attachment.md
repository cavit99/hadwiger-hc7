# Interface pockets have forced attachment surplus

## 1. Boundaried two-piece setting

Let (G) be (k)-connected.  Let (S=C\dot\cup Z) be a boundary and let
(D,D') be anticomplete nonempty shores, where (D') is connected and

\[
 D=E\dot\cup F
\]

is a partition into nonempty connected adjacent pieces.  Assume every
neighbour of (D) outside (D\cup D'\) belongs to (S), and (D') has no
edge to (D).

Put

\[
 Z_E=\{z\in Z:N_E(z)\ne\varnothing\};
\]

thus every label of (Z-Z_E) is anticomplete to (E).

Form a portal society (A_E) on (G[E]) with:

* one artificial interface terminal (t_F), adjacent to the vertices of
  (E) having a neighbour in (F); and
* one artificial terminal for **every** label in (C), each adjacent to its
  full portal set in (E).

Suppose an edge-only completion makes (A_E) a web.  Let (K) be one of
its inserted cliques behind a facial triangle containing (t_F).  The two
other vertices of that triangle are denoted (p,q).  Map an artificial
label terminal among (p,q) back to its actual boundary label, and retain
an actual (E)-vertex unchanged; call the resulting set (R).  Thus

\[
 |R|\le2.                                           \tag{1.1}
\]

### Theorem 1.1 (interface attachment surplus)

For every nonempty component (X) of the original graph (G[K]),

\[
 |N_F(X)|\ge k-|Z_E|-2.                            \tag{1.2}
\]

In particular, at a sharp (HC_7) web with (|Z_E|\le3), every surviving
interface pocket has at least two distinct neighbours in the opposite
piece (F).

### Proof

Because the web is an edge-supergraph of (A_E), an original edge from
(X) to a vertex of (E-K) can end only at one of the two non-interface
vertices of the facial triangle.  An edge from (X) to a cyclic
boundary label is represented by the corresponding artificial-terminal
edge, so that label is again accounted for by (R).  The only boundary
labels not represented in the society which can see (X) lie in (Z_E).
Finally, every edge
from (X) to (F) is recorded only by incidence with (t_F), and its
actual endpoint lies in (N_F(X)).  Therefore

\[
 N_G(X)\subseteq R\cup Z_E\cup N_F(X).             \tag{1.3}
\]

The nonempty opposite shore (D') lies outside (X\cup N_G(X)).  Hence
(N_G(X)) separates (X) from (D'), and (k)-connectivity gives

\[
 k\le |N_G(X)|\le |R|+|Z_E|+|N_F(X)|.
\]

Use (1.1) to obtain (1.2).  \(□\)

## 2. Structural interpretation

The requirement that every label of (C) be represented is essential.
Equivalently, every unrepresented boundary label which has an (E)-contact
must be charged to (Z_E) in (1.2).  Without that convention, an uncounted
boundary contact can
invalidate (1.3).

The ordinary bare-web argument removes an inserted clique whose triangle
does not contain (t_F): then (N_F(X)=\varnothing), and (1.3) is a cut
smaller than (k).  Theorem 1.1 describes exactly what replaces that
argument at the unique interface terminal.  The pocket cannot survive by
one irreplaceable portal.  It is a bridge with a quantitatively forced
attachment set in (F).

For (k=7,|Z_E|=3), choose two distinct attachments (f_1,f_2\in N_F(X)).
The connected set (X) supplies an (f_1)-(f_2) ear relative to (F).
Thus the next exchange has only two legitimate outcomes:

1. use that ear to split or reroute (F) while retaining its prescribed
   boundary contacts; or
2. show that every such ear is trapped behind an exact order-seven
   separator.

This is label-free and applies both to the degree-eight triple-lock web and
to the covering bad-split web at an arbitrary sharp order-seven adhesion.
It does not assert that two attachments alone preserve all portal classes;
that is the remaining portal-labelled peel theorem.

In the degree-eight (05)-lock application, take

\[
 C=\{2,4,6\},\qquad Z=\{0,3,5,w\}.
\]

The unique bad contact row has (N_E(3)=\varnothing), so
(Z_E=\{0,5,w\}) and (1.2) gives two distinct (F)-attachments.  If there
are exactly two, every inequality in the proof is tight: (|R|=2), the
pocket sees all three effective omitted labels, and

\[
 R\cup\{0,5,w\}\cup N_F(X)
\]

is an exact seven-cut.  Three or more attachments give a genuine surplus
(F)-ear, but do not by themselves preserve the separated (4)- and
(6)-portal classes.
