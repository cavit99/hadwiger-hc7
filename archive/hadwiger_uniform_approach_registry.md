# Uniform Hadwiger proof-search registry

This registry is keyed by mathematical mechanism.  A route is marked
**blocked** when its next assertion is false, is known only in a fixed
parameter, or is equivalent to an unproved strengthening.  It is reopened
only when a new invariant or exchange is supplied.  Fixed-\(t\) work is not
counted as progress toward the final theorem unless it produces a
label-free statement.

## U1. Contraction-generated colourful portal sets — BLOCKED IN THE
##     ABSTRACT / ACTIVE ONLY WITH MODEL GEOMETRY

In a proper-minor-minimal non-\(r\)-colourable graph, contract an induced
connected bipartite graph \(T=U\dot\cup W\).  In any colouring of the
proper minor, delete the contraction colour and one additional colour.
The external portal sets of both parities are colourful in the induced
\((r-2)\)-chromatic slice.  This is uniform and elementary.

The universality construction in
`hadwiger_uniform_bipartite_compression_barrier.md` proves that every
abstract pair of colourful sets occurs as the two parity portal sets of
one exact edge-contraction slice.  The join lift \(H\vee K_3\) shows that
even ambient proper-minor criticality contains an arbitrary lower
Hadwiger instance.  Thus colourfulness, common contraction origin, and
the individual Kempe carriers are not a rooted-model theorem.

Reopen only relative to a fixed clique model, where failure has a named
weighted cut, palette-polarized adhesion, or transit bag.

## U2. Connected-dominating induction — BLOCKED AS A SHORTCUT

Candidate lemma: every \(t\)-vertex-critical graph has a connected
dominating set \(D\) with \(\chi(G-D)\ge t-1\).  It would prove Hadwiger
immediately by induction, using \(D\) as the last branch set.  It survives
the complete graph atlas through seven vertices, Mycielski examples, and
iterated Hajós joins tested so far.

The audit in `hadwiger_connected_dominating_induction_audit.md` proves
that iterating this lemma is the Dominating Hadwiger Conjecture, a known
strengthening.  In a contraction-critical graph every nontrivial
connected dominating set \(D\) actually satisfies
\(\chi(G-D)\le t-2\), so a proposed witness must be a universal singleton.
No intermediate induction remains.

## U3. Nested contact-or-colour-gluing — ACTIVE

Audited theorem: nested minimum \(k\)-cuts transport a rooted clique model
and every disjoint capacity packet, provided the old bags lie entirely on
the processed side.  Minimum nested fragments therefore have strict
relative boundary surplus.

Current target: turn failure of full neighbourhood contact into an actual
adhesion whose equality partitions can be knitted and colour-aligned.
Merely naming a contact-or-separator lemma is equivalent to the original
model-meeting obstruction and does not count.

## U4. Kempe-colour packaging — BLOCKED

Criticality supplies rainbow neighbourhoods, pairwise Kempe connections,
and edge-deletion fans.  Pairwise two-colour connectivity does not package
rooted clique models uniformly; fixed-parameter counterarchitectures and
known failures beyond six colours rule out this input alone.

Reopen only with an operation-critical disjointness invariant, a gammoid
rank exchange, or a proof that failed packaging yields a colour-gluable
adhesion.

## U5. Degeneracy and extremal density — BLOCKED AS A STANDALONE ROUTE

The exact extremal threshold for a \(K_t\)-minor is of order
\(t\sqrt{\log t}\), whereas a \(t\)-critical graph only forces minimum
degree about \(t\).  Thus greedy degeneracy cannot reach \(t-1\) colours.
Local low-degree dependency rows occur with positive density even in
planar neighbourhood graphs, so neighbourhood-only discharging does not
repair the quantitative gap.

Reopen only if contraction-criticality is shown to force a new global
density or many coupled rooted models.

## U6. Graph-minor structure / apex-vortex colouring — BLOCKED

