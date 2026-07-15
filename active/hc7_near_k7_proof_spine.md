# `HC_7` proof spine

## Verdict and target

`HC_7` is not proved.  For the frozen hypothetical minor-minimal `HC_7`
counterexample `G`, the active target is

\[
 \boxed{
  \text{7-connected + strongly 7-contraction-critical + }K_7^\vee
  \Longrightarrow K_7\text{ minor or a fixed }\{p,q\}
  \text{ with }G-\{p,q\}\text{ }K_5\text{-minor-free}.}
\tag{T}
\]

The second outcome is terminal: `HC_5` four-colours the remainder and two
fresh colours finish.  A planar remainder is sufficient but stronger than
needed.

## Current research goal

The active proof engine is the
[`dominating-edge sink programme`](hc7_global_dominating_edge_sink_goal.md).
For a literal pair `P`, a dominating `K_5` model in `G-P` returns a literal
terminal edge.  After normalizing its last three bags to an induced cycle,
every edge of that cycle is a legal successor.  Thus the transition language
is closed on literal pairs, and every hypothetical counterexample has a sink
strongly connected component made of edges.  Every state in that sink has a
vertex-disjoint induced cycle entirely in the same sink.

The next theorem must classify the **whole closed family**:

> A closed terminal-cycle family in a seven-connected, strongly
> seven-contraction-critical, `K_7`-minor-free graph yields a literal `K_7`
> or one fixed pair meeting every `K_5` model.

The first split is chromatic.  A sink edge is either double-critical or its
two-vertex deletion remains six-chromatic.  Existing double-critical minor
theorems do not apply to a closed subfamily of edges, and the six-chromatic
branch regenerates only an unrooted `K_6`; coupling those responses is the
open global exchange.

The May 2026 near-Hajós theorem gives the accompanying pair height:
every `G-P` contains a subdivision of `K_5` or `hat K_5`.  Its shortest
support agrees with ordinary `K_5`-model support through order six, so it
geometrizes all four support-six types.  It does not itself increase under
edge rotation.  See [`hc7_global_near_hajos_pair_height.md`](hc7_global_near_hajos_pair_height.md).

The support-six pullback and actual `(1,2)` shore rank remain independent
backup mechanisms.  The twin-seam target is frozen unless it supplies a
literal transition or terminal classification in the global edge sink.

## Frozen prior research goal

The global target is the
[`K_5`-model transversal theorem](hc7_global_k5_transversal_goal.md):

\[
  \text{seven-connected}+\text{strongly 7-contraction-critical}+K_7^\vee
    \Longrightarrow K_7\text{ or }\tau_5(G)\le2.
\]

It is `HC_7`-strength.  The programme does not presently possess a
well-founded invariant for all near-model rotations; it possesses one
only for strict actual `(1,2)` packet-one-shore descent.

The global invariant gate precedes every local target below.  Normalize
near-model reselections and exact rotations by their whole neutral
components, and regard a local decoder as progress only when it gives a
legal proper-minor transition between such components, a strict actual
`(1,2)` packet-one-shore descent, or a terminal outcome.  The missing
composition theorem is:

> Every sink component of the normalized response transition system has a
> common exact state, a literal `K_7`, or one fixed pair meeting every
> `K_5` model of `G`.

Two audited obstructions make this necessary.  Rooted-core reselection has
an exact involutive cycle preserving all obvious model statistics, while a
globally maximal adjacent-pair/`K_5` contact profile can be a one-hole
near-model with a hidden, numerically invisible fixed pair.  Thus neither
contact order nor local bag improvement is a well-founded invariant.

Finiteness of the response graph only guarantees a sink.  Its state
language is not yet proved closed and its sinks are not classified, so the
displayed sink-coherence statement is a target rather than a theorem or a
constructed rank.

One global rung is now closed.  Every seven-connected graph either has a
`K_7` minor or a two-vertex transversal of all literal `K_5` subgraphs.
Therefore, in the target-free branch, the maximum over pairs of the minimum
support order of a `K_5` model after deleting that pair is at least six.
The theorem and audit are
`../results/hc7_global_literal_k5_transversal.md` and its adjacent audit.
The next support form has one two-vertex bag and four singleton bags.  It
must be handled by a global pair exchange or a uniform all-orders
principle, not by another unranked local normalization.

More precisely, let `tau_5^{<=r}(G)` be the transversal number of the
supports of all `K_5` models of order at most `r`.  The proved theorem gives
`tau_5^{<=5}(G)<=2`; the terminal is
`tau_5^{<=|G|}(G)<=2`.  The global invariant programme is the uniform
extension

\[
       \tau_5^{\le r}(G)\le2
          \Longrightarrow \tau_5^{\le r+1}(G)\le2.       \tag{U}
\]

The support-six contraction dichotomy proves the exact first-step normal
form and hands a failed contraction to an actual seven-adhesion.  In the
seven-connected contraction branch, both split endpoints are saturated in
all five other colours of every proper-minor six-colouring.  What remains
is a stateful two-transversal pullback proving `tau_5^{<=6}(G)<=2`, ideally
in a form which proves (U) for an arbitrary minimal branch bag.

The retained exact-seven subroutine is the single-trace reverse tight-lobe
carrier-or-rooted-five theorem stated in
`hc7_reverse_tight_carrier_or_rooted_five_goal.md`.  The former universal
low-demand target was overstrong: seven connected-rich residual boundaries
have absolute packet demand three.

In the reverse actual `(1,2)` cell, contract the packet-one shore together
with a maximum independent boundary set and fix any exact returned state
`Pi`.  Existing audited counting gives `d_H(Pi)<=3`; demand at most two
closes, so the live case for this trace has demand three.  The new theorem
must extract duty-correct carriers reflecting `Pi`, a five-rooted `K_5`
with two reserved packet anchors, a literal/fixed-pair terminal, or a
strictly ranked state-preserving descent.  This is the uniform rooted-model
principle needed by `S3`; it is not a boundary census.

The audited tight-lobe transition supplies the first test cell.  Its
packet analysis is now split-audited: packet-one regeneration and the
five-colour lock/crossing localization are valid, but arbitrary high
demand is not an accepted `S3` state and packet-sum `3 -> 2` is not a
well-founded `S4` rank.  In particular, the reversed vector
`(nu_D,nu_B)=(2,1)` leaves the actual packet-one shore outside the strict
lobe.

The first milestone is therefore to close the symmetric atomic twin seam
now exposed inside that reversed orientation.  Literal two-/three-gate
analysis leaves two five-contact lobes with overlapping actual
seven-boundaries.  The operations `e=zu` and `f=dt` produce crossed exact
states and packet-aligned local handoffs on both boundaries.  The immediate
theorem must turn their double-lock system into a common state, a literal or
fixed-pair terminal, or a genuinely ranked receiver.

The carrier-allocation part now has one exact audited reduction.  The
[reserve-rooted `C_4` exchange](../results/hc7_atomic_twin_seam_reserve_rooted_c4_exchange.md)
shows that an ordinary cyclic model rooted at the two gates and the two old
reserve carriers already closes: literal hubs contradict the residual
packet number, while every nonzero hub stem produces a strictly smaller
actual `(1,2)` seven-separation in the global shore-order rank.  Its
[audit](../results/hc7_atomic_twin_seam_reserve_rooted_c4_exchange_audit.md)
also verifies the named high-demand handoff.

After contracting the two reserves, Robertson--Seymour--Thomas (2.1)
reduces existence of that model exactly to two feasible pairings at the
cyclic roots `p,r_1,q,r_2`.  It may not replace a nonzero stem by a
singleton gate.  The independently audited
[stable-stem barrier](../barriers/hc7_twin_seam_stable_stem_barrier.md)
shows that the full separating bundle or response-matched bypass alone does
not justify that replacement; its examples exit only through the permitted
six-colouring and literal-`K_7` branches.

Directly forcing both pairings is now independently falsified as well.  A
25-vertex shell retains the full packet, crossed-response, equal/equal and
five-rung data; one local RST pairing fails although both labelled pairings
exist globally in the common host.  Its proper/proper colouring and literal
`K_7` show exactly which terminal hypotheses it omits.  Source:
[RST-feasibility localization barrier](../barriers/hc7_twin_seam_rst_feasibility_barrier.md)
and its [audit](../barriers/hc7_twin_seam_rst_feasibility_barrier_audit.md).

The failed branch is nevertheless planar in a literal sense.  The
[failed-RST web planarization](../results/hc7_twin_seam_failed_rst_web_planarization.md)
uses the three web gates and the three omitted common labels to eliminate
every clique-cell interior by a six-cut.  Hence the reserve quotient itself
is planar with the four represented portal classes cofacial.  Its
[audit](../results/hc7_twin_seam_failed_rst_web_planarization_audit.md)
also checks the exact active-face splice: absent an off-face attachment,
Thomassen extension leaves only a nonadjacent heavy pair, at least three
heavy vertices, or one adjacent common-singleton lock.  The last lock
localizes to one facial edge when the active cycle has length at least
four.

