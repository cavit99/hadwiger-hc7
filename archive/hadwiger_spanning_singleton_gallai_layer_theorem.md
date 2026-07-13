# Spanning one-complex-bag cells: Gallai layers and the exact owner corridor

## Status

This note treats the valid coexistence cell omitted by simultaneous
bag-contraction arguments: all bags except one are already singleton, and
the model is spanning after deleting the apex.  Here a contraction of the
complex bag both labels the singleton bags and forces a genuine
unexpandable list core.

Three new conclusions are proved.

1. In a minimal Gallai equality core, a Kempe layer whose second colour is
   outside the current block palette must hit the correspondingly labelled
   singleton bag.  The exact exception is an internal clique/odd-cycle
   detour using two colours of the same block palette, or the apex colour.
2. If the complex bag is a tree, every contraction-colour matching edge
   splits it into two connected pieces meeting every singleton portal except
   possibly the apex-selected noncontact portal.  Either that last portal
   also occurs on both sides, giving the target clique minor, or every leaf
   is an apex foot and the exceptional portal lies in one component of the
   tree after deleting the matching.
3. The whole equality-tree cell closes, and so does every equality Gallai
   core in which the contraction colour occurs only on \(K_2\)-blocks.
   Deleting the resulting matching and contracting its components gives a
   quotient in which component size equals quotient degree.  Branching
   yields an explicit three-piece \(K_{r+1}\)-model; without branching the bag is a path, whose sole
   constant-label exception is eliminated by changing the quotient colour
   of the apex.

In particular, the exact alternating owner corridor can be closed.  In the
spanning singleton cell its equality lists force every ordinary portal at
every corridor vertex, force all internal vertices away from both the apex
and the selected portal, and leave the selected portal at exactly one end.
Three explicit corridor-derived branch sets then complete the target
minor.  Theorems 3.5 and 3.6 go further and eliminate every spanning
singleton equality-tree society, and indeed every matching-\(\alpha\)
Gallai society, without first converting it to that corridor.

## 1. Setup

Let \(r\ge3\).  Let \(G\) be non-\(r\)-colourable and suppose every proper
minor of \(G\) is \(r\)-colourable.  Fix \(v\in V(G)\), put \(H=G-v\), and
assume

\[
                         V(H)=V(B)\mathbin{\dot\cup}S,
 \qquad S=\{b_1,\ldots,b_{r-1}\},                       \tag{1.1}
\]

where \(S\) is a clique, \(B\) is connected and induced, and

\[
                         (B,\{b_1\},\ldots,\{b_{r-1}\}) \tag{1.2}
\]

is a \(K_r\)-model.  Thus every portal class

\[
                         P_i=N_B(b_i)                    \tag{1.3}
\]

is nonempty.  Put \(F=N_B(v)\), and assume \(|F|\ge2\).

Contract \(B\) to \(z\) and \(r\)-colour the proper minor.  Write

\[
 c(z)=\alpha,\qquad c(b_i)=p_i,\qquad c(v)=p_j=\delta.  \tag{1.4}
\]

The selected bag \(b_j\) is noncontact.  For \(x\in B\), the expansion
list is exactly

\[
 L(x)=\{\alpha\}\cup
 \{p_i:x\notin P_i\text{ and }(i\ne j\text{ or }x\notin F)\}. \tag{1.5}
\]

There are no shadow blockers: outside \(B\) there are only the singleton
bags and \(v\).  Since expansion would colour \(G\), \(B\) is not
\(L\)-colourable.

Assume in Sections 2--4 that \(B\) is itself an inclusion-minimal
uncolourable equality core.  Hence \(|L(x)|=d_B(x)\), and the standard
degree-list theorem represents \(B\) as a Gallai tree with block palettes
\(C_K\).  The colour \(\alpha\) belongs to exactly one incident block
palette at every vertex.

For every edge \(e=xy\) in a block \(K\), the aligned Gallai transition
colours \(G-e\), agrees with \(c\) outside \(B\), and gives

\[
                         c_e(x)=c_e(y)=\beta\in C_K.     \tag{1.6}
\]

## 2. Which Kempe layers hit their labelled singleton?

### Theorem 2.1 (block-palette shadow theorem)

Fix the transition (1.6) and a model colour \(\gamma=p_i\ne\beta\).

