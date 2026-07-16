# Rooted-four contraction dichotomy in the five-support star branch

**Status:** written proof; separately audited in
[`hc7_star_kernel_rooted_four_contraction_audit.md`](hc7_star_kernel_rooted_four_contraction_audit.md).
This note does not prove the five-support star branch or Hadwiger's
conjecture for `t=7`.

## 1. Setup

Let `G` be a seven-connected graph with no `K_7` minor.  Let

\[
L=\{\ell_1,\ldots,\ell_5\}
\]

induce a literal `K_5`.  Suppose that, for each `k`, there is an edge
`e_k` in `G-L` which is anticomplete to `ell_k` and collectively adjacent
to every vertex of `L-{ell_k}`.  These are exactly the normalized defect
edges supplied by Theorem 2.3 of
[`../results/hc7_star_private_transversal_large_kernel.md`](../results/hc7_star_private_transversal_large_kernel.md).

Fix distinct `i,j` for which

\[
e_i=a_ib_i,\qquad e_j=a_jb_j
\]

are vertex-disjoint.  Put

\[
R=L-\{\ell_i,\ell_j\},\qquad J=G-R,
\]

and let `Q` be obtained from `J` by contracting `e_i` and `e_j` to
vertices `z_i` and `z_j`, respectively.  The four vertices

\[
             \ell_i,\ \ell_j,\ z_i,\ z_j                 \tag{1.1}
\]

are called the nominated vertices of `Q`.

For the refinement in Section 4, assume additionally that `G-L` contains
a literal `K_5` denoted by `Y`, and that neither defect edge has the
distinguished star centre `p` as an endpoint, where `p in Y`.  These
additional facts are supplied by Theorems 2.3 and 2.4 of the cited note.

## 2. A rooted `K_4` gives the required `K_7`

### Lemma 2.1

The graph `Q` has no `K_4` minor rooted at the four vertices in (1.1).

#### Proof

Suppose that `Q` has four pairwise disjoint, pairwise adjacent, connected
branch sets

\[
             B_i,B_j,D_i,D_j
\]

containing `ell_i,ell_j,z_i,z_j`, respectively.  Lift these branch sets
through the two contractions.  Thus the lift of `D_i` contains the whole
edge `e_i`, and the lift of `D_j` contains the whole edge `e_j`.  Lifting
preserves connectedness, disjointness, and every adjacency between the
four branch sets.

Every vertex `r in R` is adjacent to `ell_i` and `ell_j`, because `L` is
a clique.  It is also adjacent to the lifted `D_i` and `D_j`: the edge
`e_i` is collectively adjacent to `r`, since `r != ell_i`, and similarly
for `e_j`.  The three vertices of `R` are pairwise adjacent.  Consequently
the four lifted branch sets together with the three singleton branch sets
`{r}`, `r in R`, form a `K_7` minor model in `G`, a contradiction. \(\square\)

## 3. Exact lifting of small separators

### Lemma 3.1

Let `X` be a vertex cut of `Q`, and write

\[
 r_X=|X\cap\{z_i,z_j\}|.
\]

Replace each `z_k in X` by the two endpoints of `e_k`, obtaining a set
`X^uparrow` in `J`.  Then

\[
             R\cup X^\uparrow                              \tag{3.1}
\]

is a vertex cut of `G` of order

\[
             |X|+r_X+3.                                    \tag{3.2}
\]

In particular:

1. `Q` has no cut of order at most one;
2. every cut of order two is exactly `{z_i,z_j}` and lifts to an
   order-seven separation of `G`;
3. every cut of order three contains at least one of `z_i,z_j`;
4. a cut of order three containing exactly one of `z_i,z_j` lifts to an
   order-seven separation of `G`; and
5. a cut of order three containing both `z_i,z_j` lifts by this argument
   only to an order-eight separation of `G`.

#### Proof

