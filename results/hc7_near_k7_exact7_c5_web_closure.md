# Complete unbounded closure of the sharp `C5` full-shore core

## Theorem

### Theorem 1 (full `C5` web closure)

Let `G` be a seven-connected graph, let

\[
 S=\{q_0,q_1,q_2,q_3,q_4,r_1,r_2\},
 \qquad G[S]=C_5\vee K_2,                            \tag{1}
\]

where `q_0q_1q_2q_3q_4q_0` is the displayed cycle.  Suppose `G-S` has
exactly two components `D_1,D_2`, and

\[
 N(D_1)=N(D_2)=S.                                   \tag{2}
\]

Then at least one of the following holds:

1. `G` contains a `K_7` minor;
2. `G` is six-colourable.

Consequently this sharp separator cannot occur in a proper-minor-minimal
counterexample to `HC_7`.

## Proof

For `j in {1,2}` and `i in Z_5`, put

\[
 P_i^j=N_{D_j}(q_i).
\]

All ten portal sets are nonempty by (2).  Form an auxiliary graph `A_j`
from `G[D_j]` by adding five independent terminal vertices
`t_0,...,t_4`, with `t_i` adjacent precisely to `P_i^j`.  Order the
terminals as

\[
 T=(t_0,t_1,t_2,t_3,t_4)                            \tag{3}
\]

in the cyclic order of the cycle in (1).

### Claim 1: a crossed terminal tuple gives `K_7`

A crossing of the five-term tuple uses four terminals.  Up to rotation
and reflection, its disjoint paths join `t_0` to `t_2` and `t_1` to
`t_4`.  Removing the artificial ends gives disjoint paths in `D_j`
joining `P_0^j` to `P_2^j` and `P_1^j` to `P_4^j`.  Enlarge their vertex
sets to disjoint connected sets `Y,X` that are adjacent: if necessary,
take a shortest connector in connected `D_j` and split it at an edge.

Let `k=3-j` be the opposite shore.  The seven bags

\[
 \{q_0\},\quad\{q_1\},\quad\{r_1\},\quad\{r_2\},
 \quad X\cup\{q_4\},\quad Y\cup\{q_2\},\quad D_k    \tag{4}
\]

form a `K_7` model.  The first four form a clique.  The `X`-bag sees
`q_0` through `q_4q_0` and `q_1` through its portal contact; the `Y`-bag
sees `q_1` through `q_2q_1` and `q_0` through its portal contact.  They
see each other by construction and see `r_1,r_2` through their cycle
anchors.  The full opposite shore sees every boundary-containing bag.
This checks all adjacencies in (4).

Assume outcome 1 of the theorem does not hold.  Claim 1 says that the
tuple (3) is crossless in each `A_j`.  By the generalized Two Paths
Theorem (Humeau--Pous, Theorem 1.5), each `A_j` has an edge-only
completion to a `5`-web `W_j` with frame (3).  In particular the
completion has exactly the same vertex set as `A_j`; only edges are
added.  Write `R_j` for its planar rib.  A web is obtained from its rib
by inserting, in each facial triangle, a clique whose vertices have no
neighbours outside that clique and the three triangle vertices.

### Claim 2: no original shore vertex is an inserted clique vertex

Suppose the clique inserted in one facial triangle `F` of `R_j` is
nonempty, and let `X subseteq D_j` be its entire vertex set.  This
containment holds because the completion has the vertex set of `A_j`
and every artificial terminal is a frame (hence rib) vertex.  Every
neighbour of `X` represented in `A_j` is one of the at most three
vertices of `F`.
Replacing any terminal of `F` by its corresponding boundary vertex
`q_i` accounts for every edge from `X` to the five cycle vertices.  In the
original graph the only additional possible neighbours are `r_1,r_2`:
the two shores are anticomplete and there is no third component.  Hence

\[
 |N_G(X)|\le3+2=5.                                  \tag{5}
\]

The set in (5) separates `X` from the nonempty opposite shore, contrary
to seven-connectivity.  This proves the claim.

It follows that every original vertex and edge of `A_j` lies in the
planar rib `R_j`.  Replace `t_i` by `q_i` and add the five frame edges
`q_iq_{i+1}`.  Thus

\[
 G[D_j\cup\{q_0,...,q_4\}]
\]

has a plane embedding in a closed disk whose boundary is the displayed
five-cycle.

Use such an embedding for `D_1` on one side of the cycle and one for
`D_2` on the other side.  Because the two shores are anticomplete, they
glue without crossings.  Therefore

\[
 P:=G-\{r_1,r_2\}                                   \tag{6}
\]

is planar.  By the Four Color Theorem, `P` is four-colourable.  Finally,
`G` is a subgraph of `K_2\vee P`, with `r_1,r_2` as the `K_2`.  Give the
two vertices two new colours.  This is a six-colouring of `G`, proving
outcome 2. \(\square\)

## Scope and audit points

The proof does not assume planarity of a shore.  Planarity is forced only
after all five portal-linkage failures are packaged into one crossless
five-terminal tuple and the web's inserted cliques are removed by the
global seven-connectivity cut (5).

The opposite shore is used twice and in different ways:

* as the seventh branch set when a crossing exists; and
* as the vertex set lying beyond the forbidden cut in Claim 2.

The artificial terminals never become branch-set vertices.  They merely
encode the five portal sets; in (4) they are replaced by the corresponding
actual boundary roots.
