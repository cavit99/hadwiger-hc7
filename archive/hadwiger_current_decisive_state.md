# Hadwiger programme: current decisive state

**Audited internal state, 12 July 2026.**  This is not a proof announcement.
Hadwiger's Conjecture is known for `t <= 6`; neither `HC_7` nor the general
conjecture has been proved here.  The useful advance is that several
unbounded local obstructions have now been replaced by exact rooted-model
theorems.  The remaining work is no longer accurately described as a list
of small Moser cases, but it still has two theorem-strength gates.

## Audited advances that change the proof search

0. **Arbitrary near-clique models now have sixteen series--parallel
   normalization views.**  Any minor model in a connected graph can be
   made spanning by absorbing each unused component into an adjacent bag.
   Starting from an arbitrary spanning `K_7^vee` model, choose any three
   of the four neutral bags as a triangle `Q`, retain any complementary
   branch bag, and contract the other six bags.  This gives sixteen
   one-complex-bag views with three literal common-`Q` roots and one
   connected `Q`-full carrier.  Maximally refine that carrier into
   connected `Q`-full pieces.  If the contracted quotient has a `K_4`
   minor, it lifts with `Q` to a `K_7`; therefore every target-free view
   is a partial 2-tree.  Every original branch bag is retained in at
   least one view.  The sixteen structural views collapse to seven
   underlying retained-bag minors; with at least two complex original
   bags all are proper and six-colourable, but their repeated triangle
   designations are not independent colour states.  In the unique
   one-complex-bag case all nonretained-bag contractions are proper.  The unresolved object is now
   a `Q`-indecomposable bounded-leaf portal carrier on a quotient
   adhesion of order one or two, not an arbitrary near-clique model.

1. **Theta equality type: strict descent and closure at a minimum
   fragment.**  On the exact seven-boundary whose complement is

   \[
   \{01,02,05,12,15,24,45\},
   \]

   each of the crossbars `05|12` and `15|02` has a unique shore owner.
   A nonowner is either a forbidden singleton or contains a strictly
   smaller fragment behind a nested exact seven-cut.  The web proof is
   arbitrary-order: it removes one- and two-cuts, uses disk curvature to
   obtain two universal tags, and builds a `K_7` from them.

   The last same-owner lock is now also closed.  The `05|12` packet makes
   a cycle through `0,5,2,1`; a `15|02` packet in the same shore is an
   opposite-pair linkage.  Fabila-Monroy--Wood Lemma 7 gives a rooted
   `K_4`, and the unused full shore with singleton bags `3,6` completes a
   `K_7`.  Hence the two crossbars have opposite owners, both shores
   descend, and this theta type cannot occur at a globally minimum
   exact-seven fragment.

2. **Nested cuts transport relations, not boundary graphs.**  Across an
   annulus with outer boundary `S` and inner boundary `Z`, the exact datum
   is the labelled two-boundary six-colour relation

   \[
   T_A\subseteq[6]^S\times[6]^Z.
   \]

   Extension sets and every faithful deletion/contraction signature pull
   back through `T_A`, and annuli compose by relational composition.
   Seven disjoint paths transport the old boundary only as a rooted minor
   shell; they do not preserve its nonedges or equality partitions.
   Thus theta descent is valid, but it cannot be iterated by pretending
   that every inner boundary is theta.

3. **Near-`K_7`: four defect-one pieces close uniformly.**  In the
   one-complex-bag shell `K_6-{ab,ac}`, four consecutive disjoint connected
   pieces, each missing at most one shell label, always give a `K_7`.
   Three pieces are negative only for ten explicit defect words; an edge
   between the first and third pieces closes every one of them.  For a
   spanning exceptional triple, deleting two neutral labels leaves a
   uniquely embedded maximal-planar quotient.  Therefore either a local
   society/parallel-bundle rotation is incompatible, or all rotations are
   rural and coherent and the whole graph is two-apex.  This is a
   structural, arbitrary-order statement about pieces, not an order-bounded
   graph enumeration.

4. **Nested neutral triangle theorem.**  If a triangle
   `Q={q1,q2,q3}` in a seven-connected graph satisfies

   \[
   N_{G-Q}(q_3)\subseteq
   N_{G-Q}(q_1)\cap N_{G-Q}(q_2),
   \]

   then the graph has a `K_7` minor or deleting `q1,q2` leaves a planar
   graph.  The proof applies the rooted-`K_4` theorem in the
   four-connected graph `G-Q`.  Consequently a hypothetical minimal
   `HC_7` counterexample has three literal anti-nesting witnesses at every
   such triangle.  A four-vertex common portal core already gives a
   rooted `K_4` or one common face; the two-apex conclusion additionally
   needs every private portal of the third vertex on that face.

