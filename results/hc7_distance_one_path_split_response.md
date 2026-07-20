# Splitting a distance-one obstruction path

**Status:** written proof; separate internal audit GREEN in
[`hc7_distance_one_path_split_response_audit.md`](hc7_distance_one_path_split_response_audit.md).

This note treats one concrete part of the distance-one outcome in the
normalized nine-vertex boundary.  It gives an explicit `K_7`-minor model
when the obstruction path can be separated from one boundary-full residual
component.  Failure has an exact component-attachment inequality, rather
than an unspecified path collision.

## 1. Full-neighbourhood response after deleting a path interior

### Lemma 1.1

Let

\[
 V(G)=E\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
 \qquad E_G(E,C)=\varnothing,
 \qquad |B|=9,
\]

where `E,C` are nonempty and `G` is seven-connected, is not
six-colourable, and every proper minor of `G` is six-colourable.  Let `P`
be a path whose two ends lie in `B`, whose nonempty interior `P^circ` lies
in `E`, and which has no other boundary vertex.

For a component `H` of `G[E-V(P^circ)]`, put

\[
 m(H)=|B-N_G(H)|,
 \qquad
 h(H)=|N_G(H)\cap V(P^\circ)|.
\]

Then

\[
                         |N_G(H)|=9-m(H)+h(H).          \tag{1.1}
\]

The set `N_G(H)` is the boundary of an actual separation and has order at
least seven.  If `h(H)<m(H)`, it has order seven or eight and carries the
usual operation-specific response: for every crossing edge `xy` with
`x in H`, every six-colouring of `G-xy` restricts to colourings of
`G-H` and `G[H union N_G(H)]-xy`, while its boundary partition is rejected
by the intact graph `G[H union N_G(H)]`.

#### Proof

Different components of `G[E-V(P^circ)]` are anticomplete.  There are no
`E`--`C` edges.  Therefore every neighbour of `H` outside `H` lies either
in `B` or in `P^circ`, and both kinds of neighbour are included in its full
neighbourhood.  The two sets are disjoint, proving (1.1).

The nonempty set `C` lies beyond this full neighbourhood, so it is the
boundary of a nontrivial separation.  Seven-connectivity gives order at
least seven.  If `h(H)<m(H)`, equation (1.1) gives order at most eight.

For a crossing edge `xy`, `G-xy` is a proper minor and has a
six-colouring.  Its ends receive one colour, or the edge could be restored.
The restrictions give the two displayed edge-deleted colourings.  If the
same equality partition extended through the intact `H`-side, a permutation
of colour names would align it with the outside colouring and six-colour
`G`.  Hence the intact side rejects it. \(\square\)

Thus, in the absence of an order-seven or order-eight response, every
residual component obeys the sharp collision inequality

\[
                              h(H)\ge m(H).             \tag{1.2}
\]

## 2. A `K_7` decoder in the live nine-boundary

Retain the normalized setting of the rooted-partition contact-concentration
theorem after the large-boundary reduction.  Thus

\[
 |B|=9,\qquad |W|=2,
\]

and put

\[
                         F=S-\{d,e\}.
\]

The graph `G[F]` is a forest.  There are four pairwise disjoint connected
subgraphs

\[
 R_0,\qquad R_1,\qquad E\cup\{d\},\qquad D\cup\{e\}, \tag{2.1}
\]

which are pairwise adjacent and each adjacent to every vertex of `F`.
Here `R=R_0 dotcup R_1`, the two parts are connected and adjacent, and each
contains its prescribed boundary-full rooted subgraph.

### Theorem 2.1

Let `P` be the obstruction path in the `E`-shore supplied by a distance-one
exact-`{d}` Kempe transition.  Let its ends be `u,v`.  Suppose:

1. `u,v in F` lie in the same component of the forest `G[F]`; and
2. `G[E-V(P^circ)]` has a component `H` which is full to `B`.

Then `G` contains a `K_7` minor.

#### Proof

The two ends lie in different boundary components of the operated
two-colour subgraph.  Hence `uv` is not a boundary edge.  Let

\[
                  u=t_0,t_1,\ldots,t_k=v
\]

be the unique `u`--`v` path in `G[F]`.  Then `k>=2`.  Its union with `P`
is a cycle.

Split this cycle into the following three connected branch sets:

\[
 \{u\},\qquad
 \{t_1,\ldots,t_{k-1}\},\qquad
 \{v\}\cup V(P^\circ).                              \tag{2.2}
\]

They are nonempty, pairwise disjoint and pairwise adjacent.  Each contains
a vertex of `F`.

Replace the third subgraph in (2.1) by

\[
                              H\cup\{d\}.              \tag{2.3}
\]

It is connected because `H` is full to `B`.  It is adjacent to `R_0,R_1`
through the vertex `d`.  It is adjacent to `D union {e}` through either
member of `W`: that vertex belongs to `D`, and boundary-fullness of `H`
supplies an incident edge.  The four subgraphs

\[
 R_0,\quad R_1,\quad H\cup\{d\},\quad D\cup\{e\}     \tag{2.4}
\]

are therefore connected, pairwise disjoint and pairwise adjacent.  Each is
adjacent to every vertex of `F`.

The four sets in (2.4) are disjoint from the three cycle branch sets in
(2.2).  Since every set in (2.2) contains a vertex of `F`, each of the four
sets is adjacent to each of the three.  Together they are seven pairwise
adjacent connected branch sets, and hence a `K_7`-minor model. \(\square\)

## 3. Exact surviving collision

Apply Lemma 1.1 to the `E`-shore obstruction path in the distance-one
outcome.  Outside an explicit `K_7` minor and an order-seven or order-eight
full-neighbourhood response, at least one of the following remains.

1. The two selected boundary ends do not lie in one component of `G[F]`.
   In particular, one may lie in `W` or the ends may lie in different tree
   components of `F`.
2. The path interior spans all of `E`.
3. Every component `H` of `G[E-V(P^circ)]` misses at least one boundary
   vertex and satisfies

   \[
                    |N_G(H)\cap V(P^\circ)|
                       \ge |B-N_G(H)|.                 \tag{3.1}
   \]

The second obstruction path, through `C`, is disjoint from `P^circ`, but
its interior lies inside the three other subgraphs in (2.1):
`R_0 union R_1 union D union {e}` covers `C`.  Thus it cannot simply be
used as a new cycle edge while retaining all four old external branch sets.
The remaining problem is precisely a simultaneous split: use that second
path to replace whichever of those three branch sets it meets while the
inequality (3.1) controls the split of `E`.  The distance-one theorem alone
does not provide this label-preserving allocation.
