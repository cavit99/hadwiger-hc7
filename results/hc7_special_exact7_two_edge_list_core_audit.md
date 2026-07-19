# Independent audit of the special exact-seven two-edge list-critical reduction

**Verdict:** GREEN for Lemma 2.1, Lemma 3.1, Theorem 3.2, and Corollary
4.1 in
[`hc7_special_exact7_two_edge_list_core.md`](hc7_special_exact7_two_edge_list_core.md)
at source SHA-256

```text
c59ce7f61df334635c3a8bda6b8528774b4687e06203786b747175dd61ca3e08
```

This is a separate internal mathematical audit, not external peer review.

## 1. Singleton/entrance-edge dichotomy

Each `z_i` has a neighbour in `A`.  Failure of a system of distinct
representatives for the two neighbourhoods forces

\[
                         N_A(z_1)=N_A(z_2)=\{a\}.
\]

Any component `C` of `A-a` then has neighbourhood contained in
`{a}\cup Y_0`, an order-six separator from the nonempty `B` shore.
Seven-connectivity therefore forces `A={a}`, whence `N_G(a)=Y` and
`d_G(a)=7`.

If `nu_B=2`, the adaptive `(1,2)` theorem and Dirac's inequality place
`G[Y]` among the Moser spindle `M` and `M+13`.  Connected `B` is excluded
by the audited one-anchor closure.  If `B` is disconnected, fullness and
`nu_B=2` give exactly two components.  The complete pure-Moser
two-component theorem excludes `M`.  For `M+13`, the contractions

\[
                       \{a,2,5\},\qquad B_j\cup\{4,6\},
\]

together with the triangle `013`, form a `K_5` and force the exact trace

\[
                         25\mid46\mid0\mid1\mid3
\]

on each untouched closed side.  Aligning those traces colours `G-a`, and
the sixth colour absent from the boundary extends to `a`.  Thus `nu_B=1`,
and fullness then makes `B` connected.  Otherwise Hall's theorem gives
distinct entrance vertices `a_1,a_2`.  The two alternatives are exclusive.

## 2. Three operation responses

Every six-colouring of `G-e_i` makes `e_i` monochromatic, since otherwise
restoring it colours `G`.  The other edge remains proper, giving the two
exclusive signatures.  Simultaneously contracting the vertex-disjoint
edges gives the equal/equal signature after expansion.  A proper/proper
colouring would colour `G`, so it is impossible.

Every returned boundary partition is legal on `G[B\cup Y]` because both
deleted edges lie on the `A` side.  If it extended to the intact
`G[A\cup Y]` shore, equality-block alignment and gluing would six-colour
`G`.  Applying the generic exact-packet and transported-partition
reflection theorems with the shores oriented from `B` to `A` proves demand
strictly greater than `nu_B`.  For every allowed mixed support family, a
saturating matching would give the same forbidden reflection; Hall's
theorem therefore supplies the stated deficient block family.  This
argument genuinely covers the double-equality response and does not treat
it as one of the selected one-edge responses.

## 3. List-critical core

The application of the audited two-edge list-critical theorem is exact
under

\[
 L=B,\qquad S=Y,\qquad R=A,
 \qquad (x,p,y,q_0)=(z_1,a_1,z_2,a_2).
\]

The edges are vertex-disjoint, and the expanded double-contraction
colouring and boundary lists coincide literally.  Hence the minimal induced
non-list-colourable core `K` is connected, contains at least one marked
vertex, satisfies

\[
                             d_K(v)\ge |\mathcal L(v)|,
\]

and its full neighbourhood `T` is an actual separation boundary with
`|T|\ge7`.  The three failed-edge placements are exhaustive.  A proper
`K\subsetneq A` gives the strict decrease `|K|<|A|`, but not a recursive
copy of the original exact-seven configuration.

## 4. Shore-filling case

When `K=A`, both marked vertices lie in `K`.  Writing `c_Y(v)` for the
number of boundary-neighbour colours,

\[
 \rho(v)=|N_G(v)\cap Y|-c_Y(v),\qquad
 \varepsilon(v)=d_{G[A]}(v)-|\mathcal L(v)|,
\]

gives

\[
                     d_G(v)=6+\varepsilon(v)+\rho(v).
\]

Nonnegativity and seven-connectivity turn
`\varepsilon(v)+\rho(v)\le2` into an actual singleton-side separator of
order seven or eight.  If `\varepsilon` vanishes everywhere, the audited
degree-choosability argument makes every block of `G[A]` a clique or an odd
cycle.

## 5. Trust boundary

The result does not bound the returned separator by seven, repair an
opposite-side or boundary failed edge, preserve either one-edge partition,
align the double-equality partition with them, construct a `K_7`-minor
model, or force low excess in the shore-filling core.  It therefore does
not close the special exact-seven interface or prove `HC_7`.

The exact dependencies checked are the special five-plus-two response, the
adaptive `(1,2)` residual, the singleton-thin `M/M+13` extraction, the
pure-Moser two-component closure, the direct `M+13` two-anchor construction
(reproved in the source), exact packet reflection, transported-partition
Hall reflection, and the audited two-edge list-critical descent.  The
two-edge deletion-lattice barrier is used only for the stated limitation.