This split is sharp.  The audited
[two-apex failed-web barrier](../barriers/hc7_twin_seam_failed_web_two_apex_barrier.md)
is `K_2` joined to the icosahedron.  It is seven-connected,
`K_7`-minor-free and has both a failed four-web and a spanning common-host
`K_6`, but it exits through the fixed apex pair.  The remaining allocation
theorem must therefore combine the planar page with strong critical state
transitions, or detect that coherent pair; an arbitrary spanning model or
global linkage cannot close it.

The unrestricted routing part is now uniform.  In the counterexample host,
deleting the two independent named edges gives one connected graph `H` with
`chi(H)=6` and hence a spanning `K_6` model.  The two one-edge restorations
realize opposite exact edge signatures `(proper,equal)` and
`(equal,proper)`, while `(proper,proper)` is forbidden.  Contracting both
edges supplies a simultaneous `(equal,equal)` colouring in the same host.
The audited `GF(2)` component-switch theorem then gives one shared
three-/four-lock system and four common-host locks for each edge in its
own response.  The live twin-seam step is therefore allocation/confluence
in a common six-row host: make those locks disjoint and label-faithful,
split or reselect the model, force a common boundary state, or produce a
class-ranked exit.

Source: [common edge-deletion chromatic fork and `K_6`
regeneration](../results/hc7_common_edge_deletion_k6_fork.md), with its
[independent audit](../results/hc7_common_edge_deletion_k6_fork_audit.md).
The simultaneous response and lock counts are proved in
[common-host double-contraction lock allocation](../results/hc7_common_host_double_contraction_lock_allocation.md),
with its [audit](../results/hc7_common_host_double_contraction_lock_allocation_audit.md).
For an even induced terminal cycle, the stronger
[whole-cycle parity-lock theorem](../results/hc7_terminal_cycle_contraction_parity_locks.md)
and its [audit](../results/hc7_terminal_cycle_contraction_parity_locks_audit.md)
put at least four external parity-crossing locks into one common colouring.
This removes independent edge-by-edge colour choice from the even-cycle
branch, but does not make the paths disjoint or identify colours with model
rows.  Odd cycles still require a different exchange mechanism.

Accordingly the live failed-pair decoder has four named inputs rather than
another portal census: the literal planar page, the forbidden
proper/proper corner, the two one-edge responses, and the equal/equal
response.  It must turn every off-face/heavy-face residual into a common
exact state, a literal/fixed-pair terminal, or the strict global
`mathcal F_12(G)` handoff.  A result which only refines the planar portal
order is not an admissible successor.

For actual `(1,2)` cells there is one genuine global rank.  Orient every
such cell toward its packet-one shore and choose that shore globally minimum
over all actual order-seven `(1,2)` separations.  A smaller packet-one
receiver is then impossible regardless of state.  This rank is available
only if the upstream reductions apply to that unrestricted global minimum;
it does not extend to `(1,1)` or near-model rotations.

Sources:
`../results/hc7_shortest_thin_lock_tight_bypass_transition.md`,
`hc7_tight_gate_receiver_normalization.md`, its adjacent audit, and
`../barriers/hc7_tight_gate_local_orientation_shell.md`.

The online literature review through 15 July 2026 found no automatic
exchange.  Humeau--Pous gives the relevant constructive crossing/web
decomposition but transports no exact state.  Dvorak--Swart rules out an
abstract extension-language engine, while Kriesell--Mohr can package only a
literal Kempe skeleton after the required connectivity/disjointness has
been proved.  The current knitted threshold is also far above this
exact-seven interface.

## Frozen kernel

For a hypothetical minor-minimal counterexample `G`:

1. `G` is 7-connected, strongly 7-contraction-critical, and
   `K_7`-minor-free.
2. Every proper minor is six-colourable.
3. The known near-clique theorem supplies a `K_7^vee` minor.
4. Every `G-v` and `G/e` is exactly six-chromatic and contains a `K_6`
   minor; every `G-{u,v}` is at least five-chromatic and contains a `K_5`
   minor.  Model regeneration is available, but remains secondary.

No later step may identify a colour with a branch-set label without a
literal contraction or contact argument.

## Active dependency chain

### S1. From a near-`K_7` model to a terminal interface — **OPEN**

The audited normalizations and labelled rotations currently yield one of:

* a literal `K_7` model;
* an actual adhesion of order at least seven with controlled labelled
  carriers/equality states;
* another one- or two-hole near model linked by an exact reversible
  rotation; or
* a coherent fixed two-vertex endgame.

What is still missing is a well-founded composition theorem: an entire
rotation/adhesion component must produce the literal model, a common exact
boundary partition from opposite proper-minor operations, or one fixed pair
for the `K_5`-minor-free endgame.  Reversible rotations alone are not a
descent.

Principal normalization inputs:

* `../results/hc7_near_k7_deficient_path_normalization.md`;
* `../results/hc7_near_k7_coherent_spanning_transport.md`;
* `../results/hc7_near_k7_endpoint_shadow_exchange.md`;
* `../results/hc7_near_k7_rotation_edge.md`;
* `../results/hc7_near_k7_rotation_pair_overlap.md`; and
* `../results/hc7_near_k7_one_hole_height_gap.md`.

One audited local handoff is also available.  A reversed rooted-`K_4`
expansion on the six cross-lobe labels, together with two disjoint
`S`-full packets and the attained paired-triangle boundary state, contains
a literal label-faithful `K_7^vee` model.  The companion width-five example
shows that these static hypotheses do not force `K_7`; the handoff is an
S1 input, not a terminal outcome.  Sources:
`../results/hc7_exact7_cross_lobe_rooted_k4_handoff.md` and
`../barriers/hc7_exact7_rooted_k4_k7_upgrade_barrier.md`.

### S2. Actual adhesions of order seven — **`(1,3)` CLOSED; `(1,1)`, `(1,2)` OPEN**

For an actual seven-boundary `S`, let `nu_i` be the maximum number of
disjoint connected `S`-full packets in open shore `i`.  The audited packet
theorem gives, up to orientation,

\[
                       (\nu_1,\nu_2)\in\{(1,1),(1,2),(1,3)\}.
\]

Source: `../results/hc7_exact_seven_packet_packing.md`.

The new adaptive reflection theorem eliminates `(1,3)` uniformly.  One
thin-side packet contracts with an independent boundary set `I` of order
four, or a maximum one of order three.  This forces `I` as one exact block
of the boundary partition returned by a proper-minor six-colouring.  Three
opposite packets then reproduce the entire returned partition exactly.  A
boundary triangle instead gives a literal `K_7` with the four packets.

Source: `../results/hc7_exact7_adaptive_packet_reflection.md`.

Thus none of the former Moser, sparse-gate, portal-rank, or block-chain
residues is live inside an actual `(1,3)` adhesion.  Those results remain
valid supporting mathematics, not dependencies of the current proof.

### S3. Adaptive `(1,2)` reflection — **PRIMARY EXACT-SEVEN GAP**

Let `H=G[S]`.  For a partition `Pi` of `S` into independent blocks define

\[
 d_H(\Pi)=|\Pi|-\omega\bigl(H[\operatorname{sing}(\Pi)]\bigr).
\]

Two full packets reproduce any exact returned partition with
`d_H(Pi)<=2`.  The lone packet can force one independent set to be an exact
block, but unlike `(1,3)`, this does not ensure demand at most two.

The first uniform closure is now proved and audited.  It eliminates an
actual `(1,2)` adhesion whenever either:

* `H` has an independent block `I` of order at least five, an independent
  four-set with an edge in its complement, or an independent triple with a
  triangle in its complement; or
* deleting two literal anchors from `H` leaves a `K_4` minor.

The first alternative makes every state returned after forcing `I`
reflectable by the two rich packets.  The second gives a literal `K_7` from
three packet bags and four boundary-model bags.  These two mechanisms close
556 of the 685 seven-vertex boundary graphs of clique number at most three.
If the rich shore is
connected, its packets can be made adjacent and the one-anchor condition
`H-x succeq K_4` closes 33 more of the 129 residual types, leaving 96 in
that branch.  Source:
`../results/hc7_exact7_adaptive_12_boundary_closure.md`.

The exact constructive target is therefore state-specific:

> In the reverse actual `(1,2)` cell, force one canonical thin-side
> contraction by a maximum independent boundary set.  If its exact return
> has demand three, turn that same named state into three duty-correct
> carriers, a reserved-anchor five-rooted `K_5`, a literal/fixed-pair
> terminal, or a strictly ranked state-preserving descent.

