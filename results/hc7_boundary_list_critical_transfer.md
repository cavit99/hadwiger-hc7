# Boundary list-criticality and transfer to a complementary component

**Status:** written proof; separate internal audit GREEN in
[`hc7_boundary_list_critical_transfer_audit.md`](hc7_boundary_list_critical_transfer_audit.md).

This note studies the exact asymmetric order-eight interface by fixing one
boundary colouring which extends through one shore and fails on the other.
It extracts a genuine list-critical subgraph, records both its fixed-trace
Kempe constraints and the independent constraints supplied by contraction
criticality, and proves a strict transfer to a complementary connected
subgraph when the list-critical subgraph is proper.  The returned connected
subgraph has smaller order, but the theorem does not by itself define an
iteration: the new boundary need not have order eight or preserve the
inherited minor-model labels.
Nothing here proves `HC_7`.

## 1. Exact asymmetric interface

Let `G` be a graph such that

\[
 \chi(G)=7,
 \qquad \kappa(G)\ge 7,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                               \tag{1.1}
\]

Let

\[
                         V(G)=A\mathbin{\dot\cup}X
                                  \mathbin{\dot\cup}D              \tag{1.2}
\]

where `A,D` are nonempty and connected, `|X|=8`, and there is a vertex
`p in X` such that

\[
                         N_G(A)=X-\{p\},
 \qquad                   N_G(D)=X.                                \tag{1.3}
\]

Thus `A,D` are the two open shores of the separation with boundary `X`;
the first shore already has the exact order-seven boundary `X-{p}`.

Let `c` be a proper six-colouring of `G[A union X]`.  Assume that its
restriction to `X` does not extend to a proper six-colouring of
`G[D union X]`.  For `u in D`, put

\[
 L_c(u)=[6]-c(N_G(u)\cap X),                              \tag{1.4}
\]

where the expression after the minus sign is the set of distinct colours,
not a multiset.

The fixed boundary trace extends through `D` exactly when `G[D]` is
`L_c`-colourable.  Hence `G[D]` is not `L_c`-colourable.

## 2. The list-critical subgraph

### Theorem 2.1 (fixed-trace critical subgraph)

There is a connected induced subgraph `K` of `G[D]`, minimal by vertex
inclusion subject to not being `L_c`-colourable.  There is also a spanning
subgraph `F` of `K`, minimal by edge inclusion subject to not being
`L_c`-colourable.  They have the following properties.

1. Every proper induced subgraph of `K`, and every proper subgraph of `F`,
   is `L_c`-colourable.
2. For every `u in V(K)`,

   \[
                           d_K(u)\ge |L_c(u)|.             \tag{2.1}
   \]

3. Put

   \[
   \begin{aligned}
      f(u)&=|c(N_G(u)\cap X)|,\\
      \varepsilon(u)&=d_K(u)-|L_c(u)|,\\
      \rho(u)&=|N_G(u)\cap X|-f(u),\\
      \sigma(u)&=|N_G(u)\cap(D-V(K))|.
   \end{aligned}                                          \tag{2.2}
   \]

   Then the exact degree identity is

   \[
                    d_G(u)=6+\varepsilon(u)+\rho(u)+\sigma(u).
                                                               \tag{2.3}
   \]

4. The subgraph induced by the tight vertices

   \[
                     T=\{u:d_K(u)=|L_c(u)|\}              \tag{2.4}
   \]

   is a Gallai forest: each of its blocks is a complete graph or an odd
   cycle.

#### Proof

Choose an induced non-`L_c`-colourable subgraph with a minimum vertex set.
It is connected, since otherwise one of its components is a smaller
uncolourable induced subgraph.  This is `K`.  Now delete edges from `K`
as long as non-`L_c`-colourability is preserved, obtaining `F`.  A proper
vertex subgraph of `F` is contained in a proper induced subgraph of `K`;
an edge deletion contradicts the choice of `F`.  This proves assertion 1.

Colour `K-u` from its lists.  If `d_K(u)<|L_c(u)|`, some colour in `L_c(u)`
is absent from the coloured neighbours of `u`, so the colouring extends to
`u`, a contradiction.  This proves (2.1).

There are no edges from `D` to `A`.  Since `K` is induced,

\[
\begin{aligned}
 d_G(u)
   &=d_K(u)+|N_G(u)\cap(D-V(K))|+|N_G(u)\cap X|\\
   &=(6-f(u)+\varepsilon(u))+\sigma(u)+(f(u)+\rho(u)),
\end{aligned}
\]

which is (2.3).

It remains to prove assertion 4.  Let `B` be a block of `K[T]`.  Colour
`K-V(B)` from its lists, taking the empty colouring if `B=K`.  Delete from
the list of each `u in B` the colours used on its already coloured
neighbours outside `B`.  At most `d_K(u)-d_B(u)` colours are deleted, and
`u` is tight, so its residual list has order at least

