# Independent audit: boundary list-criticality and complementary transfer

**Verdict:** GREEN.

**Audited source:** `results/hc7_boundary_list_critical_transfer.md`

**SHA-256:**

```text
4e38af17e211f2f384dee804e55092b98512483eac4a897353eb5cbc3954b8f1
```

This is a separate internal mathematical audit, not external peer review.

## 1. Boundary lists and the minimal kernel

The list assignment excludes exactly the colours on literal boundary
neighbours, so list-colourability of the open shore is equivalent to
extension of the fixed boundary trace.  A vertex-minimal induced
uncolourable subgraph is connected.  Its edge-minimal spanning
uncolourable subgraph has every proper subgraph list-colourable, using
vertex minimality for deleted vertices and edge minimality for deleted
edges.  Colouring `K-u` proves `d_K(u)>=|L_c(u)|`, including when a list is
empty.

## 2. Degree identity and tight vertices

Because `K` is induced and the two shores are anticomplete, its internal
degree, neighbours in `D-K`, and boundary neighbours are disjoint.  With
`|L_c(u)|=6-f(u)`, the displayed calculation gives exactly

\[
d_G(u)=6+\varepsilon(u)+\rho(u)+\sigma(u).
\]

For a block of the tight-vertex graph, colour the rest of `K` and remove
the colours used outside the block.  Every residual list has order at least
the block degree.  The degree-choosability theorem therefore colours the
block unless it is complete or an odd cycle; such a colouring would extend
to `K`.  The Gallai-forest conclusion is valid.

## 3. Fixed-trace Kempe alternatives

Deleting an edge of the edge-minimal obstruction gives equal endpoint
colours.  After adjoining the fixed boundary colouring, a two-colour
component avoiding the boundary has no boundary neighbour in either
swapped colour; otherwise that neighbour would belong to the same
component.  Its interchange therefore preserves every list.  If the two
endpoint components are distinct, both must meet the boundary, or this
swap would separate the endpoint colours and permit restoration of the
edge.  Shortest first-hit paths are internally in `K`, disjoint, and have
distinct boundary ends.

The source correctly distinguishes this local fixed-trace colouring from a
colouring of the whole host.

## 4. Whole-host saturation

A colouring after contracting an edge expands to a colouring of its
deletion with equal endpoint colours.  For every alternate colour the
endpoints lie in one full two-colour component; otherwise a component swap
would separate them and restore the edge.  No fixed boundary trace is
claimed.

## 5. Strict complementary transfer

Every component of `D-K` has neighbourhood in `X union K` and that
neighbourhood separates it from the other shore, so its order is at least
seven.  Colour the proper minor obtained by deleting all of `D-K`.  If the
resulting trace extended through every deleted component, the extensions
would glue because those components are pairwise anticomplete and agree on
their literal neighbourhoods.  Hence one component rejects the trace and
is strictly smaller than `D`.

If its neighbourhood has order seven, it is an actual separation.  Every
component behind that boundary is full: otherwise its own neighbourhood
would have order at most six and separate it from another component.

## 6. Shore-filling endpoint

When `K=D`, vertex minimality gives, for every `u`, a colouring of `G-u`
with the same fixed boundary trace.  Every colour occurs in `N_G(u)`, or
the missing colour could be assigned to `u`.  If order-seven separations
are excluded, a degree-seven vertex is impossible because its neighbourhood
would isolate it from the nonempty opposite shore.  Thus the degree
identity gives `epsilon(u)+rho(u)>=2`; a tight vertex has at least two
repeated boundary-colour incidences.

## 7. Trust boundary

The strict transfer can enlarge or otherwise change the boundary and
preserves neither the original equality partition nor inherited
minor-model labels.  It is not an order-eight induction without an
additional boundary-control theorem.  The fixed-trace and whole-host
colouring families are not identified.

No mathematical defect was found.
