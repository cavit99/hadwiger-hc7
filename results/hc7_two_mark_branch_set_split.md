# A two-mark branch-set split or full-neighbourhood separation

**Status:** written proof; separate internal audit GREEN.  The theorem is
parameter-uniform.  Its `HC_7` corollary closes the branch-set splitting
step for a spanning one-missing-adjacency model, but it does not colour the
returned separation.

## 1. The split theorem

### Theorem 1.1

Let `t>=4`, and let

\[
                 \{c\},D,U,V_1,\ldots,V_{t-3}                 \tag{1.1}
\]

be pairwise disjoint nonempty connected vertex sets in a graph `G` such
that

1. `D,U,V_1,...,V_{t-3}` form a `K_{t-1}`-minor model;
2. `c` is anticomplete to `D` and adjacent to each of
   `U,V_1,...,V_{t-3}`; and
3. `U` contains two distinct neighbours of `c`.

Fix any protected vertex `rho in U`.  Then at least one of the following
holds.

1. `G` contains a `K_t` minor.
2. There is a nonempty proper connected set `X subset U` such that
   `N_G(X)` is the boundary of an actual separation with two nonempty open
   sides.

In outcome 1 the branch set replacing `U` can be chosen to contain `rho`.

#### Proof

Choose a spanning tree `T_U` of `G[U]`.  Let `T_0` be the minimal subtree
of `T_U` containing `rho` and every vertex of `N_G(c)\cap U`.  Since the
latter set has at least two vertices, `T_0` has a leaf

\[
                m\in N_G(c)\cap U,\qquad m\ne\rho .             \tag{1.2}
\]

Cut the edge of `T_0` incident with `m`, viewed as an edge of `T_U`.
The two components of the resulting spanning forest induce a partition

\[
                         U=Z\mathbin{\dot\cup}W                 \tag{1.3}
\]

into nonempty connected adjacent sets.  Choose the names so that
`rho in W`.  The component `Z` contains `m`, while `W` contains another
vertex of `N_G(c)\cap U`; hence both `Z` and `W` are adjacent to
`c`.

If `Z` is anticomplete to `D`, then `D` is disjoint from
`Z union N_G(Z)`.  Thus

\[
                    (Z\cup N_G(Z),\;V(G)-Z)                     \tag{1.4}
\]

is an actual separation whose open sides contain `Z` and `D`.  This is
outcome 2.

Suppose that `Z` is adjacent to `D`.  If `W` is anticomplete to some
`V_j`, the analogous separation with full boundary `N_G(W)` has open
sides containing `W` and `V_j`, again giving outcome 2.

It remains that `Z` is adjacent to `D` and `W` is adjacent to every
`V_j`.  Then

\[
                 \{c\},\quad D\cup Z,\quad W,\quad
                 V_1,\ldots,V_{t-3}                            \tag{1.5}
\]

are branch sets of a `K_t` model.  Indeed, `D union Z` is connected;
the cut edge in (1.3) supplies its adjacency to `W`; the two marked
vertices supply the adjacencies from `c` to `D union Z` and to `W`; `D`
supplies every adjacency from `D union Z` to a set `V_j`; and `W` retains
every adjacency to a set `V_j`.  All remaining adjacencies were already
present in the `K_{t-1}` model.  The residual branch set `W` contains the
protected vertex `rho`.  \(\square\)

### Corollary 1.2 (connectivity consequence)

If `G` is `t`-connected, the separator in outcome 2 has order at least
`t`.  If it has order exactly `t`, every component of its deletion is
adjacent to every boundary vertex.

#### Proof

The lower bound is `t`-connectivity.  If `N_G(X)` has order `t` and a
component `K` of `G-N_G(X)` missed one boundary vertex `v`, then
`N_G(K) subseteq N_G(X)-{v}` would separate `K` using at most `t-1`
vertices.  \(\square\)

## 2. Consequence for a spanning one-missing-adjacency model

### Corollary 2.1

Let `G` be seven-connected, and suppose that its vertex set is partitioned
into seven branch sets

\[
                        \{c\},D,U_1,\ldots,U_5                 \tag{2.1}
\]

which form a labelled `K_7^-` model whose unique missing adjacency is
`cD`.  Then `G` contains a `K_7` minor or has an actual full-neighbourhood
separation.  In the latter case the boundary has order at least seven and
is full if its order is seven.

#### Proof

Spanningness and the missing adjacency give

\[
                          N_G(c)\subseteq\bigcup_{i=1}^5U_i.   \tag{2.2}
\]

Seven-connectivity implies `d_G(c)>=7`.  Hence one of the five common
branch sets, say `U_i`, contains two neighbours of `c`.  Apply Theorem 1.1
with `t=7`, using any prescribed root in `U_i`, and then apply
Corollary 1.2.  \(\square\)

## 3. Trust boundary

The result preserves the centre, the deficient bag and every untouched
branch-set label in its explicit minor model.  It removes the need for an
unrestricted shortest centre-to-deficient-bag path or an unlabelled
first-hit allocation.

The separation outcome is not terminal for `HC_7`: its order may exceed
seven, and no common equality partition on its boundary is proved here.
The next task is a label-preserving separator-colouring theorem, not a
further donor-bag split.
