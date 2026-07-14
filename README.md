# Hadwiger `HC_7` proof programme

## Verdict

`HC_7` is **not proved** here.

The target is to rule out a minor-minimal counterexample and thereby prove
that every finite graph with no `K_7` minor is six-colourable.  A sufficient
structural endgame is either a literal `K_7` model or a fixed pair
`{p,q}` such that `G-{p,q}` is `K_5`-minor-free; `HC_5` then gives four
colours on the remainder and two fresh colours finish.

The detailed dependency chain is
[the proof spine](active/hc7_near_k7_proof_spine.md).  This `README.md` is
the sole authoritative status statement; the spine records its detailed
dependencies.

## Frozen minimal-counterexample kernel

For a hypothetical minor-minimal counterexample `G`:

1. `G` is seven-connected, strongly seven-contraction-critical, and
   `K_7`-minor-free.
2. Every proper minor is six-colourable.
3. Known `HC_6` and the near-clique theorem give an unrooted `K_6` model
   after deleting any nominated vertex and a `K_7^vee` minor in `G`.
4. Every component behind an actual seven-adhesion is full to all seven
   literal boundary vertices.
5. Palette colours may not be identified with branch-set labels without a
   literal contraction, carrier, or equality-state argument.

The first three items use known results.  The exact lemmas used later are
linked from the proof spine and from `results/`, with independent audits
beside them.

## Short dependency chain

### S1. Near-`K_7` normalization — open

Audited normalizations return a literal `K_7`, an actual labelled adhesion,
a reversible one-/two-hole model rotation, or a coherent fixed-pair
certificate.  What remains is a composition theorem for a whole rotation
component.  Reversible local rotations are not a descent.

### S2. Actual seven-adhesions — partly closed

If `nu_i` is the maximum number of disjoint connected boundary-full packets
in shore `i`, the audited packing theorem leaves, up to orientation,

```text
(nu_1,nu_2) = (1,1), (1,2), or (1,3).
```

Adaptive exact-state reflection eliminates `(1,3)` uniformly.  The live
seven-adhesion vectors are `(1,1)` and `(1,2)`.

Sources:

- [exact-seven packet packing](results/hc7_exact_seven_packet_packing.md)
  and its [audit](results/hc7_exact_seven_packet_packing_audit.md);
- [`(1,3)` adaptive reflection](results/hc7_exact7_adaptive_packet_reflection.md)
  and its [audit](results/hc7_exact7_adaptive_packet_reflection_audit.md).

### S3. Exact-seven `(1,2)` attained-duty exchange — primary target

Let `S` be the literal seven-boundary, `H=G[S]`, and let the rich shore
contain two disjoint `S`-full packets `P_1,P_2`.  A thin-shore contraction
returns an exact equality partition `Pi` of `S`.  For a maximum clique `C`
among the singleton blocks of `Pi`, suppose the remaining demand is three.
For a non-retained block `B`, define its attained duty by

\[
 D_{\Pi,C}(B)
   =B\;\cup\;\{c\in C:N_H(c)\cap B=\varnothing\}.
\]

A connected subgraph `T` in the rich shore funds this particular block when

```text
T is disjoint from P_1 and P_2, and
D_{Pi,C}(B) is contained in N_S(T).
```

Then `T union B` is connected, it sees every retained singleton, and the
two full packets fund the other two blocks.  The exact state reflects and
the shore colourings glue.  This is the correct state-specific object; an
unconditional “defect at most two” carrier is only a specialized sufficient
criterion inside the audited defect-adaptive normalization.

The theorem-strength target is:

> **Two-packet attained-duty exchange.**  In an actual `(1,2)` adhesion of a
> hypothetical counterexample, a nonrobust thin-shore return yields a
> connected rich-shore carrier discharging one attained duty, a second
> legal return of demand at most two, a literal `K_7`, or one coherent fixed
> pair whose deletion is `K_5`-minor-free.

The current constructive mechanism is packet-bridge rotation followed by a
block-terminal web/stable-skeleton analysis.  Every component outside a
selected full-packet pair has at least three literal attachments to that
pair.  A portal-free one-segment bridge can rotate a packet and free a
connected carrier.  The next proof must test that freed carrier against its
actual attained duty, not merely count its total boundary support.  Failure
of all duty-correct rotations must produce a common exact state or one
coherent rural/fixed-pair certificate.

One uniform step is now audited.  For any attained demand-three state,
choose duty-specific portals in either full packet and take the three duty
hulls in a containing tree.  If two hulls are disjoint, they split into two
adjacent duty-correct carriers and the other full packet funds the third
block, so the exact state reflects.  Otherwise the three hulls have a
literal Helly gate.  A generic gate bypass is insufficient: the unique
private two-portal cyclic obstruction has order `A B D A B D`.  The live
target is therefore label-compatible bypass, or conversion of that coherent
width-two web into an actual adhesion/state-gluing certificate.

