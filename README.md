# Hadwiger `HC_7` proof programme

## Current verdict

`HC_7` is **not proved** here.  The repository is now in proof-spine mode:
all active work targets one implication,

\[
 \text{7-connected + 7-contraction-critical + }K_7^\vee\text{ minor}
 \Longrightarrow K_7\text{ minor or a fixed pair }\{p,q\}
 \text{ with }G-\{p,q\}\text{ }K_5\text{-minor-free}.
\]

The latter outcome is enough by `HC_5`; a planar two-apex remainder is a
stronger special case.

The exact dependency chain is [active/hc7_near_k7_proof_spine.md](active/hc7_near_k7_proof_spine.md).

## Exact remaining gap

The normalization cells now have one common output, so the remaining link
is narrower than the original arbitrary-model problem:

1. **Involutive rotation/web composition or state gluing.**  Every
   normalized one-hole or two-hole model gives a literal `K_7`, an actual
   order-at-least-seven adhesion with a faithful equality-state interface,
   or an exact deficiency rotation.  Every rotation has an exact inverse.
   The task is to prove that a whole exchange component either contains a
   rooted two-carrier split (hence `K_7`), produces the same labelled
   boundary partition from operations on opposite shores (hence a
   six-colouring), or consists of compatible rural societies exposing one
   fixed pair `a,b` with `G-{a,b}` planar.

2. **Adaptive exact-seven reflection.**  The `(1,3)` packet vector is now
   eliminated.  The remaining exact-seven vectors are `(1,1)` and `(1,2)`.
   For `(1,2)`, two rich-side packets reflect every returned boundary
   partition of packet demand at most two.  The first uniform `(1,2)` theorem
   is now audited: robust independent blocks and literal two-anchor
   `K_4`-models eliminate 556 of the 685 possible `K_4`-free boundary types,
   for arbitrary shore size.  If the rich shore is connected, a one-anchor
   lift eliminates 33 more of the 129 residual types, including the Moser
   spindle.  The missing theorem must turn the remaining nonrobust returned
   state into a partial labelled carrier, a lower-demand state, or the fixed
   pair endgame.  For every absolute-demand-three boundary, an audited
   normalization now forces demand exactly three; one additional partial
   rich-shore carrier then reflects the state and glues.  A label-free
   triangle-transversal theorem also closes every adjacent near-full
   thin-shore split except an exact crossed-pure pattern.  The counts
   describe the finite boundary interface only; they do not assert that
   arbitrary favourable states are realizable.

### Exact-seven adhesions: `(1,3)` is eliminated

For an actual boundary `S` of order seven, the audited packet theorem leaves
only `(1,1)`, `(1,2)`, and `(1,3)` packet vectors.  A new independently
audited **adaptive packet-reflection theorem** eliminates `(1,3)` outright:

\[
 \text{one `S`-full packet on one shore}
 +\text{ three disjoint full packets on the other}
 \Longrightarrow K_7\text{ or a six-colouring}.
\]

If `G[S]` has a triangle, the four packets and that triangle are seven
literal clique branch sets.  Otherwise choose an independent boundary set
`I` of order four, or a maximum one of order three.  Contract the thin packet
with `I`; a proper-minor six-colouring makes `I` one exact boundary block.
After seeing the entire returned partition, the three opposite packets
reproduce it exactly: all non-retained blocks are contracted into distinct
packets, while a clique of singleton blocks remains literal.  The packet
demand is always at most three.  The two closed-shore colourings therefore
induce the same exact partition and glue.

This uses no Moser labels, gate, lobe, portal order, or connectivity beyond
what supplies the packets.  Consequently the live exact-seven adhesion
vectors are now only `(1,1)` and `(1,2)`.  The next adaptive target is
`(1,2)`, where two rich-side packets do not automatically reflect every
partition returned by the thin packet.

### First uniform `(1,2)` closure

Put `H=G[S]`.  Two independently audited mechanisms now eliminate a large
infinite family of actual `(1,2)` adhesions.

* If `H` has an independent set `I` of order at least five, or an independent
  four-set whose complement contains an edge, or an independent triple whose
  complement contains a triangle, then contracting the thin packet with `I`
  forces **every** returned equality state to have packet demand at most two.
  The two rich packets reflect that exact state and the shore colourings glue.
* If some two boundary vertices `x,y` can be deleted so that `H-{x,y}` has a
  `K_4` minor, then `Q+x`, `P_1+y`, `P_2`, and the four boundary-model bags are
  seven literal clique branch sets.  When the rich shore is connected, its
  two packets can first be made adjacent along a shortest internal path, so
  only one anchor `x` is needed and `H-x succeq K_4` suffices.

These mechanisms close 556 of all 685 unlabelled `K_4`-free seven-boundaries.
The unconditional residual has 129 types: 119 admit some abstract
demand-at-most-two state but no single forced block makes every return safe;
ten have minimum demand three, and all ten contain two disjoint triangles.
In the connected-rich branch the one-anchor lift leaves 96 types and removes
both independence-number-two residues, including Moser.  Thus raw packet
existence and boundary quotient models are now exhausted.  This last claim is
itself an audited exact theorem: adjoining three independent universal packet
vertices to `H` has a `K_7` minor **iff** a two-anchor deletion leaves a
`K_4` minor; adding the one rich packet edge changes “two anchors” to exactly
one.  The live step is therefore a shore-internal carrier exchange that
preserves information destroyed by packet contraction and controls which safe
state is actually returned.

The ten absolute-demand-three types now have a common adaptive endgame.
After forcing the audited independent block, every returned partition has
demand exactly three.  Two full rich packets fund two unfunded blocks; if a
third disjoint connected rich-shore subgraph contacts the last block and the
retained singleton clique, it funds the final block and exact state
reflection glues the shore colourings.  This is the precise carrier that
must now be extracted from internal geometry or a proper-minor transition.

There is also a uniform thin-shore obstruction.  If two adjacent connected
thin carriers each miss at most one boundary vertex, their two defects must
meet every boundary triangle.  With two disjoint boundary triangles this
forces distinct defects in different triangles, and both defect vertices
must be pure relative to their own triangle.  Otherwise the two rich packets,
the carriers, and a boundary triangle form seven literal branch sets.  For
the Moser boundary no triangle vertex is pure, so a nonsingleton thin shore
has no cutvertex and cannot have order two.  The singleton Moser shore
remains live; neither this theorem nor the finite verifier closes `(1,2)`.

