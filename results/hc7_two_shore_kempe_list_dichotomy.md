# Boundary Kempe distance gives two obstruction paths or two list-critical subgraphs

**Status:** written proof; separate internal audit GREEN in
[`hc7_two_shore_kempe_list_dichotomy_audit.md`](hc7_two_shore_kempe_list_dichotomy_audit.md).

This note turns incompatible colouring-extension sets across a separation
into one of two simultaneous host-level structures.  If the two sets are
one Kempe move apart, that same move is obstructed by a two-colour path in
each open shore.  If their distance is greater, one intermediate boundary
colouring is rejected by both shores and therefore defines an induced
list-critical subgraph in each.  This is an unbounded reduction; it neither
constructs a clique minor nor identifies colours with minor-model labels.

## 1. Extension sets on a labelled boundary

Let `q>=2`, and let

\[
                     V(G)=A\mathbin{\dot\cup}X
                              \mathbin{\dot\cup}D,       \tag{1.1}
\]

where `A,D` are nonempty and anticomplete.  Suppose `G` is not
`q`-colourable, while both closed sides `G[A union X]` and
`G[D union X]` are `q`-colourable.

Let `Gamma_q(X)` be the graph whose vertices are the labelled proper
`q`-colourings of `G[X]`.  Two vertices are adjacent when one is obtained
from the other by interchanging two colours on one connected component of
the corresponding two-colour subgraph of `G[X]`.  Assume `Gamma_q(X)` is
connected.

Write `E_A` and `E_D` for the boundary colourings which extend through the
two closed sides.  These sets are nonempty.  They are disjoint, since a
common labelled boundary colouring would glue to a `q`-colouring of `G`.

## 2. The distance dichotomy

### Theorem 2.1

Choose a shortest path

\[
                         c_0,c_1,\ldots,c_k             \tag{2.1}
\]

in `Gamma_q(X)` with `c_0 in E_A` and `c_k in E_D`.  Then `k>=1`, and
exactly one of the following holds.

1. `k=1`.  The boundary interchange from `c_0` to `c_1` is obstructed by
   a two-colour path with nonempty interior in `A` and by another such path
   with nonempty interior in `D`.  Both paths begin in the operated
   boundary component and end in another boundary component for the same
   colour pair.  Their interiors are disjoint, although their other
   boundary components need not agree.
2. `k>=2`.  Every internal colouring `c_i`, `1<=i<=k-1`, extends through
   neither closed side.  For any such `c_i`, each open shore contains a
   connected induced vertex-minimal list-uncolourable subgraph, for the
   lists obtained by deleting the colours on its literal boundary
   neighbours.

If `K_A subseteq G[A]` is the subgraph in outcome 2 and

\[
 L_A(u)=[q]-c_i(N_G(u)\cap X),                           \tag{2.2}
\]

then every vertex satisfies

\[
                 d_{K_A}(u)\ge |L_A(u)|
                    =q-|c_i(N_G(u)\cap X)|.             \tag{2.3}
\]

The analogous assertion holds for the disjoint subgraph `K_D subseteq D`.

#### Proof

Minimality of (2.1) gives

\[
 c_i\notin E_A\quad(i>0),\qquad
 c_i\notin E_D\quad(i<k).                               \tag{2.4}
\]

Suppose first that `k=1`, and let the sole move interchange colours
`alpha,beta` on a boundary two-colour component `W`.  Extend `c_0` through
`A`.  If the full `alpha`--`beta` component containing `W` met no other
boundary component, switching that full component would extend `c_1`
through `A`, contrary to (2.4).  It therefore meets another boundary
component.  A shortest path from `W` to the first such component has all
internal vertices in `A` and has nonempty interior.  Applying the reverse
move to an extension of `c_1` through `D` gives the second path.  Their
interiors are disjoint because the shores are disjoint.  This is outcome 1.

Now let `k>=2`.  Equation (2.4) says that every internal `c_i` is outside
`E_A union E_D`.  Fix one.  The colouring `c_i` extends through `A`
exactly when `G[A]` is colourable from the lists (2.2).  Since it does not,
choose an induced non-list-colourable subgraph with a minimum vertex set.
It is connected, since otherwise one component would be a smaller
obstruction.  Colouring the subgraph after deleting a vertex `u` shows
that `d(u)>=|L_A(u)|`; otherwise one available colour is absent from its
coloured neighbours and completes the colouring.  The same construction
inside `D` gives a disjoint second kernel and proves outcome 2. \(\square\)

## 3. The `HC_7` boundary range

### Corollary 3.1

Let `q=6`, suppose `G` is `K_7`-minor-free, and let `|X|<=8`.  Under the
hypotheses of Section 1, Theorem 2.1 applies without any additional Kempe-
connectivity assumption.

#### Proof

The boundary graph `G[X]` is `K_7`-minor-free and has order at most eight.
The audited small-boundary Kempe-connectivity lemma says that all its
labelled proper six-colourings belong to one Kempe class. \(\square\)

In a hypothetical minor-minimal counterexample, nonemptiness of the two
extension sets is automatic whenever both open shores are nonempty:
deleting either shore gives a proper minor and hence a six-colouring of the
opposite closed side.

## 4. Exact scope

The distance-one outcome synchronizes the colour pair and operated
boundary component, but not the other two boundary components reached by
the paths.  The list-critical subgraphs in the longer-distance outcome
need not be boundary-full, need not be components of `G-X`, and need not
have neighbourhood of order seven or eight.

The theorem therefore supplies a uniform dynamic normal form, not a
`K_7`-minor model or a colour-gluing theorem.  Its list-critical outcome can
be combined with the separate boundary list-critical transfer theorem,
which records strict complementary-component transfer and the
shore-filling endpoint under the asymmetric order-eight hypotheses.

## 5. Dependencies

- [single boundary Kempe transition between opposite-shore responses](hc7_opposite_shore_single_kempe_transition.md)
- [fresh-colour linkages, Lemma 4.1](hc7_exact7_fresh_colour_linkage.md),
  for six-colour Kempe connectivity on `K_7`-minor-free graphs of order at
  most eight.
- [boundary list-criticality and complementary transfer](hc7_boundary_list_critical_transfer.md),
  used only for the continuation described in Section 4.
