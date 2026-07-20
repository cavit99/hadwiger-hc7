# Demand-two Hall responses force a shore-internal block lock

**Archive note:** unaudited frozen order-eight draft retained for provenance;
it is not part of the current proof spine.

**Status:** written proof; separate internal audit pending.  The uniform
lemma below is unbounded.  Its final corollary applies it to the live
positive-boundary-excess order-eight interface.  It does not prove `HC_7`.

## 1. A uniform block-lock lemma

Let

\[
             V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing,
\tag{1.1}
\]

where `A` and `D` are nonempty, `G[A]` is connected, and every vertex of
`B` has a neighbour in `A`.  Suppose that every proper minor of `G` is
`q`-colourable, while `G` is not `q`-colourable.

Let `psi` be a proper `q`-colouring of `G[A\cup B]`.  Write `Sigma` for
its equality partition on `B`, and assume that `Sigma` does not extend to
a proper `q`-colouring of `G[D\cup B]`.

Choose a maximum clique `U` among the singleton blocks of `Sigma`.  Suppose
that the full-subgraph demand is exactly two, so the blocks not represented
by `U` are precisely

\[
                              C_1,C_2.                 \tag{1.2}
\]

Let their colours under `psi` be `alpha,beta`, respectively.

### Theorem 1.1 (demand-two block lock)

In every extension `psi` as above, one component of

\[
              G[A\cup B][\psi^{-1}(\{\alpha,\beta\})]
\tag{1.3}
\]

meets both `C_1` and `C_2`.  Consequently at least one of the following
holds.

1. An edge of `G[B]` joins `C_1` to `C_2`.
2. There is an `alpha`--`beta` path with one end in each of `C_1,C_2`,
   nonempty interior, and every internal vertex in `A`.

In particular, if the two unrepresented blocks are anticomplete in the
boundary, then the boundary operation which merges them is obstructed in
the intact legal shore by a literal shore-internal bichromatic connection.

#### Proof

Assume that no component in (1.3) meets both blocks.  Let `K` be the union
of all full `alpha`--`beta` components of `G[A\cup B]` which meet `C_1`.
Interchange `alpha,beta` on `K`.

Every vertex of `C_1` belongs to `K`, while no vertex of `C_2` does.  Hence
the new closed-shore colouring induces on `B` the partition obtained from
`Sigma` by replacing `C_1,C_2` with their union.  All other boundary blocks
are unchanged.  The union `C_1\cup C_2` is independent: it is one colour
class in the new proper boundary colouring.

The singleton clique `U` remains a clique of singleton blocks, and the new
partition has exactly one block outside `U`.  Thus its full-subgraph demand,
computed using a maximum singleton clique, is at most one.

Use the connected `B`-full subgraph `A` as one universal support in the
transported-partition Hall-reflection theorem.  That theorem applied to the
new colouring of `G[A\cup B]` produces a proper `q`-colouring of
`G[D\cup B]` with the same equality partition.  After a permutation of the
colour names, the two closed-shore colourings agree on `B` and glue, contrary
to the assumption that `G` is not `q`-colourable.

Therefore a component `L` in (1.3) meets both `C_1` and `C_2`.  If a
boundary edge joins the two blocks, outcome 1 holds.  Otherwise choose a
shortest path in `L` between them.  Stop it at the first hit in the opposite
block.  Any internal boundary vertex would lie in one of the two colour
classes and give an earlier endpoint, while the absence of a boundary edge
between the blocks makes the interior nonempty.  Hence every internal
vertex lies in `A`, giving outcome 2.  \(\square\)

## 2. Coupling to a shortest five-colour transition

Retain (1.1), and now suppose that both `A` and `D` are connected and
adjacent to every vertex of `B`, that `|A|,|D|\ge2`, and that `G[B]` has
no `K_5` minor.  Contraction of either open shore gives a proper minor whose
colouring restricts to a five-colour boundary colouring on the other closed
shore.  The theorem of Las Vergnas and Meyniel makes all labelled proper
five-colourings of `G[B]` one Kempe class.

Choose a shortest five-colour Kempe path

\[
                         c_0,c_1,\ldots,c_m            \tag{2.1}
\]

