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

This theorem subsumes the earlier gate-, cross-lobe-, single-missing-, and
Moser-specific paired-state component closures whenever its component and
disjoint-packet hypotheses hold.  Those earlier results remain valid
dependencies and laboratories; they are not the active target.

### Active target: state-preserving packet extraction

Prove one bridge-stable exchange theorem for a residual `(1,2)` cell:

> From two disjoint rich `S`-full packets and an attained paired-triangle
> state, either reflect the state, extract a three-connected `S`-full
> component disjoint from another full packet (so the uniform theorem
> applies), or produce a label-faithful near-`K_7`/fixed-pair handoff.
> Every recursive adhesion outcome must transport a legally attained exact
> state and strictly decrease a declared rooted measure.

The immediate obstruction is not another boundary support pattern.  After
the singleton closure, it is that two full packets can be interlaced inside
one connected rich component or can lie in nonsingleton low-connectivity
components, so the common-face cell cut has additional bridge exits.  The
current packet-bridge rotation is a reversible local move; the missing
theorem must compose a whole stable bridge component without losing literal
labels or the attained state.

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

### S4. Other interfaces — open

Even a complete S3 theorem leaves packet vector `(1,1)`, adhesions larger
than seven, and near-model rotation components that expose no actual
seven-adhesion.  These must feed back into S1.  No audited result currently
turns packet thinness alone into a bounded transversal or fixed apex pair.

## Exact remaining gap

No audited implication yet turns every hypothetical counterexample into a
literal `K_7` or a valid global six-colouring.  The immediate missing step
is the state-preserving packet-extraction theorem above.  After it, arbitrary
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
