# Hadwiger `HC_7` proof programme

## Verdict

`HC_7` is **not proved** here.

The target is to rule out a minor-minimal counterexample and thereby prove
that every finite graph with no `K_7` minor is six-colourable.  A sufficient
structural endgame is either a literal `K_7` model or a fixed pair
`{p,q}` such that `G-{p,q}` is `K_5`-minor-free; `HC_5` then gives four
colours on the remainder and two fresh colours finish.

The detailed dependency chain is
[the proof spine](active/hc7_near_k7_proof_spine.md).  This file is the sole
authoritative status statement.

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

One label-compatible web exchange is also audited.  For an attained
paired-triangle state, if two full rich packets contain alternating cycles
through the six selected duty portals, any clean transverse path between
nonhomologous portals reflects the exact state, subject only to the named
literal block edge supplied by that returned state.  Under portal-pure
attachments this eliminates every cross-packet bridge with at least three
attachments.  The surviving interface is a coherent submatching of
homologous portal classes, not a generic cylinder theorem and not yet a
separator.

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
cycles into three disjoint duty carriers.  This is a sharp carrier barrier,
not evidence that the cylinder is `K_7`-minor-free: a separate exact search
is currently being converted into literal branch-set templates for that
residue.

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

- `results/`: proved live lemmas, with `_audit.md` files beside them.
- `active/`: the current proof spine, current proof attempt, and scripts.
- `barriers/`: explicit counterexamples and blocked mechanisms.
- `archive/`: superseded, retracted, peripheral, or frozen work.

Do not add new files at the repository root.  Historical status reports in
`archive/` are not current.
