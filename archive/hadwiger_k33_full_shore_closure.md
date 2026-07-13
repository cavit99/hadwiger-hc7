# Full closure of the `2K3+K1` six-edge boundary

## 1. The theorem

### Theorem 1.1

Let `G` be a seven-connected graph with minimum degree at least seven.
Let

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{c\},
 \qquad |A|=|B|=3,
\]

and suppose

\[
 G[S]=K_1\vee K_{3,3},                              \tag{1.1}
\]

where `c` is universal in `G[S]` and `A,B` are the two independent
parts.  Suppose `G-S` has exactly two connected components `D_1,D_2`,
each with neighbourhood `S`.  If every proper minor of `G` is
six-colourable but `G` is not six-colourable, then `G` contains a
`K7` minor.

Equivalently, the missing-edge graph `2K3+K1` cannot be the boundary of
an order-seven counterexample-derived two-full-shore adhesion.

For the remainder of the proof, suppose for a contradiction that `G` is
`K7`-minor-free.

## 2. The split-contact lemma

Call a subset of `S` **small** if it is contained in a boundary triangle

\[
 \{c,a,b\},\qquad a\in A,\ b\in B.                  \tag{2.1}
\]

Thus a set is not small precisely when it contains two vertices of `A`
or two vertices of `B`.

### Lemma 2.1

Let `D` be one shore, and let

\[
 D=X\mathbin{\dot\cup}Y
\]

be a partition into nonempty connected sets with an edge between them.
If neither `N_S(X)` nor `N_S(Y)` is small, then `G` contains a `K7`
minor.

### Proof

Since `D` is full, `N_S(X) union N_S(Y)=S`.  Put

\[
 p=|N_S(X)\cap A|,\quad q=|N_S(X)\cap B|,\quad
 r=|N_S(Y)\cap A|,\quad s=|N_S(Y)\cap B|.
\]

Then `p+r>=3` and `q+s>=3`, while nonsmallness says

\[
 (p\ge2\text{ or }q\ge2),\qquad
 (r\ge2\text{ or }s\ge2).                           \tag{2.2}
\]

At least one of `p>=2,s>=2` and `q>=2,r>=2` holds.  Indeed, if both
failed, symmetry lets us take `p>=2`.  The first failure gives `s<=1`,
so `q>=2` by `q+s>=3`; the second failure then gives `r<=1`, contrary
to the second condition in (2.2).  Thus, after possibly interchanging
`X,Y` and `A,B`, choose

\[
 a_1,a_2\in N_S(X)\cap A,
 \qquad b_1,b_2\in N_S(Y)\cap B.                    \tag{2.3}
\]

Let `a_3,b_3` be the unused vertices of the two parts, and let `D'` be
the opposite full shore.  The seven bags

\[
 \{a_1\},\quad \{b_1\},\quad \{c\},\quad D',\quad
 \{a_3,b_3\},\quad X\cup\{a_2\},\quad
 Y\cup\{b_2\}                                      \tag{2.4}
\]

form a `K7` model.  The last two bags are connected and adjacent through
the edge between `X,Y`.  Their contacts in (2.3) make them adjacent to
the first two singleton bags.  The mixed bag `{a_3,b_3}` is connected
and sees both of them through the complete bipartite graph `G[A,B]`.
The singleton `{c}` and the full shore `D'` see every boundary-rooted
bag.  All remaining pairs are boundary edges from (1.1).

### Corollary 2.2

In a `K7`-minor-free realization, every connected bipartition of a shore
has a small contact side.

## 3. Local cuts and internal four-connectivity

For every nonempty proper set `X subset D_i`, seven-connectivity and the
opposite shore give

\[
 |N_{D_i}(X)|+|N_S(X)|\ge7.                         \tag{3.1}
\]

### Lemma 3.1 (singleton shores are impossible)

Neither shore has order one.

### Proof

Suppose `D_1={h}`.  Contract the connected star `D_1 union A` to one
vertex.  Six-colour the resulting proper minor.  Expanding only the
boundary vertices gives a six-colouring of `G-h` in which `A` is one
exact colour block: every vertex of `S-A` was adjacent to the contracted
star image.  Hence at most five colours occur on `S`.  The vertex `h`
has no neighbour outside `S`, so a sixth colour absent from `S` colours
`h`, contradicting the assumption on `G`.

### Lemma 3.2 (small shores are impossible)

Every shore has order at least five.

### Proof

Let `2<=|D|<=4`.  Choose a non-cutvertex `x` of the connected graph `D`.
Then `D-x` is nonempty and connected.  By (3.1),

\[
 |N_S(D-x)|\ge6,                                    \tag{3.2}
\]

