# The forced exact-eight gate: full shores and a sharp parity counterstate

## 1. Purpose

The forced three-cut now has exactly two lobes.  Choosing a defect-two
lobe gives an eight-vertex adhesion.  This note proves that the adhesion
has exactly two full open sides and then audits the strongest
finite-boundary conclusion available from whole-shore contractions.

The result is mixed but sharp.

* The exact-eight cell is genuinely a two-full-shore state gate, so the
  exact-block and crossed-operation theorems apply without a virtual
  lift.
* The four-polarity structure does **not**, by itself, force a common
  six-colour boundary partition.  In the antipodal/antipodal polarity
  there is an allowed boundary whose exact-block hypergraph has an
  explicit parity Property-B colouring.

Thus a final theorem must relate the state of a specified internal
deletion/contraction to the model-labelled lobe geometry.  Merely knowing
that every whole-shore block contraction has a colouring cannot suffice.

## 2. The order-eight boundary has exactly two full shores

Retain the notation of `hadwiger_c6_threecut_lobe_exchange.md`.  Thus

\[
                  D-T=C_1\mathbin{\dot\cup}C_2,                 \tag{2.1}
\]

the two lobes are anticomplete and both have an edge to every vertex of
`T`.  Let `A_i=S-N_S(C_i)`, and choose `|A_1|=2`.  Put

\[
                         X=T\mathbin{\dot\cup}(S-A_1).           \tag{2.2}
\]

### Lemma 2.1 (literal two-full-shore lift)

The graph `G-X` has exactly two components.  One is `C_1`; denote the
other by `R`.  Both are full to all eight vertices of `X`.

#### Proof

By definition, `C_1` has neighbours at all three vertices of `T` and at
all five vertices of `S-A_1`, so it is full to `X`.

The other lobe `C_2` is disjoint from `A_2`, and the polarity theorem
gives `A_1 cap A_2=emptyset`.  Hence `C_2` has an edge to each member of
`A_1`.  The old opposite shore `H` is full to `S`, so every member of
`A_1` has an edge to `H`.  Therefore

\[
                          C_2\cup A_1\cup H                      \tag{2.3}
\]

is connected in `G-X`.  Every further old component of `G-S`, if one
exists, is full to `S` and hence also joins (2.3) through `A_1`.
Together these vertices contain everything outside `X union C_1`; call
the resulting component `R`.

The component `R` is full to `S-A_1` through `H`, and it is full to `T`
through `C_2`.  Hence it is full to `X`.  No third component remains.
QED.

This proof uses actual edges.  The vertices of `T` are not contracted
owner labels, and the missed old labels `A_1` really lie in the opposite
open component.

## 3. Exact boundary-state consequence

Let `L=C_1 union X` and `M=R union X` be the two closed shores.  Let
`Omega` be the proper partitions of `X` into at most six independent
blocks, and let `E_L,E_M` be the partitions extendable over the two
closed shores.

The exact-block theorem gives

\[
 E_L\cap E_M=\varnothing,\qquad
 E_L\cap\Omega(P)\ne\varnothing\ne E_M\cap\Omega(P)             \tag{3.1}
\]

for every nonempty independent `P subseteq X`.  Equivalently, the
exact-block hypergraph of `G[X]` must have Property B.

Every statement in (3.1) is forced by a proper whole-shore contraction:
contract `C_1 union P` and delete the remainder of its open side to
obtain a state extending `M`, and symmetrically for `R union P`.  Thus
(3.1) includes all information obtained from such contractions while
forgetting which internal operation produced which state.

## 4. The antipodal polarity admits a parity counterstate

Use the fourth polarity of Theorem 2.5:

\[
                         A_1=\{0,3\},\qquad A_2=\{1,4\}.         \tag{4.1}
\]

The boundary `X` contains the old labels

\[
                             1,2,4,5,z                           \tag{4.2}
\]

and the three vertices of `T`.  Consider the allowed boundary graph
`X_0` in which `T` is independent and anticomplete to the five old
labels.  On the old labels, `z` is universal and

\[
                            1-4-2-5-1                            \tag{4.3}
\]

is the four-cycle of present edges.  Thus

\[
                              X_0=W_5\mathbin{\dot\cup}3K_1.    \tag{4.4}
\]