between the two closed-shore extension sets, minimizing over both endpoints,
with `c_0` extending through `A` and `c_m` through `D`.

### Corollary 2.1 (transition paths plus endpoint Hall locks)

The first move of (2.1) is obstructed by a literal bichromatic path with
interior in `A`, and the reverse of the last move is obstructed by such a
path with interior in `D`.

In addition, if the equality partition of either endpoint has full-subgraph
demand two, then its two blocks outside a maximum singleton clique are
joined either by a boundary edge or by the block-lock path of Theorem 1.1
through the corresponding open shore.  When the blocks are boundary-
anticomplete, the path is present in every closed-shore extension of that
endpoint colouring.

If `m=1`, the two transition-obstruction paths use the same pair of colours
and the same operated boundary component, one through each open shore.
The endpoint block-lock paths need not use that colour pair.

#### Proof

The five-colour transition and its first and last obstruction paths are the
shortest-transition argument: a successful lift of the first move through
`A`, or of the reverse last move through `D`, would shorten (2.1).  This is
also Theorem 3.1 of the five-colour two-full-shore transition note.

Each endpoint partition is legal on its named shore and rejected on the
other, since a common extension would glue.  Theorem 1.1 therefore applies
whenever that partition has demand two.  The distance-one statement follows
because the first move and the reverse last move are then the same boundary
Kempe interchange.  \(\square\)

## 3. The live positive-excess consequence

Use the notation of the audited rooted-partition contact-concentration
theorem.  Thus the components `E,C` of `G-B` are connected, anticomplete and
`B`-full, while every `E`--`B` edge-deletion response is legal on `C` and
rejected on the intact `E`-side.  The induced boundary graph `G[B]` is
`K_5`-minor-free by the double-cone vertex-deletion theorem.

### Corollary 3.1 (the hard Hall response is bichromatically locked)

Let `Sigma` be an `E`--`B` edge-deletion response of demand two, and let
`C_1,C_2` be its two blocks outside a maximum singleton clique `U`.  Then:

1. both literal duties

   \[
      D_U(C_i)=C_i\cup\{u\in U:E_G(u,C_i)=\varnothing\}
   \]

   meet `W`; and
2. either an edge of `G[B]` joins `C_1,C_2`, or every six-colouring of the
   intact `C`-side inducing `Sigma` has a bichromatic path from `C_1` to
   `C_2` with nonempty interior in `C`.

The first statement is the exact Hall obstruction from the
contact-concentration theorem; the second is Theorem 1.1 with `A=C` and
`D=E`.

Thus demand two cannot persist merely because the two boundary blocks are
Kempe-separable.  It persists only when the same response has both:

- two complete literal duties concentrated on the enlarged-boundary set
  `W`; and
- a boundary edge or shore-internal bichromatic lock joining the two
  unrepresented blocks.

## 4. Trust boundary

The theorem couples the exact Hall obstruction to a literal path, but it
does not make that path a third connected support.  Its internal vertices
may run through the two already selected connected parts, it need not be
adjacent to every vertex of either complete duty, and it need not have a
full neighbourhood of order seven.

This limitation is real.  The audited finite boundary-path barrier at an
exact seven-separation has two disjoint boundary-full connected subgraphs
and the corresponding demand-critical bichromatic path, but no third
disjoint boundary-full subgraph or smaller selected pair.  That example is
only six-connected and its boundary colouring extends through both shores;
it therefore does not refute a continuation using seven-connectivity and
the incompatible operation-specific responses of the live host.

The next positive step must use the placement of the block-lock path to
split the unique `W`-owning connected part, or else turn failure of that
split into a full neighbourhood of order seven carrying one complete
boundary partition on both sides.

## 5. Dependencies

- [Hall reflection through connected supports](../results/hc7_transported_partition_hall_reflection.md)
- [rooted-partition contact concentration](../results/hc7_order8_rooted_partition_contact_concentration.md)
- [double-cone vertex-deletion equivalence](../results/hc7_double_cone_vertex_deletion_equivalence.md)
- [five-colour two-full-shore transition](hc7_two_full_shore_five_colour_kempe_transition.md)
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, Journal of Combinatorial Theory, Series B **31** (1981),
  95--104.