For the attained paired-triangle state in the connected-rich width-two
frontier, the four-connected thin shore is now closed outright.  For every
four-label portal family, seven-connectivity gives a rank-four transversal
matroid; every literal portal is a nonloop and therefore lies in a basis.
The rooted-`K_4`/common-face dichotomy then gives a labelled `K_7^vee` or a
cofacial curvature contradiction.  No prescribed-edge extension, equality
state pullback, or recursive descent is needed.  The sole local transition
left in this frontier is the support-four lobe of a genuine three-cut; the
general 129-type statement below remains broader and open.  Source:
`../results/hc7_exact7_four_connected_basis_cover_closure.md`.

Naive composition across that three-cut is false even after imposing exact
seven-connectivity, `chi=7`, all local Dirac inequalities, and legal
paired-state attainment: an order-fourteen certificate descends from
`(1,2)` to `(1,1)` and has no compatible paired pullback.  It contains a
literal `K_7` and is not minor-minimal.  Hence the missing positive theorem
must spend `K_7`-minor-freeness or the universal proper-minor response,
rather than more local packet bookkeeping.  Source:
`../barriers/hc7_exact7_threecut_descent_packet_collapse_barrier.md`.

The exact unconditional boundary residue has 129 types.  Of these, 119 have
a combinatorially safe partition which has not yet been forced by a legal
shore operation; ten have no demand-at-most-two partition at all, and all
ten contain two disjoint boundary triangles.  In the connected-rich branch
the one-anchor lift reduces the residue to 96 and the absolute-demand-three
part to seven.  These finite counts locate the interface but are not the
proof mechanism.  The live theorem must be a two-carrier exchange in the
thin shore, with a web/separator certificate when the exchange fails.

The packet-demand identity

\[
 \min_\Pi d_H(\Pi)
 =\min\{\chi(H-U):H[U]\text{ is a clique}\}
\]

is now independently audited.  Hence the 119 safe-state residuals are
exactly those with a clique odd-cycle transversal.  The constructive target
is therefore “force a clique-OCT state,” not “search 119 partitions.”  The
identity does not itself realize that state by a legal shore operation.
Source: `../results/hc7_exact7_packet_demand_identity.md`.

Two hygiene constraints are binding here.  First, failure to attain a
clique-OCT state, even together with failure of one generic carrier
construction, does **not** reduce the whole `(1,2)` cell to Moser; the Moser
reduction below is confined to the singleton-thin, `alpha(H)<=2` cell.
Second, carrier sufficiency is relative to the partition actually returned.
The correct datum is its attained duty `D_U(B)`: which block and retained
singleton adjacencies that particular carrier must fund.  More precisely,
if `C` is the retained singleton clique of an attained partition `Pi`, put

\[
 D_{\Pi,C}(B)=B\cup\{c\in C:N_H(c)\cap B=\varnothing\}.
\]

A connected carrier `T` disjoint from the two full packets funds `B` when
`D_{\Pi,C}(B) subseteq N_S(T)`.  A bound such as
“defect at most two” is only a proved sufficient surrogate in the audited
hard-boundary normalizations where the forced block was chosen from that
defect; it is not a state-independent carrier criterion.

The first state-specific geometric exchange is now proved.  In either full
packet, choose duty-specific portals for the three attained duties and a
tree containing them.  If two duty hulls are disjoint, cutting their joining
path gives two adjacent duty-correct carriers; the other full packet funds
the third block, so the exact state reflects.  Otherwise the three hulls
have a literal Helly gate.  This conclusion is valid for every witness
selection, but the gate need not be canonical.

A generic gate bypass does not force a split.  The sharp private two-portal
cycle obstruction has cyclic order `A B D A B D`: every packet tree has a
bypassed common gate while no pair of duty-correct carriers is disjoint.
Every other private two-portal cyclic order does split.  Thus the live
uniform mechanism is a label-compatible bypass-or-web theorem followed by a
web-to-adhesion/state-gluing step using the second packet and criticality.
Sources: `../results/hc7_exact7_attained_duty_tree_gate.md` and
`../barriers/hc7_exact7_gate_bypass_falsifier.md`.

The selected-gate quantifier is now removed for each fixed packet spanning
tree.  Apply the Aharoni--Berger--Ziv point--tree theorem to the three
families of all attainable duty hulls.  Nonreflection makes those families
cross-intersecting, so one attainable hull meets every attainable hull.
Minimizing inside it gives either one literal vertex common to all three
families, or one exceptional duty with pairwise disjoint leaf witnesses
around a core contained in every hull of the other two duties.  This core
can still change with the spanning tree and need not meet carriers using
non-tree edges; the live descent must use endpoint-preserving augmentation
or state transitions to make it tree-invariant or expose an adhesion.
Source: `../results/hc7_exact7_point_tree_gate_core.md`.

Pap's permutation-labelled non-returning-path theorem remains a guarded
backup, not a proved lift.  The current rotations form a groupoid of partial
state-dependent moves: state vertices preserve legality but lose literal
disjointness, while resource vertices preserve disjointness but do not carry
one total permutation action.  Perfect--Pym endpoint augmentation does not
repair that label defect.  Source:
`../barriers/hc7_exact7_permutation_path_encoding_gap.md`.

The first two-packet web composition is now proved for an attained
paired-triangle state.  If both full packets contain cycles through the six
selected duty portals, a clean path joining nonhomologous portals splits the
two cycles into three disjoint duty carriers.  Two representative
adjacencies come from literal cycle edges and the third is the precisely
named boundary block edge required for that offset, so the attained state
reflects.  Under portal-pure attachments, every complementary component
meeting both cycles has at least three attachments and therefore closes;
the only surviving cross-cycle interface is a submatching of homologous
portal classes.  The theorem is an unbounded web-exchange result, but it
does not turn that coherent matching cylinder into a separator or a global
state.  Source:
`../results/hc7_exact7_two_packet_cyclic_web_exchange.md`.

The coherent cyclic residue is itself impossible in the pure-Moser state.
If both disjoint full packets contain the exceptional literal portal cycle
`2,4,5,3,1,0`, any third disjoint full packet completes a literal `K_7`.
Six gap-avoiding models lift along a clean first-hit path from boundary
literal `6` to either cycle, so no rung, common rich component, or on-cycle
seventh portal is required.  The remaining structural gap is now to extract
such a literal cycle from an arbitrary alternating duty web, or turn its
failure into an actual adhesion/state-gluing certificate.  Source:
`../results/hc7_exact7_moser_cyclic_packet_completion.md`.

That extraction is now uniform for a 4-connected packet with three binary
attained duties.  Pairwise failure of the three two-duty linkages puts all
six portals on one facial cycle in order `A B D A B D`.  If a whole shore
component is not 4-connected, an internal gate of order at most three has
lobe support at least `7-r`.  In the paired-triangle attained state, a
dutyless three-gate lobe has exactly the singleton `c` and one literal from
each duty in its boundary support.  Adjoining the three gate vertices gives
its literal neighbourhood of order seven, hence a strictly smaller actual
exact-seven adhesion.  This descent may change both the returned state and
the packet vector, so it does not yet terminate S3.  Source:
`../results/hc7_exact7_binary_duty_cycle_or_gate.md`.

The packet vector can nevertheless be recovered in every nondegenerate gate
exit system.  For a dutyless lobe `K`, every sibling lobe is either already
full to the new boundary or has a nonempty exit set in the three discarded
old-boundary vertices.  Two self-full siblings, a self-full sibling plus any
other sibling, or two siblings with distinct exit representatives combine
literally with the two old full packets to give two disjoint full packets on
the new opposite shore.  The packet theorem then orients the descendant as
`(1,2)` or `(1,3)`, with `K` thin, and adaptive reflection closes `(1,3)`.
The exact residuals are:

1. one sibling lobe, with no further exit restriction; or
2. at least two non-self-full siblings whose exit sets are all the same
   singleton.

Source: `../results/hc7_exact7_three_gate_exit_matching.md`.

The second residue is now closed in the attained paired-triangle setting.
Every common-exit sibling has exactly one missing retained label.  The old
rich component is `S`-full, while none of its lobes sees the other two
discarded labels, so those labels have literal contacts in the three-gate.
Three siblings give explicit `K_7` bags or a new exact `(1,3)` cell.  For
exactly two siblings, contract the two old full packets and the three lobes.
The resulting fixed fifteen-vertex quotient contains a literal `K_7` for
every paired-triangle boundary and every placement of the two forced gate
contacts.  A frozen solver-free catalogue covers the essential
`11,520+13,824` two-sibling cases with 37 monotone branch-set templates;
an independent implementation replayed every certificate.  Source:
`../results/hc7_exact7_common_exit_gate_closure.md`.

No exact equality state has been transported.  A verified 14-vertex,
seven-connected local architecture satisfies the old `(1,2)` packet data,
legal paired-triangle attainment, and the dutyless gate trace while every
old-support/gate pair is an edge.  It therefore rules out deriving the
proposed three paired blocks from the audited local hypotheses alone.  The
host is six-colourable, so it is a barrier to that inference rather than an
`HC_7` counterexample.  Source:
`../barriers/hc7_exact7_three_gate_pullback_matching_barrier.md`.

