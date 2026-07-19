# Independent audit of the exact-seven bichromatic-path barrier

**Verdict:** GREEN for the finite same-shore barrier, the fixed-skeleton
completion certificate, and the stated trust boundary at the exact revisions
below.

This is a separate internal mathematical and code audit, not external peer
review.

## Exact revisions

The barrier source
`hc7_exact7_bichromatic_path_full_subgraphs_barrier.md` has SHA-256

```text
6db581f47fedffb4105028568630dfa0df3d07da83856142654e21218c1996bc
```

The deterministic verifier
`hc7_exact7_bichromatic_path_full_subgraphs_barrier_verify.py` has SHA-256

```text
41ee3590f9521c47c293f379f404a59a923b570852d4b1a7d40971efc77c6f2c
```

## Mathematical check

The twelve-vertex, thirty-eight-edge construction has the literal
seven-boundary `S` and anticomplete nonempty open shores `A` and `{b}`.
Within `A`, the sets `{a1,a2}` and `{c1,c2}` are connected, adjacent, and
meet every boundary neighbourhood.  Exhaustion of all connected subsets of
`A` confirms that they are its only inclusion-minimal boundary-full
connected subgraphs.  Hence `A` contains no three disjoint such subgraphs,
and every disjoint pair has total order at least four.  The corrected source
consistently restricts this conclusion to the same open shore; globally,
`{b}` is also boundary-full.

The proper boundary partition is exactly

```text
{0,3,5} | {1} | {2} | {4} | {6}.
```

On `Q={1,2,4,6}` the only edge is `12`, so the stated packet demand is
`5-2=3`.  The induced graph on the two colours of `4` and `6` in the closed
`A`-shore is exactly the path `4-a2-c1-6`; its internal vertices lie one in
each selected full subgraph.  Assigning colour 5 to `b` extends the same
partition across the other closed shore and properly colours the whole
graph.  Thus the source now states the correct limitation: it does not model
the incompatible boundary responses of a hypothetical counterexample.

The exhaustive deletion check proves connectivity at least six, while the
displayed six-set disconnects the graph.  Its connectivity is therefore
exactly six.  The canonical connected-partition search is complete for
spanning seven-bag minor models.  Spanning is without loss in this connected
host because every unused component can be absorbed into an adjacent branch
set.  Its negative result proves that the base graph is `K_7`-minor-free.

## Augmentation census

There are exactly seventeen absent edges individually compatible with the
separation, fixed colouring, required nonedge `46`, and triangle-free
singleton graph.  The verifier also rejects combinations that create a
singleton triangle.  Its low-degree filter is a necessary condition for
seven-connectivity, and its increasing-size minimal-mask pruning is lossless:
every admissible seven-connected edge set contains an inclusion-minimal one,
while all four admissibility constraints are hereditary under deleting added
edges.

The census contains exactly 165 minimal seven-connected augmentations, with
size distribution

```text
4:2  5:66  6:89  7:8.
```

An independent enumeration reproduced all 165 and independently validated
a spanning `K_7`-minor model in every one.  Minor containment is monotone
under adding edges, so this proves exactly the fixed-skeleton completion
certificate and no unbounded generalization.

## Trust boundary and verifier run

The example lacks seven-connectivity, seven-chromaticity and therefore the
seven-contraction-critical hypothesis, and an actual critical-triangle
transition with incompatible proper-minor responses.  It refutes only the
same-shore geometric implication stated in the corrected source.

The pinned verifier was rerun and produced exactly:

```text
GREEN exact-seven bichromatic-path/full-subgraph barrier
base: vertices=12 edges=38 connectivity=6 K7_minor=no demand=3
augmentations: allowed_edges=17 minimal_7_connected=165 all_have_K7=yes
augmentation_sizes: 4:2 5:66 6:89 7:8
```