The point--tree Koenig theorem now makes the gate portal-choice-invariant
relative to a fixed packet spanning tree.  Either one literal vertex lies
in every attainable hull of all three duties, or one exceptional duty has
pairwise disjoint leaf witnesses around a common subtree contained in every
hull of the other two duties.  The core is not yet tree-invariant, bounded,
or a separator; that gate-descent is the immediate structural gap.

The permutation-labelled non-returning-path route has been audited but is
not yet a theorem in this setting.  Pap's packing theorem would give two
disjoint useful transitions or a two-vertex transversal only after a
faithful encoding in which auxiliary disjointness lifts to literal carrier
disjointness.  Current packet rotations are partial state-dependent moves,
so that encoding is missing.  Perfect--Pym augmentation preserves endpoint
sets, not the permutation label.  A separate verified 7-connected
icosahedral-tube construction also rules out a connectivity-only clean-ear
or gate-bypass shortcut.  Both are guardrails, not new reductions.

One label-compatible web exchange is also audited.  For an attained
paired-triangle state, if two full rich packets contain alternating cycles
through the six selected duty portals, any clean transverse path between
nonhomologous portals reflects the exact state, subject only to the named
literal block edge supplied by that returned state.  Under portal-pure
attachments this eliminates every cross-packet bridge with at least three
attachments.  The surviving interface is a coherent submatching of
homologous portal classes, not a generic cylinder theorem and not yet a
separator.

The atomic coherent cylinder is now eliminated in the pure-Moser state.
If both disjoint full packets contain an exceptional alternating cycle in
literal portal order `2,4,5,3,1,0`, any third disjoint full packet completes
an explicit `K_7`.  Six gap-avoiding branch-set templates handle an
arbitrary clean first-hit path from literal `6` to either cycle, arbitrary
subdivisions, and cycles in the same or different rich components.  The
remaining web gap is therefore extraction: an alternating duty web need
not yet contain such a literal cycle.

A uniform cycle-or-gate theorem now performs that extraction for every
4-connected packet with three binary attained duties.  If no two duties
have disjoint linkage paths, the packet is planar and all six literal duty
portals lie on one facial cycle in order `A B D A B D`.  Without
4-connectivity, a whole shore component instead exposes an internal gate of
order at most three; an `r`-gate lobe contacts at least `7-r` boundary
literals.  For an attained paired-triangle state and a completing full
packet in the same rich shore, every dutyless three-gate lobe has the exact
`c`-plus-one-from-each-duty trace.  Its literal neighbourhood is therefore
a new seven-boundary and gives a strictly smaller exact-seven adhesion.
This is a real descent, but it does not preserve the attained state.

A state-free exit-matching theorem now controls the packet vector after
most such descents.  Relative to the new boundary, sibling lobes and the two
old full packets construct two disjoint full packets unless either there is
exactly one sibling lobe, or at least two siblings all use one common
singleton exit outside the new boundary.  In every other case the new cell
is `(1,2)` or `(1,3)`, with the descended lobe as its thin shore; `(1,3)`
closes by adaptive reflection.

The paired-triangle **common-exit** configuration is now eliminated.  Every
sibling has the exact support consisting of the common exit plus three of
the four retained labels.  Fullness of the old rich component forces the
other two discarded labels to hit the literal three-gate.  Three or more
siblings close by explicit branch sets or `(1,3)` reflection.  With exactly
two siblings, a fixed fifteen-vertex quotient contains a literal `K_7` in
every case.  Its essential finite core is certified solver-free by 37 frozen
monotone templates covering `11,520+13,824` quotients; an independent replay
rechecked connectivity, disjointness, and all 21 bag adjacencies without
using the verifier's graph routines.

The remaining **one-sibling** gate is now sharply funnelled by a
parameter-uniform Hall principle.  If boundary labels missed by both lobes
can enter the old component only through its three-gate, they have distinct
gate representatives.  Combining those representatives with the attained
paired-triangle duties reflects every support pattern except, after
renaming, exactly:

1. the cross-lobe family `T subseteq N_S(J)`; or
2. `N_S(J)={c,a_1,t_2,t_3}`, where every possible second-duty gate
   completion is absent or all nonempty completion sets are concentrated at
   one literal gate vertex.

This is an infinite-family reduction by literal duty carriers, not a
boundary census.  It is also sharp at the static level: a fourteen-vertex
treewidth-five quotient remains `K_7`-minor-free even when the gate is a
triangle and the lobe quotient is `K_5` minus one edge.  Therefore the live
handoff must use internal portal distribution, a genuinely attained
proper-minor state, label-preserving near-`K_7` regeneration, or the
fixed-pair endgame.  No equality state or global descent measure has yet
been transported.

