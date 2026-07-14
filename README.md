# Hadwiger `HC_7` proof programme

## Verdict

`HC_7` is **not proved** here.

The objective is to prove that every finite graph with no `K_7` minor is
six-colourable.  We work from a hypothetical minor-minimal counterexample.
A sufficient terminal outcome is either a literal `K_7` model or a fixed
pair `{p,q}` such that `G-{p,q}` is `K_5`-minor-free: known `HC_5` then
four-colours the remainder, and two fresh colours finish.

This file is the sole authoritative status statement.  The
[proof spine](active/hc7_near_k7_proof_spine.md) records the detailed
dependency chain.

## Frozen kernel

For a hypothetical minor-minimal counterexample `G`:

1. `G` is seven-connected, strongly seven-contraction-critical, and
   `K_7`-minor-free.
2. Every proper minor is six-colourable.
3. Deleting any nominated vertex leaves a six-chromatic graph containing a
   `K_6` minor; a known near-clique theorem also gives a `K_7^vee` minor.
4. Every component behind an actual seven-adhesion is full to all seven
   literal boundary vertices.
5. Palette colours are never identified with branch-set labels without a
   literal contraction, carrier, or exact equality-state argument.

Audited results are frozen unless a concrete inconsistency is found.

## Short dependency chain

### S1. Near-`K_7` normalization — open

Existing normalizations return a literal `K_7`, an actual labelled
adhesion, a reversible one-/two-hole model rotation, or a candidate
fixed-pair certificate.  A whole-component composition theorem is still
missing; local rotations are involutions, not a descent.

The label-faithful rooted-`K_4` handoff produces a named `K_7^vee`, but a
sharp width-five example shows that this static data alone need not produce
`K_7`.

Sources: [handoff theorem](results/hc7_exact7_cross_lobe_rooted_k4_handoff.md),
[audit](results/hc7_exact7_cross_lobe_rooted_k4_handoff_audit.md), and
[upgrade barrier](barriers/hc7_exact7_rooted_k4_k7_upgrade_barrier.md).

### S2. Actual seven-adhesions — partly closed

If `nu_i` is the maximum number of disjoint connected boundary-full packets
in shore `i`, the only packing vectors, up to orientation, are

```text
(1,1), (1,2), (1,3).
```

Adaptive exact-state reflection eliminates `(1,3)`.  The live vectors are
`(1,1)` and `(1,2)`.

Sources: [packet packing](results/hc7_exact_seven_packet_packing.md),
[audit](results/hc7_exact_seven_packet_packing_audit.md),
[`(1,3)` reflection](results/hc7_exact7_adaptive_packet_reflection.md), and
[audit](results/hc7_exact7_adaptive_packet_reflection_audit.md).

### S3. Exact-seven `(1,2)` attained-duty exchange — primary trench

Let `S` be the literal boundary and let the rich shore contain two disjoint
`S`-full packets.  A thin-shore contraction returns an exact equality state
`Pi`.  For a retained singleton clique `K` and an unretained block `B`, the
correct carrier obligation is the state-specific duty

\[
 D_{\Pi,K}(B)=B\cup\{k\in K:N_{G[S]}(k)\cap B=\varnothing\}.
\]

A raw contact count is not a palette-to-label theorem.

One new uniform reflection theorem is now proved and independently audited.
Suppose the attained state is

\[
 \Pi=\{\{a_1,t_1\},\{a_2,t_2\},\{a_3,t_3\},\{c\}\},
\]

the three pairs are independent, distinct pairs have literal inter-block
edges, and `c` has a literal neighbour in every pair.  If the rich shore
has a three-connected `S`-full component `C` and a disjoint connected
`S`-full packet `Q`, then `Pi` reflects.  This holds for every order of
`C`, arbitrary portal multiplicities, shared portals, internal gates, and
web strips.

The proof is structural.  A four-label Hall separator forces two duties to
have distinct nonadjacent portal witnesses.  The audited two-witness theorem
puts all six complete portal stars on one facial cycle.  Orders four and
five contradict outerplanarity or minimum degree; at larger order a
six-label matching has cyclic word `A B D A B D`, while the circle incidence
bound `|F|+6` contradicts the curvature lower bound `2|F|+6`.

