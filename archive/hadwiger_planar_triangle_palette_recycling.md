# Palette recycling closes the rooted-triangle planar frame

This note records a direct colouring lemma for the planar outcome in
Theorem 2.10 of `hadwiger_near_k7_two_complex_bag_round.md`.  It is
independent of the degree-seven neighbourhood classification.

## 1. The colouring lemma

### Theorem 1.1 (cofacial common-neighbour palette recycling)

Let (G) be a graph and let (T={q_1,q_2,q_3}) induce a triangle.
Put (J=G-T).  Suppose that

1. (J) has a plane embedding; and
2. every vertex of (J) adjacent to all three vertices of (T) lies on
   the boundary of one face (F) of this embedding.

Then

\[
   \chi(G)\le 6.
\]

#### Proof

The boundary of (F) is a closed facial walk.  Add a new vertex (z)
inside (F) and join it to every vertex occurring on that walk.  The
resulting graph (J^+) is planar: draw the new edges as noncrossing spokes
inside (F).  By the Four Colour Theorem, fix a proper colouring

\[
   c:V(J^+)\longrightarrow\{0,1,2,3\}.
\]

Let

\[
   Z=\{u\in V(J):c(u)=c(z)\}.
\]

The set (Z) is independent.  Moreover, (Z) is disjoint from the
boundary of (F), since every boundary vertex is adjacent to (z).
Consequently no vertex of (Z) is adjacent to all three vertices of
(T).

Introduce two new colours (4,5).  We shall use (c(z),4,5) on
(q_1,q_2,q_3), respectively.  Before doing so, recolour every vertex
(u\in Z\cap N_G(q_1)) as follows:

* if (u\notin N_G(q_2)), give (u) colour (4);
* otherwise give (u) colour (5).

The second instruction is legitimate: in that case (u) is adjacent to
(q_1) and (q_2), and, since (u\in Z) is not adjacent to all of
(T), it is not adjacent to (q_3).  The recoloured vertices remain
pairwise nonadjacent because they all belonged to the independent set
(Z).  Neither colour (4) nor colour (5) was previously used on
(J), so this recolouring creates no other monochromatic edge in (J).

Now colour

\[
   q_1\text{ with }c(z),\qquad q_2\text{ with }4,
   \qquad q_3\text{ with }5.
\]

The three colours are distinct, so the edges of (T) are proper.  All
old-colour neighbours of (q_1) in (Z) were recoloured.  A vertex
recoloured (4) was chosen to miss (q_2), and a vertex recoloured (5)
was proved to miss (q_3).  Thus no edge between (T) and (J) is
monochromatic.  We have obtained a proper six-colouring of (G).
\(\square\)

### Remark 1.2

No saturation hypothesis is used.  The argument only needs a four-colour
class avoiding all common neighbours of the triangle; cofaciality supplies
such a class by the auxiliary-vertex construction.

## 2. Consequence for the near-(K_7) branch

### Corollary 2.1 (the planar-frame outcome is impossible in an HC7
counterexample)

Let (G) be a seven-chromatic graph satisfying the hypotheses of Theorem
2.10 in `hadwiger_near_k7_two_complex_bag_round.md`: (T) is a triangle,
(J=G-T) is planar, and all vertices complete to (T) occur on a common
face of (J).  Then no such (G) exists.

#### Proof

Theorem 1.1 gives (chi(G)\le6), contrary to (chi(G)=7).
\(\square\)

In particular, in a hypothetical minor-minimal counterexample to
Hadwiger's conjecture for (t=7), the rooted-triangle frame alternative of
Theorem 2.10 cannot occur.  Hence the six degree-seven vertices exported
by Corollary 2.11 never need a Moser-neighbourhood classification.  The
fact that their five cyclically ordered (J)-neighbours need not induce a
(C_5) is therefore harmless.

## 3. Exact audit of the tempting Moser inference

Equality (d_{J^+}(x)=d_J(x)) alone does not say that the link edges added
by the triangulation were already present in (J).  In the present setting,
however, four-connectivity and Dirac's independence bound repair this gap.

### Lemma 3.1 (the five neighbours really induce a cycle)

