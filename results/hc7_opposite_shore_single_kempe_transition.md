# A single boundary Kempe transition between opposite-shore edge responses

**Status:** written proof; separate internal audit GREEN in
[`hc7_opposite_shore_single_kempe_transition_audit.md`](hc7_opposite_shore_single_kempe_transition_audit.md).

This note strengthens the elementary incompatibility of proper-minor
colouring responses on opposite sides of a separation.  If two such
responses differ by one Kempe interchange on the boundary, then that same
interchange is obstructed by a two-colour path in each open side.  At an
eight-vertex boundary in a seven-connected graph, each supporting component
is either adjacent to the whole boundary or has a full neighbourhood of
order seven.  Nothing here proves `HC_7`.

## 1. Boundary colourings and response edges

Let `q` be a positive integer, and let `G` be a graph which is not
`q`-colourable.  Suppose

\[
             V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D,          \tag{1.1}
\]

where `A,D` are nonempty and there is no edge between `A` and `D`.  Let

\[
                 e_A\in E(G[A]),\qquad e_D\in E(G[D]),              \tag{1.2}
\]

and suppose that `G-e_A` and `G-e_D` have proper `q`-colourings.  This is
automatic when every proper minor of `G` is `q`-colourable.

Fix a proper `q`-colouring `c_D` of `G-e_D` and a proper `q`-colouring
`c_A` of `G-e_A`.  Their restrictions to `G[A ∪ X]` and
`G[D ∪ X]`, respectively, are colourings of the two *unchanged* closed
sides.  Write

\[
                      gamma_D=c_D|X,\qquad gamma_A=c_A|X.            \tag{1.3}
\]

For a boundary colouring `gamma`, an `alpha`--`beta` **boundary Kempe
interchange** means interchanging `alpha,beta` on one connected component
of

\[
                     G[X][\gamma^{-1}(\{\alpha,\beta\})].           \tag{1.4}
\]

## 2. The simultaneous obstruction theorem

### Theorem 2.1

Assume, after a permutation of the colour names in `c_A` if necessary,
that `gamma_A` is obtained from `gamma_D` by one
`alpha`--`beta` boundary Kempe interchange on a component `K` of (1.4).
Then there are paths `P_A,P_D` with the following properties.

1. `P_A` uses only the colours `alpha,beta` in the colouring `c_D`, its
   internal vertices all belong to `A`, one end belongs to `K`, and its
   other end belongs to a different `alpha`--`beta` component of the
   boundary graph `G[X]` under `gamma_D`.
2. `P_D` uses only the colours `alpha,beta` in the colouring `c_A`, its
   internal vertices all belong to `D`, one end belongs to `K`, and its
   other end belongs to a different `alpha`--`beta` component of `G[X]`
   under `gamma_A`.

In particular, both paths have nonempty interiors.  Their interiors are
vertex-disjoint, although no disjointness of their boundary ends is
asserted.

#### Proof

Consider the full `alpha`--`beta` component `L_A` of
`G[A ∪ X]` under `c_D` which contains `K`.  Suppose first that

\[
                              L_A\cap X=K.                         \tag{2.1}
\]

Interchange `alpha,beta` on `L_A`.  This preserves properness on the
unchanged closed side `G[A ∪ X]` and changes its boundary colouring
from `gamma_D` to exactly `gamma_A`.  The restriction of `c_A` to
`G[D ∪ X]` is proper on the other unchanged closed side and already
has boundary colouring `gamma_A`.  The two colourings therefore glue to a
proper `q`-colouring of `G`, contrary to the hypothesis.  Hence (2.1) is
false.

The component `L_A` consequently meets another component of the boundary
two-colour graph.  Choose a shortest path in `L_A` from `K` to such a
component, stopping at its first boundary vertex outside `K`.  No internal
vertex of this path belongs to `X`, by the choice of its two ends.  Its
internal vertices therefore lie in `A`; this is `P_A`.

Now apply the same argument in the reverse direction.  Under `gamma_A`,
the set `K` is still one `alpha`--`beta` component of `G[X]`, with the two
colour names interchanged.  Let `L_D` be the full two-colour component in
`G[D ∪ X]` under `c_A` which contains `K`.  If `L_D ∩ X=K`,
interchanging on `L_D` produces the boundary colouring `gamma_D`, which
then glues to `c_D|G[A ∪ X]`.  This again contradicts the failure of a
`q`-colouring of `G`.  A shortest path from `K` to another boundary
component inside `L_D` gives `P_D` with all internal vertices in `D`.

