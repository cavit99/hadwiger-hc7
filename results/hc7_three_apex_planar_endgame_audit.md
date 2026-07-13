# Independent audit: three-apex planar endgame

## Verdict

**GREEN.**  Uniform Lemma 0 and every specialized deletion-set case are
correct, the palette-recycling colourings are proper on all edges, and
the cited Martinsson--Steiner theorem has exactly the strength used.  In
the uniform lemma every rooted bag has literal contact with all `s` apex
singletons; in the specialized theorem this gives all twelve
apex-to-branch-set adjacencies of the final `K_7` model.

The only suggested edit is typographical: replace the terminal text
`` `square` `` by `\(\square\)`.  No mathematical repair is needed.

## 1. Uniform Lemma 0

Take a subgraph minimal subject to chromatic number at least `r+s`.
Deleting any vertex leaves an `(r+s-1)`-colourable graph, so adding that
vertex back proves that the minimal subgraph has chromatic number exactly
`r+s`.  Intersecting the given deletion set with this subgraph preserves
both the bound `|A|<=s` and `chi(G-A)<=r`.

The source's edge-deletion version is equally valid: for every edge `e`,
minimality gives `chi(G-e)<=r+s-1`, while
`chi(G)<=chi(G-e)+1` (if the ends share a colour, give one end one new
colour).  Thus the current explicit sentence also proves equality.

If `|A|<s`, use at most `r` colours on `G-A` and one new colour on each
vertex of `A`.  This uses at most `r+s-1` colours, a contradiction.
Thus `|A|=s`.  With `H=G-A`, the same disjoint-palette argument shows
`chi(H)=r`: otherwise `r-1` colours on `H` and `s` fresh colours on `A`
would suffice.  It also forces `G[A]=K_s`.  Indeed, any noncomplete graph
on `s` vertices has chromatic number at most `s-1` (give one nonadjacent
pair the same colour), so it and `H` would again use at most `r+s-1`
disjoint colours.

Let

\[
                         X=\bigcap_{a\in A}N_H(a).
\]

Suppose an `r`-colouring of `H` has colour 1 absent from `X`, and let
`Z` be its independent colour-1 class.  For every
`z in Z cap N_H(a_1)`, the fact `z notin X` and `za_1 in E(G)` supplies
an index `j(z) in {2,...,s}` with `za_{j(z)} notin E(G)`.  Recolour `z`
with the new colour `f_{j(z)}`.  All recoloured vertices lie in the
independent set `Z`, so no two conflict; no unrecoloured vertex of `H`
uses a fresh colour.  Give `a_1` colour 1 and give each `a_j`, `j>=2`,
its distinct colour `f_j`.  The clique `A` is proper, every old colour-1
neighbour of `a_1` was recoloured, and every new colour-`f_j` neighbour
candidate was selected nonadjacent to `a_j`.  Hence this is an
`(r+s-1)`-colouring, a contradiction.

The edge case `s=1` is also covered: then `X=N_H(a_1)`, so
`Z cap N_H(a_1)` is empty and no choice of `j(z)` is required.

Thus `X` is colourful.  Strong Hadwiger for `r` returns an `X`-rooted
`K_r` model.  Choose one `X` vertex in every rooted bag.  It is adjacent
to every member of the clique `A`, so the `r` rooted bags and the `s`
apex singletons have all `rs` cross-edges as well as their two internal
clique systems.  They form a literal `K_{r+s}` model.  Lemma 0 is valid
for every positive `r,s` under its stated Strong-Hadwiger hypothesis.

## 2. Reduction to chromatic number seven

If `chi(G)>=7`, take an inclusion-minimal subgraph `H` with
`chi(H)>=7`.  For every vertex `x` of `H`, minimality gives
`chi(H-x)<=6`, and therefore

\[
                     \chi(H)\le \chi(H-x)+1\le7.
\]

Thus `chi(H)=7`.  Replacing `A` by `A cap V(H)` leaves at most three
vertices, and

\[
                         H-(A\cap V(H))
\]

is a subgraph of the planar graph `G-A`.  A `K_7` minor in `H` is one in
`G`.  Hence the opening reduction is valid, including when the critical
subgraph uses fewer than all original apex vertices.

## 3. The cases `|A|<=3`

If `|A|<=2`, four colours properly colour the planar remainder and two
new colours properly colour the vertices of `A` (using distinct new
colours if they are adjacent).  This is a six-colouring.

