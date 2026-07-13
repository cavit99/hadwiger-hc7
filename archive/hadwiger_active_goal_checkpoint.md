# Active-goal checkpoint: exact transfers, contact adhesions, and the remaining locks

> **Supersession notice (2026-07-12).**  Any statement below claiming
> complete closure of the six-defect (C_6\dot\cup K_1) boundary is
> retracted.  The SPQR leaf-reflection step does not preserve portal
> cofaciality.  See
> `hadwiger_c6_closure_spotcheck_counteraudit.md` and
> `c6_rank_four_leaf_counterexample.py`.  The safe six-defect residue
> is a nontrivial SPQR tree with a rank-two/rank-two portal-face
> transition.

## Status

This checkpoint records only results proved and audited during the current
execution round.  It is not a proof of Hadwiger's Conjecture.  Its purpose is
to keep the two live closure programmes synchronized.

## 1. General least-counterexample advances

Let `t` be the least failing parameter, let `r=t-1`, and let `G` be a
proper-minor-minimal counterexample.

### 1.1 Portalized exact transfer

`hadwiger_portal_exact_boundary_transfer.md` proves exact state transfer for
an adhesion `X=N(v) union portals`.  If the complement of a piece
clique-realizes an exact partition `Pi`, then `Pi` extends over that piece.
For every label-preserving one-step deletion or contraction in one piece,
minor-criticality forces a new low-neighborhood state which is admitted by
all other pieces and was not admitted by the original piece.

### 1.2 Full-shore exact-block hypergraph

`hadwiger_exact_block_hypergraph.md` proves the following.  Across a
separation with two connected full shores, the two side extension families
are disjoint, but each family contains a state having every prescribed
nonempty independent `P subset S` as an exact block.  Hence the associated
exact-block hypergraph has Property B.

Consequences:

* If `G[S-P]` has a unique partition into at most `r-1` independent blocks,
  the separation is impossible.
* In particular, it is enough that `G[S-P]` be complete; no completeness
  between `P` and `S-P` is needed.
* More generally the palette-tight uniquely `(r-1)`-colourable remainder is
  impossible.
* The missing-edge graph `Q=complement(G[S])` is nonsplit, and therefore
  contains an induced `2K2`, `C4`, or `C5`.
* When `|S|<=r`, nonsplitness is also the exact limit of the static
  Property-B argument: parity of the number of blocks gives a Property-B
  colouring for every nonsplit `Q`.

Thus further progress past the nonsplit cores must use minor transitions,
linkage, or branch-set augmentation rather than static extension sets alone.

### 1.3 Full-shore minor augmentation

If a connected open shore `D` touches every vertex of `S`, then adjoining
`D` to a clique model in `G[S]` raises its order by one.  Consequently every
counterexample-derived full-shore contact adhesion satisfies

    eta(G[S]) <= t-2.

For the pair-pair boundary
`complement(G[S])=2K2 + isolates`, the boundary has an explicit
`K_(|S|-1)` model; the full shore gives `K_|S|`.  Hence

    kappa(G) <= |S| <= t-1.

For `t=7`, Mader connectivity gives `kappa(G)>=7`, so this entire contact
cell is impossible.  This supersedes the earlier alternating-web residual
for that exact boundary.

The analogous exact core `Q=C4+isolates` is also killed in the `t=7`,
`|S|=7` cell by using both full shores.  If the core of `G[S]` is the two
disjoint edges `x1x2,y1y2`, use the bags

    D_A union {x1,x2}, {y1}, {y2}, the isolate-complement singletons, D_B.

They form `K_|S|`.

The exact quotient classification is now complete through five missing
edges.  Every order-seven boundary with at most four missing edges gives a
`K7` model from the two full shores.  With five missing edges there are
exactly two quotient exceptions:

    Q=C5+2 isolates,        Q=K3+2K2.

If `G-S` has a third component, seven-connectivity makes it a third full
shore and both exceptions close by explicit models.  Thus either sharp core
has exactly two shores.  Both two-shore exceptions are now closed for
shores of arbitrary order, without the earlier finite order restrictions.

