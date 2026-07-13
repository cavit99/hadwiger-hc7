# Three-shore block capacity and the web residue

## 1. Setting

Let \(G\) be \(r\)-minor-critical: \(G\) is not \(r\)-colourable,
whereas every proper minor of \(G\) is \(r\)-colourable.  Let \(S\) be
a separator such that

\[
 G-S=D_1\mathbin{\dot\cup}D_2\mathbin{\dot\cup}D_3,
 \qquad N(D_i)=S\quad(i=1,2,3).
\]

Fix a proper colouring partition

\[
 \Pi=A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_p
\]

of \(G[S]\).  For two distinct blocks \(A_h,A_k\), say that a shore
\(D_i\) **doubly realizes** \((A_h,A_k)\) if there are disjoint
connected sets \(X_h,X_k\subseteq D_i\) such that every vertex of
\(A_h\) has a neighbour in \(X_h\), and every vertex of \(A_k\) has a
neighbour in \(X_k\).

The two carriers may always be taken adjacent.  Indeed, take a shortest
\(X_h\)-to-\(X_k\) path in the connected shore \(D_i\), split that path
at one of its edges, and absorb its two halves into the corresponding
carriers.  This preserves disjointness, connectivity, and all prescribed
contacts.

## 2. The capacity theorem

### Theorem 2.1 (three-shore two-block gluing)

Suppose that \(\Pi\) has one of the following forms.

1. \(p=3\), and two distinguished blocks are \(A_2,A_3\).
2. \(p=4\), the block \(A_4=\{s\}\) is a singleton, and
   \(A_1,A_2,A_3\) are the other three blocks.  Moreover \(\Pi\) is an
   optimal colouring of \(G[S]\).

In case 1, if at least two of the shores doubly realize
\((A_2,A_3)\), then \(G\) is \(r\)-colourable.

In case 2, if at least two of the shores each doubly realize some two
distinct members of \(\{A_1,A_2,A_3\}\) (the selected pair may depend
on the shore), then \(G\) is \(r\)-colourable.

#### Proof

Call the two shores with the asserted capacity \(D_a,D_b\).  We show
that the exact labelled partition \(\Pi\) extends over
\(G[S\cup D_i]\) for every \(i\in\{1,2,3\}\).

Fix \(i\).  At least one of \(D_a,D_b\) is different from \(D_i\);
choose such a shore and call it \(R\).  Let \(F\) be the third shore,
different from both \(D_i\) and \(R\).

In case 1, use adjacent disjoint carriers \(X_2,X_3\subseteq R\) for
\(A_2,A_3\), and put

\[
 Q_2=X_2\cup A_2,\qquad
 Q_3=X_3\cup A_3,\qquad
 Q_1=F\cup A_1.
\]

In case 2, suppose that \(R\) realizes \(A_h,A_k\), and let \(A_\ell\)
be the remaining member of \(\{A_1,A_2,A_3\}\).  Put

\[
 Q_h=X_h\cup A_h,\qquad
 Q_k=X_k\cup A_k,\qquad
 Q_\ell=F\cup A_\ell,
\]

and leave \(s\) uncontracted.

All displayed sets are connected and pairwise disjoint.  The two
\(R\)-sets are adjacent by the preliminary observation.  The full shore
\(F\) sees every nonempty boundary block, so its set is adjacent to both
\(R\)-sets.  In case 2, optimality of \(\Pi\) implies that \(s\) has a
neighbour in each of \(A_1,A_2,A_3\): otherwise \(s\) could be merged
with a block and the number of colours reduced.  Hence \(s\) sees both
\(R\)-sets through boundary edges, and it sees the \(F\)-set by
fullness.

Contract the three sets \(Q_j\) and delete every unused vertex outside
\(S\cup D_i\).  In case 1 their images form a \(K_3\); in case 2 their
images together with \(s\) form a \(K_4\).  The resulting graph is a
proper minor of \(G\), so it has an \(r\)-colouring.  Expanding only the
boundary vertices of each contracted set gives a colouring of
\(G[S\cup D_i]\) whose equality partition on \(S\) is exactly \(\Pi\).

