# Uniform rooted-model principle: current state ledger

## Executive verdict

There is no complete uniform rooted-model theorem yet.  The search has,
however, now proved its first nontrivial infinite rooted-model cell and has
isolated a substantially narrower live mechanism.

Static hypotheses are exhausted.  Colour saturation, every independent
trace, two colourful portal sets from one contraction, Kempe carriers, a
pre-existing clique model, and even a nested colourful elimination flag do
not force the required rooted model.  Explicit counterexamples exist for
each proposed packaging step.

The first hypothesis not absorbed by those counterexamples is **dynamic
boundary-state novelty under every proper-minor operation**.  Across a
separation, one edge-deletion transition either changes the exact boundary
partition, or its apex colour is pinned to the adhesion, or it forces every
free boundary colour to have neighbourhood capacity on the edge's shore.
Two opposite unpinned transitions in one state require double capacity and
are incompatible with a private trace colour.  A minimum pinned transition
carries a canonical missing-colour Kempe fan.

Thus the live target is no longer “colourful set implies rooted clique.”  It
is a transition theorem which converts **partition change or pinning** into
a label-preserving model move or a colour-gluable adhesion.  In the exact
coexistence cell where one branch bag is a full minimal tree obstruction and
all other bags are singleton, this programme now succeeds completely: the
dynamic transitions collapse the tree to an alternating two-colour owner
path, and that path has an explicit target clique model.  The remaining
uniform problem is to force this coexistence by exchanging away hanging
parts and nontrivial foreign bags, or to turn their first hits into a smaller
Hall circuit.

The sections below distinguish proved statements from conjectural targets.

## 1. Standard counterexample setup

For the uniform discussion, write the parameter as follows.  Let (G) be
minor-minimal subject to not being (r)-colourable, so

\[
                         \chi(G)=r+1,
\]

and every proper minor is (r)-colourable.  Fix (v\in V(G)), put

\[
                         H=G-v,\qquad N=N_G(v),
\]

and fix an (r)-colouring of (H).  Every colour occurs on (N).  Under
induction at the least failing Hadwiger parameter, (H) also contains an
unrooted (K_r)-model.  The required last step is to alter such a model so
that every bag meets (N), after which ({v}) is the final branch bag.

This last sentence states the application, not a theorem assumed below.

## 2. Verified uniform progress

### 2.1 Exact contraction traces

For every nonempty independent set (S\subseteq N), contracting the star
(G[\{v\}\cup S]) and colouring the proper minor produces an
(r)-colouring of (H) in which one colour has trace exactly (S) on
(N).  All (r) colours occur on (N).  When

\[
                         |N-S|=r-1,
\]

the (r-1) vertices outside (S) have pairwise distinct colours, private
on (N).

More generally, contracting an induced connected bipartite graph
(T=U\dot\cup W) and deleting the contraction colour from a selected
palette makes the external portal sets of **both** parities colourful in
the induced palette slice.  This is valid for every palette size.

### 2.2 Exact model-versus-capacity dichotomy

For a fixed (K_r)-model and a portal set (X), a target-slot strict
gammoid and Rado's theorem give an exact alternative:

* disjoint model-avoiding paths can be absorbed so that every bag meets
  (X); or
* a named subfamily of bags has linkage rank strictly below its size.

Applying this successively to two portal sets gives the corresponding
biportal theorem.  The failure certificate is a genuine
**model-relative capacity cut**.  It is not automatically an ambient graph
separator, because forbidden paths may instead use old bags, the contracted
bipartite set, or omitted colour classes.

### 2.3 Palette/model-haven dichotomy

For every (X\subseteq V(H)), one component of (H-X) contains neighbours
of (v) in every colour absent from (c(X)).  Comparing this palette
component with the component containing the untouched bags of a fixed
clique model yields three proved outcomes:

1. a palette-polarized adhesion;
2. an (N)-meeting clique model; or
3. a model-clean double foot: two disjoint neighbourhood prefixes first hit
   the same branch bag.

A minimum polarized adhesion is a rainbow gate: every adhesion vertex is
simultaneously essential to the model side and to each missing-colour side.

### 2.4 Nested-cut transport

Across nested minimum (k)-cuts, (k) disjoint adhesion-to-adhesion paths
transport all root labels, an already-built outer clique model, and every
disjoint capacity packet into the inner cut.  The old bags must lie wholly
on the processed side; that condition is necessary.

