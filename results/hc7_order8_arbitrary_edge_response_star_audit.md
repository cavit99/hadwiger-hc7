# Independent audit of the arbitrary-edge response-star theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_order8_arbitrary_edge_response_star.md`](hc7_order8_arbitrary_edge_response_star.md)

**Audited SHA-256:**
`1002b613be45b830372c88dc3f3c7c16d501ab8779f38169976a865ebe8c6e8d`

This is an internal mathematical audit, not external peer review.  The
audited theorem is an unbounded host-level reduction.  It does not prove
the remaining order-eight response-coupling theorem or `HC_7`.

## 1. Hypotheses and scope

The source assumes a seven-connected graph `G` with chromatic number seven
whose every proper minor is six-colourable.  It also assumes an eight-set
`S` for which `G-S` has exactly two connected components `C,D`, each
adjacent to every literal vertex of `S`.

The proof uses minor-criticality only in the following two legitimate ways.

1. Deleting an edge `e=vx` gives a six-colouring in which `v,x` have one
   colour.  Every alternate-colour Kempe component containing `v` must
   contain `x`, or one interchange would make `e` proper and six-colour
   `G`.
2. In the order-eight separator alternative inherited from the audited
   prescribed-omission theorem, the deleted crossing edge supplies the
   stated operation-specific boundary response.

No step identifies a palette colour with a boundary vertex or a
minor-model label.

## 2. Lemma 2.1: preserving seven first edges

### 2.1 The no-eight-fan alternative

If there is no eight-fan from `v` to `S` in `G[C union S]`, the fan form of
Menger's theorem gives a separator of order at most seven.  The component
containing `v` lies in `C`; a member of `S` surviving the separator has,
by boundary-fullness, a neighbour in `C` outside that component.  The
opposite open component `D` makes the separation genuine.  Seven-
connectivity therefore makes the full neighbourhood have order exactly
seven and makes the component a proper subset of `C`.  Outcome 1 is valid.

### 2.2 The strict-gammoid formulation

Normalize any eight-fan by truncating each limb at its first vertex of
`S`.  Its eight first neighbours at `v` are distinct.  After deleting `v`,
they are linked by pairwise vertex-disjoint paths to all eight vertices of
`S`.

The source correctly handles direct boundary first neighbours by taking
the strict-gammoid ground set to be

\[
                 N_G(v)\cap(C\cup S),
\]

and by making every member of `S` a sink.  A source already in `S` uses the
length-zero path to itself.  Thus the first-neighbour set `B` of the
eight-fan is an independent eight-set and hence a basis: the target set has
order eight, so the gammoid rank cannot exceed eight.

Let `P` be the seven prescribed first neighbours.  Because `P` has order
seven, a literal vertex `r in S-P` exists.  The prescribed-omission theorem
with this choice of `r` has exactly the three uses claimed in the source:

- an order-seven full-neighbourhood return;
- an order-eight crossing-edge response on a proper subset of `C`; or
- seven paths preserving the first edges and ending at `S-{r}`.

In the third case, deleting `v` witnesses that `P` is independent in the
same strict gammoid.  Matroid augmentation from the independent seven-set
`P` to the basis `B` gives a member `b in B-P` for which `P union {b}` is
independent.  Its order is eight, so its linkage has all of `S` as its
endpoint set.  Prepending the seven prescribed edges and `vb` produces the
claimed eight-fan.  This proves Lemma 2.1, including the cases in which a
prescribed or added first neighbour already lies in `S`.

The normalization at the first boundary hit is implicit in the source's
phrase “the eight-fan says exactly”; it is harmless and does not alter any
first edge or create coincident ends.

## 3. Theorem 3.1: target and source ownership

### 3.1 Five critical first edges

In a six-colouring of `G-e`, the ends `v,x` have a common colour `alpha`.
For every one of the other five colours `beta`, a simple
`alpha,beta` path from `v` to `x` exists.  Its first neighbour `v_beta`
has colour `beta`.  Hence the five first edges are pairwise distinct and
different from `e`.  Seven-connectivity supplies one further incident
edge, so Lemma 2.1 applies to exactly seven prescribed edges.

