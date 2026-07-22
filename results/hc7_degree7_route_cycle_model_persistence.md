# Doubled Kempe routes: a persistent model edge or a short bag cycle

**Status:** written proof; [separate internal audit **GREEN**](hc7_degree7_route_cycle_model_persistence_audit.md).
This theorem
refines the doubled-route residue in the degree-seven branch.  It identifies
an edge whose proper-minor response coexists with the fixed rooted model, or
normalizes the failure of every such edge to a literal cycle through three,
four, or five rooted bags.  It does not align a response colouring with the
bag labels, construct a `K_7`-minor model, or prove `HC_7`.

## 1. Setup

Use the setup of the audited
[tight-pole localization theorem](hc7_degree7_tight_pole_edge_localization.md).
Thus `G` is seven-connected,

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G,
\tag{1.1}
\]

`u` has degree seven, and

\[
 S=N_G(u),\qquad C=G-N_G[u],\qquad A=G-u,
 \qquad H=G[S],\qquad F=\overline H.                 \tag{1.2}
\]

Choose a matching `\{e_0,e_1,e_2\}` in `F`, write `e_0=ab`, and put

\[
                              U=S-\{a,b\}.             \tag{1.3}
\]

Fix an exact-`e_0` six-colouring of `A`.  For `i=1,2`, write
`e_i=x_i y_i` and let `K_i` be the corresponding full bichromatic
component.  Then

\[
 K_i\cap S=\{x_i,y_i\},\qquad K_i-S\subseteq C,       \tag{1.4}
\]

and `K_1,K_2` are vertex-disjoint.  Assume that each `K_i` contains two
internally vertex-disjoint `x_i-y_i` paths.  Choose two such paths and let

\[
                              Z_i                       \tag{1.5}
\]

be their union.  The graph `Z_i` is a literal simple cycle, and
`Z_1,Z_2` are vertex-disjoint.  Every edge `h` of `Z_i` is nonseparating
for the layer's root connection: `Z_i-h` still contains an
`x_i-y_i` path.

The exact matching theorem supplies a fixed `U`-rooted `K_5` model

\[
                       \mathcal B=(B_r:r\in U)          \tag{1.6}
\]

in `A-\{a,b\}`, where `r\in B_r`.  Put

\[
                         W=\bigcup_{r\in U}B_r.         \tag{1.7}
\]

An edge `h` is **persistent for `\mathcal B`** when the same five sets in
(1.6) remain a labelled `U`-rooted `K_5` model after deleting `h`.

For an edge set `Q`, let `\mathcal R(Q)` be the family of boundary
matchings induced on `S` by all six-colourings of `G-Q`, and put

\[
 \mathfrak T_i=\{M:M\text{ is a matching of }F,
                         \ \{e_0,e_i\}\subseteq M\}.   \tag{1.8}
\]

Call `Q` **response-aligned for layer `i`** when
`\mathcal R(Q)\cap\mathfrak T_i\ne\varnothing`.  For one edge we write
`\mathcal R(h)` and say that `h` is response-aligned.

## 2. Exact model-persistence test

### Lemma 2.1

Let `h` be any edge of `A-\{a,b\}`.

1. If at least one end of `h` lies outside `W`, then `h` is persistent for
   `\mathcal B`.
2. If both ends lie in one bag `B_r`, then `h` is persistent exactly when
   it is not a bridge of `G[B_r]`.
3. If the ends lie in distinct bags `B_r,B_s`, then `h` is persistent
   exactly when there is another edge between `B_r` and `B_s`.

#### Proof

Deleting an edge with an end outside `W` changes neither the connectivity
of a displayed bag nor an adjacency between two displayed bags.  This
proves item 1.  An edge internal to `B_r` affects the displayed model
exactly when its deletion disconnects that bag, proving item 2.  An edge
between distinct bags affects neither bag's connectivity; it destroys the
required `B_r-B_s` adjacency exactly when it was the sole edge realizing
that adjacency.  This proves item 3. \(\square\)

### Corollary 2.2 (a persistent edge carries the response with the model)

