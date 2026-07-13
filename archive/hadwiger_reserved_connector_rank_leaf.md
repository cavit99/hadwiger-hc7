# Rank-one web leaves in the Moser reserved-connector shore

## 1. Relative-shore setting

In the sharp order-six reserved-connector cell, one terminal side has a
connected shore \(D\) with all its neighbours in

\[
 D\cup L,\qquad |L|=7,
\]

where \(L=S\cup\{a\}\) or \(S\cup\{b\}\).  It is full to \(L\), has
order at least six, and seven-connectivity gives

\[
 |N_D(X)-X|+|N_L(X)|\ge7                         \tag{1.1}
\]

for every nonempty proper \(X\subsetneq D\).

Let \(Q=\{q_0,q_1,q_2,q_3\}\subseteq L\).  Add four independent
artificial terminals, terminal \(i\) adjacent to the full portal set

\[
 P_i=N_D(q_i).
\]

Order them as \((q_0,q_1,q_2,q_3)\), and call the society crossless if
there are no disjoint \(P_0\)-\(P_2\) and
\(P_1\)-\(P_3\) paths in \(D\).

## 2. Hall and the bare web

### Lemma 2.1 (four distinct portals)

The four portal sets \(P_0,\ldots,P_3\) have an SDR.

### Proof

If Hall fails for \(I\subseteq\{0,1,2,3\}\), put

\[
 R=\bigcup_{i\in I}P_i,\qquad |R|<|I|.
\]

If \(D-R\ne\varnothing\), a component \(C\) of \(D-R\) satisfies

\[
 N_G(C)\subseteq R\cup(L-\{q_i:i\in I\}),
\]

whose order is at most

\[
 (|I|-1)+(7-|I|)=6,
\]

contrary to (1.1).  Hence \(D=R\) and \(|D|\le3\), contrary to the
installed bound \(|D|\ge6\). \(\square\)

### Lemma 2.2 (relative bare web)

If the four-terminal society is crossless, then \(D\) has a plane
embedding in which all four full portal sets lie on one face.

### Proof

The generalized Two Paths Theorem embeds the society in a same-vertex
web.  A nonempty clique part behind a facial triangle has at most three
neighbours in the society.  Replace any artificial terminal among those
neighbours by its boundary label, and add the three labels of \(L-Q\).
The resulting set has order at most six and separates the clique part
from the opposite terminal side, contradicting (1.1).  Thus the web is
a bare planar rib.  Deleting the four frame terminals merges the outer
face with their incident faces, placing every vertex of every \(P_i\) on
one face of \(D\). \(\square\)

## 3. The orientation-free rank-one leaf

Call a one- or two-separation **facially flippable** if the common portal
face meets both interiors and a Whitney flip of either interior preserves a
single face containing all four portal sets.  (If the face misses one
interior, that interior already has portal rank zero.)  This is the precise
notion supplied by an SPQR leaf whose poles occur on the portal face; an
arbitrary separation of the abstract shore need not have this property.

### Theorem 3.1 (relative web leaf)

Assume the society is crossless.  Let a proper one- or two-separation of
\(D\) be facially flippable in the plane embedding of Lemma 2.2, with separator
\(Z\), \(|Z|\le2\), and connected nonempty interiors \(X,Y\).  Then one
of \(X,Y\) is a singleton.  More precisely, the portal incidence graph
on that interior has matching number at most one.

### Proof

Choose any SDR of the four portal sets on the common face.  Reflect the
\(X\)-side of the separation.  Its representatives form one contiguous
block in the facial order, and the reflection reverses that block while,
by facial flippability, leaving all four full portal sets on one face.  Four
distinct representatives of a crossless frame must alternate: otherwise
two disjoint arcs of the facial cycle give the forbidden linkage.  Reversing a block
containing exactly two of them destroys alternation, whereas the reflected
embedding is still a common-face embedding of the same crossless society.
Thus no SDR uses exactly two representatives in \(X\).

The possible values \(|B\cap X|\), over all bases \(B\) of the
rank-four portal transversal matroid, form an integer interval.  Hence
either \(r(X)\le1\) or \(r(D-X)\le1\).  In the latter case
\(r(Y)\le1\).  Let \(K\in\{X,Y\}\) be the corresponding low-rank
interior.

By König's theorem, one vertex covers every incidence between \(K\) and
the four represented boundary labels.  If the cover is a boundary
label \(q\), then

\[
 N_G(K)\subseteq Z\cup(L-Q)\cup\{q\},
\]

