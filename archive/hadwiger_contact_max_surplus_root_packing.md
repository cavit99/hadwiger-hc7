# Spanning contact maximum: triple-root and two-double packing

## 1. Terminal normalization

Use Theorem 3.1 of
`hadwiger_contact_maximal_spanning_normalization.md`.  In the \(HC_7\)
terminal cell, a spanning contact-maximal \(K_6\)-model has five contacted
bags and one uncontacted bag \(U\).  All seven (or more) roots lie in the
five contacted bags.  With exactly two units of root surplus, either

1. one contacted bag contains at least three roots; or
2. two contacted bags contain at least two roots each.

This note gives exact branch-set criteria for both distributions.  Every
successful construction produces six contacted bags, contradicting
contact maximality.

## 2. A triple-root bag and the uncontacted helper

Let \(B\) contain distinct roots \(a,z,c\), and let
\(K_1,K_2,K_3,K_4\) be the other four contacted clique bags.  The sixth
old bag \(U\) is uncontacted.  Suppose \(B\) contains three pairwise
disjoint, pairwise adjacent connected sets

\[
                         A,Z,C                            \tag{2.1}
\]

with \(a\in A,z\in Z,c\in C\), and suppose \(C\sim U\).  Put

\[
                         C^+=C\cup U.                     \tag{2.2}
\]

It is connected, contains the root \(c\), and is adjacent to every
\(K_i\) through the old clique edges from \(U\).

For \(i\in[4]\), record the pole mask

\[
 \sigma(i)=\{A:E(A,K_i)\ne\varnothing\}
          \cup\{Z:E(Z,K_i)\ne\varnothing\}.              \tag{2.3}
\]

The mask may be empty.  Call \(i\) crossing when
\(\sigma(i)=\{A,Z\}\).

### Theorem 2.1 (uncontacted-helper triangle packing)

The model admits a six-contact \(K_6\)-model if either

1. at least three of the four labels are crossing; or
2. exactly two are crossing and the masks of the other two labels have
   union \(\{A,Z\}\).

#### Proof

Partition the four \(K_i\)'s into three nonempty blocks.  Use two
crossing labels as singleton blocks.  In outcome 1, put the remaining
two labels into the third block, which contains a crossing label.  In
outcome 2 put the two noncrossing labels into the third block; together
they see both poles.

Replace a block by the union of its old clique bags.  The three block
carriers are connected and pairwise adjacent.  Each sees \(A,Z\) by
construction and sees \(C^+\) through the old edges to \(U\).  Hence

\[
                    A,Z,C^+,\text{ three block carriers} \tag{2.4}
\]

are six pairwise adjacent connected sets.  All six are contacted: the
first three contain \(a,z,c\), while every block contains at least one
of the four originally contacted bags.  Thus (2.4) is the required
contact augmentation. \(\square\)

### Corollary 2.2 (exact triple-root two-pole lock)

At contact maximum, every rooted triangle (2.1) whose third piece meets
\(U\) has either

1. at most one crossing label; or
2. exactly two crossing labels, while the two remaining masks fail to
   cover both poles.

This is stricter than the double-root helper lock: there is no
same-contact exception, because the unique uncontacted bag is spent as
the helper and all four remaining labels are contacted.

The hypothesis \(C\sim U\) is the exact residual placement issue.  If
\(B\) is 2-connected, three distinct roots have a rooted triangle, but a
separate argument is still needed to make the branch piece rooted at
\(c\) capture a prescribed \(U\)-portal.  This requirement is not hidden
in the theorem.

## 3. Two double-root bags: the one-bag test

Let \(A\) contain roots \(a_1,a_2\), let \(B\) contain roots
\(b_1,b_2\), and let \(K_1,K_2,K_3\) be the other contacted bags.  The
bag \(U\) is uniquely uncontacted.

### Lemma 3.1 (one double bag opens)

If \(A=A_1\dot\cup A_2\) is a connected adjacent rooted split, with
\(a_i\in A_i\), and each \(A_i\) is adjacent to

\[
                         B,K_1,K_2,K_3,                   \tag{3.1}
\]

then

\[
                  A_1,A_2,B\cup U,K_1,K_2,K_3            \tag{3.2}
\]

are six contacted clique bags.  The symmetric statement holds for a
split of \(B\).

#### Proof