\[
             |L_c(u)|-(d_K(u)-d_B(u))=d_B(u).            \tag{2.5}
\]

The degree-choosability theorem colours `B` from these residual lists
unless `B` is complete or an odd cycle.  Such a colouring would extend the
colouring of `K-V(B)` and contradict the choice of `K`.  Every block is
therefore complete or an odd cycle. \(\square\)

The quantities in (2.3) separate three genuinely different sources of
degree: internal list-degree excess, repetition of a boundary colour on
literal boundary neighbours, and neighbours in the rest of the original
shore.  In particular, the palette information alone does not identify
which literal boundary vertices, or which inherited minor-model branch
sets, supply the repeated contacts.

## 3. Fixed-trace Kempe constraints

### Theorem 3.1 (locked edge in an edge-minimal critical subgraph)

Let `uv` be an edge of `F`, and let `phi` be an `L_c`-colouring of
`F-uv`.  Then

\[
                             \phi(u)=\phi(v)=\alpha       \tag{3.1}
\]

for some colour `alpha`.  For every `beta ne alpha`, exactly one of the
following component alternatives holds in the properly coloured graph
formed from `F-uv`, `G[X]`, and all `K`--`X` edges.

1. The `alpha`--`beta` component containing `u` also contains `v`, and
   hence contains a literal `u`--`v` path.
2. The two components containing `u,v` are distinct and both meet `X`.
   Consequently there are vertex-disjoint first-hit paths from `u,v` to
   two distinct literal vertices of `X`, respectively, with internal
   vertices in `K`.

In particular, in this fixed-trace colouring each of `u,v` has a neighbour
of every colour other than `alpha`, either in `K` or at the literal
boundary.

#### Proof

If the endpoints of `uv` had different colours, `phi` would colour `F`,
contrary to its choice.  Thus (3.1) holds.  Adjoin the fixed colouring `c`
of `X`.  The list definition makes the resulting colouring proper on the
displayed graph.

Fix `beta ne alpha`.  If the two endpoint components coincide, outcome 1
holds.  Otherwise suppose, for example, that the component containing `u`
does not meet `X`.  Interchange `alpha,beta` on that component.  The
boundary trace is unchanged, and the ends of `uv` now have different
colours.  Restoring `uv` gives an `L_c`-colouring of `F`, a contradiction.
Thus both components meet `X`.  Shortest paths to their first boundary
vertices have internal vertices in `K`; they are disjoint and have
distinct ends because the two components are disjoint.  The final
assertion follows from the path in either alternative. \(\square\)

This theorem gives actual paths in `G`, but the colouring `phi` need not
colour the edges of `G[K]-F`, nor any vertex of `D-K`.  It is a local
fixed-trace statement, not a colouring of a proper minor of `G`.

## 4. The separate whole-host constraint

### Theorem 4.1 (contraction-colouring saturation)

For every edge `uv` of `G`, a six-colouring of `G/uv` expands to a proper
six-colouring `psi` of `G-uv` with

\[
                             \psi(u)=\psi(v)=\lambda.    \tag{4.1}
\]

For each colour `mu ne lambda`, the `lambda`--`mu` subgraph of `G-uv`
contains a `u`--`v` path.

#### Proof

The contraction is a proper minor and hence is six-colourable.  Expanding
its contraction vertex gives (4.1).  If the two endpoints lay in distinct
`lambda`--`mu` components, interchange the two colours on the component
containing `u`.  The endpoints would then have different colours, so the
edge `uv` could be restored and `G` would be six-coloured.  This contradicts
`chi(G)=7`. \(\square\)

The boundary trace of `psi` is not asserted to be `c`.  Thus Theorems 3.1
and 4.1 are two different saturation statements: one preserves the fixed
boundary trace on an edge-minimal list obstruction but need not colour the
host, while the other colours the whole proper minor but may change the
boundary trace.  Identifying these two families is precisely a missing
state-transfer theorem; it cannot be assumed.

## 5. Transfer when the critical subgraph is proper

### Theorem 5.1 (strict rejected-trace transfer)

If `K` is a proper subgraph of `G[D]`, let

\[
                         R_1,\ldots,R_m                 \tag{5.1}
\]

be the components of `G[D-V(K)]`.  Then:

1. `N_G(R_i) subseteq X union V(K)` and `|N_G(R_i)|>=7` for every `i`.
2. A six-colouring `t` of the proper minor `G-(D-V(K))` extends through
   `A`, `X`, and `K`.  For at least one component `R_i`, the restriction of
   `t` to `N_G(R_i)` does not extend through `R_i`.
