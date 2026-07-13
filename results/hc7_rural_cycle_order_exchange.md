# Two rural boundary cycles: planar gluing or a rooted `K_4`

## Status and role

This is an **audited theorem**.  It supplies the
missing positive hypothesis exposed by the order-four path barrier: a cyclic
order mismatch alone is too weak, but a mismatch between two *two-connected*
rural shores forces a literal rooted `K_4` subdivision.

The statement is uniform and contains no Moser or near-clique labels.  Its
`HC_7` use is exact: three fixed clique bags complete the rooted `K_4` to a
literal `K_7` whenever each of the four roots has the three prescribed
contacts.

## Lemma 1 (a second Hamiltonian order creates crossing chords)

Let `C` and `D` be cycles on the same finite vertex set `S`, with
`|S|>=4`.  If their cyclic orders are not equal up to reversal, then `D`
has two edges `ab,cd` whose four ends occur alternately on `C`.
Consequently `C union D` contains a subdivision of `K_4` with branch
vertices `a,b,c,d`.

### Proof

Place the vertices of `S` on a circle in the order given by `C`, and draw
every edge of `D` as a chord.  If no two independent `D`-edges cross, the
polygonal drawing of `D` is a simple Hamiltonian polygon on points in
strictly convex position.  Such a polygon must use the circular order (or
its reverse): otherwise some two of its sides cross.  This contradicts the
hypothesis.  Hence two independent edges `ab,cd` of `D` cross, which means
their ends alternate on `C`.

The four `C`-arcs between consecutive members of `{a,b,c,d}`, together
with the two crossing chords `ab,cd`, are internally disjoint and form a
subdivision of `K_4`. \(\square\)

The convex-polygon sentence is purely combinatorial: a cyclic permutation
of points on a circle is noncrossing exactly when it is the boundary order
or its reverse.

## Theorem 2 (two-shore rural cycle exchange)

Let `H_1,H_2` be graphs such that

\[
 V(H_1)\cap V(H_2)=S,\qquad E(H_1)\cap E(H_2)=\varnothing, \tag{2.1}
\]

where `|S|>=4`.  Suppose each `H_i` has an embedding in a closed disk in
which every vertex of `S` lies on the boundary, and suppose each `H_i` is
two-connected.  Then exactly one of the following two **order cases**
holds, with the stated conclusion.

1. The two boundary orders on `S` agree up to reversal.  The disk
   embeddings glue to a plane embedding of `H_1 union H_2`.
2. The two boundary orders differ up to reversal, and `H_1 union H_2`
   contains a subdivision of `K_4` whose four branch vertices belong to
   `S`.  The subdivision is contained in the union of the two facial
   cycles through `S`.

### Proof

In a two-connected plane graph every facial boundary is a cycle.  Let
`C_i` be the boundary cycle of the distinguished disk face in `H_i`.
It contains all of `S`, each exactly once.

If the induced orders agree up to reversal, reflect one disk if necessary,
place one drawing inside a circle and the other outside it, and identify
the equally labelled points of `S` in their common order.  The two open
disks are disjoint, so this is a plane embedding of the union.

Suppose the orders differ.  Contract in each `C_i` every maximal path whose
internal vertices avoid `S`.  The union `C_1 union C_2` then has as a minor
two cycles on the common vertex set `S`, with the two original cyclic
orders.  Lemma 1 gives crossing edges of the second cycle relative to the
first.  Before contraction, those two edges are internally disjoint
`S`-paths in `C_2`, while the four intervening arcs are internally disjoint
`S`-paths in `C_1`.  Because (2.1) makes the two shores disjoint outside
`S`, these six paths lift to a literal subdivision of `K_4` with four
branch vertices in `S`.  This is outcome 2.

The two cases are exclusive by equality or inequality of the two cyclic
orders.  No claim is made that an otherwise planar union cannot contain
some unrelated `K_4` subdivision. \(\square\)

## Corollary 3 (three-row lift to `K_7`)

In Theorem 2, suppose `R_1,R_2,R_3` are three further pairwise disjoint,
connected, pairwise adjacent branch sets, disjoint from `H_1 union H_2`,
and every vertex of `S` has a neighbour in each `R_j`.  If the two rural
orders mismatch, the host graph contains a literal `K_7` model.

### Proof

Convert the rooted subdivision to four rooted minor branch sets as follows.
On each of its six subdivided edge paths, choose one edge as a cut edge and
assign the two remaining path segments to the branch sets at their two
ends.  The pieces assigned to one root are connected through that root;
the four resulting branch sets are disjoint and pairwise adjacent.

Take these four branch sets and the three sets `R_1,R_2,R_3`.  Each of the first four
contains a branch vertex in `S`, so it is adjacent to each `R_j`.  The
three `R_j` are pairwise adjacent, and the first four form a clique minor.
These are seven pairwise adjacent connected branch sets. \(\square\)

The pointwise full-contact hypothesis can be weakened to the literal
condition that every returned rooted branch set meets every `R_j`; the
pointwise form is the stable hypothesis available at a full adhesion.

## Corollary 4 (the order-four barrier is sharp)

If either shore is only connected, Theorem 2 is false: the two subdivided
boundary paths with orders `1234` and `1324` have incompatible orders but
their union is `K_4-e` (with one parallel edge before simplification), so
it has no `K_4` minor.  Thus two-connectivity is not cosmetic; it supplies
the missing closing arcs which turn the order conflict into the two
crossing diagonals of a `K_4` subdivision.

## Exact remaining lift

At an actual near-`K_7` adhesion, this theorem terminates every interface
for which both open shores are two-connected rural societies and four
boundary roots have three common fixed-row contacts.  The only remaining
interfaces are therefore:

1. a shore is not two-connected, in which case its block/adhesion state
   must be exposed;
2. the full contacts are distributed across nonsingleton row bags rather
   than pointwise on the four rooted branch sets; or
3. the two boundary orders agree, in which case the societies glue and
   must be propagated toward one coherent planar/two-apex expansion.

This is a rooted-model exchange, not another finite portal enumeration.