1. If

   \[
                \gamma\notin C_K,\qquad
                \beta\ne\delta,\qquad\gamma\ne\delta,   \tag{2.1}
   \]

   then the \(\{\beta,\gamma\}\)-component containing \(x,y\) contains
   \(b_i\).  If \(\beta=p_k\) is also a model colour, it contains both
   \(b_i,b_k\).
2. If \(\gamma\in C_K\), the component already has an \(x\)-to-\(y\)
   detour wholly in \(K-e\).  Thus no contact with \(b_i\) is forced.
3. If either colour is \(\delta=c(v)\), an \(x\)-to-\(y\) layer may use
   \(v\) instead of the singleton bag.  This is the apex-transit exception.

#### Proof

In every \(r\)-colouring of \(G-e\), the ends \(x,y\), which have the same
colour \(\beta\), lie in the same \(\{\beta,\gamma\}\)-component.  Otherwise
switching one endpoint component makes the ends different and restores
\(e\), colouring \(G\).

Suppose (2.1) holds.  In the canonical colouring of the root block \(K-e\),
no vertex of \(K\) has colour \(\gamma\).  Its two \(\beta\)-coloured
endpoints cannot be joined by a \(\{\beta,\gamma\}\)-path inside \(K-e\).
Nor can a path leave one vertex of a block and return at a different vertex
through the rest of a Gallai tree: that would create an external path
between two vertices of one block, contradicting maximality of the block.
Hence the endpoint component must leave \(B\).

The graph is spanning as in (1.1), and \(v\) is unavailable under (2.1).
Among the singleton vertices, the only one of colour \(\gamma\) is \(b_i\);
if \(\beta=p_k\), the only singleton of colour \(\beta\) is \(b_k\).
Thus the component contains \(b_i\).  In the latter case the clique edge
\(b_ib_k\) puts both in the same component.

If \(K\) is a clique and \(\gamma\in C_K-\{\beta\}\), the unique vertex
of colour \(\gamma\) in the standard colouring of \(K-e\) is adjacent to
both ends.  If \(K\) is an odd cycle, its palette is
\(\{\beta,\gamma\}\), and \(K-e\) is the required alternating path.  This
proves part 2.  Part 3 follows because \(v\) is the additional singleton
vertex in the corresponding two-colour subgraph. \(\square\)

The theorem is the exact answer to the Kempe-layer packaging question.
Gallai structure does not make every layer hit a portal label.  The
preventing pattern is not an arbitrary shadow vertex in this spanning
cell; it is precisely a block-palette colour whose clique or odd cycle
supplies an internal detour.  The apex colour is the only external shadow.

### Corollary 2.2 (two separated carriers cannot both inherit one label)

Suppose a simultaneous-operation lock gives distinct
\(\{\beta,p_i\}\)-components at the two ends of an edge.  At most one of
those components contains the unique singleton \(b_i\).  Therefore the
Kempe-layer union lemma does not turn the two components into two
\(i\)-portal carriers.

The component missing \(b_i\) can meet a marked gate only through

1. a \(p_i\)-coloured vertex of \(B\), which is automatically outside
   \(P_i\);
2. a \(\beta\)-coloured vertex with no edge to \(b_i\); or
3. \(v\), when one of the two colours is \(\delta\).

These are the exact spanning-cell shadows.  If unions of separated endpoint
components intersect, the layer-union lemma gives a multicolour detour.  If
the unions stay disjoint, they are adjacent connected carriers, but the
preceding list shows why their gate hits need not be prescribed portal
labels.  Additional portal capacity, not Gallai incidence alone, is needed
to label both carriers.

## 3. Contraction-colour bridge blocks split all ordinary labels

Let \(e=xy\) be a \(K_2\)-block whose palette is \(\{\alpha\}\).  Then
\(e\) is a bridge of \(B\).  Write \(A,D\) for the two components of
\(B-e\).

### Theorem 3.1 (alpha-bridge contact dichotomy)

For every \(i\ne j\),

\[
                         A\cap P_i\ne\varnothing,\qquad
                         D\cap P_i\ne\varnothing.        \tag{3.1}
\]

For the selected noncontact label \(j\), at least one of the following
holds:

\[
\begin{array}{ll}
\text{portal crossing:}&A\cap P_j\ne\varnothing
                         \text{ and }D\cap P_j\ne\varnothing;\\
\text{foot crossing:}&A\cap F\ne\varnothing
                         \text{ and }D\cap F\ne\varnothing.
\end{array}                                               \tag{3.2}
\]