If an edge `h` of `Z_i` is persistent for `\mathcal B`, then the same
rooted `K_5` model occurs in `G-h`.  Every six-colouring of `G-h` has all
of the following properties:

1. the ends of `h` are monochromatic;
2. its boundary matching belongs to `\mathcal R(h)` and has order two or
   three; and
3. for each of the other five colours, the ends of `h` lie in one
   bichromatic component.

Consequently a response-aligned persistent edge realizes a returned
matching containing the prescribed pairs `e_0,e_i`, possibly with a third
pair, together with the fixed rooted labels in one edge-deleted host.  If
a persistent edge is not response-aligned, its nonempty response family is
an exact operation-specific mismatch: every returned matching omits `e_0`
or `e_i`.

#### Proof

The persistence assertion is the definition and Lemma 2.1.  The edge `h`
has at least one end in `C`, because (1.4) holds and `x_i y_i` is not an
edge of `H`.  It is therefore not an edge of the pole shore `G[N[u]]`.
The audited off-pole-shore edge-response theorem gives the three colouring
conclusions.  The last sentence is precisely the definition of response
alignment and its negation. \(\square\)

The coexistence in Corollary 2.2 is not yet a terminal allocation.  The
five palette colours in the edge response are not thereby identified with
the five rooted branch-set labels.

## 3. A minimal bond gives the exact multi-edge response

Fix a layer `i`.  An `x_i-y_i` **bond** in `K_i` is a set

\[
                  D=E_{K_i}(X,Y),\qquad
                  V(K_i)=X\mathbin{\dot\cup}Y,         \tag{3.1}
\]

where `x_i\in X`, `y_i\in Y`, and both `K_i[X]` and `K_i[Y]` are
connected.  Such a bond is an inclusion-minimal `x_i-y_i` edge cut.

### Theorem 3.1 (minimal aligned bond response)

Let `D` be an `x_i-y_i` bond.  Then:

1. `|D|\ge2`, and every edge of `D` is individually nonseparating for the
   `x_i-y_i` connection in `K_i`.
2. The graph `G-D` has a six-colouring with exact boundary matching
   `\{e_0,e_i\}` in which the ends of every edge of `D` are
   monochromatic.  This colouring descends through the simultaneous
   contraction of all edges of `D`.
3. Choose an inclusion-minimal nonempty `J\subseteq D` which is
   response-aligned for layer `i`.  Either `J=\{h\}` and `h` is the
   desired response-aligned nonseparating edge, or `|J|\ge2` and all of
   the following hold:

   a. every proper subset of `J` rejects every matching in
      `\mathfrak T_i`;
   b. in every `\mathfrak T_i`-response colouring of `G-J`, the ends of
      every edge of `J` are monochromatic;
   c. fix such a colouring, an edge `h=pq\in J`, and a colour different
      from the common colour of `p,q`.  Either `p,q` lie in one
      bichromatic component, or their two endpoint components both meet
      `S`, and switching either one produces a boundary matching outside
      `\mathfrak T_i`;
   d. for every `h\in J`, every six-colouring of `G-h` has a boundary
      matching of order two or three outside `\mathfrak T_i`, makes the
      ends of `h` monochromatic, and supplies all five endpoint locks.

#### Proof

The two internally vertex-disjoint `x_i-y_i` paths are edge-disjoint, so
every `x_i-y_i` edge cut meets them in two distinct edges.  This proves
`|D|\ge2`.  Deleting one edge still leaves the other selected path, so
every edge of `D` is individually nonseparating.

Let `alpha_i,beta_i` be the two colours of the roots in the fixed
exact-`e_0` colouring.  Interchange those colours on all vertices of `X`
and leave the colouring unchanged elsewhere in `A`.  The only
`alpha_i-beta_i` edges crossing from `X` to `Y` are the edges of `D`, so
this is a proper colouring of `A-D`.  Its only boundary change is that
`x_i` acquires the colour of `y_i`.  The colour `alpha_i` is now absent
from `S`; give it to `u`.  The result is a six-colouring of `G-D` with
exact matching `\{e_0,e_i\}`.

