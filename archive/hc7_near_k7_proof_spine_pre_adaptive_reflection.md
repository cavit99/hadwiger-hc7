# `HC_7` proof spine (superseded before adaptive `(1,3)` reflection)

This former active chain is retained for provenance.  Its exact `(1,3)`
thin-shore branch was eliminated uniformly by
`results/hc7_exact7_adaptive_packet_reflection.md`.

This file is the only active dependency chain.  All other workspace notes
are frozen supporting material unless cited here.

## Target

Prove

\[
 \boxed{
  \text{7-connected + 7-contraction-critical + a }K_7^\vee\text{ minor}
  \Longrightarrow
  K_7\text{ minor or a fixed pair }\{p,q\}
  \text{ with }G-\{p,q\}\text{ }K_5\text{-minor-free}.}
\tag{T}
\]

The second outcome is terminal because `HC_5` four-colours
`G-{p,q}`, and two fresh colours finish `G`.  A coherent 2-apex structure
with `G-{p,q}` planar is a stronger sufficient certificate, not the only
permitted endgame.

## Frozen input

1. A minor-minimal counterexample to `HC_7` is 7-contraction-critical,
   7-connected, and `K_7`-minor-free.
2. The known near-clique theorem gives a `K_7^vee` minor in every
   non-6-colourable graph.
3. A `K_7^vee` model can be made spanning: its bag union is connected;
   absorb each component outside the union into an adjacent bag.
4. Label a spanning model by
   \[
     A,B,C,D_1,D_2,D_3,D_4,
   \]
   with only the pairs `AB,AC` not prescribed.  A label-preserving split
   of `A` repairing these two pairs gives a literal `K_7` model.
5. Model regeneration is always available as a secondary invariant:
   every `G-v` and `G/e` is exactly 6-chromatic and contains a `K_6`
   minor by `HC_6`; every `G-{u,v}` is at least 5-chromatic and contains
   a `K_5` minor by `HC_5`.  An extremal `(v,M)` experiment may therefore
   re-choose the `K_6` model `M` in `G-v` after a collision.  This remains
   a generality check, not the primary route.

## Active links

### P1. General-model normalization or coherent two-vertex endgame — **OPEN**

From an arbitrary spanning labelled `K_7^vee` model, prove either

* a spanning singleton/bipartite shell satisfying P3, including two
  literal portals per singleton label; or
* a literal `K_7` model; or
* one fixed pair `a,b` for which `G-{a,b}` is planar.

This link may not assume that foreign bags are singleton or that the
deficient bag is bipartite.  Those are conclusions to be earned.

Two audited normalizations now precede the unresolved exchange.  In a
deficient-first nonspanning model the deficient bag is an induced path
whose four neutral portal classes are singleton `2+2` endpoint rows.
Re-spanning by whole exterior components preserves one fixed missing
twin and exposes an actual adhesion of order at least seven at every
absorbed lobe.  Sources:
`../results/hc7_near_k7_deficient_path_normalization.md` and
`../results/hc7_near_k7_coherent_spanning_transport.md`.

The endpoint shadow exchange is stronger than the former ordered-corridor
analysis.  If transport repairs either missing twin while `|P|>=2`, delete
a safe endpoint of `P` and absorb it into one of its two endpoint rows.
The cut edge restores that row, the repaired twin and opposite endpoint
rows survive, and the old missed twin plus the unabsorbed endpoint row are
exactly the two allowed missing spokes.  This strictly decreases the first
coordinate of the deficient-first model.  Therefore, in a target-free
host, every nontrivial normalized path and every exterior component meeting
it are anticomplete to both original twins.  Source:
`../results/hc7_near_k7_endpoint_shadow_exchange.md`.

This leaves two live normalization cells only.

* If `P` is a singleton, all remaining difficulty lies in the six
  generally nonsingleton foreign bags.  A labelled split, a full-adhesion
  equality-state splice, or one globally compatible two-apex expansion is
  required.
* If `|P|>=2`, the branch is genuinely both-missing.  Every incident lobe
  has adhesion contained in `P` and the four neutral bags.  The literal
  terminal is three pairwise adjacent shores, each meeting all four neutral
  rows.  Source: `../results/hc7_near_k7_literal_shore_completion.md`.

