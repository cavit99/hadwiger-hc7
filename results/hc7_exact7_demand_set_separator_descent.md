# Demand-set reflection and full-neighbourhood descent at an exact seven-boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_exact7_demand_set_separator_descent_audit.md`](hc7_exact7_demand_set_separator_descent_audit.md).
This theorem is
an unbounded follow-on to the forced bichromatic paths in
[`hc7_exact7_critical_triangle_full_subgraph_demand.md`](../results/hc7_exact7_critical_triangle_full_subgraph_demand.md).
It closes every path component which supplies one of three exact boundary
demands and turns every non-direct path end into a strictly smaller connected
side of a full-neighbourhood separation.  It does not close the case in which
both ends of the path enter the two selected boundary-full subgraphs directly,
and it does not preserve the old boundary labels through a nested separation.

## 1. Setup and terminology

Let `G` be a graph such that

\[
 \chi(G)=7,\qquad \kappa(G)\ge 7,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}. \tag{1.1}
\]

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,                                      \tag{1.2}
\]

where `L` and `R` are nonempty and there is no edge between `L` and `R`.
Suppose the closed side `G[S union R]` has a proper six-colouring whose exact
equality partition on the literal boundary is

\[
 \Pi=M\mid\{x\}\mid\{y\}\mid\{k\}\ (k\in K),       \tag{1.3}
\]

where

\[
 S=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,
 \qquad (|M|,|K|)\in\{(2,3),(3,2)\},                 \tag{1.4}
\]

`M` is independent, `K` is a clique, and `xy` is not an edge.  Thus `Pi`
has at most six blocks.  These are exactly the two boundary-partition forms
which arise in Theorem 2.1(6) of the cited critical-triangle result after
the maximum clique of remaining singleton blocks has been fixed.

A connected subgraph of `G[R]` is **boundary-full** if it has a neighbour at
every literal vertex of `S`.  Fix two vertex-disjoint boundary-full connected
subgraphs

\[
                         P_1,P_2\subseteq G[R].          \tag{1.5}
\]

For a block `B` in `\{M,\{x\},\{y\}\}`, define its **demand set relative to
`K`** by

\[
 D_K(B)=B\cup\{k\in K:E_G(k,B)=\varnothing\}.          \tag{1.6}
\]

The vertices added to `B` in (1.6) are precisely the clique singletons whose
adjacency to the representative of `B` cannot be supplied by a boundary edge.

## 2. Exact reflection from one additional connected subgraph

### Theorem 2.1 (demand-set reflection)

Under (1.1)--(1.6), there is no connected subgraph

\[
                 Z\subseteq G[R-(V(P_1)\cup V(P_2))]   \tag{2.1}
\]

which has a neighbour at every literal vertex of `D_K(B)` for some
`B in \{M,{x},{y}\}`.

More generally, before assuming that `G` is not six-colourable, the existence
of `Z` produces a proper colouring of `G[L union S]` whose exact equality
partition on `S` is `Pi`.  It therefore glues to the given colouring of
`G[S union R]`.

#### Proof

Fix `B` and `Z`, and call the other two members of
`\{M,{x},{y}\}` by `B_1,B_2`.  Each of the following three vertex sets is
connected, and the three are pairwise disjoint:

\[
       Z\cup B,\qquad V(P_1)\cup B_1,\qquad V(P_2)\cup B_2. \tag{2.2}
\]

For the first set this follows from `B subseteq D_K(B)` and the hypothesis on
`Z`; for the other two it follows from boundary-fullness.  Contract a spanning
tree in each set in (2.2), and delete unused vertices of `R` if necessary.
This is a proper minor of `G`.

The three contraction representatives together with the literal singleton
vertices of `K` form a clique.  Indeed, each representative using `P_1` or
`P_2` is adjacent to every other block representative and every member of
`K`, by boundary-fullness.  The representative of `Z union B` is adjacent to
the other two for the same reason, using the contacts of `P_1,P_2` with `B`.
For `k in K`, it is adjacent to `k` either through an edge from `k` to `B`, or,
when no such edge exists, through the required contact of `Z` with
`k in D_K(B)`.  Finally, `K` itself is a clique.

The clique just constructed has one representative for every block of `Pi`.
A six-colouring of the proper minor therefore gives these representatives
pairwise different colours.  Restrict it to the unchanged vertices of
`L union S`, and expand each of `B,B_1,B_2` with the colour of its contraction
representative.  This is proper because the three blocks are independent and
every original edge incident with a contracted boundary vertex was represented
in the minor.  Its exact equality partition on the literal boundary is `Pi`.

After a permutation of colour names, this colouring agrees on every boundary
vertex with the given colouring of `G[S union R]`.  The two colourings glue
because there is no edge between `L` and `R`.  This six-colours `G`, contrary
to (1.1).  \(\square\)

## 3. Forced paths and smaller full-neighbourhood sides

Assume in addition that `G[S union R]` contains an `x`--`y` path `P` whose
internal vertices lie in `R`.  In the applications, `P` is the forced
bichromatic path from Theorem 2.1(6) of the critical-triangle result.

For a connected set `X subseteq R-(V(P_1) union V(P_2))`, write

\[
 T_X=N_G(X)\cap S,
 \qquad
 A_X=N_G(X)\cap(V(P_1)\cup V(P_2)).                    \tag{3.1}
\]