Every edge of `D` originally joined opposite colours and has exactly one
end interchanged.  Its two ends are therefore monochromatic in the new
colouring.  Equality propagates through every component of the graph with
edge set `D`, so the colouring descends through simultaneous contraction.
No other edge has both ends in one such component, since that would be a
monochromatic edge of `G-D`.

The set `D` is response-aligned by the displayed colouring, while the
empty set is not because `G` is not six-colourable.  Hence an
inclusion-minimal nonempty aligned subset `J` exists.  Its definition
proves item 3a.

Let `psi` be any aligned response colouring of `G-J`.  If an edge
`h\in J` had differently coloured ends, restoring `h` would give an
aligned colouring of `G-(J-\{h\})`, contrary to minimality.  This proves
item 3b and also shows that `psi` descends through simultaneous contraction
of `J`.

Fix `h=pq\in J` and an alternate colour.  If the two endpoint components
are distinct, switch the component containing `p`.  This is a proper
colouring of `G-J` in which `p,q` have different colours, so `h` can be
restored.  The resulting boundary matching cannot remain in
`\mathfrak T_i`, by item 3a.  In particular the switched component must
meet `S`; otherwise the boundary trace would not change.  Apply the same
argument to the component containing `q`.  This proves item 3c.

When `|J|\ge2`, each singleton `\{h\}` is a proper subset of `J` and is
therefore not response-aligned.  The off-pole-shore edge-response theorem
applies to `h`: it gives a nonempty response family of matching order two
or three, monochromatic ends and all five locks.  Every matching in that
family lies outside `\mathfrak T_i`, proving item 3d. \(\square\)

### Proposition 3.2 (common-host bond-response signatures)

For every `h\in D`, choose one six-colouring of `G-h` and restrict it to
the common host `G-D`.  Across the edges of `D`, its equality signature is
exactly `\{h\}`: the ends of `h` are equal, while every edge of
`D-\{h\}` is present in `G-h` and hence has differently coloured ends.
Together with the all-equal colouring in Theorem 3.1(2), these give
`|D|+1` operation-labelled signatures on one host.

When `D=\{h_1,h_2\}`, the signatures are precisely

\[
       (\mathrm{equal},\mathrm{equal}),\quad
       (\mathrm{equal},\mathrm{proper}),\quad
       (\mathrm{proper},\mathrm{equal}).               \tag{3.2}
\]

The missing `(proper,proper)` signature would restore both edges and
six-colour `G`.

#### Proof

Minor-minimality supplies a six-colouring of every `G-h`.  Its ends on
`h` are equal, or `h` could be restored and `G` would be six-colourable.
Every other edge of `D` is present and therefore proper.  Restriction to
`G-D` preserves these equalities and inequalities.  Theorem 3.1(2)
supplies the all-equal signature.  The final assertion follows by restoring
both proper edges. \(\square\)

## 4. Failure of persistence is a short rooted-bag cycle

For a cycle `Z_i` containing no persistent edge, traverse `Z_i` once and
record a transition whenever two consecutive vertices lie in different
bags.  Let `T_i` be the subgraph of `K_U` whose edges are the unordered
pairs of bag labels occurring at those transitions and whose vertices are
the ends of those edges.  Unused bag labels are not isolated vertices of
`T_i`.

### Theorem 4.1 (essential contact-cycle normalization)

Suppose neither `Z_1` nor `Z_2` contains an edge persistent for
`\mathcal B`.  Then:

1. `Z_i\subseteq W` for `i=1,2`.
2. Each `T_i` is a nonempty connected simple Eulerian graph, and

   \[
       3\le |E(T_i)|,\qquad
       E(T_1)\cap E(T_2)=\varnothing.                  \tag{4.1}
   \]

3. For some `j\in\{1,2\}`,

   \[
                         T_j\cong C_m
                         \quad\text{for }3\le m\le5.   \tag{4.2}
   \]

   The labels `x_j,y_j` are distinct vertices of this cycle.
