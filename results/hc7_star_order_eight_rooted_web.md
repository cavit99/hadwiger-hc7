# The rooted web forced by the exact order-eight star boundary

**Status:** written proof; exact revision internally audited in
[`hc7_star_order_eight_rooted_web_audit.md`](hc7_star_order_eight_rooted_web_audit.md).  This
theorem classifies the remaining order-eight outcome of the five-support
star branch.  It does not by itself eliminate that outcome or prove the
support-six transversal theorem.

## 1. Setup

Let `G` be seven-connected and `K_7`-minor-free.  Let

\[
                         L=\{\ell_1,\ldots,\ell_5\}
\]

be a five-clique.  For distinct indices `i,j`, let `e_i,e_j` be
vertex-disjoint edges outside `L` such that `e_k` is anticomplete to
`ell_k` and collectively adjacent to `L-{ell_k}`.  Put

\[
 R=L-\{\ell_i,\ell_j\},\qquad J=G-R,
\]

and let `Q` be obtained from `J` by contracting `e_i,e_j` to vertices
`z_i,z_j`.  Assume:

1. `Q` has no cut of order at most two;
2. `Q` has a cut of order three;
3. every cut of order three in `Q` contains both `z_i,z_j`;
4. `Q` has no `K_4` minor rooted at
   `ell_i,ell_j,z_i,z_j`;
5. `e_i` and `e_j` are anticomplete;
6. `G-L` contains a five-clique `Y` disjoint from `L`; and
7. for every three-vertex cut `T={z_i,z_j,x}` of `Q`, if

   \[
      S_T=R\cup V(e_i)\cup V(e_j)\cup\{x\},
   \]

   then every component of `G-S_T` is adjacent to every vertex of
   `S_T`.

These hypotheses are exactly the branch left after the order-seven
separator outputs of
[`../results/hc7_star_kernel_rooted_four_contraction.md`](../results/hc7_star_kernel_rooted_four_contraction.md)
have been excluded.  Indeed, seven-connectivity gives every component
behind a lifted three-cut at least seven neighbours in its eight-vertex
boundary; failure of hypothesis 7 is therefore precisely an actual
order-seven separator of the kind already returned by that theorem.
Hypothesis 5 is the other conclusion of its unresolved order-eight
branch.  The clique `Y` is supplied by the preceding five-support star
reduction.

## 2. The missing linkage has a forced pairing

### Lemma 2.1

The graph `Q` contains each of the following two linkages:

\[
 (\ell_i\ell_j,z_i z_j),
 \qquad
 (\ell_i z_j,\ell_j z_i).                              \tag{2.1}
\]

It does not contain an `(ell_i z_i,ell_j z_j)` linkage.

#### Proof

The two paths in the second linkage are the two vertex-disjoint edges
`ell_i z_j` and `ell_j z_i`.  They exist because `e_j` is collectively
adjacent to `ell_i`, and `e_i` is collectively adjacent to `ell_j`.

For the first linkage, take the edge `ell_i ell_j`.  Choose a
three-cut `T={z_i,z_j,x}` of `Q`.  The graph `Q-T` has at least two
components.  Since `Q` has no cut of order at most two, every component
of `Q-T` has a neighbour at each of the three vertices of `T`: otherwise
the at most two vertices of `T` which it does meet would separate it
from another component of `Q-T`.  If neither `ell_i` nor `ell_j` equals
`x`, their mutual edge puts them in the same component of `Q-T`; if one
equals `x`, the other lies in at most one component.  In either case
some component `D` of `Q-T` avoids both `ell_i,ell_j`.  Connectedness of
`D` and its contacts with `z_i,z_j` give a `z_i-z_j` path whose internal
vertices lie in `D`.  This path is disjoint from the edge
`ell_i ell_j`, proving the first linkage.

If the third displayed pairing also had a linkage, Theorem 8 of
Fabila-Monroy and Wood, *Rooted K4-Minors*, would give a `K_4` minor
rooted at the four nominated vertices, contrary to hypothesis 4.
\(\square\)

### Theorem 2.2 (canonical web order)

The graph `Q` is a spanning subgraph of an

\[
                  (\ell_i,\ell_j,z_i,z_j)\text{-web}.   \tag{2.2}
\]

Equivalently, the only rooted Two-Paths obstruction is the one whose
crossing demand is

\[
                         \ell_i-z_i,qquad \ell_j-z_j.   \tag{2.3}
\]

#### Proof

By hypothesis 1, `Q` is three-connected.  Lemma 2.1 identifies the
unique missing one of the three pair-linkages on the four nominated
vertices.  Apply the Two Paths theorem in the web form used by
Fabila-Monroy and Wood (their Lemma 2): failure of the linkage in (2.3)
is equivalent to `Q` being a spanning subgraph of a web with outer order
`(ell_i,ell_j,z_i,z_j)`. \(\square\)

This conclusion retains the labels that were lost in the four-colour
boundary census: the virtual outer edge is `z_i z_j`, while the two
failed repairs are the same-index pairs in (2.3).

## 3. The second five-clique selects a facial triangle

Write the web in Theorem 2.2 as `H^+`.  Thus `H` is an embedded planar
graph with outer face

\[
                 (\ell_i,\ell_j,z_i,z_j),               \tag{3.1}
\]

every internal face is a triangle, every triangle of `H` is facial, and
for each facial triangle `T` an optional clique `X_T` is made complete
to `T` and has no other neighbours outside `X_T`.

### Lemma 3.1 (four-cliques in a web)