The **one-sibling** gate has an exact Hall-and-duty
normal form.  Write `A={c,a_1,a_2,a_3}` for the dutyless lobe support,
`T={t_1,t_2,t_3}`, and `B=N_S(J)` for the sibling support.  Boundary
labels in `T-B` have a matching into the literal three-gate: Hall failure
would give the separator

\[
              (S-U)\cup N_X(U)
\]

of order below seven.  Distinct gate representatives give two adjacent
duty-correct carriers and reflect the attained state.  Consequently every
nonreflecting one-sibling gate lies in exactly one of:

1. `T subseteq B`; or
2. after permuting duties, `B={c,a_1,t_2,t_3}`, with all possible
   second-duty gate completions either absent or concentrated at one gate.

Source: `../results/hc7_exact7_one_sibling_gate_funnel.md`.

The first family is now closed uniformly.  Pairwise failure of two original
duty carriers lets the generalized Two Paths Theorem place each pair of
duty stars on a web page.  Seven-connectivity removes every clique cell,
and nonadjacent opposite-lobe witnesses plus Whitney uniqueness force all
six complete literal portal sets onto one common face.  The component has
order at least six; a Hall cut then gives six distinct representatives, and
nonreflection forces their cyclic duty word to be

\[
                         A\ B\ D\ A\ B\ D.
\]

On that literal cycle, failure of any two disjoint duty carriers confines
each portal set to its selected sector.  Each of the six adjacent portal-set
pairs overlaps in at most one vertex, so the total six-label incidence is at
most `|F|+6`.  Planar Euler curvature and minimum degree seven force at
least `2|F|+6`, a contradiction.  Hence the attained state reflects.  This
closes arbitrary portal multiplicities and both rooted-expansion and
parallel-strip outcomes without transporting a new equality state.
Sources: `../results/hc7_exact7_cross_lobe_common_face.md` and
`../results/hc7_exact7_cross_lobe_curvature_exchange.md`.

The second family is now closed as well.  Pairwise artificial-terminal
pages require no opposite-lobe witness.  Duties `2,3` each have a
nonadjacent portal pair across `K,J`, and these two pairs identify all three
facial pages by Whitney uniqueness.  One face therefore contains every
portal of all six non-`c` labels, including the complete gate-supported
first-duty stars.  The order-five case is excluded by outerplanarity or
minimum degree; Hall gives six distinct representatives for larger `C`,
and the same facial-incidence/curvature contradiction reflects the state.
Thus isolated and concentrated gate contacts both close.  Source:
`../results/hc7_exact7_single_missing_curvature_exchange.md`.

A stronger uniform theorem now subsumes both one-sibling closures and every
other paired-state gate analysis whenever the geometric object is a whole
three-connected rich component.  Let

\[
 \Pi=\{\{a_1,t_1\},\{a_2,t_2\},\{a_3,t_3\},\{c\}\}
\]

be a legally attained state with the named inter-block and `c` adjacencies.
If the rich shore contains a three-connected `S`-full component `C` and a
disjoint connected `S`-full packet `Q`, then `Pi` reflects, for every order
and every portal distribution.  A four-label Hall separator makes at least
two duties have distinct nonadjacent portal witnesses.  The two-witness
common-face theorem places all six complete portal stars on one face.
Orders four and five contradict outerplanarity or minimum degree; at larger
order a six-label SDR has cyclic word `A B D A B D`, and the facial
incidence upper bound `|F|+6` contradicts the curvature lower bound
`2|F|+6`.  Source:
`../results/hc7_exact7_uniform_paired_curvature_reflection.md`.

Consequently the old one-sibling and common-exit taxonomies are no longer
the active paired-state component problem.  The live obstruction lies
outside the new theorem's hypotheses: two full packets can be interlaced in
one connected rich component, or a full component can have a low-order
internal decomposition.  External packet bridges then create exits that
invalidate the common-face cell cut.  The next exact implication is one
state-preserving packet-extraction/composition theorem: reflect directly,
extract a whole three-connected full component disjoint from another full
packet, or return a label-faithful near-`K_7`/fixed-pair certificate.  Any
recursive adhesion outcome must transport a legal exact state and decrease
a declared rooted measure.

The demand-three residue now has one common exact endgame.  For each of its
ten boundary types an audited independent block forces every returned state
to have demand exactly three.  If, after the return is known, the rich shore
contains one partial carrier disjoint from its two full packets and contacting
the third unfunded block plus the retained singleton clique, the three
contracted representatives reproduce that exact state and the colourings
glue.  This discharges the state-transfer step once the carrier exists.

On the thin side, two adjacent connected carriers of defect at most one
force their defect set to meet every boundary triangle.  With two disjoint
triangles, every non-`K_7` instance is funnelled to two distinct pure defects
in opposite triangles.  The Moser spindle has no such pure triangle vertex;
hence a nonsingleton Moser thin shore has no cutvertex and is not of order
two.  Its singleton case is terminal by the next theorem.  Source:
`../results/hc7_exact7_double_triangle_partial_packet_exchange.md`.

For a singleton thin shore `{q}`, the frozen 129-boundary census reduces the
cell to `M` and `M+13`: Dirac gives `alpha(G[S])<=2`, and these are exactly
the two alpha-two residual orbits.  Contracting the star `q union {2,5}`
forces an exact `25` trace and hence a literal bichromatic `4-6` path with
interior in the rich shore.  If this path avoids both rich full packets,
seven explicit bags give `K_7`.  Otherwise truncate at its first packet hit:
the hit packet, the other full packet, and five anchored bags give a literal
`K_7^-`, hence a labelled `K_7^vee`.  This uses only edges common to `M` and
`M+13`, assumes no packet-packet edge, and closes the entire singleton-thin
residual as an `S1` handoff.  Source:
`../results/hc7_exact7_singleton_thin_near_model_closure.md`.

Thus the named constructive substep in S3 is:

> Stabilize the bridges of an extremal pair of full packets while preserving
> the attained labels.  Either expose two duty-correct carriers and reflect,
> isolate a whole three-connected full component so the uniform curvature
> theorem applies, or return a labelled near-`K_7`/fixed-pair certificate.
> A descended adhesion is useful only with a legally transported exact state
> and a strict rooted descent.

For an arbitrary demand-three state, this remains the more general task of
extracting a carrier which discharges its exact duty `D_U(B)`.  Static
contact or defect counts alone cannot do so.

One infinite subfamily now supplies that carrier.  If the rich shore has
two components and one has a cutvertex, split that component at the
cutvertex into two adjacent near-full carriers and use the other component
as the full third carrier.  An audited adaptive boundary theorem chooses the
thin forced block after the two defects are known but before the proper-minor
colouring is returned, and reflects every possible return.  Therefore both
components of a surviving two-component rich shore are cutvertex-free.
Source: `../results/hc7_exact7_rich_cutpacket_exchange.md`.

The singleton component is now also eliminated inside the frozen
129-boundary residual.  Reorienting at it produces a degree-seven vertex
with exactly two exterior components, because the opposite packet number is
one.  Dirac and the audited residual extraction leave only `M` and `M+13`;
the complete pure-Moser two-component theorem closes the first, and a direct
two-anchor exact-state gluing closes the second.  Source:
`../results/hc7_exact7_two_component_singleton_closure.md`.

A uniform multishore synchronization theorem now closes a further infinite
branch without choosing the returned colouring in advance.  If one
component supplies adjacent labelled carriers for independent blocks `I,J`
and the residual boundary is a three-set containing an edge, two other full
components first produce an actual exact state.  A third full component and
the same two labelled carriers then reproduce that state separately on
every component side, after which palettes align and glue.  Its duty-aware
form records precisely which retained singletons each carrier representative
must see.

For the complementary two-lobe lock

```
Delta(X)={a1,a2}=:P,    Delta(Y)={t1,t2}=:T,
```

this proves that `P,T` cannot both be independent.  If `P` is an edge and
`T` is independent, put `D=N_H(T) cap P`; every survivor satisfies
`|D|<=1`, and if `D={p}` then `cp` is absent.  The symmetric statement holds
with `P,T` exchanged.  Source:
`../results/hc7_exact7_multishore_state_synchronization.md`.

Thus the precise two-component residue is a nonsingleton cutvertex-free
complementary lock with at least one edged defect pair, sparse cross-duty
contact as above, and the previously forced Kempe-component locks.  Static
boundary-and-lobe data with only one full packet do not close it, but the
actual `(1,2)` cell has a second full packet on the old thin shore.  Using
that packet is decisive: the two lobes, the two full packets joined to
`B_1,B_2`, and `c,B_3` form a spanning labelled `K_7^vee` model whose two
possible missing spokes share a singleton centre.  The audited near-model
trichotomies then output `K_7`, an actual separator, or a proper-bag
deficiency rotation.  Source:
`../results/hc7_exact7_complementary_lock_near_k7_handoff.md`.

