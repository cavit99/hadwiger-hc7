# Independent audit of the wheel linkage barrier

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- barrier file: `hc7_five_defect_edges_three_connected_linkage_barrier.md`
- SHA-256: `08a5b6d96c7d742094ffb2af6d94bc0a0f4a4d913ca4531bb5daf20a3e87ca8f`

After the substantive audit, only the link to the promoted star-kernel
theorem was changed from `active/` to `results/`; the hash above is the
resulting revision.

## Checks performed

Let the rim vertices be indexed modulo five and let `z` be the hub.
Deleting any zero, one, or two vertices from this wheel leaves it connected,
so the stated graph `H` is three-connected.

For each `i`, the neighbours of `ell_i` in `H` are exactly the three rim
vertices outside the endpoints of `e_i`.  Hence `e_i` is anticomplete to
`ell_i`.  Two distinct rim edges of a five-cycle do not have the same two
endpoints, so for `j!=i` at least one endpoint of `e_i` lies outside
`V(e_j)` and is adjacent to `ell_j`.  Thus every distinguished edge has
exactly the collective boundary contacts required by the false claim.

The edges `e_0=v_0v_1` and `e_2=v_2v_3` are disjoint.  Any connected
subgraph containing `e_0`, disjoint from a subgraph containing `e_2`, and
containing a neighbour of `ell_0` cannot use `v_2` or `v_3`; its only
possible such neighbour is therefore `v_4`.  Symmetrically, the second
subgraph cannot use `v_0` or `v_1`, so its only possible neighbour of
`ell_2` is also `v_4`.  The required repairs cannot be vertex-disjoint.
Connectivity of the subgraphs cannot evade this forced common vertex.

An independent exhaustive check over all connected vertex subsets of the
six-vertex wheel found no disjoint pair satisfying the two repair
requirements.

## Exact scope

The counterexample refutes only the assertion that three-connectivity plus
the five local edge-contact patterns forces the paired repair linkage.  As
the source says, the graph obtained after adjoining `L` is not
seven-connected and is not a counterexample to `HC_7`, Proposition 3.1,
or the star-kernel reduction.  Stronger seven-connectivity or colouring
criticality hypotheses remain available to a future completion.

No unresolved gap remains in the stated counterexample.