Sources: [uniform reflection theorem](results/hc7_exact7_uniform_paired_curvature_reflection.md)
and its [independent audit](results/hc7_exact7_uniform_paired_curvature_reflection_audit.md).

A second audited theorem closes every **singleton component** in a
two-component rich shore of the frozen 129-boundary residual.  Reorienting
at the singleton gives a degree-seven vertex with exactly two exterior
components.  Dirac and the frozen residual leave only the Moser spindle and
`M+13`; the former is covered by the complete two-component Moser theorem,
while a direct two-anchor contraction synchronizes the exact state
`25|46|0|1|3` in the latter.

Sources: [singleton-component closure](results/hc7_exact7_two_component_singleton_closure.md)
and its [independent audit](results/hc7_exact7_two_component_singleton_closure_audit.md).

A third audited theorem gives a genuinely multishore exact-state
synchronization principle.  If one component contains two adjacent labelled
carriers for independent blocks `I,J`, three boundary vertices remain, and
at least two other full components are available, the state returned using
those two components can be reproduced on every component side and glued.
The duty-aware form requires only the literal adjacencies needed by the
state actually returned, rather than complete carrier contact.

Applied to the complementary two-lobe lock, this closes the whole branch in
which both defect pairs are independent.  If exactly one defect pair is an
edge, it also closes every case where the opposite independent pair contacts
both edge endpoints, or contacts one endpoint which is adjacent to the
retained singleton.  A survivor therefore has a literal edge in at least
one defect pair and sharply sparse cross-duty contact.

Sources: [multishore synchronization](results/hc7_exact7_multishore_state_synchronization.md)
and its [independent audit](results/hc7_exact7_multishore_state_synchronization_audit.md).

The remaining complementary two-lobe lock now has a direct, audited
near-model exit.  Its two lobe bags, the old thin full shore joined to one
paired block, the other rich component joined to a second paired block, and
the three remaining boundary vertices form a **spanning labelled
`K_7^vee` model**.  The two possible missing edges share a named singleton
centre.  Existing near-model trichotomies then return `K_7`, an actual
separator, or a proper-bag deficiency rotation.  Thus this entire lock has
left the local portal programme and entered `S1`; it is not a remaining
two-cut case.

Sources: [complementary-lock handoff](results/hc7_exact7_complementary_lock_near_k7_handoff.md)
and its [independent audit](results/hc7_exact7_complementary_lock_near_k7_handoff_audit.md).

The first deficiency rotation of that decorated near model is now
label-rigid.  In the no-`K_7^-` branch a packet donor must transfer exactly
one of its two literal anchors; moving neither or both is impossible.  The
rotated seven bags form a literal `K_3 join C_4`, with the two missing
diagonals named by the moved anchor and the old missing twin.  If the move
changes the twin to `c`, the three relevant boundary vertices are forced
into one named bichromatic Kempe component.  This is a state-transition
invariant, not yet a terminating composition theorem.

Sources: [packet-donor rotation lock](results/hc7_exact7_packet_donor_rotation_lock.md)
and its [independent audit](results/hc7_exact7_packet_donor_rotation_lock_audit.md).

Combining that handoff with the audited cutvertex, small-component, and
three-connected closures gives a concise theorem for the **entire
two-component rich-shore paired-state family**: it either reflects and
six-colours `G`, or supplies the spanning labelled near model above.  A
single two-cut and a two-set Hall calculation suffice; the former exact
two-lobe enumeration and Kempe trace analysis are not dependencies.

Sources: [two-component paired-state trichotomy](results/hc7_exact7_two_component_paired_trichotomy.md)
and its [independent audit](results/hc7_exact7_two_component_paired_trichotomy_audit.md).

A new label-free boundary-core theorem supplies a direct `S1` handoff in
the connected-rich cell.  If a connected boundary set `D` of order one or
two dominates a disjoint three-set `T` containing an edge, then the thin
full packet, two adjacent rich full packets, `D`, and the three vertices of
`T` form a literal labelled `K_7^vee` model.  This closes an unbounded
family without inspecting packet interiors or portal multiplicities.  Its
failure is a sparse boundary-web obstruction, not a new packet case.

