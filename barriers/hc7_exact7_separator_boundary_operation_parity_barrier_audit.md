# Independent audit: exact-seven separator boundary-operation parity barrier

**Verdict:** **GREEN** as a barrier to arguments using only the boundary
operations and whole-shore contractions stated in the source note.

This is an internal mathematical audit, not external peer review.  The
construction is not a counterexample to `HC_7`.

## 1. Audited revision

- construction:
  `barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md`
- audited SHA-256:
  `2737b8a7aedbefe54d93dc2c4ee77812e766909a2841d0ea04c4136329432a6d`
- deterministic checker:
  `barriers/hc7_exact7_separator_boundary_operation_parity_barrier_verify.py`
- checker SHA-256:
  `dfafc67e675f5e525ebedc8a22794e5a8cd5f878445dd85027f76780f5d2f0d2`

The source revision audited here includes the explicit covering choice

```text
P_1=C_1,   P_2=C_2 union ... union C_7
```

in its two-connected-subgraph application.  That choice is important: two
individual layers would leave five layers unaccounted for in the proposed
minor colouring.

The hash above differs from the line-by-line audited revision
`7ef04910215da370a691b8410f539309a3a11e19fefb2254d73541e64bb62f9e`
only because the source status was updated from "audit pending" to the
GREEN verdict recorded here; the construction and proof are unchanged.

## 2. Realization theorem and boundary relations

The invocation of Dvořák--Swart is correct.  Theorem 3 of *A note on
extendable sets of colorings and rooted minors* (arXiv:2504.07764) states
that, for every `k>=3`, every finite boundary `X`, and every set of labelled
`k`-colourings of `X` closed under permutations of the colour names, there
is a finite graph realizing exactly that relation.  The theorem supplies
additional rooted-minor exclusions for the initial realizer, but the source
does not rely on those exclusions after its connectivity amplification.

For each family of equality partitions in the construction, taking all
maps `S->[6]` with an equality partition in that family is closed under all
permutations of `[6]`.  Hence the theorem realizes exactly

```text
E union D   and   O union D.
```

Here `E,O` are the even- and odd-block proper partitions of
`H=2K_3 dotunion K_1`, and `D` consists of the six-block partitions
`Lambda_e` which identify exactly the ends of one edge `e` of `H`.
Every `Lambda_e` is improper on `H` and proper on `H-e`.  Adding all six
edges of `H` therefore removes precisely `D` and leaves exact closed-shore
relations `E` and `O`.

The induced-boundary argument is also valid.  Every nonedge `xy` of `H` is
an independent block, and each parity family contains a proper partition
having `{x,y}` as an exact block.  Consequently neither realizer can already
contain the edge `xy`.  Adding the edges of `H` therefore makes the induced
boundary exactly `H`.

There is an elementary explanation for the exact-block calculation used
here and in the shore-contraction argument.  A nonempty independent set
`I` meets each triangle of `H` in at most one vertex.  The graph `H-I` is
noncomplete and has chromatic number at most three.  Starting with an
optimal colouring of `H-I` and splitting a nonsingleton colour class gives
two proper partitions with consecutive block counts.  Adjoining `I` as one
exact block yields at most six blocks of opposite parity.  Thus both `E`
and `O` contain a partition having `I` as an exact block.

## 3. Connectedness and seven-connectivity

The connected-full augmentation preserves the exact extension relation in
both directions.  Given an old colouring, choose any colour for the new
central vertex.  Each new middle vertex on a length-two path then has to
avoid at most two colours, so it can be coloured with six colours available.
Conversely, restricting any augmented colouring gives an old colouring.
The new open interior is connected and collectively adjacent to every
boundary vertex.

Replacing each open vertex by an independent false-twin class of order
seven also preserves the relation.  Uniformly colouring each class lifts
an old colouring.  Conversely, selecting one representative from every
class in an amplified colouring gives a proper colouring of the old graph,
with the same boundary trace.

After deleting at most six vertices, every false-twin class still has a
representative and at least one of the seven boundary vertices remains.
The quotient of either amplified open shore is connected, every remaining
boundary vertex still has a neighbour on both shores, and a remaining
boundary vertex joins the two shores.  Thus the glued graph remains
connected after every deletion of fewer than seven vertices.  It is
therefore seven-connected; the boundary itself is an order-seven cut.

The same amplification deliberately introduces the omitted target minor.
For each index `h`, choosing the `h`-th twin of every old open vertex gives
a connected subgraph `C_h` adjacent to every boundary vertex.  The seven
sets `C_1,...,C_7` are disjoint and pairwise adjacent, so either amplified
shore contains an explicit `K_7`-minor model.

