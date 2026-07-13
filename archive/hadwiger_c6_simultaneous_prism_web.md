# Simultaneous webs in the \(C_6\dot\cup K_1\) contact core

## 1. Setting

Let

\[
 S=W\dot\cup\{z\},\qquad W=\{c_0,\ldots,c_5\},
\]

where \(z\) is complete to \(W\), and the missing boundary edges are

\[
 e_i=c_ic_{i+1}\qquad(i\in\mathbb Z/6\mathbb Z).       \tag{1.1}
\]

Thus \(G[W]\) is a triangular prism.  Its two triangles are the even
and odd vertices of (1.1), and its identity matching is

\[
 c_0c_3,\qquad c_1c_4,\qquad c_2c_5.                 \tag{1.2}
\]

Assume that \(G\) is seven-connected, \(\delta(G)\ge7\), and
\(G-S\) has two anticomplete connected components \(D_1,D_2\), each
full to \(S\).  Put

\[
 P_i^j=N_{D_j}(c_i).
\]

No representative of a portal set is fixed: every statement below is
about the full sets \(P_i^j\).

## 2. A global three-flow forced by seven-connectivity

### Lemma 2.1

In the auxiliary graph obtained from \(D_1\dot\cup D_2\) by adjoining
the six terminals \(c_0,\ldots,c_5\), retaining just terminal--shore
edges and shore-internal edges, there are three vertex-disjoint paths
from the even terminal set to the odd terminal set.  Their interiors lie
outside \(S\), and every path lies in one shore.

### Proof

Every \(c_i\) has four neighbours in \(G[S]\).  Minimum degree seven
therefore gives it at least three neighbours in \(D_1\cup D_2\).

If the asserted linkage does not exist, Menger's theorem gives a
separator \(K\) of order at most two between the two three-element
terminal sets.  Both terminal sets have a surviving vertex.  No
surviving terminal loses all its exterior neighbours, since it has at
least three and \(|K|\le2\).  Choose a component \(C\) of
\((D_1\cup D_2)-K\) adjacent to a surviving even terminal.  It has no
surviving odd terminal neighbour.  Consequently

\[
 N_G(C)\subseteq
 \{c_0,c_2,c_4\}\cup(K\cap\{c_1,c_3,c_5\})
 \cup\{z\}\cup(K\cap(D_1\cup D_2)).                \tag{2.1}
\]

The right side has order at most six.  It separates \(C\) from the
opposite nonempty shore, contrary to seven-connectivity.  Thus the
linkage exists.  Since all six terminals are its distinct endpoints,
the paths may be shortened to have no internal terminal; a path then
lies wholly in one shore. \(\square\)

The pairing supplied by Lemma 2.1 is not controlled, and its three paths
may split \(2+1\) between the shores.  The theorem in
`hadwiger_c6_three_linkage_exclusion.md` says that if all three occur in
one shore, their pairing must be the identity matching (1.2).  This is
the precise distribution gap; Menger alone does not put all three paths
in one component.

## 3. Three bare four-webs in every shore

For \(r=0,1,2\), form \(A_r^j\) from \(G[D_j]\) by adding four
independent artificial terminals for

\[
 c_r,c_{r+1},c_{r+3},c_{r+4},                       \tag{3.1}
\]

each adjacent to its full portal set, and take the frame order

\[
 (c_r,c_{r+3},c_{r+1},c_{r+4}).                    \tag{3.2}
\]

A crossing of (3.2) is exactly an \(e_r\mid e_{r+3}\) linkage.  Each
of these three antipodal two-linkages has an explicit positive
\(K_7\) quotient.  Hence all six auxiliary societies are crossless in a
\(K_7\)-minor-free realization.

### Lemma 3.1 (simultaneous bare-web lemma)

For every \(j\) and \(r\), \(A_r^j\) has a same-vertex edge-completion
to a bare planar four-web with frame (3.2).  In particular \(D_j\) is
planar, and in the induced embedding of \(D_j\) the four portal sets in
(3.1) lie on one face.

### Proof

Apply the generalized Two Paths Theorem to the crossless tuple (3.2).
It gives a same-vertex web completion.  Suppose a nonempty inserted
clique \(X\subseteq D_j\) lies behind a facial triangle \(T\).  Replace
each artificial terminal in \(T\) by its boundary label.  The resulting
set of at most three vertices accounts for every neighbour of \(X\) in
\(D_j\) and in the four represented boundary classes.  Add the three
omitted boundary vertices.  The resulting set has order at most six and
separates \(X\) from the opposite shore, contrary to
seven-connectivity.  Thus the web is a bare rib.

Deleting its four frame terminals leaves a plane embedding of \(D_j\)
in which every neighbour of those terminals is incident with the merged
outer face. \(\square\)

This conclusion uses portal sets, not selected portal vertices.  It
therefore survives all representative-multiplicity objections to a
formal cyclic-order argument.

## 4. The three-connected face trichotomy

Fix a three-connected shore \(D=D_j\).  Its plane embedding is unique up
to reflection.  By Lemma 3.1 there are faces \(F_0,F_1,F_2\) with

\[
\begin{aligned}
F_0&\supseteq P_0\cup P_1\cup P_3\cup P_4,\\
F_1&\supseteq P_1\cup P_2\cup P_4\cup P_5,\\
F_2&\supseteq P_0\cup P_2\cup P_3\cup P_5.
\end{aligned}                                       \tag{4.1}
\]

Here containment means containment in the facial boundary.

### Lemma 4.1 (face trichotomy)

Exactly one of the following can occur.