Choosing a minimum nested fragment then gives strict relative surplus:
every nonempty proper subset of a nonsingleton fragment has external
neighbourhood at least (k+1).  Consequently a local theorem with outcomes
“target model / forbidden capacity / smaller exact cut” would terminate;
the exact-cut outcome cannot recurse forever.

### 2.5 Edge-transition novelty

For every edge (e=xy\in E(H)), an (r)-colouring of (G-e) has
(x,y) in one colour and has the colour of (v) absent from (N).  The
equality partition it induces on (N) is a genuinely new boundary state:

\[
 \Pi_N(G-e)\notin\mathcal P_r(H,N),\qquad
                         |\Pi_N(G-e)|\le r-1.          \tag{2.1}
\]

Otherwise a colouring of (H) with the same equality partition could be
palette-aligned and extended to (v).

This edge-by-edge novelty is stronger than global saturation or the family
of independent traces.  It is the smallest verified dynamic axiom that
excludes the principal static counterexamples.

### 2.6 Transition splicing across an adhesion

Let ((A,B)) be a separation of (H), with adhesion (X), and let
(e\) lie only on the (A)-side.  Compare an honest colouring (c) of
(H) with a colouring (d) of (G-e) which induces the same equality
partition on (X).

* If (d(v)\notin d(X)) (the transition is **unpinned**), every colour
  absent from (c(X)) occurs on (N\cap(A-X)).
* If (d(v)\in d(X)), its boundary block fixes a colour which must occur
  on (N\cap A).

Therefore opposite unpinned transitions preserving the same boundary state
force every free colour to occur in both open shores:

\[
                         |N-X|\ge2(r-|c(X)|).          \tag{2.2}
\]

An exact trace with a private free colour rules this out.

If a transition is pinned, choose a colouring minimizing the pinned block.
For every colour missing on (X), each pinned vertex lies in the
corresponding two-colour component with (v).  Removing the last edge at
(v) produces a canonical fan from the adhesion to differently coloured
vertices of (N).

This proves the current **transition gate**:

\[
\boxed{
\begin{array}{c}
\text{an essential transit adhesion changes the exact state,}\
\text{or it carries a minimum pinned missing-colour fan,}\
\text{or double capacity/contact is forced.}
\end{array}}
\tag{2.3}
\]

### 2.7 Fixed-model consequence

For a contact-maximal (K_r)-model with (s) contact bags, if a pinned gate
(X\) uses fewer than (r-s) colours, the missing-colour fan has more
distinct neighbourhood endpoints than the model currently contains.  A
first-hit truncation is model-clean and gives either a new contact or a
certified double-foot bag.

Combining this with transition splicing proves: a small off-haven transit
gate cannot preserve the exact trace state unless it causes a
label-preserving contact augmentation or a double foot.  This excludes an
infinite family of static transit-comb obstructions.

### 2.8 Join-prime normalization and product barriers

A least-parameter Hadwiger counterexample is a nontrivial-join-prime graph.
If (G=A\vee B), induction gives clique models of orders
(chi(A),\chi(B)), and the join combines them into a
(K_{\chi(G)})-model.

Universal-clique suspension is nevertheless an exact adversarial test.  For
every graph (F),

\[
 \chi(K_\ell\vee F)=\ell+\chi(F),\qquad
 \eta(K_\ell\vee F)=\ell+\eta(F).                   \tag{2.4}
\]

If (F) is proper-minor-minimal at its chromatic number, then so is
(K_\ell\vee F).  Thus a hypothetical counterexample has suspensions with
connectivity and minimum-degree ratios tending to one, while its Hadwiger
defect stays constant.  Any useful theorem must act on the least-parameter
join-prime core rather than on raw connectivity or degree.

Standard product amplification also fails.  Join powers manufacture large
complete multipartite minors and drive (chi/\eta) below two.
Lexicographic clique blow-ups satisfy

\[
 \chi(F[K_m])=\chi_m(F),
\]

so their normalized colour growth is fractional chromatic number.  Their
clique minors are exactly depth-(m) families of pairwise-touching connected
sets with vertex congestion at most (m).  Congestion-two rounding has an
unbounded gap even in planar wiring graphs.  Static fractional-to-integral
minor rounding is therefore unavailable.