The nonplanar part of the first family is now closed uniformly.  If the
three-connected lobe component contains no two disjoint duty carriers,
three four-terminal web certificates synchronize to one literal face:
seven-connectivity excludes every clique cell and Whitney uniqueness joins
the three pages.  Hall then selects six distinct portals, and nonreflection
forces their facial duty word to be `A B D A B D`; the component has order
at least six.  Under a simultaneous side-specific cofacial matching, the
literal cross-lobe linkage is the reversal
`a_1-t_3, a_2-t_2, a_3-t_1`.  This is geometry, not state transport: the
reversed paths do not legally attain the transposed equality partition.
The immediate target is therefore a proper-minor/Kempe transition from this
literal alternating page to reflection, a named near-`K_7` handoff, or one
coherent two-vertex terminal certificate.

Controlling sources:

- [general labelled-carrier reflection](results/hc7_exact7_rich_cutpacket_exchange.md)
  and its [audit](results/hc7_exact7_rich_cutpacket_exchange_audit.md);
- [packet-demand/clique-deletion identity](results/hc7_exact7_packet_demand_identity.md)
  and its [audit](results/hc7_exact7_packet_demand_identity_audit.md);
- [connected-rich carrier constraints](results/hc7_exact7_connected_rich_cutvertex_exchange.md)
  and its [audit](results/hc7_exact7_connected_rich_cutvertex_exchange_audit.md);
- [portal-preserving packet rotation](results/hc7_exact7_packet_bridge_rotation.md)
  and its [audit](results/hc7_exact7_packet_bridge_rotation_audit.md);
- [stable labelled skeleton](results/hc7_exact7_portal_matching_stable_skeleton.md)
  and its [audit](results/hc7_exact7_portal_matching_stable_skeleton_audit.md);
- [attained-duty tree split or gate](results/hc7_exact7_attained_duty_tree_gate.md)
  and its [audit](results/hc7_exact7_attained_duty_tree_gate_audit.md);
- [portal-choice-invariant gate core](results/hc7_exact7_point_tree_gate_core.md)
  and its [audit](results/hc7_exact7_point_tree_gate_core_audit.md);
- [two-packet cyclic-web exchange](results/hc7_exact7_two_packet_cyclic_web_exchange.md)
  and its [audit](results/hc7_exact7_two_packet_cyclic_web_exchange_audit.md);
- [Moser cyclic-packet completion](results/hc7_exact7_moser_cyclic_packet_completion.md)
  and its [audit](results/hc7_exact7_moser_cyclic_packet_completion_audit.md);
- [binary-duty cycle or labelled gate](results/hc7_exact7_binary_duty_cycle_or_gate.md)
  and its [audit](results/hc7_exact7_binary_duty_cycle_or_gate_audit.md);
- [state-free three-gate exit matching](results/hc7_exact7_three_gate_exit_matching.md)
  and its [audit](results/hc7_exact7_three_gate_exit_matching_audit.md);
- [paired-state common-exit gate closure](results/hc7_exact7_common_exit_gate_closure.md)
  and its [audit](results/hc7_exact7_common_exit_gate_closure_audit.md);
- [one-sibling Hall-and-duty funnel](results/hc7_exact7_one_sibling_gate_funnel.md)
  and its [audit](results/hc7_exact7_one_sibling_gate_funnel_audit.md);
- [cross-lobe common-face theorem](results/hc7_exact7_cross_lobe_common_face.md)
  and its [audit](results/hc7_exact7_cross_lobe_common_face_audit.md);
- [three-gate prescribed-pullback barrier](barriers/hc7_exact7_three_gate_pullback_matching_barrier.md)
  and its [verifier](barriers/hc7_exact7_three_gate_pullback_matching_barrier_verify.py);
- [permutation-labelled encoding gap](barriers/hc7_exact7_permutation_path_encoding_gap.md);
- [block-terminal clean-ear barrier](barriers/hc7_block_terminal_clean_ear_barrier.md)
  and its [verifier](barriers/hc7_block_terminal_clean_ear_barrier_verify.py);
- [alternating gate-bypass barrier](barriers/hc7_exact7_gate_bypass_falsifier.md)
  and its [audit](barriers/hc7_exact7_gate_bypass_falsifier_audit.md);
- [static packet-quotient exhaustion](results/hc7_exact7_three_packet_quotient_characterization.md)
  and its [audit](results/hc7_exact7_three_packet_quotient_characterization_audit.md).

Two scope rules are frozen:

- Failure to attain a clique odd-cycle-transversal state, together with
  failure of one generic carrier construction, does **not** reduce the
  general `(1,2)` cell to Moser.  The Moser reduction requires the extra
  singleton-thin and `alpha(H)<=2` hypotheses.