3. Such an `R_i` is a strict connected obstruction: `|R_i|<|D|`.  If
   `|N_G(R_i)|=7`, its full neighbourhood is an actual order-seven
   separator.  Moreover, every component of `G-N_G(R_i)` is adjacent to
   every literal vertex of this separator.

#### Proof

Different components in (5.1) are anticomplete.  Since `D` is a component
of `G-X` and `K` is induced, their neighbours lie in `X union V(K)`.
Their full neighbourhoods separate them from the nonempty set `A`, so
seven-connectivity gives the lower bound in assertion 1.

Because `D-V(K)` is nonempty, deleting it gives a proper minor.  Let `t`
be a six-colouring of the remaining graph.  Suppose its boundary
restriction extended through every `R_i`.  Choose one such extension for
each component.  The components are pairwise anticomplete and all the
extensions agree with `t` on their literal neighbourhoods, so they glue
to `t` and six-colour all of `G`.  This is impossible.  Hence some `R_i`
rejects the displayed trace.

The selected component is disjoint from the nonempty `K`, so it has fewer
vertices than `D`.  If its neighbourhood has order seven, it is the full
boundary of a nontrivial separation.  If a component behind that boundary
missed one boundary vertex, its own full neighbourhood would have order at
most six and would separate it from another component, contradicting
seven-connectivity.  This proves assertion 3. \(\square\)

The theorem gives a strict host-level transfer, but it changes the boundary
from `X` to the literal set `N_G(R_i)`, whose order may exceed eight.  It
does not by itself preserve the original five branch-set labels or the
equality partition on `X`.  Therefore Theorem 5.1 must not be iterated as
an order-eight induction without an additional boundary-control theorem.

## 6. The shore-filling endpoint

### Theorem 6.1 (synchronized vertex-deletion colourings)

If `K=D`, then for every `u in D` there is a proper six-colouring of `G-u`
which agrees with the same fixed colouring `c` on `A union X`.  In every
such colouring the neighbours of `u` contain all six colours.

If, in addition, there is no actual order-seven separation in `G`, then

\[
                        \varepsilon(u)+\rho(u)\ge2       \tag{6.1}
\]

for every `u in D`.  Consequently every tight vertex of `D` has at least
two repeated boundary-colour incidences.

#### Proof

By vertex-minimality, `D-u` has an `L_c`-colouring.  Glue it to `c` on
`A union X`.  This is a proper six-colouring of `G-u` with the required
fixed trace.  If a colour were absent from `N_G(u)`, assign that colour to
`u` and obtain a six-colouring of `G`.  Thus all six colours occur in its
neighbourhood.

When `K=D`, the term `sigma` in (2.3) is zero.  Seven-connectivity gives
`d_G(u)>=7`.  If equality held, `N_G(u)` would be an actual order-seven
separator separating `u` from the nonempty set `A`, since there are no
`A`--`D` edges.  Under the displayed extra hypothesis, `d_G(u)>=8`.
Equation (2.3) now gives (6.1). \(\square\)

This is the strongest fixed-trace conclusion supplied by list-criticality:
all vertex-deletion witnesses inside the shore may be synchronized on the
same literal order-eight boundary.  It still assigns colours rather than
the labels of the inherited `K_6`-minor branch sets.

## 7. Rural sharpness check and exact remaining barrier

The rural graph in
[`../barriers/hc7_near_k7_palette_rural_counterarchitecture.md`](../barriers/hc7_near_k7_palette_rural_counterarchitecture.md)
is `K_2` joined to a planar frequency-two icosahedral triangulation.  It is
seven-connected and `K_7`-minor-free, but it is six-colourable.  Its
displayed global six-colouring restricts to a boundary trace which extends
through both closed shores of its order-eight interface.  For that trace,
the colouring on the opposite shore is itself an `L_c`-colouring, so no
critical subgraph `K` exists.  The example therefore exits at the common-
trace alternative and does not refute any theorem above.

The same example verifies the sharp limitation: endpoint saturation and a
distinct-colour transversal of five fixed branch sets do not align palette
colours with branch-set labels.  In the present theorem this mismatch
appears exactly between Sections 3 and 4.  A completion of the asymmetric
interface needs one further host-level statement that does at least one of
the following:

1. aligns a fixed-trace locked edge of `F` with a contraction colouring of
   the same edge while preserving the named branch sets;
2. converts the rejected trace on `N_G(R_i)` into a compatible order-seven
   boundary colouring rather than merely an order-seven separator; or
3. uses universal rejection of all traces extending through `A` to turn
   the synchronized endpoint in Theorem 6.1 into a labelled split of the
   inherited minor model (or a coherent two-apex terminal).

None of these conclusions follows from boundary list-criticality alone.