Source: [double-triangle partial-packet exchange](results/hc7_exact7_double_triangle_partial_packet_exchange.md)
— [independent audit](results/hc7_exact7_double_triangle_partial_packet_exchange_audit.md).

The adaptive carrier has now been forced for another infinite geometric
family.  In a two-component rich shore, if either full component has a
cutvertex, splitting it at that cutvertex gives two adjacent connected
carriers which each miss at most one boundary vertex; the other component
is the full third carrier.  For every one of the ten absolute-demand-three
boundary types, an independently audited adaptive choice of the thin forced
block makes these three carriers reflect **every** subsequently returned
state.  Hence both components of any surviving two-component rich shore are
cutvertex-free.  Singleton components remain possible, and the theorem does
not yet handle a connected rich shore.

Source: [adaptive rich cut-packet exchange](results/hc7_exact7_rich_cutpacket_exchange.md)
— [independent audit](results/hc7_exact7_rich_cutpacket_exchange_audit.md).

A separate label-free cutvertex theorem handles every nonempty bipartite
boundary except one exact crossed-frame residue.  If the thin shore has a
cutvertex, either two disjoint adjacent carriers realize the bipartition
state and the two rich packets reflect it, or there are exactly two lobes
with distinct same-parity boundary defects, both missed by the cutvertex.
Dirac's inequality forces at least three cutvertex-to-lobe neighbours in
that residue.  A verified 24-vertex construction shows that 7-connectivity,
packet vector `(1,2)`, and all static Dirac inequalities still do not force
the carriers; the construction deliberately contains `K_7`, so it isolates
the need for `K_7`-freeness or proper-minor transitions rather than refuting
the HC7 theorem.

Source: [bipartite thin-shore cutvertex exchange](results/hc7_exact7_bipartite_cutvertex_exchange.md)
— [audit](results/hc7_exact7_bipartite_cutvertex_exchange_audit.md); barrier:
[connectivity-and-Dirac counterarchitecture](barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md).

The degree-seven pure-Moser two-component branch now has a stronger
low-separator closure.  Every exterior component is full to the seven
literal neighbours.  A cutvertex gives a literal `K_7`; an arbitrary
two-cut splits a component into adjacent connected carriers with disjoint
defects of order at most two.  An exact ten-vertex quotient enumeration
gives an `N(v)`-meeting `K_6` for 258 of the 260 defect pairs.  The two
exceptions `[13|24]` and `[14|23]` are eliminated symbolically by producing
and reproducing one of three exact complementary-defect boundary states.
Consequently every surviving exterior component is either of order at most
three or internally 3-connected.  This closes the old 33 two-cut geometries,
but not the 3-connected or tiny two-component Moser residue.

Source: [pure-Moser two-component low-cut exchange](results/hc7_exact7_moser_rich_twocut_exchange.md)
— [independent audit](results/hc7_exact7_moser_rich_twocut_exchange_audit.md).

The favourable pure-Moser crossing now closes **every** geometry of the
opposite exterior component.  The older thin-rural exchange eliminates
singletons, bridges, cutvertices, cycles, and cactus shores.  A
dependency-free ten-vertex certificate closes the triangular shore by
covering all 3,928 allowable triples of vertex defects.  The low-cut theorem
forces every remaining component of order at least four to be
three-connected.  In that last case, the four-port theorem gives either the
two crossing row carriers and a literal `K_7`, or a rural disk.  Two facial
arcs in the disk are adjacent connected carriers for the complementary
independent blocks `13` and `24`; proper-minor contractions then reproduce
exactly every possible returned boundary state and glue to a six-colouring.

Consequently a two-exterior pure-Moser counterexample cannot contain the
specific disjoint `0`--`5` and `2`--`4` crossing.  The remaining gap is no
longer internal shore geometry: it is the **multi-frame crossing-selection
step**.  One must prove that the four exact-trace five-cycles force a
favourable frame, or compose their incompatible rural orders into a literal
model or a common equality state.  Paths supplied in different frames may
not be assumed mutually disjoint.

Sources: [thin-rural exchange](results/hc7_moser_thin_rural_exchange.md) —
[audit](results/hc7_moser_thin_rural_exchange_audit.md);
[triangular shore closure](results/hc7_exact7_moser_triangle_shore.md) —
[audit](results/hc7_exact7_moser_triangle_shore_audit.md) —
[certificate](active/hc7_exact7_moser_triangle_shore_verify.py); and
[three-connected rural exchange](results/hc7_exact7_moser_3connected_web_exchange.md)
— [independent audit](results/hc7_exact7_moser_3connected_web_exchange_audit.md).

The connected-rich branch now has a uniform capacity theorem.  For each of
the ten absolute-demand-three boundary types, after seeing the defect set
but before receiving the minor colouring, one can force a maximal independent
exact block so that **two full packets plus any disjoint connected carrier
meeting at least five boundary vertices** reproduce every returned state.
All 290 boundary/defect cells were independently checked.  Consequently:

* every cutvertex of a connected rich shore has exactly two deletion lobes;
* for any chosen pair of disjoint full packets, every component outside
  their union has at least three distinct attachment vertices on the packet
  union; and
* a complementary bridge attached to both rich packets cannot contact a
  whole boundary triangle and any further boundary literal, since those
  contacts give seven explicit clique branch sets.

The second statement is a stable-bridge condition, not yet a linkage: it
does not prescribe how the three attachments are distributed between the
packets.  The new constructive target is a packet rerouting/stable-bridge
exchange turning those attachments into a third defect-two carrier, a common
state, or a coherent rural/two-apex certificate.

Source: [connected-rich carrier exchange](results/hc7_exact7_connected_rich_cutvertex_exchange.md)
— [independent audit](results/hc7_exact7_connected_rich_cutvertex_exchange_audit.md).

The first literal packet rerouting step is also audited.  Choose one portal
witness for each boundary label in a full packet and a minimal tree through
those witnesses.  Its labelled skeleton has at most twelve vertices and
eleven portal-free segments.  If a complementary rich-shore bridge has three
attachments on one segment, replacing the old segment between the extreme
attachments by a path through the bridge preserves both disjoint full
packets and frees the deleted segment as a third connected carrier.  Support
at least five closes by the preceding defect-two theorem; otherwise this is
an exactly reversible low-support rotation.  This is a uniform
label-preserving exchange, but it does not yet prove that an arbitrary
sequence of rotations terminates or has a coherent rural embedding.