The old clique edge \(BU\) makes \(B\cup U\) connected.  Conditions
(3.1), the split edge, and all old clique edges give every required
adjacency in (3.2).  The split pieces contain \(a_1,a_2\), the third bag
contains \(b_1,b_2\), and each \(K_i\) retains its old root. \(\square\)

If \(A\) is 2-connected and \(|N_A(B)|\ge2\), an
\(a_1\)-\(a_2\) bipolar ordering has a cut with a \(B\)-portal on each
side.  Thus the \(B\)-row itself can always be made two-sided.  In a
surviving lock, the obstruction in Lemma 3.1 is consequently confined to
the three rows \(K_1,K_2,K_3\): every such pole split loses at least one
of those named rows on one side.  Portal multiplicity for \(B\) alone is
not incorrectly treated as simultaneous multiplicity for all four rows.

## 4. Simultaneous splits and the exact seven-piece quotient

Take connected adjacent rooted splits

\[
             A=A_1\dot\cup A_2,\qquad
             B=B_1\dot\cup B_2,                          \tag{4.1}
\]

with the roots separated.  Assign the uncontacted bag to one singleton
carrier, say

\[
                         K_1^+=K_1\cup U.                 \tag{4.2}
\]

This is connected through the old clique edge and remains contacted by
the root of \(K_1\).  Define the seven-vertex support graph \(Q\) on

\[
                    A_1,A_2,B_1,B_2,K_1^+,K_2,K_3        \tag{4.3}
\]

by putting an edge precisely when the corresponding connected pieces are
adjacent in \(H\).  The edges

\[
 A_1A_2,\quad B_1B_2,\quad
 K_1^+K_2,K_1^+K_3,K_2K_3                              \tag{4.4}
\]

are forced.  Each singleton carrier has a neighbour in at least one \(A\)-piece
and at least one \(B\)-piece, and at least one edge joins an \(A\)-piece
to a \(B\)-piece.  The seven pieces now partition \(V(H)\), since the
old model was spanning.  Assigning \(U\) instead to \(K_2\) or \(K_3\)
gives two further support supergraphs which may also be tested.

### Lemma 4.1 (seven vertices to six)

For an arbitrary graph \(Q\) on seven vertices, \(Q\) has a \(K_6\)
minor if and only if at least one of the following holds.

1. Some vertex \(x\) meets every nonedge of \(Q\); equivalently,
   \(Q-x\cong K_6\).
2. There are adjacent vertices \(x,y\) such that
   \(Q-\{x,y\}\cong K_5\) and every other vertex is adjacent to at
   least one of \(x,y\).  Contracting \(xy\) gives \(K_6\).

Equivalently, if \(F=\overline Q\), then either \(F\) has a one-vertex
cover, or it has a two-vertex cover \(\{x,y\}\) such that

\[
                         xy\notin E(F),
                 \qquad N_F(x)\cap N_F(y)=\varnothing.   \tag{4.5}
\]

#### Proof

A six-branch-set minor model on a seven-vertex graph either uses six
vertices as singleton bags, deleting the seventh, or uses all seven and
has exactly one two-vertex connected bag.  These are respectively
outcomes 1 and 2.  Translating the two conditions into the complement
gives (4.5). \(\square\)

### Theorem 4.2 (exact simultaneous-split criterion)

The simultaneous splits (4.1) give a six-contact \(K_6\)-model if and
only if their support graph \(Q\) satisfies Lemma 4.1.

#### Proof

Every vertex of \(Q\) represents a disjoint connected branch piece and
contains a root: the four split pieces contain \(a_1,a_2,b_1,b_2\), and
the \(K_i\)'s retain their roots.  A \(K_6\)-minor model in \(Q\) lifts
by replacing every quotient vertex with its connected piece.  Every
lifted branch set remains contacted.

Conversely, a six-branch model obtained solely by grouping the seven
displayed pieces contracts back to a \(K_6\)-minor of \(Q\).  Lemma 4.1
is therefore exact for this simultaneous-split construction. \(\square\)

### Corollary 4.3 (uniform two-double support web)

If contact maximality survives every simultaneous rooted split, then for
every resulting support graph \(Q\), the complement \(F=\overline Q\)
has no one-vertex cover and every two-vertex cover is blocked in one of
the following two exact ways:

1. its two cover vertices are themselves nonadjacent in \(Q\); or
2. some third quotient vertex is nonadjacent in \(Q\) to both cover
   vertices.

Thus failure is a finite seven-piece support web.  It is not an
unspecified four-row portal obstruction: the missing edges have cover
number at least three, except for the two explicitly blocked cover
patterns above.