Let `phi:J -> Q` be the contraction map.  Every component of `Q-X` has
a nonempty inverse image in `J-X^uparrow`, and distinct components have
no edge between their inverse images.  Hence `X^uparrow` is a vertex cut
of `J`.  Deleting the additional three vertices `R` shows that (3.1) is
a vertex cut of `G`.  Replacing a contracted vertex by the two endpoints
of its edge increases the order by one, which proves (3.2).

Seven-connectivity gives `|X|+r_X+3>=7`.  Substitution for
`|X|<=3` yields all five assertions.  In the order-seven cases, both
open sides are nonempty because they contain the nonempty inverse images
of two components of `Q-X`; hence these are actual separations, not merely
formal vertex cuts. \(\square\)

### Corollary 3.2 (rooted-four contraction dichotomy)

At least one of the following occurs:

1. `G` contains a `K_7` minor;
2. `G` has an actual order-seven separation obtained from a cut of `Q`
   of order two, or from a cut of order three containing exactly one of
   `z_i,z_j`;
3. `Q` has a three-vertex cut containing both `z_i,z_j`, which lifts by
   Lemma 3.1 to an order-eight separation; or
4. `Q` is four-connected and planar, and the four nominated vertices lie
   on a common face.

#### Proof

If `Q` is four-connected, apply Theorem 6 of Fabila-Monroy and Wood,
*Rooted K4-Minors*, Electronic Journal of Combinatorics 20(2) (2013),
P64, <https://doi.org/10.37236/3476>.  Their theorem says that a
four-connected graph either contains a `K_4` minor rooted at four given
vertices or is planar with those vertices on a common face.  Lemma 2.1
excludes the first outcome unless `G` already has a `K_7` minor.

If `Q` is not four-connected, Lemma 3.1 lists all possible cuts of order
at most three and gives the stated lifted separations. \(\square\)

The order-eight outcome in item 3 is not claimed to be an order-seven
separation.  Eliminating or orienting that exceptional cut remains an
open obligation.

## 4. Refinement using the second literal five-clique

### Lemma 4.1

Assume outcome 4 of Corollary 3.2 and let `Y` be the second literal
`K_5` from the setup.  Then both `e_i` and `e_j` are edges of `Y`.

#### Proof

If at most one of the two contractions identifies two vertices of `Y`,
then the image of `Y` in `Q` contains a literal `K_4`: contracting an
edge with at most one endpoint in `Y` does not identify two vertices of
`Y`, while one contraction internal to `Y` reduces its five distinct
images only to four.

A four-connected planar graph containing a literal `K_4` is itself
`K_4`.  Indeed, in a planar embedding the four triangles of that `K_4`
bound its four faces.  Any component outside the clique lies in one of
those faces and has all its attachments in the bounding triangle, which
would give a vertex cut of order at most three.  Four-connectivity rules
this out.  But if `Q=K_4`, its four nominated vertices are its four
vertices and themselves form a rooted `K_4`, contrary to Lemma 2.1.
Therefore both contractions identify pairs of vertices of `Y`, as
claimed. \(\square\)

Since the defect edges are disjoint and neither contains `p`, Lemma 4.1
also says that they form a perfect matching of the four-clique `Y-{p}`.

### Lemma 4.2

Under the hypotheses of Lemma 4.1, the four nominated vertices induce
the chordless cycle

\[
             z_i z_j \ell_i \ell_j z_i,               \tag{4.1}
\]

and this cycle bounds their common face in the planar graph `Q`.  The
triangle

\[
             z_i z_j p                                \tag{4.2}
\]

also bounds a face.  Thus the faces in (4.1) and (4.2) are the two faces
incident with the edge `z_i z_j`.

#### Proof

Because `Y` is a clique and the two contracted edges lie in `Y`, the
edges `z_i z_j`, `z_i p`, and `z_j p` are present in `Q`.  Since `L` is
a clique, `ell_i ell_j` is present.  Collective adjacency of `e_i` to
`L-{ell_i}` gives `z_i ell_j`, and collective adjacency of `e_j` to
`L-{ell_j}` gives `z_j ell_i`.  On the other hand, the anticompleteness
conditions give

