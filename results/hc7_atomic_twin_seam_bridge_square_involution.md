# Twin-seam bridge-square involution

**Status:** proved and independently audited.

This theorem identifies the exact algebra of the response-matched swaps in
the separating branch of the atomic twin seam.  It proves that the reverse
bridge response is an involution, not a descent mechanism.

## Theorem 1 (complementary bridge swaps)

Let `e=zu` and `f=dt` be vertex-disjoint edges of a graph `G`.  Let `phi`
be a proper colouring of `G-e` with

\[
                         \phi(z)=\phi(u)=\alpha.
\]

For `beta ne alpha`, let `L` be the `alpha,beta` component of `G-e`
containing `z,u`.  Suppose `f` is a bridge of `L` separating `z` from
`u`.  Write

\[
                 L-f=X\mathbin{\dot\cup}Y,
                 \qquad z\in X,\quad u\in Y.          \tag{1.1}
\]

For a set `W` of `alpha,beta` vertices, let `phi^W` denote the colouring
obtained by interchanging `alpha,beta` on `W`.  Then:

1. `phi^X` and `phi^Y` are proper colourings of `G-f`; the ends of `f`
   have equal colours, so both descend to `G/f`.
2. `phi` and `phi^L` are proper colourings of `G-e`; both descend to
   `G/e`.
3. In either `G-f` colouring, the `alpha,beta` component containing the
   four named vertices is exactly `(L-f)+e`, and `e` is a bridge with
   sides `X,Y`.
4. The four legal swaps form the involutive square

   \[
   \begin{array}{ccc}
       \phi & \longleftrightarrow & \phi^X\\
       \updownarrow && \updownarrow\\
       \phi^Y & \longleftrightarrow & \phi^L.
   \end{array}                                        \tag{1.2}
   \]

### Proof

The edge `f` is the only `alpha,beta` edge between `X` and `Y` in `G-e`.
Swapping either side makes the ends of `f` equal and changes exactly one
of `z,u`, making `e` proper.  No other edge becomes monochromatic: an
`alpha,beta` edge leaving a side would contradict either the definition of
the component or the fact that `f` is its bridge.  This proves item 1.

Swapping all of `L` is an ordinary Kempe exchange in `G-e`; both ends of
`e` are swapped and remain equal.  This proves item 2.

All four colourings have the same set of `alpha,beta` vertices.  Passing
from `G-e` to `G-f` deletes the sole edge `f` between `X,Y` and restores
`e`, whose ends lie one in each side.  Hence `(L-f)+e` is the entire
named component and `e` is its bridge, proving item 3.

Finally, symmetric difference of the swap sets gives

\[
  (\phi^X)^X=\phi,
  \quad (\phi^X)^Y=\phi^L,
  \quad (\phi^Y)^Y=\phi,
  \quad (\phi^Y)^X=\phi^L.
\]

These identities are exactly (1.2), and every move is its own inverse.
\(\square\)

## Corollary 2 (the counterexample-derived twin square is fully crossed)

In the frozen atomic twin seam, let `Pi_Omega(c)` be the exact partition
induced by a response `c` on either `Omega_D` or `Omega_E`.  Then for every

\[
 a\in\{\phi,\phi^L\},\qquad
 b\in\{\phi^X,\phi^Y\},
\]

one has

\[
                         \Pi_\Omega(a)\ne\Pi_\Omega(b). \tag{2.1}
\]

### Proof

Both members of the first family descend to `G/e`; both members of the
second descend to `G/f`.  The audited twin-seam crossed-state theorem
quantifies over every response to either operation.  Apply it to both
`G/e` colourings and both `G/f` colourings on each twin boundary.  This
gives all eight inequalities in (2.1).  \(\square\)

## Consequence for the active decoder

The reverse `e`-lock in the separating branch is not an independent
response and cannot orient a strict scalar rank: every legal side swap is
reversible, while every cross-operation comparison in the whole square
remains mismatched.  A successful decoder must therefore use information
external to the square, such as an internal-edge response, a literal duty,
a labelled row split, or an actual globally ranked `(1,2)` receiver.
