# Relaxed cyclic frames close four six-edge contact cells

## 1. The artificial-frame web lemma

Let (G) be a graph, let (S=R\mathbin{\dot\cup}Z), and suppose that
(G-S) has exactly two connected components (D_1,D_2) with

\[
N_G(D_1)=N_G(D_2)=S. \tag{1.1}
\]

Give (R=(r_0,\ldots,r_{m-1})), (m\geq4), a cyclic order.  We call this
order a **relaxed cyclic frame** when

\[
 E(G[R])\subseteq
 \{r_ir_{i+1}:i\in\mathbb Z/m\mathbb Z\}. \tag{1.2}
\]

Thus frame edges are allowed to be absent, but actual non-frame chords are
not allowed.

For (j=1,2), form the terminal augmentation (A_j) of (G[D_j]) by
adding independent terminals (t_0,\ldots,t_{m-1}), where

\[
 N_{A_j}(t_i)=N_{D_j}(r_i). \tag{1.3}
\]

### Theorem 1.1 (relaxed-frame web gluing)

If

\[
 \kappa(G)\geq |Z|+4, \tag{1.4}
\]

then either the ordered terminal tuple is crossed in at least one of
(A_1,A_2), or (G-Z) is planar.  Consequently,

\[
 \text{either a shore tuple is crossed, or }
 \chi(G)\leq4+\chi(G[Z]). \tag{1.5}
\]

#### Proof

Suppose both tuples are crossless.  Complete each (A_j), on its fixed
vertex set, to a maximal crossless graph.  The generalized Two Paths
Theorem gives an (m)-web whose planar rib has the terminals on the outer
face in the displayed cyclic order.  As in the exact-cycle proof, no actual
shore vertex can lie in a clique inserted in a facial triangle: such a
clique (X) has

\[
 |N_G(X)|\leq 3+|Z|<\kappa(G),
\]

and this neighbourhood separates (X) from the opposite nonempty shore.
Hence all actual shore vertices lie in the planar rib.

The web completion contains the outer polygon
(t_0t_1\cdots t_{m-1}t_0).  Replace (t_i) by (r_i).  By (1.2), every
actual edge of (G[R]) is one of these polygon edges.  If a polygon edge
is absent in (G[R]), regard it as an artificial edge in both disk
embeddings.  The two disks therefore have the same polygonal boundary and
can be glued on opposite sides.  Delete the artificial polygon edges after
gluing.  This gives a plane embedding of (G-Z).  Four-colour (G-Z) and
colour (G[Z]) from a disjoint palette.  This proves (1.5). \(\square\)

The crossing quotient is unchanged from the exact-cycle version.  If an
alternating crossing joins (r_i) to (r_j) and (r_k) to (r_l), delete
its artificial terminal ends.  Enlarge the two disjoint path interiors
along a shortest connector in the connected shore and split that connector
at an edge.  This yields adjacent connected sets (X,Y), with (X)
touching (r_i,r_j) and (Y) touching (r_k,r_l).  Contract the opposite
full shore to (H).  Thus any clique model in the finite quotient on

\[
 G[S]+H+XY+\{Xr_i,Xr_j,Yr_k,Yr_l\}, \tag{1.6}
\]

where (H) is complete to (S), lifts to (G).

## 2. Four uniform closures at the six-missing-edge layer

Write (F=\overline{G[S]}), with (S=\{0,\ldots,6\}).  In each row below,
(R) is a relaxed cyclic frame, (G[Z]) is bipartite, and every alternating
crossing quotient (1.6) has the displayed (K_7)-model.  Concatenation in a
bag denotes union; (X,Y,H) have the meaning above.

### 2.1 House plus two isolated vertices

Take

\[
 E(F)=\{01,03,04,12,14,23\},\qquad
 R=(0,1,3,4,2),\qquad Z=\{5,6\}. \tag{2.1}
\]

Here (G[R]) is the frame cycle with the edge (01) deleted and (G[Z])
is (K_2).  The five alternating crossings and clique models are

| (X)-ends | (Y)-ends | seven branch sets |
|---|---|---|
| (0,3) | (1,4) | (3;4;5;6;H;1Y;02X) |
| (0,3) | (1,2) | (2;5;6;H;34;0X;1Y) |
| (0,4) | (1,2) | (2;4;5;6;H;0X;13Y) |
| (0,4) | (3,2) | (2;4;5;6;H;0X;3Y) |
| (1,4) | (3,2) | (3;4;5;6;H;1X;2Y) |

### 2.2 A four-cycle with leaves at adjacent vertices, plus an isolate

Take

\[
 E(F)=\{01,03,05,12,14,23\},\qquad
 R=(0,2,5,3),\qquad Z=\{1,4,6\}. \tag{2.2}
\]

The only crossing has (X)-ends (0,5) and (Y)-ends (2,3).  A model is

\[
 2;4;5;6;H;0X;3Y. \tag{2.3}
\]

Moreover (G[Z]) is the path (1-6-4).

### 2.3 The subdivided claw

Take

\[
 E(F)=\{03,06,13,15,23,24\},\qquad
 R=(0,1,3,5),\qquad Z=\{2,4,6\}. \tag{2.4}
\]

The crossing has (X)-ends (0,3) and (Y)-ends (1,5).  A model is

\[
 0;4;5;H;26;3X;1Y. \tag{2.5}
\]

Here (G[Z]) is the path (2-6-4).

### 2.4 A five-cycle with one leaf, plus an isolate

Take

\[
 E(F)=\{03,04,05,12,14,23\},\qquad
 R=(1,2,4,3),\qquad Z=\{0,5,6\}. \tag{2.6}
\]

The crossing has (X)-ends (1,4) and (Y)-ends (2,3).  A model is

\[
 1;3;5;6;H;4X;02Y. \tag{2.7}
\]

Here (G[Z]) is the path (0-6-5).

In every displayed model, a composite bag is connected because it contains
one of its crossing ends (or a present boundary edge), (H) is adjacent to
every boundary-containing bag, and a direct check against the six listed
missing edges verifies all remaining bag adjacencies.  Thus (1.6) lifts
each row to a (K_7)-minor.  If neither shore is crossed, Theorem 1.1 and
(\chi(G[Z])\leq2) give a six-colouring.  Hence all four boundary types are
impossible in a seven-chromatic graph satisfying (1.1) and
(\kappa(G)\ge7), independently of the orders and internal structures of
the two shores.

## 3. Exact residual after the relaxation

The script `contact_order7_sixedge_subcycle_web.py` enumerates every cyclic
order on four and five boundary vertices, checks (1.2), tests bipartiteness
of (G[Z]), and performs an exact connected-branch-set search in every
crossing quotient.  (Six vertices cannot satisfy (1.2) with only six
missing edges, since a chordless six-frame requires nine missing chords.)

Of the six previously residual nonsplit types, the four types in Section 2
close.  Exactly two types remain on this method:

* (F=2K_3+K_1).  Every four-frame leaves one vertex of each triangle and
  the isolated vertex; these three vertices induce (K_3) in (G[Z]), so
  the planar alternative only gives seven colours.  No five-frame exists.
* (F=C_6+K_1).  There are six admissible four-frames with bipartite
  omitted set, but for each frame its unique crossing quotient is
  (K_7)-minor-free.  These are genuine crossing-quotient failures, not a
  failure to find a frame.

Thus the artificial-frame relaxation closes four entire infinite shore
families and isolates the two geometries for which genuinely new portal or
colour-transition information is necessary.