### 2.9 Whole-tree contractions have a matched obstruction core

Contract an induced transit tree \(T\) to one vertex of colour
\(\alpha\), and give each \(x\in T\) the colours absent from its external
neighbourhood as its expansion list.  Every list contains \(\alpha\), but
the tree is not list-colourable.  A proved minimal-obstruction theorem gives
an inclusion-minimal uncolourable subtree \(R\) and a proper edge-colouring
\(\lambda\) such that

\[
                 L(x)=\{\lambda(e):e\ni x\}
                 \qquad(x\in V(R)).                  \tag{2.5}
\]

For every edge, the two components force their endpoints to its edge colour.
The \(\alpha\)-labelled edges form a perfect matching of \(R\).  Thus one
whole contraction aligns many local equality gates in a single outside
colouring; they are not unrelated Kempe witnesses.  The remaining issue is
to align these forced colours with the fixed branch-bag labels and to handle
parts of \(T\) hanging outside \(R\).

There is a decisive compatibility restriction.  Contracting the other
nontrivial model bags produces a canonically coloured clique, but expansion
of \(T\) then colours only that partially contracted proper minor, not
\(G\); unexpandability is no longer forced.  Canonical bag labels and the
forced core coexist automatically only when the other bags are singleton
(or a separate expansion theorem is supplied).  In that valid case the
quotient colour of \(v\) selects one noncontact bag, but the core labels are
**anti-portals**: an edge carrying bag \(i\)'s colour has both ends outside
the \(i\)-portal class.  For an arbitrary induced transit society, a
minimal unexpandable core satisfies
\(|L(x)|\le d_R(x)\); it either has strict internal surplus or is a Gallai
tree with a contraction-colour block cover.  A uniform explicit family
shows that this static information need not yield a label-preserving split.
Every mismatch is instead witnessed by a same-coloured external shadow
blocker, making shadow exchange the dynamic object that remains.

### 2.10 Crossed minor operations and Hall-circuit rainbow states

Crossed colour splicing is valid for arbitrary opposite minor operations,
not just edge deletions.  The exact condition is **closed-shore
faithfulness**: the operation on one side must preserve injectively every
vertex and edge of the other closed shore.  This permits strict open-shore
operations and contractions rooted at one adhesion vertex, while forbidding
the merger of two adhesion labels.

For a minimum Hall-deficit circuit (I), with
(|X|=|I|-1), the root prefixes can be contracted to force the star
(vX), and the far-side circuit model can be contracted to force a clique
on (X).  Contracting both systems simultaneously forces

\[
                         \{v\}\cup X
\]

to be rainbow.  At least one one-shore expansion of this state is locked.
The obstruction is therefore not failure to produce a rainbow core; it is
failure to synchronize its equality pattern on the genuine extra portal
set (P).

### 2.11 Hall-circuit anti-diamond and collision carriers

If the host is (k)-connected and the Hall circuit has order (h), its
promoted portal set satisfies

\[
 |P|\ge k-h,qquad
 \sum_{j\notin I}\max(0,|P_j|-1)\ge k-r.             \tag{2.6}
\]

Every (r)-colour boundary state which is rainbow on
(\{v\}\cup X) has at least (k-r) corresponding colour collisions on
(P): repeated portal colours or portal colours repeated on the rainbow
core.  Each collision has an actual connected carrier in at most two
accessible model bags, in one accessible bag plus the named rooted circuit
bag, or through the root region to (v).  For a co-rank-one circuit all
portals lie in one multiply hit accessible bag, so label and colour
collision are already aligned.  What remains is to clean the carrier, or
use its first extra portal to exchange to a smaller circuit.

For an arbitrary promoted circuit, the root-shore gammoid on (X\cup P)
has rank at least

\[
                         \min\{k-1,|R|\}.               \tag{2.6a}
\]

Thus (X) extends to a basis containing individually named portals, and a
minimum-length basis linkage meets (P) first at its prescribed endpoints.
In the co-rank-one cell with (k\ge r+1), this supplies two clean mutually
disjoint portal carriers, simultaneously disjoint from the full
(X)-linkage.  The inevitable colour collision can be chosen among these
basis portals.  A connected split of their accessible bag which loses at
most one deficient label gives an explicit rooted (K_r)-model.  A safe
first-hit peel increases contact and either finishes or produces a strictly
smaller Hall circuit.  For a tree accessible bag, every surviving
root-free lobe owns at least two entire deficient labels; in (HC_7) the
residue is a two-ended owner corridor with at most one mobile label.

