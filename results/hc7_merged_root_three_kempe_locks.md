# Three colour-indexed Kempe locks on a merged-root shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_merged_root_three_kempe_locks_audit.md`](hc7_merged_root_three_kempe_locks_audit.md).
This is a
conditional unbounded reduction inside the exact order-eight
opposite-response interface.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing,
 \qquad |S|=8.                                      \tag{1.1}
\]

Assume that `G` is not six-colourable.  Let `d,e` be distinct nonadjacent
vertices of `S`, and let

\[
                    S-\{d,e\}=X\mathbin{\dot\cup}Y                 \tag{1.2}
\]

be a bipartition of `G[S-{d,e}]`, where `X,Y` are nonempty.  Suppose that
the closed `L`-shore has a six-colouring in which

\[
                         X\mid Y\mid\{d,e\}                         \tag{1.3}
\]

is the exact boundary equality partition, but has no six-colouring with
boundary equality partition

\[
                         X\mid Y\mid\{d\}\mid\{e\}.                \tag{1.4}
\]

This is the merged-root side of the audited opposite-response theorem.

## 2. Three simultaneous Kempe locks

### Theorem 2.1

Let `c` be any six-colouring of \(G[L\cup S]\) inducing (1.3).  Write
`alpha` for the common colour of `d,e`, and write `xi,eta` for the two
distinct colours on `X,Y`.  Put

\[
                  \{\beta_1,\beta_2,\beta_3\}
                  =[6]-\{\alpha,\xi,\eta\}.                         \tag{2.1}
\]

For each \(i\in\{1,2,3\}\), the vertices `d,e` belong to the same
connected component of the subgraph induced by colours
`{alpha,beta_i}`.  Consequently there is an `alpha`--`beta_i`
`d`--`e` path `P_i` whose internal vertices all lie in `L`.

In particular, each of `d,e` has a neighbour of colour `beta_i` in `L`,
for every `i`.  For distinct indices `i,j`, every common vertex of
`P_i,P_j` has colour `alpha`.

#### Proof

Fix `beta=beta_i`.  Suppose that `d,e` lie in distinct components of the
`alpha`--`beta` subgraph of \(G[L\cup S]\).  Interchange `alpha,beta` on
the component containing `d`.  This preserves properness and changes the
colour of `d` while leaving the colour of `e` unchanged.

No vertex of \(X\cup Y\) changes colour: its colour is `xi` or `eta`,
whereas the interchange uses `alpha,beta`.  After the interchange, `X,Y`
remain two distinct monochromatic blocks and `d,e` have distinct colours,
both different from the block colours.  The resulting colouring therefore
induces (1.4), contrary to the hypothesis.  Thus `d,e` lie in one
`alpha`--`beta` component.

Only `d,e` have colour `alpha` on the boundary, and `beta` is absent from
the boundary.  A shortest `d`--`e` path in this component consequently has
all internal vertices in `L`.  Its first and last edges prove the
neighbour assertion.  Finally, a vertex common to `P_i` and `P_j` has a
colour in

\[
 \{\alpha,\beta_i\}\cap\{\alpha,\beta_j\}=\{\alpha\},
\]

which proves the last assertion. \(\square\)

## 3. Exact gain and trust boundary

All three paths occur in one fixed colouring and require no edge deletion
or contraction.  This sharpens the general merged-pair Kempe swap in the
archived two-block full-shore theorem by recording the exact three absent
colours, endpoint saturation, and the pairwise intersection rule in the
live order-eight notation.

The paths need not be internally disjoint: paths with different private
colours may share arbitrary `alpha`-coloured vertices.  The
[three-path bottleneck barrier](../barriers/hc7_three_kempe_paths_common_bottleneck_barrier.md)
shows that this intersection rule alone gives neither three disjoint paths
nor a host separator.  The theorem does not place the first hits in named
branch sets, produce a common boundary response, or return an order-seven
separation.

## 4. Dependencies

- [opposite colouring responses at an independent two-vertex odd-cycle
  transversal](hc7_order8_independent_oct_opposite_response.md);
- [the archived general merged-pair Kempe carrier](../archive/hadwiger_two_block_full_shore_state.md),
  cited for provenance; the proof above is self-contained.
