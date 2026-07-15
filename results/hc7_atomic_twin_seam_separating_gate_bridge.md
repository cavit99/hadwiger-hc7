# Atomic twin-seam separating gate bridge

**Status:** proved and independently audited.

## 1. Setup

Use the twin seam and notation of
[the crossed-state theorem](hc7_atomic_twin_seam_crossed_states.md).  Put
`e=zu`, let `phi` be a six-colouring of `G/e` expanded to `G-e`, and write
`alpha=phi(z)=phi(u)`.

For an alternate colour `beta`, let `L_beta` be the `alpha-beta` component
of `G-e` containing `z,u`.  This component contains both ends: otherwise
swapping the component containing `z` makes `e` proper and six-colours
`G`.  Let

\[
                         f=dt,qquad d\in D, t\in Z,    \tag{1.1}
\]

be a bridge of `L_beta` which separates `z` from `u`.  Let `X` be the
vertex set of the `z`-component of `L_beta-f`.

Swap `alpha,beta` on `X`, obtaining `psi`.  The edge `e` is now proper,
while the ends of `f` have the same colour.  Thus `psi` is simultaneously
a six-colouring of `G-f` and, after identifying `d` with the literal gate
`t`, of `G/f`.

## 2. Simultaneous mismatch paths

### Theorem 2.1

Unless `G` is six-colourable, the same pair `(phi,f)` supplies both:

1. a literal `t`--`Omega_D` path `P_D` contained in
   `G[D union Omega_D]`, whose other endpoint lies in `Omega_D-{t}` and
   whose internal vertices lie in `D`; and
2. a literal `t`--`Omega_E` path `P_E` contained in
   `G[B_E union Omega_E]`, whose other endpoint lies in `Omega_E-{t}` and
   whose internal vertices lie in `B_E`.

Both paths are `alpha-beta` paths in the original lock `L_beta` and both
contain the edge `f`.

### Proof

Consider `Omega_D`.  The colouring `phi` is proper on the closed side
`D union Omega_D`, while `psi` is proper on the opposite closed side.
Put `U_D=X intersect Omega_D`.

Suppose every `alpha-beta` component of
`G[D union Omega_D]` has its boundary trace wholly inside `U_D` or wholly
outside it.  Starting from `phi`, swap precisely those components whose
boundary trace lies in `U_D`.  The resulting colouring agrees with `psi`
on `Omega_D`, because `psi` differs from `phi` there exactly on `U_D`.
Palette-aligned gluing with `psi` on the opposite closed side six-colours
`G`, a contradiction.

Hence one `alpha-beta` component on the `D`-closed side meets both `U_D`
and its complement in `Omega_D`.  Take a shortest path in that component
between the two boundary parts.  Its internal vertices avoid `Omega_D`.
It lies in the global component `L_beta`, begins in `X` and ends outside
`X`, so the bridge `f` lies on it.  Since `t` is a boundary vertex and
`f=dt`, shortestness forces `t` to be an endpoint.  This is `P_D`.

For `Omega_E`, use `phi` on the colour-intact closed side
`B_E union Omega_E` and `psi` on the opposite `E`-closed side.  With
`U_E=X intersect Omega_E`, the same component-swap argument produces a
shortest boundary-crossing `alpha-beta` path in the `phi`-side.  It too
lies in `L_beta`, crosses from `X` to its complement, contains `f`, and has
`t` as a boundary endpoint.  This is `P_E`.  \(\square\)

## 3. Exact scope

The two paths are coupled: they come from one colouring, one Kempe lock and
one named gate-edge contraction.  They need not be otherwise disjoint and
may overlap for their entire portions in `B_E`.

The theorem must use the two `phi`-intact sides.  The opposite `psi`-sides
exclude `d` and therefore cannot contain `f`.

Finally, a first or shortest lock excursion need not have a bridge entry;
a theta graph is the immediate obstruction.  The safe residual dichotomy is

\[
 f\text{ separates }z,u\text{ in }L_\beta
 \quad\text{or}\quad
 L_\beta-f\text{ contains a }z\text{--}u\text{ bypass}. \tag{3.1}
\]

The first branch now has the two literal paths above.  Turning them into
disjoint carriers or a rooted model, and resolving the bypass branch, are
the two tasks of the active double-lock exchange goal.
