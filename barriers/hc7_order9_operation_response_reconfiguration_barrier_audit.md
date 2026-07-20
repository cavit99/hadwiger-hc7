# Independent audit of the operation-response reconfiguration barrier

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source
[`hc7_order9_operation_response_reconfiguration_barrier.md`](hc7_order9_operation_response_reconfiguration_barrier.md)
at SHA-256

```text
f49fbcbb454c5001763c4bfea0c045ffa475ed0f397c7fa2dbac230bf305d27d
```

The final source revision changes only its status paragraph and the
repository-relative verifier invocation after promotion to `barriers/`;
the audited mathematics is unchanged.

and the deterministic verifier
[`hc7_order9_operation_response_reconfiguration_barrier_verify.py`](hc7_order9_operation_response_reconfiguration_barrier_verify.py)
at SHA-256

```text
646abb832e9c97819f575324a2e75dfd329082390920d949ed0a88a7c4152fef
```

The finite partition barrier, full single-vertex recolouring connectivity,
Dvořák--Swart realization, connected boundary-full augmentation, controlled
edge-deletion and edge-contraction responses, seven-chromaticity conclusion,
and stated trust boundary are correct.

## 1. Independent finite check

The graph6 string `GA_?G?` decodes to the graph with edges `04,13,56`, so
the displayed boundary graph is indeed `3K_2` together with two isolated
vertices.  The verifier enumerates set partitions canonically and retains
exactly those whose blocks are independent.  Its moves are exactly the
changes of equality partition obtainable by recolouring one literal vertex:
moving it to an existing independent block, or creating a new singleton
block when fewer than five blocks are present.  Recolouring a singleton to
an unused colour leaves the equality partition unchanged and is correctly
irrelevant to adjacency between distinct partitions.

Running the pinned verifier reproduced

```text
PASS partitions=1834 full=674 maximum_independent=8 left=682 right=300 anchors=107 adjacencies=20232
```

An independent brute-force check over all `5^8` labelled assignments found
`200000` proper labelled five-colourings, reproduced all seven displayed
partition and adjacency counts, verified that both languages contain every
nonempty independent set as an exact block, and found the labelled
single-vertex recolouring graph connected on all `200000` vertices.

The written inductive connectivity proof is also valid.  After deleting a
degree-at-most-one vertex, a recolouring path of the smaller graph can be
lifted.  If its unique possible neighbour is about to change from colour
`a` to colour `b`, the deleted vertex can first be assigned one of the three
remaining colours.  Its target colour can be restored after the lifted
path.  Iterating reaches the one-vertex base.

## 2. Realizing the two extension languages

Adding the universal boundary vertex `d` turns every partition in either
language into a proper six-colour equality partition of
`F=K_1\vee H`, with `{d}` a singleton block.  Taking every labelled
six-colouring inducing those partitions gives a relation closed under all
permutations of the six colour names.

Dvořák--Swart, Theorem 3 of *A note on extendable sets of colorings and
rooted minors*, applies exactly here: for every permutation-closed set of
`k`-colourings of a boundary `X`, it supplies a finite graph realizing
exactly that relation, while excluding an `X`-rooted `K_{k+1}` minor and an
unrooted `K_{k+2}` minor.  The invocation with `k=6` therefore realizes
each of `L^+` and `R^+`.

Adding the edges of `F` does not remove a prescribed colouring because all
prescribed partitions are proper on `F`.  Conversely, no nonedge of `F`
can already occur in a realizer: every such pair lies in `H`, and each
language contains a prescribed colouring in which that pair is one exact
block.  Thus the common boundary is induced exactly as claimed.

The connected-full augmentation preserves the extension relation.  Choose
any colour for its central open vertex.  Every new middle vertex on a
length-two path then avoids at most the two endpoint colours, independently
of all other new middle vertices.  Restriction gives the converse.  The
augmentation connects every old open-interior component and supplies an
open-interior neighbour of every literal boundary vertex.  Gluing the two
realizers therefore gives two connected, anticomplete, boundary-full open
shores, while the disjoint extension relations prevent a six-colouring.

## 3. Controlled proper-minor responses

For a forbidden boundary partition `tau`, the enlarged primitive relation
requires the two control vertices to be equal exactly over `tau` and
distinct over every other proper boundary partition.  It is
permutation-closed, so Theorem 3 realizes it.  The realizing graph cannot
already contain the control edge because the relation includes an equal
colouring over `tau`.

After that edge is added, the primitive rejects exactly `tau`.  Taking the
union of one primitive for every partition outside `C^+`, with disjoint
interiors and only `S` shared, intersects their projected extension
relations and therefore realizes exactly `C^+`.

Deleting the control edge for `tau` changes its primitive projection from
the complement of `tau` to all proper boundary partitions, so the whole
shore realizes `C^+\cup\{tau\}`.  Contracting the edge identifies its ends;
the operated primitive then accepts exactly the equal case `tau`, so the
whole shore realizes exactly `tau`.  These conclusions remain true after
the connected-full augmentation.

For `tau` in the opposite shore language, both the deletion and contraction
therefore have a common boundary colouring with the intact opposite shore.
The source now correctly restricts the seven-colour upper-bound argument to
such a nonempty opposite-language choice.  A six-colouring after deleting
that edge has its endpoints equal; assigning a new seventh colour to one
endpoint restores the edge and gives a proper seven-colouring.  Disjointness
of the intact languages supplies the matching lower bound, so the glued
host has chromatic number exactly seven.

## 4. Trust boundary

The verifier certifies the finite partition calculations only; the graph
realizations and operation logic are theorem-level deductions from the
cited Dvořák--Swart result.  The construction does not assert
seven-connectivity, `K_7`-minor-freeness, or six-colourability after every
proper minor.  Although each raw primitive realizer has the exclusions
provided by Theorem 3, boundary-edge augmentation, unions, and the final
two-shore gluing need not preserve them.

Accordingly, this is a barrier to inferring connected operation-response
languages from exact independent-block probes, even when the probes come
from designated internal edge deletions and contractions.  It is not a
counterexample to `HC_7`, nor to a theorem whose alternatives include an
explicit `K_7`-minor model or a full-neighbourhood separation of order at
most seven.