Sources: [three-packet boundary-core handoff](results/hc7_exact7_three_packet_boundary_core_handoff.md)
and its [independent audit](results/hc7_exact7_three_packet_boundary_core_handoff_audit.md).

The connected-rich paired-state quotient is now classified exactly.  After
partitioning the connected rich shore into adjacent full packets `P,Q`, the
thin full packet and `P,Q` contain a `K_7^vee` precisely when the boundary
has a `K_4` minor or some one-vertex deletion has a
triangle-with-pendant minor.  If neither occurs, the paired boundary is
exactly a tree, a six-cycle with one pendant vertex, or
`K_{1,3} dotcup K_3`; in particular it has treewidth at most two and a
clique odd-cycle transversal of order at most one.  This is an unbounded,
label-free frontier theorem, not a census of Moser labels.

The same theorem eliminates every cutvertex of the thin packet.  A
duty-faithful bipartition split gives a common exact state and six-colours
`G`; the sole apparent two-lobe lock instead has seven explicit bags forming
a labelled `K_7^vee`.  Thus the paired connected-rich local residue is a
cutvertex-free thin packet over this width-two boundary.

Sources: [connected-rich width-two frontier](results/hc7_exact7_connected_rich_width2_frontier.md)
and its [independent audit](results/hc7_exact7_connected_rich_width2_frontier_audit.md).

The remaining thin geometry has now been reduced further without boundary
casework.  If a thin-shore vertex has internal degree at most three and its
deletion leaves the shore connected, the literal seven-adhesion and Dirac's
critical-neighbourhood inequality produce seven explicit bags forming a
labelled `K_7^vee`.  Consequently every surviving cutvertex-free thin shore
has internal minimum degree at least four.  Moreover, any two-cut with at
least three deletion lobes gives the same handoff.

Sources: [low-internal-degree and two-gate handoffs](results/hc7_exact7_low_internal_degree_handoff.md)
and their [independent audit](results/hc7_exact7_low_internal_degree_handoff_audit.md).

The residual binary two-cut is now closed as well.  Its two lobes, anchored
at opposite gate vertices, are adjacent connected carriers whose supports
have order at least five and cover `S`.  A label-free incidence lemma on the
width-two boundary then gives seven explicit bags forming a labelled
`K_7^vee`.  Thus, after the near-model handoff is excluded from `S3`, the
surviving thin shore is **three-connected** and has internal minimum degree
at least four.

Sources: [binary two-gate near-model theorem](results/hc7_exact7_binary_gate_near_model.md)
and its [independent audit](results/hc7_exact7_binary_gate_near_model_audit.md).

Two additional uniform tools control the next block.  No common portal core
for three boundary labels can contain a `K_4` model; every such core is
two-degenerate.  A `K_4` model in a two-label core can be met by any third
label in at most one model bag unless a labelled `K_7^vee` already exists.
Also, a prescribed portal edge for at most four boundary labels either
extends to a literal matching, or a tight Hall witness exposes a strictly
smaller actual seven-adhesion with an explicit boundary map.  In a
four-connected thin shore the tiny-shore exception is impossible and the
descended side is connected and full.

Sources: [common-portal core obstruction](results/hc7_exact7_common_portal_core_obstruction.md),
its [audit](results/hc7_exact7_common_portal_core_obstruction_audit.md),
[prescribed portal extension or adhesion](results/hc7_exact7_prescribed_portal_extension_or_adhesion.md),
and its [audit](results/hc7_exact7_prescribed_portal_extension_or_adhesion_audit.md).

The non-four-connected thin geometry now has one uniform exit except for a
single literal transition.  A three-cut either has a lobe supported on
exactly four old boundary labels, which is itself a smaller full exact-seven
shore, or all lobes have support at least five and split into two adjacent
near-full carriers, forcing a labelled `K_7^vee`.