The nontrivial branch is now a crossed-frame society rather than an
arbitrary six-bag model.  Fixing `P` and minimizing one missed twin forces
that twin to be an induced `2+(at most 1)+2` portal path.  The full envelope
of `P` and its incident exterior components has an actual separator `S`
contained in the four neutral bags, with `|S|>=7`; some neutral bag is
multiply hit, and at `|S|=7` every member of `S` is full to every opposite
component.  Sources:
`../results/hc7_near_k7_both_missing_second_path.md` and
`../results/hc7_near_k7_both_missing_neutral_separator.md`.

Thus the next literal discharge is a surplus-root exchange: split one or
more multiply hit neutral bags while retaining the old `K_6` model, move
two surplus rooted pieces into the two missed twins, and keep one rooted
piece in each neutral row.  The resulting `S`-meeting `K_6`, together with
the envelope, is `K_7`.  Failure must be converted on the full actual
adhesion into a matching equality state or one compatible rural expansion;
mere endpoint allocation in the two paths is provably insufficient.

The internal donor obstruction is no longer informal.  Relative to a
connected core containing one protected root and one portal from every
foreign row, a surplus root outside the core lies in a monopoly-free
component: it transfers to either twin it meets, and otherwise exposes an
actual nested separator of order at least seven.  A surplus root belonging
to every such core canonically defines a detachable gate owning an entire
row portal family; if it cannot transfer to a met twin, it owns a second
literal row as well.  Source:
`../results/hc7_near_k7_surplus_core_gate.md`.  The live dynamic step is to
splice the state of these nested/multi-owner gates or prove that all of
their rural expansions use the same two actual apex vertices.

At an exact seven-adhesion, the literal transfer is now exhaustive up to
those two composition outputs.  Opposite protected-root choices give
disjoint canonical gates and disjoint monopoly sets, so one orientation
has deficiency at most two.  Distinct multiply hit donors provide two
freely assignable surplus pieces unless an actual adhesion or labelled
deficiency rotation occurs.  If all three surplus roots are concentrated
in one donor, two leaf edges of a marked spanning tree partition it into
two moved rooted pieces and one protected rooted core; this again gives
`K_7`, an actual adhesion, or a rotated `K_7^-`/`K_7^vee` model.  Source:
`../results/hc7_near_k7_surplus_root_transfer.md`.  Thus no exact-seven
root-distribution case remains; only well-founded composition of the
adhesion/rotation outputs remains.

Every actual exact-seven adhesion is now oriented toward one genuinely
thin open shore.  If `nu_i` is the maximum number of disjoint connected
subgraphs in shore `i` meeting all seven literal boundary vertices, then

\[
 \nu_1+\nu_2\le4,\qquad\min(\nu_1,\nu_2)=1,
 \qquad\omega(G[S])\le6-(\nu_1+\nu_2).
\]

This is stronger than the old component bound: it controls packets inside
one connected component.  The packet-rich/pair-rich side is closed by a
literal clique lift or by opposite proper-minor contractions inducing the
same equality partition.  Source:
`../results/hc7_exact_seven_packet_packing.md`.  Therefore the exact-seven
composition theorem may assume one connected shore has no two disjoint
full packets.  In the extremal `(1,3)` cell, any two disjoint adjacent
connected pieces of that thin shore which each contact at least six of the
seven boundary vertices force a literal `K_7` or the same exact two-block
state from opposite proper-minor operations.  Consequently the thin shore
is genuinely 2-connected and every one of its 2-cuts has exactly two lobes.
Moreover, literal portal matching plus rooted-`K_4` exchange closes every
four-connected thin shore and every planar three-connected thin shore.
Sources: `../results/hc7_exact7_thin_shore_exchange.md`,
`../results/hc7_exact7_portal_rooted_k4.md`, and
`../results/hc7_exact7_rooted_portal_face_closure.md`.  The exact
three-gate resource exchange further closes every nonplanar gate with at
least three lobes.  Hence a surviving actual three-cut has exactly two
lobes.  The forbidden-label matching exchange in those lobes closes every
shore of order at most seven, every literal triangle gate, and every
two-edge gate whose middle has a boundary portal.  The exact survivor has
order at least eight and a sparse gate (zero/one edge, or a two-edge path
with unlabelled middle); every literal gate edge has endpoint portal rank at
most one.  Sources:
`../results/hc7_exact7_three_gate_resource_exchange.md` and
`../results/hc7_exact7_two_lobe_gate_exchange.md`.

