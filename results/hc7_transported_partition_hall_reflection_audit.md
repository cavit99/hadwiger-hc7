# Independent audit: Hall reflection through mixed connected supports

**Verdict:** **GREEN** for the exact source revision below.

This is a separate internal mathematical audit, not external peer review.
It checks the matching construction, every branch-set adjacency, the exact
boundary-colouring pullback, the subordinate-system converse, and the
seven-vertex demand classification.

## Audited revision

The audited source is
`results/hc7_transported_partition_hall_reflection.md`.

**Source SHA-256:**

```text
e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4
```

## 1. Assigned connected supports

For a matched block `C_i`, its assigned boundary-full subgraph meets every
literal vertex of `C_i`.  A matched named subgraph `W_k` does the same
because `C_i subseteq D_U(C_i)`.  Since each block is independent, this is
exactly what is needed for `V(Y_i) union C_i` to be connected.

Two assigned named subgraphs are adjacent by hypothesis.  If one assigned
subgraph is boundary-full, it is adjacent to every vertex of the other
nonempty boundary block.  Thus all assigned unions are pairwise adjacent,
without any unproved adjacency between the open-side supports themselves.

For `u in U`, either a boundary edge joins `u` to `C_i`, or `u` belongs to
the duty of `C_i`.  In the latter case a named assigned support meets `u` by
the incidence condition; a boundary-full support meets it automatically.
The assigned unions and the singleton clique `U` therefore form the stated
clique minor after contraction.

## 2. Colouring and gluing

The assumption `d>=1` guarantees that at least one boundary--open-side edge
is contracted, so the minor is proper.  There is one clique vertex for each
block of `Sigma`, and there are at most `q` of them.  Any `q`-colouring of
the proper minor consequently gives different colours to different blocks.

Pulling the image colour back only to the boundary vertices of its block
gives a proper colouring of the untouched closed shore: all edges from
that block to the untouched shore or to another boundary block are
represented at the contracted image.  The induced partition is exactly
`Sigma`, not a coarsening.  A palette permutation then aligns it with the
given colouring of the first closed shore, and the two colourings glue
because the open sides are anticomplete.

## 3. Exact Hall converse in the stated class

The converse is deliberately limited to systems assigning one whole listed
support to each remaining block.  A named support can be assigned only if
it meets every block vertex, for connectedness, and every singleton in `U`
which has no boundary edge to the block, for the required clique
adjacency.  This is precisely the duty incidence.  Boundary-full supports
are universal, and disjointness requires distinct supports.  Hence such a
subordinate system is exactly a saturating matching, and Hall's deficient
family (2.1) is exact.

The specialization with `r` universal supports and one named support is
then immediate: at most `r` blocks need no duty incidence, the next block
must use the named support, and more than `r+1` blocks exceed capacity.

## 4. Seven-vertex enumeration

Let `k` be the number of blocks, `s` the number of singleton blocks and
`omega` the clique number on their vertices.  The demand is `k-omega`.
The integer partitions of seven verify the source tables:

* for five blocks the only shapes are `3+1+1+1+1` and
  `2+2+1+1+1`; demand at least four means `omega=1`;
* for six blocks the only shape is `2+1+1+1+1+1`; demand at least four
  means `omega<=2`; and
* with four blocks, at least one singleton exists, so demand is at most
  three.

Solving `k-omega=3` gives exactly the six demand-three rows listed in the
source.  No block shape is omitted.

## 5. Trust boundary

The theorem does not assert that the legally coloured shore contains the
required supports.  In particular, a universal endpoint lift of an
order-seven separation does not automatically place two disjoint
boundary-full connected subgraphs and one duty-compatible named subgraph
on the same shore as the legal trace.

Failure of the displayed Hall condition rules out only systems subordinate
to the displayed supports.  Other connected subgraphs or a branch-set
rerouting may still succeed.  The theorem neither repairs an improper
transported assignment nor proves `HC_7`.

No mathematical error was found.