If portal crossing holds, \(G\) contains a \(K_{r+1}\)-minor.

#### Proof

Use the canonical colouring of \(G-e\), whose ends both have colour
\(\alpha\).  For \(i\ne j\), the \(\{\alpha,p_i\}\)-component joins the
two ends and avoids \(v\).  Since \(B-e\) has the two components \(A,D\)
and the only outside vertex with either colour is \(b_i\), the connecting
component must use \(b_i\), with a neighbour in each side.  This is (3.1).

For \(i=j\), the only outside vertices in the two-colour layer are
\(b_j\) and \(v\), both of colour \(p_j\) and nonadjacent to one another.
After contracting the portions of the layer in \(A,D\), a connection
between the two sides must have one of \(b_j,v\) adjacent to both sides.
These are exactly the two alternatives in (3.2).

Under portal crossing, both connected sets \(A,D\) meet every \(P_i\).
At least one contains a foot; call it \(A\).  The branch sets

\[
                         A\cup\{v\},\quad D,\quad
                         \{b_1\},\ldots,\{b_{r-1}\}
                                                               \tag{3.3}
\]

form a \(K_{r+1}\)-model. \(\square\)

### Corollary 3.2 (the exact spanning-tree residue)

Suppose \(B\) is a tree.  Its \(\alpha\)-edges form a perfect matching
\(M_\alpha\).  Either \(G\) has a \(K_{r+1}\)-minor, or

1. every leaf of \(B\) belongs to \(F\); and
2. the entire portal class \(P_j\) lies in one component of
   \(B-M_\alpha\).

#### Proof

If any matching edge has portal crossing, Theorem 3.1 gives the minor.
Otherwise every matching edge has foot crossing.  A leaf edge is labelled
\(\alpha\), and one side of its deletion is the singleton leaf; hence every
leaf is a foot.

If two \(P_j\)-vertices lay in different components of
\(B-M_\alpha\), their tree path would contain a matching edge, putting
\(P_j\) on both sides of that edge.  This would be portal crossing.
\(\square\)

Thus the surviving tree is an alternating owner corridor: all terminal
leaves are apex feet, and every portal to the apex-selected noncontact bag
is confined between matching cuts.  This is exactly the colour layer which
cannot be forced through a singleton bag because it may use \(v\).

### Theorem 3.3 (noncontact foot sets form an antichain)

Let \(J\) be the set of noncontact singleton labels, and for \(i\in J\)
put

\[
                              F_i=F\cap P_i.             \tag{3.4}
\]

Under the equality-core hypothesis for one selected \(j\in J\), there is
no \(k\in J\) with

\[
                              F_j\subsetneq F_k.          \tag{3.5}
\]

#### Proof

The quotient \(G/B\) may be coloured with \(v\) receiving \(p_k\) for any
noncontact \(k\).  Let \(L_k\) be the corresponding expansion lists.
Outside the foot set, \(L_k=L_j\).  At a foot \(x\),

\[
 |L_k(x)|-|L_j(x)|
   ={\bf1}_{x\notin P_j}-{\bf1}_{x\notin P_k}.           \tag{3.6}
\]

If (3.5) holds, then \(L_k(x)\supseteq L_j(x)\) at every vertex, with a
strict inclusion at a foot in \(F_k-F_j\).  Since
\(|L_j(x)|=d_B(x)\), the standard greedy degree-list lemma colours a
connected graph whenever every list has order at least its degree and one
list is larger.  Hence \(B\) is \(L_k\)-colourable, expanding the quotient
colouring to an \(r\)-colouring of \(G\), a contradiction. \(\square\)

Thus a second noncontact label does not automatically close the owner
corridor, but it must have a foot-incidence pattern incomparable with that
of the selected owner.  In particular, every other noncontact label whose
portal set contains all leaf feet forces a compensating internal foot in
\(P_j-P_k\).

### Theorem 3.4 (the alternating owner corridor closes)

Suppose (B) is a tree and every edge outside its \(\alpha\)-perfect
matching has label \(\delta=p_j\).  Then (G) contains a
\(K_{r+1}\)-minor.

#### Proof

