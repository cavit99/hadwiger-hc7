# An endpoint `K_4` gives a strict branch-set transfer or an order-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_endpoint_k4_transfer_or_order7_audit.md`](hc7_endpoint_k4_transfer_or_order7_audit.md).
This note treats the
endpoint-`K_4` alternative in the exact two-edge response obtained after the
three lost branch-set adjacencies have been concentrated in one component.
It does not synchronize the colourings across the returned separation and
does not prove `HC_7`.

## 1. Setting

Use the hypotheses, notation, and lexicographic model choice of the
[three-owner concentration theorem](../results/hc7_three_owner_reserved_component_concentration.md).
Thus `G` is seven-connected and has a spanning labelled
`K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3,                 \tag{1.1}
\]

whose only possible missing adjacency is `X-Y`.  The donor branch set is

\[
                 U=U_0\mathbin{\dot\cup}C,            \tag{1.2}
\]

where

\[
                 U_0=U'\cup(W-C)                     \tag{1.3}
\]

is connected, contains the prescribed root of `U`, and is adjacent to the
connected set `C`.  The three owners are

\[
                 I=\{R_i,R_j,R_k\}\subseteq
                    \{X,Y,F_1,F_2,F_3\}.              \tag{1.4}
\]

Every old `U-R` contact for `R in I` has its end in `U` inside `C`.
Every branch set among `X,Y,F_1,F_2,F_3` which is not an owner has an edge
to `U'`, and the fixed response edge joins `D` to `U'`.

The literal order-eight boundary theorem also gives one boundary vertex
`s_R in R` for each of the six branch sets different from `U`, such that

\[
                 N_G(C)-U=\{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.
                                                               \tag{1.5}
\]

Let

\[
                 e=a_ir_i,\qquad f=a_jr_j             \tag{1.6}
\]

be the disjoint differently labelled contact edges supplied by Corollary
4.1 of the concentration theorem.  Thus `a_i,a_j in C` are distinct,
`r_i in R_i`, and `r_j in R_j`.  Assume that

\[
                 G[\{a_i,a_j,r_i,r_j\}]\cong K_4.     \tag{1.7}
\]

## 2. Endpoint-clique fork

### Theorem 2.1

Under the setting above, at least one of the following holds.

1. The displayed branch sets can be modified to give an explicit
   `K_7`-minor model in `G`.
2. There is a nonempty connected set `B subseteq C` whose full
   neighbourhood is

   \[
       N_G(B)=\{a_i,s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.       \tag{2.1}
   \]

   In particular, this is the boundary of an actual order-seven
   separation.
3. There is another compatible spanning labelled
   `K_7`-minus-one-edge model with the same possible missing pair,
   prescribed roots, selected boundary partition, fixed response subgraph,
   and relaxed first-hit rank at least that of the old model, in which the
   donor `U` is replaced by a proper connected subset.

Consequently, for the lexicographically chosen model in a `K_7`-minor-free
host, outcome 2 must hold.

#### Proof

Write

\[
                         a=a_i,\qquad b=a_j.           \tag{2.2}
\]

Let `Q` be the component of `G[U-a]` containing `U_0`.  This component is
well-defined because `U_0` is connected and is disjoint from `a`.

Suppose first that `b notin Q`, and let `B` be the component of `G[U-a]`
containing `b`.  Every vertex of `U_0` belongs to `Q`, so `B subseteq C`.
As `B` is a component after deleting `a`,

\[
                         N_G(B)\cap U=\{a\};           \tag{2.3}
\]

the inclusion from right to left uses the edge `ab` in the endpoint
`K_4`.  Every neighbour of `B` outside `U` is a neighbour of `C`, and
(1.5) therefore gives

\[
  N_G(B)\subseteq
  \{a,s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\}.          \tag{2.4}
\]

The set `Q` is nonempty and has no vertex in `B union N_G(B)`.  Hence the
full neighbourhood of `B` is an actual vertex cut.  Seven-connectivity
gives `|N_G(B)|>=7`; (2.4) gives the reverse inequality.  Equality holds,
which proves (2.1) and outcome 2.

It remains that `b in Q`.  Put

\[
                         L=U-Q.                        \tag{2.5}
\]

The set `L` is connected.  Indeed, it consists of `a` together with all
components of `G[U-a]` other than `Q`, and every such component has a
neighbour at `a` because `G[U]` is connected.  It is nonempty, lies in
`C`, contains `a`, and omits `b`.  The set `Q` is connected, contains the
prescribed root of `U`, and is adjacent to `L` through the edge `ab`.

Let

\[
                         A_{R_k}=N_G(R_k)\cap C.       \tag{2.6}
\]

If `A_{R_k}\cap Q` is nonempty, enlarge `R_i` by `L`.  The enlarged set is
connected through the edge `ar_i`.  The retained donor `Q` is adjacent to
both `R_i` and `R_j` through the endpoint-`K_4` edges `br_i` and `br_j`,
and it remains adjacent to `R_k` through the retained portal in
`A_{R_k}\cap Q`.

If `A_{R_k}\cap Q` is empty, then all the nonempty portal set `A_{R_k}`
lies in `L`.  Enlarge `R_k` by `L`.  This enlarged set is connected through
an `A_{R_k}-R_k` edge, and it is adjacent to the retained donor `Q` through
the edge `ab`.  Again `Q` is adjacent to `R_i` and `R_j` through `br_i`
and `br_j`.

In either subcase every nonowner among
`X,Y,F_1,F_2,F_3` retains its old edge to `U' subseteq U_0 subseteq Q`,
and `D` retains the fixed response edge to `U'`.  Enlarging one outside
branch set destroys none of its old adjacencies.  Thus replacing `U` by
`Q` and the selected recipient by its union with `L` gives seven disjoint
connected spanning branch sets.  If the operation repairs `X-Y`, they are
an explicit `K_7`-minor model, which is outcome 1.  Otherwise their only
possible missing adjacency remains `X-Y`.

All prescribed roots and the fixed response subgraph remain in their old
labelled branch sets.  The relaxed first-hit rank does not decrease.  A
ranked path whose terminal label is not `U` avoided all of the old donor
and therefore avoids `L`.  A ranked `U`-path ending in `L` is replaced,
using the same designated source port, by a path inside the fixed connected
response subgraph followed by the fixed response edge into `U' subseteq Q`.
This is exactly the rank-preserving replacement used in the audited
branch-set-transfer theorem.  Since `L` is nonempty, `Q` is a proper subset
of `U`.  This proves outcome 3.

For the lexicographically chosen model, outcome 3 contradicts maximum
first-hit rank followed by minimum donor order.  In a `K_7`-minor-free host
outcome 1 is excluded.  Hence outcome 2 remains. \(\square\)

## 3. Adjacency interpretation

The endpoint `K_4` is therefore not merely an unlabelled local clique.
One donor endpoint supplies simultaneous retained contacts to the two
selected owner labels while the other endpoint is peeled into an owner
branch set.  If the two endpoints cannot remain connected to the rooted
part of the donor after one is deleted, the separated component has only
one neighbour inside `U` and at most the six literal outside-boundary
neighbours, which is exactly where seven-connectivity returns order seven.

The theorem does not determine a common six-colouring of the two closed
shores of (2.1).  That colouring-compatibility question remains part of the
exact-seven gluing programme.

## 4. Dependencies

- [three-owner concentration and the two-edge response substrate](../results/hc7_three_owner_reserved_component_concentration.md)
- [literal order-eight boundary normal form](../results/hc7_reserved_component_linkage_completion.md)
- [rank preservation under a label-preserving branch-set transfer](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md)