5. **Exact surviving near-clique cross state.**  The independently rerun
   cross-split atlas closes every mixed exceptional word.  In a homogeneous
   negative word, every inclusion-maximal split has exactly four common
   external owner classes; five common classes give a `K_7`.  Combined
   with seven-connectivity and the nested-triangle theorem, the residue is
   a literal **four-common-owner capacity lock** with distributed portal
   surplus and three private anti-nesting witnesses.  At the retained-web
   level it is the first incompatible rural rotation/owner-set conflict in
   a chain of at most three exceptional defect-one pieces.  Defect-two
   pieces and failure of the retained decomposition remain outside this
   local theorem.

6. **Every indecomposable carrier has one adhesion-two rainbow torso.**
   Project the inclusion-minimal connected transversals of its portal
   classes to any tree decomposition.  They are pairwise intersecting,
   so subtree Helly gives one common bag meeting every transversal; every
   component outside that bag is portal-dark and attaches through one
   adhesion.  In the Tutte decomposition the common torso is exactly a
   one/two-vertex gate, a cycle, or a 3-connected torso.  This removes
   arbitrary block trees and arbitrary chains of 2-separations at once.
   The result and an independent GREEN audit are in
   `hadwiger_rainbow_torso_helly_core.md` and
   `hadwiger_rainbow_helly_core_audit.md`.

7. **Biportal rooted cores now close uniformly.**  Suppose a torso has a
   rooted `K_r`, each rooted bag has a disjoint extension meeting both
   boundary pools and one reserved biportal bag, and an opposite connected
   set is full to the boundary.  The rooted bags, the reserve, and the two
   pooled boundary bags form a literal `K_{r+3}` model.  For `r=4`, the
   rooted-`K_4` theorem therefore gives `K_7` or one precise rooted web;
   in a 4-connected torso the alternative is planar and cofacial.  This
   closes the whole arbitrary-order biportal 3-connected carrier family.
   The proved and audited statements are in
   `hadwiger_biportal_rooted_k4_web_exchange.md` and its audit.

8. **Full-shore owner pooling collapses Hall failure to one zero row.**
   If a protected `m`-frame lies outside a boundary split
   `S=B dotcup T`, every frame bag sees both pools, and one connected set
   is full to `S`, then the frame, `B`, and the pooled bag `R union T`
   form `K_{m+2}`.  Distinct boundary representatives are unnecessary.
   In particular a target-free frame with one common portal `s` has a
   literal bag whose entire boundary row is `{s}`.  In a covered minimum
   seven-fragment that row forces at least seven distinct internal contact
   vertices and hence a double-hit owner.  This is uniform in the target
   order; the exact theorem and its sharp static counterarchitecture are
   in `hadwiger_two_pool_hall_lock.md`.

9. **Seven-view state cocycle.**  The sixteen `Q`-full normalizations are
   only seven underlying retained-bag colour minors: the four structural
   views retaining each of `A,B,C` repeat the same contraction map.
   Equality states alone have no cross-view parity; a `K_7`-minor-free
   leaf expansion of `K_7^vee` realizes every independent `AB/AC` choice
   in the four neutral views.  In the first faithful cell, where the four
   neutral carriers are edges and each rigidly permits one repeated state,
   a portal matching bit `s_ij` joins each pair.  With state bits `t_i`, a
   mismatch `s_ij != t_i xor t_j` gives an explicit `K_7` model, while
   the flat selected skeleton `s=delta t` switches into two `K_4` layers
   and has an explicit six-colouring.  Extra wrong-layer edges are governed
   by an exact bipartite cross-nonedge relation.  The preliminary
   canonical-deletion analysis remains valid, but it is no longer the
   closure mechanism: the stronger matching theorem in item 11 treats the
   full literal host directly.  The reusable invariant supplied here is an
   operation-sensitive portal relation whose first coordinate is a signed
   cocycle, not an equality partition.  The minor half already extends to
   any number of arbitrary connected two-shore carriers:
   wrong holonomy gives `K_{n+3}`, while flat holonomy gives two coherent
   labelled `K_n` models.  What remains open is forcing those two connected
   state shores, and transporting the full operation relation, inside an
   indecomposable unbounded carrier.

10. **Noncanonical palette states have bounded deficiency.**  In an
   `(n+2)`-colouring after deleting an operated cross edge, the two
   `K_n` carrier layers omit two colours each, so their palette distance is
   only `d=0,1,2`.  The common colours give a cross-nonedge matching of
   size `n-d` containing the operated edge.  Distance zero is canonical;
   distance one exposes at least one boundary-reusable `p` shore; distance
   two exposes one `p` shore of each type.  Hence the remaining
   canonicalization problem is a deficiency-one/two
   Dulmage--Mendelsohn augmentation rooted at the edge-critical common
   colour, not an unbounded portal enumeration.  The exact theorem is in
   `hadwiger_noncanonical_two_palette_transition.md`.