### 2.12 Dynamic full-tree collapse

Under the full minimal-core hypothesis, the matched tree has one canonical
aligned colouring for every internal edge deletion.  Crossed splicing of
the operations in two lobes proves the following uniform normal form:

\[
\boxed{
\begin{array}{c}
\text{clean label-preserving rotation, or named foreign-bag transit,}\
\text{or the whole core is a path labelled }
\alpha,\delta,\alpha,\delta,\ldots,\alpha,
\end{array}}
                                                            \tag{2.7}
\]

where (delta) is the apex colour.  In particular every branching core
and every non-apex internal colour is eliminated simultaneously; this is
not a bounded case enumeration.  The alternating residue is end-locked:
only its two ends can be apex feet, and every internal vertex has full
external saturation in all colours outside ({\alpha,\delta\}).

There is now also a weaker but much more general collapse which removes the
full-core hypothesis from the geometry.  For an arbitrary spanning tree of
the whole branch bag, choose one colouring of (G-e) for every tree edge
and mark the edge by one bit according as its monochromatic defect colour
does or does not equal the apex colour.  Two incident lobes with the same
bit have the same marked state on the singleton adhesion at their common
vertex.  Crossed splicing or an ambient bypass therefore gives

\[
\boxed{
\text{clean rotation, or named foreign transit, or a path whose bits
alternate.}}                                             \tag{2.7a}
\]

This binary transition-tree theorem includes all portal-bearing hanging
parts outside a minimal list core.  It does not supply the named lists of
the stronger theorem; recovering capacity on the surviving binary path is
the new colour-theoretic core-exchange residue.

### 2.13 First complete infinite rooted-model cell

Assume (G-v) is the disjoint vertex union of one induced complex branch
bag (B) and an ((r-1))-clique of singleton branch bags, and assume that
(B) is the full minimal equality-tree obstruction for its contraction
colouring.  Then (G) contains a (K_{r+1})-minor.

The proof is uniform and now covers every tree, not only the alternating
normal form.  Delete the perfect matching of contraction-colour edges and
contract its complementary components.  The quotient is a tree satisfying

\[
                    d_R(C)=|C|.                           \tag{2.8}
\]

Root it at the unique component containing the selected noncontact portal.
A branching quotient vertex supplies two independently footed,
portal-complete shores and gives three explicit new branch sets.  If there
is no branching, the size--degree identity forces the original bag to be a
path with alternating contraction edges.  Colour switching closes the sole
constant-label exception.

In particular, dynamic collapse reduces the most visibly locked tree to

\[
 B=x_0x_1\cdots x_{2m-1},qquad
 \lambda=\alpha,\delta,\alpha,\ldots,\alpha.
\]

Every path vertex is then a portal to every ordinary singleton bag; the
internal vertices are neither feet nor portals to the apex-selected bag
(b_j); both ends are feet; and the nonempty (b_j)-portal class occurs
at exactly one end, say (x_0).  The explicit branch sets

\[
 \{v,x_{2m-1}\},\quad \{x_0,b_j\},\quad
 \{x_1,\ldots,x_{2m-2}\},\quad
 \{b_i\}\ (i\ne j)
                                                            \tag{2.9}
\]

form a (K_{r+1})-model.  The two-vertex case closes separately by the
same portal argument.  This is the first verified rooted-model theorem in
the programme that eliminates an unbounded family for every (r); the
tree's size, degree, branching, and internal label sequence are all
unrestricted.

The equality-Gallai extension is also closed after dynamic block
normalization.  If every alpha-block is a (K_2), the matching quotient
proof applies verbatim.  Otherwise, the rigid block structure is an
alpha-block tree joined by delta bridges.  A leaf alpha-block whose exterior
contains both a foot and the selected portal supplies the target using its
internal (K_{|C|+1})-capacity.  Failure forces an alpha-block path with
the two owner sets at opposite ends.  Changing the quotient colour then
forces every endpoint-palette singleton to contact (v), and one such
contact closes the path.  Hence every rigid full equality-Gallai core in
the spanning one-complex/singleton cell contains (K_{r+1}).

