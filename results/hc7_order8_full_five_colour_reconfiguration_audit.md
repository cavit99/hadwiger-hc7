# Independent audit of the order-eight full five-colouring reconfiguration theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order8_full_five_colour_reconfiguration.md`](hc7_order8_full_five_colour_reconfiguration.md)
at SHA-256

```text
c15e2a66b6926d926ff269c79a8abb33a9ee5e75ecbf925b4c43315a3c46dd07
```

and the deterministic verifier
[`hc7_order8_full_five_colour_reconfiguration_verify.py`](hc7_order8_full_five_colour_reconfiguration_verify.py)
at SHA-256

```text
579aa66ceca3edc82d860ef2e55d5bfeca4ff705dccc657446ad5bf0f219fdbe
```

The low-degree lifting, reduction to the minimum-degree-four cores, exact
`K_5`-minor test, five-colouring enumeration, reconfiguration search, and
host shortest-path consequence are correct.  An independent C++
implementation reproduced the six surviving cores, their edge and
colouring counts, and one-component verdicts without using the verifier's
expected table.

## 1. Low-degree lifting and core reduction

Let `v` have degree at most three.  During a lifted recolouring sequence in
`H-v`, the only obstruction is a proposed recolouring of a neighbour of
`v` with the current colour of `v`.  At most three colours occur on
`N_H(v)`, so at least two of the five colours are available at `v`.  One is
the current colour and a distinct available colour can be used first.
After that change the proposed neighbour recolouring is legal.  The new
colour at `v` remains absent from its neighbourhood because the operated
neighbour changes from an old forbidden colour to the former colour of
`v`.

At the end of the lifted sequence, the neighbours of `v` have their target
colours.  The target colour of `v` is therefore available and gives the
requested endpoint.  This proves the lifting lemma between arbitrary
specified source and target colourings, not merely between their
restrictions.

Deleting degree-at-most-three vertices until none remain either empties the
graph or leaves its induced four-core.  `K_5`-minor exclusion is inherited
by induced subgraphs.  With at most eight vertices a nonempty four-core has
order between five and eight, so checking exactly those minimum-degree-four
graphs and lifting the deleted vertices in reverse order is exhaustive.

## 2. Completeness of the finite core search

For each order from five through eight, `geng -q -d4 n` generates one
representative of every unlabelled simple graph of that order and minimum
degree at least four.  The observed stream sizes are respectively

```text
1, 4, 29, 424.
```

The verifier's `partitions` generator is a restricted-growth enumeration
of every set partition of each retained vertex set into five nonempty
blocks.  The outer retained-set loop permits unused vertices, as required
for a minor model.  Connectivity is checked in the induced subgraph on
each block, and every pair of blocks is required to have a host edge.
These conditions are exactly the branch-set definition of a `K_5` minor;
there is neither a clique-subgraph shortcut nor a hidden spanning
assumption.

The minor test leaves exactly the following six cores:

```text
order  graph6    edges  proper labelled five-colourings
6      E]~o      12       780
7      FUZ~o     15      1800
8      GEhf~w    18      4980
8      GQyurg    16      6120
8      GQyurw    17      4440
8      GQyuzw    18      3480
```

As an independent spot check, a separate dependency-free C++ program used
bit-mask branch sets, a separately written direct colouring recursion, and
integer-state breadth-first search.  It reproduced all six rows and found
one full reconfiguration component in each.  It also independently found
one component on 35,060 states for `K_{2,6}` and one component on 18,000
states for ``I_2 join (2K_2 disjoint union 2K_1)``.

## 3. Colouring and adjacency enumeration

The graph6 reader supplied by NetworkX labels the vertices consecutively,
which agrees with the tuple positions used by `proper_colourings`.
Vertices are assigned in nonincreasing degree order.  At each step the
recursion excludes exactly the colours already assigned to neighbours;
every proper labelled five-colouring occurs once.

For every state and every vertex, `component_sizes` tries every colour not
currently used by a neighbour and different from the present colour.  In
the full graph this is precisely one-vertex adjacency in `R_5(H)`.  In the
surjective run, membership in the prefiltered state set admits exactly
those moves that remain surjective.  Breadth-first search therefore gives
the exact component sizes.

Running the pinned verifier produced

```text
PASS full_R5_connected_for_every_K5_minor_free_graph_of_order_at_most_8
```

and all displayed core and static-example counts.  The surjective counts
for the two static examples also agree with their existing independently
audited invariants: colour transfer between the two join sides is blocked
when all five colours must remain in use.  These surjective calculations
are sharpness checks and are not used to prove the full reconfiguration
theorem.

## 4. Host-level shortest-path consequence

After fixing colour six exactly on the independent set `I`, a boundary
colouring is exactly a proper colouring of `H=G[B-I]` with the other five
labelled colours; unused colours are allowed.  Thus the two nonempty shore
extension sets are subsets of `R_5(H)`.  They are disjoint under the stated
no-common-extension hypothesis.  Connectivity supplies a shortest path
between them.

If that path has at least two edges, any internal state extending either
shore would shorten the path from one endpoint set to the other.  Hence
every internal state is rejected by both.  Extension failure is equivalent
to failure of the list assignment left on the corresponding open shore.
A vertex-minimal non-list-colourable induced subgraph is connected, because
otherwise one of its components is already non-list-colourable.  This
proves outcome 2.

If the path has one edge, its endpoints differ only at a literal boundary
vertex `x`, from `alpha` to `beta`.  Properness at both endpoints says that
`x` has no boundary neighbour of either colour.  Thus `x` is a singleton
component of the boundary `alpha`--`beta` graph.

Take an extension of the first endpoint through its shore.  If the full
two-colour component containing `x` met no other boundary two-colour
component, it would meet the boundary only in `x`; swapping it would
extend the other endpoint through the same shore, contradicting the
disjointness of the two extension sets.  It must therefore meet a second
boundary component.  A shortest subpath from `x` to its first further
boundary vertex has all internal vertices in that open shore.  Reversing
the roles of the shores and endpoints gives the second path.  Their
interiors are disjoint because the open shores are disjoint and
anticomplete.  No alignment of their remote boundary endpoints is proved
or used.

The phrase “endpoint minimality” in the source is stronger than needed in
this one-edge argument; disjointness of the extension sets suffices.  It
does not create a gap.

## 5. Trust boundary

The result is finite and computer-assisted.  It proves connectivity of the
full five-colouring reconfiguration graph only through order eight.  Paths
may and in the two static examples necessarily do pass through
non-surjective colourings.  The theorem does not preserve which shore owns
an intermediate boundary trace, synchronize the two remote endpoints in
the one-step outcome, inherit prior minor-model labels, give a `K_7` minor,
or return a compatible exact order-seven separation.

The host corollary requires all of its stated inputs separately: connected
boundary-full open shores, the exact independent block, nonempty extension
sets on both sides, `K_5`-minor exclusion for `H`, and absence of a common
exact boundary extension.  None of those host properties is inferred from
the finite census.
