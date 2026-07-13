# Apex web closure for degree-eight and degree-nine neighborhoods

## 1. Purpose

The full-shore web theorem applies directly to an order-seven adhesion, but
an application at the neighborhood of a vertex has an extra apex.  This
note isolates the versions in which that apex causes no color loss.  It
also gives explicit crossing certificates which use the near-full exterior
components as branch sets.

Throughout, `G` is seven-connected, `v` is a vertex, `N=N_G(v)`, and the
components of `G-N[v]` are called exterior components.  For a cyclically
ordered set

\[
 R=(x_0,x_1,\ldots,x_{k-1}),\qquad k\in\{4,5\},       \tag{1.1}
\]

write `Z=N-R`.  We require that `G[R]` be exactly the cycle in (1.1).
This is essential on the crossing side: the four cyclic arcs are actual
parts of the rooted `K_4` certificate, not edges added only to a planar
supergraph.

For an exterior component `D`, put

\[
 P_i(D)=N_D(x_i).
\]

The tuple is **crossed in `D`** if, for some four terminals occurring in
the cyclic order `i<r<j<s`, there are vertex-disjoint paths in `D` joining
`P_i(D)` to `P_j(D)` and `P_r(D)` to `P_s(D)`.

---

## 2. The rooted `K_4` supplied by a cross

### Lemma 2.1 (cross lemma)

Suppose `P_i(D),P_r(D),P_j(D),P_s(D)` are nonempty and the tuple is
crossed in `D`.  Then `G[D\cup R]` contains a `K_4`-model

\[
 \mathcal K=(B_1,B_2,B_3,B_4)                         \tag{2.1}
\]

such that every `B_a` meets `R`.

#### Proof

Extend the two disjoint paths by their terminal edges to
`x_i,x_j,x_r,x_s`.  Together with the four cyclic arcs of the frame, they
form a subdivision of a four-cycle with both diagonals.  Contract each
cyclic arc to one of its terminal ends.  If `k=5`, the unused fifth frame
vertex lies on one of the four arcs and is contracted with that arc.  The
result is `K_4`, and every branch set contains a frame vertex. \(\square\)

The proof only uses the two crossing paths.  All unused vertices of `D`
may be deleted; no adjacency between the two paths is required.

The independent script `degree89_apex_web_certificate_verify.py` checks
the unique four-terminal crossing of a four-frame and all five crossing types
of a five-frame.  It verifies both the seven-bag completion below and the
six-bag opposite-shore completion of Lemma 4.2 by exhaustive connected-bag
search.

### Lemma 2.2 (universal-pair completion)

If there are adjacent vertices `p,q\in Z`, each complete to `R`, then a
cross in any exterior component gives a `K_7`-minor in `G`.

#### Proof

Use the four bags in (2.1) and the singleton bags

\[
 \{v\},\qquad\{p\},\qquad\{q\}.                       \tag{2.2}
\]

The three singletons form a triangle.  Each is adjacent to every bag of
`\mathcal K`, because every such bag meets `R`, `v` sees all of `N`, and
`p,q` are complete to `R`.  These seven bags form a `K_7`-model.
\(\square\)

---

## 3. One exterior component

### Theorem 3.1 (one-shore apex web closure)

Assume `G-N[v]` has exactly one component `D`.  Suppose:

1. `P_i(D)` is nonempty for every `i`;
2. `G[R]` is exactly the cycle (1.1);
3. at most three vertices of `Z` have a neighbor in `D`;
4. `G[Z]` is bipartite; and
5. every cross in `D` gives a `K_7`-minor.

Then `G` contains a `K_7`-minor or `G` is six-colorable.

#### Proof

Adjoin independent artificial terminals `t_i` to `D`, where `t_i` sees
exactly `P_i(D)`.  If the terminal tuple is crossed, hypothesis 5 gives
the minor.  Suppose it is crossless.  By the generalized Two Paths
Theorem, add edges on the same vertex set to obtain a `k`-web with this
terminal frame.