The gate itself now has an audited rooted-model funnel.  Every non-singleton
lobe contains a literal `K_3` model rooted at the three gate vertices.  If
the three rooted bags have an SDR of three literal boundary contacts, the
other lobe supplies a fourth carrier and the opposite packets complete a
literal `K_7`.  Hence every such rooted triangle in a survivor has portal
matching rank at most two, while the lobe-level matching theorem supplies
three distinct labelled portal vertices independently.  Source:
`../results/hc7_exact7_rooted_triangle_portal_rank.md`.

The remaining task is therefore either the labelled width-two web/state
exchange or the **maximal portal-rank triangle exchange** in this single
exact sparse two-lobe nonplanar gate resource.  The earlier median exchange
remains useful for a different object: the connector of three chosen
labelled arm sets inside a lobe.  It closes every arm-rooted triangle,
every Steiner `Y` with a usable gate or boundary-label edge, and every path
whose median is incompatible with the literal gate.  A one-edge or
unlabelled-middle path survivor therefore has one canonical median on each
such connector and nonadjacent leaf representatives; in the edgeless case
the arm connector can retain the narrower label-order alternative even
though a gate-rooted triangle is guaranteed.  Source:
`../results/hc7_exact7_sparse_gate_median_exchange.md`.  The next step must
turn the independent three labelled portals into rank three on a rooted
triangle, a matching proper-minor state, or a coherent two-vertex endgame.
Packing number one must not be replaced by an unproved bounded transversal.

The nested family is now linearized inside that exchange.  If a vertex of
either gate lobe has three or more deletion components, every component
sees at least two literal gate vertices and at least three literal boundary
labels.  Three components and the opposite lobe then give four explicitly
anchored clique carriers.  If instead a maximal two-connected block has
three distinct attachment cutvertices, root a `K_3` model at those
attachments and use the same gate/contact Hall lift; this again gives the
four carriers and a literal `K_7`.  Consequently every cutvertex node and
every block node has degree at most two, so the block--cutvertex tree of
each surviving lobe is a path.  Sources:
`../results/hc7_exact7_nested_cutvertex_exchange.md` and
`../results/hc7_exact7_block_chain_exchange.md`.  This is a linear block
order, not a claim that each lobe is a graph-theoretic path.  The rank-two
block chains are closed below; genuinely two-connected portal-monopoly
blocks remain.

The literal split and state outputs now share one exact interface.  Fix a
spanning gate-rooted triangle in one lobe.  If the opposite lobe can be
split into the prescribed connected star, two fresh boundary portals repair
a rank-two triangle and the four carriers lift to `K_7`.  Failure is
certified by crossed projection inequalities in **every** spanning tree;
for a tree lobe this is one crossed path order.  Source:
`../results/hc7_exact7_portal_rooted_triangle_exchange.md`.

For a portal-rank-two rooted triangle, the multi-block negative side first
becomes canonical.  At each cutvertex any gate-duty pair other than
`{i,j}|{i,k}` gives `K_7`; the crossed orientation is constant, its common
gate is literally `S`-unlabelled, and either cutvertex allocation yields
three spanning pairwise adjacent carriers with every palette support of
order at least four.  Source:
`../results/hc7_exact7_block_chain_list_exchange.md`.

More generally, let three connected pairwise adjacent carriers span the
thin shore and list at each `s in S` the carriers it contacts.  A proper
three-list-colouring of `G[S]` partitions `S` into independent blocks.
Contracting each block into its selected carrier on one side and into three
distinct full packets on the other produces the same exact equality state;
the two proper-minor six-colourings then glue.  Source:
`../results/hc7_exact7_triangle_list_state.md`.  The same proof holds
uniformly for strongly `k`-contraction-critical graphs with `q<=k-1`
spanning clique carriers opposite `q` full packets; see
`../results/hc7_uniform_carrier_list_state_gluing.md`.