Distinct two-colour components of `G[X]` have no edge between them in the
two-colour graph, so both paths have a nonempty interior.  Finally `A` and
`D` are disjoint, which makes the two interiors disjoint.  \(\square\)

### Corollary 2.2 (the order-eight consequence)

Assume in addition that `G` is seven-connected and `|X|=8`.  For each
`Z ∈ {A,D}`, let `Q_Z` be the component of `G-X` containing the internal
vertices of `P_Z`.  Then

\[
                  |N_G(Q_Z)|\in\{7,8\}.                            \tag{2.2}
\]

If the order is seven, `N_G(Q_Z)` is an actual order-seven separator.  If
the order is eight, then

\[
                           N_G(Q_Z)=X.                              \tag{2.3}
\]

Consequently, unless an actual order-seven separator occurs, the two
Kempe obstructions in Theorem 2.1 are supported by two distinct components
of `G-X`, each adjacent to every vertex of `X`.

#### Proof

The internal vertices of each path form a connected nonempty set in
`G-X`, so they lie in one component `Q_Z`.  Its neighbourhood is contained
in `X`.  The other open side in (1.1) is nonempty, so this neighbourhood
separates `Q_Z` from another vertex of `G`.  Seven-connectivity gives
`|N_G(Q_Z)|>=7`, while `|X|=8` gives the upper bound in (2.2).  Equality
eight is precisely (2.3).  The two components are distinct because one
lies in `A` and the other in `D`.  \(\square\)

## 3. Why deletion and contraction of one edge do not give this transition

The two response edges in Theorem 2.1 must be genuinely different.  In
fact the stronger statement below shows that deletion and contraction of
one critical edge have identical Kempe dynamics.

### Proposition 3.1 (critical-edge Kempe-graph identity)

Let `f=rs` be an edge of a non-`q`-colourable graph `G`, and suppose
`G-f` is `q`-colourable.  Lifting and identifying the ends of `f` gives a
bijection

\[
                       Col_q(G/f)\longleftrightarrow Col_q(G-f).    \tag{3.1}
\]

Moreover this bijection is an isomorphism of the two Kempe-reconfiguration
graphs: a swap of two colours on one full two-colour component corresponds
to the same swap after lifting or contraction.  Therefore, on every
labelled set disjoint from `r,s`, the two graphs have identical boundary
trace languages and identical trace transitions.

#### Proof

Every proper `q`-colouring of `G-f` gives `r,s` one common colour, say
`alpha`; otherwise restoring `f` would colour `G`.  This proves the
bijection (3.1).

Fix another colour `beta`.  The vertices `r,s` lie in the same
`alpha`--`beta` component of `G-f`.  Otherwise interchanging the two
colours on the component containing `r` would give the ends of `f`
different colours, again allowing `f` to be restored.  Contracting `r,s`
therefore contracts two vertices inside one two-colour component and does
not merge two distinct components.  Components for a pair of colours not
containing `alpha` are unchanged.  Thus full two-colour components, and
the interchanges on them, correspond in both directions.  This proves the
Kempe-graph assertion and its trace consequence.  \(\square\)

## 4. Exact scope

Theorem 2.1 does not assert that two opposite-shore response colourings can
be selected one boundary Kempe move apart.  Along a longer boundary Kempe
sequence there may be intermediate colourings extending through neither
closed side.  The theorem also does not assign the two paths to prescribed
branch sets of a minor model, make their boundary ends distinct, or produce
a common boundary partition.

At an asymmetric boundary `X=Y ∪ {p}` with `N_G(A)=Y`, the separator
`Y` already has order seven.  In that application, a bare order-seven
separator is not progress by itself: a useful continuation must retain the
named two-colour transition, produce compatible boundary colourings, or
strictly decrease a declared host-level parameter.

Proposition 3.1 rules out a tempting shortcut.  Comparing `G-f` and `G/f`
at the same internal edge cannot create a second response or a new trace
transition.  A dynamic continuation must compare distinct operations,
for example critical edges on opposite shores or a coupled double
contraction, and must still use the labelled branch-set geometry.

## 5. Dependencies

- [boundary incompatibility of proper-minor responses on opposite
  shores](hc_opposite_shore_minor_response_incompatibility.md), whose
  gluing mechanism is strengthened here from disjointness to a two-sided
  obstruction for one boundary Kempe interchange.
- No external theorem is used.
