# Nested full-neighbourhood descent

**Status:** written proof; separate internal audit GREEN.  This is a general
separator lemma.  It identifies the exact obstruction to decreasing the
literal separator excess of a connected side.  It does not by itself
preserve a previously chosen boundary partition or minor-model branch sets.

## Theorem 1 (strict descent or a boundary-full interface)

Let `G` be a seven-connected graph.  Let `R` be a nonempty connected
vertex set, put

\[
                         X=N_G(R),
\]

and suppose that `G-(R union X)` is nonempty.  Write

\[
                    |X|=7+\varepsilon,qquad \varepsilon\ge 0.
\]

For every component `C` of `G-X`, put

\[
 d_X(C)=|X-N_G(C)|.
\]

Then

\[
 0\le d_X(C)\le\varepsilon,
 \qquad
 |N_G(C)|=7+\varepsilon-d_X(C).                 \tag{1.1}
\]

Consequently, for every component `C` other than `R`, one of the following
holds.

1. `d_X(C)>0`, and `C` is a connected side of an actual separation whose
   literal separator excess is strictly smaller than `epsilon`.
2. `d_X(C)=0`, and `C` is adjacent to every literal vertex of `X`.

In particular, if `epsilon=1`, then either `G` has an actual order-seven
separation, or every component of `G-X` is adjacent to all eight vertices
of `X`.  The latter is the exact irreducible order-eight obstruction to
separator-excess descent.

### Proof

Every neighbour of a component `C` of `G-X` belongs to `X`, so

\[
                      N_G(C)=X-(X-N_G(C)).
\]

This gives the equality in (1.1).  The set `N_G(C)` separates the nonempty
connected set `C` from another nonempty component of `G-X`: if `C=R`, use
the assumed nonempty far side, and otherwise use `R`.  Seven-connectivity
therefore gives `|N_G(C)|>=7`, and (1.1) gives
`d_X(C)<=epsilon`.

If `d_X(C)>0`, the full neighbourhood `N_G(C)` is the boundary of an
actual separation and has separator excess

\[
 |N_G(C)|-7=\varepsilon-d_X(C)<\varepsilon.
\]

If `d_X(C)=0`, the displayed identity says exactly that `N_G(C)=X`.
For `epsilon=1`, a positive integer `d_X(C)` can only equal one and hence
returns an order-seven separator.  If no such component exists, every
component is `X`-full.  \(\square\)

## Corollary 2 (clique packing in the full-interface obstruction)

Assume additionally that `G` has no `K_7` minor, that every component of
`G-X` is adjacent to every vertex of `X`, and that `G-X` has `m`
components.  If `Q` is a clique in `G[X]`, then

\[
                         m+|Q|\le 6.                 \tag{2.1}
\]

### Proof

Since `G` has no `K_7` minor, `|Q|<=6`; otherwise `Q` itself contains a
`K_7` subgraph.  Thus `7-|Q|` is positive.

If `m+|Q|>=7`, choose `7-|Q|` distinct components
`C_1,...,C_{7-|Q|}` and the same number of distinct vertices
`x_1,...,x_{7-|Q|}` in `X-Q`.  The seven sets

\[
 C_i\cup\{x_i\}\quad(1\le i\le 7-|Q|),
 \qquad
 \{q\}\quad(q\in Q)
\]

are disjoint and connected.  They are pairwise adjacent: every component
contacts every boundary anchor, and the singleton sets from `Q` form a
clique.  They are therefore an explicit `K_7`-minor model, a contradiction.
This proves (2.1).  \(\square\)

Thus, for example, a triangle in an eight-vertex full interface permits at
most three open components, while a four-clique forces exactly two whenever
the separation is nontrivial.

## Application to the exact-seven first-entry branch

In the hard exact order-seven `(1,2)` branch, let `K` be a non-direct
first-entry component and write

\[
 T_K=N_G(K)\cap S,
 \qquad
 A_K=N_G(K)\cap(V(P_1)\cup V(P_2)).
\]

The audited first-entry theorem gives

\[
 N_G(K)=T_K\mathbin{\dot\cup}A_K,qquad
 |T_K|\le4,qquad |A_K|\ge3.
\]

Hence its literal separator excess is

\[
 \varepsilon(K)=|T_K|+|A_K|-7.
\]

Theorem 1 shows that any complementary component which misses one of
these literal separator vertices gives a strict host-level decrease of
`epsilon(K)`.  At the first positive value `epsilon(K)=1`, failure of
strict descent is not an unclassified bridge: it is an actual
eight-vertex separator all of whose open components are adjacent to every
boundary vertex.  Corollary 2 supplies the corresponding component/clique
restrictions.

## Exact trust boundary

The descent preserves the literal host graph and the connected side, but
it need not preserve the old seven boundary labels.  In the first-entry
application the new boundary is a subset of

\[
                 T_K\mathbin{\dot\cup}A_K;
\]

it can therefore cut through either named boundary-full connected
subgraph.  Nor does an order-seven full-neighbourhood separation by itself
align the equality partitions returned by contractions on its two shores.

Accordingly, the precise remaining mechanism is **label-preserving
descent through a nested full-neighbourhood separation**.  Either the
named connected subgraphs must survive on the new sides with their seven
contacts, or proper-minor colouring data must synchronize the new
boundary.  When `epsilon=1`, the only alternative to such a strict descent
is the boundary-full order-eight interface stated in Theorem 1.  Geometry
of the separator order alone cannot distinguish its two shore colourings.
