# Gate A: faithful one-torso lift and the sharp two-carrier obstruction

## Status

This note combines the audited full-state bi-Helly extraction, the
two-layer matching dichotomy, and the faithful quotient-cut lift.

It proves an infinite-family theorem for a quotient cut containing one
rooted gate: either the carrier splits with every required portal row
preserved, an actual cut of order at most six appears, or one straddling
lobe has a named missing row.  It also gives the exact combined-network
consequence for two gated carriers.

The hoped-for final step

> straddling dark lobes automatically assemble into one coherent
> two-apex web

is false from the current local hypotheses.  A sharp two-star network at
the end of the note has maximal `Q`-full partition, large combined
left--right capacity, no state split, and two nonplanar straddling lobe
systems with incompatible missing labels.  The missing hypothesis is a
**state-forcing cross-lobe theorem**: a crossing between complementary
missing-row lobes must lift to two full state carriers or a labelled
clique model.  Ordinary path surplus does not provide that lift.

## 1. Full-row shore extraction is sound

For a carrier `D`, include among the required rows all intercarrier portal
sets `Q_{ij}=N_{D_i}(D_j)` as well as the three state rows `A,B,C`.
Theorem 2.1 of `hadwiger_full_state_shore_bihelly.md` is valid:

1. if a left state carrier and a right state carrier are disjoint, a
   shortest connector and a spanning-tree cut extend them to a full
   typed shore bipartition;
2. if no such pair exists, the trace subtrees of all minimal left and
   right carriers cross-intersect in any tree decomposition;
3. subtree Helly either gives one bag meeting every left carrier, or two
   disjoint left traces force every right trace through their joining
   path.

Thus every carrier has either a full typed split retaining **every**
intercarrier row, or one rooted gate/cycle/3-connected torso.  In the
all-split case every two-by-two shore contact graph has no isolated
vertex and therefore a perfect matching.  The connected-shore cocycle
and matching dichotomies then apply without further portal enumeration.

The only global Gate A residue is consequently a carrier with one rooted
torso (or the first incompatibility between two such torsos), not failure
to preserve an old whole-bag contact.

## 2. A strengthening of the elementary two-gate outcome

Let `P_1,P_2,P_3` be three portal classes in a connected carrier.  If
neither elementary typed shore state exists, Theorem 2.1 of
`hadwiger_state_shore_or_two_gate.md` gives gates `z_2,z_3` such that

\[
 z_2\text{ meets every }(P_1\cup P_3)\text{--}P_2\text{ path},
 \qquad
 z_3\text{ meets every }(P_1\cup P_2)\text{--}P_3\text{ path}. \tag{2.1}
\]

The components after deleting the gates are not merely dark.

### Lemma 2.1 (portal-monochromatic gate lobes)

Every component of `D-{z_2,z_3}` meets at most one of
`P_1,P_2,P_3`.

#### Proof

A component meeting `P_1,P_2` contains a path between them avoiding
`z_2`; a component meeting `P_1,P_3` contains such a path avoiding
`z_3`; and a component meeting `P_2,P_3` contradicts either gate.
\(\square\)

For the full-row bi-Helly gate the analogous conclusion is that every
off-gate lobe misses a **named required row**.  Portal monochromaticity is
special to the elementary three-row two-gate certificate.

## 3. Complete one-gated-carrier quotient-cut lift

Use the notation of `hadwiger_qfull_carrier_adhesion_lift.md`.  Thus
`Q={q_1,q_2,q_3}` is the neutral triangle, `R` is the maximal `Q`-full
quotient, and a quotient separator `S` has its components divided into
nonempty left and right families.  Suppose `S` contains exactly one
nonsingleton carrier `D`; its possible second member is a singleton, and
write that singleton set as `S_0`.

### Theorem 3.1 (one rooted gate: split, cut, or straddling defect)

Assume one of the following carrier certificates.

* **Full-state certificate:** `D` has a full typed shore split, or a
  bi-Helly gate `B` of order at most two such that every component of
  `D-B` misses a named row required by the obstructed state half.
* **Elementary `Q` certificate:** `D` has an elementary typed shore split,
  or the gate set `B={z_2,z_3}` from (2.1), of order at most two.

Then at least one of the following holds.

1. `D` has the corresponding typed shore split.
2. `Q union S_0 union B` is an actual separator of `G`, of order at most
   six.
3. Some component `K` of `D-B` meets both `N_D(L)` and `N_D(R)`.  In the
   full-state version it misses a named required row; in the elementary
   `Q` version it meets at most one neutral portal class.

Consequently, in a seven-connected graph, failure of the split forces the
straddling-defect outcome.

#### Proof

Assume there is no split and choose the displayed gate.  If no component
of `D-B` meets both quotient incidence sides, then `B` separates all
left carrier portals from all right carrier portals.  The faithful lift
lemma makes `Q union S_0 union B` an actual separator.  Its order is at
most

\[
                         3+1+2=6.                  \tag{3.1}
\]

Otherwise a straddling component exists.  Its missing-row conclusion is
the bi-Helly torso conclusion in the full-state case and Lemma 2.1 in the
elementary case. \(\square\)

This removes all internal block trees and all carrier order from a
one-carrier cut.  The residual is one explicit straddling lobe, not an
unlocated portal configuration.

## 4. Exact two-carrier combined-network consequence