1. \(F_0=F_1=F_2\); hence all six portal sets lie on one face.
2. The three faces are distinct.  In this case either \(|D|\le5\), or
   their pairwise intersections are three pairwise vertex-disjoint edges
   and \(D\) is their unsubdivided triangular-prism union.

The triangular-prism subcase contradicts \(\delta(G)\ge7\).
Consequently every three-connected shore of order at least six is in the
common-face outcome; orders four and five remain a finite contact base.

### Proof

Two distinct faces of a three-connected plane graph intersect in at
most one vertex or one edge.  If, for example,
\(F_0=F_1\ne F_2\), then the common face contains all six portal sets,
while \(F_2\) shares with it the four sets

\[
 P_0\cup P_2\cup P_3\cup P_5.
\]

Their union \(X\) has order at most two.  Since \(|D|\ge4\), a
component of \(D-X\) is separated in \(G\) by

\[
 X\cup\{c_1,c_4,z\},
\]

of order at most five.  This is impossible.  Thus either all faces
coincide or all are distinct.

Assume they are distinct.  From (4.1),

\[
\begin{aligned}
P_1\cup P_4&\subseteq F_0\cap F_1,\\
P_2\cup P_5&\subseteq F_1\cap F_2,\\
P_0\cup P_3&\subseteq F_2\cap F_0.                 \tag{4.2}
\end{aligned}
\]

Let \(X\) be the union of all six portal sets.  Equation (4.2) gives
\(|X|\le6\).  If \(D-X\ne\varnothing\), every component \(C\) of it
satisfies

\[
 N_G(C)\subseteq X\cup\{z\}.                       \tag{4.3}
\]

Seven-connectivity forces equality throughout: \(|X|=6\), the three
face intersections in (4.2) are disjoint edges, and each contains
exactly the two portal representatives of its displayed label pair.
If \(D=X\), the same conclusion follows unless \(|D|<6\); retain that
possibility as the finite base case.

The union of three distinct facial cycles which pairwise share three
disjoint edges is a subdivision of the triangular prism: the shared
edges are its rungs, and the two private arcs on each facial cycle form
the two rim cycles.  No vertex can lie off the six rung endpoints.
Indeed, after deleting those endpoints, every remaining component is
drawn in one of the two cap regions and has neighbours in at most the
three endpoints on that cap; together with \(z\) this gives a cut of
order at most four.  Thus the subdivision is unsubdivided and
\(D=X\) is the triangular prism.

Finally, a vertex of this prism has three neighbours in \(D\), can see
only the two boundary labels belonging to its rung in (4.2), and can
also see \(z\).  Hence its degree in \(G\) is at most six, contrary to
\(\delta(G)\ge7\).  This eliminates outcome 2. \(\square\)

The script `c6_distinct_face_small_core_verify.py` deliberately tests
only the linkage and face-incidence hypotheses at orders four and five.
It finds abstract survivors, so those hypotheses alone do **not** close
the finite base.  Any closure there must also impose the full
minimum-degree/contact rows or replay the actual \(K_7\) quotient.  This
is a useful guard against overstating the face argument.

## 5. Exact residual: common-face portal coherence

The sole three-connected residual has all six full portal sets on one
face of each shore.  It is not legitimate to choose one representative
from each set independently for six different linkage demands.  The
needed closure statement is the following genuinely simultaneous form.

> **Common-face prism lemma.**  Let \(D_1,D_2\) be the two planar
> full-portal societies above, with all six portal sets of each society
> on one face.  Assume the three antipodal linkages
> \(e_i\mid e_{i+3}\) are absent in each society; every one of the six
> same-parity frame linkages occurs in exactly one society, with opposite
> frames having the same owner; and neither society has a nonidentity
> even-to-odd three-linkage.  Then the two societies contain a
> boundary-rooted \(C_6\) model, or their two disk embeddings glue to a
> six-colourable graph.

This statement keeps the entire portal sets and therefore does not make
the invalid common-representative inference.

There is a sharp coherent special case.  If the six portal sets occupy
six disjoint intervals of the common face, the three antipodal web
orders leave, up to reversal, only six cyclic label orders.  In every
one, exactly one opposite pair of same-parity frames is noncrossing.
But the ownership theorem forces one shore to own at least two opposite
pairs.  Hence the coherent-interval case is impossible.  A surviving
common-face shore must therefore have nested or overlapping portal
sets.  The remaining local theorem is now:

> **Portal uncrossing lemma.**  In the common-face case, nested or
> overlapping full portal stars either admit a simultaneous uncrossing
> into six disjoint intervals, or expose a two-cut whose defect pair is
> one of \(\{v\}\mid N_{C_6}(v)\) or
> \(M_i\mid M_j\).

The two-cut alternatives are exactly the already enumerated rope locks.
Thus this is the narrow interface between the generalized Two Paths
Theorem and the exact two-piece atlas.

## 6. Relation to the specified-edge prism theorem

Contracting the two pieces of a same-parity frame crossing produces a
specified edge.  The Costalonga--Reid--Wu specified-edge prism theorem
then gives either a prism through that edge, one of its wheel/
\(K_{3,n}\)-type exceptions, or a specified three-cut with tree pieces.
The theorem is not by itself portal-preserving: a prism through the
specified edge can put the outward portal classes on the two wrong root
bags.  Exact quotient replay shows that every other placement closes.

Consequently a valid derivation from that theorem must add precisely one
claim: in a seven-connected full-portal society, the wrong-root placement
either reroutes through the prism, or its specified three-cut projects to
one of the two-cut defect locks above.  This is equivalent to the portal
uncrossing lemma, not to an unrooted prism theorem.