Properness of the edge labelling and the fact that every vertex is incident
with one \(\alpha\)-edge imply that (B) has maximum degree at most two.
Thus, writing its vertices in order,

\[
 B=x_0x_1\cdots x_{2m-1},
 \qquad
 \lambda(x_{2q}x_{2q+1})=\alpha,
 \quad
 \lambda(x_{2q+1}x_{2q+2})=\delta .                    \tag{3.7}
\]

If \(m=1\), this is the single-block case closed in Proposition 4.1, so
assume \(m\ge2\).

For every ordinary model label \(i\ne j\), the colour \(p_i\) occurs in
no list on the path.  Formula (1.5) therefore gives

\[
                         V(B)\subseteq P_i
                         \qquad(i\ne j).                 \tag{3.8}
\]

Every internal vertex has list \(\{\alpha,\delta\}\).  By (1.5), the
presence of \(\delta=p_j\) in this list says that the vertex is neither a
foot nor a member of \(P_j\).  Corollary 3.2 says that the two leaves
\(x_0,x_{2m-1}\) are feet.  Since \(P_j\ne\varnothing\), it consequently
meets at least one endpoint.  It cannot meet both: after deletion of the
\(\alpha\)-matching the two endpoints are distinct singleton components,
contrary to Corollary 3.2.  Reverse the path if necessary so that

\[
                         x_0\in P_j,
 \qquad                   x_{2m-1}\notin P_j.            \tag{3.9}
\]

Now take the following disjoint connected branch sets:

\[
 \{v,x_{2m-1}\},\qquad
 \{x_0,b_j\},\qquad
 \{x_1,\ldots,x_{2m-2}\},\qquad
 \{b_i\}\ (i\ne j).                                    \tag{3.10}
\]

The first set is connected because the last endpoint is a foot; the second
because \(x_0\in P_j\); and the third is a nonempty path.  The first and
third, and the second and third, are adjacent through the two end edges of
(B).  The first and second are adjacent through the edge \(vx_0\), since
\(x_0\) is also a foot.  Formula (3.8) makes each of the first three sets
adjacent to every singleton \(b_i\), \(i\ne j\), while those singleton
sets are pairwise adjacent and are adjacent to the set containing \(b_j\).
Thus (3.10) is a \(K_{r+1}\)-model. \(\square\)

This proof uses no corridor-length case analysis.  It also explains why
the static four-vertex corridor is not an obstruction once full
minor-criticality and the exact spanning singleton society are imposed:
its two end owners themselves furnish two of the three new branch sets.

### Theorem 3.5 (uniform spanning singleton tree theorem)

If the full equality core (B) is a tree, then (G) contains a
(K_{r+1})-minor.

#### Proof

Suppose otherwise.  Let (M_\alpha) be the perfect matching of
(\alpha)-labelled edges and contract every component of
(B-M_\alpha) to one vertex.  The resulting graph (R) is a tree.  If
(C) is one of the contracted components, then

\[
                              d_R(C)=|C|.                \tag{3.11}
\]

Indeed, every vertex of (C) has exactly one incident
(\alpha)-edge, all these edges leave (C), and two of them cannot join
(C) to the same other component without creating a cycle in (B).

By Corollary 3.2, (P_j) is contained in one component (Q) of
(B-M_\alpha).  Root (R) at (Q).  Suppose some vertex of (R) has
two children, and let (e_1,e_2) be the corresponding
(\alpha)-edges of (B).  Deleting them gives two child-side components
(A,D) and a third component (C) containing (Q).  Since we have
assumed that the target minor does not exist, Theorem 3.1 says that each
of (A,D) contains a foot and meets every (P_i), (i\ne j).  The set
(C) meets (P_j).  Hence

\[
 A\cup\{v\},\qquad D,\qquad C\cup\{b_j\},\qquad
 \{b_i\}\ (i\ne j)                                    \tag{3.12}
\]

are pairwise adjacent connected branch sets: the two deleted edges join
(C) to (A,D), and a foot in (D) joins (D) to the first set.
The ordinary portal crossings and the clique on the singleton bags give
all remaining adjacencies.  This is a (K_{r+1})-model, a contradiction.

Consequently every vertex of the rooted tree (R) has at most one child.
Thus (R) is a path and (Q) is an endpoint.  Formula (3.11) says that
the endpoint components have one vertex and every internal component has
two vertices.  It follows that (B) itself is a path

