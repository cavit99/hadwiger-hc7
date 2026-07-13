# Final independent audit: singleton-triangle packet/web closure

## Verdict

**GREEN for every nonsingleton atomic web, after minor edge-case
corrections to the preceding note.**  The two-tag construction below
turns the owner packet and any two positive-curvature vertices of the
web into seven explicit clique branch sets.  Thus a nonsingleton
packet-free shore with no proper relative seven-boundary is impossible
in a (K_7)-minor-free graph.

The exact remaining descendants are:

1. a packet-free shore of order one; or
2. a packet-free shore containing a nonempty proper set (X) with
   (|\partial_B(X)|=7), equivalently a nested exact seven-cut.

Nothing in this audit eliminates those two non-atomic outcomes.

## Audited construction

Use

\[
 P=\{h,c\},\qquad Q=\{r,a\},\qquad R=\{1,2,b\}.
\]

Let (X,Y) be the disjoint owner carriers for (P,Q), respectively.
The curvature lemma in
`hadwiger_singleton_triangle_q2_web_exchange.md` produces at least six
distinct original vertices (z) of the atomic web such that

\[
 z\sim1,2,b,\qquad z\sim p(z),q(z)
 \quad(p(z)\in P,\ q(z)\in Q).                  \tag{1}
\]

Choose two, (u\ne v).  In a spanning tree of the connected web,
delete an edge on the (u)-(v) path.  Its two components have vertex
sets (A,B), with (u\in A,v\in B).  They are disjoint, connected,
cover the web, and are adjacent through the deleted tree edge.

Now use

\[
 \{1\}\mid\{2\}\mid\{b\}\mid
 (X\cup\{h,c\})\mid(Y\cup\{r,a\})\mid A\mid B. \tag{2}
\]

Every bag is connected.  The first three form a triangle.  The
(Xhc)-bag sees them through (h1,h2,cb), and the (Yra)-bag
through (r1,r2,ab).  Those two bags are adjacent through (hr).
By (1), (A) and (B) each see all three singleton bags and both
owner bags.  Finally (A\sim B).  The shores are disjoint and the
five boundary sets in (2) are disjoint, so no branch-set overlap is
hidden.  These are seven pairwise adjacent connected bags.

This proof does not need the SDR/Hall lemma or a rooted (K_4)
subdivision after the curvature vertices have been obtained.

## Audit of the preceding structural chain

The relative Two Paths step is valid provided the cited same-vertex web
form is available.  Artificial terminals correctly encode overlapping
portal sets.  Before applying the relative-boundary inequality to a
facial insertion, the main proof should add that the inserted set is
proper: the whole shore cannot lie behind a triangle because fullness
gives neighbours at all four artificial terminals.

Lemma 3.2's two-cut form is correct.  Atomicity makes every lobe meet
both cut vertices and exactly six boundary labels.  All defects lie in
one active pair; three lobes give two disjoint carriers; with two lobes,
packet failure forces complementary defects and forces the cut vertices
to miss both defective roots.  Lemma 4.1 then gives the displayed
(K_7)-model (and its (P\leftrightarrow Q) symmetric version).

The bilateral web gluing in Theorem 5.1 is correct.  If a shore is a
singleton, invoke directly the planar wheel consisting of that vertex
and the frame (C_4), rather than Theorem 2.1, which assumes shore order
at least two.  The theorem's final three-connectivity clause must also
be qualified by (|D|\ge2); atomicity is vacuous for a singleton.

The curvature identity and cofacial argument are sound in the
nonsingleton atomic branch.  Positive curvature comes only from an
interior degree-five vertex or an outer degree-three vertex and hence
from a common neighbour of (R).  The rooted-(K_4) characterization
forces all such common neighbours onto one face; fan retriangulation
forces that face to be the web face.  A final triangulation then has no
positive interior vertex, so every positive vertex satisfies (1), has
degree eight in (G), and the total curvature forces at least six
distinct such vertices.

Accordingly, the atomic web family is closed for arbitrary shore order.
The nested exact-cut and singleton descendants are the precise remaining
gap on this branch.