11. **The full literal edge-carrier cell is closed uniformly.**  In fact
    the operated-colour normalization is unnecessary once the carrier
    shores are literal vertices.  Let `M` be the cross-nonedge graph of
    the two clique layers.  A perfect matching colours the host; matching
    co-rank at least two gives a large core clique completed by `{b,c}`;
    at co-rank one, a favourable unmatched type reuses a boundary colour,
    while otherwise the alternating-reachability minimum cover gives a
    labelled `K_{n+1}` core completed by `{a,b,x_r}` and `{c}`.  Hence
    every full literal edge-carrier host is `(n+2)`-colourable or has a
    `K_{n+3}` minor, for every `n>=4`.  For arbitrary connected two-shore
    carriers the same proof leaves only perfect compatible transport or
    one favourable exposed shore; every other state is already the target
    minor.  This is the first full arbitrary-order rooted-model principle
    extracted from the portal programme.  Its proof and independent audit
    are in `hadwiger_flat_full_host_matching_dichotomy.md` and
    `hadwiger_flat_full_host_matching_dichotomy_audit.md`.

12. **A typed shore exists unless the carrier has a two-vertex gate.**
    Let a connected carrier have three nonempty portal classes `A,B,C`.
    Protected-source Menger gives either disjoint adjacent connected
    shores with rows `AB|BC`, or one vertex meeting every
    `(A union C)`--`B` path.  Interchanging `B,C` gives either the other
    row `AC|BC`, or a second one-vertex gate.  Therefore every carrier
    has one of the two state-shore splits needed by item 11, unless all
    rainbow connectivity is confined by an explicit gate of order at
    most two; every off-gate component is portal-dark.  This remains valid
    for overlapping portal sets and order-one paths and was checked on
    129,650 small rooted instances.  The theorem and independent audit are
    in `hadwiger_state_shore_or_two_gate.md` and
    `hadwiger_state_shore_or_two_gate_audit.md`.

    Thus the live Gate A is sharper than merely forcing a split inside one
    carrier: it is to make independently extracted shores transport
    compatibly between carriers, or to lift their gates through the
    combined carrier network.

13. **Full typed shores retain every inter-carrier row.**  The preceding
    three-row split has a stronger cross-Helly form.  Put every neutral or
    model portal row into both the left- and right-state carrier
    definitions.  If disjoint left/right carriers exist, they extend to a
    partition of the whole branch bag into adjacent connected typed shores.
    If they do not, projection to any tree decomposition gives two
    cross-intersecting subtree families: either one family is Helly, or two
    disjoint traces force every trace of the other family through their
    joining path.  Hence one bag meets every carrier of one state half.  In
    a Tutte decomposition this is one gate, cycle, or 3-connected torso,
    with every off-torso lobe missing a named row and attaching through at
    most two vertices.

    If every retained carrier takes the split outcome, both shores meet
    every other carrier.  Each resulting `2 by 2` contact graph has no
    isolated vertex and therefore has a perfect matching; the whole
    arbitrary-order system enters the signed-cocycle/two-layer theorem
    without any portal enumeration.  This theorem and its independent
    GREEN audit are in `hadwiger_full_state_shore_bihelly.md` and
    `hadwiger_full_state_shore_bihelly_audit.md`.

14. **Two four-connected rooted torsos with four columns close.**  Two
    different four-root cycle rotations already give a rooted `K_4`.
    More strongly, contract four genuine disjoint labelled columns between
    two four-connected pages.  Their union is four-connected, and each
    page has a component outside the roots which is full to all four.
    The rooted-`K_4` cofacial alternative would then contain two disjoint
    paths joining alternating facial pairs, a planar impossibility.  Thus
    the rooted model lifts with every named column and the biportal theorem
    completes `K_7`.  The compatible three-connected residue is an exact
    three-separator or a portal-deficient lobe.  The theorem and audit are
    in `hadwiger_first_incompatible_rotation_two_torso.md` and its audit.