For `Q=C5+2 isolates`, put a five-terminal auxiliary graph on each shore,
ordered by the complementary boundary `C5`.  A crossing gives an explicit
`K7` model using the opposite full shore.  Otherwise the generalized Two
Paths Theorem completes each auxiliary graph to a same-vertex `5`-web.
Seven-connectivity removes every inserted clique, and the two bare disk
ribs glue to show that `G` minus the two universal boundary vertices is
planar.  The Four Color Theorem plus two fresh colours gives a six-colouring.
The full proof is `hadwiger_c5_full_web_closure.md`.

For `Q=K3+2K2`, label the missing edges `01,02,12,34,56` and use the
four-terminal order `(1,3,2,4)` on each shore.  A crossing repairs `12`
and `34`; together with the opposite shore the explicit bags

    {1}, {3}, {5}, D_other, {0,6}, X union {2}, Y union {4}

form a `K7` model.  In the crossless alternative, the two same-vertex
`4`-web ribs are bare by seven-connectivity and glue to make
`G-{0,5,6}` planar.  Four colours on that graph, one fresh colour on `0`,
and one shared fresh colour on the nonadjacent pair `5,6` give six colours.
The full proof is `hadwiger_k322_full_web_closure.md`.

Thus neither sharp order-seven full-shore core survives.

The next exact boundary layer has six missing edges.  An exhaustive labelled
atlas (`contact_order7_six_edge_atlas.py`) reduces its 54,264 labelled cases
to twelve unlabelled two-full-shore quotient types.  The relaxed web theorem
only requires the actual boundary graph on the cyclic terminals to be a
subgraph of the chosen cyclic frame; absent frame edges may be added in the
same-vertex web completion and discarded from the final planar supergraph.
Crossing certificates and this relaxation eliminate eight of the twelve
types for shores of arbitrary order.  Two further types have split missing
graphs and are forbidden already by exact-block nonsplitness.  Of the two
remaining types, `Q=2K3+K1` is now closed completely by the two-piece
surgery theorem in `hadwiger_k33_full_shore_closure.md`.  In any connected
bipartition of a shore, either one contact side lies in a cross-triangle
`{c,a,b}`, or seven explicit bags give a `K7` model.  Seven-connectivity
then makes both shores internally four-connected and forces each of the two
independent boundary triples to have a rooted `K3` in either shore.  Taking
opposite rooted triples and the universal boundary vertex gives `K7`.
The dependency-free atlas checks all 2,187 contact pairs and finds exactly
the 18 maximal triangle-limited obstructions used by the hand proof.

Consequently the sole genuine six-edge contact boundary left at that stage
was

    Q = C6 + K1.

Here `Q` is the missing-edge graph on the seven boundary vertices.  The
classification and explicit crossing tables are recorded in
`hadwiger_six_edge_web_closures.md` and
`hadwiger_two_shore_web_gluing.md`.

The `C6+K1` cell is no longer an unconstrained quotient.  The
exact adjacent-piece atlas in `hadwiger_c6_two_piece_locks.md` has 28
maximal bad defect pairs and proves, by a hand connectivity argument, that
every nonsingleton shore has order at least four, is internally
2-connected, and has exactly two components behind every internal 2-cut.
The crossing analysis in `hadwiger_c6_crossing_portal_lock.md` turns every
one of the six cyclic crossings into a pair of mutually reversed portal
separations.  If one shore is a singleton, the opposite side realizes all
six exact one-edge boundary states; Kempe switching and tree packaging give
a rooted `K5` with a single reserved-contact rerouting still required.

More importantly, these calculations have now been repackaged in the
label-free theorem `hadwiger_defect_atlas_connectivity_principle.md`.  For
an arbitrary boundary graph `J`, let `B_k(J)` be the downward-closed family
of contact pairs for which splitting one shore into two adjacent pieces and
contracting the opposite full shore does not give `K_k`; let `beta_k(J)` be
the maximum smaller contact-row size in this family.  In a
`lambda`-connected host, every full shore has no internal separator of
order below `lambda-beta_k(J)`.  A companion locality theorem transfers the
same bad-split classification to every small connected portal set.  This
is the uniform principle behind the 4-connectivity/rooted-triangle closure
of `2K3+K1` and the 2-connected web lock of `C6+K1`; it replaces further
edge-count marching by a bad-split-to-rooted-model-or-web programme.

