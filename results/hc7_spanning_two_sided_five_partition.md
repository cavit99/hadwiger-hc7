# Spanning normalization for five two-sided connected subgraphs

**Status:** written proof; separately audited **GREEN** in
[`hc7_spanning_two_sided_five_partition_audit.md`](hc7_spanning_two_sided_five_partition_audit.md).

This note records a general extremal normalization used in the
pentagonal-bipyramid branch of the `HC_7` programme.  It is independent of
that particular quotient graph.

## Theorem (spanning two-sided packing)

Let `F` be a connected graph, let `A,B` be subsets of `V(F)`, and let
`k>=1`.  Suppose `F` contains `k` pairwise vertex-disjoint connected
subgraphs, each of which meets both `A` and `B`.

For such a tuple

\[
                       \mathcal Q=(Q_1,\ldots,Q_k),
\]

let `J(\mathcal Q)` be its **contact graph**: distinct indices `i,j` are
adjacent precisely when an edge of `F` joins `Q_i` to `Q_j`.

Choose `\mathcal Q` lexicographically so as to

1. maximize `|E(J(\mathcal Q))|`; and
2. subject to that, maximize `|\bigcup_iV(Q_i)|`.

Then

\[
                         V(F)=\bigsqcup_{i=1}^k V(Q_i).
\]

### Proof

Suppose that a component `C` of

\[
                    F-\bigcup_{i=1}^kV(Q_i)
\]

exists.  Since `F` is connected, `C` has a neighbour in at least one
`Q_i`.  Let

\[
 I_C=\{i:E_F(C,Q_i)\ne\varnothing\}.
\]

We first show that `I_C` is a clique in `J(\mathcal Q)`.  If distinct
`i,j in I_C` were nonadjacent, connectedness of `C` would give a
`Q_i`--`Q_j` path whose internal vertices lie in `C`.  Add to `Q_i` all
vertices of this path except its final vertex in `Q_j`.  The enlarged
`Q_i` remains connected, remains disjoint from the other `Q_l`, and still
meets both `A` and `B`.  No old contact is lost, while the new `Q_i` is
adjacent to `Q_j`.  This contradicts the first extremal choice.

Thus `I_C` is a clique.  Fix `i in I_C` and replace `Q_i` by `Q_i\cup C`.
This set is connected and retains its intersections with `A` and `B`.
Because `C` is a component outside the old union, it has no neighbour in
an old `Q_j` with `j notin I_C`; because `I_C` is a clique, every contact
that it can add already belongs to `J(\mathcal Q)`.  Hence the contact
graph is unchanged, while the covered vertex set grows.  This contradicts
the second extremal choice.  Therefore no such `C` exists.  \(\square\)

## Corollary (the live five-bag normalization)

Let `R_0,R_1` be the two fixed root branch sets in the spanning
pentagonal-bipyramid core `F`, and put

\[
 A=N_F(R_0),\qquad B=N_F(R_1).
\]

The seven original columns contain seven pairwise disjoint connected
subgraphs meeting both `A` and `B`, so the theorem applies with `k=5`.
Consequently one may choose a partition

\[
                         V(F)=V(Q_1)\dot\cup\cdots\dot\cup V(Q_5)
\]

into connected subgraphs, each meeting both root-neighbourhood sets, whose
contact graph has the maximum possible number of edges among all such
five-tuples.  If that contact graph is `K_5`, the five `Q_i`, together
with `R_0,R_1`, are an explicit `K_7`-minor model.

The theorem does **not** prove that the extremal contact graph is complete.
Nonplanarity or high chromatic number may remain concentrated inside one
part, and five-connectivity alone does not turn a missing quotient contact
into an edge.  The remaining task is to combine this spanning
normalization with the pentagonal-bipyramid ownership data and the
proper-minor colouring responses.