Let (J) be a four-connected plane graph, let (x) be an interior vertex
of degree five, and list its neighbours as
(y_0,y_1,y_2,y_3,y_4) in their cyclic order about (x).  If
(alpha(J[N_J(x)])\le2), then

\[
   J[N_J(x)]=y_0y_1y_2y_3y_4y_0.
\]

#### Proof

An edge (y_i y_j) between nonconsecutive neighbours, together with the
two edges to (x), is a triangle having at least one of the other
neighbours of (x) on each side.  The set ({x,y_i,y_j}) would
therefore separate (J), contrary to four-connectivity.  Hence
(J[N_J(x)]) is a subgraph of the cyclic five-edge graph.  Deleting any
edge from a (C_5) leaves a graph with an independent set of order three.
The independence hypothesis consequently forces all five cyclic edges.
\(\square\)

For a degree-seven vertex exported by Corollary 2.11, Dirac gives
(alpha(G[N_G(x)])\le2), so it gives the hypothesis of Lemma 3.1 on the
five (J)-neighbours.  Thus the induced-(C_5) conclusion is valid, but
not for the triangulation-equality reason alone.

The stronger inference that the whole seven-vertex neighbourhood is the
one-edge Moser extension is still false in the sole-exterior cell.  Write
(p,q) for the two adjacent triangle neighbours of (x), and write the
cycle as (012340).  A subtle anchor issue matters here.  An exterior
component has no edge to (x).  Therefore a local (K_5)-model upgrades
with that component and ({x}) only when the model uses at most six of
the seven boundary vertices: the unused boundary vertex must be attached
to the exterior component to make the sixth bag meet (N(x)).  A
(K_5)-model using all seven boundary vertices does not by itself close
the cell.

The exact immediate local exclusions are consequently:

1. no (K_6)-minor in (G[N(x)]), since ({x}) upgrades it; and
2. no (K_5)-minor supported on at most six vertices of (N(x)), since
   the unused vertex anchors the sole full exterior component.

Under these exact exclusions, Dirac's bound, and the induced (C_5), the
incidence census has **twelve** orbits, not one or two.  In fact the two
minor exclusions remove none of the Dirac-admissible incidence patterns.
Every neighbourhood is a subgraph of (K_2\vee C_5), which has Hadwiger
number (2+\eta(C_5)=5), so there is no local (K_6).  After deleting
either triangle vertex it is a subgraph of (K_1\vee C_5), of Hadwiger
number four; after deleting a cycle vertex it is a subgraph of
(K_2\vee P_4), also of Hadwiger number four.  Thus deleting any one
boundary vertex destroys every (K_5)-model, proving that no (K_5)-model
is supported on at most six vertices.

It remains only to enumerate the independence constraint.  It is most compact
to record the missing sets

\[
 M_p=C_5-N_{C_5}(p),\qquad M_q=C_5-N_{C_5}(q).
\]

Indeed, (p) together with two nonadjacent vertices of (C_5) would be
an independent triple exactly when (M_p) were not a clique; hence each
missing set is empty, a singleton, or a cycle edge, and this condition is
also sufficient.  Up to a dihedral symmetry and interchange of (p,q),
the twelve resulting pairs are

\[
\begin{array}{c|c@{\qquad}c|c}
 &M_p&M_q&|E(G[N(x)])|\\ \hline
1&34&34&12\\
2&34&23&12\\
3&34&12&12\\
4&4&34&13\\
5&4&23&13\\
6&34&1&13\\
7&4&4&14\\
8&\varnothing&34&14\\
9&4&3&14\\
10&4&2&14\\
11&\varnothing&4&15\\
12&\varnothing&\varnothing&16.
\end{array}
\tag{3.1}
\]

Orbit 3 is the one-edge Moser extension.  Orbit 6 is obtained from it by
one extra incidence.  The other ten orbits show decisively that the
two-helper Moser classification cannot be imported into the sole-exterior
frame.

The dependency-free verifier `planar_frame_c5_k5minor_probe.py` checks all
(2^{10}) incidence sets, all independent triples, every branch-set
partition for a (K_5)-model on five or six used vertices, and every
possible (K_6)-model on seven vertices.  It returns the twelve orbits in
(3.1), comprising 121 labelled incidence sets.  The palette-recycling
theorem makes this finite residue unnecessary for the planar-frame
closure.