Hence the complementary lock is closed as an `S3` transition and must not
receive further portal casework.  The connected-rich case and the global
`S1` rotation/adhesion composition remain open.

The first `S1` move from this handoff now preserves more literal state than
an arbitrary near-model rotation.  In the no-`K_7^-` branch, a rotation
through either packet donor moves exactly one of its two boundary anchors.
The resulting seven bags form a literal `K_3 join C_4`; its two independent
missing diagonals are the moved-anchor row and one old missing twin.  A move
which changes the missing twin to `c` is locked in a named three-terminal
Kempe component, since otherwise a swap returns an exact four-block state
with literal rich-side `K_4` representatives and glues.  This confines the
local holonomy but does not yet orient or terminate successive one-anchor
moves.  Source:
`../results/hc7_exact7_packet_donor_rotation_lock.md`.

The whole two-component paired-state family is now independently audited
as one concise trichotomy.  A cutvertex or a component of order two or
three reflects; a three-connected component reflects by uniform curvature;
and every remaining two-cut either has two distinct available duties or
has complementary defects which give the spanning `K_7^vee` above.  No
exact two-lobe, Kempe-trace, or finite-boundary continuation remains in this
branch.  Source:
`../results/hc7_exact7_two_component_paired_trichotomy.md`.

The connected-rich branch now also has a label-free static exit.  Make the
two rich full packets adjacent along a shortest rich-shore path.  If the
literal boundary has a connected set `D` of order one or two which
dominates a disjoint three-set `T` containing an edge, the three full
packets, `D`, and the three singleton vertices of `T` form a labelled
`K_7^vee`.  This is an unbounded handoff: it ignores all packet interiors
and portal multiplicities.  A surviving connected-rich boundary must fail
this small connected-core condition and still requires the dynamic
packet/state exchange; the theorem does not by itself compose the returned
near model.  Source:
`../results/hc7_exact7_three_packet_boundary_core_handoff.md`.

The entire connected-rich paired-state quotient is now exact.  With the
thin full packet and an adjacent full cover `P,Q` of the rich shore, a
three-packet `K_7^vee` exists exactly when the boundary has a `K_4` minor or
some one-vertex deletion has a triangle-with-pendant minor.  Otherwise the
paired boundary is a tree, a six-cycle with one leaf, or
`K_{1,3} dotcup K_3`, hence has treewidth at most two and a clique
odd-cycle transversal of order at most one.

This classification also closes every thin cutvertex.  A duty-faithful
split returns the boundary bipartition state on both sides and glues; the
only apparent two-lobe same-duty lock instead has an explicit seven-bag
`K_7^vee` model.  Thus the live paired connected-rich geometry is a
cutvertex-free thin packet over the width-two frontier.  Source:
`../results/hc7_exact7_connected_rich_width2_frontier.md`.

The literal adhesion and Dirac's critical-neighbourhood inequality now close
every vertex of thin-shore internal degree at most three whose deletion leaves
the shore connected.  Therefore the surviving cutvertex-free thin shore has
internal minimum degree at least four.  The same packing mechanism, without
Dirac, closes every two-cut with at least three lobes, so every surviving
two-cut has exactly two lobes.  Source:
`../results/hc7_exact7_low_internal_degree_handoff.md`.

The binary two-cut is now closed too.  Anchor its two lobes at opposite gate
vertices.  Seven-connectivity gives each resulting adjacent carrier support
at least five, and their supports cover `S`.  A repairable-incidence lemma
for every width-two frontier boundary then produces seven literal bags
forming a labelled `K_7^vee`.  Hence the live thin shore is three-connected
and still has internal minimum degree at least four.  Source:
`../results/hc7_exact7_binary_gate_near_model.md`.

Two label-free tools control the three-connected block.  First, no
three-label common portal core can contain a `K_4` model in a `K_7`-free
host, and a third boundary literal can trace at most one bag of any `K_4`
model in a two-label core unless a labelled `K_7^vee` already exists.
Second, a prescribed portal edge for at most four labels either extends to
a saturating literal matching or a tight Hall witness returns the exact
smaller boundary

\[
                       \Omega=(S-U)\cup N_L(U),
       \qquad |U|=|N_L(U)|\le3.
\]

In the four-connected branch the new shore is connected, full and strictly
smaller.  Sources:
`../results/hc7_exact7_common_portal_core_obstruction.md` and
`../results/hc7_exact7_prescribed_portal_extension_or_adhesion.md`.

The rest of the thin geometry is now exhausted as a transition.  At a
three-cut `T`, every lobe meets all three gates and at least four old
boundary labels.  Support four gives the strict full descent
`Omega=T union N_S(D)`.  If every lobe has support at least five, the lobes
and gates partition into two adjacent near-full carriers; the binary-gate
near-model theorem gives `K_7^vee`.  With no three-cut the shore is
four-connected.  For each four-label portal family containing two fixed
neighbours of `c`, either a rooted `K_4` gives a labelled `K_7^vee`, or all
complete portal sets lie on one face.  The overlapping four-label families
synchronize those faces.  Disk curvature then gives an off-face vertex of
total degree at most six, contradicting seven-connectivity.  Sources:
`../results/hc7_exact7_three_cut_portal_descent.md`,
`../results/hc7_exact7_cofacial_portal_degree_obstruction.md`, and
`../results/hc7_exact7_four_connected_portal_exchange.md`.

Thus the paired connected-rich width-two geometry has only two outputs:
a labelled near model, or a strictly smaller literal full seven-adhesion.
Within this paired connected-rich width-two subbranch, the remaining gap is
exact-state descent composition: transport the attained paired duties or a
demand-at-most-two return across either displayed boundary map, or turn a
changed packet vector into the global S1/fixed-pair handoff.  No current
theorem transports the old equality state through the descent, and
packet-vector preservation can still fail in the two-lobe matching
obstruction.

The support-four three-cut now has a stronger state-free capacity theorem.
Give every lobe and gate its literal support in `S`; two disjoint capacity
edges partition the shore into adjacent connected near-full carriers and
force a labelled `K_7^vee`.  Exit matching then proves that every gate with
at least three lobes gives that handoff or a strict packet-vector `(1,2)`
descendant.  With two lobes, matching number one has only lobe-centred star
or triangle support form: the gate-centred star would expose the five-cut
`A union {t}`.  The exact remaining obligations are legal state selection
at the strict descendant and, in the two-lobe resource, a label-faithful
proper-row split or singleton-lobe exit.  The non-singleton full-row
resource is closed.  Source:
`../results/hc7_exact7_threecut_capacity_transition.md`.

The first adaptive state-selection step is now uniform in `k`.  If one
shore has `q` disjoint full packets and the other has `q` pairwise adjacent
connected carriers, it is enough to assign each carrier a nonempty
independent seed set whose complement on the boundary is a clique.  Contract
only the carriers with their seeds.  Whatever the proper-minor colouring
does to the clique reservoir, the exact returned partition has packet demand
at most `q`; the opposite packets reproduce that actual state and the two
colourings glue.  No carrier-to-reservoir contact and no prescribed exact
state are required.  At `q=2` this closes every lobe/gate allocation with a
clique-reservoir seed partition.  A paired width-two tree shows that the
static lobe supports need not supply one, so the remaining theorem is now a
literal interior split/rerouting theorem, not a palette-selection theorem.
Source: `../results/hc7_uniform_adaptive_clique_reservoir_return.md`.

The non-singleton support-four lobe has a literal portal peel.  For
`N_G(D)=T dotunion A`, `|T|=3`, `|A|=4`, seven-connectivity gives a
removable `A`-portal `x` such that `D-x` is connected and still meets `T`.
Either `x` has a proper nonempty row in `A`, or both `{x}` and `D-x` retain
the full row `A`.  With the second lobe, the full-row outcome gives adjacent
carriers which are `A`-full and `S`-full; the adaptive theorem then closes
all three width-two frontiers.  Hence the two-lobe branch no longer needs an
unlabelled peel: its exact residue is a labelled proper-row split satisfying
the selected two seed duties, plus the separate singleton-lobe cell.
Source: `../results/hc7_exact7_support_four_literal_portal_peel.md`.

The prescribed-portal Hall descent now has an exact packet classification.
Write `U` for the inclusion-minimal deficient old-label set and
`X=N_L(U)` for the equally sized new gate set.  Either two disjoint
`X`-dominating traces in `U` pull the old adjacent packets through to the
new boundary, the unique alternating `C_6` incidence gives a labelled
`K_7^vee` through the prescribed edge, or one gate `z` has a unique
neighbour `u_* in U` and every new full packet contains `u_*`.  Hence the
Hall branch now has only one canonical packet-collapse interface, rather
than an arbitrary `(1,1)` transition.  Source:
`../results/hc7_exact7_hall_descent_packet_classification.md`.