The four-connected branch is now terminal rather than recursive.  For every
four boundary labels, seven-connectivity gives a rank-four transversal
matroid of their portal sets.  Every literal portal is a nonloop and hence
belongs to a basis.  Rooted-`K_4` facial coherence then either gives a
labelled `K_7^vee`, or puts all six non-`c` portal systems on one face; disk
curvature supplies a host vertex of degree at most six, contradicting
seven-connectivity.  No equality state, Hall descent, or minimum-shore
choice is used.

Sources: [three-cut portal descent](results/hc7_exact7_three_cut_portal_descent.md)
and its [audit](results/hc7_exact7_three_cut_portal_descent_audit.md),
[cofacial portal degree obstruction](results/hc7_exact7_cofacial_portal_degree_obstruction.md)
and its [audit](results/hc7_exact7_cofacial_portal_degree_obstruction_audit.md),
and [four-connected basis-cover closure](results/hc7_exact7_four_connected_basis_cover_closure.md)
with its [audit](results/hc7_exact7_four_connected_basis_cover_closure_audit.md).

### Active target: support-four three-cut composition

The only local transition left in the paired connected-rich width-two
geometry is a support-four lobe behind a literal three-cut.  For its new
boundary `Omega=T union N_S(D)`, prove one terminal-or-recursive theorem:

> At the new literal boundary `Omega`, either reproduce a legally attained
> state of demand at most two and reflect it; pull back the three named
> paired duties so that the smaller shore is a valid `(1,2)` recursive
> instance; or regenerate a labelled near-`K_7`/fixed-pair handoff.  A
> recursive outcome must strictly decrease the active shore order.

Every new boundary vertex literally meets the smaller lobe.  What is not
yet proved is that the old equality state or the rich-side packet vector
survives this map.  A verified order-minimal architecture shows that the
descended vector can be `(1,1)` and every natural paired pullback can fail,
even under exact seven-connectivity, `chi=7`, Dirac's inequalities, and
legal old-state attainment.  That architecture contains an explicit
`K_7` and is not minor-minimal.  Thus a positive theorem must use
`K_7`-minor-freeness or the full proper-minor response; local packet and
state data alone are exhausted.

Static carrier splitting cannot replace this dynamic step.  First, a verified
exact-seven, minimum-degree-seven graph has thirty-nine surplus contacts and
all local Dirac inequalities but no such thin split; it deliberately contains
a literal `K_7`.  Second, a verified `K_7`-minor-free width-two graph satisfies
the full thin-side degree and cut-expansion bounds but still has no duty
split; it is only five-connected and violates Dirac's neighbourhood
inequality.  Thus neither contact surplus plus connectivity nor
`K_7`-minor-freeness plus local expansion is enough.  A positive theorem must
combine the actual counterexample inputs: global seven-connectivity, Dirac,
`K_7`-minor-freeness, or genuine proper-minor state transitions.

Arbitrary attained demand-three states remain a separate, more general
`S3` obligation.  Packet vector `(1,1)` and near-model rotations remain the
global `S1/S4` escape route if the descent does not preserve `(1,2)`.

Controlling inputs:

- [labelled-carrier reflection](results/hc7_exact7_rich_cutpacket_exchange.md)
  and [audit](results/hc7_exact7_rich_cutpacket_exchange_audit.md);
- [connected-rich constraints](results/hc7_exact7_connected_rich_cutvertex_exchange.md)
  and [audit](results/hc7_exact7_connected_rich_cutvertex_exchange_audit.md);
- [portal-preserving packet rotation](results/hc7_exact7_packet_bridge_rotation.md)
  and [audit](results/hc7_exact7_packet_bridge_rotation_audit.md);
- [stable labelled skeleton](results/hc7_exact7_portal_matching_stable_skeleton.md)
  and [audit](results/hc7_exact7_portal_matching_stable_skeleton_audit.md);
- [binary-duty cycle-or-gate theorem](results/hc7_exact7_binary_duty_cycle_or_gate.md)
  and [audit](results/hc7_exact7_binary_duty_cycle_or_gate_audit.md).
- [multishore state synchronization](results/hc7_exact7_multishore_state_synchronization.md)
  and [audit](results/hc7_exact7_multishore_state_synchronization_audit.md).