With unused shadows and an (r)-connected (H), an end-locked path gives
either (K_{r+1}) or a clean rotation.  A one-attachment shadow component
must meet every singleton label whose colour it supplies, since otherwise
its neighbourhood is an adhesion of order at most (r-1).  Assigning each
such component to its unique tree attachment restores all required portal
adjacencies simultaneously.  A multi-attachment component is exactly the
clean-rotation alternative.  Thus external shadows reduce to the global
rotation/core-exchange problem rather than a disjoint-allocation problem.

### 2.14 Proper cores give an exchange ear or the target minor

There is now a uniform structural theorem for the hanging-society part of
the spanning one-complex-bag cell.  Let \(H\) be \(r\)-connected, let
\((B,\{b_1\},\ldots,\{b_{r-1}\})\) be the spanning model with singleton
clique \(S\), and let \(R\subsetneq B\) be a connected minimal core.  For
every component \(D\) of \(B-R\),

\[
        |N_R(D)|+|N_S(D)|\ge r.                         \tag{2.10}
\]

Consequently one of the following occurs:

1. \(D\) has two core attachments and supplies a clean \(R\)-ear;
2. two one-attachment components split \(B\) into two connected sets
   meeting every singleton bag, giving \(K_{r+1}\); or
3. there is exactly one hanging component, with unique attachment
   \(q\in R\), and
   \[
                         N_H(D)=S\cup\{q\}.              \tag{2.11}
   \]

In outcome 3 the far shore meets every singleton label.  If \(R\) missed
some \(b_i\), then

\[
                    (S-\{b_i\})\cup\{q\}
\]

would be a cut of order \(r-1\), separating
\(D\cup\{b_i\}\) from the nonempty set \(R-\{q\}\).  Hence
\(r\)-connectivity forces \(R\) to meet every singleton bag, and
\(D,R,S\) are the target model.  A genuine uncolourable core cannot be
the singleton \(\{q\}\), because every expansion list contains the
contraction colour.  Therefore every proper minimal core yields either a
clean exchange ear or \(K_{r+1}\).

This removes the proposed finite-state owner-adhesion residue entirely.
The sole remaining proper-core operation is to prove that a clean ear can
be absorbed while preserving (or improving) the selected minimal
uncolourable core.

### 2.15 Connected portal synchronization and Hall block packing

Two arbitrary portal classes of order at least two always synchronize in
a 2-connected complex bag: choose two vertices of the first class as the
poles of an st-numbering and cut between the first and last occurrence of
the second class.  Both shores are connected and meet both classes.
Consequently a target-free one-complex/singleton cell has at least three
nonuniversal portal labels.  The octahedron and a pentagonal-bipyramid
diamond show that three classes, and even one unexpandable contraction
state, are statically insufficient; both examples fail the all-edge
transition axiom of a genuine minor-critical graph.

At a co-rank-one Hall circuit, deficient clique bags may be merged into
label blocks rather than being retained one per far carrier.  If (s)
pairwise adjacent rooted accessible pieces and (r-s) rooted far carriers
admit a partition of the deficient labels into (r-s) groups, each group
having a supporting label at every accessible piece, merging each group
into its representative far carrier gives the target (K_{r+1})-model.

For (HC_7), a two-piece split therefore closes when four labels cross it,
or when three cross and the two exclusive labels lie on opposite shores.
Every target-free bipolar sweep of the accessible bag has at most three
active label intervals, and every mixed past/future cut has at most two.
This is a genuine unbounded **two-active-label web**, not a finite graph
enumeration.

There is also a three-piece closure.  At the old foot and two clean portal
roots, every rooted (K_3)-model whose three pieces each meet at least three
of the five deficient bags yields (K_7).  The two exceptional support-mask
patterns are closed by absorbing the two omitted clique bags as helpers.
Thus every surviving rooted triangle has a branch piece seeing at most two
deficient labels.

### 2.16 A third portal or an exact two-gate web

In the co-rank-one ((r+1))-connected cell, matroid basis exchange gives a
sharp trichotomy.  Either one Hall-interface endpoint exchanges for a third
clean portal, or the rank-two portal flat yields an exact ambient adhesion

\[
                         X\mathbin{\dot\cup}Y\mathbin{\dot\cup}\{v\},
                 \qquad |Y|=2,
\]