Two further label-free lemmas now extend that programme.  The defect-star
theorem in `hadwiger_defect_star_principle.md` bounds the number of
components behind any internal shore separator directly from a finite
invariant of the bad-split relation; it specializes to the hand proof that
every `C6+K1` two-cut has exactly two sides.  The rooted-assembly criterion
in `hadwiger_defect_atlas_rooted_assembly.md` says that when the bad width
forces enough internal connectivity and the local portal rows are thin on
two completely joined boundary classes, the shores contain the prescribed
rooted clique models and assemble the target clique minor.  This theorem
recovers the entire `2K3+K1` proof without its labels.  The only mechanism
not yet supplied is the balanced chain/uncrossing alternative: cyclic bad
transitions must either compose to a positive rooted model or uncross into
a periodic web across which the minor colourings glue.

## 2. Degree-seven pure-Moser reserved connector

Fix repeated pair `a=1,b=3`, unique roots
`U={0,2,4,5,6}`, and missing-root cycle
`05,25,24,46,06`.

### 2.1 Portal transfer

`hadwiger_reserved_connector_portal_transfer.md` proves a bilateral
four-block transfer across an `a-b` separation in `H=G-v`, correctly
handling the apex bypass by contracting `{v,a,b}`.  A fifth portal-only
block is allowed when it is adjacent to the star image.  Any bilateral
realization of one missing-root pair plus the other three root blocks
therefore colours `G` with six colours.

### 2.2 Full seven-connectivity at an order-six adhesion

Let `S=U union {w}` be inclusion-minimal subject to containing `U` and
separating `a,b`.  Full `kappa(G)>=7` proves:

* `H-S` has only the `a`- and `b`-components;
* every component of `R_a-a` has external neighborhood exactly
  `S union {a}`, and symmetrically at `b`;
* three or more such terminal-side pieces give an explicit
  `N(v)`-meeting `K6`.

Thus each side consists of its terminal and one connected full shore.

### 2.3 Complete two-exterior closure and small portal shores

The older two-exterior pure-Moser case is fully closed by the supported-pair
transfer theorem in `hadwiger_moser_supported_pair_transfer_closure.md`.
For two vertex-disjoint missing-pentagon edges supported in one component,
their disjoint bichromatic paths plus a shortest connector realize an exact
triple-pair state on the opposite side.  Exact-state exclusivity and
two-anchor coverage then forbid every mixed support word; a confined word
gives the rooted `K5` and hence `K7`.  Together with the labelled
seven-vertex neighbourhood atlas and the two-anchor elimination of the
one-edge Moser extension, this proves that a degree-seven vertex has no
two-component exterior.

For the distinct order-six reserved-connector separation, the same local
certificate programme gives the following size bound.

The same note and independent verifiers prove that either distinguished
shore has order at least six.

* Order one contradicts the degree of the terminal.
* An order-two shore is excluded against an arbitrary opposite shore by
  49 explicit quotient `K6` certificates.
* A three-vertex path is excluded by 2,729 explicit certificates.
* For a triangle shore, 5,047 of 5,051 canonical attachment systems have
  explicit `K6` certificates; the four exceptions contain a literal
  six-vertex cut, contradicting seven-connectivity.
* All six connected order-four shore types are excluded over 2,820,640
  canonical attachment systems.
* All 21 connected order-five shore types are excluded by 8,928 monotone
  model supports, independently replayed over every labelled attachment
  system.

The current exact order-six lock is therefore

    |D_a|>=6 and |D_b|>=6,

with both shores connected and fully attached to their six portals and
their terminal.  `hadwiger_relative_shore_contraction.md` proves that in a
minimum no-model shore every internal edge is either terminal-tight or is
protected by an exact order-seven separator.  Uncrossing those tight
separators is the next structural task.  Separators of order greater than
six remain a separate reserved-connector issue.

### 2.4 All-crossless pentagram curvature