### Lemma 4.4 (the three atomic nonedge certificates)

Let \(Q\) be any graph on seven vertices with no \(K_6\)-minor.  Its
complement contains a subgraph, on the same vertex set with isolated
vertices allowed, isomorphic to one of

\[
                         K_3,\qquad P_4,\qquad 3K_2.      \tag{4.6}
\]

Each graph in (4.6) is itself an inclusion-minimal certificate: even if
every other missing edge of \(Q\) is added, the resulting graph still has
no \(K_6\)-minor.  Conversely, these are all inclusion-minimal
certificates.

#### Proof

Use the complement criterion in Lemma 4.1 and choose an
inclusion-minimal subgraph \(F_0\subseteq\overline Q\) which still has
neither an admissible one-cover nor an admissible two-cover.

If \(F_0\) has a matching of order three, minimality leaves exactly those
three edges, so \(F_0=3K_2\).  Suppose its matching number is at most two.
If \(F_0\) contains a three-edge path, that \(P_4\) already has no good
cover: the middle-vertex cover uses an edge, while either alternative
two-cover uses vertices with a common neighbour.  Minimality gives
\(F_0=P_4\).

It remains to suppose that \(F_0\) has no \(P_4\) subgraph.  Every
nontrivial component is then a star or a triangle.  A star has a
one-vertex cover, and two star components have a good two-cover at their
centres.  Three edge-containing components would give a three-edge
matching.  Hence failure with matching number at most two requires a
triangle component.  The triangle alone already has no good two-cover,
because each of its two-vertex covers consists of adjacent vertices.
Minimality gives \(F_0=K_3\).

Directly, none of the three graphs in (4.6) has an admissible cover in
Lemma 4.1: \(3K_2\) has cover number three; every two-cover of \(K_3\)
uses an edge; and every two-cover of \(P_4\) either uses its middle edge
or has a common neighbour.
Deleting any edge from any of them creates a good cover. \(\square\)

### Corollary 4.5 (three-motif reduction)

Every failed simultaneous split of two double-root bags names three
missing adjacencies among the seven pieces which form one of the motifs
in (4.6).  Repairing any one of those three adjacencies destroys that
particular atomic certificate; if no other atomic certificate remains,
the quotient immediately gives the six-contact model of Theorem 4.2.

Thus a dynamic proof only has to transport one of three motifs through
successive rooted splits.  The placement of their vertices among the two
root pairs and three singleton carriers is finite, but the structural
types themselves are uniform and label-free.

The forced edges (4.4) sharpen the triangle motif completely: a missing
triangle must consist of one \(A\)-half, one \(B\)-half, and one
singleton carrier \(K_i\), mutually nonadjacent.  A missing matching may
contain at most one \(A\)--\(B\) nonedge; its other edges join singleton
carriers to distinct rooted halves.  The \(P_4\) motif is the only
atomic case in which two missing edges can share a rooted half without
forming the missing triangle.  These observations follow immediately
because \(A_1A_2,B_1B_2\), and all \(K_iK_j\) are forced edges of
\(Q\).

## 5. Readable sufficient subcases

The quotient criterion contains several useful hand-checkable closures.

1. If every \(K_i\) sees both \(B_1,B_2\), and each \(B_j\) sees at
   least one of \(A_1,A_2\), contract the edge \(A_1A_2\).  The other
   five quotient vertices form a clique, and the contracted vertex sees
   all of them.
2. Symmetrically, one may contract \(B_1B_2\).
3. If \(A_1,A_2\) are complete to \(B_1,B_2\), one \(K_i\) sees all
   four halves, and the union of two other \(K\)-rows sees every half,
   contract the edge between those two \(K\)-vertices.
4. If \(A_pB_q\) and \(A_{3-p}B_{3-q}\) are edges, every \(K_i\) sees
   both \(A_{3-p},B_{3-q}\), and every \(K_i\) sees at least one of
   \(A_p,B_q\), contract \(A_pB_q\).

Every listed contraction gives six explicit branch sets by taking the
union of the two contracted pieces and retaining the other five pieces.

## 6. Exact remaining structural work

The triple-root case is reduced to capturing the unique uncontacted row
in one piece of a rooted triangle and then avoiding the two-pole lock of
Corollary 2.2.  The two-double case is reduced to finding simultaneous
splits whose seven-piece complement passes the exact cover test (4.4).

