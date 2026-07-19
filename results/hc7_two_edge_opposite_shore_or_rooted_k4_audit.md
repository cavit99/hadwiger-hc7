# Independent audit: two-edge opposite-shore placement or rooted `K_4`

**Verdict:** **GREEN**, with the redundancy/scope qualification in Section 6.

**Audited source:**
[`hc7_two_edge_opposite_shore_or_rooted_k4.md`](hc7_two_edge_opposite_shore_or_rooted_k4.md)

**Source SHA-256:**

```text
acedd318665d68c1d03ef0efd463db2897dc3e6d131f1da8f112d74094308e15
```

The change from the initially checked source is limited to the opening
status line recording this GREEN audit; the mathematics is unchanged.

This is a separate internal mathematical audit.  It checks the complete
source: the chromatic signatures, the connectivity estimates, the literal
separator lifts, both uses of linkage theory, the three-edge probe, and the
stated label-preservation limitation.  It is not external peer review.

## 1. Exact two-edge response and chromatic number

The two marked edges form a matching.  For each nonempty subset of that
matching, contracting precisely the selected edges gives a proper minor of
`G`, hence a graph with a proper six-colouring.  Expanding the contracted
vertices makes precisely the selected endpoint pairs monochromatic.  Every
unselected marked edge remains an edge with two distinct ends, so its pair
is bichromatic.  This gives exactly the three asserted signatures.  An
all-bichromatic signature would remain proper after restoring both edges
and would six-colour `G`, so it is absent.

The common deletion `H` is a proper minor and is therefore six-colourable.
If it had a four-colouring, recolouring one end of `e` with a fresh fifth
colour and one end of `f` with a distinct fresh sixth colour would preserve
all old edges and repair both deleted edges.  The ends are distinct because
the marked edges form a matching; a possible edge between the two recoloured
vertices is proper because the fresh colours differ.  This would six-colour
`G`.  Thus

```text
5 <= chi(H) <= 6.
```

The proof correctly does not claim `chi(H)=6` for two arbitrary independent
edges.  Equality is available in the stronger opposite-open-shore setting,
but that hypothesis is absent here.

## 2. Connectivity after deleting the matching

For a separation of `H` with boundary `T` and two nonempty open sides,
seven-connectivity gives seven internally vertex-disjoint paths in `G`
between fixed vertices on opposite sides.  Every such path either meets
`T` or uses a deleted edge crossing the two sides.  At most `|T|` paths can
use distinct boundary vertices, and the matching property permits at most
one further internally disjoint path per crossing deleted edge.  Therefore

```text
|T| + number of crossing marked edges >= 7.
```

There are only two marked edges, so `kappa(H)>=5`.  This is exactly the
two-edge instance of the separately audited matching-deletion separator
budget.  The argument also covers adjacent choices of the two Menger
terminals.

## 3. The order-five lift and exact edge placement

If `kappa(H)=5`, any order-five separation attains equality in the preceding
budget.  Both marked edges therefore cross its open sides.  After orienting

```text
a,c in L,   b,d in R,
```

the set `T union {b,c}` has order seven and meets both restored crossing
edges.  No edge remains between `L-{c}` and `R-{b}`: every unmarked such edge
would already contradict the separation in `H`, while each marked edge has
one selected end.  The residual sides are nonempty because they contain
`a` and `d`, respectively.

In the resulting two closed shores, `e=ab` occurs only on the left and
`f=cd` occurs only on the right.  Thus the claimed actual order-seven
separation and opposite placement are literal and require no quotient
interpretation.

## 4. The rooted four-terminal model

If `kappa(H)>=6`, Jung's theorem makes `H` two-linked.  It consequently
supplies a linkage for each of the three pairings of the four distinct
roots `a,b,c,d`.  Fabila-Monroy--Wood, Theorem 8, applies because `H` is
three-connected and converts those three linkages into a `K_4`-minor model
rooted at the four nominated vertices.

The strengthening in Remark 2.2 is also correct.  Since `chi(H)>=5`, the
Four Colour Theorem makes `H` nonplanar; since `kappa(H)>=5`, it is
four-connected.  Jung's four-connected nonplanar theorem therefore makes
`H` two-linked even when `kappa(H)=5`, and the same rooted-`K_4`
characterization applies.

## 5. The third-edge probe

With a third vertex-disjoint marked edge, the three edges are a matching.
Contracting each nonempty subset gives all seven exact signatures other
than the all-bichromatic signature; the latter would six-colour `G`.
The matching-deletion separator budget gives `kappa(J)>=4`.

At an order-four separation, equality forces all three marked edges to
cross.  Select the end of `e` on one open side, the end of `f` on the other,
and either end of `h`.  The three selected ends together with the four
boundary vertices hit every restored crossing edge.  The unselected ends
of `e` and `f` remain in opposite open sides, so neither side is erased.
The lifted boundary has order seven and places `e,f` in opposite closed
shores exactly as asserted.

## 6. Redundancy and trust boundary

The theorem is valid, but its rooted-model branch is not a new consequence
of the response-signature cube.  The already audited theorem
[`hc7_atomic_two_named_edge_disjoint_cycles.md`](../results/hc7_atomic_two_named_edge_disjoint_cycles.md)
proves more generally that, for any two vertex-disjoint edges in a
seven-connected graph, their common deletion is four-connected and
nonplanar and hence contains a `K_4` minor rooted at their four ends.
Accordingly, outcome 2 of Theorem 2.1 always holds under the present
hypotheses.  The value of the `kappa(H)=5` branch is the additional literal
opposite-shore placement, not an exclusive alternative to the rooted model.

Nothing in the proof makes the four rooted branch sets avoid or respect
the inherited five labelled completing branch sets.  The Section 4
absorption statement is explicitly identified as unproved, and the source
does not use it as a conclusion.  Likewise, the separator lift does not
produce a common boundary-colouring partition.  The note therefore does
not close the concentrated three-owner branch or prove `HC_7`.
