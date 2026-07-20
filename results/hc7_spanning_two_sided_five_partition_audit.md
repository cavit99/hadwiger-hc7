# Independent audit of the spanning two-sided packing theorem

**Verdict: GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_spanning_two_sided_five_partition.md`](hc7_spanning_two_sided_five_partition.md)

**Audited SHA-256:**
`e05a3bcbf4f3dab128f22719b3ed9ca799090eb20e6b136c5c31453e3b950605`

Relative to the originally audited revision, this source changes only the
status line and adds the link to this GREEN audit.  Its theorem statement,
proof, corollary, and trust boundary are mathematically unchanged.

This is an internal mathematical audit, not external peer review.

## 1. Extremal choice

The eligible tuples form a finite nonempty family.  Hence maximizing the
number of contact-graph edges and then the number of covered vertices is
well-defined.  Enlarging one member of a tuple never removes its existing
vertices, so it cannot lose an intersection with either of the prescribed
sets `A,B`.

## 2. Path absorption

Let `C` be a component outside the selected subgraphs and let distinct
`i,j` both belong to `I_C`.  Choose an edge from `Q_i` to `C`, an edge from
`C` to `Q_j`, and a path in the connected graph `C` between their ends.
This gives a `Q_i`--`Q_j` path whose internal vertices all lie in `C`.

Adding all vertices of this path except its final vertex in `Q_j` to
`Q_i` preserves the following facts.

- The enlarged set is connected: it contains the old connected `Q_i` and
  the attached initial path.
- It is disjoint from every other selected subgraph: every added vertex is
  in `C`, and the only path vertex in `Q_j` was excluded.
- It still meets `A` and `B`, because it contains the old `Q_i`.
- Every old contact remains.  The final path edge creates the previously
  absent `Q_iQ_j` contact.

Thus, if `i,j` were nonadjacent in the old contact graph, the first
extremal coordinate would strictly increase.  It follows correctly that
`I_C` is a clique.

This argument does not require `A` and `B` to be disjoint, and it remains
valid if added path vertices themselves belong to either set.

## 3. Whole-component absorption

Fix `i in I_C` and replace `Q_i` by `Q_i union C`.  An edge between `C`
and `Q_i` makes the union connected, and the old `Q_i` preserves both
required set intersections.  Disjointness is immediate because `C` lies
outside the old union.

No old contact is lost.  A new contact from `C` to an old `Q_j` can occur
only when `j in I_C`; because `I_C` is a clique, the contact `Q_iQ_j`
already existed.  There is no contact from `C` to a selected subgraph with
index outside `I_C`, by the definition of that index set.  Hence the
contact graph is unchanged while the covered vertex set strictly grows,
contradicting the second extremal coordinate.

Every leftover component is therefore excluded, proving that the selected
subgraphs partition `V(F)`.

## 4. Five-bag application

In the stated pentagonal-bipyramid application, the standard phrase
“fixed root branch sets” supplies the properties used in the final
sentence: the roots are disjoint connected subgraphs outside the core,
they are adjacent to one another, and each original column contains a
neighbour of each root.  Seven disjoint two-sided columns supply any five
eligible initial subgraphs.  The theorem therefore yields five connected
parts spanning the core and meeting both root-neighbourhood sets.

If their contact graph is complete, each of the five parts is adjacent to
both root branch sets, while the roots are adjacent to one another.  These
are exactly seven disjoint connected, pairwise adjacent branch sets of a
`K_7`-minor model.

For complete self-containment, a later editorial revision could spell out
those standard root-branch-set assumptions in the corollary.  They are
already part of the named live setup and do not affect the theorem or its
application.

## Trust boundary

The proof establishes only a spanning extremal partition.  It neither
forces the five-part contact graph to be complete nor transfers a boundary
colouring.  The source states these limitations correctly.
