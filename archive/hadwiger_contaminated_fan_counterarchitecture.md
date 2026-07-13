# A ten-connected contaminated-fan counterarchitecture

## 1. Purpose

The natural local conjecture

\[
 \text{five edge-Kempe detours} +\ \kappa\ge7
 \quad\Longrightarrow\quad
 \text{a bag-aligned detour or a separator of order at most six}
                                                               \tag{1.1}
\]

is false, even for a genuine two-vertex donor bag in a rooted
(K_4)-model and an edge whose deletion lowers the chromatic number.
The example below is uncontracted.  It explains why the remaining
singleton proof must use (K_7)-freeness and the completion-group labels,
not only first/last hits of the five coloured paths.

## 2. Construction

Start with the complete six-partite graph whose parts are

\[
 A_0=\{x,y,k\},\qquad A_i=\{u_i,v_i\}quad(1\le i\le5).       \tag{2.1}
\]

Delete the cross-edge (xu_1), and add the within-part edge (xy).
Call the resulting graph (F).

Use the four rooted branch bags

\[
 D=\{x,y\},\qquad K_0=\{u_1\},\qquad
 L=\{u_2\},\qquad M=\{u_3\}.                                \tag{2.2}
\]

They form a (K_4)-model.  The donor bag (D) is the literal tree
edge (xy); after deleting that edge its two sides are
(X=\{x\}) and (Y=\{y\}).  The donor--(K_0) adjacency is
(yu_1), while the prospective aligned edge (xu_1) is precisely the
deleted cross-edge of the construction.

## 3. Exact properties

### Proposition 3.1

The graph (F) has all of the following properties.

1. (kappa(F)=10).
2. (chi(F)=7), while (F-xy) has the proper six-colouring given by
   the six parts in (2.1).
3. In every six-colouring of (F-xy), the vertices (x,y) have the
   same colour.  In the part colouring, write that colour as
   (alpha) and the colour of (A_i) as (beta_i).  The five
   explicit edge-Kempe detours are

   \[
   x-v_1-k-u_1-y,qquad x-u_i-y\quad(2\le i\le5).              \tag{3.1}
   \]

4. No (x)-(y) path meeting (K_0) has all its vertices other
   than (y) in (X\cup K_0=\{x,u_1\}).  Thus none of the five
   detours is bag-aligned in the sense of Theorem 2.1 of
   `hadwiger_singleton_dark_rung_alignment.md`.
5. No set of at most six vertices separates (X) from (K_0).

#### Proof

The complete graph in (2.1) has connectivity

\[
                    13-\max_i|A_i|=10.                         \tag{3.2}
\]

The same lower bound can be checked directly after the two edge changes.
Delete at most nine vertices.  At least four remain.  All vertices in
different parts are adjacent except the pair (x,u_1), and (xy) is
an additional edge.  A disconnected remainder would have to be contained
in (A_0\cup A_1) and isolate (x) or (u_1); every such isolation
leaves at most three vertices and therefore requires deleting at least
ten.  Hence the remainder is connected.  On the other hand, deleting
the ten neighbours of (x) leaves (x) separated from the edge
(ku_1).  This proves (1).

The seven vertices

\[
                         x,y,v_1,u_2,u_3,u_4,u_5               \tag{3.3}
\]

form a (K_7), while seven colours plainly suffice.  Deleting (xy)
restores the part colouring, proving (2).  If a six-colouring of
(F-xy) gave (x,y) different colours, restoring (xy) would
six-colour (F), impossible.  The usual edge-critical Kempe switch then
puts (x,y) in one (alpha/\beta_i)-component for every (i), and
(3.1) gives the paths explicitly.

The only possible path whose internal vertices lie in the singleton
(K_0) would be (x-u_1-y), but (xu_1\notin E(F)).  This proves
(4).  Finally (5) follows immediately from (kappa(F)=10).
\(\square\)

## 4. Consequence for the singleton programme

The example deliberately contains a (K_7), as (3.3) exhibits; it is
not a counterexample to Hadwiger and is not claimed to be globally
minor-critical.  It is, however, edge-critical at the named donor rung,
ten-connected, uncontracted, and carries the required rooted
(K_4)-interface.

Therefore no proof may derive a six-cut or a bag-aligned detour solely
from

* seven-connectivity;
* a genuine donor bridge;
* the five edge-Kempe paths; and
* the existence of the adjacent rooted bags.

The missing hypothesis must be used constructively.  In the real
singleton cell it is the absence of a (K_7), together with the
specific (A\mid C) boundary completion and potential-maximality.  The
counterarchitecture shows exactly what those hypotheses must rule out:
a large complete-multipartite contaminating reservoir can carry all five
colours while maintaining arbitrarily high local connectivity.

`contaminated_fan_counterarchitecture_verify.py` independently constructs
the thirteen-vertex graph, exhausts all vertex cuts to certify
(\kappa=10), and checks the displayed (K_7), six-colouring, and five
two-colour detours.
