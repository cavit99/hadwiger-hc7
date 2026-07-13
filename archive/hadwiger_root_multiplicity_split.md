# Root multiplicity forces a portal split or a sharp cut

## 1. A label-free two-class splitter

Let `R` be a connected full shore on a boundary `S`: every vertex of
`S` has a neighbour in `R`.  For boundary labels `a,b`, write

\[
 A=N_R(a),\qquad B=N_R(b).
\]

### Theorem 1.1 (double-root split or cutvertex)

Suppose `|A|>=2` and `|B|>=2`.  Then one of the following holds.

1. There is a connected bipartition

   \[
   R=R_1\mathbin{\dot\cup}R_2
   \]

   with `R_1R_2` adjacent such that both contact rows contain both
   repeated roots:

   \[
   \{a,b\}\subseteq N_S(R_1)\cap N_S(R_2).       \tag{1.1}
   \]

   Since `R` is full, the two contact rows also cover `S`.
2. There is a vertex `q in R` meeting every `A-B` path in `R`.
   The graph `R-q` has at least two components, and no component contains
   both a vertex of `A-{q}` and a vertex of `B-{q}`.

#### Proof

Adjoin vertices `a_0,b_0`, make `a_0` adjacent to every vertex of `A`,
and make `b_0` adjacent to every vertex of `B`.  By the two-path form of
Menger's theorem, either there are two internally vertex-disjoint
`a_0-b_0` paths or one vertex `q in R` meets every such path.

In the first case, deleting the artificial ends gives two vertex-disjoint
`A-B` paths `P_1,P_2` with distinct portal endpoints.  If the paths are
not adjacent, take a shortest path between them.  Its interior avoids
both; split it at any edge and absorb its two halves into `P_1,P_2`.
This gives disjoint connected adjacent carriers, each meeting `A` and
`B`.  Contract the two carriers, take a spanning tree containing their
joining edge, and delete that tree edge.  Expanding the contractions
extends the carriers to a connected bipartition of all of `R`.  The
resulting sides retain both portal classes, proving
(1.1).  Fullness gives row coverage.

In the second case, a component of `R-q` containing vertices of both
`A-{q}` and `B-{q}` would contain an `A-B` path avoiding `q`.  Moreover,
because each portal class has order at least two, both `A-{q}` and
`B-{q}` are nonempty; they lie in different components.  This proves
alternative 2. \(\square\)

This theorem is deliberately independent of a cyclic labeling, a web,
or a clique target.  It converts **portal multiplicity** into either a
new covering split retaining two prescribed labels on both sides, or a
one-vertex internal separator.

## 2. The sharp-cut consequence of the separator outcome

Suppose now that `R` lies behind a `k`-vertex boundary `S` in a
`k`-connected ambient graph.  Let `Z` be the set of possible neighbours
of `R` outside `R union S`; in the applications below `|Z|<=1`.
For a component `C` of `R-q`, put

\[
 Z_C=Z\cap N_G(C).
\]

Then

\[
 N_G(C)\subseteq N_S(C)\cup\{q\}\cup Z_C,
\]

and the opposite full shore lies outside this set.  Therefore