This respects the forced polarity: `T` necessarily misses
`0,1,3,4`, and (4.4) merely allows it to miss the two additional old
labels as well.  The polarity theorem explicitly permits such additional
misses.

### Theorem 4.1 (parity Property B)

Colour every proper partition `Pi` of `X_0` into at most six blocks by

\[
                              c(\Pi)=|\Pi|\pmod2.                 \tag{4.5}
\]

For every nonempty independent `P subseteq V(X_0)`, the exact-block edge
`Omega(P)` contains partitions of both parities.  Consequently the
families

\[
             \mathcal R=\{\Pi:|\Pi|\text{ even}\},\qquad
             \mathcal B=\{\Pi:|\Pi|\text{ odd}\}               \tag{4.6}
\]

are disjoint and satisfy every exact-block requirement in (3.1).

#### Proof

Fix a nonempty independent set `P` and put `F=X_0-P`.  The graph `X_0`
is three-colourable, so `F` has a proper partition into
`h=chi(F)<=3` nonempty independent colour classes.

If some class has at least two vertices, split off one vertex.  This
gives proper partitions of `F` into `h` and `h+1<=4` blocks.  Adjoining
the exact block `P` gives two members of `Omega(P)`, each using at most
five blocks, and their parities differ.

It remains to rule out the case in which every class of a minimum
colouring is a singleton.  Then `F` is complete.  We claim that no
independent `P` has complete complement in `X_0`.

If `z in P`, no rim vertex of the wheel belongs to `P`; hence all four
rim vertices lie in `F`, where they induce a four-cycle rather than a
clique.  If `z notin P`, then `z in F`.  For `F` to be complete, all
three isolated vertices of (4.4) must lie in `P`.  The remaining part of
`P` is an independent subset of the four-cycle, of order at most two.
After deleting such a subset, at least two rim vertices remain; if two
were deleted, the remaining two are the opposite, nonadjacent pair.
Thus the rim vertices left in `F` do not form a clique.  This proves the
claim and completes the parity construction.  QED.

The standalone verifier `c6_exact8_orbit4_parity_verify.py` enumerates
all 573 proper at-most-six-block partitions of `X_0` and checks (4.5)
for all 63 nonempty independent blocks.

## 5. A formal contraction-state countermodel

The parity construction is more than a hypergraph curiosity.  It gives a
precise countermodel to the following proposed inference:

> two full shores, all whole-shore exact-block contractions, and
> opposite-operation state disagreement force a common boundary state.

Assign the even states (4.6) to one unoperated shore and the odd states
to the other.  For every contraction with prescribed exact block `P`,
Theorem 4.1 supplies an even and an odd member of `Omega(P)`, so the two
whole-shore contraction requirements can be met.  Assign every faithful
operation supported in the first open shore an odd state and every
faithful operation supported in the second an even state.  Then

* each operated state is accepted on the unoperated opposite side;
* it is rejected by its original side; and
* states assigned to operations on opposite sides never agree.

These are exactly the formal novelty and crossed-disagreement conclusions
of proper-minor criticality.  Nevertheless no common state exists.

This is a countermodel to the listed **state axioms**, not an actual
seven-contraction-critical graph: arbitrary assignments in (4.6) need
not be simultaneously realizable by graph sides.  Its force is logical.
Any successful gluing theorem must use an additional graph-realizable
relation among the states of different internal edges—Kempe connectivity,
endpoint ownership, or a labelled branch-set rerouting.  State existence,
exact-block saturation, parity counts, and crossed disagreement alone
cannot prove the result.

### Proposition 5.1 (the parity sides are graph-realizable and full)

For each `epsilon in {even,odd}` there is a finite graph `H_epsilon`
containing `X_0` induced on the labelled boundary `X` such that

1. a labelled six-colouring of `X` extends over `H_epsilon` exactly
   when its equality partition is proper on `X_0` and has parity
   `epsilon`; and
2. `H_epsilon-X` is connected and has neighbourhood exactly `X`.

#### Proof

Let `R_epsilon` be the set of labelled six-colourings of `X` whose
equality partitions lie in the corresponding family in (4.6).  This
relation is invariant under every permutation of the six colours.  The
finite colouring-relation realization theorem of Dvorak--Swart
(Theorem 3 of *A note on extendable sets of colorings and rooted
minors*, arXiv:2504.07764) therefore supplies a finite graph whose exact
boundary extension relation is `R_epsilon`.

