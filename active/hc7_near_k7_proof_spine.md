# `HC_7` proof spine

## Verdict and target

`HC_7` is not proved.  The active target is

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
556 of the 685 possible `K_4`-free boundary types.  If the rich shore is
connected, its packets can be made adjacent and the one-anchor condition
`H-x succeq K_4` closes 33 more of the 129 residual types, leaving 96 in
that branch.  Source:
`../results/hc7_exact7_adaptive_12_boundary_closure.md`.

The exact constructive target is therefore:

> In an actual `(1,2)` seven-adhesion of a hypothetical counterexample,
> turn a nonrobust thin-side return into a second partial labelled carrier,
> a new return of demand at most two, or one fixed `K_5`-killing pair.

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
two.  Its singleton case remains live.  Source:
`../results/hc7_exact7_double_triangle_partial_packet_exchange.md`.

For a singleton thin shore `{q}`, the frozen 129-boundary census reduces the
cell to `M` and `M+13`: Dirac gives `alpha(G[S])<=2`, and these are exactly
the two alpha-two residual orbits.  In `M+13`, exact `25` and `46` traces
plus singleton Kempe exchange force complementary bichromatic paths in the
rich shore.  Either path disjoint from the two full packets gives an
explicit literal `K_7`; hence the survivor is a packet-entanglement problem,
not a state-enumeration problem.  The paths may arise from different
colourings, so no simultaneous routing is asserted.  Source:
`../results/hc7_exact7_singleton_thin_moser_extension_escape.md`.

Thus the named constructive substep in S3 is:

> After the proper-minor state is attained, extract a rich-shore carrier
> discharging its exact duty `D_U(B)`, or turn failure into a literal `K_7`,
> a common exact state, or the fixed-pair endgame.  Static contact or defect
> counts alone cannot do this.

One infinite subfamily now supplies that carrier.  If the rich shore has
two components and one has a cutvertex, split that component at the
cutvertex into two adjacent near-full carriers and use the other component
as the full third carrier.  An audited adaptive boundary theorem chooses the
thin forced block after the two defects are known but before the proper-minor
colouring is returned, and reflects every possible return.  Therefore both
components of a surviving two-component rich shore are cutvertex-free.
Singleton components and the connected-rich case remain open.  Source:
`../results/hc7_exact7_rich_cutpacket_exchange.md`.

For a nonempty bipartite boundary, an independent cutvertex theorem also
funds the bipartition state except for one crossed two-lobe geometry:
distinct defects in the same boundary component at even parity, both missed
by the cutvertex.  Dirac forces at least three lobe neighbours but does not
close the cell.  A verified `K_7`-containing counterarchitecture shows that
connectivity and static Dirac data alone cannot do so; the next step must use
`K_7`-freeness or a proper-minor state transition.  Source:
`../results/hc7_exact7_bipartite_cutvertex_exchange.md` and
`../barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md`.

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

This does not close the one-exterior pure-Moser branch, an arbitrary
connected-rich `(1,2)` adhesion, or the other degree classes.  Those are now
the live interfaces; no multi-frame crossing-selection problem remains in
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
