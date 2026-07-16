# Three-connectivity does not force the paired repair linkage

**Status:** explicit counterexample to the intermediate claim stated
below; independently audited in
[`hc7_five_defect_edges_three_connected_linkage_barrier_audit.md`](hc7_five_defect_edges_three_connected_linkage_barrier_audit.md).
This is not a counterexample to `HC_7` or to the star-kernel reduction in
[`../results/hc7_star_private_transversal_large_kernel.md`](../results/hc7_star_private_transversal_large_kernel.md).

## False claim

Let `L={ell_0,...,ell_4}` be a five-clique and let `H` be a
three-connected graph.  Suppose `H` contains distinct edges `e_i` such
that `e_i` is anticomplete to `ell_i` and collectively adjacent to
`L-{ell_i}`.  If `e_i,e_j` are disjoint, then there are disjoint connected
subgraphs containing `e_i,e_j`, respectively, which repair their two
missing adjacencies.

This claim is false even when all five distinguished edges are present.

## Counterexample

Let `H` be the wheel with rim

\[
                 v_0v_1v_2v_3v_4v_0
\]

and centre `z`.  Put

\[
                         e_i=v_i v_{i+1}
\]

with subscripts modulo five.  Make `L` a disjoint five-clique.  For each
`i`, join `ell_i` to exactly the three rim vertices outside
`{v_i,v_{i+1}}`; no adjacency from `ell_i` to `z` is needed.

The wheel `H` is three-connected.  The edge `e_i` is anticomplete to
`ell_i`.  If `j != i`, the two distinct rim edges `e_i,e_j` cannot have
the same two endpoints, so at least one endpoint of `e_i` lies outside
`V(e_j)` and is adjacent to `ell_j`.  Thus `e_i` is collectively adjacent
to every vertex of `L-{ell_i}`.

Now consider the disjoint edges

\[
                         e_0=v_0v_1,
                 \qquad e_2=v_2v_3.
\]

A subgraph containing `e_0` and a neighbour of `ell_0` contains one of
`v_2,v_3,v_4`.  If it is disjoint from a subgraph containing `e_2`, it
cannot contain `v_2` or `v_3`, and hence must contain `v_4`.  Symmetrically,
a subgraph containing `e_2`, a neighbour of `ell_2`, and disjoint from
`e_0` must also contain `v_4`.  The two subgraphs therefore cannot be
vertex-disjoint.

## Exact scope

The graph obtained by adjoining `L` as above is not seven-connected; the
example does not satisfy the full host hypothesis of the support-six
programme.  It proves that the three-connectivity conclusion in
Proposition 3.1 cannot by itself finish the five-clique star branch.
Any completion must still use the full seven-connectivity inequalities
across `L`, contraction-critical colouring data, or both.