\[
 x_0x_1\cdots x_{2m-1}                                 \tag{3.13}
\]

whose end edges and alternate edges have label \(\alpha\); write
(\beta_q\) for the label of (x_{2q-1}x_{2q}).  Moreover

\[
                              P_j=\{x_0\},               \tag{3.14}
\]

after reversing the path if necessary, and both endpoints are feet.
The case (m=1) is Proposition 4.1, so assume (m\ge2), and put

\[
                         M=\{x_1,\ldots,x_{2m-2}\}.      \tag{3.15}
\]

For (i\ne j), a vertex of (M) fails to be an (i)-portal exactly
when its incident nonmatching edge has label (p_i).  Hence (M) meets
every ordinary portal class unless all the labels \(\beta_q\) are the
same ordinary model colour (p_k).  Outside that one exception, the
branch sets

\[
 \{x_0,b_j\},\qquad M,\qquad \{v,x_{2m-1}\},\qquad
 \{b_i\}\ (i\ne j)                                    \tag{3.16}
\]

form a (K_{r+1})-model, exactly as in the proof of Theorem 3.4.

It remains that every \(\beta_q=p_k\) for one (k\ne j).  Then every
vertex of (B) is a foot: the endpoints are feet by Corollary 3.2, while
at an internal vertex the colour \(p_j=\delta\) is absent from its list
and (3.14) rules out membership in (P_j).  Also (P_k) consists of the
two endpoints, and every vertex belongs to (P_i) for
(i\notin\{j,k\}).

We claim that (b_j) is the only noncontact singleton.  If some
(b_\ell), \(\ell\notin\{j,k\}\), were noncontact, recolour the quotient
(G/B) with (v) receiving (p_\ell).  The new expansion lists contain
the old degree lists everywhere and are strictly larger at an internal
vertex (the colour (p_j) becomes available).  The degree-list lemma
would colour (B), and hence (G), a contradiction.  If (b_k) were
noncontact, give (v) colour (p_k).  The resulting lists are

\[
 \{\alpha\}\text{ at }x_0,
 \qquad
 \{\alpha,p_j\}\text{ at every other vertex};          \tag{3.17}
\]

alternating \(\alpha,p_j\) along the path is a list-colouring, again a
contradiction.  The claim follows, so (v) is adjacent to every
(b_i), (i\ne j).

Finally the four sets

\[
 \{v\},\qquad \{x_0,b_j\},\qquad
 M,\qquad \{x_{2m-1},b_k\}                              \tag{3.18}
\]

form a (K_4)-model.  The first is adjacent to the other three because
every path vertex is a foot; consecutive sets in (3.18) are adjacent
along (B); and the second and fourth are adjacent through (b_jb_k).
Every remaining singleton (b_i), (i\notin\{j,k\}), is adjacent to all
four sets: it sees (v), it sees the two absorbed singleton vertices, and
(M\subseteq P_i).  Adding these (r-3) singleton branch sets produces
a (K_{r+1})-model, the final contradiction. \(\square\)

The proof exposes a reusable principle.  A contraction-colour perfect
matching turns an arbitrary tree society into a size--degree quotient.
Branching in that quotient supplies two independently footed and
portal-complete shores; lack of branching forces a path, where quotient
colour switching resolves the sole constant-label exception.

### Theorem 3.6 (matching-\(\alpha\) Gallai theorem)

The conclusion of Theorem 3.5 remains true when \(B\) is an arbitrary
Gallai tree, provided every block whose palette contains \(\alpha\) is a
\(K_2\)-block.

#### Proof

Every vertex belongs to exactly one block whose palette contains
\(\alpha\).  Under the stated hypothesis these blocks are pairwise
vertex-disjoint \(K_2\)-blocks, hence their edges form a perfect matching
\(M_\alpha\).  A \(K_2\)-block is a bridge of \(B\).

Delete \(M_\alpha\) and contract each remaining component.  Since all
deleted edges are bridges, the quotient \(R\) is a tree.  Every vertex of
a component \(C\) is incident with its unique edge of \(M_\alpha\), and
all those matching edges leave \(C\).  Hence the same identity as (3.11)
holds:

\[
                              d_R(C)=|C|.                \tag{3.19}
\]