The boundary obstruction itself is now exact.  After forced singleton
colours are propagated, every uncolourable state contains one of ten
critical cores; every nonconflicting survivor has at least five literal
vertices with exact two-colour lists.  Pair-list states are exact two-SAT,
so their obstruction is a contradictory pair of directed implication
paths (an implication bicycle).  The at-most-two full-list templates reduce
to the same certificate after branching.  Source:
`../results/hc7_exact7_triangle_list_critical.md`.

The raw list sweep has a stronger literal-model closure.  Pair-only states
lift through an anchored `K_4`; full raw lists lift directly by an SDR; and
every remaining no-model state has a forced unit-path certificate.  Sources:
`../results/hc7_exact7_pair_bicycle_completion.md` and
`../results/hc7_exact7_forced_path_completion.md`.

The audited boundary rooted-model trichotomy then closes the sweep instead
of transporting its certificates.  On a triangle-free literal seven-set,
support four for each of three carriers gives either a proper list-colouring,
an anchored `K_4`, or an edge `pq` with independent complement.  The last
outcome is the admissible equality state
`S-{p,q}|{p}|{q}` and glues using one full packet on each shore.  Source:
`../results/hc7_exact7_boundary_rooted_trichotomy.md`.  Consequently every
portal-rank-two rooted triangle has a cutvertex-free opposite lobe; the
entire multi-block rank-two branch is closed.  The live structural residue
is portal rank at most one, or rank two opposite a genuinely two-connected
lobe.  The next link must split that lobe into support-four carriers or turn
failure into a width-two/rural certificate with one fixed two-vertex
endgame.

The same boundary theorem gives a rank-free cut closure.  At a lobe
cutvertex, if both deletion sides meet exactly two gate vertices, those two
sides and the opposite lobe form a support-four spanning carrier triangle.
Thus every surviving cut has at least one full-gate side.  Its unresolved
lower-bound profiles are `4/3/4` and `3/3/4`; see
`../results/hc7_exact7_double_two_gate_cut_closure.md`.

That composition problem is now sharply oriented.  Every single-gate
rotation has an exact inverse, but consecutive two-hole missing pairs must
overlap.  If `mu` is the minimum deficient-centre order over all one- and
two-hole near models and `mu>=2`, every one-hole centre has order at least
`mu+1`; hence mixed rotations point away from the two-hole floor.  A
fixed-frame singleton continuation either backtracks or returns to a
two-hole floor state.  Moreover, a concentrated donor closes whenever a
selected root `r` has `U-r` 2-connected and at least two neighbours in
`U`.  Sources: `../results/hc7_near_k7_rotation_edge.md`,
`../results/hc7_near_k7_rotation_pair_overlap.md`,
`../results/hc7_near_k7_singleton_holonomy.md`,
`../results/hc7_near_k7_one_hole_height_gap.md`, and
`../results/hc7_near_k7_three_connected_concentrated_rotation.md`.

Thus the named unresolved P1 edge is the **pure two-hole width-two
composition theorem**: a robust rooted connector web, a frame-changing
nonsingleton gate, or a cutvertex/2-adhesion donor must yield one of
`K_7`, the same equality partition from proper-minor operations on opposite
open shores, or rural expansions with one fixed literal apex pair.  At a
shared pinch the required equality state and five colour-distinguished
entrances already exist, and critical-edge deletion equivalently produces
a five-chromatic core with two universally colour-saturating root sets.
Sources: `../results/hc7_near_k7_critical_pinch_state.md` and
`../results/hc7_critical_edge_double_saturation.md`.  Neither source by
itself forces the state collision or doubly rooted `K_5`; those are exactly
the palette-to-labelled-carrier gap to be discharged here.