Clique-sums allow colour gluing, but the apex and vortex budgets in the
general structure theorem exceed the exact \(t-1\) palette.  High
connectivity of known minimal counterexamples is far below what arbitrary
terminal linkage needs.

Reopen only with a relative lean decomposition in which every adhesion is
either knitted for its actual equality blocks or augments the existing
clique model.

## U7. List, DP, and Alon--Tarsi strengthenings — CLOSED NEGATIVE

They would imply false strengthenings already for planar graphs (for
example, planar graphs need not be four-choosable).  Ordinary colour
permutations across separators are essential.

## U8. Algebraic, topological, odd-minor, and fractional routes — DORMANT

Known parameters or relaxations either point in the wrong minor direction
or require a non-existent integral rounding theorem.  No current invariant
forces an ordinary \(K_{\chi(G)}\)-model.  Keep independent exploration
alive, but reject a quasi-minor, subdivision, fractional minor, or odd
minor as a substitute for the required branch sets.

## U9. Fixed \(HC_7\) portal/web laboratory — SUPPORTING ONLY

Audited outputs retained for uniform use:

* nested cut transport of labels and capacities;
* strict web-versus-capacity arguments;
* bipartite compression into colourful portal sets;
* explicit counterarchitectures showing that static contacts and Kempe
  paths do not align branch bags.

Moser labels, finite atlases, and degree-seven case closures cannot by
themselves establish the active all-\(t\) objective.

## U10. Palette components versus clique-model havens — ACTIVE

Independent permutations on every component of \(H-X\) prove that one
actual component contains neighbourhood vertices of every colour absent
from the adhesion.  Comparing this component with the haven of a fixed
\(K_r\)-model gives the audited trichotomy in
`hadwiger_uniform_coloured_model_haven.md`:

* a palette-polarized adhesion of order below \(r\);
* an \(N(v)\)-meeting \(K_r\)-model; or
* one named transit bag with two disjoint colour-root prefixes.

The last outcome cannot be cleaned from linkage data alone; the end-locked
comb in `hadwiger_linkage_model_cleaning_counterexample.md` is a uniform
counterexample.  More sharply, the five-connected icosahedral example in
`hadwiger_same_haven_cleaning_counterexample.md` has full fixed-colouring
palette/model-haven agreement and a full transversal but no rooted
(K_5).  It fails global neighbourhood saturation.  The live theorem must
therefore use all colourings or the one-step minor-transition family, not
one selected colouring and its haven.

## U11. Rooted-linkage loss-pair repair — ACTIVE / INDEPENDENT

Robertson--Seymour's clique-model-to-rooted-linkage theorem loses one
model bag for roughly every pair of difficult roots.  Exact critical
traces give private, distinctly coloured roots, and disjoint pairs have
vertex-disjoint bichromatic Kempe paths.  Test whether those paths repair
the loss without invoking a general Kempe-packaging theorem.  A positive
no-loss statement would be a scalable rooted-model principle; a
counterexample must preserve the exact trace and model-haven conditions.

## U12. Colourful elimination flags — ARBITRARY FLAG REFUTED; ADAPTIVE
CHOICE ACTIVE

Every inclusion-minimal (k)-colourful set admits a nested private-colour
descent: delete the private colour class of one essential boundary vertex,
and the remaining boundary is ((k-1))-colourful.  Iteration gives the
flag in `hadwiger_colourful_elimination_flag.md`.  The uniform construction
in `hadwiger_colourful_elimination_flag_counterexample.md` shows that an
arbitrarily selected flag need not even have matching-linked roots, despite
the full independent-trace property; this persists for every order
`k>=4`.  Thus reserved-connector induction on a fixed flag is blocked.

The surviving adaptive target is recorded in
`hadwiger_adaptive_flag_matching_linkage.md`: choose the private layers and
roots coherently so that one root set works for every matching.  A fixed
matching can always be routed by disjoint bichromatic Kempe paths, but the
root transversal then depends on the matching.  The open step is exactly
the exchange from `forall M exists R_M` to `exists R forall M`, together
with coherence across all descent levels; a separator/capacity alternative
is required if that exchange fails.