Consider a clique inserted behind a facial triangle of the web.  In the
original graph, its neighbors represented in the auxiliary graph are at
most the three vertices of that facial triangle.  It can additionally see
only the at most three vertices of `Z` which have neighbors in `D`.  It
does not see `v`.  Its neighborhood in `G` therefore has order at most
six and separates it from `v`, contrary to seven-connectivity.  Thus every
original vertex of `D` belongs to the planar rib.

Replace the artificial terminals by the vertices of `R` and add any
missing frame-cycle edges.  This embeds `G[D\cup R]` in a disk with `R` on
its boundary.  Put `v` in the complementary disk and draw its edges to
all vertices of `R`.  Since `G[R]` is the frame cycle, this proves that

\[
 G-Z\quad\hbox{is planar}.                            \tag{3.1}
\]

Four-color `G-Z`, and two-color `G[Z]` with two fresh colors.  Fresh
palettes make every edge across the cut proper, giving a six-coloring of
`G`. \(\square\)

### Corollary 3.2 (automatic crossing certificate)

In Theorem 3.1, hypothesis 5 follows if `Z` contains an adjacent pair
complete to `R`.

This is Lemma 2.2.

### Corollary 3.3 (degree eight, one component)

Let `d(v)=8`, and suppose `G-N[v]` has one component `D`.  Let `R` be a
five-element cyclic frame and put `Z=N-R`.  If

* `D` meets every vertex of `R`;
* `G[R]` is exactly the frame cycle;
* `G[Z]` is bipartite; and
* two adjacent vertices of `Z` are complete to `R`,

then `G` has a `K_7`-minor or is six-colorable.

Indeed, `|Z|=3`, so the effective omitted-contact condition in Theorem
3.1 is automatic.  Seven-connectivity already says that `D` misses at
most one of the eight vertices of `N`, so a frame avoiding that possible
defect is full.

### Corollary 3.4 (degree nine, one defective component)

Let `d(v)=9`, and suppose `G-N[v]` has one component `D` with a nonempty
boundary defect `M=N-N_G(D)`.  Let `R` be a five-element cyclic frame
disjoint from `M`, put `Z=N-R`, and assume:

* `G[R]` is exactly the frame cycle;
* `G[Z]` is bipartite; and
* two adjacent vertices of `Z` are complete to `R`.

Then `G` has a `K_7`-minor or is six-colorable.

Here `|Z|=4`, but `M\subseteq Z` is nonempty, so at most three vertices
of `Z` have a neighbor in `D`.  Recall that seven-connectivity gives
`|M|\le2`.

---

## 4. Two exterior components

Let `H=G-v`.

### Theorem 4.1 (two-shore apex web closure)

Assume

\[
 G-N[v]=D_1\mathbin{\dot\cup}D_2.                    \tag{4.1}
\]

Suppose:

1. every `D_j` meets every vertex of `R`;
2. `G[R]` is exactly the frame cycle;
3. each `D_j` has neighbors in at most three vertices of `Z`;
4. `Z` is independent; and
5. a cross in either shore gives an `N`-meeting `K_6`-model in `H`.

Then `G` contains a `K_7`-minor or is six-colorable.

#### Proof

Apply the auxiliary-terminal construction separately to `D_1,D_2`.  A
cross gives the minor by hypothesis 5 and the singleton bag `{v}`.
Suppose both terminal tuples are crossless.  As in Theorem 3.1,
seven-connectivity removes every facial insertion: such an insertion has
at most three rib neighbors and at most three neighbors in `Z`, and the
opposite nonempty shore lies beyond this cut.

Thus each `G[D_j\cup R]` embeds in a disk with boundary `R`.  Glue the two
disks on opposite sides of their common boundary.  Since the shores are
anticomplete,

\[
 H-Z\quad\hbox{is planar}.                            \tag{4.2}
\]

Four-color `H-Z` and give every vertex of the independent set `Z` one
fresh fifth color.  Give `v` a sixth color.  This is proper because
`v` has no exterior neighbor and its neighborhood is precisely `N`.
\(\square\)

