# Tight seven-boundary shores at order eight: uncrossing and a crossing obstruction

This note gives one positive uncrossing lemma and one explicit obstruction
to the tempting next step.  The obstruction satisfies the full local
(K_3\dot\cup K_4) hypotheses and is seven-connected.  It is not a
counterexample to the helper conclusion: explicit helpers exist.

## 1. Intersecting tight shores uncross

Work in the host induced by (A\cup B\cup C), and for (X\subseteq C)
write

\[
 \partial X=N(X),\qquad b(X)=|\partial X|.
\]

Seven-connectivity gives (b(X)\ge7) for every nonempty (X\subseteq C).
Call (X) *tight* when (b(X)=7).

### Lemma 1.1 (intersecting lattice)

If tight shores (X,Y\subseteq C) have nonempty intersection, then
(X\cap Y) and (X\cup Y) are tight.  Consequently, distinct globally
inclusion-minimal tight shores are disjoint.

#### Proof

Let \(\Gamma(X)=X\cup N(X)\).  Closed neighbourhood is submodular:

\[
 \Gamma(X\cup Y)=\Gamma(X)\cup\Gamma(Y),\qquad
 \Gamma(X\cap Y)\subseteq\Gamma(X)\cap\Gamma(Y).
\]

Taking cardinalities and subtracting the modular identity
\(|X|+|Y|=|X\cup Y|+|X\cap Y|\) gives

\[
 b(X)+b(Y)\ge b(X\cup Y)+b(X\cap Y).                \tag{1.1}
\]

The two terms on the right are at least seven, while the left side is
fourteen.  Equality follows.  If two globally minimal tight shores
intersect, their tight intersection forces both to equal it. \(\square\)

This does **not** imply that witnesses for boundary vertices can be
replaced by globally minimal shores: the boundary vertex can disappear
when one passes to the intersection.

## 2. A seven-connected crossing example

Let

\[
 A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3,b_4\},
\]

and let

\[
 C=\{x,y,u_1,u_2,u_3,r_1,r_2,r_3\}.
\]

As usual (A\cong K_3), (B\cong K_4), there are no (A)--(B)
edges, and (v) is adjacent precisely to (A\cup B).  On (C), take
the cycle

\[
 x u_1 u_2 u_3 y r_1 r_2 r_3 x
\]

and add the chord (u_1u_3).  Every (a_i,b_1,b_2) is adjacent to all
of (C), while

\[
 N_C(b_3)=\{r_1,r_2,r_3\},\qquad
 N_C(b_4)=\{x,r_1,r_2,r_3\}.                        \tag{2.1}
\]

All row lower bounds hold.  Notice that (x,y) lie in no tight row:
the (A)-rows and the first two (B)-rows have order eight, the
(b_3)-row of order three avoids them, and the (b_4)-row has order
four.

### Lemma 2.1

The graph just defined is seven-connected.

#### Proof

The vertex (v) has degree seven, so connectivity is at most seven.
Let (S) have order at most six.  The graph (C) is two-connected.

Five vertices of (N(v)), namely (A\cup\{b_1,b_2\}), are complete to
(C).  If one of them survives, it joins every surviving component of
(C-S).  Every remaining (A)-vertex attaches directly through (C),
and every remaining (B)-vertex attaches through its clique, (v), or
one of its (C)-neighbours.  Isolating a surviving special (B)-vertex
from this component would require deleting (v), the other three
(B)-vertices, and all its at least three (C)-neighbours, at least
seven vertices.

If none of the five (C)-complete boundary vertices survives, five
members of (S) are already used.  At most one additional vertex is
deleted.  Hence (C-S) is connected, and each surviving special
(B)-vertex retains at least two (C)-neighbours; (v), if present,
also attaches through them.  Thus (G-S) is connected in every case.
\(\square\)

For completeness, every nonempty (Z\subseteq C) also has
\(|N(Z)|\ge7\) directly: five boundary vertices are complete to (C),
and a proper shore with at least two vertices outside has at least two
(C)-boundary vertices by two-connectivity.  Shores missing only one
(C)-vertex meet all seven boundary rows, as does (C) itself.

## 3. Unique minimal witnesses cross

A direct boundary calculation gives precisely the following tight
shores:

\[
\begin{gathered}
 \{y\},\quad \{u_2\},\quad \{u_1,u_2\},\quad
 \{u_2,u_3\},\\
 \{y,u_2,u_3\},\quad \{u_1,u_2,u_3\},\quad
 \{y,u_1,u_2,u_3\},\quad C .                       \tag{3.1}
\end{gathered}
\]

For example,

\[
 N(\{u_1,u_2\})=(A\cup\{b_1,b_2\})\cup\{x,u_3\},
\]

and

\[
 N(\{u_2,u_3\})=(A\cup\{b_1,b_2\})\cup\{y,u_1\},
\]

so both shores are tight.  The complete list (3.1) follows by inspecting
the two arcs of the displayed eight-cycle; the chord only changes the
boundary of sets containing exactly one of (u_1,u_3).

The globally inclusion-minimal tight shores are \(\{y\}\) and
\(\{u_2\}\).  Neither is a witness for (x): the first is not adjacent
to (x), and (x) is not adjacent to (u_2).  The unique
inclusion-minimal tight shore having (x) in its boundary is

\[
 X=\{u_1,u_2\}.
\]

Similarly, the unique inclusion-minimal tight witness for (y) is

\[
 Y=\{u_2,u_3\}.
\]

Thus

\[
 X\cap Y=\{u_2\}\ne\varnothing,\qquad
 X\nsubseteq Y,\qquad Y\nsubseteq X.              \tag{3.2}
\]

Both (x,y) are non-cutvertices of the two-connected graph (C), and,
as observed above, neither belongs to a tight boundary row.  Hence even
under full seven-connectivity and the exact row bounds, choosing
inclusion-minimal witnesses for uncovered non-cutvertices need not give a
laminar family.

## 4. What the crossing means

The example does have the desired helper bags:

\[
 J_1=\{a_1,r_1\},\qquad J_2=\{a_2,r_2\}.             \tag{4.1}
\]

They are disjoint and connected, and both (r_1,r_2) are adjacent to
all four vertices of (B).  Thus the example is not an obstruction to
the (K_7)-minor construction.

Its consequence is narrower but decisive for the proposed route:

> Global tight atoms are disjoint, but they do not preserve specified
> boundary vertices; minimal boundary-witness shores can cross
> irreducibly.  Any proof following this minimal-witness uncrossing route
> must add a mechanism which converts such a crossing into either helper
> bags or a deletable vertex.  This route cannot obtain laminarity merely
> by replacing witnesses with intersections or globally minimal tight
> shores.

In this example the crossing intersection \(\{u_2\}\) is exactly the
kind of vertex which remains deletable.  This suggests a sharper next
lemma—“irreducible crossing implies a deletable intersection vertex or
two helpers”—but that implication is not proved here.
