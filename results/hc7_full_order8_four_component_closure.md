# Four full components close an order-eight boundary

**Status:** written proof; separate internal audit GREEN.

## 1. Statement

### Theorem 1 (order-eight four-component closure)

Let `G` be a graph such that

\[
 \chi(G)=7,
 \qquad
 \chi(M)\le 6\text{ for every proper minor }M\text{ of }G,
 \qquad
 K_7\not\preccurlyeq G.
 \tag{1.1}
\]

Let `X` be an eight-vertex set.  Suppose that `G-X` has at least four
components and every component `C` of `G-X` is adjacent to every vertex
of `X`:

\[
                         N_G(C)=X.                         \tag{1.2}
\]

Then these assumptions are inconsistent.

Thus the boundary-full order-eight alternative in the nested
full-neighbourhood descent has at most three complementary components.
The theorem does not assume that `X` is a minimum cut.

## 2. A small boundary lemma

### Lemma 2

Every triangle-free graph on at most eight vertices is three-colourable.

#### Proof

Let `H` be triangle-free and have at most eight vertices.  If
`Delta(H)<=3`, apply Brooks' theorem to each component.  A complete
component of maximum degree at most three is not `K_4`, because `H` is
triangle-free, and an odd-cycle component is itself three-colourable.
Hence `chi(H)<=3`.

Suppose instead that a vertex `v` has degree at least four.  Its
neighbourhood is independent.  Put

\[
                         R=V(H)-N_H[v].                     \tag{2.1}
\]

Then `|R|<=3`, and the triangle-free graph `H[R]` is bipartite.  Give
all of `N_H(v)` one colour, give `v` a second colour, and colour `H[R]`
with the second and third colours.  There is no edge from `v` to `R`,
and every edge from `R` to `N_H(v)` has differently coloured endpoints.
This is a proper three-colouring of `H`.  \(\square\)

## 3. Four full components force incompatible boundary structure

Put `H=G[X]` and choose four distinct components

\[
                         C_1,C_2,C_3,C_4                  \tag{3.1}
\]

of `G-X`.

### Lemma 3 (the boundary is triangle-free)

The graph `H` contains no triangle.

#### Proof

Suppose `q_1q_2q_3` is a triangle in `H`.  Choose three distinct
vertices `x_2,x_3,x_4` of `X-{q_1,q_2,q_3}`.  The seven sets

\[
 C_1,\quad C_2\cup\{x_2\},\quad C_3\cup\{x_3\},\quad
 C_4\cup\{x_4\},\quad \{q_1\},\quad\{q_2\},\quad\{q_3\} \tag{3.2}
\]

are pairwise disjoint and connected.  Full adjacency (1.2) supplies
every adjacency involving one of the first four sets, while the last
three are pairwise adjacent.  Hence (3.2) is a `K_7`-minor model,
contrary to (1.1).  \(\square\)

### Lemma 4 (the boundary needs at least four colours)

The graph `H` is not three-colourable.

#### Proof

Suppose that the nonempty colour classes of a proper three-colouring of
`H` are

\[
                         I_1,\ldots,I_p,qquad p\le3.       \tag{3.3}
\]

Fix a component `C` of `G-X`.  Since there are at least four components,
choose `p` other components `D_1,...,D_p`.  For every `j`, the set

\[
                         D_j\cup I_j                       \tag{3.4}
\]

is connected by (1.2), and these `p` sets are pairwise adjacent.
Contract all the sets in (3.4), delete the unused components of `G-X`,
and leave `C` untouched.  The resulting graph is a proper minor of `G`,
so it has a proper six-colouring by (1.1).

Let `d_j` be the image of (3.4).  The vertices `d_1,...,d_p` form a
clique and therefore have pairwise distinct colours.  Retain the colours
on `C`, discard the contracted components `D_j`, and give every boundary
vertex of `I_j` the colour of `d_j`.  This is a proper colouring of
`G[C\cup X]`: independence handles edges within each `I_j`, the distinct
colours handle edges between different classes, and every edge from
`I_j` to `C` was represented by an edge from `d_j` to the same vertex of
`C` in the minor.

The construction works for every component `C` of `G-X` and induces the
same labelled equality partition (3.3) on `X`.  Permute the six colour
names in the component-side colourings so that they agree on `X`, and
glue them.  Distinct components of `G-X` are anticomplete, so this gives
a proper six-colouring of `G`, contradicting (1.1).  \(\square\)

## 4. Proof of Theorem 1

Lemma 3 makes `H` triangle-free.  Since `|X|=8`, Lemma 2 gives
`chi(H)<=3`.  Lemma 4 gives `chi(H)>=4`, a contradiction.  \(\square\)

## 5. Exact scope

The proof closes an unbounded family: the complementary components may
have arbitrary order and internal structure.  It uses only their literal
full adjacency to the eight boundary vertices.

It leaves the cases of two or three full components open.  It also does
not preserve the seven old labels or either exact-seven equality
partition when an order-eight boundary is reached.  Those are still the
state-transfer obligations in the current first-entry programme.
