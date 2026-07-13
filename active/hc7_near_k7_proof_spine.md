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

Thus the named constructive substep in S3 is:

> Extract the adaptive third partial carrier from the rich shore, or turn
> its failure into a literal `K_7`, a common exact state, or the fixed-pair
> endgame.  Static contact patterns alone cannot do this.

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

In the pure-Moser degree-seven cell with exactly two exterior components,
all separators internal to either component of order at most two are now
closed.  Cutvertices give a literal model.  A two-cut produces two adjacent
defect-at-most-two carriers; every static quotient except `[13|24]` and
`[14|23]` has an `S`-meeting `K_6`, and those two states glue by a symbolic
complementary-defect exchange.  Thus each surviving exterior component is
tiny (order at most three) or 3-connected.  This is a genuine infinite-
family closure, but it does not close the 3-connected web residue.  Source:
`../results/hc7_exact7_moser_rich_twocut_exchange.md`.

Conditional on the favourable disjoint `0`--`5` and `2`--`4` crossing in
one exterior component, **all** internal geometries of the opposite
component are now eliminated.  The thin-rural theorem handles singleton,
bridge, cutvertex, cycle, and cactus shores; the finite crossed-page theorem
handles a triangle; the low-cut theorem reduces every remaining component
of order at least four to the three-connected case; and the new rural
complementary-block theorem closes that case.  In its disk outcome, facial
carriers for `13` and `24` reproduce each exact state returned through the
crossed shore, so palette alignment is literal and no colour-to-bag lift is
assumed.

The exact live Moser step is therefore multi-frame composition: prove that
one of the four trace frames supplies the favourable crossing, or that the
simultaneous rural orders force a literal `K_7` or the same exact boundary
state from opposite proper-minor operations.  Witness paths from different
frames are not known disjoint.  Sources:
`../results/hc7_moser_thin_rural_exchange.md`,
`../results/hc7_exact7_moser_triangle_shore.md`, and
`../results/hc7_exact7_moser_3connected_web_exchange.md`.

The connected-rich branch has a stronger uniform capacity theorem.  In all
ten absolute-demand-three boundary types, two full packets absorb any third
disjoint connected carrier of boundary defect at most two, with the forced
block chosen after the defect but before the returned state.  Hence every
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