\[
 |N_S(C)|\ge k-1-|Z_C|.                           \tag{2.1}

Equality throughout exposes the exact `k`-cut

\[
 N_S(C)\cup\{q\}\cup Z_C.                        \tag{2.2}

At `k=7`, a component with no charged external neighbour has six or
seven boundary contacts; absent an exact seven-cut it is full.  A
component with one charged neighbour has at least five contacts; absent
an exact seven-cut it has at least six and hence defect at most one.

## 3. A four-piece packing lemma

### Lemma 3.1 (three full pieces and one defect-one piece)

Let `|S|=7` and put `J=G[S]`.  Suppose `T subset S` is a triangle.
Let `C_0,C_1,C_2,C_3` be pairwise disjoint connected pieces outside
`S`, with extra edges between the pieces allowed.  Suppose
`C_1,C_2,C_3` are full to
`S`, while `C_0` misses at most one label `d`.

If there is a vertex `r_0 in S-T` contacted by `C_0` such that

\[
 d\notin T\quad\hbox{or}\quad r_0d\in E(J),       \tag{3.1}
\]

then `G` contains a `K_7` minor.

#### Proof

Assign the other three vertices of `S-T` bijectively as
`r_1,r_2,r_3` and form

\[
 B_i=C_i\cup\{r_i\}\quad(0\le i\le3),
\]

together with the three singleton bags indexed by `T`.  Each `B_i` is
connected.  The bags `B_1,B_2,B_3` are pairwise adjacent because the
pieces are full.  Each is adjacent to `B_0` through the edge from its
full piece to `r_0`; thus a possible missing contact of `C_0` causes no
problem.  Every singleton in `T` sees each full piece.  It sees `B_0`
through `C_0`, except possibly when it is `d`; that last adjacency is
provided by (3.1).  Finally `T` is a triangle.  These are seven disjoint
pairwise adjacent connected bags. \(\square\)

For

\[
 J=K_1\vee C_6,                                   \tag{3.2}
\]

the condition of Lemma 3.1 can always be met.  If the missed label `d`
is a cycle vertex, choose a triangle consisting of the universal vertex
and a cycle edge avoiding `d`.  If `d` is the universal vertex, choose
any such triangle and any contacted cycle vertex outside it as `r_0`;
that vertex is adjacent to `d`.  With no defect, the assertion is
immediate.

## 4. Application to a unique-interface `C6` adhesion

Let `G` be seven-connected and `K_7`-minor-free.  Let

\[
 S=\{z,c_0,\ldots,c_5\},\qquad G[S]=K_1\vee C_6, \tag{4.1}
\]

where `z` is universal and the `c_i` induce the cycle.  Suppose `G-S`
has two full components `D,D'`, and

\[
 D=X\mathbin{\dot\cup}Y,\qquad E(X,Y)=\{xy\}.
\]

Assume the tight-cut outcome of Theorem 2.1 in
`hadwiger_unique_interface_anchor_tight_cut.md` does not occur.  Thus
`X,Y,D'` are all full to `S`.

### Theorem 4.1 (multiplicity-to-further-split in the `C6` cell)

Some arm `R in {X,Y,D'}` and two distinct cycle roots `a,b` have

\[
 |N_R(a)|\ge2,qquad |N_R(b)|\ge2.                 \tag{4.2}

For such a choice, either `G` contains a `K_7` minor, a nested exact
seven-cut occurs, or `R` has a connected adjacent split whose two rows
both contain `a,b` and cover `S`.

#### Proof

Every cycle root has three boundary neighbours in (4.1).  Minimum degree
seven and the three nonempty portal sets in `X,Y,D'` give

\[
 |N_X(c_i)|+|N_Y(c_i)|+|N_{D'}(c_i)|
 =d_G(c_i)-3\ge4.                                 \tag{4.3}

Thus every one of the six cycle roots is repeated in at least one of the
three arms.  Assign each root to one such arm.  Pigeonhole gives an arm
assigned at least two roots, proving (4.2).

Apply Theorem 1.1 inside `R`.  Its first outcome is the claimed further
split.  Suppose instead that a cutvertex `q` separates the two portal
classes.

If `R=D'`, every component `C` of `R-q` has

\[
 N_G(C)=N_S(C)\cup\{q\}.
\]

It has at least six boundary contacts; six gives an exact seven-cut, and
otherwise it is full.  There are at least two such components.  In the
absence of the cut outcome, take two of them together with the full
pieces `X,Y`.  Lemma 3.1 (with no defective piece) gives a `K_7` minor.

Now let `R=X`; the case `R=Y` is symmetric.  If `q=x`, every component
of `X-q` is uncharged and the preceding argument applies, using two such
components together with `Y,D'`.  If `q!=x`, let `C_x` be the component
containing `x`.  Every other component is uncharged and hence, absent an
exact seven-cut, full.  The only neighbour of `C_x` outside
`C_x union S union {q}` is `y`, so (2.1) gives

\[
 |N_S(C_x)|\ge5.
\]

Equality makes `N_S(C_x) union {q,y}` an exact seven-cut.  Otherwise
`C_x` has defect at most one.  Choose another component `C_1`; it is
full.  The four pieces

\[
 C_x,\quad C_1,\quad Y,\quad D'
\]

satisfy Lemma 3.1, and (3.2) supplies its triangle/repair condition.
Thus they form a `K_7` model, a contradiction.

The separator outcome of Theorem 1.1 therefore always gives either the
clique minor or a nested exact seven-cut.  The only residual is its
connected double-overlap split. \(\square\)

## 5. Uniform multiplicity count

The counting step in (4.3) has the following label-free form.  Suppose
three full arms contain every neighbour outside `S` of the roots under
consideration, in a graph of minimum degree at least `k`.  Then every
root `s` with

\[
 d_{G[S]}(s)\le k-4
\]

has at least four portal neighbours across the arms and is repeated in
one arm.  If there are `ell` such roots, one arm repeats at least
`ceil(ell/3)` of them.  Theorem 1.1 then turns any two of those repeated
classes into a label-preserving split or a one-vertex separator, and
(2.1) converts the separator into a bounded-defect shore family.

This is the reusable mechanism exposed by the `C6` laboratory:

\[
 \text{sparse boundary root}
 \Longrightarrow \text{portal multiplicity}
 \Longrightarrow \text{double-root split or sharp separator}
 \Longrightarrow \text{clique packing or nested minimum cut}.
\]

## 6. The complementary high-boundary classification

The multiplicity mechanism has a clean complementary case.  Write

\[
 J=G[S],\qquad Q=\overline J.
\]

Thus a vertex of degree at least three in `Q` has degree at most three
in the boundary graph `J`, and is forced to have a repeated portal in
one of three full arms.  If `Delta(Q)<=2`, there is no such degree
forcing, but the possible two-full-shore quotients have a short exact
classification.

### Lemma 6.1 (one repeated root gives a covering split)

Let `R` be a connected full shore on `S`, and suppose that one boundary
label `s` has two distinct neighbours `u,v in R`.  Then there is a
connected adjacent bipartition

\[
 R=R_1\mathbin{\dot\cup}R_2
\]

such that

\[
 s\in N_S(R_1)\cap N_S(R_2),\qquad
 N_S(R_1)\cup N_S(R_2)=S.                       \tag{6.1}
\]

#### Proof

Choose a spanning tree of `R` and an edge on its unique `u-v` path.
Deleting that tree edge gives two vertex sets, one containing `u` and
the other containing `v`.  Each set induces a connected subgraph of
`R`, and the deleted tree edge joins the two sets.  Both rows contain
`s`; their union is `S` because they partition the full shore. \(\square\)

### Theorem 6.2 (degree, multiplicity, or one of eight boundaries)

Let `G` be a `K_7`-minor-free graph of minimum degree at least seven.
Let `S` have order seven, and suppose that all neighbours of `S` outside
`S` lie in three pairwise disjoint connected arms `R_1,R_2,R_3`, each
full to `S`.  Edges between different arms are allowed.  Then at least
one of the following holds.

1. The missing graph `Q` is a split graph.
2. Some arm has a repeated boundary root and hence the covering split
   in Lemma 6.1.
3. The missing graph `Q` is isomorphic to one of

   \[
   \begin{gathered}
   C_7,\quad C_3\mathbin{\dot\cup}C_4,\quad
   C_6\mathbin{\dot\cup}K_1,\quad
   2C_3\mathbin{\dot\cup}K_1,\\
   C_3\mathbin{\dot\cup}P_4,\quad
   C_5\mathbin{\dot\cup}K_2,\quad
   C_5\mathbin{\dot\cup}2K_1,\quad
   C_3\mathbin{\dot\cup}2K_2 .                  \tag{6.2}
   \end{gathered}
   \]

Moreover, if at least four vertices of `S` have boundary degree at most
three, then outcome 2 can be strengthened to the double-root split or
cutvertex alternative of Theorem 1.1.

#### Proof

Suppose first that `Delta(Q)>=3`, and choose `s` with
`d_Q(s)>=3`.  Then `d_J(s)<=3`.  Since all external neighbours of `s`
lie in the three arms,

\[
 \sum_{i=1}^3 |N_{R_i}(s)|
   =d_G(s)-d_J(s)\ge4.                            \tag{6.3}
\]

Every summand is positive by fullness, so one is at least two.  Lemma
6.1 gives outcome 2.

We may therefore assume `Delta(Q)<=2`.  If `Q` is split, outcome 1
holds.  Otherwise contract two of the full arms, discard the third, and
delete any edge between the two contracted images.  This gives the
quotient consisting of `J` and two nonadjacent vertices complete to
`S`.  It is a minor of `G`, so it is `K_7`-minor-free.  The
exact order-seven classification in
`order7_maxdegree2_boundary_verify.py` now gives precisely the eight
graphs in (6.2): among the 24 nonsplit unlabelled graphs on seven
vertices with maximum degree at most two, 16 have a certified `K_7`
model in this quotient and these eight do not.

For the final assertion, apply (6.3) to each of the at least four
low-boundary-degree roots and assign it to an arm in which it is
repeated.  One of the three arms receives two roots.  Theorem 1.1
applies to those two portal classes. \(\square\)

### 6.3 Audit of the four-piece invocation in Theorem 4.1

The applications of Lemma 3.1 in Theorem 4.1 use actual connected
components, not quotient vertices.  In the uncharged cases all four
selected components are full, so any one may play `C_0` and condition
(3.1) is vacuous.  In the charged case the selected component `C_x`
has at most one missing label and the other component of `X-q`, together
with `Y,D'`, gives the three full pieces.  For `J=K_1\vee C_6`, the
triangle choice immediately following Lemma 3.1 supplies a contacted
`r_0` satisfying (3.1), including when the missed label is the universal
vertex.  The seven displayed bags are therefore legitimate lifts in
every use of that lemma.

The classification in Theorem 6.2 also records the exact limit of the
new invariant.  A repeated portal always gives a covering split, but a
covering split is not automatically a positive clique quotient.  The
remaining negative rows must be resolved by their internal interface
geometry (or by a nested exact cut), rather than by portal multiplicity
alone.

For a concrete quotient-only audit, take `J=K_1\vee C_6`, two full
nonadjacent helpers, and adjacent split helpers `p,q`, where `p` is full
and `q` sees only the universal vertex and the ends of one rim edge.
Both split rows contain either rim endpoint and together cover `S`, but
the resulting eleven-vertex graph has no `K_7` minor.  The exact search
in `portal_multiplicity_split_probe.py` finds this row among ten maximal
negative rows (for a fixed duplicated rim root).  Its low-degree split
helper also shows why this is only a quotient obstruction: ambient
seven-connectivity must be used through the actual interface separator.

### 6.4 The exact interface certificate retained by a split

The separator information lost by the quotient can be stated without
reference to `C_6`.  Let `G` be `k`-connected, let `|S|=k`, and let
`R` be a full shore.  Assume that there is a nonempty opposite shore
with no edge to `R`.  For any connected adjacent bipartition

\[
 R=R_1\mathbin{\dot\cup}R_2
\]

put

\[
 P_i=N_S(R_i),\qquad
 T_i=N_{R_{3-i}}(R_i),\qquad
 Z_i=N_G(R_i)-(S\cup R).                          \tag{6.4}
\]

Then

\[
 \Gamma_i=P_i\mathbin{\dot\cup}T_i
                 \mathbin{\dot\cup}Z_i=N_G(R_i) \tag{6.5}
\]

is an actual portal separator between `R_i` and the opposite shore, and

\[
 |T_i|+|Z_i|\ge |S-P_i|.                          \tag{6.6}
\]

Equality in (6.6) makes `Gamma_i` an exact order-`k` cut.  Thus the
rooted split of Lemma 6.1 has the rigorous trichotomy

\[
 \text{positive multi-piece quotient},\quad
 \text{nested exact }k\text{-cut},\quad
 \text{strict portal/interface surplus}.         \tag{6.7}
\]

Indeed, (6.5) is simply the complete external neighbourhood of `R_i`;
the opposite shore certifies that it separates two nonempty sets.
Connectivity gives `|Gamma_i|>=k`, which is (6.6), and equality is
exactly the minimum-cut case.  This is the strongest conclusion that
follows from multiplicity and connectivity alone: the explicit negative
quotient above shows that the last alternative cannot be deleted without
using the placement of the surplus interface vertices.
