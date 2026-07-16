# Cold audit of four edge-local double-critical carriers

**Verdict:** **GREEN.**  The ordered-colour path lemma localizes correctly
to one double-critical edge, the three-carrier proposition handles
overlapping terminal sets correctly, and both scoped packaging barriers are
valid.  The package produces three disjoint four-contact carriers, but does
not make them pairwise adjacent or synchronize them with a prescribed
four-linkage.

**Audited SHA-256 values:**

```text
0d95eb6d41d6eac1d8798b18e2f37efb9e551deb7b8515f7717279d5e69a2615  active/hc7_four_edge_double_critical_carriers.md
a593fc245fe394de5b35bb4c4483224e8059f734dd6eaf3d94c556844d831ab9  barriers/hc7_four_edge_double_critical_packaging_barrier.md
6335009d7cfb1e70cf975fbf000b9f2cfa234beb448641aa2179fbfc7df9ae90  /tmp/double_critical.txt
```

The primary comparison is Kawarabayashi--Pedersen--Toft, Proposition 3.3
and Corollary 3.1, as extracted in the last file above.

## 1. Edge-localization of Proposition 3.3

Fix one edge `xy` with

\[
                         \chi(G-x-y)=k-2.
\]

For any proper `(k-2)`-colouring `phi` of `G-x-y`, assigning one new colour
to both `x,y` gives a proper `(k-1)`-colouring of `G-xy`.  For the cyclic
permutation

\[
                         (\mathord\star,j_1,\ldots,j_r),
\]

the generalized Kempe recolouring is proper.  If the chain from `x` omitted
`y`, recolouring it would change the colour of `x` while leaving `y` with
the new colour, so restoring `xy` would `(k-1)`-colour `G`.  This
contradicts `chi(G)=k`.

Once the chain reaches `y`, a shortest colour-respecting walk from `x` to
`y` has exactly one passage through the displayed colour cycle.  An earlier
return to the new colour would have to revisit `x` or reach `y`, since those
are its only two vertices; shortestness excludes the former and terminates
at the latter.  Thus it yields the path

\[
                         x v_1\cdots v_r y,qquad
                         \phi(v_i)=j_i.
\]

This is the source proof of Proposition 3.3.  Its contradiction uses
double-criticality only to obtain the selected colouring of `G-x-y`; it
does not invoke the chromatic drop for any other edge.  Lemma 2.1 is
therefore genuinely edge-local.  The one-colour case gives one common
neighbour in each colour, and different colours give distinct vertices.

## 2. Three outside contacts per cross-edge

For a cross-edge of the literal endpoint `K_4`, the two undeleted endpoint
vertices are adjacent and hence have two distinct colours in every
five-colouring of `G-x-y`.  Applying Lemma 2.1 to the other three colours
gives three common neighbours.  None can be an undeleted endpoint, because
its colour is outside their two colours, and none is `x` or `y`, which are
absent from the colouring.  Hence all three lie in `H=G-C` and are distinct.

The three-colour ordered instance likewise has all three internal vertices
in `H`.  This verifies Lemma 3.1 without assuming that the colourings chosen
for different cross-edges agree.

## 3. Set-Menger with overlapping terminal sets

Deleting the literal four-clique `C` from a seven-connected graph leaves a
three-connected graph `H`: a cut of order at most two in `H` would join `C`
to form a cut of order at most six in `G`.

The two common-neighbour sets `X_ac,X_bd` each have order at least three.
The set form of Menger applies even if they overlap, with a common vertex
allowed as a trivial path.  If three disjoint set-to-set paths did not
exist, a set `Z` of order at most two would leave no path from
`X_ac-Z` to `X_bd-Z`.  Both differences are nonempty.  If they still
intersected, their common vertex would itself be a trivial path; hence they
are disjoint nonempty sets in different components of `H-Z`, contradicting
three-connectivity.

Each resulting path has one end adjacent to `a,c` and the other adjacent
to `b,d`.  A trivial path lies in both common-neighbour sets.  The three
path vertex sets are therefore disjoint connected `C`-full carriers.
Adding pairwise adjacency among them would indeed make the four singleton
vertices of `C` and the three carriers a literal `K_7` model.  No argument
in the source package supplies that extra adjacency.

## 4. Wheel barrier

The six-rim wheel is three-connected: retaining the hub connects the
remainder after two deletions, while deleting it and at most one rim vertex
leaves a connected rim path.  The paths `23`, `50`, and `1h4` are three
disjoint `A-B` paths.

Any connected hub-free subgraph meeting both consecutive rim triples must
use one of the two crossing rim edges `23,50`.  Three disjoint such
subgraphs therefore require exactly one to contain the hub and the other
two to use different crossing edges.  Those two occupy `2,3` and `5,0`.
The hub-containing subgraph must then use the only remaining vertices `1`
and `4` to meet both terminal triples.  The two hub-free subgraphs are
confined to `\{2,3\}` and `\{5,0\}`, between which there is no edge.  They
cannot be pairwise adjacent.  Proposition 1.1 is correct.

## 5. Four-gate barrier

In the graph `J`, the four-set `S` separates the two four-cliques and `v`,
so connectivity is at most four.  After at most three deletions, a vertex
of `S` remains and at least one vertex of `L union R union {v}` remains;
their complete incidence, together with the two literal cliques, connects
every surviving vertex.  Thus `J` is four-connected.

Every `L-R` path uses `S`.  Four disjoint such paths use all four vertices
of `S`, exactly one per path.  A path containing `v` would enter and leave
it through two distinct vertices of `S`, leaving at most two `S`-vertices
for the other three paths, which is impossible.  Hence every four-linkage
avoids `v` and uses one gate per path.  Four-connectivity excludes a cut of
order at most three.  Proposition 2.1 and both stated consequences are
correct.

## 6. Trust boundary

Promoted here:

* the selected-edge ordered-colour path lemma;
* three disjoint connected carriers with all four endpoint contacts; and
* the two scoped counterexamples to connectivity-only packaging.

Not promoted here:

* pairwise adjacency of the three carriers;
* a carrier packing synchronized across different five-colourings;
* insertion of two common-contact vertices into one member of a prescribed
  four-linkage; or
* the exact-two branch, support-six theorem, or `HC_7`.
