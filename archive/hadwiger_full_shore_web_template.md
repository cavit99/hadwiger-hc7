# A reusable web-closure theorem for order-seven full-shore adhesions

## Theorem

Let `G` be seven-connected, let `S` be a seven-vertex separator, and
suppose `G-S` has exactly two components `D_1,D_2`, each with neighbourhood
`S`.  Choose a subset `R subseteq S`, of order `k in {4,5}`, together with
a cyclic ordering

\[
 R=(x_0,x_1,\ldots,x_{k-1})                         \tag{1}
\]

such that every edge of `G[R]` is an edge of the cycle in (1); frame edges
may be absent.  Put `Z=S-R`, and assume

\[
 \chi(G[Z])\le2.                                    \tag{2}
\]

For a shore `D_j`, write `P_i^j=N_{D_j}(x_i)`.  Say that the ordered
boundary `(R,Z)` has the **crossing-completion property** if the following
holds for every crossing pair

\[
 i<r<j<s
\]

in the cyclic order: whenever one shore contains vertex-disjoint paths
joining `P_i` to `P_j` and `P_r` to `P_s`, the original graph contains a
`K_7` minor.

### Web-closure theorem

Under these hypotheses, if `(R,Z)` has the crossing-completion property,
then

\[
 G\text{ contains }K_7\text{ as a minor}
 \quad\hbox{or}\quad
 \chi(G)\le6.                                       \tag{3}
\]

### Proof

For each shore `D_j`, form an auxiliary graph `A_j` by adding independent
terminals `t_0,...,t_{k-1}`, where `t_i` is adjacent precisely to `P_i^j`.
Order the terminals as in (1).  If this tuple is crossed, deleting the
artificial terminal ends gives the two portal paths in the definition of
the crossing-completion property, and hence a `K_7` minor.

Suppose neither tuple is crossed.  By the generalized Two Paths Theorem,
add edges on the fixed vertex set of each `A_j` to obtain a `k`-web with
the terminal tuple as frame.  Consider an inserted clique `X` in a facial
triangle of one web.  Every original neighbour of `X` represented in the
auxiliary graph is one of the at most three facial vertices.  Replace any
facial terminal by its corresponding actual vertex of `R`.  The only
boundary vertices whose incidences were omitted from the auxiliary graph
are those in `Z`, and the two shores are anticomplete.  Therefore

\[
 |N_G(X)|\le3+|Z|=10-k\le6.                         \tag{4}
\]

This separates `X` from the opposite nonempty shore, contrary to
seven-connectivity.  Hence every original shore vertex is a rib vertex.

It follows that each graph `G[D_j union R]` has a plane disk embedding
with `R` in the cyclic boundary order (1).  Actual edges of `G[R]` run
along frame arcs; absent frame edges are harmless auxiliary curves.  Glue
the two disks on opposite sides of their common cyclic boundary.  There
are no edges between the shores, so

\[
 P:=G-Z
\]

is planar.  Four-colour `P` by the Four Color Theorem and colour `G[Z]`
with at most two fresh colours using (2).  Fresh palettes make every edge
between `P` and `Z` proper.  This gives at most six colours for `G`, proving
(3). \(\square\)

## Installed applications

1. If `G[S]=C_5 vee K_2`, take `R=C_5` and let `Z` be the universal
   `K_2`.  Every crossing has the explicit model in
   `hadwiger_c5_full_web_closure.md`.
2. If `G[S]=K_{3,2,2}`, with parts `{0,1,2},{3,4},{5,6}`, take
   `R=(1,3,2,4)` and `Z={0,5,6}`.  Here `G[R]=C_4` and `G[Z]` is the
   two-edge star, hence bipartite.  The crossing model is recorded in
   `hadwiger_k322_full_web_closure.md`.

The theorem is designed for further finite boundary layers: only the
crossing-completion property is boundary-specific.  It can be checked by
explicit branch sets in a ten-vertex quotient consisting of `S`, two
contracted crossing paths in one shore, and one full opposite-shore helper.