### Lemma 4.2 (one universal vertex plus the opposite shore)

Suppose `|Z|\ge3`, and there is a vertex `p\in Z` such that

1. `p` is complete to `R`; and
2. for each `j`, the component `D_j` sees `p` and also sees some vertex
   `q_j\in Z-\{p\}`.

Then hypothesis 5 of Theorem 4.1 holds.

#### Proof

Suppose the cross occurs in `D_i`, and let `j\ne i`.  Take the rooted
`K_4` bags from Lemma 2.1.  Append

\[
 \{p\},\qquad D_j\cup\{q_j\}.                        \tag{4.3}
\]

The latter bag is connected.  It is adjacent to every rooted `K_4` bag
through the full contacts of `D_j` with `R`.  The singleton `p` is
adjacent to every rooted bag because it is complete to `R`, and it is
adjacent to the last bag through an edge from `p` to `D_j`.  All six bags
meet `N`.  Hence (4.3) completes an `N`-meeting `K_6`-model in `H`.
\(\square\)

### Corollary 4.3 (degree eight, two components)

Let `d(v)=8`, and suppose there are exactly two exterior components.  Let
`R` be a five-element cyclic frame avoiding both possible one-vertex
defects and put `Z=N-R`.  If

* `G[R]` is exactly the frame cycle;
* `Z` is independent; and
* some `p\in Z`, outside both shore defects, is complete to `R`,

then `G` has a `K_7`-minor or is six-colorable.

Indeed, each shore sees all of `R` and at most the three vertices of `Z`.
It sees `p`; because it misses at most one boundary vertex and `|Z|=3`, it
also sees some `q\in Z-\{p\}`.  Lemma 4.2 and Theorem 4.1 apply.

### Corollary 4.4 (degree nine, two defective components)

Let `d(v)=9`, suppose there are exactly two exterior components, and let
`R` be a five-element cyclic frame.  Put `Z=N-R`.  Assume:

* each shore defect is a nonempty subset of `Z`;
* `G[R]` is exactly the frame cycle;
* `Z` is independent; and
* a vertex `p\in Z` outside both defects is complete to `R`, while each
  shore sees another vertex of `Z-\{p\}`.

Then `G` has a `K_7`-minor or is six-colorable.  Each shore has at most
three effective contacts in the four-vertex set `Z`, so Theorem 4.1 and
Lemma 4.2 apply.

### Theorem 4.5 (bipartite common-defect closure)

Assume (4.1), let `R` be an induced five-cycle, and suppose:

1. both shores meet every vertex of `R`;
2. each shore has neighbors in at most three vertices of `Z`;
3. `G[Z]` has a bipartition `A\dot\cup B` such that no vertex of `A`
   has a neighbor in either shore; and
4. a cross in either shore gives a `K_7`-minor.

Then `G` contains a `K_7`-minor or is six-colorable.

#### Proof

If a shore is crossed, use hypothesis 4.  Otherwise the web argument in
Theorem 4.1 removes all facial insertions and proves that

\[
 P:=H-Z
\]

is planar, with `R` an induced five-cycle.

Fix a proper coloring of `R` with colors `1,2,3`.  We use the safe-cycle
precoloring theorem: any proper `k`-coloring of an induced cycle of length
at most `2k-5` which uses at most `k-1` colors extends to every planar
supergraph containing that induced cycle.  With `k=5`, the fixed coloring
of `R` therefore extends to a five-coloring of `P` with colors
`1,2,3,4,5`.  (This is Corollary 1 of A. Diwan, *Colouring planar graphs
with a precoloured induced cycle*, arXiv:2306.04944.)

Give every vertex of `A` color `4` and every vertex of `B` color `6`.
This is proper.  The classes `A,B` are independent; vertices of `A` have
no shore neighbors and the vertices of `R` use only colors `1,2,3`; color
`6` is absent from `P`.  Finally give `v` color `5`.  Although color `5`
may occur in the shore interiors, `v` has no exterior neighbor, while its
entire neighborhood `N=R\cup A\cup B` avoids color `5`.  Hence this is a
six-coloring of `G`. \(\square\)

