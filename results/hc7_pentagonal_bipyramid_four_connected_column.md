# Four-connected columns in a pentagonal-bipyramid expansion

**Status:** written proof; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_four_connected_column_audit.md`](hc7_pentagonal_bipyramid_four_connected_column_audit.md).

This note gives a label-preserving rooted-minor dichotomy for one column of
a pentagonal-bipyramid expansion.  It is an unbounded theorem: the column
may have arbitrary order.  It does not prove that every live column is
four-connected or that its portal matching has rank four, and it does not
by itself synchronize the planar boundary orders of different columns.

## 1. Setup

Let

\[
                         P=C_5\vee\overline {K_2}
\]

be the pentagonal bipyramid.  Suppose a graph contains pairwise disjoint
connected subgraphs

\[
                         R_0,R_1,(L_y:y\in V(P))              \tag{1.1}
\]

such that `R_0` and `R_1` are adjacent, each `R_i` is adjacent to every
`L_y`, and

\[
 E(L_y,L_z)\ne\varnothing
 \quad\Longleftrightarrow\quad yz\in E(P).                    \tag{1.2}
\]

Fix `x in V(P)`.  For every `y in N_P(x)`, define the literal portal set

\[
 Z_y=\{q\in V(L_x):N(q)\cap V(L_y)\ne\varnothing\}.           \tag{1.3}
\]

The **portal matching rank** is the maximum order of a matching in the
bipartite graph with parts `N_P(x)` and `V(L_x)`, in which `yq` is an edge
exactly when `q in Z_y`.

## 2. Completing four rooted portals

### Lemma 2.1 (four rooted portals lift to `K_7`)

Let `y_1,...,y_4` be distinct neighbours of `x`, and choose distinct
vertices `q_i in Z_{y_i}`.  If `L_x` contains a `K_4`-minor model with
branch sets `B_i` rooted at `q_i`, then the graph in (1.1)--(1.2) contains
an explicit `K_7`-minor model.

### Proof

For each `i`, choose an edge from `q_i` to `L_{y_i}` and put

\[
                              H_i=B_i\cup L_{y_i}.             \tag{2.1}
\]

These four sets are pairwise disjoint and connected.  They are pairwise
adjacent because the `B_i` form a `K_4` model.

There are exactly two labels in

\[
            V(P)-\{x,y_1,y_2,y_3,y_4\};                       \tag{2.2}
\]

call them `a,b`.  The two vertices `a,b` are adjacent in `P`, and their
union is adjacent in `P` to each `y_i`.  Indeed, if `x` is a pole, then
`a,b` are the other pole and the one unchosen rim vertex.  If `x` is a rim
vertex, then `y_1,...,y_4` are its two pole and two rim neighbours, while
`a,b` are the two remaining consecutive rim vertices.  Therefore

\[
                              H_5=L_a\cup L_b                 \tag{2.3}
\]

is connected and is adjacent to every `H_i`.

Thus `H_1,...,H_5` are branch sets of a `K_5` model.  Every one contains
at least one whole old column, so both `R_0` and `R_1` are adjacent to all
five.  The two roots are adjacent to one another.  Hence

\[
                         R_0,R_1,H_1,\ldots,H_5               \tag{2.4}
\]

are seven pairwise disjoint, connected and pairwise adjacent branch sets.
\(\square\)

## 3. Rooted minor or one facial portal order

### Theorem 3.1 (four-connected column dichotomy)

Assume that `L_x` is four-connected and its portal matching rank is at
least four.  Then at least one of the following holds.

1. The graph in (1.1)--(1.2) contains an explicit `K_7`-minor model.
2. `L_x` is planar and, in its unique plane embedding, every vertex in
   \(\bigcup_{y\in N_P(x)}Z_y\) lies on one face.

### Proof

On the union of the portal sets, take the transversal matroid whose
independent sets are the sets which can be assigned injectively to
distinct labels `y` with membership in `Z_y`.  Truncate it to rank four.
Its rank is four by hypothesis.

Let `Q={q_1,q_2,q_3,q_4}` be any basis.  Choose a representation by four
distinct labels `y_i` with `q_i in Z_{y_i}`.  If `L_x` has a `K_4` model
rooted at the four vertices of `Q`, Lemma 2.1 gives outcome 1.  We may
therefore suppose that no basis roots a `K_4` model.

The rooted-`K_4` theorem of Fabila-Monroy and Wood says that four nominated
vertices in a four-connected nonplanar graph always root a `K_4` minor.
Consequently `L_x` is planar.  The same theorem's planar case says that in
a three-connected plane graph four nominated vertices fail to root a
`K_4` minor exactly when they lie on one face.  Thus every basis of the
rank-four portal matroid lies on one face of `L_x`.

Because `L_x` is three-connected, its plane embedding is unique up to
reflection, and two distinct faces have at most two vertices in common.
The basis-exchange graph of a matroid is connected.  Consecutive bases in
that graph share three vertices, so the faces containing them cannot be
distinct.  It follows that every basis lies on one fixed face `F_x`.

Every literal portal vertex is a nonloop of the transversal matroid.  Any
nonloop extends to a basis of its rank-four truncation.  Hence every portal
vertex lies on `F_x`, proving outcome 2.  \(\square\)

## 4. Exact gain and trust boundary

The theorem turns four-connected, rank-four column societies into one of
the two outcomes needed by the live structural programme:

- a label-preserving `K_7` construction; or
- one coherent facial order containing every literal intercolumn portal of
  that column.

It does not prove that the portal matching rank is four.  Several quotient
labels may have all their literal contacts concentrated at fewer than four
vertices.  Nor does four-connectivity of the whole spanning core imply
four-connectivity of each induced column.  Finally, facial orders obtained
in different columns still have to be coupled across repeated edge
bundles.  Those are precisely the low-rank, internal-separator and global
order-compatibility branches left by this result.

## External input

R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electronic Journal
of Combinatorics **20** (2013), Paper P64, in particular the
four-connected nonplanar and three-connected planar specializations of
their characterization.
