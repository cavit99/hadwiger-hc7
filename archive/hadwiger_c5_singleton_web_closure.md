# Complete closure of the singleton-shore sharp `C5` cell

## 1. Statement

### Theorem 1.1

Let `G` be a seven-connected graph with a separation whose adhesion is

\[
 S=\{q_0,q_1,q_2,q_3,q_4,r_1,r_2\},
 \qquad G[S]=C_5\vee K_2,                            \tag{1.1}
\]

where `q_0 q_1 q_2 q_3 q_4 q_0` is the displayed cycle and
`r_1r_2` is the `K_2`.  Suppose `G-S` has exactly two components, one of
which is a singleton `{v}`, and both components have neighbourhood exactly
`S`.  If `G` is not six-colourable, then `G` contains a `K_7` minor.

Equivalently, this configuration cannot occur in a proper-minor-minimal
counterexample to `HC_7`.

The proof is unbounded in the order of the other component.  Its only
external ingredients are the generalized Two Paths Theorem and the Four
Color Theorem.

## 2. The five-terminal shore graph

Let `D` be the nonsingleton component of `G-S`, and for `i in Z_5` put

\[
 P_i=N_D(q_i).
\]

Every `P_i` is nonempty because `N(D)=S`.  Form an auxiliary graph `A`
from `G[D]` by adding five new terminals `t_0,...,t_4`, with `t_i`
adjacent precisely to `P_i`.  There are no terminal-terminal edges.  Give
the terminals the cyclic order

\[
 T=(t_0,t_1,t_2,t_3,t_4).                           \tag{2.1}
\]

### Lemma 2.1

If `T` is crossed in `A`, then `G` contains a `K_7` minor.

### Proof

A crossing of a five-term tuple chooses four terminals.  Up to a cyclic
rotation and reflection, its two paths join `t_0` to `t_2` and `t_1` to
`t_4`.  Removing the artificial terminal ends gives two vertex-disjoint
paths in `D`, one joining `P_0` to `P_2` and the other joining `P_1` to
`P_4`.

Enlarge the two paths to disjoint connected sets `Y,X subseteq D` that
are adjacent.  If necessary, join them by a shortest path in connected
`D` and split that connector at an edge.  Now use the seven bags

\[
 \{q_0\},\quad\{q_1\},\quad\{r_1\},\quad\{r_2\},
 \quad X\cup\{q_4\},\quad Y\cup\{q_2\},\quad\{v\}.
                                                               \tag{2.2}
\]

The first four bags form a clique.  The `X`-bag sees `q_0` through
`q_4q_0` and sees `q_1` through its `P_1` contact.  The `Y`-bag sees
`q_1` through `q_2q_1` and sees `q_0` through its `P_0` contact.  The two
bags are adjacent by construction, and their boundary anchors see
`r_1,r_2`.  Finally `{v}` sees every other bag because `N(v)=S`.
Thus (2.2) is a `K_7` model.  Every other crossing is a rotation or
reflection of this display. \(\square\)

Assume from now on that `G` has no `K_7` minor.  Lemma 2.1 makes `T`
crossless.  By the generalized Two Paths Theorem, `A` has a web
completion: after adding edges only, it is a `5`-web `W` whose frame is
the ordered terminal cycle (2.1).  A `5`-web consists of a plane
near-triangulation `R`, called its rib, with outer face `T`, together with
a clique inserted in each facial triangle; every inserted clique vertex
has neighbours outside its clique only in the three vertices of that
facial triangle.

## 3. Seven-connectivity removes every inserted clique

### Lemma 3.1

Every vertex of `D` is a rib vertex of `W`.  Consequently the graph
consisting of `D`, the five terminals, and all edges of `A` is planar with
the terminals on one face in the order (2.1).

### Proof

Suppose some original vertex of `D` is an inserted clique vertex.  Fix one
facial triangle `F` of the rib and let `X` be the nonempty set of original
vertices of `D` lying in the clique inserted in `F`.

In the auxiliary graph, every neighbour of `X` outside `X` is one of the
three vertices of `F`: edges were added to obtain the web, never deleted.
In the original graph `G`, the only additional possible neighbours are
`r_1,r_2`.  Indeed, a terminal `t_i` records exactly the edges from `D`
to `q_i`; the component `D` is anticomplete to `v`; and there is no third
component of `G-S`.  Therefore

\[
 |N_G(X)|\le |F|+2=5.                               \tag{3.1}
\]

The set `N_G(X)` separates the nonempty set `X` from `v`, contradicting
seven-connectivity.  Hence no original vertex lies in an inserted clique.
All vertices and edges of `A` therefore lie in the planar rib, proving the
last assertion. \(\square\)

The argument permits the web completion to contain additional formal
vertices: only the original vertices in an inserted clique are placed in
`X`.  If, as in the standard completion statement, the web has exactly
the original vertex set, the same proof simply takes the whole inserted
clique.

## 4. Planarity and the colouring contradiction

### Lemma 4.1

The graph

\[
 P=G-\{r_1,r_2\}
\]

is planar.

### Proof

Replace each artificial terminal `t_i` in the planar embedding from
Lemma 3.1 by the corresponding original boundary vertex `q_i`.  Add the
five cycle edges `q_iq_{i+1}` along the outer-frame boundary.  This remains
planar because those are precisely the frame edges of the rib.

The only remaining vertex of `P` is `v`.  It is adjacent to every `q_i`
and to no vertex of `D`.  Place `v` in the outer face and draw its five
incident edges inside that face.  This adds a wheel on the frame without
crossing any existing edge.  The resulting plane graph is exactly `P`.
\(\square\)

### Proof of Theorem 1.1

By the Four Color Theorem, `P` has a proper four-colouring.  The graph `G`
is a subgraph of the join

\[
 K_2\vee P,                                          \tag{4.1}
\]

where the `K_2` vertices are `r_1,r_2`: they are adjacent in `G`, and
adding any missing edges from them to `P` only forms the supergraph in
(4.1).  Colour `P` with four colours and give `r_1,r_2` two new distinct
colours.  This is a six-colouring of `K_2\vee P`, hence also of `G`,
contrary to the hypothesis.  Thus the crossless alternative is impossible;
Lemma 2.1 supplies a `K_7` minor in the other alternative. \(\square\)

## 5. Counterexample consequence

In the order-seven full-shore analysis of a hypothetical minimal
counterexample to `HC_7`, the five-edge quotient exceptions are

\[
 \overline{G[S]}=C_5+2K_1
 \quad\hbox{or}\quad
 \overline{G[S]}=K_3+2K_2.
\]

If a distinguished shore is a singleton, its neighbourhood is exactly
`S` and Dirac's degree-seven neighbourhood inequality gives
`alpha(G[S])<=2`.  The second quotient has
`G[S]=K_{3,2,2}` and independence number three, so it is impossible.
The first quotient is eliminated by Theorem 1.1.  Hence:

### Corollary 5.1

In either sharp five-edge contact core, neither of the two full shores is
a singleton.

Combined with the independently certified exclusions of shore orders
two through five, every surviving sharp contact shore has order at least
six.