### Theorem 3.1 (missing corners and full-neighbourhood descent)

The following statements hold.

1. Suppose the internal vertices of `P` avoid `P_1 union P_2`, and let `X`
   be the component of `R-(V(P_1) union V(P_2))` containing them.  Then there
   exist vertices `k_x,k_y in K-T_X`, not necessarily distinct, such that

   \[
                         xk_x,yk_y\notin E(G).           \tag{3.2}
   \]

2. Orient `P` from `x`.  Suppose it meets `P_1 union P_2`, but its first
   internal vertex in that union is not the first vertex after `x`.  Let `X`
   be the component of `R-(V(P_1) union V(P_2))` containing the nonempty
   internal part of the initial subpath before that first meeting.  Then there
   is a vertex

   \[
                        k_x\in K-T_X,qquad xk_x\notin E(G). \tag{3.3}
   \]

   The symmetric conclusion holds at the `y` end of `P`.
3. For every component `X` obtained in item 1 or 2,

   \[
                N_G(X)=T_X\mathbin{\dot\cup}A_X,        \tag{3.4}
   \]

   and this is the boundary of an actual separation.  In particular,

   \[
        |T_X|+|A_X|\ge7,
        \qquad |X|<|R|.                                 \tag{3.5}
   \]

   Thus `|X|` is a strict host-level connected-side parameter, independent of
   any quotient graph or auxiliary completion.  In item 1, if `k_x` and
   `k_y` are distinct then `|T_X|<=5` and `|A_X|>=2`; if they coincide then
   `|T_X|<=6` and `|A_X|>=1`.

#### Proof

In item 1, the internal vertices of `P` are nonempty because `xy` is not an
edge.  The component `X` has a neighbour at both `x` and `y`, so
`x,y in T_X`.  If every `k in K` nonadjacent to `x` also belonged to `T_X`,
then `X` would have a neighbour at every vertex of

\[
                    D_K(\{x\})=\{x\}\cup
                    \{k\in K:xk\notin E(G)\}.
\]

This contradicts Theorem 2.1.  Hence a vertex `k_x` as in (3.2) exists.
The argument for `k_y` is identical.

For item 2, the initial subpath before its first meeting with
`P_1 union P_2` is nonempty and lies in one component `X` of the displayed
vertex deletion.  This component has a neighbour at `x`, so `x in T_X`.
The same demand-set argument gives (3.3).  Reversing the path proves the
statement at `y`.

It remains to prove item 3.  Since `X` is a component after deleting
`V(P_1) union V(P_2)` from `R`, every neighbour of `X` in `R-X` belongs to
one of those two connected subgraphs.  There is no edge from `R` to `L`.
Its remaining neighbours are precisely the vertices of `T_X subseteq S`.
This proves (3.4).

The nonempty set `L` lies outside `X union N_G(X)`, so (3.4) is the boundary
of an actual separation.  Seven-connectivity gives the first inequality in
(3.5).  Both `P_1` and `P_2` are nonempty and disjoint from `X`, whence
`X` is a proper subset of `R` and the second inequality follows.  Finally,
(3.2) excludes one or two literal members of `K` from `T_X`; substituting
the resulting upper bound for `|T_X|` into (3.5) gives the last assertions.
\(\square\)

### Corollary 3.2 (the only path-end geometry not reduced)

For every forced path `P`, one of the following holds.

1. Its interior avoids `P_1 union P_2`, and Theorem 3.1(1) returns a smaller
   connected side with two endpoint-indexed missing corners.
2. At least one end has a non-direct first meeting with `P_1 union P_2`, and
   Theorem 3.1(2) returns a smaller connected side with one endpoint-indexed
   missing corner.
3. The first internal vertex after `x` and the first internal vertex before
   `y` both lie in `P_1 union P_2`.

Thus only the two-ended direct-intersection geometry in item 3 escapes this
full-neighbourhood construction.

## 4. Exact trust boundary

Theorem 3.1 gives a strict decrease from `|R|` to `|X|` in the literal host
graph, but it is not yet a recursive exact-seven induction:

1. `N_G(X)` can have order greater than seven and can contain vertices of
   `P_1` or `P_2`; the two named boundary-full connected subgraphs therefore
   need not survive as labelled objects on the new sides.
2. The old equality partition `Pi` need not induce a legal equality partition
   on `N_G(X)`.  An order-seven full-neighbourhood separation alone does not
   synchronize its two closed-side colourings.
3. Applying the audited
   [nested full-neighbourhood descent](../results/hc7_nested_full_neighbourhood_descent.md)
   can strictly reduce separator excess, but at excess one it can return an
   order-eight boundary to which every complementary component is adjacent.
   The audited
   [excess-one refinement](../results/hc7_epsilon_one_labelled_descent.md)
   closes split descended seven-boundaries and identifies the unique
   five-chromatic boundary, but leaves nonsplit four-colourable boundaries and
   the boundary-full order-eight obstruction.
4. Corollary 3.2 does not treat the two-ended direct-intersection geometry.

Consequently, the next theorem must use the contraction-critical colouring
response either to preserve an attained boundary partition through (3.4), or
to turn the two-ended direct intersection into an explicit `K_7`-minor model.
The strict inequality `|X|<|R|` alone is not claimed to provide that missing
state preservation.
