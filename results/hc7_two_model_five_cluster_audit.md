# Independent audit: two-model five-cluster

**Verdict:** GREEN.

This audits `hc7_two_model_five_cluster.md` independently of its proof
author.  The result is a useful normalized carrier, but it is not a
terminal `K_7` construction.

## 1. Representative and deletion budget

A `K_5` model on at most six vertices has five branch bags and at most one
bag of order two.  Choosing one representative per bag therefore leaves at
most one unused model vertex on each side.  The forbidden set `D` has order
at most two, is disjoint from both representative five-sets, and deleting
it from a seven-connected graph leaves a graph of connectivity at least
five.

The unpaired set form of Menger consequently supplies five disjoint paths
between the two representative five-sets.  Their ends exhaust both sets.
After choosing the paths with the usual terminal truncation, their internal
vertices avoid both representative sets.  Adjoining each unused mate to the
path ending in its chosen partner preserves connectedness and disjointness.

## 2. Clique-model adjacency

At either original model, the five enlarged paths contain its five branch
bags bijectively.  Every two distinct branch bags of a clique model have an
edge between them.  Hence every two enlarged paths are adjacent.  No
alignment of the two endpoint permutations is required.  This verifies
Theorem 1 and its label-faithful conclusion.

Corollary 2 is immediate: its two additional connected sets are disjoint,
adjacent to one another, and adjacent to every one of the five linkage
bags, so the seven displayed sets are literal branch sets of a `K_7`
model.

For Theorem 3, deleting the prescribed vertex from a six-connected graph
leaves a five-connected graph.  Menger gives five disjoint paths between
the two literal five-cliques, and their distinct clique endpoints make the
paths pairwise adjacent.  In the three-contraction quotient this really can
reserve a third contracted image; splitting that image restores two
reserved endpoints.  The theorem correctly does **not** claim that either
endpoint is adjacent to all five paths.

## 3. Trust boundary

The note does not overclaim.  A bare `K_5` prism (two `K_5` cliques joined
by a perfect matching) has no `K_7` minor, so the five-cluster cannot be a
terminal by itself.  In the live two-component residue, the missing datum
is exactly two disjoint adjacent universal carriers outside the five paths,
or a different terminal such as an exact-seven descent or a coherent
two-vertex transversal.
