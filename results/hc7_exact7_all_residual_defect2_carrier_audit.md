# Independent audit of defect-two reflection on every residual seven-boundary

**Verdict:** GREEN for Theorems 1.1 and 2.1 at the revisions identified
below.

**Audited source:**
[`hc7_exact7_all_residual_defect2_carrier.md`](hc7_exact7_all_residual_defect2_carrier.md)
at SHA-256

```text
7957de3aeb635a9f48e1e1668e34f43abbba15cac270c0f716821b2925af3fd8
```

The only change from the source revision first checked was the status line,
updated after this GREEN audit; the theorem statement and proof are
unchanged.

**Audited finite verifier:**
[`hc7_exact7_all_residual_defect2_probe.py`](hc7_exact7_all_residual_defect2_probe.py)
at SHA-256

```text
20ef45d8235dd6ad12b3688545473cc0bed98b4231945ef0be54c7d13c033a6b
```

This is a separate internal mathematical and computational audit, not
external peer review.  The result is conditional on the already-audited
129-boundary classification.  It does not prove `HC_7` and does not produce
the third connected subgraph required by Theorem 2.1.

## 1. Census coverage

The verifier starts with the complete NetworkX atlas through order seven.
Among its unlabelled seven-vertex graphs it retains exactly those with
clique number at most three.  It then applies the two invariant tests which
define the frozen residual:

1. there is no robust independent block from the adaptive `(1,2)`
   boundary closure; and
2. no deletion of two vertices leaves a graph with a `K_4` minor.

The implementation of the first test is exact in this range.  A robust
block of order two cannot occur because its five-vertex complement would
need clique number at least four.  For blocks of orders three through seven,
the imported `robust_block` conditions are exactly the three criteria in the
audited classification theorem.

The implementation of the second test is also exact.  A `K_4` model on at
most five vertices either is a `K_4` subgraph or has precisely one
two-vertex branch set, which can be contracted to leave four singleton
vertices forming a clique.  Thus checking the original graph and every
single edge contraction covers every possible model on the five remaining
vertices.

The resulting count is 129, agreeing with both promoted residual
classifications.  For each graph the verifier checks

\[
  1+7+\binom72=29
\]

literal defect sets, for a total of

\[
                         129\cdot29=3741
\]

cells.  Because every subset of orders zero, one and two is checked on each
unlabelled representative, the calculation remains valid after transporting
an actual labelled boundary and its literal defect set through an
isomorphism.

## 2. Partition coverage and quantifier order

The recursive partition generator lists all 876 set partitions of a
seven-set into at most six blocks.  The excluded seventh partition is the
seven-singleton partition and cannot be induced by a six-colouring.  A
partition is retained exactly when all its blocks are independent in the
boundary graph and the preselected block `I` occurs as one exact block.

For each `(H,D)` cell, the search order is the one required by the host
argument:

```text
boundary graph H and literal defect set D
  -> choose one non-singleton inclusion-maximal independent block I
  -> receive an arbitrary proper at-most-six-block partition containing I
  -> choose a maximum singleton clique and the block represented by T.
```

In particular, the selected `I` is fixed before the proper-minor colouring
is known.  The maximum singleton clique and carrier assignment may depend on
the actual returned partition, which is permitted by the reflection
argument.  The verifier accepts a cell only if one such `I` works for every
returned partition.

Every enumerated witness is checked directly for independence and
inclusion-maximality.  A fresh auxiliary count found selected witness sizes

```text
size 2:  535 cells
size 3: 2915 cells
size 4:  291 cells
```

and found that every selected witness admits a demand-three return.  Thus
the new calculation is not merely reusing the old robust-block closure.

## 3. Demand and maximum-clique logic

For a returned partition `Pi`, let `Q` be a maximum clique among its
singleton blocks.  Then

\[
 |\Pi|-|Q|=d_H(\Pi),
\]

so the blocks not represented by `Q` are exactly the `d_H(Pi)`
unrepresented blocks.  The verifier enumerates every maximum such clique;
its edge-count test is equivalent to the clique condition because each
candidate already has the computed maximum order.

When the demand is at most two, two boundary-full connected subgraphs can
represent all unrepresented blocks.  When the demand is three, the verifier
requires an unrepresented block `B` satisfying

\[
 B\cap D=\varnothing,
 \qquad N_H(q)\cap B\ne\varnothing\quad(q\in Q\cap D).
\]

This is exactly the required condition for a connected subgraph `T`
adjacent to every boundary vertex outside `D`:

* `B cap D=emptyset` makes `T union B` connected, since every literal
  vertex of `B` has a neighbour in `T`;
* every `q in Q-D` is adjacent directly to `T`; and
* for `q in Q cap D`, the displayed boundary edge makes `q` adjacent to
  `T union B`.

Partitions of demand above three are rejected.  The fresh run visits all
3741 cells, finds a witness in every cell, and terminates with

```text
boundaries=129
cells=3741
witnesses=3741
failures=0
CERTIFIED full-residual defect-two carrier reflection
```

Thus the finite conclusion in Theorem 1.1 has the stated universal
quantifiers.

## 4. Host-graph lift

Let `R` be the boundary-full connected subgraph on the opposite open shore.
Because `I` is independent and every vertex of `I` has a neighbour in `R`,
the set `R union I` is connected.  Contracting a spanning tree is a proper
minor operation.  Expanding a six-colouring only onto the untouched closed
`A`-shore gives every vertex of `I` the contracted image's colour.  This is
proper there, and boundary fullness makes the image adjacent to every
literal vertex of `S-I`; hence `I` is one **exact** boundary colour class.

For the returned partition `Pi`, assign the two boundary-full connected
subgraphs `P_1,P_2` to two unrepresented blocks.  At demand three, assign
`T` to the block certified in Section 3.  The resulting unions are
connected and pairwise disjoint.  They are also pairwise adjacent even
though no edge between `P_1,P_2,T` is assumed: a boundary-full subgraph has
an edge to every literal vertex of the nonempty boundary block assigned to
each other representative.  Boundary fullness similarly supplies every
adjacency to retained singleton representatives, except those repaired by
the certified boundary edges from `B` in the `T` representative.

These are precisely the hypotheses of the audited partition-specific
carrier-reflection theorem.  Contracting the representatives on the
`A`-shore produces a proper minor and a six-colouring of the untouched
closed `B`-shore with exactly the same boundary partition.  A permutation
of the six colour names aligns the two injective block-to-colour maps, and
the absence of `A`--`B` edges lets the colourings glue.

The proof also covers the demand-one and demand-two cases: the non-singleton
exact block `I` ensures the demand is nonzero, so at least one representative
is contracted and the reflecting minor is proper.

## 5. Exact trust boundary

The promoted conclusion should be stated with all of the following
conditions visible:

* the boundary graph is in the frozen 129-graph residual;
* the two boundary-full connected subgraphs and the defect-at-most-two
  connected subgraph lie pairwise disjointly in the same open shore;
* the opposite open shore contains a boundary-full connected subgraph; and
* every proper minor of the host graph is six-colourable.

The theorem supplies a preselected exact independent boundary block and
then completes the colour reflection.  It does not show that a general
`(1,2)` configuration contains the third connected subgraph, preserve an
unrelated previously selected boundary partition, or close any case outside
the audited 129-boundary classification.

## 6. Reproducibility

The audited run was

```text
PYTHONPATH=active/runtime/deps:results python3 \
  results/hc7_exact7_all_residual_defect2_probe.py
```

It terminated with the certificate reproduced in Section 3.