This works for all three values of \(i\).  Permute the colour names on
the three side colourings so that corresponding blocks of \(\Pi\) have
the same colour, and glue them.  The shores are pairwise anticomplete,
so the result is an \(r\)-colouring of \(G\), a contradiction. \(\square\)

## 3. The exact \(HC_7\) consequence

Let \(G\) now be a hypothetical proper-minor-minimal counterexample to
\(HC_7\), and let \(S\) be a seven-cut with three components.  The
full-shore block theorem gives exactly two residual optimal colour
patterns:

\[
 (3,2,2)\quad\text{when }\chi(G[S])=3,
 \qquad
 (2,2,2,1)\quad\text{when }\chi(G[S])=4.
\]

Consequently:

* for every optimal \((3,2,2)\)-partition, at most one shore contains
  disjoint connected carriers joining the two two-vertex blocks;
* for every optimal \((2,2,2,1)\)-partition, at most one shore contains
  disjoint connected carriers joining any two of the three two-vertex
  blocks.

Thus at least two shores are simultaneous two-linkage obstructions.
This conclusion is independent of the Moser labels and replaces a
finite quotient list by a capacity deficit.

## 4. Bare-web form of the deficit

Let \(A=\{a_1,a_2\}\) and \(B=\{b_1,b_2\}\) be two of the paired
blocks in one of the preceding colourings, and let \(D\) be a full
shore which does not doubly realize \((A,B)\).  Add four artificial
terminals to \(G[D]\), each adjacent to the portal set of the
corresponding root, and order them

\[
 a_1,b_1,a_2,b_2.
\]

The tuple has no cross: a cross would be precisely two disjoint
carriers for \(A\) and \(B\).  Complete the auxiliary graph, on the same
vertex set, to an edge-maximal graph with no such cross.  The standard
Two Paths Theorem gives a four-web with this terminal frame.

No nonempty set of original shore vertices can lie in a part inserted
behind a facial triangle of the web.  Take all original vertices in the
interior of such an inserted part.  Their neighbours represented in the
auxiliary graph lie among the at most three facial vertices.  Replace
each artificial facial terminal by its corresponding boundary root; this
does not increase the count.  The only original root incidences omitted
from the auxiliary graph go to the other three vertices of \(S\).  Thus
at most six actual vertices separate the nonempty inserted interior from
either of the other nonempty shores, contradicting seven-connectivity.

Therefore every obstructing shore has a bare plane-disk embedding in
which \(a_1,b_1,a_2,b_2\) occur in that cyclic order on one face.  In
particular, a surviving three-shore cut has at least two bare-web shores
for every paired demand specified above.

This is the reusable structural residue:

\[
 \text{two-block capacity}
 \quad\text{or}\quad
 \text{a bare alternating four-terminal web}.
\]

The remaining step is not another boundary atlas.  It is to combine the
simultaneous web orders (or an internal minor transition changing one of
them) into either an additional unit of block capacity or a common exact
boundary state.

## 5. Complete elimination of the \((3,2,2)\) branch

We use the following planar precolouring theorem of Diwan
(*Colouring planar graphs with a precoloured induced cycle*,
arXiv:2306.04944, Corollary 1): if an induced cycle of length at most \(2k-5\) is properly
precoloured with at most \(k-1\) colours, then that precolouring extends
to a \(k\)-colouring of every planar supergraph containing the cycle as
an induced cycle.  We need only \(k=5\) and a four-cycle.

### Theorem 5.1

In a hypothetical proper-minor-minimal counterexample to \(HC_7\), no
seven-cut with three full components can have a three-colourable
boundary.  Equivalently, the \((3,2,2)\) branch is empty.

#### Proof

Suppose that

\[
 S=T\mathbin{\dot\cup}A\mathbin{\dot\cup}B,
 \qquad |T|=3,\quad |A|=|B|=2,
\]

is an optimal three-colouring of \(G[S]\).  By Theorem 2.1, at least
two of the three shores do not contain disjoint carriers for \(A\) and
\(B\).  Call them \(D_1,D_2\), and call the remaining shore \(D_3\).
Section 4 gives, for each \(i\in\{1,2\}\), a plane graph

\[
 H_i^+=G[D_i\cup A\cup B]+E(K_{A,B}),
\]