of order (r+1), or the source set is tight: (d(v)=r+1),
(R=X\mathbin{\dot\cup}Y), and the two roots (Y) separate all (X)-roots
from the portal shore.  In the tight case every component beyond (Y)
reaches the portal set and (N_U(X)\subseteq Y).  Thus failure of a third
portal is no longer an amorphous linkage defect; it is an exact two-gate
adhesion, with one minimum-degree two-gate web as the sole exception.

### 2.17 Exact source-tight amplification and omitted-bag absorption

The minimum-degree two-gate exception now has a uniform internal
amplification.  Every component beyond the two gates has at least
(r-1) distinct neighbours in the accessible portal set.  When
(|P|=r-1), every such component has the same exact boundary

\[
                              Y\mathbin{\dot\cup}P.
\]

Two exact components can therefore act as independent connected hubs for
arbitrary portal regions of the accessible bag.  If a private portal
region owns at most one deficient label but sees at least one, omit that
label from the far Hall certificate and absorb its entire old clique bag
into one hub branch.  The other hub retains every far adjacency.  This
gives an explicit (K_{r+1})-model, with no gate--interface completeness
assumption.

It follows that a target-free exact cell has at least
(\lceil(r-1)/2\rceil) pairwise disjoint **label-dead** private portal
regions.  Now choose a contact-maximal model, minimize the Hall-circuit
order, and subject to that maximize the accessible bag.  A singleton dead
region can be replaced by one exact web component and a gate root, strictly
enlarging the accessible bag.  A nontrivial dead region has a root-free,
model-free first-hit escape.  A return to the accessible bag is again a
strict enlargement.  If the escape ends in a deficient clique bag, absorb
all path vertices except the last endpoint: the final edge preserves that
named bag adjacency, contact and disjointness are unchanged, and the
accessible bag strictly enlarges.

Consequently the whole exact multicomponent source-tight cell

\[
                 |P|=r-1,\qquad c(U-Y)\ge2
\]

has no terminal representative inside a comparison class preserving the
contact and circuit coordinates.  The absorption move is valid, but this
does **not** prove the target minor: a globally contact-maximal model cannot
carry a nontrivial Hall circuit, since each linkable singleton would
augment contact.  The earlier claimed global closure is therefore
withdrawn.  The move may exit to a higher-contact or smaller-circuit cell,
whose terminal form is the contact-maximal multiply-rooted bag split lock.

## 3. Decisive counterexamples and what each rules out

These examples are proved or exhaustively certified in the accompanying
notes.  They are tests which every new theorem must pass.

### 3.1 Universal colourful-pair realization

An arbitrary (q)-colourable graph with arbitrary (q)-colourful sets
(X,Y) occurs as the two parity portal sets in the (q)-colour slice of one
induced-edge contraction.  Hence “two colourful sets from the same
contraction” contains no hidden rooted geometry.

Moreover, if (F) is an arbitrary (q)-minor-critical graph, the join lift
(F\vee K_3) is proper-minor-minimal at the higher chromatic number and has
slice (F), with both portal sets equal to (V(F)).  Thus ambient
minor-criticality plus a single contraction trace still contains ordinary
Hadwiger at the lower parameter.  The least-parameter join-prime
normalization is essential to exclude this universal lift.

### 3.2 Icosahedral all-trace obstruction

There is a five-colourable graph (H), a five-vertex boundary (N), and an
unrooted (K_5)-model such that:

* every proper equality partition of (H[N]) extends to (H);
* in particular, every independent subset of (N) occurs as an exact colour
  trace; but
* no (N)-rooted (K_5)-model exists.

It fails global apex saturation and, maximally, fails edge-transition novelty:
deleting an internal edge creates no new boundary state.  This is why the
dynamic axiom (2.1), rather than another static trace, is the live datum.

### 3.3 Colourful elimination-flag obstruction

An explicit four-chromatic graph has a complete nested private-colour flag
whose selected roots do not root a (K_4)-model.  Two demanded root-pair
connectors are forced through one bottleneck.  Joining with cliques lifts the
bad selected flag to every order.  Thus nested private-colour descent,
pairwise Kempe information, and every independent trace still do not supply
simultaneous root-matching linkage.

### 3.4 Model-cleaning obstructions