## U13. Dynamic contraction cores and collision carriers — ACTIVE / FIRST
##      INFINITE CELL CLOSED

For every internal edge of a full minimal tree expansion core, one common
outside colouring gives a canonical defect state.  Boundary-faithful crossed
splicing collapses every branching or multicolour core to a clean rotation,
a named foreign-bag transit, or an end-locked

\[
                    \alpha,\delta,\alpha,\delta,\ldots,\alpha
\]

path.  In the spanning cell with one complex bag and (r-1) singleton
clique bags, a stronger matching-quotient argument closes **every** full
equality tree, uniformly in its order and in (r).  The theorem extends to
every equality Gallai core whose (alpha)-blocks are (K_2)'s.  Any
remaining full Gallai core has a genuine (alpha)-clique block of order at
least three or an (alpha)-odd-cycle block.

A second binary theorem removes the full-core hypothesis from the geometric
collapse.  On an arbitrary spanning tree of the whole bag, mark each edge
according as its edge-deletion defect colour equals the apex colour.  Equal
bits on incident lobes cross-splice or bypass, so every rigid tree is an
alternating-bit path.  What is lost relative to the matched core is named
colour saturation, not control of the hanging geometry.

Independently, a promoted Hall circuit in a (k)-connected host has at
least (k-r) surplus portal labels and at least (k-r) colour collisions
in every rainbow-core repair state.  Each collision has a named connected
carrier; co-rank-one circuits align the collision with one multiply hit bag
automatically.

The active uniform theorem is now **carrier/core exchange**: clean the first
foreign-bag or extra-portal hit, or exchange it to a smaller Hall circuit or
contraction core; failure must expose two faithful opposite operations with
one boundary state.  Static state algebra is blocked by the explicit
transition diamond, and connectivity alone is blocked by a high-connectivity
lift.  Actual all-minor criticality and labelled Hall geometry must both be
used.

Primary artifacts:

* `hadwiger_dynamic_transit_tree_principle.md`;
* `hadwiger_binary_transition_tree.md`;
* `hadwiger_spanning_singleton_gallai_layer_theorem.md`;
* `hadwiger_hall_circuit_anti_diamond.md`;
* `hadwiger_boundary_state_diamond_counterexample.md`.

## U14. Full minimum-cut block pressure — ACTIVE / INFINITE RANGE CLOSED

Let a `k`-contraction-critical graph have a minimum cut `S` of order
`c`, with `m` full components, and put `p=chi(G[S])`.  The uniform block
gluing theorem now gives

\[
                         m\le p\le c-m,
                         \qquad c\ge2m.
\]

The new upper bound is not a density estimate.  In every optimal boundary
colouring at least `m` colour classes must be nonsingleton; otherwise
`m-1` opposite shores connect all nonsingleton classes and enough
singleton classes, while the residual singleton classes form a literal
clique, producing one common exact partition on every side.  Moreover
each side realizes every prescribed family of at most `m-1` independent
blocks as distinct exact traces.

In a least Hadwiger counterexample, reserve lifting adds `p<=k-2` and
forces every boundary `K_{k-m}` model to use at least `c-m+2` vertices.
Thus all cells with `2m>c` are eliminated uniformly.

A further reserve-support argument now gives an actual component cap.  In
a minor-minimal `HC_k` counterexample, every minimum cut has at most
`k-3` components.  If it has exactly `m=k-3` components, its order is at
least

\[
                         m^2-2m+2=k^2-8k+17.
\]

Indeed `m>=k-2` leaves a boundary `K_1` or `K_2` core and enough reserves
to lift directly to `K_k`.  At `m=k-3`, a smaller cut would make an
`m`-chromatic boundary critical core violate the girth-five Moore bound,
giving a `K_3` supported on at most four vertices; the shores again lift
it to `K_k`.  This removes a second parameter-uniform infinite range.

