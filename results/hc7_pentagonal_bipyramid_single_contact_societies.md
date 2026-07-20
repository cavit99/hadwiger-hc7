# Single-contact four-connected expansions of the pentagonal bipyramid

**Status:** written proof; separately audited **GREEN** in
[`hc7_pentagonal_bipyramid_single_contact_societies_audit.md`](hc7_pentagonal_bipyramid_single_contact_societies_audit.md).

This note combines the four-connected column dichotomy with a global
cycle-order comparison.  It proves that a spanning expansion by arbitrary
four-connected columns is terminal when every quotient edge has one
literal contact and the contacts at each column have distinct endpoints.
The columns need not have bounded order or be trees.

## 1. Setup

Use the setup of the
[four-connected column theorem](../results/hc7_pentagonal_bipyramid_four_connected_column.md).
In addition, assume that:

1. every column `L_x` is four-connected;
2. for every edge `xy` of the pentagonal bipyramid `P`, there is exactly
   one edge between `L_x` and `L_y`; and
3. at each fixed `L_x`, those `d_P(x)` contact edges have pairwise distinct
   ends in `L_x`.

Write `q_{xy}` for the end in `L_x` of the unique `L_x`--`L_y` edge.
The portal matching rank at `L_x` is then `d_P(x)>=4`.

## 2. The outside neighbour cycle

### Lemma 2.1

For every `x in V(P)`, the graph `P-x` contains a cycle `D_x` through all
vertices of `N_P(x)` in their cyclic order around `x` in the unique plane
embedding of `P`.

### Proof

If `x` is a pole, take the rim five-cycle.  If `x=c_0` is a rim vertex,
with poles `a,b` and rim neighbours `c_4,c_1`, take

\[
                         c_4 a c_1 b c_4.
\]

This is the required order around `c_0`, up to reversal. \(\square\)

### Lemma 2.2 (an order mismatch gives `K_7`)

Suppose the portal vertices of one column `L_x` lie on a facial cycle
`C_x`, but their order on `C_x` is not the cyclic order of `N_P(x)` up to
reversal.  Then the two roots and the columns contain an explicit `K_7`
minor.

### Proof

Choose four portal vertices whose order on `C_x` differs from their order
on the cycle `D_x` of Lemma 2.1.  Such four exist because a cyclic order on
four or five elements is determined, up to reversal, by its restrictions
to four-element subsets.  Contract every column `L_y`, `y ne x`,
to one vertex, retaining the edges of `D_x`.  For each of the four chosen
labels `y`, also contract the edge from that vertex to `q_{xy}`.  After
suppressing portions between consecutive chosen roots, `C_x` and `D_x`
are two cycles on the same four-root set with different cyclic orders.
The elementary two-cycle exchange lemma gives a `K_4` minor rooted at the
four selected portal vertices.

On lifting the contractions, each of the four rooted branch sets contains
the whole external column `L_y` belonging to its selected label.  Hence
each is adjacent to both fixed roots.

It remains to form a fifth branch set.  If `x` is a pole, use the other
pole column.  It is disjoint from the rim cycle and adjacent to every
selected rim column.  If `x` is a rim vertex, use the union of the two
remaining rim columns.  They are adjacent, and collectively they contact
the two poles and the two selected rim-neighbour columns.  In either case
the fifth set is connected, disjoint from the rooted `K_4`, adjacent to
all four of its branch sets, and adjacent to both roots.  The five sets and
the two adjacent roots are an explicit `K_7` model. \(\square\)

## 3. Global dichotomy

### Theorem 3.1

Under the setup in Section 1, at least one of the following holds.

1. The graph contains an explicit `K_7`-minor model.
2. The union `F` of the seven columns is planar.  If, in addition,

   \[
      V(G)=V(F)\mathbin{\dot\cup}\{v,p,w\},\qquad
      R_0=G[\{v,p\}],\quad R_1=G[\{w\}],
   \]

   with `vp,pw` edges and `vw` a nonedge, then `G` is six-colourable.

### Proof

Apply the four-connected column theorem at every `L_x`.  If its rooted
minor outcome occurs, it already gives outcome 1.  Otherwise each `L_x`
has a plane embedding in which all its portal vertices lie on one facial
cycle `C_x`.

If the order at some `C_x` differs from the rotation of `P`, Lemma 2.2
gives outcome 1.  We may therefore reflect the seven column embeddings so
that every portal order agrees with the fixed rotation of `P`.

Replace every vertex `x` in the fixed plane embedding of `P` by a small
disc and draw `L_x` inside it with `C_x` on the disc boundary.  The unique
edge belonging to a quotient edge `xy` can then be drawn through a narrow
corridor around `xy`; there is no second edge in that corridor whose order
must be coordinated.  The discs and corridors are pairwise internally
disjoint, so this gives a plane embedding of `F`.

In the spanning root setup, four-colour `F`, give the nonadjacent vertices
`v,w` one new common colour, and give `p` a sixth colour.  This is a proper
six-colouring of `G`. \(\square\)

## 4. Trust boundary

This theorem closes an unbounded family with arbitrary four-connected
columns.  Its distinct-end and single-contact assumptions are substantive.
With repeated contacts, the orders in opposite ends of one edge bundle
must be coupled, and repeated labels can support nonplanar `K_5`-minor-free
twists.  With portal matching rank at most three, the local rooted-`K_4`
argument does not start.  With an internally separated column, a facial
order need not be unique and its separator must be lifted using literal
host vertices.  These three failures are the remaining structural
branches, rather than additional finite pentagonal-bipyramid cases.

## Dependencies

- the audited four-connected column dichotomy;
- the [two-cycle order-exchange lemma](hc7_rural_cycle_order_exchange.md#lemma-1-a-second-hamiltonian-order-creates-crossing-chords); and
- the Four Colour Theorem.
