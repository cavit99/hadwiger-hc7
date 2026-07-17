# Independent audit: disjoint ordered-path decoder barrier

**Audited file:** `barriers/hc7_disjoint_palette_two_edge_decoder_barrier.md`
**SHA-256:** `eb5950be9ab818470ce8a9454d4e8bbac7c6e568f7b4acd84914771e04a844d2`
**Verdict:** **GREEN.** The ten-vertex construction has the stated
simultaneous-equality colouring, all four ordered replacement paths, and a
valid tree decomposition of width five. It therefore has no `K_7` minor
and refutes exactly the static implication stated in Section 3.

This is an independent internal audit, not external peer review.

## 1. Construction and colouring

Each of `A` and `B` induces a five-clique. The only cross-edges are the four
edges from `{a,b}` to `{t_1,t_2}` and the four edges from `{c,d}` to
`{r_4,r_5}`. Thus `G` has ten vertices and 28 edges, while
`H=G-{ab,cd}` has 26 edges.

Under colouring (1.2), `A-ab` uses the colour classes

\[
              \{a,b\},\ \{r_3\},\ \{r_4\},\ \{r_5\},
\]

and `B-cd` uses

\[
              \{c,d\},\ \{t_0\},\ \{t_1\},\ \{t_2\}.
\]

All vertices joined by a cross-edge have different colours. Hence (1.2)
is a proper six-colouring of `H`, with both deleted edges monochromatic.
The two colours absent from `A-ab` are 1 and 2, while those absent from
`B-cd` are 4 and 5, so the natural supports are exactly the disjoint sets
displayed in (1.3).

Every consecutive pair on each path in (1.4) is an edge of `H`. Their
colour sequences are respectively

\[
 (0,1,2,0),\quad(0,2,1,0),\quad
 (3,4,5,3),\quad(3,5,4,3),
\]

so they have the claimed cyclic orientations. The two `e`-paths have
vertex set `{a,b,t_1,t_2}` and the two `f`-paths have vertex set
`{c,d,r_4,r_5}`. Therefore every path from the first pair is vertex-disjoint
from every path from the second pair, and each avoids the other three
vertices of its own five-clique.

## 2. Tree-decomposition verification

Every edge of the clique `B` lies in `X_1`, every edge of the clique `A`
lies in `X_5`, the cross-edges from `{c,d}` to `{r_4,r_5}` lie in `X_2`,
and the cross-edges from `{a,b}` to `{t_1,t_2}` lie in `X_4`. Thus every
edge of `G` is covered.

For the running-intersection condition, the bag-index sets are:

\[
\begin{array}{c|c}
c,d&\{1,2\}\\
t_0&\{1\}\\
t_1,t_2&\{1,2,3,4\}\\
r_4,r_5&\{2,3,4,5\}\\
b&\{3,4,5\}\\
a&\{4,5\}\\
r_3&\{5\}.
\end{array}
\]

Every set is an interval in the path `X_1-X_2-X_3-X_4-X_5`. Hence (2.1)
is a tree decomposition. Its bag orders are `5,6,5,6,5`, so its width is
five.

Treewidth is minor-monotone and `tw(K_7)=6`. Therefore `G` contains no
`K_7` minor. This proves the advertised minor exclusion without relying on
a finite minor-search heuristic.

The construction, colouring, four paths, edge coverage, running-intersection
condition, and bag orders were also reproduced by an independent
deterministic check during this audit.

## 3. Exact scope

The example satisfies every premise of the static implication quoted in
Section 3 and violates its `K_7` conclusion. It is therefore a valid
barrier to decoding the ordered paths using only the two clique/path
systems.

It is not seven-connected and does not have the literal balanced
order-eight boundary or the proper-minor response incompatibility of the
active `HC_7` configuration. Nothing in the construction refutes a theorem
that materially uses those hypotheses, and it is not a counterexample to
`HC_7` or Hadwiger's Conjecture.
