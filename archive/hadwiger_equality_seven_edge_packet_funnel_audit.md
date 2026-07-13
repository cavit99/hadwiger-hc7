# Adversarial audit: seven-edge equality packet funnel

**Verdict: GREEN AS PATCHED.**  The finite classification and the
mathematical compatibility/packet deductions in
`hadwiger_equality_seven_edge_packet_funnel.md` are sound under the stated
counterexample-derived hypotheses.  The strengthened verifier
`equality_gate_seven_edge_packet_atlas.py` reruns successfully under
`.venv/bin/python` and now asserts the cyclic-hull status of every direct
witness, replays every displayed positive model, fixes the graph6/edge
manifest, and checks that the seven full triangles, two centre locks, and
one theta core exhaust the ten-way residue.

Three manuscript scope points were repaired:

1. contracting two singleton shores need not produce a *proper* minor,
   although it always produces a minor and therefore remains `K_7`-free;
2. a nonbipartite compatibility graph closes **or descends to a nested
   exact seven-cut**, so its three new types are removed from the current
   cut only modulo that descent; and
3. an arbitrary internal operation need not preserve the displayed split
   geometry.  Boundary-faithful open-shore operations give strict states,
   while the cited ear/two-anchor theorem specifically decorates
   interface-edge deletions.

This is an internal audit of correctness and executable coverage, not an
external novelty determination.

## 1. Reproduction and independent checks

The principal command was

```text
.venv/bin/python equality_gate_seven_edge_packet_atlas.py
```

It completed with the asserted summary:

```text
direct cyclic-hull closures 18
nonbipartite compatibility types (1, 2, 6, 15, 20)
residual types (0, 7, 8, 9, 10, 11, 16, 22, 29, 30)
all seven-edge packet-atlas assertions verified
```

The following checks were then performed independently of the atlas's
hard-coded classification sets.

* A brute clique/independent-set partition test was used as a second split
  graph recognizer on every seven-edge graph in the order-seven NetworkX
  atlas.  It agreed with `is_split()` in every case.
* On all 54 nonsplit seven-edge types, a second exhaustive branch-partition
  checker agreed with the imported nine-vertex checker.  Exactly 31 were
  negative after adjoining two nonadjacent full helpers.
* All cyclic hulls of all 31 types were regenerated, rather than merely
  testing the hard-coded orders.  Exactly the 18 indices in
  `DIRECT_WITNESSES` possessed a hull whose every covering crossing
  quotient was positive, and every displayed order was literally one of
  the regenerated cyclic hulls.
* The two centre-locked rows were recomputed with the independent generic
  minor search.  Their centre signs were respectively `+,+,-` and
  `+,-,+`, exactly as claimed.

The graph6 strings emitted by the rerun agree label-for-label with the ten
rows in the manuscript.  They are now executable assertions rather than
unverified print output.

## 2. The 31-type universe

The filters used by `seven_edge_types()` are exhaustive for the stated
finite cell:

1. `nx.graph_atlas_g()` contains one representative of every unlabelled
   graph on seven vertices;
2. order and edge count are both tested to be seven;
3. nonsplitness is tested by the Földes--Hammer forbidden induced
   subgraphs, and was independently cross-checked by the defining
   clique/independent partition;
4. the complement is the boundary graph `J`; and
5. two vertices complete to `S` and anticomplete to one another represent
   the two contracted full shores exactly.

The nine-vertex minor search enumerates all disjoint connected
seven-branch models, including unused vertices.  A `K_7` model in this
quotient lifts through the two connected shores.  Conversely, the global
`K_7`-minor-free hypothesis makes the quotient negative.  Properness of
the quotient operation is unnecessary for this implication and is now no
longer asserted when both shores are singleton.

The resulting 31 representatives are stable within the run.  The ten
residual graph6 codes decode to exactly the manuscript's missing-edge
sets; the new `EXPECTED_RESIDUAL_MANIFEST` checks both the code and every
edge.

## 3. Full-split cyclic-hull filter

`cyclic_hulls()` checks precisely the hypotheses needed by the audited
two-shore web theorem:

* the ordered core has between four and seven vertices;
* every actual boundary edge inside the core is a frame edge; and
* the omitted set, of order at most three, induces a bipartite boundary
  graph.

For each alternating four-tuple, two crossed carriers extend to adjacent
connected sets whose contact rows cover `S`.  Surplus overlaps may be
deleted.  It is therefore enough to assign each of the three remaining
labels to one side, giving the eight minimal disjoint rows tested by
`split_crossing_forces()`.  Swapping the two carrier sides gives an
isomorphic quotient, so no second orientation is lost.

The verifier now first asserts that every hard-coded direct order is a
regenerated cyclic hull.  It then reconstructs and independently replays
each returned seven-bag certificate.  Exactly 18 of the 31 types pass
this existential hull test.  In the counterexample setting, the crossed
case lifts `K_7`, while the all-crossless case six-colours `G`; hence these
18 are genuinely closed.

## 4. Compatibility graph and portal two-colouring

For a boundary label `s` with `d_Q(s)>=2`, seven-connectivity gives