Source: [portal-preserving packet-bridge rotation](results/hc7_exact7_packet_bridge_rotation.md)
— [independent audit](results/hc7_exact7_packet_bridge_rotation_audit.md).

Inside the 3-connected pure-Moser exterior components, the local rotations
can now be globalized without an unproved termination potential.  A general
separator lemma gives an `S`--component portal matching of order
`min(7,|C|)`.  Thus every component of order at least four has four distinct
labelled portal witnesses, and a minimal tree through all seven selected
witnesses has at least three skeleton segments.  Tutte's stable-bridges
theorem then reroutes those segments while fixing every witness so that no
bridge has all its attachments on one segment.  This removes the entire
one-segment drift family, but multi-segment web bridges remain.

Source: [portal matching and stable skeleton](results/hc7_exact7_portal_matching_stable_skeleton.md)
— [independent audit](results/hc7_exact7_portal_matching_stable_skeleton_audit.md); the false
unrestricted one-segment formulation is retained as a
[barrier](barriers/hc7_exact7_tutte_single_segment_barrier.md).

#### Retained `(1,3)` infrastructure (superseded on this branch)

The detailed thin-shore results below remain proved and may be reusable in a
different interface, but none is needed to eliminate an actual `(1,3)`
adhesion.  Before adaptive reflection, that branch had been reduced as
follows:

* the thin shore is 2-connected;
* every 2-cut has exactly two lobes;
* four-connected shores are impossible;
* planar three-connected shores give a literal `K_7` by the portal-face
  curvature construction; and
* a surviving three-connected shore is nonplanar and exposes a literal
  three-vertex web gate.  The gate is **not** assumed to be a triangle:
  its web-completion edges may be absent from the graph.

The audited three-gate resource exchange now closes **every** gate with at
least three lobes by explicit literal carriers.  Thus every surviving actual
three-cut has exactly two lobes.  Each lobe meets all three gate vertices,
contacts at least four boundary labels, and retains matching rank
`min(4-|F|,|C|)` after forbidding up to three boundary labels.  This closes
all shores of order at most seven, every literal triangle gate, and every
two-edge gate whose middle vertex has a boundary portal.  Thus the exact
survivor has order at least eight and a sparse gate: zero or one literal
edge, or a two-edge path with an unlabelled middle; every literal gate edge
also has endpoint portal rank at most one.

A new audited funnel removes an ambiguity in the earlier connector
language.  Every lobe of order at least two contains a literal `K_3` minor
rooted at the three gate vertices.  If its three bags have three distinct
literal boundary representatives, that model and the other lobe give the
four labelled carriers and hence a literal `K_7`.  Therefore every
surviving gate-rooted triangle has boundary-portal matching rank at most
two, even though a lobe of order at least three independently has three
distinct matched portal vertices.  The constructive front at that stage was
**maximal portal-rank triangle exchange**: distribute those three literal
portals among the rooted bags, force a matching proper-minor state, or
expose one coherent two-vertex endgame.  This is distinct from the earlier
"rooted triangle" on three chosen arm sets inside a lobe; that arm-rooted
connector may still have path/`Y` form.

The nested obstruction is now linearized uniformly.  If deleting any
vertex inside either lobe creates at least three components, crossed gate
incidence and seven-connectivity turn three of those components, together
with the opposite lobe, into four distinctly anchored clique carriers.
Likewise, if a maximal two-connected block has three distinct attachment
cutvertices, three branches rooted through that block give the same four
carriers and a literal `K_7`.  Thus every cutvertex node and every block
node has degree at most two: the block--cutvertex tree of each surviving
lobe is a path.  This does **not** say that a lobe is itself a path or
bound the order of any two-connected block.  This linearization feeds the
rank-two closure below; the genuinely two-connected blocks remain.

Two audited exchanges make that task literal.  A rank-two gate-rooted
triangle closes whenever the opposite lobe admits a connected star split
placing two fresh boundary portals on the required sides.  Failure is not
an arbitrary lack of linkage: every spanning tree has the same crossed
projection inequalities, and a tree lobe reduces to one crossed path
order.  Independently, any spanning partition of the thin shore into
three connected pairwise adjacent carriers whose boundary-contact lists
admit a proper three-list-colouring manufactures the same equality
partition from proper-minor contractions on both shores and six-colours
`G`.  The proof is uniform: for every strongly `k`-contraction-critical
graph, `q<=k-1` pairwise adjacent spanning carriers opposite `q` full
packets synchronize any proper `q`-list-colouring of the literal adhesion.
This discharges the palette-to-labelled-carrier step without assuming that
such a carrier/list system exists.

The rank-two multi-block case first acquires a canonical order.  At every
lobe cutvertex, any gate-duty pattern other than the exact cross
`{i,j}|{i,k}` gives a literal `K_7`; crossed supports cannot drift, the
common gate has no boundary portal, and either allocation of each cutvertex
produces three spanning pairwise adjacent carriers, each with at least four
literal boundary contacts.

A new audited **boundary rooted-model trichotomy** closes this entire
infinite branch.  For any triangle-free graph on a literal seven-set and
three nonempty contact lists with each palette support at least four, one of
the following holds:

1. the boundary is list-colourable;
2. the boundary plus the carrier triangle has an anchored `K_4`; or
3. some edge `pq` leaves `S-{p,q}` independent.

The three outcomes respectively give the synchronized carrier state, a
literal `K_7`, or the admissible one-block state
`S-{p,q}|{p}|{q}`, funded by one full packet on each shore.  The exhaustive
certificate covers all 107 triangle-free seven-vertex graphs; a direct
verifier and an independent Z3 encoding agree that the only 150 states left
after the first two outcomes lie on `K_2+5K_1`, `P_3+4K_1`, or
`P_4+3K_1`, all of which have the required edge.  Therefore a portal-rank-two
rooted triangle cannot have a cutvertex in its opposite lobe.  All
multi-block rank-two chains are eliminated, rather than merely reduced to a
forced-bicycle transport problem.