Every clique of order at least four in `H^+` is contained in
`T union X_T` for one facial triangle `T` of `H`.  If the clique contains
a vertex of `X_T`, then `T` is a three-vertex cut in every spanning
subgraph which contains that clique and contains an outer vertex outside
`T`.

#### Proof

The graph `H` has no four-clique.  Otherwise its plane embedding would
contain the four triangles of a `K_4`; they cannot all be faces unless
the whole embedded graph is `K_4`, whose outer face has order three,
contrary to (3.1).

Let `K` be a clique of order at least four in `H^+`.  It therefore
contains a vertex `u` of some `X_T`.  By the construction of `H^+`, every
neighbour of `u` outside `X_T` belongs to `T`, so
`K subseteq T union X_T`.

The set `K cap X_T` is nonempty and connected after `T` is deleted.  No
vertex of `X_T` has a neighbour outside `T union X_T`.  An outer vertex
outside `T` therefore lies in another component after deletion of `T`,
which proves the separator assertion. \(\square\)

### Theorem 3.2 (localization of the second clique)

There is a facial triangle

\[
                          T=\{z_i,z_j,x\}               \tag{3.2}
\]

in the web completion such that the image of `Y` in `Q` is contained in
`T union X_T`.  In particular:

1. `z_i z_j` is the virtual outer edge of this facial triangle; it is not
   an edge of `Q`;
2. `x` is distinct from `ell_i,ell_j`;
3. `Q-T` has exactly two components;
4. one component contains `ell_i,ell_j`; and
5. every vertex of the image of `Y` outside `T` lies in the other
   component, which is contained in `X_T`.

After lifting the two contractions, (3.2) gives an eight-vertex boundary

\[
                 R\cup V(e_i)\cup V(e_j)\cup\{x\}       \tag{3.3}
\]

whose two open components separate the two original five-cliques in the
stated way.

#### Proof

Because the two defect edges are anticomplete, the clique `Y` meets the
endpoints of at most one of them.  Contracting `e_i,e_j` therefore
identifies at most one pair of vertices of `Y`.  Its image in `Q` is a
clique of order at least four.

Apply Lemma 3.1 to that image.  It is contained in `T union X_T` for a
facial triangle `T`, and `T` is a three-vertex cut of `Q`: at least one
outer nominated vertex lies outside `T`, while the image of `Y` contains
a vertex of `X_T`.  Hypothesis 3 now forces
`{z_i,z_j} subseteq T`; write its third vertex as `x`.  Since the outer
order is (3.1), `z_i z_j` is an outer edge of the web completion.  Its
absence in `Q` follows from the anticompleteness of the two original
defect edges.

We next show that `x` is not one of the other two outer vertices.  If,
for example, `x=ell_i`, then the facial triangle incident with the outer
edge `z_i z_j` uses the diagonal `z_i ell_i` of the outer four-cycle.
Deleting the two ends of this diagonal separates `ell_j` from `z_j` in
the planar graph `H`: they lie in the two regions cut off by the
diagonal.  Adding the cliques `X_U` does not reconnect these regions,
because each such clique has neighbours only in its supporting facial
triangle.  Thus `{z_i,ell_i}` is a cut of order two in the whole web
completion and hence also separates those two surviving outer vertices
in its spanning subgraph `Q`, contrary to hypothesis 1.  The case
`x=ell_j` is symmetric.

The lifted separator is the eight-vertex set `S_T` in hypothesis 7, so
every component of `G-S_T` is adjacent to all eight boundary vertices.
There are at least two such components because `T` is a cut of `Q`.
There cannot be three.  Indeed, if `C_1,C_2,C_3` are three of them and
`e_j=a_jb_j`, then

\[
 C_1\cup\{a_j\},\quad C_2\cup\{b_j\},\quad
 C_3\cup\{x\},\quad e_i,\quad \{r\}\ (r\in R)
\]

are seven pairwise disjoint connected branch sets.  Full boundary
adjacency supplies every adjacency except those internal to the displayed
boundary sets; `a_jb_j` joins the first two branch sets, and the clique
`R` together with the collective adjacency of `e_i` supplies the
remaining ones.  They form a `K_7` minor, contrary to the setup.  Hence
there are exactly two components.

The edge `ell_i ell_j` puts the two outer roots in one component of
`Q-T`.  Every vertex of `X_T` has no neighbour outside `T union X_T`,
and the part of the image of `Y` in `X_T` is connected.  It consequently
lies in the other component.  Lifting the contractions gives the final
assertion. \(\square\)

## 4. Consequence and remaining exchange

The exact order-eight residue is therefore not an arbitrary pair of
four-colour boundary-extension languages.  It is a labelled rooted
Two-Paths obstruction with one virtual outer edge.  One open component
contains the two omitted vertices of the original clique `L`; the other
contains the nonboundary part of the second clique `Y`.

The remaining constructive theorem must realize the virtual edge
`z_i z_j` by disjoint connected expansions of `e_i,e_j`, or show that
failure of this realization has one of the two global outputs already
allowed by the support-six programme:

1. an actual order-seven separation preserving the two named defect
   edges and the two five-cliques, with a strict induction parameter; or
2. a two-vertex set meeting every support in `mathcal F_6(G)`.

Static independent-block traces cannot supply this step, by
[`../barriers/hc7_star_order_eight_boundary_state_barrier.md`](../barriers/hc7_star_order_eight_boundary_state_barrier.md).

## Source boundary

The external theorem used above is R. Fabila-Monroy and D. R. Wood,
*Rooted K4-Minors*, Electronic Journal of Combinatorics 20(2) (2013),
P64, especially their Lemma 2 and Theorem 8.  The canonical
pairing and the localization of the second five-clique are deductions for
the present exact boundary.
