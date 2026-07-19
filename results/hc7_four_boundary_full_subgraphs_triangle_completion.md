# Four boundary-full connected subgraphs and a boundary triangle give a `K_7` minor

**Status:** written proof; separate internal audit GREEN in
[`hc7_four_boundary_full_subgraphs_triangle_completion_audit.md`](hc7_four_boundary_full_subgraphs_triangle_completion_audit.md).

This note records a literal branch-set construction at an eight-vertex
boundary.  Its immediate consequence is that none of the three
boundary-full components in the audited 82-type order-eight case can be
split into two disjoint boundary-full connected subgraphs.  Thus the
defect-two reflection theorem cannot be entered at the raw order-eight
boundary by splitting one component into two full connected subgraphs; its
seven-vertex boundary must first be produced by a genuine host separation.

## 1. Four full connected subgraphs

### Theorem 1.1

Let `G` be a graph, let `X subseteq V(G)`, and suppose that `G[X]`
contains a triangle

\[
                         \Delta=\{q_1,q_2,q_3\}.
\tag{1.1}
\]

Assume that `X-Delta` contains three distinct vertices `x_1,x_2,x_3`.
Let

\[
                         P_0,P_1,P_2,P_3
\tag{1.2}
\]

be pairwise vertex-disjoint connected subgraphs of `G-X`.  If every
`P_i` is adjacent to every literal vertex of `X`, then `G` contains a
`K_7` minor.

#### Proof

Consider the seven sets

\[
 P_0,\qquad
 P_1\cup\{x_1\},\qquad
 P_2\cup\{x_2\},\qquad
 P_3\cup\{x_3\},\qquad
 \{q_1\},\ \{q_2\},\ \{q_3\}.
\tag{1.3}
\]

They are pairwise disjoint.  Each is connected: the four `P_i` are
connected, and for `i=1,2,3` the full adjacency of `P_i` to `X`
supplies an edge from `P_i` to `x_i`.

The first four sets are pairwise adjacent.  The unanchored set `P_0` is
adjacent to `P_i union {x_i}` through an edge from `P_0` to `x_i`.
For distinct `i,j in {1,2,3}`, the full adjacency of `P_i` supplies an
edge from `P_i` to `x_j`, which lies in the branch set
`P_j union {x_j}`.

Every one of the first four sets is adjacent to each singleton
`{q_j}`, again by full adjacency to `X`.  Finally, the three singleton
sets are pairwise adjacent because `Delta` is a triangle.  Hence the
seven sets in (1.3) are the branch sets of an explicit `K_7`-minor model.
\(\square\)

## 2. Consequence for the 82 order-eight boundary types

### Corollary 2.1

Let `G` be `K_7`-minor-free, let `X` have order eight, and suppose
`G-X` has three components `C_0,C_1,C_2`, each adjacent to every literal
vertex of `X`.  If `G[X]` is one of the 82 boundary graphs in the audited
three-component order-eight classification, then no `C_i` contains two
vertex-disjoint connected subgraphs which are both adjacent to every
vertex of `X`.

Equivalently, the maximum number of pairwise vertex-disjoint
`X`-full connected subgraphs contained in each `C_i` is exactly one.

#### Proof

The audited 82-type classification proves that every surviving boundary
contains a triangle: 80 types contain two disjoint triangles, and the
other two contain a vertex-disjoint triangle and a five-cycle.  Fix such a
triangle `Delta`.  Since `|X|=8`, there are five vertices outside `Delta`,
so the three anchors required in Theorem 1.1 can be chosen.

Suppose, by symmetry, that `C_0` contains two disjoint `X`-full connected
subgraphs `P_0,P_1`.  Take `P_2=C_1` and `P_3=C_2`.  These four connected
subgraphs are pairwise disjoint, lie outside `X`, and are adjacent to every
vertex of `X`.  Theorem 1.1 gives a `K_7` minor, a contradiction.

Each `C_i` itself is connected and `X`-full, so its packing maximum is at
least one.  The preceding paragraph makes it at most one.  \(\square\)

## 3. Consequence for the current proof route

At the raw three-component order-eight interface, splitting one component
into two disjoint `X`-full connected subgraphs is already terminal by
Corollary 2.1.  In the two-component asymmetric order-eight setting, the
same packing-one conclusion is the separately audited asymmetric-shore
split theorem.

The uniform defect-two reflection theorem instead concerns an **actual
seven-vertex boundary**.  On the rich side of such a returned separation
it asks for two boundary-full connected subgraphs and a third connected
subgraph missing at most two boundary vertices, while the opposite side
contains another boundary-full connected subgraph.  Corollary 2.1 neither
constructs nor rules out that seven-boundary configuration.  It shows only
that one must first obtain the literal seven-vertex separation; treating
the raw eight-vertex boundary as though it were the input to defect-two
reflection is invalid.

## 4. Dependencies and trust boundary

- the [three-component order-eight boundary classification](../results/hc7_order8_three_component_boundary_classification.md), solely for the fact that every one of the 82 boundary types contains a triangle;
- the [asymmetric two-component shore split](../results/hc7_star_order_eight_asymmetric_shore_split.md), for the separate two-component comparison in Section 3.

Theorem 1.1 is an elementary unbounded host-graph result.  It assumes no
colouring and no inherited branch-set labels.  Corollary 2.1 does not
produce a compatible seven-boundary partition, split a component into a
defect-two connected subgraph, preserve a proper-minor response, or prove
`HC_7`.