of order at most \(2+3+1=6\), contradicting (1.1).  If the cover is a
shore vertex \(x\in K\) and \(K-\{x\}\ne\varnothing\), a component
\(C\) of \(K-x\) satisfies

\[
 N_G(C)\subseteq Z\cup(L-Q)\cup\{x\},
\]

again of order at most six.  Therefore \(K=\{x\}\). \(\square\)

This conclusion does not orient an SPQR leaf: the singleton may be on
either displayed side.  That orientation error is exactly the one
removed from the \(C_6\) proof.

## 4. Minimal-shore consequence

Choose a minimum-order relative shore satisfying (1.1), full attachment,
and having no target \(N(v)\)-meeting \(K_6\)-model.  If a crossless
frame exposes a singleton two-separation side \(\{x\}\), with shore
neighbours \(p,q\), then for each incident edge \(xp,xq\), Corollary 2.2
of `hadwiger_relative_shore_contraction.md` gives the following exact
dichotomy:

1. the edge joins two neighbours of the terminal while the terminal
   degree inequality is tight; or
2. there is a nonempty proper \(Y\subseteq D\) with relative boundary
   exactly seven, and both ends of the edge lie in \(N_D(Y)\).

Otherwise the edge can be contracted, the smaller shore has the target
model by minimality, and expanding the contracted pair lifts the model.

Thus a crossless web cannot hide arbitrary unbounded SPQR geometry.  It
ends either in a terminal-tight ear or in an exact order-seven separator,
whose components are themselves full shores for the new adhesion.  This
is the promised unbounded portal-concentration/next-rung invariant; it
uses no order enumeration.

## 5. Five-cycle synchronization

For the pure-Moser trace \(a b=13\), the five root portals are

\[
 U=\{0,2,4,5,6\},
\]

and their missing-edge graph is a \(C_5\).  Its five **frames** are the
pairs of vertex-disjoint missing-cycle edges.  If a three-connected shore
is crossless for three frames, Whitney uniqueness lets us compare the three
bare-web embeddings.  Their associated portal faces coincide:
two distinct frames share three portal classes, and the five portal sets
have an SDR by the Hall proof above (with two permanently omitted labels
in \(L\)); distinct faces of a three-connected plane graph cannot share
three distinct vertices.

On that common face the SDR order must satisfy three alternating
four-point constraints.  Exhausting the \(4!=24\) oriented circular
orders shows that the only orders satisfying at least three frames are

\[
 0,2,4,1,3
 \quad\text{and its reverse}                      \tag{5.1}
\]

after cyclic relabelling of the missing \(C_5\).  These are the two
pentagram orders.  The tiny SDR check is
`moser_c5_crossless_order_probe.py`.

The occurrence-level strengthening below removes the former qualification
that this was only an order constraint.

### Theorem 5.1 (three crossless frames force all five)

In the three-connected common-face shore above, if any three of the five
missing-cycle frames are crossless, then all five frames are crossless.

#### Proof

Fix an SDR on the common facial cycle.  Its order is one of the two
pentagram orders in (5.1).  Suppose one of the remaining frames has
vertex-disjoint connected supports.  Choose two facial attachments for
each support.  Attachments within one support may coincide; attachments
belonging to the two disjoint supports cannot coincide.  If all four are
distinct, the two pairs are nonalternating on the facial cycle, since two
disjoint connected subgraphs in a disk cannot join alternating pairs.

For each of the three crossless frames, choose arbitrarily one occurrence
from each of its four portal classes, using either an SDR occurrence or one
of the four new support occurrences.  Whenever the two demanded pairs are
disjoint, crosslessness has the following exact disk consequence:

* neither pair can collapse to one occurrence, since that singleton and a
  facial arc joining the other pair would be disjoint supports; and
* the four occurrences must alternate, since otherwise two disjoint facial
  arcs join the demanded pairs.

These necessary circular constraints are inconsistent.  There are ten
choices of the three crossless frames.  Each permits exactly the two
pentagram SDR orders, and there are two choices for the proposed remaining
linked frame.  The forty resulting weak circular-order systems are all
unsatisfiable.  The verifier
`moser_c5_three_crossless_exact_probe.py` constructs the constraints rather
than taking the pentagram conclusion as an input; it allows every
coincidence not excluded by genuine disjointness and prints

    checked 40 satisfiable 0.

Every real disk configuration induces one of these weak circular orders,
so no remaining linked frame exists. \(\square\)