If neither occurs, the next valid theorem may target either:

* a two-cut/owner decomposition forcing the same blocked cover in every
  simultaneous split; or
* an internal deletion/contraction in one of the four rooted halves whose
  equality state agrees with a faithful operation on the opposite half.

No exterior shadow component is available in this spanning normalization.
All dirty paths and owner cores lie inside the six named model bags.

## 7. Atomic support motifs lift to actual full-shore separators

The spanning hypothesis turns the three quotient motifs into genuine
ambient separations.

### Lemma 7.1 (quotient separator amplification)

Let \((D_q:q\in V(Q))\) be a spanning clique-model quotient in a
\(k\)-connected graph \(G\).  Suppose \(S\subseteq V(Q)\) separates
two nonempty connected subgraphs \(Q_1,Q_2\) of \(Q-S\).  Then there is
an inclusion-minimal vertex separator

\[
                         Z\subseteq\bigcup_{s\in S}D_s    \tag{7.1}
\]

between the connected unions \(D(Q_1),D(Q_2)\), and

\[
                         |Z|\ge k.                         \tag{7.2}
\]

Moreover the components \(R_1,R_2\) of \(G-Z\) containing those two
unions satisfy

\[
                         N_G(R_1)=Z=N_G(R_2).              \tag{7.3}
\]

#### Proof

Because the model is spanning, every vertex of \(G\) belongs to a named
bag.  No edge joins bags in different components of \(Q-S\), by the
definition of the quotient.  Hence the union in (7.1) is a separator.
Choose an inclusion-minimal subset \(Z\) which still separates the two
fixed connected unions.  Connectivity gives (7.2).

Let \(R_i\) be the reachable component from the corresponding union in
\(G-Z\).  Its neighbourhood is contained in \(Z\).  If some
\(z\in Z\) had no neighbour in \(R_i\), then restoring \(z\) could not
create a path from that shore to the other fixed union, contradicting
inclusion-minimality of \(Z\).  Thus every member of \(Z\) meets both
reachable shores, proving (7.3). \(\square\)

### Theorem 7.2 (three motifs, two separator orders)

For a failed simultaneous split in the \(HC_7\) cell, the seven pieces
partition \(H=G-v\).  Since the known reduction gives
\(\kappa(G)\ge 7\), the graph \(H\) is six-connected.  Choose an atomic
complement certificate from Lemma 4.4.

1. If it is a missing \(K_3\), the other four quotient bags separate any
   two of the three mutually nonadjacent pieces.
2. If it is a missing path \(v_1v_2v_3v_4\), the four quotient bags
   outside \(\{v_1,v_2,v_3\}\) separate the middle piece \(v_2\) from
   \(v_1\) (and from the component containing \(v_3\)).
3. If it is a missing matching \(3K_2\), the five bags outside the ends
   of any matched nonedge separate those two pieces.

Consequently an actual full-shore separator \(Z\) exists with

\[
 |Z|\ge6,\qquad
 Z\subseteq\text{the union of four named bags in cases 1--2, or five in
 case 3}.                                                \tag{7.4}
\]

In cases 1--2 the portal surplus over one vertex per separator bag is at
least two; in case 3 it is at least one.  In particular some named
separator bag contains at least two vertices of \(Z\).

#### Proof

The asserted quotient separations follow by deleting the listed vertices
from \(K_7-K_3\), \(K_7-P_4\), and \(K_7-3K_2\), respectively.
Additional nonedges in the actual support graph cannot destroy a
separation.  Apply Lemma 7.1 to \(H\) with \(k=6\).  Distributing at
least six separator vertices among four or five named bags gives the
surplus claims. \(\square\)

### Corollary 7.3 (exact adhesion or portal surplus)

If \(|Z|=6\), then \(Z\cup\{v\}\) is an exact seven-vertex adhesion in
\(G\) with two full shores: (7.3) gives the six neighbours in \(H\),
and each shore contains a rooted quotient piece and hence has a neighbour
of \(v\).  Any crossed-splicing argument must align the boundary state on
the full adhesion \(Z\cup\{v\}\), not on \(Z\) alone.

If \(|Z|>6\), the same four- or five-bag separator union contains strict
portal surplus.  A subsequent argument must split a multiply hit
separator bag or turn its locked owner core into a faithful operation
state.  Thus simultaneous-split failure has been lifted from a quotient
mask to exactly the two accepted structural outcomes: an actual adhesion
or a named multiply hit bag.
