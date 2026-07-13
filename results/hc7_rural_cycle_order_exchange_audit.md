# Independent audit: rural cycle-order exchange

## Overall verdict: **GREEN**

Lemma 1 is correct, the contracted cycle argument in Theorem 2 lifts to a
literal `S`-rooted `K_4` subdivision, and Corollary 3's pointwise row-contact
hypothesis is sufficient for a literal `K_7` minor model.  No HC7 conclusion
follows without the stated two-connectivity, shore-disjointness, and
pointwise-contact assumptions.

The only recommended change is expository: Corollary 3 should explicitly
construct the four rooted minor branch sets from the subdivision rather than
refer to “the four branch sets” as though a subdivision came with a canonical
minor model.

## Lemma 1 (second Hamiltonian order): **GREEN**

Put `S` in the `C` order on a strictly convex circle.  If a Hamiltonian cycle
`D` uses a diagonal `uv`, that diagonal separates the other boundary points
into the two open `u-v` arcs.  The complementary `u-v` path in `D` visits
vertices on both sides, so some edge of that path crosses `uv`.  The crossing
edge is independent of `uv`, since geometric edges incident with `u` or `v`
meet `uv` only at their common endpoint.  Consequently, a noncrossing
Hamiltonian polygon on a convex point set uses only boundary edges and has
exactly the `C` order or its reversal.

Thus a genuinely different cyclic order supplies independent `D`-edges
`ab,cd` with alternating ends.  In the alternating order, say

\[
                            a,c,b,d,
\]

the four intervening `C` arcs realize the cycle edges

\[
                            ac,cb,bd,da,
\]

and `ab,cd` are its two diagonals.  Their interiors are disjoint, so these
six paths are a subdivision of `K_4` rooted at `a,b,c,d`.

There is no exceptional four-vertex order and no dependence on a geometric
genericity assumption beyond the chosen strictly convex placement.

## Theorem 2 (two-shore rural cycle exchange): **GREEN**

### Boundary cycles

Two-connectivity is used exactly where claimed.  In a two-connected plane
graph every facial boundary walk is a cycle, so the distinguished disk face
contains each member of `S` exactly once.  This gives a well-defined cyclic
order even if additional non-`S` vertices lie on that face.

### Equal-order gluing

When the orders agree up to reversal, reflect one disk and use thin collars
on opposite sides of a Jordan curve through the labelled `S` vertices.  The
between-`S` boundary arcs of the two shores can be drawn in their respective
collars.  The hypotheses

\[
 V(H_1)\cap V(H_2)=S,\qquad E(H_1)\cap E(H_2)=\varnothing
\]

ensure no additional identification or shared edge must be accommodated.
Hence the union is planar.

### Mismatched-order lifting

Contracting every maximal facial-cycle subpath whose internal vertices avoid
`S` turns each `C_i` into a cycle on vertex set `S`.  An edge of the quotient
cycle corresponds before contraction to an `S`-path whose interior avoids
`S`.  Lemma 1 returns independent quotient edges `ab,cd` in the second cycle
whose endpoints alternate in the first.

Lifting gives:

* two internally disjoint `S`-paths `P_{ab},P_{cd}` in `C_2`, with no
  internal `S` vertices; and
* four internally disjoint arcs of `C_1` between consecutive members of
  `{a,b,c,d}`.

Although those four `C_1` arcs may contain other members of `S`, neither
lifted `C_2` path can meet those members internally, because its interior
avoids all of `S`.  The two shores meet nowhere outside `S`, so a `C_1` arc
cannot meet a `C_2` path away from the four selected endpoints.  Therefore
the six lifted paths are literally internally disjoint in the required
pattern.  This is an actual subdivision rooted at four vertices of `S`, not
merely a quotient minor.

Equality versus inequality of the two cyclic orders makes the two order
cases exclusive.  As the note correctly says, the planar equal-order case
may still contain an unrelated `K_4` subdivision.

## Corollary 3 (three-row lift): **GREEN**

Every subdivision of `K_4` rooted at `a,b,c,d` contains a rooted `K_4`
minor model.  For completeness, on each of its six subdivided edge paths,
choose one edge as the cut edge and assign the two remaining path segments
to the branch sets at its two ends.  The union of all segments assigned to
one root is connected through that root; the four resulting branch sets are
pairwise disjoint and pairwise adjacent, and each contains its prescribed
root in `S`.

The pointwise contact assumption now does exactly what is needed.  Since
each of `a,b,c,d` has a neighbour in every `R_j`, each rooted branch set is
adjacent to every `R_j`.  The three `R_j` are connected, disjoint, and
pairwise adjacent by hypothesis, and they are disjoint from both shores.
Thus the four rooted branch sets together with `R_1,R_2,R_3` form seven
literal pairwise adjacent connected branch sets.

It is not enough that each row merely meet the set `S` somewhere; it must
meet every returned rooted branch set, and the pointwise hypothesis ensures
this uniformly before the four roots are known.

## Corollary 4 (sharpness): **GREEN**

The two path shores with boundary orders `1234` and `1324` are connected but
not two-connected.  After suppressing their private subdivision vertices,
their union has edges

\[
 12,23,34,13,23,24,
\]

namely `K_4-14` with `23` doubled.  Its underlying simple graph has
treewidth two and no `K_4` minor.  Hence the closing facial arcs supplied by
two-connectivity are essential.

## Trust boundary

The result closes exactly a two-shore interface in which both shores are
two-connected rural societies with the same literal boundary set, are
otherwise vertex-disjoint, and expose four roots with pointwise contacts to
three fixed rows.  It does not cover a block-cut shore, distributed contacts
inside nonsingleton row bags, or agreement of the two rural orders.  Those
remain separate composition cases.