That compulsory interface now composes down to one atom.  Minimal Hall
traces partition `U` so that the old packets and the new lobe form three
`W`-full carriers with exact adjacency path `A-B_1-B_2`, where `|W|=6`.
A `K_4` minor in `G[W]` gives a literal `K_7^-`.  The twin boundary
`W union {u_*}` is an actual exact-seven boundary and strictly decreases
the active shore for `|U|=2,3`.  Thus only `|U|=1` is nondecreasing.  Its
surviving six-core is `K_4`-minor-free, has no required portal-rooted
triangle, and carries five exact Kempe locks for the sole bridge `zu_*`.
The saturated bridge fan roots `K_2 join G[W]`, but the bridge ends need
not be the global fixed pair; the composition note includes a sharp
`K_2`-join falsifier.  Source:
`../results/hc7_compulsory_portal_bridge_composition.md`.

The atomic state is now compressed to one literal path obstruction.  Use
the width-two partition `S=I dotunion J dotunion K`, with `I,J`
independent, `u_* in I`, and `K` empty or a singleton clique.  Contracting
the thin shore with `I` returns an exact `I`-trace.  Block-Kempe exchanges
either merge all `J` blocks (and detach `K`) to obtain the demand-at-most-
two state `I|J` or `I|J|{k}`, which reflects and glues, or produce a
bichromatic path in the rich shore between two named `J` blocks or from
`k` to `J`.  The live implication is not path existence but state-faithful
packet escape: the path may intersect both full packets, and contracting it
does not preserve the independently produced `I`-trace.  Source:
`../results/hc7_compulsory_portal_atomic_state_exchange.md`.

Two audited refinements now make that obstruction exact.  First, two named
adjacent thin-side carriers synchronize precisely when their literal contact
lists properly two-colour the width-two frontier; in the connected bipartite
case the only obstruction is one component-orientation bit.  The
clique-reservoir duty is automatic in both atomic frontier forms.  Thus a
legal carrier-piece reassignment closes exactly when its affected portal set
repairs the conflicting bit.  Source:
`../results/hc7_exact7_two_carrier_list_obstruction.md`.

Second, the smallest four-vertex rich packet path has been classified over
all 8,192 trace-legal edge extensions.  A blocking path can genuinely traverse
both packets without giving an escape or near model, but every extension of
that frozen architecture either has `K_7^vee` or retains the canonical
fixed-pair terminal.  Under the current strict terminal list this does not
remove the architecture: three singleton near-model triggers do not certify
the canonical pair, and no decreasing normalized S1 handoff is known.  The
classification is retained as a finite laboratory rather than a closure.
Source:
`../results/hc7_atomic_four_vertex_packet_path_classification.md`.

The current constructive checkpoint supplies independently attained blocking
paths on both bipartition duties.  The raw commuting-contraction comparison
does not align their states, but two literal couplings now sharpen the atom.

For disjoint `e=zu_*` and a rich edge `f=xy`, every colouring of `G/e/f`
satisfies a boundary-preserving saturation fork: literal `z` sees all five
alternative colours, or both literal rich endpoints do.  At a leaf of a
selected path/`Y` core, the rich branch forces five boundary contacts, a
chord, or an off-core bridge attachment.

For a final two-duty bichromatic trace, every separating edge (including a
boundary--rich edge) localizes the compressed demand-at-most-two state to
one colouring of `G-f`.  All five `f`-locks coexist there, and the old-colour
lock necessarily contains a literal connector between the two named duty
blocks whose internal vertices lie in the thin shore.  If no edge separates
the blocks, two edge-disjoint rich-side routes exist.

The compulsory edge now has a state-faithful composition whenever one of
its own five locks has a rich-internal or boundary--rich separating bridge
`f`.  Swapping the `z`-side of that same lock gives a named colouring of
`G-f` and `G/f`.  On the twin boundary

\[
                    \Omega=(S-\{u\})\cup\{z\},
\]

the shores `A-z` and `R union {u}` are connected and full.  Every full
packet on the latter contains `u`.  Two full packets on `A-z` would, after
adjoining `z` to one, be the audited adjacent old-boundary carriers of
supports seven and six; hence that branch already six-colours `G` or gives
`K_7`.  The twin packet vector is therefore exactly `(1,1)`.  The named
`f`-contraction legally attains the literal root-substitution state
`u -> z`, its demand is at least two, and packet sum drops `3 -> 2`.

This is a normalized labelled entry into `S4`, not a solution of `S4`.
For each alternate `f`-colour, the receiver additionally has either an
internal right-shore lock or a literal boundary-to-boundary crossing through
the left shore; otherwise the exact traces reproduce and glue.  Thus the
only compulsory-lock residue remaining locally is that every one of the
five locks, in every `G-zu` colouring, has no rich-internal or
boundary--rich separating bridge.  No vertex-disjointness is inferred.
Sources: `../results/hc7_compulsory_edge_lock_state_lift.md` and
`../results/hc7_compulsory_lock_twin_state_transfer.md`.

In one fixed residual colouring, contract every component of a lock outside
the rich shore and retain parallel rich edges.  The audited quotient theorem
then gives, for each alternate colour, either a literal thin `z-u` path or
two edge-disjoint rich-edge source--target routes.  Systems for distinct
colours use disjoint retained rich edges.  They may share arbitrary
`alpha`-coloured articulation vertices, so edge-Menger does not supply the
needed vertex-disjoint bags.  A thin lock forces a distinct rainbow
boundary neighbour of `u`; five thin locks force the exact `2+5`
bipartition and a six-block trace.  Source:
`../results/hc7_compulsory_lock_rich_quotient_two_routes.md`.

There is now a uniform root normalization.  In every nonsingleton atom,
`A-z` is connected and meets all six literals of `W=S-{u}`.  A geometric
duty connector can therefore avoid `z`; retaining that path and adjoining a
shortest `z`-tail gives a path or subdivided `Y` with `z` as a leaf.  Every
component `D` outside the core satisfies

\[
                    |N_T(D)|+|N_S(D)|\ge7,
\]

and equality gives an actual exact-seven boundary.  The replacement
connector need not be bichromatic and no equality state is automatically
transported.

The audited near-full carrier exchange now closes every clean core edge and
proves that every nonsingleton atomic shore is two-connected.  Its named
contractions manufacture a fresh demand-at-most-two state, so the hard
branch no longer needs a state pullback.  Two further audited lemmas close
all connected-bipartite atoms with `d_{G[A]}(z)<=2` and every bare cycle
shore `C_n`, `n>=4`.

At the first uncovered order, exact rooted enumeration is also terminal.
For `|A|=4`, both possible rooted thin graphs and all 19 rooted paired
frontiers were tested symbolically against every literal contact map
satisfying the complete relative seven-cut system.  Negating every adaptive
carrier return is unsatisfiable in all 38 cells.  This is a bounded audited
lemma only; no larger-order induction is inferred.  Source:
`../results/hc7_atomic_order_four_carrier_exhaustion.md`.

The corrected order-five guardrail likewise tests all 14 rooted
biconnected thin types and 19 rooted paired frontiers, for 266 symbolic
cells over the full `2^30` contact space.  Every cell is unsatisfiable.
The first possible atomic obstruction therefore has order at least six.
This is a bounded falsification certificate only and the census stops
there.  Source: `../results/hc7_atomic_order_five_carrier_guardrail.md`.

The list-theoretic part of the next theorem is now closed.  At the canonical
split `{z}|(A-z)`, failure of every adaptive empty/singleton reservoir gives
two vertex-disjoint parity-bad boundary paths by set-Menger.  Their four
endpoints are distinct literal roots, and seven-connectivity supplies a
four-portal matching.  The audited four-port theorem returns literal
disjoint linkage paths through `A` or a literal rural disk.

The rural half is now reduced to one exact direct-reserve cell.  A
nontrivial leftover boundary connector already gives labelled `K_7^vee`;
in the last cell a reoriented seven-separation regenerates a rooted
`K_4^-` with one root replaced by `z`.  The exact rooted-`K_4` obstruction
theorem eliminates five obstruction classes and every hidden fill clique:
failure of the upgrade is a literal clean cofacial web.  The active child
must decode that web into an anchored five-bag certificate, adaptive
carriers, or an exact receiving adhesion.

The adaptive carrier half has advanced uniformly.  Any connected split
`A=X dotunion Y` with `z` on the six-contact side and support at least
`(5,6)` six-colours `G`.  Since the shore is already two-connected, this
forces `delta(G[A])>=3` and eliminates the entire outerplanar rural family.
For a nonroot degree-three vertex, the same argument either closes or gives
the literal receiver boundary

\[
                  \Omega_v=\{v\}\cup(S-\{q\})=N_G(A-v)
\]

and the named contraction `qv`, whose minor colouring induces an exact
state on the intact closed `A-v` side.  This is only a one-sided receiver:
it supplies no packet vector, reflection, or global descent rank.