In the overlap-one cell `D={a,b}`, `E={a,c}`, a detachable common-row
core touching an endpoint is no longer part of that gap: absorbing it into
`F_a` gives a one-hole model with the same centre.  If the connector has
three disjoint connected carriers—old-side `b`, middle `a`, and new-side
`c`—the seven literal bags are `X+L`, `F_a+K`, `W+R`, and the four
unchanged rows.  Sources:
`../results/hc7_near_k7_common_portal_absorption.md` and
`../results/hc7_near_k7_common_row_promotion.md`.  In a 4-connected
connector, two private rooted carriers give `K_7^-`; otherwise every
private portal lies on one facial cycle in the exact crossed labelled
order.  A common core cannot feed the two private sides through distinct
components without giving a literal `K_7`.  Source:
`../results/hc7_near_k7_common_row_rural_book.md`.  Hence a surviving
shared portal is a cut/two-row monopoly pinch or a single ordered rural
page; the false shortcut “four-connected connector implies a carrier” is
excluded by the minimal planar double-book in
`../barriers/hc7_near_k7_robust_carrier_4connected_barrier.md`.

The set-rooted strengthening is now audited: changing the selected
attachment vertices inside that same 4-connected connector cannot create
holonomy.  Absence of the private set linkage puts both whole root sets and
both private portal sets in one facial block order.  This leaves only
connector-torso changes, overlapping portal classes, actual
1-/2-adhesions, or the concentrated two-piece rotation as sources of
noncoherence.  Source:
`../results/hc7_near_k7_set_root_rural_order.md`.

Composition through a tree of simultaneously port-labelled planar torsos
is also audited.  Vertex/edge adhesions and non-overfull facial triangles
glue planarly; a fixed set of at most two actual vertices meeting every
overfull triangle gives the coherent two-apex output.  Thus small-adhesion
orientation chains have no holonomy of their own.  Source:
`../results/hc7_near_k7_torso_tree_apex_gluing.md`.  The first geometric
interface not covered there has order at least four or incompatible
overfull triangles.

At an order-at-least-four interface, the two-connected pointwise-full
subcase is terminal.  Two rural boundary cycles with different cyclic
orders contain a literal boundary-rooted `K_4` subdivision; equal orders
glue planarly.  Source: `../results/hc7_rural_cycle_order_exchange.md`.

The same exchange now preserves literal port edges before any contraction.
Two disjoint port cycles joined by a matching either glue as a planar
cylinder or yield four `K_4` branch sets, each retaining a different port
edge; four contiguous label blocks return one branch set of every label.
Source: `../results/hc7_port_matching_cycle_exchange.md`.  Thus quotient
rotation mismatch is terminal whenever the port endpoints are distinct and
the required three-row contacts are pointwise on those literal edges.

The point-contact hypothesis now has an audited unbounded extension.  A
port may be thickened to a disjoint cyclic sector carrying its three row
contacts; disjoint off-skeleton packets may repair all remaining duties;
and a same-row packet on one corner connection gives `K_7^-`, with the
literal floor centre preserved when applicable.  Matching equality states
from opposite open shores splice on the actual adhesion.  Source:
`../results/hc7_port_distributed_row_exchange.md`.  The remaining interface
is extraction of disjoint sectors/packets from overlapping contact spans,
multi-row or three-plus-duty deficiency, or state-disjoint opposite shores;
fullness to a component alone does not perform that extraction.

The web side of this interface is now uniform.  Two anticomplete connected
shores which are full to a Hamiltonian boundary frame, with at most three
external guards, give either a same-shore crossing or a planar remainder
after deleting the guards.  The planar remainder is terminal for all three
guards: the uniform clique-apex lifting theorem, specialized to Strong
Hadwiger for four colours, says that every seven-chromatic graph with a
three-vertex deletion to a four-colourable graph has a literal `K_7` minor.
Source: `../results/hc7_three_apex_planar_endgame.md`.  The guarded result also supplies the exact dynamic terminal for
the separated three-span branch: if both shores augment one common partition
of the actual adhesion into six pairwise adjacent connected carriers, the
two proper minors force that labelled partition on opposite closed sides and
their six-colourings glue.  Source:
`../results/hc7_guarded_cycle_web_exchange.md`.

