# Split-edge completion at the exact order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_star_order_eight_split_edge_completion_audit.md`](hc7_star_order_eight_split_edge_completion_audit.md).
This is an explicit branch-set lemma for the exact order-eight outcome of
the five-support star reduction.  It does not produce the two required
paths and does not prove `HC_7`.

## Theorem 1 (split-edge completion)

Let `G` contain pairwise disjoint vertex sets `A,S,B`, where

\[
                 S=R\mathbin{\dot\cup}V(e)
                    \mathbin{\dot\cup}V(f)\mathbin{\dot\cup}\{x\}.
\]

Assume the following.

1. `R` is a three-vertex clique, and `e,f` are edges disjoint from `R`
   and from one another.
2. The edge `e` is collectively adjacent to every vertex of `R`.
3. `G[B]` is connected and every vertex of `S` has a neighbour in `B`.
4. There are adjacent vertices `ell_e,ell_f in A`, each adjacent to every
   vertex of `R`, such that `ell_f` has a neighbour in `V(e)` and `ell_e`
   is adjacent to one endpoint `f_2` of `f`.
5. The graph `G[A]` contains vertex-disjoint connected subgraphs `P,Q`
   such that

   \[
        \ell_f\in V(P),\qquad \ell_e\in V(Q),
   \]

   `P` has a neighbour at `x`, and `Q` has a neighbour in `V(e)`.

Then `G` contains a `K_7` minor.

### Proof

Let `f_1` be the endpoint of `f` different from `f_2`.  Consider the
following seven vertex sets:

\[
 \{r\}\ (r\in R),\qquad
 V(e),\qquad
 V(P)\cup\{x\},\qquad
 V(Q)\cup\{f_2\},\qquad
 V(B)\cup\{f_1\}.                                    \tag{1.1}
\]

They are pairwise disjoint.  The set `V(e)` is connected because `e` is
an edge.  The `P`-set is connected by the assumed `P`--`x` edge.  The
`Q`-set is connected by the edge `ell_e f_2`, and the `B`-set is connected
because `G[B]` is connected and `f_1` has a neighbour in `B`.  The three
remaining sets are singletons.

It remains to verify the pairwise adjacencies.  The singleton sets from
`R` are pairwise adjacent.  Each of the other four sets is adjacent to
every singleton from `R`: this follows respectively from the collective
`e`--`R` adjacency, the presence of `ell_f` in `P`, the presence of
`ell_e` in `Q`, and the boundary-fullness of `B`.

Among the four nonsingleton sets, the six adjacencies have the following
witnesses:

- `V(e)` is adjacent to `P union {x}` through an edge from `ell_f` to
  `V(e)`;
- `V(e)` is adjacent to `Q union {f_2}` by the assumed `Q`--`V(e)` edge;
- `V(e)` is adjacent to `B union {f_1}` because `B` has a neighbour at
  each boundary vertex, in particular at an endpoint of `e`;
- `P union {x}` is adjacent to `Q union {f_2}` through the edge
  `ell_e ell_f`;
- `P union {x}` is adjacent to `B union {f_1}` through an `x`--`B` edge;
  and
- `Q union {f_2}` is adjacent to `B union {f_1}` through the edge
  `f_1f_2`.

Thus the seven sets in (1.1) are pairwise adjacent connected branch sets,
and they form a `K_7`-minor model in `G`.  \(\square\)

## Corollary 2 (the corresponding two-path linkage is forbidden)

In the `K_7`-minor-free exact order-eight configuration, let `A` be the
open component containing the two omitted vertices `ell_e,ell_f` of the
original five-clique, and let `B` be the other boundary-full component.
Then `A` does not contain vertex-disjoint connected subgraphs `P,Q`
satisfying item 5 of Theorem 1.  The same conclusion holds after
interchanging the labels `e,f`.

### Proof

All other hypotheses of Theorem 1 are supplied by the labelled defect
edges, the original five-clique, and the boundary-fullness of `B`.
Theorem 1 would otherwise give a `K_7` minor.  The relabelled statement is
symmetric.  \(\square\)

## Exact contribution and limitation

Theorem 1 is distinct from the earlier
[asymmetric shore split](hc7_star_order_eight_asymmetric_shore_split.md).
That result requires both connected subgraphs in one shore to contact the
boundary vertex `x`.  The present theorem requires only `P` to contact
`x`; it instead splits the endpoints of `f` between two branch sets and
uses the edge `ell_e ell_f` to join the two shore-derived branch sets.

Equivalently, after adjoining terminal vertices for the boundary contact
sets, the new hypothesis is a prescribed two-path linkage inside `A`:
one path joins `ell_f` to a neighbour of `x`, and the other joins `ell_e`
to a neighbour of `V(e)`.  In the canonical rooted web this is a crossing
linkage.  The theorem therefore identifies the exact structural
alternative which must be combined with seven-connectivity and
proper-minor colourings; it does not assert that the linkage exists.