The supporting list theory remains useful outside that closed branch.
After singleton propagation every uncolourable state has one of ten audited
critical cores; pair-only states lift through an anchored `K_4`, full raw
lists lift by an SDR, and every remaining no-model state has an exact forced
unit-path certificate.  These facts explain the finite trichotomy but are no
longer an open dependency for the rank-two block chain.

Immediately before adaptive reflection, the `(1,3)` residue was structural:
portal rank at most one, or a
portal-rank-two rooted triangle whose opposite lobe is cutvertex-free (and
hence two-connected when it has at least three vertices).  The next target
is a connected split of such a lobe into three support-four carriers, or a
width-two/web certificate producing a fixed pair for the `K_5`-minor-free
endgame.  Adaptive reflection now eliminates this actual `(1,3)` cell, but
none of these local results closes `(1,1)`, `(1,2)`, or `HC_7`.

There was also a rank-free gain at every remaining lobe cutvertex.  If both
deletion sides meet exactly two of the three gate vertices, they and the
opposite lobe form a support-four carrier triangle, so the new boundary
trichotomy closes the cell.  Hence every surviving cut has a side meeting
all three gates.  The residual capacity profiles were `4/3/4` or `3/3/4`,
not an arbitrary block chain.  This remains a proved local theorem, not a
live `(1,3)` dependency.

### Secondary model-regeneration invariant

For a minimal `HC_7` counterexample, every `G-v` and every `G/e` is exactly
six-chromatic and therefore contains a `K_6` minor by `HC_6`; every
`G-{u,v}` is at least five-chromatic and therefore contains a `K_5` minor
by `HC_5`.  This permits a secondary extremal experiment which re-chooses a
`K_6` model after avoiding a nominated vertex, rather than preserving one
fixed near-`K_7` model.  It is not currently the primary route.

For the endgame, it is enough to produce one fixed pair `{p,q}` for which
`G-{p,q}` is `K_5`-minor-free: `HC_5` then four-colours the remainder and
two fresh colours finish.  A planar remainder is a stronger sufficient
certificate, not a necessary target.

The deficient-first normalization makes the deficient bag an induced path
`P`, with two literal neutral-row contacts at each endpoint.  A new endpoint
shadow exchange now eliminates the entire nontrivial **one-missing** path
branch: once either missing twin is repaired, one safe endpoint can be
absorbed into one of its two endpoint rows, producing a strictly smaller
labelled `K_7^vee` model.  Hence a target-free deficient-minimal model with
`|P|>=2` is genuinely both-missing.  Moreover every exterior component
meeting `P` is anticomplete to both missing twin bags; otherwise it gives
`K_7` directly or repairs one twin and triggers the same shrink.

The ordered one-missing corridor is therefore no longer an open cell.  The
normalization has two entry residues:

1. **Singleton core.**  `P` has one vertex.  The remaining obstruction is
   wholly inside the six generally nonsingleton foreign bags: they must be
   split or singletonized label-faithfully, or their proper-minor states
   must glue, or their societies must expose one global two-apex pair.
2. **Nontrivial core.**  Both twins remain missing and every `P`-lobe has
   adhesion contained in `P` and the four neutral bags.  A literal `K_7`
   requires three pairwise adjacent shores each meeting all four neutral
   rows.  The missing theorem must produce that third full-row shore, a
   faithful colour-gluable adhesion, or one compatible global plane
   expansion.

The nontrivial residue has two further audited structural constraints.
After fixing `P` and minimizing one missing twin, that twin is another
induced path: at least two of its five row classes are locked at each
endpoint and at most one row class can have a nontrivial portal span.  Also,
the envelope consisting of `P` and all incident exterior components has an
actual separator of order at least seven contained in the four neutral
bags.  Hence one neutral bag contains at least two literal envelope portals;
if the separator has order seven, every separator vertex is full to every
component on the other side.  The audited seven-root theorem now processes
all root distributions at every separator order: it returns `K_7`, a
nested actual adhesion, or a one-/two-hole rotation.  The singleton
one-hole cell has the same trichotomy.

A rotation is not a descent.  If `U=Z dotunion W` is the donor split,
moving `Z` from `U` into the old centre and then moving the same `Z` back
are both legal rotations.  Thus no potential depending only on the current
labelled model can strictly decrease along every move.  The exact local
positive certificate is also known: disjoint rooted carriers in `Z` for
the old and new missing-row demands give seven literal branch sets.
Without such carriers, even a 2-connected connector can have alternating
terminal order, so the residue is a genuine Two-Paths/web interface rather
than a hidden cutvertex case.

The mixed one-hole/two-hole part now has a genuine height orientation.
Let `mu` be the minimum deficient-centre order over all one- or two-hole
near models.  If `mu>=2`, every one-hole centre has order at least
`mu+1`; hence every floor state is two-hole and a mixed rotation strictly
rises away from that floor.  Consecutive two-hole missing pairs must
overlap, singleton fixed-frame pivots backtrack, and a concentrated donor
with `U-r` 2-connected at a selected root closes by `K_7`, an actual
adhesion, or a forbidden singleton centre.  The remaining rotation cell is
therefore the pure two-hole width-two web (including frame changes and
non-3-connected two-piece donors), not an arbitrary near-model walk.

The shared-label two-hole cell now has two literal exchange mechanisms.
A freely detachable common-row portal core produces a `K_7^-` model with
the same endpoint centre and is therefore excluded either outright or by
the height floor.  More strongly, three disjoint carriers for the two
exclusive rows and the common row promote the common row itself to the
seventh branch set and give a literal `K_7`.  For a singleton common
portal, the residue is consequently a label-exact cut/two-row monopoly or
an alternating rural page; a portal attached to both endpoints supplies
the audited actual-adhesion state.

For a 4-connected connector, absence of the two private carriers now has
one audited output: all private portals lie on a single facial cycle in
the crossed labelled order `alpha,P_c,P_b,beta`.  Distinct useful traffic
cannot leave a common portal core through different components without
giving a literal `K_7`.  Thus the live composition issue is no longer an
arbitrary 4-connected capacity problem; it is transport of one ordered
rural page across a change of connector torso or an actual 1-/2-adhesion.