15. **One-carrier quotient cuts now lift at arbitrary order.**  At a
    quotient cut containing one complex carrier, full-state cross-Helly
    gives a typed split or a gate of order at most two.  If no component
    behind the gate meets both quotient shores, the neutral triangle, the
    possible singleton cut vertex, and the gate form an actual separator
    of order at most six, contradicting seven-connectivity.  Hence the
    sole residue is one straddling lobe with a named missing row; for the
    elementary three-row gate it is in fact portal-monochromatic.

    For a two-carrier quotient cut, every combined separator of order at
    most three similarly lifts to a forbidden cut, so the combined network
    has four disjoint left--right paths.  Two individual two-gates either
    leave a combined straddler or form one exact seven-vertex adhesion.
    This is tight: a verified two-star network with two complementary
    `K_{3,3}` cross-lobe blocks has no typed split, combined separator six,
    no common missing label, and no rural embedding.  Thus connectivity
    and path surplus alone cannot finish Gate A; minor-critical
    state-forcing is essential.  The theorem, counterarchitecture, and
    audit are in `hadwiger_gate_a_combined_network_round.md` and
    `hadwiger_qfull_carrier_adhesion_lift_audit_addendum.md`.

## The two decisive remaining gates

### Gate A: boundary-faithful lifting of the normalized carrier

Every non-six-colourable graph has a `K_7^\vee` minor by the known
near-clique theorem.  The normalization theorem gives sixteen structural
`Q`-views but only seven underlying retained-bag minors.  A retained view
is proper precisely when a nonretained bag is nontrivial, so the
unique-complex-bag case remains a separate normalization outcome.  In
every target-free structural view the `Q`-full quotient is a partial
2-tree.  What remains is the faithful lift back through its one- or
two-carrier adhesions.  Inside each carrier, item 12 now supplies a typed
split or an explicit gate of order at most two.  A quotient cut
vertex may represent an arbitrarily large portal tree; contracting it
coalesces labels and does not preserve seven-connectivity.  The missing
theorem must align the splits and inter-carrier contacts across two
views, lift the gates through the combined carrier network, or identify
a coherent apex pair.  Multiple complex bags,
defect-two pieces, and portal concentration are precisely the possible
failures of this lift.  No local closure should be advertised as `HC_7`
until this lifting theorem is proved.

### Gate B: uniform retained-interface exchange

At the normalized interface, prove one label-preserving exchange theorem:

> A first rural-rotation/owner-capacity conflict either splits a labelled
> branch bag to form `K_7`, exposes the same faithful six-colour state on
> opposite shores, or forces one globally coherent pair of apex vertices.

The torso--Helly, full-state cross-Helly, and biportal theorems sharpen
this gate.  Every carrier either supplies full typed shores or is already
reduced to one gate, cycle, or 3-connected torso; four disjoint biportal
root extensions plus one reserve give `K_7` or the exact rooted-web
alternative.  Once four genuine columns join two four-connected torsos,
item 14 closes them regardless of rotation.  Thus the live selection
problem is to obtain those columns/extensions from the named missing-row
lobes, or prove that their failure makes all cofacial orders compatible
with one apex pair.  With two
quotient carriers, cross-edges must still be stabilized in the combined
carrier network.  The theta theorem shows the desired pattern in one full
equality type--operation-state ownership, rooted linkage, then strict
descent--but transfer through a non-theta annulus still requires the full
relation code, not a single equality bit.

## Counterarchitectures that delimit any valid proof

* A connected `K_7`-minor-free permutation annulus, followed by its inverse,
  has seven disjoint boundary paths but returns every labelled colour state.
  Therefore neither linkage nor boundary partitions alone can define a
  strictly decreasing nested-cut potential.  Contraction-criticality or a
  faithful operation-state exchange must do real work.
* The ten-vertex graph `K_3` joined to a seven-vertex 2-tree is
  `K_7`-minor-free and not two-apex, while exhibiting the homogeneous
  near-clique portal pattern.  Its connectivity is exactly five.  It shows
  why owner-class incidence is weaker than literal portal nesting and why
  seven-connectivity must be used at vertex level.
* Static theta rail absorption has center-only obstructions: neither a
  median portal nor a retained rail component need capture the required
  labels.  The successful theta proof works through rooted-cycle linkage
  and operation-state ownership, not through a purely geometric median
  claim.

## What would prove `HC_7`

Gates A and B together are sufficient.  A minor-minimal counterexample is
seven-connected, non-six-colourable, and contains a `K_7^\vee` minor.
Gate A would lift one normalized partial-2-tree interface faithfully back
to the original model.
Gate B would then give a `K_7`; or a common faithful state, which crossed
splicing turns into a six-colouring; or a coherent two-apex graph, also
six-colourable.  Every outcome contradicts the counterexample.

At present minor-level normalization is proved, but faithful carrier
lifting and the uniform portal exchange are not.  The honest frontier is
therefore: the theta minimum-fragment type is closed and the near-clique
residue is sharp, but the carrier-lifting theorem needed to finish
`HC_7` remains open.