## 4. Chromatic number and boundary operations

The even and odd final extension relations are disjoint, so the glued graph
is not six-colourable.  For any edge `e=xy` of `H`, the common partition
`Lambda_e` colours both closed shores after deleting `e`; the two colourings
can be aligned by a colour permutation.  It gives a six-colouring of `G-e`
with `x,y` equal, which descends to `G/e`.

Neither `G-e` nor `G/e` is five-colourable.  A five-colouring of `G-e`
would become a six-colouring of `G` after recolouring one endpoint of `e`
with a fresh colour.  A five-colouring of `G/e` first lifts to `G-e` with
the endpoints equal and gives the same contradiction.  Thus

```text
chi(G-e)=chi(G/e)=6.
```

A six-colouring of one `G-e` and a fresh seventh colour also show
`chi(G)<=7`; disjointness of the two relations shows `chi(G)>6`.  Hence
`chi(G)=7`.

The displayed partitions `Pi_*`, `Pi_z1`, and `Pi_z2` have the stated
parities and are proper on `H`.  Deleting `z1` makes the restrictions of
`Pi_*` and `Pi_z1` equal, and deleting `z2` makes the restrictions of
`Pi_*` and `Pi_z2` equal.  Gluing proves the two six-colourability upper
bounds.  Since deleting one vertex lowers chromatic number by at most one,

```text
chi(G-z1)=chi(G-z2)=6.
```

Nevertheless `Pi_*` belongs to `E` and not to `O`, so it does not extend
through the opposite closed shore.

## 5. Whole-shore and two-subgraph contractions

Let `X` be one open shore and `I` a nonempty independent subset of `S`.
The set `X union I` is connected because `X` is connected and boundary-full.
Choose on the retained closed shore a colouring in which `I` is one exact
block and contract `X union I` to `x_I`.

- Every vertex of `S-I` is adjacent to `X`, and exactness gives it a colour
  different from `x_I`.
- The open shores are anticomplete.  Hence a retained open-shore vertex is
  adjacent to `x_I` only through an old neighbour in `I`, and the retained
  colouring gives it a different colour.
- All other edges are already proper in the retained closed-shore
  colouring.

This proves the claimed six-colourability for every such proper minor.

The repaired two-subgraph paragraph is correct.  Put

```text
P_1=C_1,   P_2=C_2 union ... union C_7.
```

These two sets are connected, disjoint, adjacent, boundary-full, and cover
the entire amplified shore.  Contracting `P_1` with
`{j0,j1,q}` and `P_2` with `{b,z1}` therefore leaves no uncoloured part of
that shore.  The odd closed-shore colouring with partition `Pi_z2` assigns
the corresponding two distinct colours to the quotient vertices and still
merges `r,z2`.  Thus even these two actual connected contractions do not
force the remaining singleton blocks to be distinct.

## 6. Verifier replay

Both

```text
python3 barriers/hc7_exact7_separator_boundary_operation_parity_barrier_verify.py
python3 -O barriers/hc7_exact7_separator_boundary_operation_parity_barrier_verify.py
```

returned identically:

```text
GREEN boundary operation parity barrier
states=174 even=93 odd=81
boundary_edges=6 independent_sets=31
```

The checker does not use Python `assert`; its explicit `require` checks
remain active under optimization.  It independently enumerates all proper
at-most-six-block partitions, checks `Pi_*` and both vertex-deletion
partners, checks every `Lambda_e` against `H-e`, and checks the exact-block
property for all 31 nonempty independent sets.  `git diff --check` also
passes on the construction and checker.

## 7. Trust boundary

The source preserves the essential limitations accurately.

- The graph is not `K_7`-minor-free; either amplified shore already contains
  the explicit seven-branch-set model above.
- The graph is not asserted to be seven-contraction-critical or to have
  every proper minor six-colourable.
- Operations internal to an amplified shore and operations on edges between
  a boundary vertex and a shore are not controlled.
- The construction retains an actual order-seven separation.
- It does not preserve the three literal Kempe paths whose Menger separator
  creates the active exact-seven interface.

Accordingly, the construction is a valid barrier only to proofs based on
the listed boundary deletions/contractions, the returned equality
partitions, and the whole-shore independent-block contractions.  It does
not refute an argument that uses global `K_7`-minor exclusion,
seven-contraction-criticality, incident shore-edge operations, or the
labelled path geometry of the active host.