- [complementary-lock near-model handoff](results/hc7_exact7_complementary_lock_near_k7_handoff.md)
  and [audit](results/hc7_exact7_complementary_lock_near_k7_handoff_audit.md).
- [packet-donor rotation lock](results/hc7_exact7_packet_donor_rotation_lock.md)
  and [audit](results/hc7_exact7_packet_donor_rotation_lock_audit.md).
- [two-component paired-state trichotomy](results/hc7_exact7_two_component_paired_trichotomy.md)
  and [audit](results/hc7_exact7_two_component_paired_trichotomy_audit.md).
- [three-packet boundary-core handoff](results/hc7_exact7_three_packet_boundary_core_handoff.md)
  and [audit](results/hc7_exact7_three_packet_boundary_core_handoff_audit.md).
- [connected-rich width-two frontier](results/hc7_exact7_connected_rich_width2_frontier.md)
  and [audit](results/hc7_exact7_connected_rich_width2_frontier_audit.md).
- [low-internal-degree and two-gate handoffs](results/hc7_exact7_low_internal_degree_handoff.md)
  and [audit](results/hc7_exact7_low_internal_degree_handoff_audit.md).
- [binary two-gate near-model theorem](results/hc7_exact7_binary_gate_near_model.md)
  and [audit](results/hc7_exact7_binary_gate_near_model_audit.md).
- [common-portal core obstruction](results/hc7_exact7_common_portal_core_obstruction.md)
  and [audit](results/hc7_exact7_common_portal_core_obstruction_audit.md).
- [prescribed portal extension or adhesion](results/hc7_exact7_prescribed_portal_extension_or_adhesion.md)
  and [audit](results/hc7_exact7_prescribed_portal_extension_or_adhesion_audit.md).
- [three-cut portal descent](results/hc7_exact7_three_cut_portal_descent.md)
  and [audit](results/hc7_exact7_three_cut_portal_descent_audit.md).
- [cofacial portal degree obstruction](results/hc7_exact7_cofacial_portal_degree_obstruction.md)
  and [audit](results/hc7_exact7_cofacial_portal_degree_obstruction_audit.md).
- [four-connected basis-cover closure](results/hc7_exact7_four_connected_basis_cover_closure.md)
  and [audit](results/hc7_exact7_four_connected_basis_cover_closure_audit.md).
- [three-cut state-collapse barrier](barriers/hc7_exact7_threecut_descent_packet_collapse_barrier.md)
  and its dependency-free verifier.
- [surplus-only barrier](barriers/hc7_exact7_width2_surplus_thin_split_barrier.md)
  and its executable verifier.
- [`K_7`-minor-free static-split barrier](barriers/hc7_width2_k7free_static_split_barrier.md)
  and its executable verifier.

### S4. Other interfaces — open

Even a complete S3 theorem leaves packet vector `(1,1)`, adhesions larger
than seven, and near-model rotation components that expose no actual
seven-adhesion.  These must feed back into S1.  No audited result currently
turns packet thinness alone into a bounded transversal or fixed apex pair.

## Exact remaining gap

No audited implication yet turns every hypothetical counterexample into a
literal `K_7` or a valid global six-colouring.  The immediate missing step
is the exact-seven descent-composition theorem above.  The new boundary and
strictly smaller full shore are literal and audited; the attained paired
state and packet vector are not yet transported.  After that, arbitrary
attained demand-three states, `(1,1)`, larger adhesions, and S1 rotation
components remain.

Finite certificates in this repository prove only the interfaces stated in
their accompanying notes.  They do not replace an unbounded exchange
theorem.

## Repository layout

- `results/`: proved live lemmas, adjacent audits, and cited certificates;
- `active/`: the current detailed proof spine and current proof attempt;
- `barriers/`: explicit counterexamples and falsifiers;
- `archive/`: superseded, retracted, peripheral, frozen, or unaudited work.

Do not add research files at the repository root.  Historical reports in
`archive/` are not current.

## License

This repository is available under the [MIT License](LICENSE).