Now let the quotient separator be `S={D,E}` and put

\[
 U=D\cup E
\]

including every cross-edge between the two carriers.  Let `L_U,R_U` be
the combined portal sets from the two quotient shores.

### Theorem 4.1 (combined capacity or a literal cut)

In a seven-connected graph, every `L_U`--`R_U` vertex separator in
`H[U]` has order at least four.  Equivalently, in the set version of
Menger's theorem, `H[U]` contains four pairwise vertex-disjoint
`L_U`--`R_U` paths, with order-one paths allowed when the portal sets
overlap.

#### Proof

A separator `T` of order at most three lifts faithfully to the actual
separator `Q union T` of order at most six, contradicting
seven-connectivity.  Set-Menger gives the linkage formulation. \(\square\)

Suppose both carriers have gate sets `B_D,B_E` of order at most two.  If
their union separates the combined portal sets, it gives an actual cut of
order at most seven.  This is tight rather than contradictory: four
distinct gate vertices give an allowed exact seven-cut.  If the union
does not separate, a component of

\[
                    U-(B_D\cup B_E)                \tag{4.1}
\]

straddles the quotient shores.

In the elementary three-row setting, split that component at the
cross-edges between `D` and `E`.  Every resulting lobe in either carrier
has one portal label by Lemma 2.1.  A combined component can nevertheless
contain several labels: along a path in its lobe-contact graph, the label
may change at a cross-carrier edge.  Thus individual darkness does not
give one common missing neutral label.

Theorem 4.1 is the strongest conclusion supplied by seven-connectivity
alone.  It controls combined path capacity, not the label sequence or
rotation of those paths.

## 5. Sharp cross-lobe counterarchitecture

The following network satisfies all the local conclusions above and
shows why a web does not follow automatically.

Take two carriers `D,E`.  Each is a star, with centres `d,e`; its leaves
are its portal vertices.  In `D` take three leaves of label 1, three of
label 2, and one of label 3.  In `E` take one leaf of label 1, three of
label 2, and three of label 3.  Add the cross-edges

\[
 K_{3,3}[D_1,E_2]\quad\text{and}\quad
 K_{3,3}[D_2,E_3],                                 \tag{5.1}
\]

and no other `D`--`E` edges.  Let the left quotient shore meet every
leaf in `D_1 union D_2`, and the right quotient shore meet every leaf in
`E_2 union E_3`.

The properties are exact.

1. Each carrier is `Q`-full, but any connected subgraph meeting two
   portal labels contains its star centre.  Hence two disjoint typed
   carriers do not exist; `d` and `e` are the respective one-vertex
   gates.
2. After deleting the gates there are two straddling combined components.
   One has label profile `{1,2}` and misses 3; the other has profile
   `{2,3}` and misses 1.  There is no common missing label.
3. Separating the combined left and right portal sets requires a vertex
   cover of both disjoint `K_{3,3}` contact graphs, hence six vertices.
   In particular the four-path consequence of seven-connectivity is far
   too weak to eliminate the network.
4. Every connected `Q`-full subgraph of `D union E` contains `d` or `e`,
   because every component after deleting the two centres misses a
   portal label.  Therefore there are at most two disjoint connected
   `Q`-full subgraphs.  The partition into `D,E` is already maximal; the
   counterarchitecture does not disappear by repartitioning.
5. Each cross-lobe system in (5.1) is nonplanar.  It has no compatible
   rural disk embedding, despite the fact that the individual carriers
   are trees.

This is a counterexample to the proposed **local implication**, not a
seven-connected counterexample to Hadwiger: a full ambient host may impose
additional contraction-critical restrictions.  It proves that gates,
maximal `Q`-full partition, and even combined linkage surplus do not by
themselves yield a coherent two-apex web.

## 6. The precise missing hypothesis

The remaining theorem must use more than path capacity.  One sufficient
form is:

> **State-forcing cross-lobe hypothesis.**  In the combined lobe-contact
> graph of the first one/two rooted torsos, any crossing or non-rural
> block involving lobes with different missing rows expands either to
> two disjoint full state carriers preserving every intercarrier row, or
> directly to the labelled `K_7` model.

Under this hypothesis, the full-state bi-Helly theorem gives the desired
trichotomy.

* If all carriers split, their two-by-two contact graphs have perfect
  matchings, and the connected-shore matching dichotomy gives the target
  minor or the perfect/singly-exposed transport state.
* A separated gate lifts to an actual cut of order at most six by
  Theorem 3.1.
* A non-rural straddling network fires the state-forcing hypothesis.
* If no crossing fires, all lobe rotations are compatible.  A coherent
  two-apex conclusion then additionally requires an outerplane quotient
  and one common neutral row on the outer boundaries.

The outerplane condition is necessary, not cosmetic.  If
`G-(Q-{q_k})` is planar, contracting every `Q`-full carrier shows that
`q_k` joined to the quotient `R` is planar; therefore `R` is outerplanar.
A merely `K_4`-minor-free quotient can contain `K_{2,3}` and need not be
outerplanar.

Thus the current machinery completely handles the all-split family and a
one-gated-carrier cut.  Gate A is now concentrated in one statement:
turn the first cross-label, non-rural lobe interaction inside a
cycle/3-connected rooted torso into a full-row state split or labelled
minor.  Without that state-forcing lift, the counterarchitecture (5.1)
is the sharp obstruction.