so this contact set is not small.  On the other hand

\[
 |N_S(x)|=d_G(x)-d_D(x)\ge7-(|D|-1)\ge4,            \tag{3.3}
\]

which is not small either.  The connected bipartition
`{x},D-x` contradicts Corollary 2.2.

### Lemma 3.3

Every shore is four-connected.

### Proof

Let `D` be a shore.  Its order is at least five by Lemma 3.2.  Suppose
`W subset D`, `|W|<=3`, and `D-W` has distinct components `C_1,C_2`.
Equation (3.1) gives

\[
 |N_S(C_j)|\ge7-|W|\ge4\quad(j=1,2).                \tag{3.4}
\]

Contract each component of `D-W` to a vertex in an auxiliary connected
graph on those component vertices and `W`.  Choose a spanning tree and
delete an edge on the tree path between the vertices representing
`C_1,C_2`.  Lifting the two tree components back to `D` partitions `D`
into connected sets `X,Y`, with an edge between them, such that
`C_1 subset X` and `C_2 subset Y`.  Both `N_S(X)` and `N_S(Y)` have
order at least four by (3.4), contrary to Corollary 2.2.  Thus no set of
at most three vertices disconnects `D`.

## 4. Portal classes

### Lemma 4.1

For every `x in D`, the contact set `N_S(x)` is small.  For every edge
`xy in E(D)`, the union `N_S(x) union N_S(y)` is small.

### Proof

Four-connectivity and `|D|>=5` imply that `D-x` is connected and
nonempty.  Equation (3.1), applied to `D-x`, gives at least six boundary
contacts.  Hence the large side of the connected bipartition
`{x},D-x` is not small, and Corollary 2.2 forces `N_S(x)` to be small.

Likewise `D-{x,y}` is connected and nonempty.  Its internal neighbour
set has order at most two, so (3.1) gives it at least five boundary
contacts.  Apply Corollary 2.2 to the connected bipartition
`{x,y},D-{x,y}` to prove that `N_S(x) union N_S(y)` is small.

For `a in A`, put `P_a=N_D(a)`, and define `P_b` analogously for
`b in B`.

### Corollary 4.2

The three sets `(P_a:a in A)` are nonempty, pairwise disjoint, and
pairwise anticomplete in `D`.  The same is true of the three `B`-portal
sets.

### Proof

They are nonempty because `D` is full.  A vertex in two distinct
`A`-portal sets would have two `A` contacts, contradicting the first
part of Lemma 4.1.  An edge between two distinct `A`-portal sets would
put two `A` contacts in the union at its ends, contradicting the second
part.  The `B` argument is identical.

## 5. Rooted triangles and the final minor

### Lemma 5.1

Every shore contains an `A`-rooted `K3` model and a `B`-rooted `K3`
model.

### Proof

Choose one vertex from each of the three nonempty `A`-portal sets.
They are distinct by Corollary 4.2.  We recall the elementary rooted
triangle argument.  In a 2-connected graph, take a cycle `C` through
two prescribed roots `p_1,p_2`.  If the third root `p_3` lies on `C`,
cut the cycle at three suitable edges into three arcs, one containing
each root; the arcs are connected, disjoint, and pairwise adjacent.  If
`p_3` is off `C`, the fan lemma gives two internally disjoint paths from
`p_3` to distinct vertices `x,y` of `C`, otherwise disjoint from `C`.
Of the two assignments of `x,y` to `p_1,p_2`, one is noncrossing in the
cyclic order.  Cut `C` at two edges into disjoint arcs, one containing
`p_1` and its assigned fan end and the other containing `p_2` and the
other fan end.  Those two arcs, together with the union of the fan paths
with `x,y` deleted, are three connected pairwise adjacent bags rooted at
`p_1,p_2,p_3`.  Thus every 2-connected graph has the required rooted
`K3` model.

Lemma 3.3 says that `D` is 4-connected, so this rooted model exists in
`D`.  Add each corresponding
boundary vertex of `A` to the branch set containing its chosen portal.
The three enlarged bags are connected and remain pairwise adjacent,
giving an `A`-rooted triangle in `G[D union A]`.  Repeat for `B`.

### Completion of Theorem 1.1

Take an `A`-rooted triangle in `D_1`, a `B`-rooted triangle in `D_2`,
and the singleton bag `{c}`.  The three bags in either shore are
pairwise adjacent.  Every `A`-rooted bag sees every `B`-rooted bag
through `G[A,B]`, and `{c}` sees all six rooted bags.  These are seven
pairwise adjacent disjoint connected branch sets, a `K7` model.