End-locked transit combs show that even a full transversal from all coloured
roots into all bags does not clean to distinct first-hit labels.  A
five-connected icosahedral example has fixed-colouring palette/model-haven
agreement and a full transversal but no prescribed rooted (K_5).  These
examples defeat one-colouring haven arguments; they do not satisfy the full
operation-transition family.

### 3.5 Bounded-congestion wiring obstruction

For every (m), a planarized wiring diagram has (m) pairwise-intersecting
paths with vertex congestion two.  Hence its (K_2)-clique blow-up has a
(K_m)-minor although the base graph has no (K_5)-minor.  No static
bramble, fractional minor, or pairwise-touching system admits the required
uniform integral rounding.

### 3.6 Boundary transition diamonds

A uniform Hajós-type two-shore construction realizes three boundary
states: the left shore forces a portal to equal one rainbow anchor, the
right forces it to equal another, and operating both shores creates a fresh
third colour.  It satisfies abstract transition novelty and crossed-state
disjointness but never synchronizes the original shores.  It has no
separating clique.  A separate construction raises connectivity to
(r+1), retains an unrooted (K_r), and still realizes incompatible
states.  That lift is visibly not minor-critical.  Hence neither finite
state algebra, join-primality, connectivity, nor an unrooted model alone is
the missing principle; actual Hall portal geometry together with
all-minor criticality is indispensable.  The collision bounds in Section
2.11 are exactly what excludes the one-shadow diamond in a genuine Hall
circuit.

## 4. Why all static rooted principles now fail

The counterexamples establish a quantifier barrier.

* One colourful set is the premise of Strong Hadwiger.
* Two colourful sets from one contraction are completely universal.
* Every independent trace records only the one-block projections of the
  boundary extension relation.
* A full elimination flag can select mutually incompatible roots.
* One fixed colouring plus a fixed model can agree at every small cut while
  still having a locked transit bag.
* Static bounded-congestion linkages can realize arbitrary planar wirings.

Consequently a theorem of the form

\[
 \text{“saturated boundary + unrooted model”}
 \Longrightarrow\text{“rooted model”}
\]

is either false under its stated data or is an unproved Strong-Hadwiger type
statement.  Adding more one-colouring Kempe paths does not repair it.

The proper-minor operation family changes the quantifiers: **every internal
edge must create a new nonextendable boundary state**, and opposite shores
must satisfy those state changes consistently.  No current static
counterexample has that property.

## 5. The dynamic carrier-exchange candidate

The emerging candidate has two layers.

### Layer A: ambient lifting of a model-relative defect

Start with a minimum Rado/target-slot capacity defect for a contact-maximal
clique model.  Prove that either

1. omitted colour classes or the opposite parity portals augment the model;
   or
2. the auxiliary cut lifts to an ambient adhesion (X) whose model shore,
   palette shore, and essential transit edges are all identified, with the
   palette inequality needed by the fixed-model transition theorem.

This layer must explicitly account for paths through old bags, the
contracted bipartite set, and omitted colour classes.  Silently treating the
target-slot separator as an ambient separator is invalid.

### Layer B: closure of a dynamic gate

At the lifted adhesion, apply edge-deletion colourings to essential transit
edges on both shores.

* A repeated unpinned boundary state contradicts private-colour capacity.
* A minimum pinned state gives the canonical missing-colour fan; the required
  new step is to split or rotate the transit bag while retaining all labelled
  interbag adjacencies.
* If every transition changes the boundary equality partition, the required
  new step is to show that the finite sequence of operation states either
  returns to a compatible state or yields two side colourings whose equality
  blocks have connected realizations and can be glued.

This is strictly more structured than a generic rooted-minor conjecture.  It
mentions a minimum capacity cut, a fixed labelled clique model, exact
edge-deletion states, and the all-operations novelty axiom.

The new full-tree theorem proves Layer B whenever the selected contracted
bag is exactly its minimal tree core and the other bags are singleton.  In
general, the remaining failures now have only two forms:

1. a portal-bearing lobe hangs outside the minimal core, so the canonical
   edge colourings do not extend through it; or
2. a collision carrier reaches a nontrivial foreign bag or an extra portal
   before it becomes a clean rotation.

Both are exchange problems.  They should be treated by the same descent:
absorb the first hanging/foreign segment and minimize the core/circuit, or
obtain two faithful opposite operations with one boundary state.

## 6. Exact remaining theorem (conjectural)