At a lex-minimal detachable row lobe, exact two-owner support meeting the
missed row is no longer residual: transferring the lobe repairs the old hole
and returns a literal one- or two-hole near model.  In the complementary
branch seven-connectivity yields at least `4-|Z|` actual peer-side endpoints;
it does not turn two owner labels into a bounded cut.  Source:
`../results/hc7_contact_transversal_amplification.md`.  Thus the named live
edge is now **contact-to-carrier amplification**: use those actual endpoints
to construct either the packets required by the distributed-row lift, the
same six partition carriers on both shores, or the common rural system from
the guarded theorem.

The row-support part of that amplification is now exhaustive.  Comparing the
rotation and median reassignments of one detachable lobe sends every number
of owned/met rows to a missing-star model with at most two spokes, to
`K_7^-`, or to one exact `K_3\vee C_4` carrier whose two absent pairs are
independent.  Two disjoint diagonal packets close the last carrier literally.
Source: `../results/hc7_three_anchor_lobe_median.md`.  Accordingly the live
edge is no longer a support-mask enumeration: it is the label-preserving
linkage/state/web composition for this one carrier.

The three common carrier rows now have a uniform audited normalization.
In a lex-minimal six-duty row each non-cutvertex owns at least two disjoint
duties, so the row has at most three non-cutvertices and only edge/triangle
blocks.  Absorption closure plus seven-connectivity collapses the entire
three-root arm family to a literal triangle.  The sole unbounded row is an
induced path with at most two mobile portal classes; a path of order at least
seven has at least five internal mobile portals.  Source:
`../results/hc7_lexminimal_carrier_block_rigidity.md`.  Thus the next
literal discharge is the **mobile-path exchange**: combine the audited
bilateral full-palette cut on that bipartite path with its one/two mobile
label classes to obtain the diagonal packets, an opposite equality-state
splice, or a three-guard four-colourable torso tree.

The first constructive subfamilies of that exchange are explicit.  Merging
one rim edge of `K_2\vee C_4` leaves five literal clique carriers; two
label-exact packets attached to the two path shores complete a literal
`K_7`.  Protected two-portal supports supply those packets, leaving only
their audited rural/cutvertex/degenerate outputs.  The proof is in
`../results/hc7_mobile_path_exchange.md`; it does not infer physical packets
from palette colours.

Wholesale piece transfer, path-portal Helly, row promotion, protected
two-row linkage, rural-face descent, and full-adhesion equality states
remain available inside these cells; their sources are respectively
`../results/hc7_near_k7_wholesale_piece_transfer.md`,
`../results/hc7_near_k7_path_portal_helly.md`,
`../results/hc7_near_k7_rooted_triangle_promotion.md`,
`../results/hc7_near_k7_locked_two_row_linkage.md`,
`../results/hc7_near_k7_offface_transfer_closure.md`, and
`../results/hc7_near_k7_dynamic_locked_gate.md`.  None yet turns colours
inside a nonsingleton foreign bag into literal branch labels.

The tempting shortcut of contracting three common foreign bags to a
triangle and applying a rooted-`K_4` theorem is not lift-safe.  The graph
`K_2` joined with the icosahedron gives an exact seven-connected,
`K_7`-minor-free `K_3`-join-`C_4` quotient whose actual two apex vertices
are hidden inside nonsingleton common bags.  Thus quotient separators and
rurality are terminal only after full port-labelled expansion or a
colour-gluable state on the actual lifted adhesion.

The canonical universal rural family is fully terminal: if
`G=K_2 vee H` is seven-connected and `K_7`-minor-free, Wagner's theorem
forces `H` planar; a connected universal carrier of order at least three
already yields an explicit `K_7`.  Source:
`../results/hc7_near_k7_two_universal_rural_rigidity.md`.  The unresolved
capacity pieces are not yet known to be universal, which is why this does
not close P1 by itself.

The broader first-hit shortcut is now excluded by a sharp literal barrier.
For the icosahedron `T`, a vertex `z`, `R=T-z`, and
`H=K_2 vee R`, the seven-set `X=N_T(z) union V(K_2)` is robust through all
six-deletions and `H` has an unrooted `K_6`, but no `X`-meeting `K_6`.
Adding the vertex with neighbourhood `X` reconstructs the seven-connected,
`K_7`-minor-free graph `K_2 vee T`; its unique escape is the coherent
cofacial two-apex pair.  Source:
`../barriers/hc7_rooted_jorgensen_apex_barrier.md`.  Thus first-hit
robustness and an unrooted model cannot replace the actual-adhesion
proper-minor states.