- A carrier is sufficient relative to `D_{Pi,C}(B)`.  Raw contact count is
  not a palette-to-label theorem.

### S4. Other interfaces — open

Even a complete S3 theorem leaves packet vector `(1,1)`, adhesions of order
greater than seven, and near-model rotation components that never expose an
actual seven-adhesion.  Those interfaces must feed back into S1.  No current
result turns packet thinness into a bounded transversal or an apex pair.

## Exact status of the degree-seven Moser laboratory

The pure-Moser two-exterior case is closed.  In the sole-exterior case the
all-crossless family is closed by one block-terminal web, while a surviving
shore has a crossed frame and a model-carried connector separator.  This is
supporting infrastructure, not a reduction of general `(1,2)` to Moser.

One further infinite cyclic family is closed.  For the normalized attained
state `23|14|05|6`, a cycle through the six selected duty portals reflects
unless its duty pairs alternate.  Of the eight literal alternating orders,
six give audited explicit `K_7` models using the other rich full packet and
the thin full packet.  Only the symmetry orbit represented by
`2,4,5,3,1,0` remains; arbitrary bridges not containing such a six-portal
cycle are outside this theorem.

For two such packet cycles, the audited transverse-web theorem eliminates
every nonhomologous clean cross-path in the paired-triangle state.  Its
static verifier also shows that homologous rungs alone do not split the
cycles into three disjoint duty carriers.  The separate audited
cyclic-packet completion now kills that entire coherent residue directly:
the two exceptional cycles and the third full packet already form a
literal `K_7`, even with no rungs or path between the cycles.

A recent audit corrected the conditional exact-order-six rural endgame:

- two disjoint crossed-frame carriers join alternating pairs on the literal
  `U`-cycle, so the shore cannot be a single disk page with that cycle as
  boundary;
- a planar contracted two-pole quotient does not remove this obstruction;
- opposite failed Kempe switches may simply return to their already owned
  blocks.

The valid dynamic gain is narrower: in the exact-order-six cell, a mismatch
of supported decoration states gives a literal first-hit Kempe path owned by
an actual named core block.  Rank-one mismatch leaves a **self-locking gate**;
it does not yet give the opposite attained duty.  This exact-six branch is
frozen while S3 is primary.

Sources:

- [owned first-hit Kempe gate](results/hc7_exact7_bilateral_decoration_kempe_lock.md)
  and its [audit](results/hc7_exact7_bilateral_decoration_kempe_lock_audit.md);
- [crossed-frame disk barrier](barriers/hc7_exact7_crossed_frame_disk_barrier.md),
  [audit](barriers/hc7_exact7_crossed_frame_disk_barrier_audit.md), and
  [verifier](barriers/hc7_exact7_crossed_frame_disk_barrier_verify.py);
- [paired-Kempe self-lock barrier](barriers/hc7_exact7_two_shore_kempe_pairing_barrier.md)
  and [verifier](barriers/hc7_exact7_two_shore_kempe_pairing_barrier_verify.py).
- [Moser cyclic duty exchange](results/hc7_exact7_moser_cyclic_duty_exchange.md)
  and its [audit](results/hc7_exact7_moser_cyclic_duty_exchange_audit.md).
- [two-packet cyclic-web exchange](results/hc7_exact7_two_packet_cyclic_web_exchange.md)
  and its [audit](results/hc7_exact7_two_packet_cyclic_web_exchange_audit.md).
- [Moser cyclic-packet completion](results/hc7_exact7_moser_cyclic_packet_completion.md)
  and its [audit](results/hc7_exact7_moser_cyclic_packet_completion_audit.md).

## Exact remaining gap

No audited theorem currently turns every hypothetical counterexample into a
literal `K_7` or a valid global six-colouring.  The immediate missing
implication is S3's two-packet attained-duty exchange.  After that, S1 and
S4 still require a uniform composition theorem.

Computational certificates in the repository establish only the finite
interfaces stated in their accompanying proofs.  They are not a substitute
for the unbounded shore-exchange theorem, and they remain a trust boundary
until their encodings and coverage are independently checked.

## Repository layout

- `results/`: proved live lemmas, their adjacent `_audit.md` files, and the
  exact verification assets cited by those lemmas.
- `active/`: only the current proof spine.  The ignored `active/runtime/`
  directory is local tooling, not mathematical status.
- `barriers/`: explicit counterexamples, falsifiers, and blocked mechanisms.
- `archive/`: superseded, retracted, peripheral, frozen, or unaudited work.

`README.md` is the only authoritative status file.  Do not add new files at
the repository root.  Historical status reports in `archive/` are not
current, and moving a draft there is not a mathematical retraction unless
its own text says so.

## License

This repository is available under the [MIT License](LICENSE).