`hadwiger_reserved_connector_rank_leaf.md` and
`hadwiger_moser_pentagram_curvature.md` add an unbounded structural reduction.
In a three-connected shore, crosslessness of any three missing-(C_5) frames
forces all five crossless by an exact occurrence-level disk theorem (40 weak
circular-order systems, all unsatisfiable).  All five root portal sets then
lie on one facial cycle in pentagram order.

Portal sets for the ends of a missing edge need not be disjoint.  The exact
replacement is: if (x\in P_i\cap P_{i+1}), then

    P_(i+3)={x}.

Consequently every shore vertex has either at most two (U)-contacts forming
a present edge of `G[U]`, or the exact triple profile
`{i,i+1,i+3}` with a unique opposite portal.  A wheel realization and
`moser_c5_portal_overlap_probe.py` show that the triple exception is genuine;
the stronger disjointness assertion is false.

Triangulated-disk curvature now forces either an interior vertex of shore
degree five seeing exactly `w,a`, or an outer-face vertex of shore degree
three.  The latter has either a present (U)-pair and sees both `w,a`, or is
a triple-lock.  Every degree-seven triple-lock is impossible: its two facial
neighbours are nonadjacent (otherwise a Jordan triangle cuts off an interior
component by at most five vertices), and Dirac then forces its unique opposite
portal to see one of them, contradicting uniqueness.

Contracting the connected remainder `D-x` gives a defect-at-most-one body.
The exhaustive quotient replay `moser_curvature_quotient_probe.py` closes
degree-eight triple-locks based on missing pairs `52,24,46`.  Thus the exact
triple curvature residual is only the two degree-eight profiles based on
`05` and `60`, with `x` seeing both `w,a`.  The interior profile and most
ordinary-pair profiles remain.  In a minimum shore their three or five
incident edges are terminal-tight or carry exact order-seven witnesses;
crossing those witnesses is the current geometric obstruction.

The simultaneous five-terminal interpretation has now been audited.  If
both reserved shores are all-crossless, edge-maximal crossless completions
give two bare pentagonal webs with the same labelled boundary cycle.  Glue
their disks along that cycle, four-colour the resulting sphere graph, give
`a,b` one fresh common colour and `w,v` a second fresh common colour, and
obtain a six-colouring of `G`.  Thus the two shores cannot both be
all-crossless.  At minimum shore order six, the complete portal-profile
audit is even sharper: every three-connected all-crossless shore is a
six-vertex wheel with one of ten incidences, and all proper six-colour
states of its seven-label boundary extend through it.  Deleting the shore
then contradicts minor-criticality.  The unbounded residual is therefore
an extension-preserving web reduction or a tight seven-separator, not an
unresolved finite wheel list.

`hadwiger_allcrossless_wheel_closure.md` removes the word "minimum" for
the entire wheel family.  The exact five/six-occurrence circular theorem
shows that a longer all-crossless wheel has a unique triple-lock and every
other rim vertex has the same complementary present-pair profile.  Deleting
the triple vertex from the rim then has relative boundary exactly six,
contradicting the seven-cut inequality.  Hence every such wheel is one of
the ten six-vertex systems and is boundary-universal.  All thirty
high-root/nonstar transition states are therefore impossible on an
arbitrary-order wheel; the unresolved all-crossless core is genuinely
non-wheel planar geometry.

## 3. Degree-eight portal transitions

`hadwiger_degree8_portal_transition_smallpieces.md` proves, with an
independent exhaustive verifier, that the sharp `K3 disjoint-union C5`
static portal obstruction cannot satisfy every forced one-step transition
when all three connected piece interiors have order at most two.  The
replay checks 2,355 exact states, 215 branch signatures, 156 exterior
signatures, and 7,211,100 compatible triples.  Hence some piece in any
surviving exact-defect architecture has order at least three.

`hadwiger_degree89_apex_web_closure.md` adds an unbounded structural
family.  For a sole exterior shore, a full induced `C4`/`C5` frame with at
most three effective omitted contacts gives either an explicit crossing
`K7` or a planar `G-Z`, hence a six-colouring.  It applies directly to the
degree-eight one-component frame cell and to the degree-nine cell when a
nonempty defect lies in `Z`.  A two-shore version closes the corresponding
cells when `Z` is independent, and a safe-cycle extension closes a further
bipartite common-defect family.  These are conditional frame theorems, not
yet a classification of all degree-eight or degree-nine neighborhoods.

