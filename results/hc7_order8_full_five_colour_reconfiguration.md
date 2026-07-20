# Four-or-five-colour reconfiguration on the eight-vertex residual

**Status:** strengthened written computer-assisted theorem; separate
internal audit GREEN in
[`hc7_order8_full_five_colour_reconfiguration_audit.md`](hc7_order8_full_five_colour_reconfiguration_audit.md).

## Definitions

For a graph `H`, let `R_5(H)` be the graph whose vertices are all proper
colourings `V(H) -> {1,2,3,4,5}`.  Two colourings are adjacent when they
differ at exactly one vertex.  Colours may be unused.

Let `R_5^sur(H)` be the subgraph induced by the colourings that use all five
colours.  This is different from the graph whose moves are Kempe changes.

Let `R_5^{>=4}(H)` be the subgraph induced by the proper colourings which
use at least four of the five colours.

## Theorem

> **Order-eight four-or-five-colour reconfiguration theorem.**  If `H` is
> a `K_5`-minor-free graph with `4<=|H|<=8`, then `R_5^{>=4}(H)` is
> connected.

In particular `R_5(H)` is connected.  Indeed, from any colouring using at
most three colours, some colour class is repeated because `|H|>=4`.
Recolour one vertex of that class with a globally unused colour.  This is
proper, the old class remains nonempty, and the number of used colours
increases by one.  Repeating reaches `R_5^{>=4}(H)`.  The restriction to
order at least four only avoids calling the empty induced state graph
connected; it is automatic in the live eight-vertex application.

In particular, the theorem applies to the live residual in which `H` has
eight vertices and is known separately to be four-colourable.  The
four-colourability hypothesis is not needed for this finite theorem.

## Palette-preserving low-degree lifting lemma

Suppose `|H|>=5`, `v` has degree at most three, and
`R_5^{>=4}(H-v)` is connected.  Then `R_5^{>=4}(H)` is connected.

First normalize an endpoint colouring `c` if its restriction to `H-v` uses
only three colours.  The colour of `v` is then a fourth colour.  Since
`|H-v|>=4`, one of the three restriction classes contains at least two
vertices.  Recolour one vertex of that class with the fifth colour, which
is absent from all of `H`.  This is proper, the old class remains nonempty,
and the restriction now uses four colours.  The move can be reversed after
the lifted sequence reaches the similarly normalized target.

Now take a path in `R_5^{>=4}(H-v)` between the two normalized
restrictions and lift it one move at a time.  If the next move recolours a
neighbour of `v` with the current colour of `v`, first recolour `v`.  At
most three colours occur in `N_H(v)`, so at least two colours are available
at `v`.  If the current colouring of `H` uses four colours, choose the
globally unused fifth colour; otherwise losing the old colour still leaves
at least four.  Thus this temporary move never leaves
`R_5^{>=4}(H)`.  The intended move in `H-v` is then legal.  At the end,
the restriction already uses at least four colours, so restoring the target
colour of `v` also preserves the threshold.  Reversing the endpoint
normalizations completes the lift.

For order four, every state under consideration is an injection from the
four vertices to the five colours.  Recolouring one vertex with the unique
spare colour implements the usual spare-symbol exchanges, so these states
form one connected graph.  This is the base case.

Repeatedly applying the lemma reduces the theorem either to its order-four
base or to a nonempty 4-core.  Such a core is an induced
`K_5`-minor-free graph of minimum degree at least four and order between
five and eight.

## Exact finite verification of the cores

The verifier uses `geng -q -d4 n` for `5 <= n <= 8`.  For every graph it
checks `K_5`-minor exclusion directly by enumerating five disjoint nonempty
connected, pairwise adjacent branch sets.  It then enumerates every labelled
proper five-colouring and every legal one-vertex recolouring.

There are exactly six `K_5`-minor-free graphs of minimum degree at least four
in this range:

```text
order  graph6    edges  |R_5(H)|  |R_5^{>=4}(H)|
6      E]~o      12       780          720
7      FUZ~o     15      1800         1800
8      GEhf~w    18      4980         4920
8      GQyurg    16      6120         6120
8      GQyurw    17      4440         4440
8      GQyuzw    18      3480         3480
```

The exact search finds one component in `R_5^{>=4}(H)` in every row.
Together with the palette-preserving low-degree lifting
lemma and the order-four base, this proves the theorem for every
`K_5`-minor-free graph of order four through eight, not merely the six
displayed cores.

Run:

```sh
python3 results/hc7_order8_full_five_colour_reconfiguration_verify.py
```

The verifier requires NetworkX and the `geng` executable from nauty on
`PATH`.

The final line is:

```text
PASS R5_ge4_connected_for_every_K5_minor_free_graph_of_order_4_through_8
```

