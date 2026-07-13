# The `C_4`/common-triangle quotient forgets the actual apex vertices

## Status

The ordered path interface suggests contracting the three rows common to
both path shores to a triangle and seeking a rooted `K_4` on the four
`C_4` roles `L,R,F,H`.  The rooted-model branch is valid only when its
four branch sets avoid the common triangle.  The separator and rural
branches do not lift automatically when the three common rows are
nonsingleton.

The sharp static witness `K_2 vee I`, where `I` is the icosahedron,
contains an exact spanning `K_3 vee C_4` quotient of this form.  It is
seven-connected and `K_7`-minor-free.  Its genuine two-apex pair is
hidden inside the contracted common bags, and deleting the three common
bags destroys the ambient connectivity.  Thus a valid continuation needs
port-labelled expansion societies or a proper-minor state on the full
actual adhesions; quotient planarity and quotient separators alone are
insufficient.

The executable certificate is
`hc7_near_k7_c4_triangle_quotient_barrier_verify.py`.

## 1. Exact spanning frame

Label the icosahedron by

\[
 t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

with indices modulo five and edges

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}.
\]

Let `p,q` be adjacent universal vertices and put `G=K_2 vee I`.  Define
three common bags

\[
\begin{aligned}
 T_1&=\{p,b,w_0,w_1,w_2,w_3,w_4\},\\
 T_2&=\{q\},\\
 T_3&=\{t\},
\end{aligned}                                             \tag{1.1}
\]

and four root bags

\[
 X_1=\{u_0,u_1\},\qquad X_2=\{u_2\},\qquad
 X_3=\{u_3\},\qquad X_4=\{u_4\}.                         \tag{1.2}
\]

These seven sets partition `V(G)` and are connected.  The `T_i` are
pairwise adjacent, and every `T_i` is adjacent to every `X_j`.  Among the
four root bags the only adjacencies are

\[
                     X_1X_2,X_2X_3,X_3X_4,X_4X_1.        \tag{1.3}
\]

Indeed (1.3) is the upper five-cycle after contracting its edge
`u_0u_1`.  Contracting the seven bags therefore gives exactly

\[
                              K_3\vee C_4.                \tag{1.4}
\]

The icosahedron is five-connected, planar, and has Hadwiger number four.
Consequently

\[
       \kappa(G)=7,\qquad \delta(G)=7,\qquad \eta(G)=6.  \tag{1.5}
\]

Thus `G` is `K_7`-minor-free.  Deleting the actual vertices `p,q` leaves
the planar icosahedron, so the correct terminal outcome is coherent
two-apex.  The graph is six-colourable and hence is not a hypothetical
contraction-critical counterexample; its role is to falsify any static
quotient lift.

## 2. Why the rooted branch must avoid the triangle

In the full quotient `K_3 vee C_4`, the four cycle roots do have a rooted
`K_4` if the three triangle vertices may be consumed.  With cycle order
`x_1x_2x_3x_4x_1` and triangle `a,b,c`, take

\[
       \{x_1,a\},\quad\{x_2,c\},\quad\{x_3,b\},\quad\{x_4\}.
                                                               \tag{2.1}
\]

The cycle edges give four consecutive adjacencies, `ab` repairs the
`x_1x_3` diagonal, and `cx_4` repairs the `x_2x_4` diagonal.  But (2.1)
uses all three common rows, leaving no three triangle bags to complete a
`K_7` model.

Therefore the useful conclusion is not a rooted `K_4` in the whole
contracted quotient.  It is a rooted `K_4` in the complement of the three
common bags, or an equivalent model whose four branch sets are certified
disjoint from three private common-row extensions.

## 3. Connectivity does not survive deletion of nonsingleton rows

After deleting the three contracted common vertices from (1.4), the
residual quotient is just `C_4`, of connectivity two.  The original graph
is nevertheless seven-connected by (1.5).  There is no contradiction:
deleting a contracted triangle vertex corresponds to deleting a whole
branch bag, not one actual vertex.  Similarly, a separator of a quotient
which contains a contracted bag vertex lifts to an arbitrarily large set,
not to an ambient separator of order at most three.

Thus seven-connectivity permits the familiar rooted-triangle argument
only when the common triangle consists of three actual singleton
vertices.  With nonsingleton rows one instead needs a relative hypothesis,
for example:

* four-connectivity of the actual graph remaining after reserving the
  three common rows; or
* a theorem saying that every quotient separator using a contracted row
  lifts to a full actual adhesion whose proper-minor equality state is
  colour-gluable.

The first is generally false in the transported model; the second is a
new state theorem.

## 4. Rural quotients need port-labelled expansion data

The quotient records only that each common bag meets the four roots.  It
forgets which internal vertices carry those contacts, their cyclic order,
and which internal vertex can serve as a genuine apex.  In the witness,
one common bag `T_1` contains the actual universal apex `p` together with
the entire lower wheel of the icosahedron.  The quotient label `T_1` does
not identify `p`; deleting the quotient vertex deletes seven actual
vertices, while the valid global conclusion deletes only `p` (together
with `q`).

Consequently a cofacial `C_4` quotient lifts only under both of the
following label-faithful conditions.

1. **Rural expansion.**  Every contracted root/common bag has a society
   embedding in the disk with its actual portal occurrences in the cyclic
   order induced by the quotient.  A nonrural society must instead return
   an explicit alternating port cross.
2. **Actual apex selection.**  The rural expansions identify one fixed
   pair of actual vertices, not two or three contracted bags, whose
   deletion makes all pages and annuli planar in compatible rotations.

Even local rurality is insufficient if different quotient frames select
incompatible rotations or different internal apex vertices.  Their
compatibility must be proved by an active-root exchange or by matching
proper-minor equality partitions on the full actual interface.

## 5. Exact safe version of the proposed route

The `C_4`/triangle idea remains useful in the following restricted form.

* Reserve three pairwise disjoint connected common-row extensions.
* Find a rooted `K_4` on `L,R,F,H` disjoint from those extensions.  This
  immediately yields seven literal branch sets.
* If the rooted model fails, retain every contracted bag as a port-labelled
  expansion society.  A small quotient separator is terminal only when
  its full lift is an actual colour-gluable adhesion.  A rural quotient is
  terminal only when all societies expand with one compatible rotation
  and expose one pair of actual apex vertices.

Without these italicized disjointness, adhesion-state, and apex-selection
requirements, the proposed shortcut is exactly falsified by (1.1)--(1.5).