## 4. Exact remaining objectives

The current round has not closed `HC7` or the all-`t` conjecture.  The
live, non-equivalent gaps are:

1. continue the now-complete six-edge boundary induction into denser
   missing graphs, using the `C6+K1` closure as the structural template;
2. split either full shore in the order-six Moser reserved-connector cell,
   now reduced in its three-connected all-crossless branch to the interior
   curvature profile, ordinary degree-three profiles, and the two
   degree-eight triple-locks `05/60`;
3. extend the exact degree-eight portal-transition exclusion beyond
   two-vertex pieces and to the other one/two-component cells;
4. turn the general nonsplit contact adhesion plus one-step transitions
   into a contact augmentation or a colour-gluable separator for every
   least failing `t`.

## 5. Label-free machinery extracted from the local cells

The local web work now yields two results which no longer mention the
Moser labels or a particular missing cycle.

First, `hadwiger_terminal_specific_two_shore_web.md` permits two
anticomplete shores to have different small exposure sets outside one
cyclic terminal frame.  If

    kappa(G) > 3 + max(side-exposure size),

then either one ordered terminal tuple is crossed, or deleting the union
of the exposure labels leaves a planar graph.  The latter has the uniform
colour bound `4+chi(exposure)`.  This strictly strengthens the earlier
common-full-boundary web lemma and is exactly what makes the bilateral
reserved-connector gluing valid at connectivity seven.

Second, `hadwiger_label_free_portal_splitter.md` treats an arbitrary finite
family of forbidden connected portal-support patterns.  Nonrealization is
closed under internal contraction.  Tutte contraction plus exact relative
boundary calculus therefore gives either a safe contraction preserving all
portal obstructions, or an exact tight adhesion of the ambient connectivity
order.  In an `r`-minor-critical graph every safe contraction creates a new
exact boundary-colouring state.  This is the reusable recursion promised by
the `C6` laboratory:

    portal obstruction
      -> new critical boundary state
         or exact minimum adhesion.

Arbitrary successive contractions cannot be pigeonholed: after the first
step the whole graph is already colourable.  Only equal states on two nested
shells retained simultaneously in the original graph admit valid pumping.

The pure-Moser six-colour trace census has 42 possible matching states:
12 three-colour `T` traces and 30 genuine high-root/nonstar residues.  The
opposite-shore web theorem forces a crossed frame whenever one shore stays
all-crossless, but conservative contraction of that crossing has Hadwiger
number exactly six in all ten side/frame cases.  Thus the remaining local
conversion must retain portal placement; linkage count alone is provably
insufficient even under the full relative cut inequalities.

`hadwiger_contraction_state_saturation.md` adds a quantitative exchange
invariant.  If an internal edge `xy` is contracted and a minor colouring
creates the new boundary state, then at either endpoint `u`

    d_D(u) + number of distinct colours on its boundary neighbours >= r.

Equality makes the other internal neighbours rainbow and palette-disjoint
from the boundary neighbours.  For the Moser curvature profiles this forces
at least three boundary colours at every facial transition, and makes the
interior `a=w` case an exact four-rainbow Kempe configuration.  This is a
general, all-`t` bridge between the portal splitter and colouring exchange;
the crossed-shore conversion is still open.

`hadwiger_minimum_adhesion_core_crossing.md` closes the routing half at a
minimum full-shore adhesion whenever an induced obstruction core leaves an
omitted boundary graph of chromatic number at most `r-4`.  Exact-block criticality makes the
boundary complement nonsplit, hence it has an induced `2K2`, `C4`, or
`C5`.  If both shores are crossless on such a core, the side-specific web
theorem makes the graph planar after deleting only `k-4` or `k-5` adhesion
vertices, giving at most `r` colours.  Therefore every eligible induced core
is crossed in at least one shore.  When `k<=r`, every induced core is
eligible.  The remaining question is exactly whether
that crossed contact pair is positive in the boundary bad-split relation;
if not, it is a balanced transition rather than another unstructured case.

