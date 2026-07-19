# Full-subgraph demand at an exact-seven critical-triangle transition

**Status:** written proof; separate internal audit GREEN in
[`hc7_exact7_critical_triangle_full_subgraph_demand_audit.md`](hc7_exact7_critical_triangle_full_subgraph_demand_audit.md).

This note treats the exact order-seven separator returned by a Kempe
transition between the two response families of two incident critical
edges whose outer ends are adjacent.  The two response colourings agree
literally on the separator, but each fails on one of the two crossing
edges.  Exact reflection by boundary-full connected subgraphs nevertheless
closes the case whenever the
common boundary partition has demand at most the full-subgraph packing
number of the opposite open side.  In every remaining case the boundary
partition has one of two explicitly described forms.

The result is unbounded in the orders of the two open sides.  It does not
eliminate the residual low-demand-capacity configurations and does not
prove `HC_7`.

## 1. Setup

Let `G` satisfy

\[
 \chi(G)=7,\qquad \kappa(G)\ge7,\qquad
 K_7\npreccurlyeq G,
 \qquad\text{and every proper minor of }G\text{ is six-colourable}.
                                                               \tag{1.1}
\]

Let

\[
                         e=va,\qquad f=vb                 \tag{1.2}
\]

be distinct incident edges with

\[
                              ab\in E(G),                \tag{1.3}
\]

and put `H=G-{e,f}`.  Suppose the critical-triangle transition theorem
supplies proper six-colourings `phi,psi` of `H` and a connected component
`D` of one two-colour subgraph such that, after naming the two colours
`alpha,beta`,

\[
        \phi(v)=\phi(a)=\alpha,\qquad \phi(b)=\beta,     \tag{1.4}
\]

and `psi` is obtained from `phi` by interchanging `alpha,beta` on `D`.
The transition theorem gives exactly one of the following placements.

1. **Centre placement:**

   \[
       v\in D,\qquad a,b\notin D.                       \tag{1.5}
   \]

   Neither `a` nor `b` belongs to `D`; the `alpha`-coloured side of `D`
   has a neighbour of every colour outside `{alpha,beta}`.
2. **Outer-edge placement:**

   \[
       a,b\in D,\qquad v\notin D.                       \tag{1.6}
   \]

   Each of the two colour sides of `D` has a neighbour of every colour
   outside `{alpha,beta}`.

In the centre placement, every member of `N_G(D)-{a,b}` has a colour
outside `{alpha,beta}`.  In the outer-edge placement, every member of
`N_G(D)-{v}` has a colour outside `{alpha,beta}`.  These are precisely the
placement and saturation conclusions of the audited
[critical-triangle transition theorem](../results/hc7_joint_persistent_incident_colour_fork.md),
Theorem 3.1.

Assume that `D` is not dominating and that

\[
                              S=N_G(D),\qquad |S|=7.     \tag{1.7}
\]

Put

\[
 C=G[D\cup S],\qquad
 O=G-D,\qquad
 R=V(G)-(D\cup S),\qquad
 F=G[S].                                                \tag{1.8}
\]

Thus `R` is the nonempty opposite open side and `(C,O)` is an actual
order-seven separation.

A connected subgraph disjoint from `S` is **`S`-full** when it has a
neighbour at every literal vertex of `S`.  Let `nu_D` be the maximum
number of pairwise vertex-disjoint `S`-full connected subgraphs contained
in `G[D]`, and define `nu_R` analogously in `G[R]`.

For a proper equality partition `Pi` of the literal seven-set `S`, put

\[
 \operatorname{sing}(\Pi)
   =\{s\in S:\{s\}\in\Pi\},
 \qquad
 d_F(\Pi)
   =|\Pi|-\omega\bigl(F[\operatorname{sing}(\Pi)]\bigr). \tag{1.9}
\]

This is the exact full-subgraph demand: each block other than a maximum clique of
singleton blocks needs one disjoint `S`-full connected subgraph in the
shore on which the connected-subgraph contractions are performed.

## 2. The exact transition obstruction

### Theorem 2.1

Let `Pi` be the equality partition of `S` induced by `phi` (equivalently,
by `psi`).  Then all of the following hold.

1. Both `e` and `f` cross the separation `(C,O)`.  The restrictions
   `phi|O` and `psi|O` coincide literally and properly colour the original
   closed shore `O`, inducing `Pi`.  On `C`, the first colouring fails
   only on `e` and the second fails only on `f`.
2. Every component of `G-S` is `S`-full, and

   \[
                 (\nu_D,\nu_R)\in\{(1,1),(1,2),(2,1)\}. \tag{2.1}
   \]

   In particular, the open side whose packing number is one is connected.
3. One has the strict demand inequality

   \[
                              d_F(\Pi)>\nu_R.            \tag{2.2}
   \]

   Before invoking `K_7`-minor exclusion and the assumption
   `chi(G)=7`, the reverse inequality produces either an explicit
   `K_7`-minor model or proper colourings of both original closed shores
   with the same exact boundary partition `Pi`.