## The surjective subgraph is not connected in general

The corresponding statement for `R_5^sur(H)` is false, even for the
eight-vertex graph `K_{2,6}` (graph6 `G??F~w`).  In a surjective proper
five-colouring of `K_{2,6}`, the palettes on the two bipartition classes are
disjoint.  A one-vertex recolouring that remains surjective cannot transfer
a colour from one side to the other.  Consequently, the number of colours
used on the two-vertex side is invariant and may be either one or two.

The verifier finds 25 components in `R_5^sur(K_{2,6})`: twenty of order 540
and five of order 1560.  Nevertheless, `R_5^{>=4}(K_{2,6})` is connected
on 33,120 vertices (and its full graph is connected on 35,060 vertices).

The same distinction survives in the closer static boundary graph

```text
I_2 join (2K_2 disjoint union 2K_1),
```

whose graph6 code is ``G?`F~w``.  Its four-or-five-colour reconfiguration
graph is connected on 17,520 colourings (and its full graph on 18,000),
whereas its surjective induced subgraph has twenty components of order 276
and five of order 1104.

Thus the theorem supplies a path between any two surjective endpoint
colourings which never uses fewer than four colours.  In the live two-shore
application, the ownership/orientation of a four-colour intermediate trace
is not currently controlled.

## Host-level consequence: a one-vertex transition

The finite theorem does sharpen the existing two-shore Kempe transition in
the order-eight residual.  Use the following setting.  Let

```text
V(G) = A disjoint-union B disjoint-union D,
E_G(A,D) = empty,
```

where the open shores `A,D` are connected and full to `B`.  Fix a nonempty
independent set `I subset B`, assume that both closed shores have a proper
six-colouring in which `I` is exactly colour six on `B`, and put
`H=G[B-I]`.  Assume `|H|<=8`, `H` has no `K_5` minor, and no exact boundary
colouring extends through both shores.  For the strengthened conclusion
below, assume additionally that each shore-extension set contains an exact
boundary colouring whose restriction to `H` uses at least four colours.

Boundary colourings exact at `I` correspond to the vertices of `R_5(H)`.
The two shore-extension sets are nonempty and disjoint.  Choose a shortest
path in `R_5^{>=4}(H)` from one set to the other, with endpoints also
minimized over those sets.  Exactly one of the following occurs.

1. The path has one edge.  It recolours one literal vertex `x` from colour
   `alpha` to colour `beta`.  In each open shore there is an
   `alpha`--`beta` path from `x` to a different boundary component of those
   two colours, with all internal vertices in that shore.  The two path
   interiors are disjoint.
2. The path has at least two edges.  Every internal boundary colouring is
   rejected by both shores and therefore gives one connected
   vertex-minimal list-colouring obstruction in each open shore.

For outcome 1, legality of the one-vertex recolouring says that `x` has no
boundary neighbour of colour `beta`; properness says that it has no
boundary neighbour of colour `alpha`.  Thus `{x}` is a whole component of
the boundary two-colour graph.  If the full two-colour component containing
`x` in an extension through the first shore met no other boundary
two-colour component, swapping that full component would extend the other
endpoint through the same shore, contrary to endpoint minimality.  A
shortest route to the next boundary component has interior in the open
shore.  The symmetric argument applies to the other shore.  Outcome 2 is
the usual minimal rejected-list-subgraph argument.

Unlike the unbounded Las Vergnas--Meyniel Kempe-equivalence input, this
order-eight result makes the operated boundary component in the one-step
outcome a single literal vertex.  It still does not align the two remote
ends of the resulting shore paths or by itself construct a `K_7`-minor
model.

In the live maximum-palette residual, every surjective exact colouring
extends through exactly one shore.  Subject to the additional endpoint
hypothesis in the preceding paragraph, outcome 2 has an extra consequence:
each internal colouring rejected by both shores is non-surjective on `H`.
The strengthened theorem keeps the whole path at four or five colours, so
every such internal colouring uses **exactly four** of the five available
colours.  Its two shore list assignments therefore share one common colour
absent from the literal boundary.  This is a sharper input to the paired
list-critical branch, but it does not by itself colour either shore or
align their lists.

## Trust boundary

This is a computer-assisted finite theorem about graphs of order four
through eight.  It is not an unbounded recolouring theorem.  It does not
prove that `R_5^sur(H)` is connected, preserve which shore extends a
boundary colouring, or show that a four-colour intermediate colouring
extends to either closed shore.  The common unused colour in the resulting
paired list-critical kernels is palette data, not a minor-model label.
Nor does the finite theorem force each shore-extension language to meet
`R_5^{>=4}(H)`; a live application must prove that endpoint condition or
retain the alternative that one shore attains at most three colours on
`H`.
