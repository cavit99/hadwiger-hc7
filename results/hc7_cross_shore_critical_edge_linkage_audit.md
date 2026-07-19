# Independent audit: opposite-shore critical-edge linkage

**Verdict:** **GREEN.**

**Audited source:**
[`hc7_cross_shore_critical_edge_linkage.md`](hc7_cross_shore_critical_edge_linkage.md)

**Source SHA-256:**

```text
05314416338b3fe7128a4fbe88a28e084cee258d1d64f895f22334f078356872
```

This revision includes Proposition 5.1, independently checked after the
earlier theorem audit.  Two independent checks were performed at
`2183bc36...`; the current hash differs only by their recommended
palette-invariant wording clarification ("the same equality partition"
followed by a colour permutation).

This is a separate internal mathematical audit, not external peer review.
It covers Lemma 2.1, Theorem 3.1, Corollary 4.1, Theorem 4.2, the
fixed-trace application and mixed-response lift in Section 5, and the stated
trust boundary.

Two defects found in earlier drafts were repaired before this verdict:

1. simultaneous contraction of two incident marked edges is now asserted
   only when the edge between their two outer ends is absent; and
2. Section 5 now assumes the common **fixed-equality** trace, rather than
   inferring endpoint equality from mere extendability of the boundary
   partition.

## 1. Two-edge chromatic compression

Let `h=ab` and `e=cd` lie in the two anticomplete open shores.  The four
ends are distinct, and the common edge deletion `H=G-{h,e}` is a proper
minor, so it is six-colourable.

If `H` had a colouring with at most five colours, assigning one fresh sixth
colour to `a` and `c` would preserve every old edge: `a,c` are nonadjacent,
and the fresh colour occurs nowhere else.  It also repairs both deleted
edges because `b,d` keep old colours.  This would six-colour `G`.  Hence
`chi(H)=6`.

For every nonempty subset of the two-edge matching, simultaneous
contraction gives a proper minor.  On expansion, exactly the contracted
endpoint pairs are equal; the uncontracted marked edge remains a genuine
edge with distinct ends because the marked edges are vertex-disjoint.
Deleting both marked edges therefore gives the three exact signatures.
The missing all-proper signature is exactly a six-colouring of `G`.

## 2. Connectivity after deleting the matching

For a separation of `H` with boundary `T` and nonempty open shores, every
path in `G` between the open shores either meets `T` or uses a marked edge
which crosses the shores.  Seven-connectivity and the local form of
Menger's theorem give seven internally disjoint paths.  At most `|T|` of
them can use boundary vertices, and at most one further path can use each
crossing edge of the deleted matching.  Thus

\[
 |T|+|\{g\in\{h,e\}:g\text{ crosses the open shores}\}|\ge 7.
\]

The second term is at most two, proving `kappa(H)>=5`.  This is precisely
the two-edge specialization of the separately audited matching-deletion
separator theorem cited by the source; it also covers adjacent choices of
the two Menger terminals.

## 3. Six-connectivity gives the rooted four-vertex model

If `H` is six-connected, Jung's theorem gives two disjoint paths for each
of the three pairings of `a,b,c,d`.  Fabila-Monroy--Wood, Theorem 8, says
that in a three-connected graph these three linkages are equivalent to a
`K_4`-minor rooted at the four nominated vertices.  The roots are distinct,
and six-connectivity supplies the required three-connectivity, so the
external theorem applies exactly as stated.

The source cites Jung through Stephens--Ye, *Connectivity for Kite-Linked
Graphs*, Theorem 1.1, and cites the published Fabila-Monroy--Wood theorem by
its correct theorem number.

## 4. The exact five-cut and universal endpoint choice

If `kappa(H)=5`, an order-five separation attains equality in the separator
budget, so both marked edges cross its open shores.  Selecting one endpoint
of each crossing edge and adding them to the five-vertex boundary hits
every edge restored between the residual shores.

The proof that **every** endpoint selection leaves both residual shores
nonempty is correct.  If the two selected endpoints exhausted one shore,
that shore would consist of exactly one endpoint of each marked edge.
Each such vertex has only seven possible neighbours: the other shore
vertex, the five boundary vertices, and its own matching mate.  Minimum
degree seven forces all those edges.  Thus the two shore vertices form a
clique complete to the boundary.

In the exact signature where both marked pairs are equal, the two shore
vertices have distinct colours, their two mates have the corresponding
colours, and the boundary uses neither colour.  Swapping the two colours
on the two shore vertices preserves every incident old edge and makes both
crossing marked edges proper.  No other edge joins the two open shores.
This would colour `G`, a contradiction.  Hence every endpoint selection
gives an actual order-seven separation.  Choosing the endpoint opposite a
desired closed shore also preserves a two-vertex branch set supported by a
marked edge, exactly as claimed.

## 5. Two repeated edges and the joint three-edge fork