For the sharp HC7 cuts one has `k=7>r=6`, so a five-vertex core is
automatic and a four-core needs its omitted boundary triple to be
bipartite.  The broader sharp-cut cyclic-hull classification is a
separate current target and must not be inferred from the `k<=r` theorem.

That sharp-cut classification is now proved and independently audited in
`hadwiger_full_split_cyclic_hull.md`.  Every quotient-negative nonsplit
seven-boundary has a relaxed cyclic hull with bipartite omitted set, except
`Q=2K3+K1`; the latter is already excluded by the rooted-triangle closure.
The proof reduces all 783 former atlas types to one `4 x 3` incidence
lemma.  Exact replay of all `2*2^12` matrices gives

    2K2 core: 1214 quotient-positive, 2876 hull, 6 exceptional labelings;
    C4 core:   127 quotient-positive, 3969 hull, 0 exceptions.

The six exceptions are precisely the labelings of `2K3+K1`.  Hence every
order-seven two-full-shore adhesion in a hypothetical HC7 counterexample
has a crossed cyclic hull.  Enlarging the two crossed carriers to a
connected bipartition of the whole shore makes their contacts cover all
seven labels.  Each crossing therefore either gives `K7`, or yields one of
only `2^(7-4)=8` covering bad-split assignments together with the forced
one-step minor-transition state.  Routing existence is completely closed;
the sharp-cut residual is now a uniform covering bad split, not a boundary
atlas.

`hadwiger_interface_pocket_attachment.md` gives the next uniform pressure
step.  In a web on one piece `E` with an artificial interface terminal for
the adjacent piece `F`, a surviving inserted pocket behind an
interface-triangle has at least `k-|Z_E|-2` distinct neighbours in `F`,
where `Z_E` consists only of unrepresented boundary labels that actually
see `E`.  At `k=7, |Z_E|<=3` this is at least two.  Thus the residual bad split carries
an actual `F`-ear; it cannot be maintained by a single irreplaceable
portal.  The remaining peel theorem must either use that ear to preserve
the portal classes of `F`, or expose another exact seven-cut.

### 4.1 Exact-state depth replaces informal separator descent

`hadwiger_minimum_separator_state_depth.md` proves a uniform theorem for
every pair of integers `r,k`.  In a `k`-connected, `r`-minor-critical graph,
every strict nested chain of order-`k` separations has fewer than

    2^N(r,k),   N(r,k)=sum_{q<=min(r,k)} Stirling(k,q),

annuli.  The proof is label-free.  Connectivity and Menger supply clean
`k`-linkages between consecutive minimum adhesions, including fixed trivial
paths at overlapping roots.  These linkages propagate their own labels.
Two repeated inward extension families can then be pumped by deleting the
intervening annulus and contracting the linkage, producing a proper minor
with exactly the same colouring obstruction.

For `HC7`, any exact seven-separator descent therefore has depth below
`2^876`; for the special `K2 join C5` boundary, the fixed clique roots and
dihedral transport of the pentagon preserve its ten labelled states and
sharpen this to `1024`.  Thus the exact order-seven separators exposed by
the Moser rank-leaf theorem cannot generate an unbounded ladder.  The
remaining alternatives are a bounded-depth torso or a crossing-separator
family which must still be uncrossed into a rooted model or a colour-gluable
decomposition.

`hadwiger_exact_state_branching.md` supplies the parallel companion.  If
pairwise anticomplete nonempty child regions all attach through one fixed
support `X` in an `r`-minor-critical graph, deleting each child produces a
distinct private equality state on `X`.  Hence the number of children is at
most `N(r,|X|)`, and at most ten for a fixed labelled `K2 join C5` support.
This is sharper than counting extension families.  It also identifies the
exact uncontrolled alternative: many incomparable adhesions whose union
uses more than `k` torso vertices.  A binary clique-tree counterexample
shows that connectivity and repeated unlabelled leaf types alone cannot
control that distributed-support branching.

## 5. Structural pivot: defect profiles, linkage ownership, and knitted adhesions

The six-edge analysis has now produced machinery which is not tied to a
list of labelled cases.

* The defect-atlas connectivity and defect--Helly theorems convert the
  bad quotient relation into internal shore connectivity and sharp bounds
  on the branching behind an internal separator.