The proof of Corollary 3.2 uses only the matching bridge blocks and
Theorem 3.1.  Thus, in the absence of the target minor, \(P_j\) is
contained in one quotient component \(Q\), and every matching bridge has
foot crossing and all ordinary portal crossings.

Root \(R\) at \(Q\).  If a quotient vertex has two children, the branch
sets (3.12) give the target exactly as before; the internal structure of
the three shores is irrelevant.  Otherwise \(R\) is a path rooted at an
endpoint.  Identity (3.19) forces its endpoint components to have one
vertex and every internal component to have two vertices.  Each
two-vertex component is connected and therefore consists of one edge.
Consequently \(B\) itself is the alternating path (3.13), and the rest of
the proof of Theorem 3.5 applies verbatim. \(\square\)

Thus any unresolved full equality Gallai core contains an
\(\alpha\)-block which is either a clique of order at least three or an
odd cycle.  This is the exact point at which the contraction colour has
genuine internal block-palette capacity rather than a matching cut.

## 4. Single-block and shortest block-tree audit

### Proposition 4.1 (single equality block)

If the equality core \(B\) has one block, then either it is \(K_2\) with
palette \(\{\alpha\}\), or the fixed model hypotheses are inconsistent.

#### Proof

In a single block every vertex has the common block palette.  If a model
colour \(p_i\) belongs to that palette, no vertex is an \(i\)-portal,
contrary to \(P_i\ne\varnothing\).  Hence the palette contains no model
colour.  Since the full palette is
\(\{\alpha,p_1,\ldots,p_{r-1}\}\), its order is at most one.  A clique
block therefore has order at most two, and an odd-cycle block, which needs
two colours, is impossible. \(\square\)

In the \(K_2\) case, Theorem 3.1 applies.  If there are at least two
noncontact singleton bags, repeat the contraction colouring with either
noncontact colour on \(v\).  Both ends must then be portals to the other
noncontact bag, giving portal crossing and the target minor.  If there is
only one noncontact bag \(b_j\), both ends are feet and portals to every
other singleton; if \(P_j\) meets both ends, Theorem 3.1 applies.  If it
meets only one end \(x\), then

\[
 \{v\},\quad \{x,b_j\},\quad \{y\}                       \tag{4.1}
\]

are three pairwise adjacent connected bags, each adjacent to all
\(b_i\), \(i\ne j\).  Together with those \(r-2\) singleton bags they
form a \(K_{r+1}\)-model.  Thus the single-block cell always closes.

There is no equality core with exactly two blocks.  Both would be leaf
blocks of the block tree.  Every noncut vertex belongs to only its leaf
block and must have \(\alpha\) in that block palette.  The two palettes
would then both contain \(\alpha\) at their common cutvertex, contradicting
the required disjointness of incident block palettes.

With exactly three blocks, the middle block must be \(K_2\): its vertices
are the two cutvertices, while both leaf blocks carry \(\alpha\).  Its
single colour is the sole nonmatching corridor label.  If that label is
not \(c(v)\), the aligned marked-state bypass theorem supplies a clean
rotation or a hit in a named singleton bag.  The formerly exceptional
apex-coloured middle corridor has edge labels

\[
                              \alpha,\delta,\alpha.       \tag{4.2}
\]

It is the four-vertex instance of Theorem 3.4, and hence also closes.

## 5. Exact boundary

Theorems 2.1 and 3.1 are genuine label-alignment results, but they do not
close every Gallai core.

* Colours in one clique/odd-cycle block palette have internal Kempe detours
  and need not hit their singleton portals.
* The apex colour can replace its selected noncontact singleton in a layer.
* Every full equality-tree core is eliminated by Theorem 3.5, and
  Theorem 3.6 eliminates all Gallai cores whose \(\alpha\)-blocks are
  \(K_2\)'s.  Thus neither a foreign transit nor a prior dynamic
  normalization is needed in this spanning singleton cell.
* Strict-surplus cores and proper minimal cores with hanging societies are
  outside the theorem.

The next local target is now precise: handle a genuine \(\alpha\)-block
which is a clique of order at least three or an odd cycle.  Such blocks
introduce internal palette shadows, so the quotient must record block
palette rank rather than only component order.  Separately,
one needs a **core exchange theorem** to absorb portal-bearing hanging
societies when the minimal equality core is proper.  These are structural
extensions of Theorems 3.5--3.6, not further Moser-labelled cases.