This remains correct when `x` belongs to `C-v` and when `x` belongs to
`S`.  In the boundary case, `x` is a sink in the gammoid; the linkage path
whose source is `x` is necessarily the length-zero path to `x`, so after
prepending `e` the target limb is the direct edge `vx`.

### 3.2 The order of quantifiers for `p`

The boundary vertex `p` is chosen **after** the augmented eight-linkage:
it is the end of the unique limb whose first edge was not one of the seven
prescribed edges.  Consequently:

- the limb beginning with `e` and the five limbs beginning with the Kempe
  first edges all end outside `p`;
- those six ends are pairwise distinct;
- the auxiliary prescribed limb has the seventh end outside `p`; and
- `p` is not accidentally identified with the target or with a source
  column.

This quantifier order is essential.  No theorem asserting an arbitrary
preselected omitted endpoint is used.

### 3.3 The two roots and seven columns

Put the whole unprescribed `v`--`p` limb into `R_C`.  Boundary-fullness of
`D` supplies a neighbour `w in D` of the now selected `p`.  An ordinary
eight-fan from `w` to `S` exists unless the same Menger argument returns an
order-seven full-neighbourhood separation.  Its `p`-limb may be replaced by
the direct edge `wp`, and `R_D={w}`.

For every `s in S-{p}`, the two fan tails joined through the literal vertex
`s` form one connected column.  Separate fan limbs and the disjoint open
components make all columns and roots pairwise disjoint.  The first fan
edges give every root-to-column adjacency, and `pw` joins the roots.

The column belonging to the `e`-limb contains `x`.  The five distinct
columns belonging to the five critical first edges contain the five
literal vertices `v_beta`.  Fan disjointness shows that these six columns
are distinct; the seventh is the auxiliary column.  Deleting `v` from the
original Kempe path gives exactly the asserted literal path from its owned
source column to the target column.  The path may meet other model pieces,
as the theorem explicitly permits.

Thus the theorem removes the palette-to-label ambiguity at the two ends of
each response path without making the invalid inference that the path is a
clean new column contact.

## 4. Contact consequences

The two roots together with a `K_5` model in the seven-column contact graph
lift to seven disjoint pairwise adjacent connected branch sets.  Hence the
contact graph is `K_5`-minor-free whenever the host is `K_7`-minor-free.

Corollary 4.1 is the exact degree count on the six columns other than the
target.  Five are sources and one is auxiliary.  In the pentagonal
bipyramid a rim vertex has two nonneighbours and a pole has only the other
pole as a nonneighbour, giving the three stated cases.

For Corollary 4.2, the internal vertices of the assumed subpath avoid both
roots and all seven columns.  Absorbing them into the source column
preserves every branch-set label, old contact and root contact and adds the
missing target contact.  The separately audited seven-column structure
theorem proves that adding any missing edge to the pentagonal bipyramid
creates a `K_5` minor, so the resulting explicit `K_7` lift is valid.

## 5. Trust boundary and remaining gap

The source states its limitations accurately.

- The strict order-eight response can belong to any one of the seven
  prescribed edges; it need not preserve the originally selected response.
- The five response paths have literally owned endpoints, but an internal
  path can meet either root or an intermediate column.  Such a path is not
  a new edge of the contact graph.
- When the target is a pole of the pentagonal bipyramid, the auxiliary
  column can be the other pole and all five source columns can already
  contact the target.  The present theorem does not exclude that placement.
- No compatible pair of boundary equality partitions is produced.

Accordingly, the audited theorem is a genuine unbounded synchronization
result, not the response-coupling closure.  The remaining operation-specific
problem is to convert dirty response paths into label-preserving column
splits or a compatible order-seven separation, or to force a response role
onto the exceptional auxiliary column.

## 6. Verdict

The prescribed-first-edge augmentation, the post-linkage choice of `p`,
the root construction, the target/source ownership and the clean-contact
corollary are all correct at the audited source hash.  **GREEN.**