* Nested connected shore splits have monotone defect coordinates and
  stabilize after at most \(2|S|\) strict changes. Exact colour states,
  rather than contact rows alone, glue along a laminar decomposition;
  a cyclic decomposition additionally requires trivial colour holonomy.
* For the \(C_6\dot\cup K_1\) laboratory, compatible opposite frame
  crossings give an explicit \(K_7\), so each opposite frame pair has a
  unique shore owner and one shore owns at least four frames. Neither
  shore contains any antipodal two-linkage or any nonidentity
  prism-matching three-linkage. The exact residual is therefore one
  shore carrying intersecting pairwise-but-not-triple rope linkages.
* No inference is made from symbolic portal labels to a common order of
  actual portal representatives. The former oriented-precedence claim
  was rejected under adversarial audit because different frame locks may
  use different representatives. The sound replacement is the explicit
  linkage-ownership theorem in
  hadwiger_c6_opposite_crossing_dichotomy.md.

The general-\(t\) side has also advanced. Theorem 3.1 of
hadwiger_small_nonclique_knitted_adhesion.md proves the following
contact-or-separator statement. Let a counterexample-derived adhesion
be complete multipartite, let \(T\) be the union of its nonsingleton
parts, and let \(R\) be the singleton clique. If

\[
 8|T|+|R|<t+1,
\]

then either one open side has a relative separator of order below
\(|T|\), or the Kawarabayashi--Yu knittedness theorem realizes the same
exact multipartite boundary partition on both sides and the two proper-
minor colourings glue. This eliminates an infinite adhesion family for
every \(t\), and identifies the remaining quantitative obstruction:
large nonclique cores must be reduced by rooted absorption or decomposed
by their forced relative separators.

### 5.1 Audited refinements after the structural pivot

The following subsequent gains supersede the cruder portal-multiplicity
discussion above.

* The portal-transversal theorem in
  hadwiger_portal_transversal_or_small_shore.md is label-free. For a
  minimum cut \(S\) and a component \(D\) of \(G-S\), either the portal
  family \((N_D(s):s\in S)\) has an SDR, or
  \(D=\bigcup_{s\in I}N_D(s)\) and \(|D|<|I|\) for a Hall-deficient
  \(I\subseteq S\). Thus a deficient component forces
  \(|S|\ge\lceil(t+2)/2\rceil\), while every component behind a smaller
  minimum cut has distinct portals for all of \(S\).
* Every independent \(I\subseteq S\) is an exact colour trace obtained
  by contracting a full opposite shore together with \(I\). Moreover,
  deletion of every internal shore vertex or edge creates a boundary
  state extending the modified shore and the opposite side but not the
  original shore. This is the precise minor-switching axiom absent from
  connectivity-only web examples.
* Exposure-weighted knitting and full-component block witnesses give
  the certified bound \(m\le2q-1\) when \(G-S\) has \(m\) components and
  a complete-quotient independent partition of \(S\) has \(q\)
  nonsingleton blocks. The strict separator descent decreases cut order,
  but its cut sets need not be nested or laminar.
* In the \(C_6\dot\cup K_1\) core, Hall plus exact finite certificates
  eliminates every high-owner shore of order four or five. A shore of
  order at least six has a six-portal SDR. The label-free circular
  obstruction theorem then shows that a three-connected common-face
  shore can own only one complementary frame pair, whereas ownership
  forces one shore to own at least two. Hence the high-owner shore is
  necessarily two-connected but not three-connected.
* The remaining \(C_6\) obstruction is therefore a genuine SPQR/Yu
  ladder of two-separations. The circular frame index is invariant under
  every common-face leaf flip; any disagreement localizes at a two-cut
  carrying two to four roots.

One earlier two-cut claim has been retracted. Section 4, Lemma 4.1 of
hadwiger_c6_opposite_crossing_dichotomy.md incorrectly asserted that a
visible support cannot contain opposite frames. Its own exact verifier
has the counterstates 001001, 010010, and 100100. No later argument may
use that assertion. The orientation-free SPQR-rank argument in Section
5.2 bypasses it and closes the cell.

No statement above is to be read as a complete proof until all four
objectives, including the general-`t` augmentation, have been discharged.

