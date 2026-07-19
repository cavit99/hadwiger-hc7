# Independent audit: split-shore transversal barrier

**Verdict:** GREEN.

**Audited source:**
`barriers/hc7_order8_split_shore_transversal_barrier.md`

**Source SHA-256:**
`77f34e0f7e588ed0b93f5b8576a9f6d94af918c6e37d14d589d767f3816e079f`

**Audited verifier:**
`barriers/hc7_order8_split_shore_transversal_barrier_verify.py`

**Verifier SHA-256:**
`c841ea30f724e9cab2af630622d751f7052189742b1f33a54d061b871ba26d15`

The source was audited after replacing an imprecise reference to three
connected shore subgraphs by the generalized formulation actually checked:
the root set is connected, while each of the other two shore vertex sets is
only required to become connected after its three boundary vertices are
added.

## Construction and colouring audit

The displayed edge list is exactly the 36 pairs in `EDGE_LIST`.  There are
no loops or repeated edges.  The shore induced by
`R={8,9,10,11}` is `K_4`.  Its two sets `{8,9}` and `{10,11}` are disjoint
and connected.  Direct inspection of the incidence lists shows that each
boundary vertex `0,...,7` has a neighbour in each set, so both are
boundary-full.

For the split boundary partition, the verifier fixes colours

```text
X=0, Y=1, d=2, e=3
```

and exhaustively searches all six-colour assignments on `R`.  It returns
the stated proper colouring `(3,4,5,2)` on `(8,9,10,11)`.  In the merged
case it instead fixes both roots to colour 2, retains distinct colours 0
and 1 on `X` and `Y`, and exhaustively returns no extension.  Thus the
computation tests the exact split and merged boundary partitions claimed in
the note, rather than merely testing unrestricted six-colourability.

## Support-family audit

The root-support family consists of the nonempty connected subsets of `R`
adjacent to both `d` and `e`.  The other two families consist of all
nonempty sets `F` for which `G[X union F]`, respectively `G[Y union F]`, is
connected.  The latter enumeration deliberately does not require `F`
itself to be connected, matching the generalized boundary-block-carrier
definition.

Independent inspection confirms the displayed inclusion-minimal members:

```text
root: {9}, {8,11}, {10,11}
X:    {8,9}, {8,11}, {9,10}, {10,11}
Y:    {11}, {8,9}, {8,10}
```

Every support contains one of its inclusion-minimal members, so it is
enough for a hand check to use these lists.  They admit no pairwise-disjoint
choice, one from each row.  Also, every common transversal must contain 9
to meet the singleton root support and 11 to meet the singleton `Y`
support; it must then contain 8 or 10 to meet the `Y` support `{8,10}`.
Hence its order is at least three.  The set `{8,9,11}` meets every displayed
minimal support and therefore every support.  The verifier independently
enumerates all supports and all transversals of order at most two, so the
claimed common transversal number is exactly three.

## Tree-decomposition audit

The verifier checks, rather than assumes, all three tree-decomposition
axioms: vertex coverage, edge coverage, and connected occurrence bags.  It
also checks that each proposed decomposition graph is a tree.

For the twelve-vertex closed shore, the seven displayed bags have maximum
order six.  Their tree is

```text
0--1--6--3
      |
      5--4--2
```

and direct inspection agrees with the verifier's edge-coverage and
running-intersection checks.  This proves treewidth at most five.  Since
treewidth is minor-monotone and `tw(K_7)=6`, the graph has no `K_7` minor.

For the boundary graph, the six displayed bags have maximum order three.
The verifier again checks every boundary edge and every occurrence
subtree, proving treewidth at most two.  Since `tw(K_5)=4` (indeed,
`tw(K_4)=3`), this is more than sufficient to exclude a `K_5` minor.

The verifier was executed independently and printed exactly:

```text
GREEN K7-minor-free split-shore packing/transversal barrier
shore: |R|=4, two connected S-full parts, split-only response
three-piece packing=none; common transversal number=3
treewidth upper bounds: tw(G[S union R])<=5, tw(G[S])<=2
scope: no opposite merged shore, seven-connectivity, or minor-criticality
```

## Scope and trust boundary

The example refutes only the static one-shore implication stated in the
source.  It has no opposite merged-response shore and is not asserted to
extend to a seven-connected, seven-chromatic, contraction-critical host.
It therefore does not refute the active disjunction allowing a `K_7` minor,
a compatible order-seven separation, or a strict host-level descent.  The
source states these omissions explicitly and does not overstate the
construction as a counterexample to `HC_7`.

No unresolved defect remains in the stated finite counterexample.