```text
|N_D0(s)| + |N_D1(s)| >= 7-d_J(s) = 1+d_Q(s) >= 3.
```

Thus `s` has at least two portals in one shore.  Assigning one such shore
to every vertex of `L(Q)` is an actual two-colouring of the vertex set,
not an abstract choice detached from the graph.

For a pair `a,b`, `covering_rows()` enumerates all `3^5` possibilities:
`a,b` lie in both rows, and each remaining label lies in the first row,
the second, or both.  Hence an edge of `A(Q)` means exactly that **every**
covering split retaining `a,b` on both sides has a positive ten-vertex
quotient.

If `A(Q)` is nonbipartite, the portal-shore assignment has a monochromatic
edge.  The label-free double-root theorem applied to those two portal
classes gives either:

* their connected covering split, which is positive by definition;
* a full/full split, also positive; or
* a nested exact seven-cut.

No stronger connectivity is used.  The computation gives precisely the
five nonbipartite indices `(1,2,6,15,20)`; indices `6,15` were already in
the 18 direct closures.  Thus three more types leave the current cut,
modulo the nested-cut outcome.  This qualification is now explicit in
Theorem 4.1.

## 5. Cyclic packet ownership

A packet demand consists of the two vertex-disjoint chord pairs of an
alternating four-tuple in a cyclic hull.  Those pairs really are missing
boundary edges: alternating endpoints are nonconsecutive in the hull,
while every boundary edge on the hull is a frame edge.

For each demand, apply the two-shore web theorem to its hull.  If both
shore societies were crossless, deleting the bipartite omitted boundary
would leave a planar graph; four colours there and two fresh colours on
the omitted boundary would six-colour `G`.  The standing non-six-
colourability therefore forces a cross in at least one shore.  Removing
the artificial terminals leaves two nonempty vertex-disjoint connected
carriers incident with the demanded pairs.

This proves an owner for **each packet edge separately**.  It does not
choose coherent owners or simultaneous paths for different packet edges.
The manuscript states this limitation, and none of the finite assertions
silently upgrades it.

## 6. Matching triangles and centre quotients

For three disjoint demanded missing edges, a simultaneous three-linkage in
one shore gives three disjoint carriers.  A minimal connector makes their
contracted adjacency graph a tree; on three vertices its centre is one of
the three carriers.  The opposite full shore becomes vertex `10` and is
complete to the seven boundary vertices but anticomplete to the carrier
vertices.  This is exactly the eleven-vertex graph built by
`packet_tree_models()`.

The mapping from the three `TREES` rows to centres was checked:

```text
7-8-9  -> matching[1]
8-7-9  -> matching[0]
7-9-8  -> matching[2]
```

Every positive returned model is now replayed for nonempty, disjoint,
connected, pairwise adjacent branch bags.  Such a quotient model lifts:
the three carrier vertices represent disjoint connected shore pieces, the
helper represents the opposite shore, and boundary vertices are literal
singletons.  Extra contacts in the actual graph are harmless.

The result is exactly:

* seven types positive for all three centres;
* type `Fh_gG` positive for the first two centres and negative only when
  carrier `45` is central;
* type ``F`o_g`` positive except when carrier `01` is central.

Therefore a fully positive triangle is pairwise-linkable, by individual
packet ownership, but cannot occur as a simultaneous triple in either
shore.  In a centre-locked type, any simultaneous triple which survives
must use the unique negative carrier as centre.  The assertion is only a
necessary orientation constraint; it does not claim such a triple exists.

## 7. Theta core and exhaustive ten-way residue

The final residual `FwJG?` has matching number two.  Its nontrivial
five-vertex component is the stated `K_4-e` with the missing edge replaced
by a two-edge path, plus two isolated vertices.  Its packet-demand graph
is connected with seven vertices, eight edges, degree sequence
`3,3,2,2,2,2,2`, and cycle rank two; equivalently it is a theta core.

The verifier now asserts the exact disjoint union

```text
FINAL_RESIDUAL
 = {theta type}
   union FULL_PACKET_TRIANGLES
   union CENTER_LOCKED_TRIANGLES.
```

Thus the claimed `7+2+1` classification is exhaustive, not merely a
catalogue of structures found in ten already-known rows.

## 8. Exact frontier consequence

Modulo nested exact-cut descent, the complete nonsplit, two-full-shore,
seven-missing-edge cell has been reduced to ten explicit boundaries but
only two label-free obstruction forms:

1. a matching-packet triangle whose three pair demands have individual
   shore owners but no target-positive simultaneous triple (with two
   oriented centre locks); or
2. a rank-two theta packet graph with every demand individually owned.

This is a sound finite funnel, not a closure of the seven-edge layer and
not a proof of `HC_7`.  The still-missing uniform theorem must coordinate
the independently owned packet edges.  It must turn pairwise-but-not-
triple linkage into a bounded-adhesion rope/ladder descent, or produce two
opposite boundary-faithful operations with a common equality state.

Larger missing-edge layers are outside this atlas.  The ten graph6 labels
are diagnostic representatives; the reusable mathematical target is the
state-decorated packet exchange, which no longer depends on those labels.