The literal gate geometry is now uniform.  Every two-gate either closes by
the unordered `(5,6)` theorem or yields a twin seam with two five-contact
lobes and support intersection three.  Every three-gate either exposes an
actual support-four receiver, reduces to that twin seam, or gives its
three-gate `K_{2,3}` version.  Completion edges are not used.

On the twin seam, `e=zu` and each lobe-gate contraction `f=dt` return
different exact states on both overlapping actual seven-boundaries.  The
four strict demand inequalities give a packet-aligned named local handoff.
If `f` separates a compulsory Kempe lock, one swap gives two simultaneous
literal `t`-rooted mismatch paths through the same edge.  The paths need not
otherwise be disjoint.

The immediate rural child is therefore the
[twin-seam double-lock exchange](hc7_atomic_twin_seam_double_lock_exchange_goal.md).
It must decode the separating-edge paths into carriers/model/ranked state
and resolve the complementary gate-edge-bypass branch.  Bare alignment on
the common five-set is false even for a `K_7`-minor-free, `K`-clean shell;
that shell has the permitted rooted `K_5`, so the correct target is
alignment **or terminal model**.
Completion edges are not host edges and no palette colour may be promoted
to a branch label.  Sources:
`hc7_atomic_blocking_path_packet_escape.md`,
`../results/hc7_atomic_double_contraction_state_split.md`, and
`../results/hc7_atomic_bichromatic_bridge_state_localization.md`,
`../results/hc7_atomic_root_deletion_normalization.md`, and
`../results/hc7_atomic_near_full_two_carrier_exchange.md`,
`../results/hc7_atomic_low_root_degree_closure.md`,
`../results/hc7_atomic_cycle_shore_closure.md`,
`../results/hc7_two_list_reservoir_menger_dichotomy.md`,
`../results/hc7_closed_shore_rooted_connectivity.md`,
`../results/hc7_rural_reserved_connector_near_k7.md`,
`../results/hc7_direct_reserve_one_root_substitution.md`,
`../results/hc7_direct_reserve_rooted_k4_obstruction.md`, and
`../results/hc7_atomic_asymmetric_56_carrier_closure.md`,
`../results/hc7_atomic_degree_three_receiver_peel.md`, and
`../results/hc7_atomic_literal_two_gate_transition.md`,
`../results/hc7_atomic_literal_three_gate_normal_form.md`,
`../results/hc7_atomic_twin_seam_crossed_states.md`,
`../results/hc7_atomic_twin_seam_separating_gate_bridge.md`,
`hc7_atomic_twin_seam_double_lock_exchange_goal.md`, and
`hc7_atomic_connector_tree_bridge_audit.md`.

In the separate two-lobe proper-row branch, an exact bounded falsifier found
no seven-connected nonpeel instance among dense lobes or every eligible
thin atlas skeleton through seven vertices.  Its useful invariant is the
uncrossing of four literal mixed-terminal separators into a six-cut, unless
their crossing gives a labelled near model.  This remains a candidate
unbounded theorem, not a promoted closure.  Source:
`hc7_two_lobe_peel_or_six_cut_probe.md`.

The frontier has at least fourteen surplus packet contacts, but that count
cannot be used as a static splitting theorem.  A verified 18-vertex graph
has exact seven-connectivity, minimum degree seven, packet vector `(1,2)`,
thirty-nine surplus contacts, and all local Dirac inequalities, yet no
disjoint carriers funding the two duties.  It contains a literal `K_7`, so
the positive theorem must use `K_7`-minor-freeness or a genuine proper-minor
state transition.  Source:
`../barriers/hc7_exact7_width2_surplus_thin_split_barrier.md`.

`K_7`-minor-freeness plus all thin-side degree and cut-expansion inequalities
is also insufficient.  A verified twelve-vertex width-two graph has no duty
split and no `K_7` minor, although every nonempty thin subset has boundary at
least seven.  It is only five-connected and fails Dirac's neighbourhood
inequality.  Together the two barriers force the live theorem to spend the
counterexample hypotheses in combination, rather than another static portal
count.  Source:
`../barriers/hc7_width2_k7free_static_split_barrier.md`.

The pure-Moser degree-seven cell with exactly two exterior components is now
closed in full.  A single four-port call on `1,2,3,4` returns adjacent
carriers for `13|24` in its linkage outcome or `14|23` in its rural outcome.
Both complementary independent matchings feed one exact-state exchange, so
the former favourable-crossing and multi-frame compatibility gaps disappear.
The low-cut theorem sends every component of order at least four into this
two-connected closure; open twins, Hall matchings, and the cutvertex theorem
handle orders one, two, and three.  Sources:
`../results/hc7_exact7_moser_four_corner_exchange.md` and
`../results/hc7_exact7_moser_two_component_closure.md`.

This does not close the one-exterior pure-Moser branch, the descent-
composition step in an arbitrary connected-rich `(1,2)` adhesion, or the
other degree classes.  No multi-frame crossing-selection problem remains in
the exact two-component Moser cell.

In the one-exterior pure-Moser branch, the all-crossless family is already
closed uniformly by one five-terminal web: it makes the sole exterior plus
the five unique roots planar and yields a `4+1+1` colouring.  Thus a survivor
has a literal crossed frame.  The active step is not another frame census;
it is to reserve a connector outside the rooted bags or expose a bilateral
internal adhesion on which the four-corner equality state can be transferred.
Source: `../results/hc7_exact7_moser_one_component_allweb_closure.md`.

The atomic alternating packet web is now label-sensitive.  In the normalized
attained state `23|14|05|6`, any actual cycle through the six duty portals
closes when two duty pairs are nonalternating.  When all three alternate,
six of the eight literal orientations have explicit seven-bag models using
the other rich full packet and the thin full packet.  The only surviving
literal orbit is `2,4,5,3,1,0`.  This is an infinite six-portal-cycle
closure, not a claim about arbitrary multi-attachment bridges.  Source:
`../results/hc7_exact7_moser_cyclic_duty_exchange.md`.

When two exceptional cycles coexist in the paired-triangle state, the
two-packet cyclic-web theorem eliminates every clean transverse path and
leaves only homologous rungs and one-sided bridges.  Its exhaustive static
carrier verifier proves that homologous rungs alone need not yield three
disjoint duty carriers.  The audited cyclic-packet completion bypasses that
carrier barrier: the two exceptional cycles and the third full packet
already contain a literal `K_7`, even without a path between the cycles.
The six explicit templates handle arbitrary subdivisions and an arbitrary
packet-internal first-hit path from boundary literal `6`.  Source:
`../results/hc7_exact7_moser_cyclic_packet_completion.md`.

The carrier step cannot follow from shore connectivity alone.  The audited
essential-portal barrier `../barriers/hc7_sole_exterior_reserved_connector_barrier.md`
has a seven-connected, minimum-degree-seven, `K_7`-minor-free shore with both
complementary carrier pairs, no disjoint full connector, and no internal cut
of order at most six.  The next lemma must therefore spend an exact
proper-minor state transition, literal-boundary connectivity/degree, or a
global `K_7`-free extremality argument.

The exact five-root trace now supplies a model-carried interface uniformly.
The rooted `K_5` either has an `a-b` connector outside all five bags, giving
a literal `K_7` with `v`, or it contains an inclusion-minimal `a-b`
separator `Z` of order at least six.  Both terminal components are literally
`Z`-full and one named bag is hit twice.  The separator is arbitrary:
neither order six nor the form `U union {w}` has been proved.  Source:
`../results/hc7_exact7_rooted_k5_connector_separator.md`.

For a fixed adjacent complementary carrier pair `X,Y`, each component `R`
of the remaining sole exterior obeys
`|N_S(R)|+|N_{X union Y}(R)|>=7`.  Equality is an actual full exact-seven
adhesion; strict failure has surplus at least eight.  If the remainder is
connected but deficient, `X union Y` consumes an entire literal portal
class, of multiplicity at least two for root `0` and at least three for all
other Moser roots.  Thus the constructive bridge step has only two valid
inputs: multiple-portal exhaustion or surplus attachments.  Source:
`../results/hc7_exact7_moser_sole_exterior_failure_certificate.md`.