4. For every label `r\in V(T_j)`, the intersection `Z_j\cap B_r` is one
   path, called the `r`-sector, and it is the unique `B_r`-path between
   its two transition vertices (the trivial path when both transitions
   use one sector vertex).  Every edge of a nontrivial `r`-sector is a
   bridge of `G[B_r]`.  Every component of
   `G[B_r]-V(Z_j\cap B_r)` has exactly one attachment vertex in the
   sector; explicitly, for every such component `Q`,

   \[
       |N_{B_r}(Q)\cap V(Z_j\cap B_r)|=1.              \tag{4.3}
   \]
5. Every transition edge of `Z_j` is the unique edge in the entire host
   between its two consecutive rooted bags.  Contacts between
   nonconsecutive bags, including contacts from off-sector vertices, are
   not otherwise constrained.

Thus failure of model persistence on both doubled layers is not an
arbitrary dirty-path configuration.  One layer is a literal cyclic chain
of three to five bridge sectors joined by unique labelled bag contacts.
Conversely, on any literal cycle, containment in `W`, the bridge property
for every within-bag cycle edge, and uniqueness of every cross-bag contact
are sufficient for every cycle edge to be nonpersistent.  The displayed
normal form is therefore exact.

#### Proof

Fix `i`.  If a vertex of `Z_i` lay outside `W`, either incident cycle edge
would have an end outside `W` and would be persistent by Lemma 2.1(1).
Hence `Z_i\subseteq W`.

A transition edge between `B_r` and `B_s` is nonpersistent.  By
Lemma 2.1(3), it is the unique edge in the whole graph between those two
bags.  In particular, the same unordered label pair cannot occur at two
different transitions of `Z_i`.  Hence `T_i` is simple.  The cyclic order
on `Z_i` gives a closed trail through the successive bag labels, using
every edge of `T_i` once.  It follows that `T_i` is connected and every
one of its vertex degrees is even.

The graph `T_i` is nonempty.  Otherwise the whole literal cycle `Z_i`
would lie in one bag, and each of its edges would be a nonbridge of that
bag, contrary to Lemma 2.1(2).  A nonempty connected simple Eulerian graph
contains a cycle, so it has at least three edges.

The literal cycles `Z_1,Z_2` are vertex-disjoint.  If the same label pair
`rs` occurred in both `T_1` and `T_2`, their two transition edges would be
distinct edges between `B_r` and `B_s`.  Each would then be persistent by
Lemma 2.1(3), a contradiction.  This proves (4.1).

There are only ten unordered pairs of the five labels in `U`.  Therefore

\[
                         |E(T_1)|+|E(T_2)|\le10,        \tag{4.4}
\]

and one of the two graphs, say `T_j`, has at most five edges.  A connected
simple Eulerian graph decomposes into edge-disjoint cycles.  Since every
such cycle has at least three edges, a graph with three to five edges has
only one cycle and no remaining edges.  It is therefore `C_m` for some
`3\le m\le5`, proving (4.2).  The cycle `Z_j` contains the distinct roots
`x_j\in B_{x_j}` and `y_j\in B_{y_j}`, so both labels occur in `T_j`.

Because `T_j` is a simple cycle, its closed trail meets each of its labels
in one maximal sector.  Hence `Z_j\cap B_r` is one path.  Every edge of
that path is nonpersistent and lies inside `B_r`; Lemma 2.1(2) makes it a
bridge of `G[B_r]`.  An alternative path in `G[B_r]` between the two
transition vertices would bypass a sector edge, so the sector is the
unique such path.  When the sector consists of one vertex, this is the
trivial path and needs no bridge argument.

Let `Q` be a component of
`G[B_r]-V(Z_j\cap B_r)`.  Connectivity of `B_r` gives at least one
neighbour of `Q` in the sector.  If it had two distinct sector neighbours,
a path through the connected graph `Q` between those neighbours would,
together with the intervening sector subpath, put a sector edge on a cycle
inside `G[B_r]`.  That edge would not be a bridge, a contradiction.  Thus
the neighbour is unique.  The transition-edge assertion was already proved
from Lemma 2.1(3), and no part of the argument controls the remaining
cross-bag contacts.