where \(K_{A,B}\cong K_{2,2}\) is the frame four-cycle.  The cycle is
induced in \(H_i^+\): each of \(A,B\) is independent, and all possible
edges between them are precisely the four frame edges.

Contract the two disjoint connected sets

\[
 Q_0=D_1\cup T,
 \qquad
 Q_1=D_2\cup A,
\]

and delete no vertex of \(D_3\cup B\).  Delete any other unused
vertices.  The two contracted images \(q_0,q_1\) are adjacent, since
the full shore \(D_1\) sees every vertex of \(A\).  Moreover each
\(q_j\) is adjacent to both vertices of \(B\), by fullness of the shore
it contains.  This is a proper minor and therefore has a six-colouring.

Expand only the retained boundary vertices and keep the colouring on
\(D_3\).  We obtain a proper six-colouring \(c\) of
\(G[S\cup D_3]\) with the following properties:

* all vertices of \(T\) have one colour, say \(0\);
* both vertices of \(A\) have a second colour, say \(1\);
* each vertex of \(B\) has a colour different from both \(0\) and
  \(1\).

For \(i=1,2\), precolour the induced frame cycle of \(H_i^+\) by the
restriction of \(c\) to \(A\cup B\).  This is proper even on the added
frame edges: every vertex of \(A\) has colour \(1\), whereas neither
vertex of \(B\) does.  It uses only colours from the five-colour palette
\(\{1,2,3,4,5\}\).  Diwan's theorem extends it to a five-colouring of
all of \(H_i^+\).

Use these two extensions on \(D_1,D_2\), and use \(c\) on
\(S\cup D_3\).  They agree on \(A\cup B\).  Every vertex of
\(D_1\cup D_2\) avoids colour \(0\), so all its edges to the
colour-\(0\) set \(T\) are proper.  Distinct shores are anticomplete,
and every remaining boundary edge was already proper under \(c\).
The three colourings therefore combine to a six-colouring of \(G\), a
contradiction. \(\square\)

### Corollary 5.2

Every three-component seven-cut in a hypothetical \(HC_7\)
counterexample has a four-chromatic boundary.  By the audited
seven-vertex support classification and the clique-residual block
theorem, that boundary is the pure Moser spindle.  Thus all
multi-component minimum-cut geometry has converged to the same single
seven-vertex core that arose independently from the degree-seven
neighbourhood analysis.

The proof of Theorem 5.1 is label-free.  Its mechanism is the reusable
chain

\[
 \text{block-capacity failure}
 \Longrightarrow
 \text{two bare webs}
 \Longrightarrow
 \text{force one omitted block and one frame block in a minor}
 \Longrightarrow
 \text{safe planar precolouring extension}.
\]

## 6. Four-colour Helly closure for three web shores

The companion theorem
`hadwiger_facial_c4_three_pattern_theorem.md` proves the following
consequence of the Four Colour Theorem and a Kempe-chain count identity:
for a plane graph with an induced facial four-cycle, at least three of
the four possible boundary equality patterns extend to a four-colouring.
Therefore three plane disks with the same labelled facial frame have a
common extendable pattern, since each omits at most one element of a
four-element set.

### Theorem 6.1 (three-web closure)

Let \(S\) be a seven-vertex boundary with three full shores.  Suppose
that

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}Z,
 \qquad |A|=|B|=2,
\]

where \(A,B\) are independent and \(G[Z]\) is bipartite.  If none of
the three shores contains disjoint carriers for \(A\) and \(B\), then
\(G\) is six-colourable.

#### Proof

Section 4 turns all three shores into plane disks with the same labelled
induced facial frame \(K_{A,B}\cong C_4\).  By the facial-four-cycle
three-pattern theorem, choose one boundary equality pattern which
extends to a four-colouring of every disk.  Permute the four colours so
that the three disk colourings agree at each of the four labelled frame
vertices, and glue them.  This gives a four-colouring of

\[
 G\bigl[(D_1\cup D_2\cup D_3)\cup A\cup B\bigr].
\]

Colour the bipartite graph \(G[Z]\) with two fresh colours.  Every edge
between \(Z\) and the four-coloured graph has differently coloured ends
because the palettes are disjoint.  This is a six-colouring of \(G\).
\(\square\)