The following is the cleanest current formulation.  It is **not proved**.

> **Dynamic carrier-exchange closure theorem.**  Let (G) be a
> least-parameter, join-prime, proper-minor-minimal non-(r)-colourable
> graph.  Fix (v), an exact independent star trace on (N(v)), and a
> contact-maximal (K_r)-model in (G-v).  Let a minimum target-slot
> capacity defect protect a noncontact labelled subfamily of bags.  Then one
> of the following occurs:
>
> 1. a model-avoiding absorption increases contact;
> 2. a minimum pinned transition or a Hall collision carrier admits a
>    label-preserving split/rotation of its transit bag;
> 3. two operation colourings induce compatible equality blocks on an
>    ambient adhesion, and the two proper-minor colourings glue to an
>    (r)-colouring of (G).

If this theorem holds for every defect, repeated contact augmentation ends
with an (N(v))-meeting (K_r)-model; alternative 3 is impossible because
(G) is not (r)-colourable.  This supplies the final branch bag
({v}) and closes the induction.

The theorem has two genuine unresolved subclaims:

* **ambient-lift inequality:** obtain an actual adhesion with enough free
  private colours from the model-relative rank defect; and
* **core/carrier exchange:** absorb every portal-bearing part outside the
  minimal contraction core and clean every first foreign-bag/extra-portal
  hit, or prove that the resulting descent repeats a boundary state and
  colour-glues.

Any formulation omitting these two mechanisms is merely the original
model-meeting obstruction in new language.

## 7. Next falsification and proof tests

1. **Boundary-state search, not graph-order search.**  Enumerate equality
   partitions and one-edge transition relations on a fixed adhesion.  Impose
   global saturation, every exact independent trace, transition novelty for
   every internal edge, and the two-shore capacity inequalities.  Search for
   the smallest join-prime signature which survives without a rooted model.

2. **Pinned-fan first-hit test.**  For a minimum pinned block, apply Rado to
   the fan endpoints and labelled bag boundaries.  Prove that one endpoint
   is model-clean, or extract an ambient separator.  The adversarial instance
   is the prescribed-root flag bottleneck; the new proof must use several
   edge operations, not one fan.

3. **Core/carrier descent.**  Optimize lexicographically over the Hall
   circuit, its rooted contractions, the selected contraction core, and the
   number of foreign/extra portal hits.  Prove that absorbing the first hit
   strictly improves this tuple.  If it cannot be absorbed, isolate the
   actual adhesion around that hit and apply crossed minor splicing.  The
   full-core singleton theorem in Section 2.13 is the terminal cell of this
   descent and must not be reproved by enumeration.

4. **Ambient lift audit.**  Starting from the target-slot Menger separator,
   add omitted colour classes and the contracted parity set one at a time.
   At each addition require either a model augmentation or a quantified
   increase in separator order.  Nested-cut transport then removes exact-cut
   recursion.

5. **Mandatory countertests.**  Every candidate lemma must be tested on:
   the universal colourful-pair realization, the join lift
   (F\vee K_3), the all-trace icosahedral graph, the bad colourful flag,
   the locked transit comb, and the planar wiring bramble.  It should fail
   for an explicit missing dynamic hypothesis on each, and it should use
   join-primality somewhere essential.

6. **Abandon black-box product amplification.**  Standard joins,
   lexicographic products, OR products, and fractional rounding have exact
   countermechanisms.  Reopen amplification only if a construction both
   preserves integral palette incompatibility and reflects every large minor
   to a depth-one model in a factor.

## 8. Bottom line

The verified advance now includes one genuine uniform rooted clique theorem
(Section 2.13), but not the general theorem.  The broader discovery is an
operation-sensitive gate which static counterexamples cannot satisfy:

\[
 \text{edge-by-edge new boundary states}
 \quad+\quad
 \text{two-shore capacity orientation}
 \quad+\quad
 \text{minimum pinned fans}.
\]

The exact research burden is now visible.  Lift a model-relative capacity
cut to an ambient palette adhesion, then prove that every hanging-core or
dirty-carrier encounter can be exchanged away; repetition must create two
compatible faithful minor states.  The full-core singleton case proves that
this mechanism terminates correctly once alignment is achieved.  This
carrier-exchange descent is the strongest current candidate for a genuinely
new uniform rooted-model principle.