Small rural adhesions themselves no longer carry holonomy.  A tree of
simultaneously port-labelled planar torsos glued through vertices, edges,
or non-overfull facial triangles is planar.  If one fixed set of at most
two actual vertices meets every overfull triangle, deleting it makes the
whole tree planar.  The first genuine geometric interface is therefore an
order-at-least-four adhesion (or incompatible overfull triangles); the
cycle-order exchange handles the two-connected, pointwise-full subcase.

At a cyclic mismatch, distributed contacts are now usable over an unbounded
family: four disjoint thick port sectors retain literal row contacts, and
disjoint row packets may repair all corner duties.  A packet on one corner
connection produces the exact one-hole model needed by the height gap, while
matching opposite-shore states splice on the actual adhesion.  What is not
yet proved is that every raw trichotomy adhesion supplies such disjoint
sectors or packets; overlapping spans and multi-row deficiencies remain the
literal extraction gap.

The cyclic-web branch and one exact state mechanism are now closed uniformly.
For two anticomplete connected shores full to a Hamiltonian boundary frame,
with at most three guarded vertices outside that frame, seven-connectivity
gives either a same-shore crossing or a common planar remainder after deleting
the guards.  The planar branch is now terminal even with three guards: a
uniform palette-recycling lemma shows that Strong Hadwiger for `r` colours
lifts across any clique apex set of order `s`; at `(r,s)=(4,3)`, every
seven-chromatic three-apex graph contains a literal `K_7`.  Independently, if each shore augments the same partition of the
actual adhesion into six clique carriers, proper-minor minimality forces the
same six-block state from opposite sides and the colourings glue.  The live
application gap is consequently precise: in the residual three-span cell,
extract either the distributed packets needed for the crossed lift or those
same six labelled partition carriers on both shores.  A static interval
argument cannot do this; the sharp cyclic packing/transversal value is three.

Actual adhesions of order seven now have a sharper, audited orientation.  If
`nu_i` is the maximum number of disjoint connected packets in shore `i` which
meet all seven literal boundary vertices, then
`nu_1+nu_2<=4`, one `nu_i` equals one, and
`omega(G[S])<=6-(nu_1+nu_2)`.  This controls packets inside a connected
shore, not only the number of components.  In the pure-Moser crossing, the
opposite carrier/rural component is therefore literally packet-thin: two
full packets would satisfy the two-row carrier completion and give `K_7`.
Before adaptive reflection, in the extremal `(1,3)` vector a near-full carrier exchange made the
thin shore 2-connected with exactly two lobes at every 2-cut.  A maximum
literal portal matching and rooted-`K_4` lift then eliminate every
four-connected thin shore.  In the three-connected branch, facial curvature
and three adjacent portal arcs eliminate the entire planar case.  Those
arguments had left a width-two lobe exchange or a nonplanar
three-connected web with a literal three-vertex gate; web-completion edges
at that gate may not be treated as graph edges.  Adaptive packet reflection
now bypasses both cells for an actual `(1,3)` adhesion; the warning against
reinterpreting packing number one as a bounded transversal remains valid.

At a detachable lex-minimal row lobe, the exact local transfer is also known.
If the lobe meets the missed row and owns exactly two foreign rows, moving it
repairs the old hole and returns a literal one- or two-hole near model.  If
that transfer is unavailable, seven-connectivity supplies at least
`4-|Z|` **actual** peer-side contact vertices, not merely row labels.  Turning
those vertices into distributed packets or opposite partition carriers is
the current constructive edge; ownership alone does not bound an actual cut.

The common rows feeding that edge now have an audited uniform normal form.
In a lex-minimal six-duty row every non-cutvertex owns at least two literal
duties, and distinct non-cutvertices own disjoint duties.  Hence there are
at most three non-cutvertices and every block is an edge or one possible
triangle.  With the permitted unused-component absorption,
seven-connectivity collapses the entire unbounded three-arm family to a
literal `2+2+2` triangle.  The sole unbounded row is an induced path whose
endpoints concentrate at least four duties and whose interior carries at
most two mobile duty classes.  If the path has order at least seven, one
mobile class has at least three distinct internal portals.  The active
constructive edge is therefore the **mobile-path exchange**: turn those one
or two spans into literal diagonal packets, matching opposite-shore states,
or one deletion of at most three vertices to a four-colourable clique tree.

At a shared pinch edge, criticality also produces a faithful equality
partition on the literal adhesion and five bichromatic entrances.  A
matching state from the opposite shore six-colours the graph.  Equivalently,
deleting the common colour class produces a five-chromatic core with two
root sets saturated in every five-colouring; a `K_5` model meeting both
sets in every bag lifts literally to `K_7`.  Saturation alone is false as a
rooted-model theorem, so the live step must use the fixed rows, actual
adhesion, or coherent rural pair.

The audited Hall, protected-linkage, rural-face, list-state, and path-Helly
lemmas remain reusable mechanisms inside those two residues.  They do not
by themselves align palette colours with nonsingleton branch-bag labels.
A static shortcut which contracts three common bags to a triangle is also
invalid: `K_2` joined with the icosahedron gives a seven-connected,
`K_7`-minor-free witness in which the quotient forgets both portal rotations
and the actual apex vertices.  Any continuation must therefore preserve
literal carriers or equality states on the full uncontracted adhesion.

A sharper rooted-model shortcut is also false.  In the 13-vertex deletion
of `K_2` joined with the icosahedron, the seven-vertex neighbourhood set is
robust under every six-deletion and the remaining graph has an unrooted
`K_6`, but it has no neighbourhood-meeting `K_6`.  The sole valid output is
the same universal pair, whose deletion leaves the neighbourhood cofacial.
This shows that connectivity and first-hit data alone cannot close the gap;
the next theorem must use contraction-critical proper-minor states on an
actual adhesion.  See
[the barrier](barriers/hc7_rooted_jorgensen_apex_barrier.md).

Completing this composition link gives `K_7`, a six-colouring, or a planar
graph after deleting one fixed pair; each contradicts a hypothetical
minimal counterexample.  No theorem in the repository currently completes
that link.

## Audited live results