Thus the three-connected residual is a single all-crossless pentagram web,
not five separate frame cases.  This is a genuine structural cell, not a
generic rooted \(K_5\) problem.

## 6. Exact finite-state obstruction: the \(w\)-coordinate

The supported-pair transfer labels a frame crossed in one shore with the
triple equality state \(T_{ij}=\{13,e_i,e_j\}\) on the opposite side.
For the order-six separator, however, the adhesion also contains
\(w\).  The undecorated state \(T_{ij}\) has five possible equality
positions for \(w\): it may join one of the four colour blocks

\[
 13,\quad e_i,\quad e_j,\quad\{r\},
\]

when independence permits, or be a new singleton block.  Exact-state
exclusivity applies only after this \(w\)-coordinate is fixed.

Consequently the supported-pair and two-anchor axioms alone do **not**
force crossing ownership.  Even if the same frame is crossed in both
shores, transfer may put two different decorated \(T_{ij}\)-states on
the opposite sides.  Abstractly, one side may admit only the singleton
\(w\)-state and the other only a root-sharing state, while all
undecorated coverage constraints remain satisfied.

The exact missing local statement is therefore:

> **Bilateral \(w\)-state overlap lemma.**  If the same disjoint pair of
> missing \(C_5\) edges is linked in both full relative shores, then
> some common decorated \(T_{ij}\)-state extends to both sides.

This lemma would close that frame by exact-state gluing.  It would also
make the two shores' crossed-frame sets disjoint; among five frames one
shore would then be crossless for at least three.  Sections 3--5 would
reduce that shore to a pentagram three-connected core, a terminal-tight
ear, or an exact new seven-adhesion.

Without the \(w\)-state overlap lemma, no ownership conclusion is valid.
This is the precise remaining gap in transplanting the completed
\(C_6\) mechanism to the reserved-connector cell.

## 7. A geometric certificate for the singleton \(w\)-state

The five decorations in Section 6 distinguish equality with the terminal
colour \(13\) from a genuinely new singleton colour.  The latter has a
particularly concrete branch-set certificate.

Fix one shore with terminal \(a\), a frame consisting of disjoint missing
root edges \(e,f\), and leftover root \(r\).  Suppose the supported paths
and a split shortest connector have produced disjoint connected adjacent
sets \(E,F\), with

\[
 E\cap S=e,\qquad F\cap S=f.
\]

Call a connected set \(W\) a **singleton \(w\)-absorber** if

\[
 W\cap S=\{w\},\qquad
 W\cap(E\cup F\cup\{r,a\})=\varnothing,
\]

and \(W\) is adjacent to each of \(E,F,\{r\},\{a\}\).

### Lemma 7.1 (bilateral absorber exclusion)

The same frame cannot have a singleton \(w\)-absorber in both terminal
shores.

### Proof

On either side the four sets

\[
 E,\quad F,\quad\{r\},\quad W
\]

are disjoint, connected and pairwise adjacent.  The first three pairwise
adjacencies are the supported-pair construction and the Moser boundary
edges: the root left outside two disjoint missing-cycle edges has a
neighbour in each edge.  The definition of \(W\) supplies the remaining
adjacencies.  Their traces on \(S\) are the same four independent blocks

\[
 e\mid f\mid\{r\}\mid\{w\}.
\]

The first three blocks meet \(U\); the fourth is portal-only and is
adjacent to the star through its edge to the terminal.  Thus Corollary 2.3
of `hadwiger_reserved_connector_portal_transfer.md` applies to bilateral
absorbers and six-colours \(G\), a contradiction. \(\square\)

For fixed \(E,F\), absorber existence has an exact component formulation.
Delete their shore vertices from \(D\), and let \(R_w\) be the union of
all remaining components having a neighbour at \(w\).  (The union may be
empty.)  Then \(\{w\}\cup R_w\) is connected, and an absorber exists
precisely when this maximal \(w\)-region is adjacent to all four targets

\[
 E,\quad F,\quad r,quad a.                         \tag{7.1}
\]

(Direct edges from \(w\) count in (7.1), including the possibility
\(R_w=\varnothing\).)  Conversely, every absorber lies in
\(\{w\}\cup R_w\) and can be enlarged to that set.  Hence failure of the
singleton state is no longer an abstract colouring event: the union of
the contact signatures of all \(w\)-components of \(D-(E\cup F)\),
together with the direct contacts of \(w\), misses at least one of the four
target classes in (7.1).  This four-target signature is the precise input
needed by a Two Paths web or portal-order argument.