\[
             z_i\ell_i,\ z_j\ell_j\notin E(Q).
\]

This proves that the nominated vertices induce the cycle (4.1).

In a three-connected plane graph, every facial boundary is an induced
cycle: a chord of a facial cycle, together with its two boundary arcs,
would make the endpoints of the chord a vertex cut of order at most two.
The four nominated vertices lie on one facial boundary by Corollary 3.2,
and all four edges of their induced cycle are present.  Each root must
therefore be consecutive on that boundary to its two neighbours in
(4.1).  The boundary is exactly (4.1).

Finally, a triangle in a four-connected plane graph is facial.  If it
had vertices on both sides, its three vertices would be a cut; if all
remaining vertices lie on one side, the other side is a face.  Apply
this to (4.2).  Both facial cycles contain `z_i z_j`, so they are the two
faces incident with that edge. \(\square\)

## 5. The five defect edges eliminate the planar outcome

The planar outcome for one pair need not be contradictory by itself.  The
fact that there are five distinct normalized defect edges is enough to
eliminate it simultaneously for every disjoint pair.

### Lemma 5.1

It is impossible that the quotient `Q` is four-connected for every pair
of vertex-disjoint edges among `e_1,...,e_5`.

#### Proof

Assume the contrary.  Fix one disjoint pair `e_i,e_j`, which exists by
Theorem 2.3 of the star-kernel note cited in Section 1.  Lemma 4.1 says
that both edges lie in the second clique `Y`.

Consider any other defect edge `e_k`.  If it meets both `e_i` and `e_j`,
then, because those two edges are disjoint, its two endpoints consist of
one endpoint of `e_i` and one endpoint of `e_j`.  Hence `e_k` lies in
`Y`.  Otherwise `e_k` is disjoint from at least one of `e_i,e_j`.
Apply Lemma 4.1 to that disjoint pair; the standing assumption that its
quotient is four-connected again shows that `e_k` lies in `Y`.

Thus all five distinct defect edges lie in the four-clique

\[
                         W=Y-\{p\}.
\]

They are exactly five of the six edges of `W`; let `f` be the unselected
sixth edge.  We claim that `f` is collectively adjacent to every vertex
of `L`.

Fix `ell_k` and write `e_k=ab`, with `W-{a,b}={c,d}`.  Of the two edges
`ac,bc`, at most one is the unselected edge `f`, so at least one is a
selected defect edge `e_h`, where `h != k`.  The edge `e_h` is
collectively adjacent to `ell_k`, while `ell_k` is anticomplete to
`{a,b}`.  Therefore `c` is adjacent to `ell_k`.  The same argument with
`ad,bd` shows that `d` is adjacent to `ell_k`.  Since `f != e_k`, at
least one endpoint of `f` belongs to `{c,d}`.  This proves the claim.

Now put

\[
                         S=L\cup V(f),
\]

so `|S|=7`, and let `D` be the component of `G-S` containing `p`.
For every `s in S`, the vertex `s` has a neighbour in `D`.  Otherwise
`N_G(D)` would be a subset of `S-{s}` of order at most six, and deleting
it would separate the nonempty set `D` from the still present vertex
`s`, contrary to seven-connectivity.

Consequently `D` and the edge `f` are disjoint connected subgraphs,
adjacent to each other and each adjacent to every vertex of `L`.  Together
with the five singleton vertices of the clique `L`, they form a `K_7`
minor model in `G`, a contradiction. \(\square\)

### Theorem 5.2 (separator output)

For at least one vertex-disjoint pair among `e_1,...,e_5`, its contracted
graph `Q` has one of the following:

1. a two-vertex cut `{z_i,z_j}`, whose lift is an actual order-seven
   separation of `G`;
2. a three-vertex cut containing exactly one of `z_i,z_j`, whose lift is
   an actual order-seven separation of `G`; or
3. a three-vertex cut containing both `z_i,z_j`, whose direct lift is an
   actual order-eight separation of `G`.

#### Proof

