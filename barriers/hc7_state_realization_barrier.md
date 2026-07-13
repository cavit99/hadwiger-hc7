# Complementary boundary states: a uniform realization barrier

## 1. Statement

Fix an integer `k>=3`, a finite labelled boundary set `X`, and a graph
`F` on `X`.  Let `Omega_k(F)` be the equality partitions of `X`
induced by proper labelled `k`-colourings of `F`.  Suppose

\[
                 \Omega_k(F)=\mathcal A\mathbin{\dot\cup}\mathcal B
                                                               \tag{1.1}
\]

is a partition into two nonempty families.

### Theorem 1.1 (complementary-state realization barrier)

There are finite `X`-boundaried graphs `R_A,R_B` whose exact boundary
extension relations are `A,B`, respectively.  Consequently their open
interiors may be taken disjoint and glued along `X` to give a graph
which is not `k`-colourable.

Moreover the following two strengthenings are available, separately.

1. **Full connected realization.**  Each open interior can be made
   connected and collectively adjacent to every vertex of `X`, without
   changing its extension relation.
2. **Internal one-step criticality.**  The realizers can be chosen so
   that deletion of any open-side vertex, or deletion or contraction of
   any edge with both ends in one open side, makes the glued graph
   `k`-colourable.

The first strengthening can in fact be amplified: for every
`m<=|X|`, the two full connected realizers can be glued to form an
`m`-connected non-`k`-colourable graph while preserving both exact
extension relations.

If, in addition, each of `A,B` contains a state equating `x,y` for every
nonedge `xy` of `F`, the boundary in every realizer may be required to
induce exactly `F`.

The theorem does **not** assert that full connectedness and internal
one-step criticality occur simultaneously, nor that the glued graph is
highly connected or excludes any prescribed clique minor.

## 2. Exact realization

For `C in {A,B}`, let `\widehat C` be the set of labelled `k`-colourings
of `X` whose equality partition belongs to `C`.  It is invariant under
simultaneous permutation of the `k` colours.  The finite colouring-
relation realization theorem of Dvorak--Swart (Theorem 3 of *A note on
extendable sets of colorings and rooted minors*, arXiv:2504.07764)
therefore supplies an `X`-boundaried graph whose exact extension
relation is `\widehat C`.

Add all edges of `F` on `X`.  Every intended colouring is proper on
`F`, so the exact relation is unchanged.  Under the additional
equatability hypothesis, the resulting boundary is induced: if a
realizer contained an edge at a nonedge `xy` of `F`, it could not admit
the promised state equating `x,y`.

Since `A cap B` is empty, a colouring of the two realizers glued along
`X` would induce a boundary state accepted by both.  Hence the glued
graph is not `k`-colourable.

## 3. Making each open side connected and full

Starting from either realizer, add a new open vertex `c`.  For every
`x in X`, add a fresh vertex `l_x` and the path

\[
                              x-l_x-c.               \tag{3.1}
\]

For every component `Q` of the old open interior choose `u_Q in Q`, add
a fresh vertex `m_Q`, and add the path

\[
                              c-m_Q-u_Q.              \tag{3.2}
\]

Every old colouring extends over (3.1)--(3.2): after choosing a colour
for `c`, each new middle vertex must avoid at most two colours, and
`k>=3`.  Conversely every colouring of the augmented graph restricts
to one of the old realizer.  Thus the exact relation is unchanged, the
open interior is connected, and its neighbourhood is all of `X`.

Doing this independently on the two sides proves strengthening 1.

### Theorem 3.1 (connectivity amplification)

Let the two connected full open interiors just constructed be disjoint
and glued along `X`.  Fix `m<=|X|`.  Replace every open-side vertex `u`
by an independent false-twin class `T_u` of order `m`; replace every old
open edge `uv` by all edges between `T_u,T_v`, and every old boundary
edge `xu` by all edges from `x` to `T_u`.  Keep `X` unchanged.

The resulting glued graph is `m`-connected and the two exact boundary
extension relations are unchanged.

#### Proof

An old colouring extends by colouring each class `T_u` uniformly.
Conversely, selecting one representative of every class from a colouring
of the amplified graph recovers a colouring of the old side.  Thus both
relations are preserved.

Delete fewer than `m` vertices.  Every twin class still has a survivor,
so each amplified open side remains connected because its old quotient
was connected.  At least one boundary vertex remains because
`m<=|X|`.  Every remaining boundary vertex still has a neighbour class
on each side by old fullness, and that class has a survivor.  Hence the
two sides and all remaining boundary vertices lie in one component.  No
set of fewer than `m` vertices disconnects the graph.  QED.

The boundary `X` itself remains a cut, so the amplification is sharp at
the adhesion order.  It introduces redundant twins and makes no
minor-exclusion claim.

## 4. Internal one-step criticality

Instead return to any finite exact realizer before the harmless
connectivity augmentation.  Repeatedly delete an open-side vertex or an
edge with both ends in the open side whenever that deletion leaves the
same exact extension relation.  Choose a deletion-minimal realizer
`M_C` for each `C in {A,B}`.

Deleting an internal object cannot destroy a boundary extension.
Minimality therefore says that every such deletion creates a new state.
For `M_A` the new state lies outside `A`, hence in `B`, and so extends
over `M_B`; the two extensions glue.  The same argument applies with
the roles reversed and proves the vertex- and edge-deletion statements.

For an internal edge `uv` of `M_A`, choose a new state and a colouring
of `M_A-uv` which realizes it.  The endpoints `u,v` have the same
colour.  Otherwise this colouring would also colour `M_A`, contrary to
the novelty of the state.  Identifying `u,v` therefore gives a proper
colouring of `M_A/uv` with the same boundary state, which again extends
over `M_B`.  Symmetry proves the contraction statement on both sides.

This proves strengthening 2.

## 5. Consequence for exact-adhesion proofs

The theorem is label-free and palette-uniform.  In particular, a proof
across a fixed adhesion cannot succeed from the following data alone:

* two disjoint extension-state families;
* saturation by prescribed exact independent blocks;
* crossed disagreement of states produced on opposite sides; and
* the assertion that every internal vertex/edge deletion and internal
  edge contraction unlocks a state accepted by the other side.

Whenever those requirements admit a complementary two-colouring of the
proper boundary-state space, Theorem 1.1 realizes the entire abstract
transition pattern by actual graph gadgets.  The missing positive input
must therefore constrain the geometry of the realizers: high
connectivity, portal placement, clean linkage, or exclusion of the
target minor.

For the forced exact-eight `C_6+K_1` gate, take

\[
              F=W_5\mathbin{\dot\cup}3K_1,
\]

and split the proper at-most-six-block states by block-count parity.
The parity verification in `hadwiger_c6_exact8_state_gate.md` shows that
both classes meet every exact independent-block family, including every
two-vertex nonedge block.  Thus all hypotheses above hold, and the
uniform theorem recovers Propositions 5.1--5.2 of that note.

## 6. Trust boundary

This is a negative structural theorem about proof methods, not a
counterexample to Hadwiger.  In particular, it supplies no graph which
is simultaneously

1. seven-connected;
2. seven-contraction-critical;
3. equipped with the literal two-full-shore exact-eight geometry; and
4. `K_7`-minor-free.

The conjunction of those four properties remains precisely where a
geometric parity-breaking or rooted-model exchange theorem can act.