For the converse assertion, an edge on such a cycle is either a bridge of
one displayed bag or the sole contact between two displayed bags.
Lemma 2.1(2)--(3) makes it nonpersistent in either case.
\(\square\)

## 5. Exact response/allocation trichotomy

### Corollary 5.1

For the two selected doubled-route cycles and the fixed rooted model,
exactly one of the following holds.

1. **Aligned persistent response.**  Some cycle edge is persistent for
   `\mathcal B` and response-aligned for its layer.  A returned boundary
   matching containing the prescribed pairs `e_0,e_i`, possibly with a
   third pair, all five endpoint locks and the same five rooted bags
   coexist in one proper edge-deleted minor.
2. **Persistent response mismatch.**  At least one cycle edge is
   persistent, but no persistent cycle edge is response-aligned.  Every
   persistent cycle edge still has a nonempty order-two-or-three response
   family and five locks, while every such response omits `e_0` or the
   corresponding `e_i`.
3. **Essential short cycle.**  No cycle edge is persistent.  One layer has
   the literal `C_3`, `C_4` or `C_5` rooted-bag structure of Theorem 4.1.

#### Proof

First ask whether a response-aligned persistent edge exists.  If so,
Corollary 2.2 gives outcome 1.  If not, ask whether any persistent cycle
edge exists.  Corollary 2.2 gives outcome 2 when it does, and Theorem 4.1
gives outcome 3 otherwise.  The defining conditions make the outcomes
mutually exclusive. \(\square\)

## 6. Trust boundary and next operation

Outcome 1 proves the matching/model **coexistence** part of the proposed
nonseparating-edge response lemma.  It does not prove the additional
palette-to-bag incidence needed for a terminal `K_7` construction.

Theorem 3.1 shows why a single-edge formulation is not the unconditional
route output.  The pole switch is always carried by a whole bond.  A
minimal aligned subset either collapses to one edge or leaves a genuinely
multi-edge response whose every single operation returns a different
boundary matching.  Proposition 3.2 retains the operation provenance on
one common deleted host.

Outcome 2 is the exact dynamic obstruction: contraction-criticality
returns a colouring and the fixed model survives, but the operation returns
the wrong boundary matching.  Repeating deletion and contraction of the
same edge cannot help, because those two response families coincide.
No example of this mismatch is known under all hypotheses (1.1).  Finite
boundary-response realizations show only that exact matching languages,
doubled routes and fixed-model persistence do not by themselves eliminate
the branch; the global minor exclusion and criticality must do further
work.

Outcome 3 is the exact static allocation obstruction.  The next bridge
argument should use the whole short cycle, not one path or one bag.  A
bridge whose attachments span separated sectors can potentially split the
cycle into labelled branch sets; interval-local bridges should instead be
tested for an actual order-seven separation.  The decreasing parameter must
be the order of a connected literal side of that separation, not the cycle
length or the number of bags.

The short-cycle outcome is realizable from rooted-model data alone.  Take
tree bags `B_1,...,B_5`; use disjoint paths in `B_5` to form two
vertex-disjoint cycles with bag traces `1-2-5-1` and `3-4-5-3`; join the
two paths inside `B_5` by one tree path; and add exactly one contact for
each of the four unused bag pairs.  Every transition is then the unique
contact of its pair and every within-bag cycle edge is a bag bridge.  Thus
neither triangle has a persistent edge.  This construction is not asserted
to satisfy the chromatic or connectivity hypotheses in (1.1); it shows why
those global hypotheses must be spent in the next operation.

## Dependencies

- [exact matching languages and the fixed rooted `K_5` model](hc7_degree7_matching_bridge_bundle.md)
- [tight-pole edge localization and the doubled-route residue](hc7_degree7_tight_pole_edge_localization.md)
- [off-pole-shore edge responses](hc7_degree7_one_spoke_bridge_corollaries.md)
- [deletion/contraction response equivalence](hc7_marked_edge_response_coupling.md#1-one-edge-has-only-one-response-family)