Add the edges of `X_0` on the boundary.  This removes no intended
colouring, because every member of `R_epsilon` is proper on `X_0`, and
it adds none.  It also creates no conflict with the exact relation:
for every nonedge `xy` of `X_0`, Theorem 4.1 applied to the independent
block `{x,y}` supplies an intended state in which `x,y` are equal, so
no realizing graph could already have forced that nonedge to be an
edge.

It remains to make the open interior connected and collectively full
without changing the relation.  Add a new interior vertex `c`.  For
each `x in X`, add a fresh vertex `l_x` and the path `x-l_x-c`.  For
each component `Q` of the old open interior, choose `u_Q in Q`, add a
fresh vertex `m_Q`, and add the path `c-m_Q-u_Q`.  Any old colouring
extends: choose a colour for `c`, and then colour each new middle vertex
differently from its at most two already coloured neighbours.  The
converse follows by restriction.  The augmented open interior is
connected and has a neighbour at every boundary vertex.  QED.

Gluing `H_even` and `H_odd` along their common boundary gives an actual
non-six-colourable graph with two connected open components, each full
to all eight boundary vertices.  It need not be seven-connected,
minor-critical, or `K_7`-minor-free; hence it is a counterarchitecture
to a full-shore state theorem, not a counterexample to `HC_7`.

### Proposition 5.2 (internal one-step transitions are also realizable)

There are finite boundaried graphs `M_even,M_odd` with exact extension
relations (4.6) such that, after their open interiors are made disjoint
and their copies of `X` are identified, deleting an open-side vertex,
or deleting or contracting an edge with both ends in one open side,
makes the union six-colourable.

#### Proof

Start with the boundary-induced finite realizers of the two exact
relations constructed in the first two paragraphs of Proposition 5.1
(before the connectivity augmentation), and,
on each side, repeatedly delete an interior vertex or an edge with both
ends in the interior whenever the deletion leaves the exact same
boundary extension relation.  Finiteness gives a deletion-minimal
realizer `M_epsilon`.

Deleting an internal object cannot destroy an extension.  By
minimality, every displayed deletion therefore creates a new boundary
state.  Since `M_epsilon` already accepts *every* proper state of parity
`epsilon`, the new state has the opposite parity and is accepted by
`M_{1-epsilon}`.  The two extensions glue.

For an internal edge `uv`, take a new opposite-parity state extending
over `M_epsilon-uv`.  In every corresponding extension, `u,v` have the
same colour: otherwise it would already colour `M_epsilon`.  Identifying
`u,v` therefore gives an extension of the same state over
`M_epsilon/uv`, and it again glues to the opposite side.  QED.

Propositions 5.1 and 5.2 deliberately establish two different sharp
barriers.  Proposition 5.1 has connected full shores but redundant
augmentation paths; Proposition 5.2 has every internal one-step
transition but need not retain connectedness or fullness after
minimization.  No assertion here combines those features with
seven-connectivity and `K_7`-minor-freeness.

## 6. Exact next theorem

The remaining target can now be stated without ambiguity.

> **Geometric parity-breaking theorem.**  In a seven-connected,
> `K_7`-minor-free, non-six-colourable graph with the literal two-full-
> shore adhesion of Lemma 2.1, the two extension relations cannot be
> separated by block-count parity while every proper internal operation
> is globally six-colourable.  More concretely, either two opposite
> operations induce one common equality partition, or an endpoint
> Kempe component crosses the three-gate `T` in a way which expands to
> seven model-clean branch bags.

Theorem 4.1 and Propositions 5.1--5.2 show why every adjective in this
target matters.  Whole-shore exact blocks, actual extension relations,
connected full shores, and abstract internal one-step transitions each
admit parity counterarchitectures.  A proof must use the joint geometric
package: seven-connectivity, portal placement, endpoint Kempe paths and
the absence of the target minor.

## 7. What Kempe switching actually forces

The formal countermodel becomes genuinely restrictive once one asks that
all of one parity be realized by colourings of an actual shore.

### Lemma 7.1 (singleton parity-switch cohesion)

Let `J` be a graph containing a labelled boundary `X`, and suppose every
boundary state extendable over `J` has the same block-count parity.  Let
`c` be an extending six-colouring in which `{x}` is a singleton boundary
block of colour `alpha`.

