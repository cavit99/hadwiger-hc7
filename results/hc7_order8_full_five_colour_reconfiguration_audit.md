# Independent audit of the four-or-five-colour reconfiguration theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete strengthened source
[`hc7_order8_full_five_colour_reconfiguration.md`](hc7_order8_full_five_colour_reconfiguration.md)
at SHA-256

```text
ca51586f29412fc8f861ad8bb22c79cecf2f2c063060bc1d20e5d6b0459c0d71
```

and the deterministic verifier
[`hc7_order8_full_five_colour_reconfiguration_verify.py`](hc7_order8_full_five_colour_reconfiguration_verify.py)
at SHA-256

```text
3d30726bde4ebcecac8692eb2ba6818d61679a18978301bbd4d3df0abd3e2967
```

The palette-preserving low-degree lift, order-four base, reduction to the
six minimum-degree-four cores, strengthened finite census, full
reconfiguration corollary, and the explicitly conditional two-shore
consequence are correct.  The host consequence now includes the necessary
hypothesis that both shore-extension languages meet the four-or-five-colour
state graph; this condition is not inferred from mere nonemptiness.

## 1. Palette-preserving low-degree lifting

Let `v` have degree at most three and let a proper five-colouring of `H`
use at least four colours.  Its restriction to `H-v` uses either at least
four colours or exactly three.  In the latter case the colour on `v` is a
fourth colour.  Since `|H-v|>=4`, a restriction colour class contains at
least two vertices.  Recolouring one member with the globally absent fifth
colour is legal, leaves the old class nonempty, and makes the restriction
use four colours.  This normalization stays in `R_5^{>=4}(H)` and is
reversible at the target.

During the lift of a path in `R_5^{>=4}(H-v)`, the only possible conflict
is that a neighbour of `v` is about to receive the current colour of `v`.
At most three colours occur on `N_H(v)`, so at least two colours are
available at `v`.  If the current whole colouring uses four colours, the
globally absent fifth colour is available and replacing the colour on `v`
cannot lower the palette.  If it uses all five colours, changing `v` can
remove at most its old colour and therefore leaves at least four.  After
this temporary move the proposed neighbour recolouring is legal.  At the
end, the restriction already uses at least four colours, so restoring the
target colour at `v` is also safe.

For four vertices, the relevant states are the injections into five
colours.  The one unused colour gives the standard spare-symbol exchanges,
so the base graph is connected.  Repeated deletion of degree-at-most-three
vertices therefore reduces every graph in the theorem either to this base
or to a nonempty induced four-core of order five through eight.

## 2. Completeness of the finite core census

For each order from five through eight, `geng -q -d4 n` produces one
representative of every unlabelled simple graph of that order and minimum
degree at least four.  The streams have orders

```text
1, 4, 29, 424.
```

The verifier's branch-set routine enumerates every retained vertex subset
and every partition of it into five nonempty blocks.  It checks induced
connectivity inside every block and an edge between every two blocks.
These are exactly the conditions for a `K_5`-minor model; unused vertices
are allowed, so there is no hidden spanning assumption.

Exactly six graphs survive the minor test.  Direct enumeration of their
proper labelled five-colourings gives one component in
`R_5^{>=4}` of the following orders:

```text
graph6    edges   |R_5|   |R_5^{>=4}|
E]~o       12       780       720
FUZ~o      15      1800      1800
GEhf~w     18      4980      4920
GQyurg     16      6120      6120
GQyurw     17      4440      4440
GQyuzw     18      3480      3480
```

For each retained state and vertex, the breadth-first search tries exactly
the colours absent from its neighbourhood and retains the resulting state
only when it still uses at least four colours.  It therefore computes the
claimed induced reconfiguration graph rather than the unrestricted graph.

Running the pinned verifier reproduced all displayed data and ended with

```text
PASS R5_ge4_connected_for_every_K5_minor_free_graph_of_order_4_through_8
```

It also reproduced the two sharpness checks:

```text
graph6    |R_5|   |R_5^{>=4}|   components of R_5^sur
G??F~w     35060     33120       20*540 + 5*1560
G?`F~w     18000     17520       20*276 + 5*1104.
```

## 3. The unrestricted reconfiguration corollary

Take any proper five-colouring using at most three colours.  Because the
graph has at least four vertices, some colour class is repeated.  Moving
one member of that class to a globally unused colour is proper, keeps the
old class nonempty, and increases the palette by one.  Iteration reaches
`R_5^{>=4}`.  Since that induced subgraph is connected, every state of the
full reconfiguration graph lies in its single component.  Thus the stated
full-`R_5` corollary follows without an additional census.

## 4. Conditional host consequence

Fixing colour six exactly on an independent boundary set `I` identifies
the exact boundary colourings with the proper labelled five-colourings of
`H=G[B-I]`.  A trace extending through both closed shores would glue to a
six-colouring, so the two extension languages are disjoint.

The strengthened source separately assumes that **each** extension
language contains a trace whose restriction to `H` uses at least four
colours.  This hypothesis is essential: nonempty extension languages alone
do not imply it, and boundary palette completion need not preserve a shore
extension.  Under the stated hypothesis, connectivity supplies a shortest
path inside `R_5^{>=4}` between the two extension languages.

If the path has at least two edges, an internal trace extending either
shore would shorten it, so every internal trace is rejected by both shores.
The usual list-colouring correspondence then gives one connected
vertex-minimal list obstruction in each open shore.

If the path has one edge, its endpoints differ only at a literal boundary
vertex `x`.  Properness at both endpoints makes `{x}` a component of the
corresponding boundary two-colour graph.  In an extension through either
shore, its full two-colour component must meet another boundary component;
otherwise switching it would make the opposite endpoint extend through
the same shore.  A shortest first-hit subpath has nonempty interior in that
open shore.  Reversing the endpoints gives the path in the other shore,
and their interiors are disjoint because the open shores are disjoint.

In the maximum-palette residual, every surjective trace extends through
exactly one shore.  Hence no internal trace rejected by both shores can use
five colours.  The selected path never uses fewer than four, so every such
internal trace uses exactly four colours.  The fifth available colour is
absent from the complete boundary and belongs to every list in both shore
obstructions.  This is palette information only; it does not identify a
minor-model branch set.

## 5. Trust boundary

The theorem is a finite computer-assisted statement for graphs of order
four through eight.  It does not make the surjective reconfiguration graph
connected, determine which shore owns an intermediate trace, or imply that
either shore-extension language contains a four-or-five-colour trace.

The two-shore corollary must therefore retain the explicit endpoint
hypothesis or the alternative that one shore attains at most three colours
on `H`.  Even in the four-colour paired-rejection outcome, the common
unused colour does not give an explicit `K_7`-minor model, compatible
order-seven shore colourings, or a strict state-preserving descent.
