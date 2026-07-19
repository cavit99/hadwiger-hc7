# Independent audit of the two-mark list-excess barrier

**Verdict:** GREEN at the exact source revision below.

**Audited source:** `hc7_two_mark_list_excess_barrier.md`, SHA-256

```text
4e612b07e9ec84492c779c90b7c5d0f896be159ddd7fc0e84b1bd250ab34824a
```

This is a separate internal mathematical audit, not external peer review.

For the odd wheel with rim `C_{2m+1}`, the uniform three-colour lists make
the graph uncolourable.  Deleting the hub leaves a three-colourable odd
cycle; deleting a rim vertex leaves a universal hub over a bipartite path,
which is also three-colourable.  Hence every proper induced subgraph is
list-colourable.  Giving two rim vertices colours four and five, colouring
the remaining rim paths with one and two, and giving the hub colour three
is proper and has exactly the two claimed exceptions.  Only the hub has
positive excess, namely `2m+1-3=2m-2`.

The six-boundary-colour variant is also correct.  With adjacent forced rim
vertices carrying singleton lists `{1}` and `{2}`, deletion of an ordinary
rim vertex leaves a two-colourable path with the required orientation;
deletion of either forced vertex allows the hub to take its missing forced
colour; and deletion of the hub leaves an odd cycle which can use colour
three once on the long arc.  Its two-exception colouring is proper and the
excess is `(2m-2)+2+2=2m+2`.  The stated boundary contacts exclude exactly
the complementary colours from each list.  This variant is used only to
refute a bound based on the number of boundary colours; it is not claimed
to preserve seven-connectivity.

The exact-seven realization is also correct.  The three boundary colours
four, five and six make every forbidden list exactly `{1,2,3}`; after
deleting `xp,yq`, those are the only monochromatic crossing edges.  Deleting
at most six vertices from the host leaves a boundary vertex.  If a wheel
vertex remains, the complete boundary-wheel join connects the graph; if
the entire six-vertex smallest wheel is deleted, the opposite vertex and
the boundary remain connected.  Thus the host is seven-connected, with
connectivity exactly seven because the opposite vertex has degree seven.

Finally, six disjoint boundary-wheel edges and the unused seventh boundary
vertex form an explicit `K_7`-minor model.  The example therefore refutes
only a bound deduced from the two exceptions, local list-criticality and
even seven-connectivity.  It does not refute a statement that also assumes
`K_7`-minor exclusion or contraction-criticality.