For every other colour `beta` used on `X`, the `alpha,beta` Kempe
component of `J` containing `x` meets a `beta`-coloured boundary vertex.

#### Proof

If that component met no `beta`-coloured boundary vertex, interchange
`alpha,beta` on it.  The only `alpha`-coloured boundary vertex is `x`, so
colour `alpha` disappears from the boundary, while colour `beta` remains
on the boundary outside the switched component.  The resulting proper
colouring of `J` therefore induces a boundary partition with exactly one
fewer block, contrary to the fixed-parity hypothesis.  QED.

### Conditional Corollary 7.2 (Kempe star plus a clique transversal)

Retain the two-full-shore exact-eight gate of Lemma 2.1.  Suppose one
shore extension family consists only of even-block states and the other
only of odd-block states, as in the formal countermodel (4.6).  Let an
extending six-colouring on one closed shore have singleton boundary
block `{x}`.  Suppose, in addition, that one can select a boundary root
from each of the other five colour blocks so that those five selected
roots form a clique in `G[X]`.  Then `G` has a `K_7` minor.

#### Proof

Choose one boundary root in each of the other five colour blocks.  By
Lemma 7.1, the root `x` is joined to the selected root of every other
colour inside the corresponding two-colour component of the closed
shore.  The five leaf roots are pairwise adjacent by hypothesis.  Thus
the five direct leaf--leaf edges together with the five Kempe
connections from `x` give the rooted `K_6` certificate: equivalently,
the only auxiliary connections which must be packaged are the edges of
a star, and all complementary root pairs are already adjacent.

Every rooted branch bag contains a vertex of `X`.  The opposite open
shore is connected, disjoint from the model, and full to `X`; it is
therefore adjacent to all six rooted bags.  Adding it gives a `K_7`
model.  QED.

The earlier claim that fixed parity by itself implied
`chi(G[X])<=4` was **incorrect and is retracted**.  Lemma 7.1 supplies
only the five centre--leaf Kempe connections.  The rooted-minor
property for a star still requires every pair of leaf roots, which is a
nonedge of that star, to be already adjacent.  Distinct boundary colour
blocks do not provide those edges.  Therefore neither a rooted `K_6`
nor the chromatic conclusion follows without the extra clique-
transversal (or an equivalent model-clean leaf-packing) hypothesis.

The inequality `chi(G[X])<=4` has since been proved independently for
every `K_7`-minor-free bilateral full eight-adhesion, by the full-shore
reserve lift and the seven-vertex critical-core elimination in
`hadwiger_exact8_critical_core_elimination.md`.  That proof does not use
Lemma 7.1 and does not repair the Kempe-star inference above.

The sound residual dynamic question is consequently: correlate the
specified internal operation states strongly enough to produce either
a common state, a clique transversal for a singleton Kempe star, or a
different model-clean packing of the five leaf blocks.

## 8. Why a whole lobe is not automatically a releasable reserve

The reserve-sacrifice theorem in
`hadwiger_common_carrier_cubic_rural_exchange.md` cannot be invoked by
simply naming `C_1` or `C_2` as the released bag.  Its hypotheses require

1. a protected `K_5` frame before release;
2. four pairwise disjoint rooted bags after release; and
3. every rooted bag adjacent to each of the four retained frame bags.

None of these is supplied merely by the two-lobe cut.  The lobes
`C_1,C_2` are anticomplete.  The old full shore `H` is also anticomplete
to both lobes, and its useful adjacencies run through old boundary
vertices.  The three gate vertices join the two lobes, but absorbing
them into proposed rooted bags may overlap the other bags and is exactly
the allocation problem to be proved.  Finally the four-polarity table
does not make four unused boundary labels a clique in every row.

There is one legitimate conditional use.  If an independent argument
produces four disjoint rooted bags in

\[
                   C_1\cup T\cup C_2\cup A_1\cup H             \tag{8.1}
\]

which remain adjacent to a protected retained `K_4` frame, then one may
release whichever old bag they consume and group them as `2+1+1`.
But those four rooted bags are already the missing model-labelled output
of the operation-correlation theorem.  Reserve sacrifice completes that
output; it does not create it from the cut alone.

This role audit prevents a circular shortcut.  The usable new input from
the two-lobe theorem is the literal opposite-operation separation on
`X`, not an automatically available protected frame.