Now let `|A|=3`.  A noncomplete graph on three vertices is bipartite, so
if `G[A]` is not a triangle, two fresh colours on `A` and four colours
on `P` again give six colours.  Consequently failure of six-colourability
forces `G[A]=K_3`.

If `P` were three-colourable, the triangle could be assigned three
fresh, pairwise distinct colours.  This also uses only six colours.
The Four Colour Theorem gives `chi(P)<=4`, hence in the surviving case

\[
                              \chi(P)=4.
\]

No connectivity of `P` is used or needed.

## 4. Palette recycling

Fix a proper four-colouring `c` of `P` in which colour 1 is absent from

\[
                 T=N_P(a_1)\cap N_P(a_2)\cap N_P(a_3),
\]

and let `Z=c^{-1}(1)`.  The set `Z` is independent.  Recolour precisely
the vertices in `Z cap N_P(a_1)` as follows:

* use colour 5 if the vertex is not adjacent to `a_2`;
* use colour 6 if it is adjacent to `a_2`.

In the second case the vertex is adjacent to `a_1,a_2`.  Since it has
colour 1 and colour 1 is absent from `T`, it is not adjacent to `a_3`.
Thus the stated safety inference is exact.

All edges of `P` remain proper.  Every recoloured vertex belonged to the
independent set `Z`, so there is no edge between two vertices recoloured
5 or 6, including one recoloured 5 and one recoloured 6.  No unrecoloured
vertex of `P` has colour 5 or 6.

Assign

\[
                         c(a_1),c(a_2),c(a_3)=1,5,6.
\]

The three apex edges are proper because these colours are distinct.  For
the apex--remainder edges:

* every old colour-1 neighbour of `a_1` was recoloured;
* every new colour-5 vertex was selected outside `N_P(a_2)`; and
* every new colour-6 vertex was proved outside `N_P(a_3)`.

There are no other vertices of colours 5 or 6 in `P`.  Hence every edge
of `G` is proper, and the construction is a genuine six-colouring.  Its
contradiction proves that every proper four-colouring of `P` uses all
four colours on `T`.

## 5. Exact Martinsson--Steiner input

Martinsson and Steiner, *Strengthening Hadwiger's conjecture for 4- and
5-chromatic graphs*, Theorem 1.3, states:

> If `H` has chromatic number four and `S` is colourful in `H`--that is,
> every proper `chi(H)`-colouring uses all four colours on `S`--then `H`
> contains an `S`-rooted `K_4` minor.

Their definition of `S`-rooted is exactly that every one of the four
branch sets meets `S`.  The theorem does not assume that `H` is
connected, planar, critical, or that `S` consists of four prescribed
vertices.  Thus it applies directly to `H=P` and `S=T`, because the
previous sections prove `chi(P)=4` and colourfulness of `T` in precisely
this sense.

It returns pairwise disjoint, nonempty connected and pairwise adjacent
sets `B_1,...,B_4`, with `B_i cap T` nonempty for each `i`.

## 6. Literal `K_7` branch sets

Choose `t_i in B_i cap T`.  The branch sets lie in `P`, while the three
apex vertices lie in `A`, so

\[
     \{a_1\},\ \{a_2\},\ \{a_3\},\ B_1,B_2,B_3,B_4
\]

are pairwise disjoint and connected.  Their adjacencies are exhaustive:

1. the three singleton apex bags are pairwise adjacent because `G[A]`
   is a triangle;
2. the four `B_i` are pairwise adjacent by the rooted `K_4` model; and
3. for every `j in {1,2,3}` and `i in {1,2,3,4}`, membership
   `t_i in T` gives the actual edge `a_jt_i`.

Item 3 supplies all `3*4=12` cross-adjacencies separately.  It does not
use collective contact of a union of bags or identify a colour with a
branch-set label.  The seven sets therefore form a literal `K_7` minor.

## 7. Consequences and trust boundary

The equivalence with six-colourability of `K_7`-minor-free graphs is
valid by contraposition.  In particular, any hypothetical `HC_7`
counterexample with a planar remainder after deleting at most three
vertices is terminated immediately.  This applies to the three-guard
outcome of the guarded cyclic-shore theorem without any bipartiteness
assumption on the three guards.

The proof depends on the Four Colour Theorem and the proved four-colour
case of Strong Hadwiger.  It makes no claim for four or more apex
vertices and does not supply planarity; it closes the endgame once such
a deletion set has already been produced.
