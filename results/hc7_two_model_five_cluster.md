# A branch-faithful five-cluster between two small `K_5` models

**Status:** proved and independently audited.

This note gives a uniform linkage fact for the support-six programme.  It
uses no separator labels, colouring states, or portal choices.

## Theorem 1 (two-model five-cluster)

Let `G` be a seven-connected graph, and let `M_1,M_2` be vertex-disjoint
`K_5` models, each supported on at most six vertices.  Then `G` contains
five pairwise vertex-disjoint, pairwise adjacent connected subgraphs

\[
                         C_1,\ldots,C_5                 \tag{1.1}
\]

such that every `C_j` meets one branch bag of `M_1` and one branch bag of
`M_2`, and at each model the five subgraphs meet the five branch bags
bijectively.

In particular, the five subgraphs form a literal branch-faithful `K_5`
model linking `M_1` to `M_2`.  The pairing of the branch bags at the two
ends may be an arbitrary permutation.

### Proof

For `i=1,2`, choose one representative from each of the five branch bags
of `M_i`; call the resulting five-set `A_i`.  If `M_i` has a two-vertex
branch bag, let `d_i` be its vertex not chosen as representative.  If all
five bags of `M_i` are singletons, there is no such vertex.  Put

\[
 D=\{d_i:d_i\text{ exists}\}.
\]

Thus `|D|<=2`, and `D,A_1,A_2` are pairwise disjoint.  The graph `G-D` is
at least five-connected.  By the set version of Menger's theorem it has
five pairwise vertex-disjoint `A_1`--`A_2` paths, using all vertices of
`A_1` and all vertices of `A_2`.

Choose the paths so that their total number of edges is minimum.  No path
then has an internal vertex in `A_1 union A_2`: truncate at the last
vertex of `A_1` or the first vertex of `A_2` if necessary.  Denote the
five paths by `P_1,...,P_5`.

For each `d_i` that exists, adjoin `d_i` to the unique path whose end at
`M_i` is the chosen representative of the two-vertex bag.  The added
vertex is adjacent to that representative.  Since the two models are
vertex-disjoint, the two possible added vertices are distinct; since the
paths avoided `D`, all five enlarged subgraphs remain vertex-disjoint and
connected.  Call them `C_1,...,C_5`.

Take two distinct enlarged paths `C_a,C_b`.  At `M_1` they contain two
distinct whole branch bags: a singleton bag is already wholly present,
and the unique nonsingleton bag, when it exists, was completed by adjoining
`d_1`.  Distinct branch bags of a clique model are adjacent.  Hence
`C_a` and `C_b` are adjacent.  The same conclusion also follows at
`M_2`; in particular, the arbitrary Menger pairing between the two
five-element representative sets causes no compatibility issue.  Thus
the five subgraphs are pairwise adjacent.  Their endpoint bags are
bijective at each model by construction.  \(\square\)

## Corollary 2 (the exact connector needed for `K_7`)

Under the hypotheses of Theorem 1, suppose there are two further disjoint
connected subgraphs `R_1,R_2`, disjoint from all five `C_j`, such that

\[
 E(R_1,R_2)\ne\varnothing
 \quad\text{and}\quad
 E(R_h,C_j)\ne\varnothing
 \quad(h=1,2;\ j=1,\ldots,5).                           \tag{2.1}
\]

Then `C_1,...,C_5,R_1,R_2` are the seven branch sets of a `K_7` minor.

This corollary is deliberately stated because it isolates the remaining
two-shore issue exactly.  In the pointwise-full expanded separator from
`hc7_three_split_minimal_bad_contraction.md`, an unoccupied open component
would be such a connector once every `C_j` meets a distinct boundary
atom.  With only two quotient components, however, the five linkage paths
may use both components.  Seven-connectivity and pointwise boundary
fullness do not by themselves say that either component minus those paths
contains a connected subgraph satisfying (2.1).  A proof of that reserved
connector assertion would close the residue; silently replacing a
component by the whole component is invalid because it can intersect the
five linkage bags.

## Theorem 3 (one reserved vertex after contraction)

Let `H` be six-connected, let `L_1,L_2` be disjoint literal `K_5`
cliques, and let `w` lie outside their union.  Then `H-w` contains five
disjoint, pairwise adjacent `L_1`--`L_2` paths, using every vertex of both
cliques.

### Proof

The graph `H-w` is five-connected.  Menger gives five disjoint
`L_1`--`L_2` paths.  Truncate terminal re-entries as in Theorem 1.  Their
ends are the five distinct vertices of each literal clique, so any two
paths are adjacent at either end.  \(\square\)

In the minimal-bad-contraction quotient, Theorem 3 can reserve any one
vertex outside two selected quotient cliques.  In particular, when three
split edges were contracted, it can reserve the third contracted image;
on expansion the resulting five-cluster is disjoint from both ends of the
third split edge.  This is stronger than applying Theorem 1 directly in
the original graph, where completing the first two split bags consumes the
entire two-vertex forbidden-set budget.  It still does not make the two
reserved endpoints complete to the five linkage bags.

## Trust boundary

The theorem proves a `K_5` cluster, not a `K_7` cluster.  It also does not
claim that the linkage avoids a third six-vertex model: avoiding the two
unused vertices of the nonsingleton bags already consumes the complete
two-vertex forbidden-set budget in the five-linkage argument.  These are
the exact reasons that the theorem does not, on its own, close the
three-model two-component residue.
