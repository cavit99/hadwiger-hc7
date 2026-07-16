# A connector between the two unmatched linkage paths in the `2+2` form

**Status:** written proof; separately internally audited GREEN in the adjacent
audit.

This note closes one unbounded class in the minimal `2+2` configuration
from
[`hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md`](hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md).
It does not prove the six-terminal crossing theorem, the support-six
transversal theorem, or `HC_7`.

## 1. Normalized configuration

Let `G` contain disjoint vertex sets

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\}.
\]

Assume the following.

- The set `Q={a_0,a_1,a_2,a_3}` is a clique, `xy` is an edge, and
  \[
       N_Q(x)=\{a_0,a_1\},\qquad N_Q(y)=\{a_2,a_3\}.
  \]
- Every pair of vertices of `B` is adjacent except possibly `p,q`.
- There are six pairwise vertex-disjoint paths, internally disjoint from
  `A union B`, with ends
  \[
  \begin{array}{lll}
   P_0:a_0\mathbin{-}p,&
   P_1:a_1\mathbin{-}b_0,&
   P_2:a_2\mathbin{-}b_1,\\
   P_3:a_3\mathbin{-}b_2,&
   P_4:x\mathbin{-}r,&
   P_5:y\mathbin{-}q.
  \end{array}
  \]

For a path `P` and an end `z`, the notation `P-z` means the path with
that end deleted.

## 2. Connector theorem

### Theorem 2.1

Suppose that `R` is a path with one end

\[
                     u\in V(P_0)
\]

and the other end

\[
                     v\in V(P_5),
\]

whose internal vertices avoid `A union B` and all six paths
`P_0,...,P_5`.  Then `G` contains a `K_7` minor.

### Proof

Define three connected vertex sets

\[
\begin{aligned}
 L&=V(P_0)\cup V(R-v),\\
 M&=V(P_5),\\
 W&=\{a_1,a_2,a_3,x\}
      \cup V(P_1-b_0)\cup V(P_2-b_1)
      \cup V(P_3-b_2)\cup V(P_4-r).
\end{aligned}
\]

The set `L` is connected because `R-v` meets `P_0` at `u`; `M` is a
path; and `W` is connected because `a_1,a_2,a_3` lie in the clique `Q`,
`a_1x` is an edge, and each of the four truncated paths meets its named
left end.  The cleanliness of `R` and the disjointness of the six displayed
paths imply that the seven sets

\[
                  L,\quad M,\quad W,\quad
                  \{b_0\},\quad\{b_1\},\quad
                  \{b_2\},\quad\{r\}                 \tag{2.1}
\]

are pairwise disjoint.

They are pairwise adjacent.  Indeed:

- `L` and `M` are adjacent along the last edge of `R` at `v`;
- `L` and `W` are adjacent by `a_0a_1`, while `M` and `W` are adjacent
  by `yx`;
- `L` contains `p` and `M` contains `q`, so each is adjacent to every one
  of `b_0,b_1,b_2,r` in `B`; the possibly absent edge `pq` is not used;
- `W` is adjacent to `b_0,b_1,b_2,r` along the final edges of
  `P_1,P_2,P_3,P_4`, respectively; and
- `b_0,b_1,b_2,r` form a clique in `B`.

Thus (2.1) is an explicit `K_7`-minor model.  \(\square\)

## 3. Exact scope

Together with the two crossed-linkage constructions in the normalized
`2+2` bridge-augmentation theorem, Theorem 2.1 closes three elementary
ways in which paths outside the three-path subsystem
`P_0 union P_1 union P_5` can force a crossing:

1. one path from `P_0` to `P_5`;
2. two oppositely ordered paths from `P_0` to `P_1`; or
3. two oppositely ordered paths from `P_1` to `P_5`.

These three alternatives do **not** exhaust arbitrary six-terminal
crossings; a concrete barrier is recorded in
[`hc7_two_two_three_pattern_extraction_barrier.md`](../barriers/hc7_two_two_three_pattern_extraction_barrier.md).