An actual full adhesion is already colour-gluable whenever it has an
independent trace whose complement is uniquely 5-colourable; contracting
the two shores gives identical boundary partitions.  Source:
`../results/hc7_near_k7_rigid_boundary_splice.md`.  What remains is to
force such a trace, a labelled split, or the global planar pair on every
non-rigid order-seven/eight adhesion.

For a full exact seven-adhesion, every boundary with at most four missing
edges already gives `K_7`; the two sharp five-defect graphs are closed at
unbounded shore order by a same-shore crossing or two compatible planar
webs.  Sources: `../results/hc7_near_k7_exact7_boundary_threshold.md`,
`../results/hc7_near_k7_exact7_k322_web_closure.md`, and
`../results/hc7_near_k7_exact7_c5_web_closure.md`.

### P2. Bipartite total-contraction split — **GREEN**

For every connected induced bipartite carrier `X`, total contraction is
chromatically tight.  In every contraction colouring, every spanning tree
of `X` has an edge whose two connected sides simultaneously see all five
secondary colours.  Contracting the two sides gives an incompatible state
on the actual adhesion `N(X)`.

Source: `../results/hc7_near_k7_bipartite_total_contraction.md`.

### P3. Palette to literal labels in the singleton shell — **GREEN in its
scope**

For a spanning shell with one bipartite complex bag and five singleton
clique bags:

* every apex-nonneighbour label gives an all-but-one literal split;
* with `d>=2` deficient labels, same-side witnesses give `K_7` unless a
  `d`-set disconnects the bag or captures a whole portal class;
* for `d=2`, 3-connectivity plus three portals per label gives `K_7`.

Source: `../results/hc7_near_k7_palette_label_alignment.md`.

### P4. Singleton-shell exchange — **GREEN in its scope**

The unique-shadow subcase is **GREEN**: a saturated vertex and the two
poles lie on a common cycle in the 3-connected remainder, and the two
arcs of that cycle give a literal `K_7` model.  Source:
`../results/hc7_near_k7_rainbow_cycle_completion.md`.

For two deficient singleton labels, capture of an ordinary portal by the
two same-side witnesses is **GREEN**: a fixed ordinary triangle and the
five common roots give a rooted `K_4` or one planar face, while exact
capture makes one triangle neighbourhood nested and hence gives `K_7` or
a global two-apex pair.  Source:
`../results/hc7_near_k7_two_defect_rooted_face.md`.

The alternative in which the two witnesses disconnect the complex bag is
also **GREEN**: seven-connectivity gives exact literal contact rows on
every component, and two components assemble into seven explicit branch
sets.  Source: `../results/hc7_near_k7_two_defect_cut_closure.md`.

Consequently, once P1 has earned the audited spanning singleton/bipartite
shell and its two-portal multiplicity, P4 returns one of exactly three
terminal outputs:

1. a label-preserving split and literal `K_7` model;
2. matching marked states on opposite sides, hence a 6-colouring by
   crossed gluing; or
3. a rural embedding after deleting a named pair `a,b`.

No fourth “structured residue” is an acceptable conclusion.

### P5. Endgame — **GREEN once P1 holds**

The split branch gives `K_7`, contradicting minor exclusion.  The common
state branch gives a 6-colouring, contradicting criticality.  A fixed pair
whose deletion is `K_5`-minor-free leaves a four-colourable graph by `HC_5`,
so two fresh colours also give a 6-colouring.  The coherent planar 2-apex
branch is the principal stronger instance.  Hence no minimal counterexample
exists.

## Falsification gates

Before accepting a proof of P1, test it against:

* non-bipartite 3-connected deficient bags;
* a palette colour occurring in several foreign bags;
* the unique apex-shadow colour;
* two local rural pieces requiring different apex pairs;
* portal concentration on a 2-cut; and
* branch-set adjacency after every proposed transfer.

An argument failing one gate is terminated, not refined into labelled
casework.