### Corollary 4.6 (automatic crossing in the common-defect cell)

In Theorem 4.5, hypothesis 4 follows if there are adjacent vertices
`p,q\in Z`, each complete to `R`.  This is the universal-pair completion
of Lemma 2.2.

In particular, this closes an unbounded degree-eight two-component family:
`|Z|=3`, one bipartition class of `G[Z]` consists entirely of common shore
defects, and an edge across the bipartition has both ends complete to the
induced frame `C_5`.

---

## 5. Exact audit and limitations

### Proposition 5.1 (connectivity retained by a crossless web)

In the crossless outcome of Theorem 3.1,

\[
 \kappa(G-Z)\ge 7-|Z|.                               \tag{5.1}
\]

In the crossless outcome of Theorem 4.1,

\[
 \kappa(H-Z)=\kappa(G-(Z\cup\{v\}))\ge 6-|Z|.        \tag{5.2}
\]

These are the standard inequalities
`\kappa(G-X)\ge\kappa(G)-|X|`.  Consequently a degree-eight one-shore
five-web has a four-connected planar core `G-Z`, while a degree-eight
two-shore five-web has a three-connected planar core `H-Z`.

### Proposition 5.2 (the sharp `K_3\dot\cup C_5` sole-shore core)

Suppose additionally that `G` is a minimal `HC_7` counterexample,
`d(v)=8`, `G[N]=K_3\dot\cup C_5`, and there is one exterior component
`D`.  Then every boundary vertex has at least four distinct neighbors in
`D`; in particular `D` has no boundary defect.

Indeed, every vertex of `G[N]` has boundary degree two, is adjacent to
`v`, and has total degree at least seven.  Hence it has at least four
neighbors in `D`.  If the `C_5` terminal tuple is crossless, deleting the
three triangle vertices leaves the four-connected planar graph

\[
 G-V(K_3).                                            \tag{5.3}
\]

Thus the familiar `K_3\dot\cup C_5` quotient survivor is not an arbitrary
web: its disk core is four-connected and each of the three omitted clique
vertices has at least four portals into that core.  What is still missing
is a theorem converting those three distributed portal sets into the
rooted bags needed to complete `K_7`.

### Limitations

The following distinctions are essential.

1. **Bipartite alone is not enough with two shores.**  If `Z` is merely
   bipartite, (4.2) gives a six-coloring of `H`, but all six colors may
   occur on `N`; no color is then available for `v`.  The independent-set
   hypothesis in Theorem 4.1 supplies the required one-color slack.
   Theorem 4.5 recovers that slack only when one bipartition class has no
   shore neighbors, using a five-color safe-cycle extension.
2. **The apex causes no loss with one shore.**  In Theorem 3.1, `v` is
   drawn on the side of the frame opposite the sole web, so `G-Z` itself
   is planar.  This is why bipartite `Z` suffices there.
3. **The facial-module count uses actual contacts.**  A five-frame in a
   nine-vertex neighborhood leaves four omitted vertices.  It is valid
   only when at least one is an actual shore defect; a dummy defect cannot
   be used to reduce the cut from seven to six.
4. **Three disk shores do not glue in the plane.**  The argument does not
   settle the remaining three-component degree-nine cell.
5. **Contact placement remains the residual.**  A generic cross supplies
   only a rooted `K_4`.  The universal-pair and opposite-shore lemmas show
   exactly which extra contacts turn it into the required `K_7` or
   `N`-meeting `K_6`.  Without such distributed contacts, the quotient
   alone does not force the completion.

Thus these theorems close unbounded degree-eight/nine web families, but do
not by themselves eliminate every one- or two-component neighborhood.
Their main contribution is a safe apex-aware interface between the Two
Paths web alternative and the minor/coloring requirements of `HC_7`.