The live step is
completion-state synchronization for the first `m` nonsingleton blocks;
fewer blocks are already automatically synchronized side by side.

Primary artifacts: `hadwiger_uniform_full_cut_inequalities.md` and
`hadwiger_hc7_minimum_eight_cut_four_shores.md`.

At the equality layer, a rejecting side now also has a clean internal
Kempe carrier for every boundary pair.  A `q`-packet of disjoint pairwise
adjacent carriers inside one shore lifts, with the other full shores, to
`K_{m+q-1}`.  Thus target-minor exclusion forces an exact labelled
component defect before `q=k-m+1` carriers can be assembled.  This is the
positive geometric content which survives the sharp state-realization
barrier; the live problem is to exchange the defect certificates obtained
from different pair orders.

Additional artifact: `hadwiger_uniform_last_pair_carrier_exchange.md`.

The reserve-support method has also been extended from literal short
cycles to arbitrary clique-minor density thresholds.  Sampling
`c-m+1` vertices of a critical boundary core gives expected average
degree at least `m(m-1)/(2m-1)`; a density-forced `K_{t-m}` on that
support leaves exactly the required `m-1` reserves.  This closes
`m=t-3` for all `t>=8`, closes `m=t-4` for `t>=10`, and forces
`t-m=Omega(t/sqrt(log t))` asymptotically.  This is now the strongest
parameter-uniform output of the minimum-cut family.

## U15. Combining unrooted contraction models — BLOCKED WITHOUT COLOUR
##      STATES

The family `J_r=K_r join I`, with `I` the icosahedron and `t=r+5`, has

\[
 chi(J_r)=eta(J_r)=t-1,\quad kappa(J_r)=t,\quad delta(J_r)\ge t,
\]

contains no `K_t` minor, and every contraction of an icosahedral edge
still has chromatic and Hadwiger number `t-1`.  For `r=0` this is every
edge contraction.  Hence abundant tight `K_{t-1}` models, even with
connectivity and degree at the counterexample scale, cannot be combined
by an unrooted overlap invariant.  Reopen only with a condition using the
missing `chi(G)=t` datum: a common labelled boundary state, a Kempe
exchange tied to model bags, or an operation-sensitive carrier.

Primary artifact: `hadwiger_icosahedral_multi_contraction_barrier.md`.

## U16. Bipartite total-contraction split states — ACTIVE / UNIFORM SPLIT
##      THEOREM PROVED

For every connected induced bipartite set in a proper-minor-minimal
non-`q`-colourable graph, total contraction has chromatic number exactly
`q`.  In any colouring of that contraction, every spanning tree contains
an edge whose two connected sides both see all `q-1` secondary colours.
The proof is a palette-uniform poor-side orientation: without such an
edge, one vertex has only rich tree branches, which can be coloured by
putting the contraction colour on one global bipartition class and a
branch-specific common colour on the other.

Separately contracting the two returned sides forces a faithful state
jump on their actual external neighbourhood.  In a near-clique model,
alignment of the secondary colours with pairwise adjacent labelled
carriers gives the target clique immediately.  The live obstruction is a
single palette-to-label collision (for `HC_7`, potentially the apex-shadow
colour), not unrelated local edge states.

Primary artifact: `hadwiger_constant_corridor_total_contraction_state.md`.

In the spanning singleton-shell cell, the palette-to-label exchange is now
literal.  If the one complex bag is bipartite and `d>=2` singleton labels
miss the apex, proper-minor quotient colourings put `d` distinct witnesses
in one bipartition class.  They and the apex form one connected carrier;
the residual bag is the other.  Target-minor exclusion therefore forces
either a `d`-vertex deletion which disconnects the bag or an entire
singleton portal class concentrated on those `d` witnesses.  This closes
all such shells with bag connectivity and portal multiplicity at least
`d+1`.

Additional artifact: `hadwiger_palette_label_alignment_bipartite_shell.md`.