Corollary 4.1 is a direct application of Theorem 3.1 to `(h,e)` and
`(h,f)`.  The source correctly makes preservation of the five inherited
labels and of a selected boundary response an additional hypothesis; the
universal endpoint lift alone does not establish either property.

Suppose first that `h,e,f` are a matching and put `J=G-{h,e,f}`.

* A four-colouring of `J` extends to a six-colouring of `G` by giving one
  endpoint of `h` and one endpoint of `e` a common fresh fifth colour and
  one endpoint of `f` a fresh sixth colour.  The first two chosen vertices
  are anticomplete because they lie in opposite shores; the two chosen
  vertices in the second shore use different fresh colours.  Thus
  `chi(J)>=5`, while proper-minor colourability gives `chi(J)<=6`.
* If `chi(J)=5` and one endpoint of `e` were nonadjacent to one endpoint
  of `f`, those two vertices together with either endpoint of `h` would be
  independent.  Recolouring all three with one fresh sixth colour repairs
  all marked edges.  Hence the two endpoint pairs are complete to each
  other, and together with `e,f` induce a `K_4`.
* Contraction of any nonempty subset of the three-edge matching gives all
  seven non-all-proper exact signatures.  The matching-deletion theorem
  gives `kappa(J)>=4`; at equality all three rows cross, and its separately
  audited derangement theorem makes every endpoint selection an actual
  order-seven lift.

Now suppose `e=sw` and `f=st` are incident.  A colouring of `J` with at
most five colours extends by assigning one fresh sixth colour to one end
of `h` and to `s`; those vertices are anticomplete, and changing `s`
repairs both incident marked edges.  Thus `chi(J)=6`.

The exact-signature qualification is necessary and is now correct.  If a
contracted set does not contain both `e,f`, no uncontracted marked edge has
its ends identified.  If it contains both, the only additional possible
edge inside the contracted three-vertex class is the outer edge `wt`.
Consequently simultaneous contraction of both incident edges yields the
claimed exact signature exactly under the stated hypothesis `wt notin
E(G)`.  No matching-deletion connectivity conclusion is asserted for the
incident pair.

## 6. Fixed paired boundary trace

Section 5 now assumes explicitly a proper six-colouring of the opposite
closed shore after deleting `e,f` which

1. induces the selected partition `Pi` on the literal boundary; and
2. makes both marked endpoint pairs monochromatic.

This is the fixed-equality branch of the repeated-exposure theorem, not
mere extension of `Pi`.  If the marked edges are incident, all three of
their vertices receive one colour, so properness of the deletion host
indeed forces the outer edge `wt` to be absent.

After a palette permutation, this colouring glues to the `Pi`-colouring of
the first closed shore, producing on `G-{h,e,f}` the chamber in which
`e,f` are monochromatic and `h` is proper.  Independently, a colouring of
the proper minor `G/h`, expanded and then restricted after deleting `e,f`,
produces the chamber in which `h` is monochromatic and `e,f` are proper.
Its restriction to the unchanged opposite closed shore is proper.

If that second chamber induced `Pi` on the boundary, a palette permutation
would align it with the original `Pi`-colouring of the first shore and the
two colourings would glue to a six-colouring of `G`.  Its boundary
partition is therefore different, proving the stated cross-shore drift.

## 7. Mixed-response lift

For the order-five separation of `G-{h,e}`, orient the crossing edges as
`a,c in L` and `b,d in R`.  Because `f` remains an edge of that graph, it
cannot join `L-T` to `R-T`.

If `f` meets `L-T`, the lifted boundary `T union {a,d}` puts `e,f` only in
the left closed shore and `h` only in the right closed shore.  Thus the
fixed-equality chamber is proper on the right and the `h`-contraction
chamber is proper on the left.  The symmetric endpoint choice handles an
`f` meeting `R-T`.  If the two legal boundary partitions agreed after a
palette permutation, those two proper restrictions would glue and
six-colour `G`.  Their partition families are therefore disjoint.  If both
ends of `f` lie in `T`, the fixed-equality chamber gives them the same
colour on every lifted boundary and hence supplies no legal boundary
partition there.

This verifies Proposition 5.1, including every placement of `f`.  It also
justifies the source's sharper trust boundary: endpoint orientation creates
opposite legal responses, not a common trace, and the old partition is not
literally a partition of the new boundary.

## 8. Trust boundary

The conclusions are exactly those stated in the source:

* a rooted `K_4` in the deletion host may use vertices of the three named
  branch sets needed to complete a `K_7` model;
* an exact order-seven lift preserves arbitrary endpoint-side choices but
  does not automatically preserve five branch-set labels or reflect either
  transported boundary partition through the opposite shore; and
* the fixed-trace comparison proves that the two proper-minor responses
  differ, not that either one is reflected through the opposite shore.

Thus the theorem gives genuine host geometry for the cross-shore response
but does not prove the remaining label-preserving absorption or colouring
step, and it does not prove `HC_7`.
