# Full five-colouring reconfiguration on the eight-vertex residual

**Status:** written computer-assisted theorem; separate internal audit GREEN
in
[`hc7_order8_full_five_colour_reconfiguration_audit.md`](hc7_order8_full_five_colour_reconfiguration_audit.md).

## Definitions

For a graph `H`, let `R_5(H)` be the graph whose vertices are all proper
colourings `V(H) -> {1,2,3,4,5}`.  Two colourings are adjacent when they
differ at exactly one vertex.  Colours may be unused.

Let `R_5^sur(H)` be the subgraph induced by the colourings that use all five
colours.  This is different from the graph whose moves are Kempe changes.

## Theorem

> **Order-eight full reconfiguration theorem.**  If `H` is a
> `K_5`-minor-free graph with at most eight vertices, then `R_5(H)` is
> connected.

In particular, the theorem applies to the live residual in which `H` has
eight vertices and is known separately to be four-colourable.  The
four-colourability hypothesis is not needed for this finite theorem.

## Low-degree lifting lemma

Suppose that `v` has degree at most three and that `R_5(H-v)` is connected.
Then `R_5(H)` is connected.

To see this, take a recolouring sequence in `H-v` and lift it one move at a
time.  If its next move recolours a neighbour of `v` with the current colour
of `v`, first recolour `v`.  At most three colours occur in `N_H(v)`, so at
least two of the five colours are available at `v`; one is its current
colour and there is another.  The intended move in `H-v` is then legal in
`H`.  At the end, recolour `v` to its colour in the target colouring.  This
lifts a path between any two prescribed colourings of `H`.

Repeatedly applying the lemma reduces the theorem to the nonempty 4-core of
`H`.  Such a core is an induced `K_5`-minor-free graph of minimum degree at
least four and order between five and eight.

## Exact finite verification of the cores

The verifier uses `geng -q -d4 n` for `5 <= n <= 8`.  For every graph it
checks `K_5`-minor exclusion directly by enumerating five disjoint nonempty
connected, pairwise adjacent branch sets.  It then enumerates every labelled
proper five-colouring and every legal one-vertex recolouring.

There are exactly six `K_5`-minor-free graphs of minimum degree at least four
in this range:

```text
order  graph6    edges  |R_5(H)|
6      E]~o      12       780
7      FUZ~o     15      1800
8      GEhf~w    18      4980
8      GQyurg    16      6120
8      GQyurw    17      4440
8      GQyuzw    18      3480
```

The exact search finds one component in `R_5(H)` in every row.  Together
with the low-degree lifting lemma, this proves the theorem for every graph
of order at most eight, not merely the six displayed cores.

Run:

```sh
python3 results/hc7_order8_full_five_colour_reconfiguration_verify.py
```

The verifier requires NetworkX and the `geng` executable from nauty on
`PATH`.

The final line is:

```text
PASS full_R5_connected_for_every_K5_minor_free_graph_of_order_at_most_8
```

## The surjective subgraph is not connected in general

The corresponding statement for `R_5^sur(H)` is false, even for the
eight-vertex graph `K_{2,6}` (graph6 `G??F~w`).  In a surjective proper
five-colouring of `K_{2,6}`, the palettes on the two bipartition classes are
disjoint.  A one-vertex recolouring that remains surjective cannot transfer
a colour from one side to the other.  Consequently, the number of colours
used on the two-vertex side is invariant and may be either one or two.

The verifier finds 25 components in `R_5^sur(K_{2,6})`: twenty of order 540
and five of order 1560.  Nevertheless, its full graph `R_5(K_{2,6})` is
connected, with 35,060 vertices.

The same distinction survives in the closer static boundary graph

```text
I_2 join (2K_2 disjoint union 2K_1),
```

whose graph6 code is ``G?`F~w``.  Its full reconfiguration graph is connected
on 18,000 colourings, whereas its surjective induced subgraph has twenty
components of order 276 and five of order 1104.

Thus the theorem supplies a path between any two surjective endpoint
colourings, but that path may pass through a colouring using at most four
colours.  In the live two-shore application, the ownership/orientation of
such a non-surjective intermediate trace is not currently controlled.

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
colouring extends through both shores.

Boundary colourings exact at `I` correspond to the vertices of `R_5(H)`.
The two shore-extension sets are nonempty and disjoint.  Choose a shortest
path in `R_5(H)` from one set to the other, with endpoints also minimized
over those sets.  Exactly one of the following occurs.

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
extends through exactly one shore.  Therefore outcome 2 has an extra
consequence there: each internal colouring rejected by both shores is
non-surjective on `H`, and hence uses at most four of the five available
colours.  This is a sharper input to the paired list-critical branch, but it
does not by itself colour either shore or align their lists.

## Trust boundary

This is a computer-assisted finite theorem about graphs of order at most
eight.  It is not an unbounded recolouring theorem.  It does not prove that
`R_5^sur(H)` is connected, preserve which shore extends a boundary
colouring, or show that a non-surjective intermediate colouring extends to
either closed shore.
