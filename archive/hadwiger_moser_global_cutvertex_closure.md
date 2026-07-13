# Global cutvertex closure for the two-component pure-Moser cell

## Theorem

Let (G) be seven-connected, let (d(v)=7), put (N=N_G(v)), and
suppose

\[
G[N]\cong M,
\qquad
G-N[v]=C_1\mathbin{\dot\cup}C_2,
\]

where

\[
E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

Then, if either (C_1) or (C_2) has a cutvertex, (G) contains a
(K_7)-minor.  Consequently both exterior components in a surviving
pure-Moser cell are cutvertex-free.

This conclusion is independent of the selected exact trace and its support
word.

## Proof

Suppose (z) is a cutvertex of (C_1), and let (D) be one component of
(C_1-z).  Put (E=C_1-D).  The sets (D,E) are disjoint and connected,
and an edge joins them.  A second component of (C_1-z) lies in (E).

Since

\[
N_G(D)\subseteq N\cup\{z\},
\]

seven-connectivity gives (|N_N(D)|\ge6).  Applying the same argument to
a second component of (C_1-z) gives (|N_N(E)|\ge6).  Thus each shore
(D,E) has at most one boundary defect.  Their nonempty defects are
distinct, because (D\cup E=C_1) and (N_G(C_1)=N).

The other exterior component (C_2) is connected and adjacent to every
vertex of (N).  We construct six branch sets from (D,E,C_2) and three
singleton boundary vertices.

The four triangles of (M) are

\[
012,\qquad034,\qquad126,\qquad345.                 \tag{1}
\]

Let (d_D,d_E\in N\cup\{\varnothing\}) denote the two defects.  There
exist a triangle (T\) from (1) and three distinct vertices

\[
a_D,a_E,a_2\in N-T
\]

such that:

* (a_D\ne d_D) and (a_E\ne d_E);
* if (d_D\in T), then (a_Dd_D\in E(M));
* if (d_E\in T), then (a_Ed_E\in E(M)).

This is a finite seven-vertex assertion.  The dependency-free verifier
`moser_global_cutvertex_verify.py` checks all 57 ordered possibilities for
the two distinct-or-empty defects against the four triangles and all anchor
assignments.

Now take the six bags

\[
\{t\}\ (t\in T),\qquad
D\cup\{a_D\},\qquad E\cup\{a_E\},\qquad
C_2\cup\{a_2\}.
\]

They are disjoint, connected, and all meet (N).  The singleton bags form
a triangle.  The (C_2)-bag is adjacent to every other bag because (C_2)
meets every boundary vertex.  The (D)- and (E)-bags are adjacent to one
another through the (DE)-edge.  Each is adjacent to every singleton
triangle bag: it directly meets every triangle vertex except possibly its
unique defect, and the anchor supplies the missing adjacency in that case.
Hence the six bags form an (N)-meeting (K_6)-model in (G-v).  Adding
the singleton bag ({v}) gives a (K_7)-model. \(\square\)