Inside the conditional exact-order-six connector cell
`T=U union {w}`, bilateral crossed frames now have an audited state
exchange.  Two admissible `w`-contacts on each side force a common decorated
block and six-colour `G`.  Admissible means both geometrically supported and
independent on the literal trace.  Rank at most one produces one of three
named certificates: a literal `w`--root incompatibility, direct-core
concentration, or a recursive adhesion with at least five attachments to one
named carrier block.  This discharges state matching once rank two occurs;
it does not reduce the arbitrary model separator to order six.  Exact degree
accounting now excludes every root-contact set containing a nonzero-centred
three-vertex arc of the Moser missing cycle, leaving at most three root
neighbours and at least four shore contacts.  A protected-tree surgery
label-faithfully transfers a pendant lobe whenever it contains both a
`w`-attachment and a portal to an admissible foreign block.  Hence every
surviving five-attachment lock has all useful foreign portals concentrated
on a central path or subdivided `Y`, or in pendant lobes with no
`w`-attachment.  Equality at five is a literal exact-seven adhesion governed
by the packet theorem; otherwise the lock has at least six distinct named
carrier attachments.  Two audited carrier peels eliminate a two-connected
singleton-trace block with any movable nonroot portal and a three-connected
pair-trace block when one locked attachment is also a movable portal.  The
exact residue is a cutvertex/2-cut, a literal singleton gate, or a
pair-trace rail capturing every locked attachment and separating it from
every movable foreign portal.  Seven-connectivity now amplifies the
pair-trace residue to three simultaneous outside-core portals.  Tutte's
two independent nonseparating paths then segregate all nonroot locked
attachments onto one rail and all three movable portals onto the other;
each rail complement is connected.  Distinct reversed cross-rail bridges
spanning both label sets peel; every four-connected residue is one coherent
rural face; and a nonrural three-connected residue exposes a three-cut in
which every trace-free portal component is pure with respect to the locked
attachments.  The five-contact input is componentwise, so
disconnected locked regions do not evade this route by scattering contacts.
One block-terminal augmentation now eliminates pairwise web drift entirely:
the whole portal set and whole attachment set have one same-vertex web.
Every marked vertex lies on its rib; every nonempty cell is behind a literal
full three-gate in the induced carrier and has at least four distinct
outside-carrier neighbours.  Rank-first, size-last optimization evacuates
every such cell without lowering contact rank.  Thus a three-connected
lex-optimal carrier is a literal planar/rural page; the alternative is an
actual cut of order at most two.  The quotient and low-cut results still
return literal crosses, attained-duty rotations, or a spanning planar
two-pole quotient.  They do **not** return a one-disk shore.

Indeed, a supported crossed frame already contains two disjoint carriers
joining alternating pairs on the literal `U`-cycle.  The shore therefore
cannot embed in a disk with that cycle as boundary, even when both
contracted poles are rural.  The exact barrier, including a planar
width-five spanning quotient, is
`../barriers/hc7_exact7_crossed_frame_disk_barrier.md`.  Consequently the
former “induced-pole expansion to two disk pages” endgame is retracted.

The surviving dynamic statement is
`../results/hc7_exact7_bilateral_decoration_kempe_lock.md`: a mismatch of
supported decoration states either switches to a common exact state or
returns a terminal-free bichromatic path whose first core hit lies in an
actual named supported block.  In rank-one mismatch both paths may return
to their already owned blocks.  The explicit self-lock example
`../barriers/hc7_exact7_two_shore_kempe_pairing_barrier.md` shows that this
does not itself produce an opposite attained duty.  The remaining exact-six
obstruction is therefore a critical owner change, a duty-correct labelled
peel, or a common colour-gluable adhesion—not induced-pole expansion.
Sources:
`../results/hc7_exact7_moser_order6_decorated_exchange.md` and
`../results/hc7_exact7_five_attachment_carrier_peel.md`, and
`../results/hc7_exact7_pair_carrier_bypass.md`, and
`../results/hc7_exact7_two_rail_bridge_overlap.md`, and
`../results/hc7_exact7_block_terminal_web.md`, and
`../results/hc7_exact7_tree_pole_rotation_exchange.md`, and
`../results/hc7_exact7_spanning_rural_quotient.md`, and
`../results/hc7_exact7_rural_rotation_rooted_k4.md`, and
`../results/hc7_exact7_set_terminal_cross_rotation.md`, and
`../results/hc7_exact7_terminal_free_state_or_rural.md`, and
`../results/hc7_exact7_terminal_free_lowcut_descent.md`, and
`../results/hc7_exact7_terminal_free_bilateral_endgame.md`.

The frame-mismatch part is also closed whenever both exact terminal shores
are three-connected and non-all-web.  Three crossless Moser frames force
all five crossless at the level of literal portal occurrences; therefore a
non-all-web shore has at least three crossed frames, and two such shores
share one.  The only frame-level residue is a genuinely one-sided all-web
shore.  Source:
`../results/hc7_exact7_moser_three_crossless_synchronization.md`.

The connected-rich branch has a stronger specialized capacity theorem.  In
the ten absolute-demand-three boundary types, once the defect is known, a
forced block can be chosen before the returned state so that two full packets
absorb the resulting defect-at-most-two carrier.  This is not an
unconditional carrier criterion: outside that normalization the carrier
must discharge its attained duty `D_U(B)`.  Hence every
cutvertex has exactly two deletion lobes, and every component outside any
fixed pair of full packets has at least three distinct attachment vertices
on their union.  The remaining problem is now a stable-bridge rerouting
problem, not boundary palette assignment.  Three attachments alone do not
give their distribution or three disjoint paths.  Source:
`../results/hc7_exact7_connected_rich_cutvertex_exchange.md`.

If a complementary bridge attaches to both rich packets and contacts a
whole boundary triangle plus one further literal, seven explicit bags give
a `K_7`; this removes one cross-packet support pattern without converting
the remaining attachment count into linkage.

One local rerouting is now rigorous.  A minimal portal-witness tree for a
full packet has at most twelve skeleton vertices.  Three bridge attachments
on one portal-free segment permit an exact tree rotation: the replacement
packet stays full and disjoint from the other packet, while the deleted
nonempty segment becomes a third connected carrier.  Boundary support at
least five closes by adaptive defect-two reflection; otherwise the move is
an exactly reversible low-support rotation.  The live S3 task is therefore
global composition: show that these rotations expose a support-five peel,
a common exact state, or a bounded stable/rural society.  Source:
`../results/hc7_exact7_packet_bridge_rotation.md`.

For an actual pure-Moser exterior component of order at least four, a
separator--component matching supplies four distinct portal witnesses.
Together with internal 3-connectivity, this puts the portal tree within the
safe order-at-least-three form of Tutte's stable-bridges theorem.  All seven
selected labels remain fixed and no bridge of the rerouted tree has its
attachment set contained in one segment.  Hence S3 no longer needs a
termination proof for one-segment rotations in this branch; its exact live
geometry is a bounded multi-segment bridge/web society.  Source:
`../results/hc7_exact7_portal_matching_stable_skeleton.md`.

Static packet contraction is now rigorously exhausted, not merely
computationally unproductive.  The exact quotient theorem says that three
independent universal packet vertices yield `K_7` exactly in the two-anchor
`K_4` case; when the rich pair is adjacent, exactly the one-anchor case is
obtained.  Source:
`../results/hc7_exact7_three_packet_quotient_characterization.md`.
Consequently the missing step must use a packet split, an internal path or
bridge, or a proper-minor state transition.

This is an adaptive state problem.  A static weakening of the support-four
carrier theorem is false: profile `(3,4,4)` already has a sparse
`2K_2+3K_1` counterexample with no anchored `K_4` and no clique vertex cover
of order at most two.  Geometry or minor-critical state transitions must be
used.  Source: `../barriers/hc7_exact7_support_344_static_trichotomy_barrier.md`.

### S4. The remaining interfaces — **OPEN**

Even a complete `(1,2)` theorem would leave:

* actual packet vector `(1,1)`;
* adhesions of order greater than seven; and
* rotation components which never expose an actual exact-seven adhesion.

These must feed back into S1.  No existing result turns packet thinness into
a bounded transversal or an apex pair, and no such inference is permitted.

One normalized `(1,1)` entry is now available.  A rich separating bridge
of a compulsory lock produces the twin boundary above, an exact state
attained by one named edge contraction, a literal old-to-new root map, and
five receiver lock/crossing alternatives.  Its local packet-sum rank drops
from three to two.  This does not provide a global anti-cycle rank: a
receiver theorem must prevent an involutive root exchange or a later return
to packet sum three.  Source:
`../results/hc7_compulsory_lock_twin_state_transfer.md`.

## Audited supporting principles

The following are proved but no longer live inside `(1,3)`:

* uniform carrier/list state synchronization:
  `../results/hc7_uniform_carrier_list_state_gluing.md`;
* seven-boundary colour/model/one-block trichotomy:
  `../results/hc7_exact7_boundary_rooted_trichotomy.md`;
* pair/full/forced-path list completions:
  `../results/hc7_exact7_pair_bicycle_completion.md` and
  `../results/hc7_exact7_forced_path_completion.md`;
* rank-free double-two-gate cut closure:
  `../results/hc7_exact7_double_two_gate_cut_closure.md`; and
* rooted portal and rural-page results listed in the authoritative
  `../README.md`.

They remain candidates for a demand-three certificate in `(1,2)` or for a
larger adhesion, but they are not a proof of either.

## Completion criterion

The programme may claim `HC_7` only after S1--S4 form an audited end-to-end
implication from a hypothetical counterexample to a literal `K_7` model or
a global six-colouring.  At present S1, S3, and S4 are open.