4. In the centre placement (1.5), there is an independent two-set
   `I\subseteq S-{a,b}` such that

   \[
             \Pi=I\mid\{q\}\ (q\in Q),
             \qquad Q=S-I,qquad |Q|=5,                 \tag{2.3}
   \]

   and `a,b\in Q` with `ab\in E(F)`.  Consequently

   \[
                  d_F(\Pi)=6-\omega(F[Q]).              \tag{2.4}
   \]

   If `nu_R=2`, then `F[Q]` is `K_4`-free.  If `nu_R=1`, then `F[Q]`
   is `K_5`-free.
5. In the outer-edge placement (1.6), the colour `beta` is absent from
   `S`, the vertex `v` is the unique boundary vertex of colour `alpha`,
   and the remaining six boundary vertices use all four other colours.
   Thus `Pi` has five blocks, and the four blocks on `S-{v}` have sizes

   \[
                       (3,1,1,1)\quad\text{or}\quad(2,2,1,1). \tag{2.5}
   \]

   If `Q=sing(Pi)`, then `|Q|=4` in the first case and `|Q|=3` in the
   second, and

   \[
                  d_F(\Pi)=5-\omega(F[Q]).              \tag{2.6}
   \]

   If `nu_R=2`, then `F[Q]` is triangle-free.  If `nu_R=1`, then
   `F[Q]` is `K_4`-free.
6. Assume `nu_R=2`, and give `O` the common colouring `phi|O`.  If
   `x,y` are nonadjacent singleton blocks of `Pi`, then `O` contains an
   `x-y` path in their two colours, with all internal vertices in `R`,
   in either of the following two situations:

   - the centre placement holds and `F[Q-{x,y}]` is a triangle; or
   - the outer-edge placement has `|Q|=4` and the two vertices of
     `Q-{x,y}` are adjacent.

   Thus every singleton merge that would reduce the exact demand to two
   is replaced by a literal bichromatic connection through the opposite
   open side.

### Proof

#### Step 1: literal placement of the two deleted edges

In the centre placement, `v\in D` while `a,b\notin D`.  The edges
`va,vb` therefore put `a,b` in `N_G(D)=S`.  In the outer-edge placement,
`a,b\in D` while `v\notin D`, so either edge puts `v` in `S`.  Thus both
deleted edges run between `D` and `S` in either placement; neither is
internal to an open side or wholly contained in the boundary.

The Kempe interchange changes colours only on `D`.  Hence `phi` and `psi`
agree literally on `O=G-D`.  Both deleted edges have one endpoint in `D`,
so neither is an edge of the induced graph `O`; their common restriction
is a proper colouring of the original closed shore.  By definition of the
two response signatures, among the two restored edges `e,f`, the
colouring `phi` is improper exactly on `e`, while `psi` is improper
exactly on `f`.  Their restrictions to `C` therefore fail exactly as
asserted.  This proves item 1.

#### Step 2: packing at an actual seven-boundary

Let `K` be a component of `G-S`.  If it missed a boundary vertex `s`, then

\[
                         N_G(K)\subseteq S-\{s\}
\]

would separate `K` from another component of `G-S` using at most six
vertices.  There are at least two components, one in `D` and one in `R`.
This contradicts seven-connectivity.  Therefore every component is
`S`-full, and in particular `nu_D,nu_R>=1`.

The audited
[exact-seven boundary-full connected-subgraph packing theorem](../results/hc7_exact_seven_packet_packing.md),
Theorem 1, gives

\[
                 \nu_D+\nu_R\le4,qquad
                 \min\{\nu_D,\nu_R\}=1.                \tag{2.7}
\]

The audited
[adaptive `(1,3)` full-subgraph reflection theorem](../results/hc7_exact7_adaptive_packet_reflection.md),
Theorem 1.1, excludes the packing vector `(1,3)` in either orientation.
Together with (2.7), this leaves exactly the three vectors in (2.1).

If an open side of `G-S` had two components, both would be disjoint
`S`-full connected subgraphs.  A side with packing number one is therefore
connected.  This proves item 2.

#### Step 3: exact reflection of the common partition

Suppose that

\[
                              d_F(\Pi)\le\nu_R.          \tag{2.8}
\]

Choose `d_F(Pi)` pairwise disjoint `S`-full connected subgraphs in `R`.
Lemma 2.1 of the adaptive full-subgraph reflection theorem applies to the exact
partition `Pi`.  Its first outcome is an explicit `K_7`-minor model in
`G`.  In its second outcome, contractions supported in the closed shore
`G[R\cup S]` produce a proper minor whose six-colouring pulls back to a
proper colouring `eta` of the untouched original closed shore `C`, with
equality partition on the literal boundary exactly `Pi`.

Item 1 already gives the proper colouring `phi|O` of the other original
closed shore with the same exact partition.  Permute the six colour names
of `eta` so that the two colourings agree on every block of `Pi`, and glue
them across `S`.  This gives a proper six-colouring of `G`.

Under (1.1), both reflection outcomes are impossible.  Hence (2.8)
is false and (2.2) holds.  This also proves the more general terminal
statement in item 3.