### 5.2 Complete closure of the six-edge `C6+K1` cell

The later synthesis `hadwiger_c6_core_closure.md`, independently audited in
`hadwiger_c6_full_closure_audit.md`, now eliminates this entire boundary
cell.  The unbounded mechanism is orientation-free:

1. a four-terminal web and a portal transversal make one side of every
   SPQR leaf separation have transversal rank at most one;
2. seven-connectivity turns that low-rank side into a degree-two singleton;
3. the exact lock and Dirac's neighbourhood inequality force the two cut
   vertices to be adjacent, canonically exposing a singleton S-ear; and
4. the exact one-ear frontier is either closed by a seven-fan model or, in
   its double-thin state, by a cofacial Two Paths web whose quotient contains
   a subdivision of `K3,3`.

This replaces and retracts the earlier false claim that all actual SPQR
leaves are singleton or that the SPQR tree must be a path.  The safe theorem
is the orientation-free singleton-to-S-ear implication.  Thus the six-edge
boundary induction is complete; the active degree-seven gap has moved to the
pure-Moser one-component/order-six reserved-connector shore and denser
missing-edge layers.

### 5.3 Structural convergence after the cyclic-hull round

The later files listed below replace several unbounded local searches by
reusable structural alternatives.

1. hadwiger_full_split_cyclic_hull.md proves that every sharp
   order-seven two-full-shore adhesion has a crossed cyclic hull, apart
   from the already closed \(2K_3\dot\cup K_1\) boundary. Extending a
   crossing to the whole shore reduces the routing problem to a covering
   bad split on seven labels.
2. hadwiger_bad_split_interface_exchange.md decorates every
   edge-deletion state at such a split by either a bichromatic interface
   ear or two boundary-anchored components for each other color.
3. hadwiger_unique_interface_anchor_tight_cut.md proves that a
   one-edge interface gives either a nested exact seven-cut or five
   internally disjoint one-label ears together with a boundary-pinned or
   exact five-block transition state.
4. hadwiger_root_multiplicity_split.md converts low boundary degree into
   duplicated portal classes. Two repeated classes in one shore give a
   connected covering split retaining both labels on both sides, or a
   cutvertex. In the \(K_1\vee C_6\) laboratory the cutvertex outcome is
   already a \(K_7\) model or a nested exact seven-cut. The complementary
   high-boundary case consists of exactly eight transparent path/cycle
   unions.
5. hadwiger_removable_fan_state_split.md completely closes every
   removable outer fan in the reserved all-crossless Moser web cell:
   \(K_7\), a six-coloring, or an exact seven-cut. The exact verifier
   covers all fifteen adjacent ordinary-profile pairs and all 5,000
   three-profile cells; Dirac's neighborhood bound repairs every sparse
   two-profile exception.

The surviving sharp object is therefore no longer an arbitrary web,
fan word, or crossing pattern. It is a negative covering split with
strictly surplus, portal-separated interface geometry, or recursion
through an exact seven-cut.

### 5.4 Uniform all-\(t\) contact augmentation

hadwiger_contact_augmentation_hall_menger.md gives a uniform
model-meeting trichotomy. For a \(K_m\)-model and a root set \(N\) with
\(|N|\ge m\), either:

1. the model can be augmented by disjoint model-avoiding paths to become
   \(N\)-meeting;
2. one branch bag contains two roots and admits a connected two-root
   split; or
3. a nonempty subfamily \(I\) of uncontacted bags has all of its external
   portals separated from the unused roots, relative to paths avoiding
   the model, by a set \(X\) with \(|X|<|I|\).

The artificial-terminal proof was adversarially corrected: \(X\) is not
claimed to be a global separator or even a separator in the artificial
terminal graph. Its exact valid conclusion is separation of the external
portal sets in the graph obtained after deleting all current model bags.

For a hypothetical least-\(t\) counterexample, \(m=t-1\) and
\(|N(v)|\ge t\), so an immediate augmentation gives \(K_t\). The uniform
remaining gap is precise: promote the relative Hall deficit, using the
clique-model geometry and contraction-critical coloring transitions, to a
genuine color-gluable adhesion, a portal-rich bag split, or a \(K_t\)
model.