Choose a vertex-disjoint defect-edge pair whose quotient is not
four-connected, as supplied by Lemma 5.1.  Lemma 2.1 excludes the
four-vertex exceptional graph, because its four nominated vertices would
themselves form a rooted `K_4`.  Lemma 3.1 now gives exactly the three
listed possibilities. \(\square\)

Thus the four-connected planar outcome is no longer part of the global
five-edge residual.  The exact remaining obligation is to orient or
strictly descend through the two order-seven outputs, or to eliminate the
honest order-eight output in item 3.  This draft does not claim that the
order-eight separator can automatically be trimmed to order seven.

## 6. The order-eight output is either trim-able or has two full components

### Lemma 6.1

In item 3 of Theorem 5.2, write the three-cut of `Q` as

\[
                         \{z_i,z_j,x\}
\]

and put

\[
             S=R\cup V(e_i)\cup V(e_j)\cup\{x\}.       \tag{6.1}
\]

Thus `|S|=8`.  Then either:

1. `G` has an actual order-seven separation; or
2. `G-S` has exactly two components, both are adjacent to every vertex
   of `S`, and there is no edge between `e_i` and `e_j`.

In the second outcome `G[S]` is four-colourable.

#### Proof

The components of `G-S` are the nonempty inverse images of the components
of `Q-{z_i,z_j,x}`.  In particular, there are at least two.  For every
component `D` of `G-S`,

\[
                         N_G(D)\subseteq S.
\]

Seven-connectivity gives `|N_G(D)|>=7`.  If equality holds for some
`D`, then `N_G(D)` is an actual order-seven separator: `D` is one open
side, and the inverse image of any other component remains on the other
side.  Otherwise every component has all eight vertices of `S` in its
neighbourhood.

Suppose that an edge joins `e_i` and `e_j`, and choose two components
`C,D` of `G-S`.  The seven connected branch sets

\[
 C\cup\{x\},\quad D,\quad e_i,\quad e_j,
 \quad\{r\}\ (r\in R)                                \tag{6.2}
\]

are pairwise adjacent.  Fullness makes `C` and `D` adjacent to every
boundary branch set, and `D` is adjacent to `C union {x}` through a
neighbour of `x`.  The assumed cross-edge joins the two edge branch sets;
each defect edge is collectively adjacent to every vertex of `R`; and
`R` is a clique.  Hence (6.2) is a `K_7` minor model, a contradiction.
Thus the two defect edges are anticomplete.

There cannot be three or more components.  If `C_1,C_2,C_3` are three
of them and `e_j=a_jb_j`, use the seven branch sets

\[
 C_1\cup\{a_j\},\quad C_2\cup\{b_j\},\quad
 C_3\cup\{x\},\quad e_i,
 \quad\{r\}\ (r\in R).                               \tag{6.3}
\]

Each of the first three sets is connected by fullness.  The first two
are adjacent through `a_jb_j`; the third is adjacent to each through its
neighbours at `a_j,b_j`; and fullness makes all three adjacent to `e_i`
and to every singleton in `R`.  Finally `e_i` is collectively adjacent
to every vertex of `R`, and `R` is a clique.  Thus (6.3) is another
`K_7` minor model.  Since at least two components already exist, there
are exactly two.

Choose two components in outcome 2.  They are nonempty, connected,
pairwise anticomplete, and each is adjacent to every vertex of the
eight-set `S`.  The audited boundary-absorption theorem in
[`../results/hc7_two_full_shore_boundary_absorption.md`](../results/hc7_two_full_shore_boundary_absorption.md)
therefore implies that `G[S]` is four-colourable. \(\square\)

Combining Theorem 5.2 and Lemma 6.1, the five-support star branch now
returns either an actual order-seven separation, or an eight-vertex
boundary inducing a four-colourable graph whose complement has exactly two
components, each adjacent to every boundary vertex; the two distinguished
defect edges in that boundary are anticomplete.
The remaining difficulty is state-preserving colouring composition across
that boundary; four-colourability alone does not perform the composition.