- [Bipartite total-contraction split](results/hc7_near_k7_bipartite_total_contraction.md) — [audit](results/hc7_near_k7_bipartite_total_contraction_audit.md)
- [Palette-to-label alignment in a singleton shell](results/hc7_near_k7_palette_label_alignment.md) — [audit](results/hc7_near_k7_palette_label_alignment_audit.md)
- [Arbitrary-model literal-rooting bridge](results/hc7_near_k7_literal_rooting_bridge.md) — [audit](results/hc7_near_k7_literal_rooting_bridge_audit.md)
- [Deficient-path normalization](results/hc7_near_k7_deficient_path_normalization.md) — [audit](results/hc7_near_k7_deficient_path_normalization_audit.md)
- [Coherent spanning transport](results/hc7_near_k7_coherent_spanning_transport.md) — [audit](results/hc7_near_k7_coherent_spanning_transport_audit.md)
- [Wholesale transfer of foreign-contacting pieces](results/hc7_near_k7_wholesale_piece_transfer.md) — [audit](results/hc7_near_k7_wholesale_piece_transfer_audit.md)
- [Uniform path-portal Helly dichotomy](results/hc7_near_k7_path_portal_helly.md) — [audit](results/hc7_near_k7_path_portal_helly_audit.md)
- [Endpoint shadow exchange](results/hc7_near_k7_endpoint_shadow_exchange.md) — [audit](results/hc7_near_k7_endpoint_shadow_exchange_audit.md)
- [Both-missing second-path normalization](results/hc7_near_k7_both_missing_second_path.md) — [audit](results/hc7_near_k7_both_missing_second_path_audit.md)
- [Both-missing neutral separator](results/hc7_near_k7_both_missing_neutral_separator.md) — [audit](results/hc7_near_k7_both_missing_neutral_separator_audit.md)
- [Surplus-root core/gate exchange](results/hc7_near_k7_surplus_core_gate.md) — [audit](results/hc7_near_k7_surplus_core_gate_audit.md)
- [Surplus-root transfer and deficiency rotation](results/hc7_near_k7_surplus_root_transfer.md) — [audit](results/hc7_near_k7_surplus_root_transfer_audit.md)
- [Uniform seven-root trichotomy](results/hc7_near_k7_seven_root_trichotomy.md) — [audit](results/hc7_near_k7_seven_root_trichotomy_audit.md)
- [Singleton one-hole rooted exchange](results/hc7_near_k7_singleton_one_hole_trichotomy.md) — [audit](results/hc7_near_k7_singleton_one_hole_trichotomy_audit.md)
- [Exact rotation involution and rooted capacity](results/hc7_near_k7_rotation_edge.md) — [audit](results/hc7_near_k7_rotation_edge_audit.md)
- [Missing-pair overlap across a rotation](results/hc7_near_k7_rotation_pair_overlap.md) — [audit](results/hc7_near_k7_rotation_pair_overlap_audit.md)
- [Singleton fixed-frame holonomy](results/hc7_near_k7_singleton_holonomy.md) — [audit](results/hc7_near_k7_singleton_holonomy_audit.md)
- [One-hole height gap](results/hc7_near_k7_one_hole_height_gap.md) — [audit](results/hc7_near_k7_one_hole_height_gap_audit.md)
- [Three-connected concentrated-rotation closure](results/hc7_near_k7_three_connected_concentrated_rotation.md) — [audit](results/hc7_near_k7_three_connected_concentrated_rotation_audit.md)
- [Critical-pinch actual-adhesion state](results/hc7_near_k7_critical_pinch_state.md) — [audit](results/hc7_near_k7_critical_pinch_state_audit.md)
- [Critical-edge double-saturation reduction](results/hc7_critical_edge_double_saturation.md) — [audit](results/hc7_critical_edge_double_saturation_audit.md)
- [Common-row portal absorption](results/hc7_near_k7_common_portal_absorption.md) — [audit](results/hc7_near_k7_common_portal_absorption_audit.md)
- [Common-row promotion to a literal seventh bag](results/hc7_near_k7_common_row_promotion.md) — [audit](results/hc7_near_k7_common_row_promotion_audit.md)
- [Common-row carrier or ordered rural page](results/hc7_near_k7_common_row_rural_book.md) — [audit](results/hc7_near_k7_common_row_rural_book_audit.md)
- [Fixed-root rural-page holonomy](results/hc7_near_k7_fixed_root_rural_holonomy.md) — [audit](results/hc7_near_k7_fixed_root_rural_holonomy_audit.md)
- [Set-rooted four-block rural order](results/hc7_near_k7_set_root_rural_order.md) — [audit](results/hc7_near_k7_set_root_rural_order_audit.md)
- [Rural torso-tree planar/two-apex gluing](results/hc7_near_k7_torso_tree_apex_gluing.md) — [audit](results/hc7_near_k7_torso_tree_apex_gluing_audit.md)
- [Two-shore rural cycle-order exchange](results/hc7_rural_cycle_order_exchange.md) — [audit](results/hc7_rural_cycle_order_exchange_audit.md)
- [Port-matching cycle exchange](results/hc7_port_matching_cycle_exchange.md) — [audit](results/hc7_port_matching_cycle_exchange_audit.md)
- [Distributed-row port exchange](results/hc7_port_distributed_row_exchange.md) — [audit](results/hc7_port_distributed_row_exchange_audit.md)
- [Guarded cyclic-shore web exchange and opposite partition-carrier splice](results/hc7_guarded_cycle_web_exchange.md) — [audit](results/hc7_guarded_cycle_web_exchange_audit.md)
- [Contact-transversal amplification and two-owner rotation](results/hc7_contact_transversal_amplification.md) — [audit](results/hc7_contact_transversal_amplification_audit.md)
- [Three-anchor lobe-median exchange](results/hc7_three_anchor_lobe_median.md) — [audit](results/hc7_three_anchor_lobe_median_audit.md)
- [Uniform clique-apex lifting and the three-apex `HC_7` theorem](results/hc7_three_apex_planar_endgame.md) — [audit](results/hc7_three_apex_planar_endgame_audit.md)
- [Lex-minimal carrier block rigidity and three-arm collapse](results/hc7_lexminimal_carrier_block_rigidity.md) — [audit](results/hc7_lexminimal_carrier_block_rigidity_audit.md)
- [Exact-seven full-packet packing](results/hc7_exact_seven_packet_packing.md) — [audit](results/hc7_exact_seven_packet_packing_audit.md)
- [Adaptive exact-seven `(1,3)` packet reflection](results/hc7_exact7_adaptive_packet_reflection.md) — [audit](results/hc7_exact7_adaptive_packet_reflection_audit.md); [finite demand verifier](active/hc7_exact7_adaptive_packet_reflection_verify.py)
- [Adaptive exact-seven `(1,2)` robust-state and anchored-model closure](results/hc7_exact7_adaptive_12_boundary_closure.md) — [audit](results/hc7_exact7_adaptive_12_boundary_closure_audit.md); [boundary/model verifier](active/hc7_exact7_adaptive_12_packet_quotient_probe.py)
- [Exact three-packet quotient characterization](results/hc7_exact7_three_packet_quotient_characterization.md) — [audit](results/hc7_exact7_three_packet_quotient_characterization_audit.md); [exact minor verifier](active/hc7_exact7_three_packet_quotient_verify.py)
- [Double-triangle partial-packet exchange in exact `(1,2)`](results/hc7_exact7_double_triangle_partial_packet_exchange.md) — [audit](results/hc7_exact7_double_triangle_partial_packet_exchange_audit.md); [crossed-pure verifier](active/hc7_exact7_double_triangle_four_carrier_probe.py)
- [Adaptive three-carrier reflection and rich cut-packet closure](results/hc7_exact7_rich_cutpacket_exchange.md) — [audit](results/hc7_exact7_rich_cutpacket_exchange_audit.md); [state verifier](active/hc7_exact7_three_carrier_state_probe.py)
- [Bipartite thin-shore cutvertex exchange](results/hc7_exact7_bipartite_cutvertex_exchange.md) — [audit](results/hc7_exact7_bipartite_cutvertex_exchange_audit.md); [crossed-frame barrier](barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md)
- [Pure-Moser two-component cutvertex/two-cut closure](results/hc7_exact7_moser_rich_twocut_exchange.md) — [audit](results/hc7_exact7_moser_rich_twocut_exchange_audit.md); [exact quotient verifier](archive/moser_global_2cut_verify.py)
- [Pure-Moser triangular exterior-shore closure under the favourable crossing](results/hc7_exact7_moser_triangle_shore.md) — [audit](results/hc7_exact7_moser_triangle_shore_audit.md); [certificate](active/hc7_exact7_moser_triangle_shore_verify.py)
- [Connected-rich defect-two carrier and three-attachment exchange](results/hc7_exact7_connected_rich_cutvertex_exchange.md) — [audit](results/hc7_exact7_connected_rich_cutvertex_exchange_audit.md); [defect-two verifier](active/hc7_exact7_single_defect2_probe.py)
- [Portal-preserving packet-bridge rotation](results/hc7_exact7_packet_bridge_rotation.md) — [audit](results/hc7_exact7_packet_bridge_rotation_audit.md)
- [Portal matching and Tutte-stable skeleton in a 3-connected shore](results/hc7_exact7_portal_matching_stable_skeleton.md) — [audit](results/hc7_exact7_portal_matching_stable_skeleton_audit.md); [one-segment barrier](barriers/hc7_exact7_tutte_single_segment_barrier.md)
- [Exact-seven thin-shore near-full exchange](results/hc7_exact7_thin_shore_exchange.md) — [audit](results/hc7_exact7_thin_shore_exchange_audit.md)
- [Exact-seven portal matching and rooted-`K_4` exchange](results/hc7_exact7_portal_rooted_k4.md) — [audit](results/hc7_exact7_portal_rooted_k4_audit.md)
- [Four-connected and planar three-connected thin-shore closure](results/hc7_exact7_rooted_portal_face_closure.md) — [audit](results/hc7_exact7_rooted_portal_face_closure_audit.md)
- [Exact-seven three-gate resource exchange](results/hc7_exact7_three_gate_resource_exchange.md) — [audit](results/hc7_exact7_three_gate_resource_exchange_audit.md)
- [Exact-seven two-lobe sparse-gate exchange](results/hc7_exact7_two_lobe_gate_exchange.md) — [audit](results/hc7_exact7_two_lobe_gate_exchange_audit.md)
- [Sparse-gate labelled median exchange](results/hc7_exact7_sparse_gate_median_exchange.md) — [audit](results/hc7_exact7_sparse_gate_median_exchange_audit.md)
- [Gate-rooted triangle and portal-rank funnel](results/hc7_exact7_rooted_triangle_portal_rank.md) — [audit](results/hc7_exact7_rooted_triangle_portal_rank_audit.md)
- [Nested cutvertex crossed-arm closure](results/hc7_exact7_nested_cutvertex_exchange.md) — [audit](results/hc7_exact7_nested_cutvertex_exchange_audit.md)
- [Exact-seven branching-block closure and lobe block-chain theorem](results/hc7_exact7_block_chain_exchange.md) — [audit](results/hc7_exact7_block_chain_exchange_audit.md)
- [Portal-rooted triangle peels, cross-lobe star split, and crossed-order certificate](results/hc7_exact7_portal_rooted_triangle_exchange.md) — [audit](results/hc7_exact7_portal_rooted_triangle_exchange_audit.md)
- [Spanning-triangle boundary list-state gluing](results/hc7_exact7_triangle_list_state.md) — [audit](results/hc7_exact7_triangle_list_state_audit.md)
- [Uniform carrier-list state synchronization](results/hc7_uniform_carrier_list_state_gluing.md) — [audit](results/hc7_uniform_carrier_list_state_gluing_audit.md)
- [Triangle-free seven-boundary critical list cores and implication bicycles](results/hc7_exact7_triangle_list_critical.md) — [audit](results/hc7_exact7_triangle_list_critical_audit.md); [verifier](active/hc7_exact7_triangle_list_critical_verify.py)
- [Canonical crossed block-chain list sweep](results/hc7_exact7_block_chain_list_exchange.md) — [audit](results/hc7_exact7_block_chain_list_exchange_audit.md)
- [Exact-seven pair-bicycle and full-list completion](results/hc7_exact7_pair_bicycle_completion.md) — [audit](results/hc7_exact7_pair_bicycle_completion_audit.md); [verifier](active/hc7_exact7_pair_bicycle_completion_verify.py)
- [Exact-seven forced-path completion and five cut-switch types](results/hc7_exact7_forced_path_completion.md) — [audit](results/hc7_exact7_forced_path_completion_audit.md)
- [Exact-seven boundary colour/model/one-block trichotomy](results/hc7_exact7_boundary_rooted_trichotomy.md) — [audit](results/hc7_exact7_boundary_rooted_trichotomy_audit.md); [direct verifier](active/hc7_exact7_raw_list_no_k4_verify.py)
- [Rank-free double-two-gate cut closure](results/hc7_exact7_double_two_gate_cut_closure.md) — [audit](results/hc7_exact7_double_two_gate_cut_closure_audit.md)
- [Pure-Moser crossing carrier and packet-thin rural blocker](results/hc7_moser_crossing_carrier.md) — [audit](results/hc7_moser_crossing_carrier_audit.md)
- [Pure-Moser near-full rural split and cycle/cactus closure](results/hc7_moser_thin_rural_exchange.md) — [audit](results/hc7_moser_thin_rural_exchange_audit.md)
- [Mobile-path bilateral state and protected two-packet completion](results/hc7_mobile_path_exchange.md) — [audit](results/hc7_mobile_path_exchange_audit.md)
- [Literal shore completion and capacity dual](results/hc7_near_k7_literal_shore_completion.md) — [audit](results/hc7_near_k7_literal_shore_completion_audit.md)
- [Uniform rooted row promotion and Hall certificate](results/hc7_near_k7_rooted_triangle_promotion.md) — [audit](results/hc7_near_k7_rooted_triangle_promotion_audit.md)
- [Protected two-portal exchange](results/hc7_near_k7_two_portal_support_exchange.md) — [audit](results/hc7_near_k7_two_portal_support_exchange_audit.md)
- [Locked two-row linkage or coherent face](results/hc7_near_k7_locked_two_row_linkage.md) — [audit](results/hc7_near_k7_locked_two_row_linkage_audit.md)
- [Dynamic adhesion states and planar list splicing](results/hc7_near_k7_dynamic_locked_gate.md) — [audit](results/hc7_near_k7_dynamic_locked_gate_audit.md)
- [Two-heavy harmonica elimination](results/hc7_near_k7_harmonica_gate.md) — [audit](results/hc7_near_k7_harmonica_gate_audit.md)
- [Load-minimal literal Kempe packet](results/hc7_near_k7_load_minimal_kempe_packet.md) — [audit](results/hc7_near_k7_load_minimal_kempe_packet_audit.md)
- [Planar carrier degree escape](results/hc7_near_k7_planar_carrier_degree_escape.md) — [audit](results/hc7_near_k7_planar_carrier_degree_escape_audit.md)
- [Off-face transfer and four-connected Hall-collision descent](results/hc7_near_k7_offface_transfer_closure.md) — [audit](results/hc7_near_k7_offface_transfer_closure_audit.md)
- [Double-forced boundary-state jump](results/hc7_near_k7_double_forced_state_jump.md) — [audit](results/hc7_near_k7_double_forced_state_jump_audit.md)
- [Double-forced facial-edge localization](results/hc7_near_k7_double_forced_edge_localization.md) — [audit](results/hc7_near_k7_double_forced_edge_localization_audit.md)
- [Two-universal rural rigidity](results/hc7_near_k7_two_universal_rural_rigidity.md) — [audit](results/hc7_near_k7_two_universal_rural_rigidity_audit.md)
- [Rainbow-cycle completion](results/hc7_near_k7_rainbow_cycle_completion.md) — [audit](results/hc7_near_k7_rainbow_cycle_completion_audit.md)
- [Nested neutral-triangle rooted-model principle](results/hc7_near_k7_nested_triangle_rooted_model.md) — [audit](results/hc7_near_k7_nested_triangle_rooted_model_audit.md)
- [Two-defect rooted face and portal capture](results/hc7_near_k7_two_defect_rooted_face.md) — [audit](results/hc7_near_k7_two_defect_rooted_face_audit.md)
- [Two-defect disconnected-bag closure](results/hc7_near_k7_two_defect_cut_closure.md) — [audit](results/hc7_near_k7_two_defect_cut_closure_audit.md)
- [Rigid-boundary contraction splice](results/hc7_near_k7_rigid_boundary_splice.md) — [audit](results/hc7_near_k7_rigid_boundary_splice_audit.md)
- [Exact-seven boundary threshold](results/hc7_near_k7_exact7_boundary_threshold.md) — [audit](results/hc7_near_k7_exact7_boundary_threshold_audit.md)
- [Exact-seven `K3+2K2` web closure](results/hc7_near_k7_exact7_k322_web_closure.md) and [`C5+2K1` web closure](results/hc7_near_k7_exact7_c5_web_closure.md) — [shared audit](results/hc7_near_k7_exact7_web_closures_audit.md)
- [Fixed-extension active-face theorem](results/hc7_near_k7_fixed_extension_active_face.md) — [audit](results/hc7_near_k7_fixed_extension_active_face_audit.md)
- [Conditional active-root facial coherence](results/hc7_near_k7_active_root_face_exchange.md) — [audit](results/hc7_near_k7_active_root_face_exchange_audit.md)

These are proved only under their written hypotheses.  In particular,
the singleton/bipartite hypotheses are not a general normalization theorem.

## Active work

- [Proof spine](active/hc7_near_k7_proof_spine.md)
- [Both-missing constant-owner corridor](active/hc7_near_k7_constant_owner_corridor.md)
- [Port-labelled split versus 2-apex](active/hc7_near_k7_port_labeled_split_2apex.md)
- [Multiply-hit neutral exchange](active/hc7_near_k7_multiply_hit_neutral_exchange.md)
- [Three-connected rural transfer](active/hc7_near_k7_three_connected_rural_transfer.md)
- [Three-anchor capacity/web composition](active/hc7_three_anchor_capacity_web.md)

## Repository layout

- `results/`: proved live lemmas, with audits beside them.
- `active/`: the current proof spine, proof attempts, and current scripts.
  Generated Python dependencies and the relocatable verification runtime live
  under `active/runtime/`; they are infrastructure, not mathematical results.
- `barriers/`: explicit counterexamples and blocked proof mechanisms.
- `archive/`: all superseded, retracted, peripheral, or currently unused
  work, preserved under its original filename.

`README.md` is the only authoritative status file.  Historical status
reports in `archive/` are not current.  New files must not be added at the
repository root.
