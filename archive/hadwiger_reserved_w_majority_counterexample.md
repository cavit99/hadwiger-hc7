# A sharp obstruction to static bilateral `w`-state majority

## 1. Result

The orientation-free rank-one leaf theorem in
`hadwiger_reserved_connector_rank_leaf.md` is valid for an ordinary
four-terminal crossless frame.  A stronger static claim suggested by it is
false:

> A linked pair of disjoint Moser frames in every full relative shore
> satisfying the exact seven-cut inequalities realizes a strict majority of
> the legal equality positions of the sixth portal (w).

The counterexample below has shore order six, the smallest order compatible
with the installed reserved-connector bound.  It satisfies every local
seven-cut inequality, has the required linked frame, and has exactly two
legal (w)-positions.  Neither has a strong branch-set realization.

Thus the bilateral overlap lemma cannot follow from portal fullness, Hall,
seven-connectivity inequalities, and one linked frame alone.  Boundary
minor-switching (or an equivalent critical exchange axiom) is essential.

## 2. The wheel shore

Let

\[
 D=G[\{l_0,l_1,l_2,l_3,l_4,h\}]
\]

be the wheel whose rim is (l_0l_1l_2l_3l_4l_0) and whose hub (h)
sees all five rim vertices.  Its seven-label relative boundary is

\[
 L=\{q_0,q_1,q_2,w,q_4,r,a\}.
\]

For (i\in\mathbb Z_5), where the outer cyclic order is

\[
 q_0,q_1,q_2,w,q_4,
\]

put

\[
 N_D(q_i)=\{l_i,l_{i-1}\}.
\tag{2.1}
\]

Both (r) and (a) are complete to (D).  This is one side of the
standard icosahedron separator: adding a second hub on the other side of
the five-cycle gives the icosahedron, and joining two universal vertices
gives a seven-connected graph.  In particular the incidence system is not
an arbitrary row construction.

Directly, for every nonempty proper (X\subsetneq D),

\[
 |N_D(X)-X|+|N_L(X)|\ge7.                 \tag{2.2}
\]

Here is a short verification.  The labels (r,a) always contribute two.
If (h\notin X) and (Y=X\cap\{l_0,\ldots,l_4\}), the internal boundary
contains (h) and the rim boundary of (Y); the outer labels met by (Y)
are the union of the two cyclic shifts of (Y).  The sum of the latter two
cardinalities is at least four.  If (h\in X), write

\[
 X=\{h\}\cup Y,
\]

where (Y) is a proper rim subset.  The internal boundary contains all
(5-|Y|) omitted rim vertices, while (2.1) meets at least (|Y|) outer
labels.  Adding (r,a) again gives seven.  Full attachment is immediate.

## 3. The pure-Moser state

Let the five uniquely coloured roots be

\[
 U=\{q_0,q_1,q_2,q_4,r\},
\]

and declare their missing-edge cycle to be

\[
 q_0q_1q_2q_4rq_0.                         \tag{3.1}
\]

Thus (G[U]) is the pure-Moser five-root graph, the complement of (3.1).
Take the disjoint frame

\[
 e=q_0q_1,\qquad f=q_2q_4,
\]

with leftover root (r).  It is linked in (D): use

\[
 q_0l_0q_1
 \quad\text{and}\quad
 q_2l_2l_3q_4.                              \tag{3.2}
\]

These paths are disjoint.  Their two pair bags are adjacent through a
present Moser boundary edge, and the leftover singleton (r) is adjacent
to each pair.  No shortest connector between the paths is needed.

Give (w) the boundary contacts

\[
 wq_2,wq_4,wr,wa,wb\in E(G),
 \qquad
 wq_0,wq_1\notin E(G).                       \tag{3.3}
\]

The only legal decorations of the state

\[
 13\mid e\mid f\mid\{r\}
\]

are therefore

\[
 13\mid(e\cup\{w\})\mid f\mid\{r\},
 \qquad
 13\mid e\mid f\mid\{r\}\mid\{w\}.       \tag{3.4}
\]

The other three mergers identify (w) with an adjacent boundary vertex.

## 4. Neither legal state has a strong realization

Suppose first that the merged-(e) state in (3.4) had a strong
realization.  Its (e\cup\{w\})-bag and (f)-bag would be disjoint
connected subgraphs of the closed planar disk consisting of (D) and its
five outer terminals.  The first contains the outer terminals

\[
 q_0,q_1,w,
\]

and the second contains (q_2,q_4).  A path in the first joining (w)
to (q_0) or (q_1), and a path in the second joining (q_2) to (q_4),
have alternating ends on the outer face.  The Jordan curve theorem says
they meet, a contradiction.

For the singleton-(w) state, let (E,F,W) be its (e,f,\{w\}) bags.
The strong realization requires (E) and (W) to be adjacent.  Add one
edge witnessing that adjacency.  Then (E\cup W) is connected, contains
(q_0,q_1,w), and is disjoint from the connected (F) containing
(q_2,q_4).  The same alternating-ends argument is a contradiction.

Hence this shore realizes zero of its two legal decorations, despite
(2.2), full attachment, order six, and the explicit linkage (3.2).

The dependency-free replay
`reserved_w_majority_counterexample_verify.py` checks all 62 nontrivial
shore-subset inequalities, the linkage, the legal-position calculation,
and exhaustively rejects every allocation of the six shore vertices to
the four or five proposed branch sets.

## 5. Boundary universality and the missing critical axiom

The wheel obstruction is excluded from an actual minor-minimal
counterexample for a stronger, exactly checkable reason.  Regard the whole
seven-set

\[
 L=\{q_0,q_1,q_2,w,q_4,r,a\}
\]

as a labelled boundary.  Up to permutation of six colours there are exactly
41 partitions of (L) into at most six independent colour classes.  **Every
one of the 41 states extends across the wheel shore (D).**

The script `reserved_w_wheel_transition_probe.py` enumerates the 41 states
and verifies all 41 extensions by exact backtracking.  It also checks the 24
states on the six-vertex adhesion (L-\{a\}): all 24 already extend before
any internal operation, and hence no internal vertex deletion, edge deletion,
or edge contraction creates a new state.

Consequently this order-six web fails the critical-shore axiom in the
strongest possible way.  Colour the proper graph outside (D), restrict its
colouring to (L), and extend that state over (D); the two colourings glue.
Thus a non-six-colourable minor-minimal graph cannot contain this shore.
Equivalently, its boundary extension family is universal, whereas a critical
separation requires disjoint extension families and, after every one-step
minor operation, a genuinely new compatible state.

This finite universality is not used to prove the Jordan obstruction in
Section 4.  It identifies exactly why the obstruction is a valid
falsification of the static majority lemma but not a counterexample-derived
shore.

## 6. Exact lesson for the reserved-connector programme

The obstruction is a planar web, not a Hall defect or an SPQR leaf.  By
Section 5 it does not satisfy the counterexample's boundary-state axioms.
In particular it violates the basic incompatibility

\[
 \mathcal E_6(L,S)\cap\mathcal E_6(M,S)=\varnothing
\]

which precedes the one-step minor-switching condition.  A fortiori it
cannot model the transition requirement that every internal deletion or
contraction create a new state compatible with the opposite side but not
with the original shore.

Therefore the correct next lemma is not a static majority theorem.  It
must say that a planar five-portal web with the alternating pattern above
either has a boundary-extension-preserving internal reduction, contradicting
minor-criticality, or its one-step transition creates one of the missing
decorated states.  This is precisely the critical-web exchange axiom which
the rank-one leaf theorem by itself does not supply.
