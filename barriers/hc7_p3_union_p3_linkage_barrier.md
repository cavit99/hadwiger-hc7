# Seven-connectivity does not force two disjoint ordered three-terminal paths

**Status:** written counterexample; computer-assisted verification of the
five-connectivity assertion; separate internal audit GREEN in
[`hc7_p3_union_p3_linkage_barrier_audit.md`](hc7_p3_union_p3_linkage_barrier_audit.md).
This is a barrier to an intermediate connectivity-only statement, not a
counterexample to `HC_7`.

## 1. The refuted statement

For six distinct nominated vertices

\[
                     a_0,a_1,a_2,b_0,b_1,b_2,
\]

call a pair of vertex-disjoint paths an **ordered `P_3`-pair** when the
first path encounters `a_0,a_1,a_2` in this order and the second encounters
`b_0,b_1,b_2` in this order.

The following assertion is false:

> Every seven-connected `K_7`-minor-free graph has an ordered `P_3`-pair
> for every six distinct nominated vertices.

## 2. A five-connected planar graph with one quadrilateral face

Use the following twenty triangular faces of a plane icosahedron:

\[
\begin{split}
 &(015),(018),(05\,11),(078),(07\,11),
 (126),(128),(156),(236),(239),\\
 &(289),(346),(34\,10),(39\,10),(456),
 (45\,11),(4\,10\,11),(789),(79\,10),(7\,10\,11).
\end{split}                                                   \tag{2.1}
\]

Construct a graph `T` with vertices

\[
                  p_0,\ldots,p_{11},h_0,\ldots,h_{19}.
\]

Here `h_i` represents the `i`th face in (2.1).  Join `p_u` to `h_i`
exactly when vertex `u` belongs to face `i`, and join `h_i` to `h_j`
exactly when the two corresponding icosahedron faces share an edge.  This
is the familiar thirty-two-vertex triangulation dual to the truncated
icosahedron.  Put

\[
                              H=T-h_0h_1.                \tag{2.2}
\]

The faces indexed zero and one share the icosahedron edge `01`.  Deleting
`h_0h_1` merges its two incident triangular faces into the quadrilateral

\[
                         p_0,h_1,p_1,h_0                 \tag{2.3}
\]

in this cyclic order.

The deterministic verifier adjacent to this note checks every set of at
most four vertices of `H`: all 41,449 deletions leave a connected graph.
It also checks planarity, the unique quadrilateral face (2.3), and
`delta(H)=5`.  Therefore

\[
                              \kappa(H)=5.               \tag{2.4}
\]

The upper bound follows already by deleting the five neighbours of `h_0`.

## 3. The seven-connected `K_7`-minor-free host

Add adjacent vertices `a,b`, each complete to `H`, and call the resulting
graph

\[
                              G=K_2\vee H.               \tag{3.1}
\]

Every vertex cut which disconnects `G` must contain both `a,b`; after
their deletion its remaining part must disconnect `H`.  Conversely, the
two universal vertices together with a minimum cut of `H` disconnect
`G`.  Hence

\[
                              \kappa(G)=2+\kappa(H)=7.    \tag{3.2}
\]

The graph `G` has no `K_7` minor.  Indeed, in any clique-minor model a
branch set containing one of `a,b` can be replaced by that singleton,
since it is adjacent to every other branch set.  If `a,b` occur in
different branch sets, the other five branch sets give a `K_5` minor in
the planar graph `H`.  If they occur in one branch set, separating them
into the adjacent singleton branch sets leaves at least six pairwise
adjacent branch sets in `H`.  The cases in which one or both universal
vertices are absent are even stronger.  Every case contradicts the
planarity of `H`.

## 4. The nominated terminals

Nominate the two ordered triples

\[
                         (a,p_0,p_1),\qquad
                         (b,h_1,h_0).                   \tag{4.1}
\]

Suppose that vertex-disjoint paths with these orders existed.  The segment
of the first path from `p_0` to `p_1` cannot use `a` again and cannot use
`b`, which lies on the other path.  It is therefore a `p_0`--`p_1` path
in `H`.  Symmetrically the second path contains an `h_1`--`h_0` path in
`H`, and the two subpaths are vertex-disjoint.

This is impossible in the fixed plane embedding of `H`: the two terminal
pairs alternate on the boundary (2.3) of one face.  Equivalently, join
`p_0` to `p_1` by an arc through the interior of that face.  Together with
a hypothetical `p_0`--`p_1` path in `H`, the arc contains a Jordan curve
which puts `h_1` and `h_0` on opposite sides.  Every `h_1`--`h_0` path in
`H` must meet the first path.

Thus (3.1) with the terminals (4.1) is the asserted counterexample.

## 5. Exact scope

The example is seven-connected and `K_7`-minor-free, so adding only those
two hypotheses to an ordered-two-path theorem cannot work.  It is not
seven-chromatic or contraction-critical.  A theorem usable for `HC_7`
must retain a proper-minor colouring response, a compatible equality
partition, or another hypothesis which excludes this coherent two-apex
planar obstruction.

The construction is not claimed to have minimum order.

## Verification

Run

```bash
PYTHONPATH=active/runtime/deps python3 barriers/hc7_p3_union_p3_linkage_barrier_verify.py
```

Expected final line:

```text
certificate=PASS
```