### Corollary 6.2 (unique capacity owner)

For every optimal \((2,2,2,1)\)-partition

\[
 S=A_1\mathbin{\dot\cup}A_2\mathbin{\dot\cup}A_3
   \mathbin{\dot\cup}\{s\}
\]

of a surviving three-shore boundary, exactly one shore doubly realizes
some two of \(A_1,A_2,A_3\).

#### Proof

At most one shore has this capacity by Theorem 2.1.  If no shore had
it, fix any two paired blocks, say \(A_1,A_2\).  All three shores would
be crossless for that demand, while

\[
 Z=A_3\cup\{s\}
\]

is bipartite.  (The pair \(A_3\) is independent, so adjoining one
vertex cannot create an odd cycle.)  Theorem 6.1 would six-colour
\(G\), a contradiction. \(\square\)

For the pure Moser boundary, Corollary 6.2 assigns every one of its
sixteen optimal \((2,2,2,1)\)-partitions to a unique exterior shore.
This is the exact analogue of frame ownership in the \(C_6\) laboratory.
The remaining Moser task is to prove that one shore cannot own the
resulting family of crossing demands without either gaining a third
capacity unit or producing a portal separator whose equality state
glues.

## 7. Exact obstruction to the unrestricted planar argument

### Lemma 7.1 (arbitrary six-precolouring of two glued four-webs)

Let two bare web shores have the same paired frame
\(K_{A,B}\cong C_4\).  Every proper six-colouring of that frame extends
simultaneously over the union of the two shores and the frame.

#### Proof

Embed the two web disks on opposite sides of their common frame.  Their
union is planar, and the frame remains an induced four-cycle because the
two parts \(A,B\) are independent.  The frame precolouring uses at most
four colours.  Diwan's Corollary 1 with \(k=6\) applies, since
\(4\le2k-5=7\) and \(4\le k-1=5\). \(\square\)

This lemma answers the unrestricted facial-cycle extension question
affirmatively.  Its limitation is not the interaction between the two
web disks; it is the portal edges to the three roots omitted from the
frame.

In the standard Moser labelling, one optimal boundary partition is

\[
 \{1,3\}\mid\{2,5\}\mid\{4,6\}\mid\{0\}.       \tag{6.1}
\]

Theorem 2.1 says that at least two shores fail all three paired
two-linkages.  Thus each of those shores has a bare four-web for every
choice of two pair blocks.  However, the last step of Theorem 5.1 does
not extend formally.

For one four-web, the omitted boundary consists of a pair block and the
singleton.  These two blocks are adjacent and require two different
reserved colours.  Only four colours then remain for the induced frame
four-cycle.  This cannot be repaired by a universal planar-extension
claim: Diwan proves that no proper four-colouring of a cycle of length at
least four is safe.

There is a second, equally sharp obstruction.  The three pair blocks in
(6.1) are antipodal in the cyclic order

\[
 1,2,4,3,5,6.                                    \tag{6.2}
\]

Even if the three web orders in a shore could be synchronized into this
single six-terminal disk, reserving the singleton colour would leave a
five-colour precolouring of the frame with cyclic word

\[
 A\,B\,C\,A\,B\,C.                               \tag{6.3}
\]

This precolouring is not safe.  In Diwan's notation, take the three arcs
from positions \(1\) to \(3\), \(3\) to \(5\), and \(5\) back to
\(1\).  Each arc contains all three colours, so their common colour set
has order \(3=k-2\).  Lemma 1 of the cited paper gives an explicit planar
obstruction: add a triangle \(u_1u_2u_3\), and make \(u_i\) adjacent to
the vertices on the corresponding one of those three cyclic arcs.  No
five-colouring extends (6.3).

An arbitrary proper six-colouring of the induced frame four-cycle *is*
safe by Diwan's corollary with \(k=6\).  That fact alone does not colour
the original shore together with the three omitted roots: the planar
extension may use an omitted root's colour on one of its actual portal
neighbours.  Fullness guarantees such portal edges rather than removing
them.

Hence the pure-Moser three-shore residue needs additional information
about portal-specific forbidden colours or a minor-critical state
transition.  Bare planarity plus an unrestricted precolouring-extension
theorem is provably insufficient.