#### Step 4: the centre-placement partition

Assume (1.5).  Equation (1.4) and the edge `ab` give distinct colours
`alpha,beta` at `a,b`.  The transition theorem says that every member of
`S-{a,b}` has a colour outside `{alpha,beta}`.  It also says that the
`alpha`-coloured side of `D` has a neighbour of each of the four remaining
colours.  Every neighbour of `D` outside `D` belongs to `S`; hence each of
those four colours occurs on `S-{a,b}`.

The five vertices of `S-{a,b}` therefore use all four remaining colours.
Exactly one colour occurs twice and each other colour once.  Let `I` be
the repeated colour class.  Properness makes `I` independent.  The other
five boundary vertices form the singleton set `Q=S-I`, and `a,b\in Q`
are adjacent.  This proves (2.3).

There are six blocks, and their singleton vertices are exactly `Q`, so
(1.9) gives (2.4).  If `nu_R=2`, (2.2) says

\[
                     6-\omega(F[Q])>2,
\]

whence `omega(F[Q])<=3`.  If `nu_R=1`, the same calculation gives
`omega(F[Q])<=4`.  These are precisely the two asserted clique
restrictions, proving item 4.

#### Step 5: the outer-edge-placement partition

Assume (1.6).  The boundary vertex `v` has colour `alpha`.  Every member
of `S-{v}` has a colour outside `{alpha,beta}`, so `v` is the unique
boundary vertex of colour `alpha` and `beta` is absent from `S`.  Both
colour sides of `D` have a neighbour of every one of the four remaining
colours.  Again all such neighbours outside `D` lie in `S`, so every one
of those four colours occurs on `S-{v}`.

Thus six vertices use four colours, all nonempty.  Their multiplicities
are `(3,1,1,1)` or `(2,2,1,1)`.  Adding the singleton block `{v}` gives
five blocks in total.  In the first case the singleton set `Q` consists
of `v` and the three singleton outside-colour blocks and has order four;
in the second it consists of `v` and the two singleton outside-colour
blocks and has order three.  Formula (1.9) now gives (2.6).

If `nu_R=2`, (2.2) gives `5-omega(F[Q])>2`, so
`omega(F[Q])<=2`.  If `nu_R=1`, it gives
`omega(F[Q])<=3`.  This proves the final clique restrictions.

#### Step 6: demand-critical singleton pairs

Assume `nu_R=2`, and let `x,y` satisfy one of the two conditions in item
6.  They are singleton blocks of `Pi` and `xy` is not an edge of `F`.
Apply the audited
[singleton-block Kempe exchange](../results/hc7_exact7_singleton_block_kempe_exchange.md)
to the proper colouring `phi|O`.

If its path outcome occurs, no other boundary vertex has either of the
two colours, so every internal vertex of the resulting `x-y` path lies in
`O-S=R`, as required.

Otherwise a Kempe interchange gives a proper colouring of `O` whose
boundary partition `Pi'` is obtained by replacing the singleton blocks
`{x},{y}` with the single independent block `{x,y}`.  In the centre
placement, `Pi'` has five blocks and its three remaining singleton
vertices induce a triangle.  Hence

\[
                          d_F(\Pi')=5-3=2.              \tag{2.9}
\]

In the stated outer-edge subcase, `Pi'` has four blocks and its two
remaining singleton vertices are adjacent.  Hence

\[
                          d_F(\Pi')=4-2=2.              \tag{2.10}
\]

In either case, exact reflection using the two disjoint `S`-full
connected subgraphs in `R` produces an explicit `K_7`-minor model or a
proper colouring of `C` inducing exactly `Pi'`.  The latter glues to the
new colouring of `O` and six-colours `G`.  Both conclusions contradict
(1.1).  The merge outcome is therefore impossible, so the required path
outcome must occur.  This proves item 6 and completes the proof.
\(\square\)

## 3. Exact trust boundary

1. The theorem applies only to a **single Kempe transition** between the
   two critical-triangle response families.  It does not treat the branch
   in which those families lie in different Kempe components.
2. The transition component must be nondominating and its full
   neighbourhood must have order exactly seven.  A larger boundary and
   the connected-dominating five-chromatic core remain separate cases.
3. The compatible-partition conclusion is complete when
   `d_F(Pi)<=nu_R`: both colourings are proper on the original closed
   shores and induce exactly the same literal boundary partition.  It is
   not merely agreement between two pinched edge-deletion responses.
4. The strict inequalities and clique restrictions in Theorem 2.1 are
   necessary residual conditions, not a proof that those residual
   boundary graphs are impossible.
5. The paths in item 6 need not avoid the two `S`-full connected
   subgraphs witnessing `nu_R=2`, and different required paths need not be
   mutually disjoint.  Converting those paths into a third
   label-preserving contraction support remains an additional problem.
6. No palette colour is identified with a branch-set label.  Any spanning
   labelled near-`K_7` model preserved in `H` remains available as
   independent geometric data, but full-subgraph reflection does not align its
   labels with the blocks of `Pi`.
